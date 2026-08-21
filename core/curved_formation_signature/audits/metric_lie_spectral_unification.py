#!/usr/bin/env python3
"""Adversarial finite-Galerkin audit linking the metric-Lie/Hodge formation core
and the mother / shifted spectral-signature core.

The two implementations are kept separate on purpose:
  * physical path: sampled divergence-free Fourier fields and differential calculus;
  * core path: only the metric structure tensor T and the curl matrix C.

This is a canonical executable audit for the curved formation-signature core; it is not by itself a continuum theorem.
"""
from __future__ import annotations

import math
import numpy as np

N = 16
NU = 0.137
RNG = np.random.default_rng(20260821)
KS = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1),
]

x = 2 * np.pi * np.arange(N) / N
X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
XYZ = (X, Y, Z)
NPTS = N ** 3


def inner_field(a, b):
    return float(np.mean(np.sum(a * b, axis=-1)))


def norm_field(a):
    return math.sqrt(max(inner_field(a, a), 0.0))


def transverse_frame(k):
    k = np.array(k, dtype=float)
    kh = k / np.linalg.norm(k)
    ref = np.array([0.0, 0.0, 1.0])
    if abs(float(np.dot(kh, ref))) > 0.85:
        ref = np.array([0.0, 1.0, 0.0])
    p1 = ref - np.dot(ref, kh) * kh
    p1 /= np.linalg.norm(p1)
    p2 = np.cross(kh, p1)
    p2 /= np.linalg.norm(p2)
    return p1, p2


def build_basis(include_constants=False):
    fields = []
    labels = []
    if include_constants:
        for j in range(3):
            v = np.zeros((N, N, N, 3))
            v[..., j] = 1.0
            fields.append(v)
            labels.append(("const", j))
    for k in KS:
        phase = k[0] * X + k[1] * Y + k[2] * Z
        p1, p2 = transverse_frame(k)
        for pidx, p in enumerate((p1, p2)):
            for trig, f in (("cos", np.cos(phase)), ("sin", np.sin(phase))):
                v = np.sqrt(2.0) * f[..., None] * p
                fields.append(v)
                labels.append((k, pidx, trig))
    B = np.stack(fields, axis=0)
    return B, labels


def coeffs(B, field):
    # B is orthonormal for the mean L2 inner product.
    return np.einsum("dxyzc,xyzc->d", B, field) / NPTS


def combine(B, c):
    return np.einsum("d,dxyzc->xyzc", c, B)


def spectral_grids():
    kk = np.fft.fftfreq(N, d=1.0 / N)
    return np.meshgrid(kk, kk, kk, indexing="ij")

KX, KY, KZ = spectral_grids()
KGRID = (KX, KY, KZ)
K2 = KX * KX + KY * KY + KZ * KZ


def fft(v):
    return np.fft.fftn(v, axes=(0, 1, 2))


def ifft(vh):
    return np.fft.ifftn(vh, axes=(0, 1, 2)).real


def deriv(v, axis):
    return ifft((1j * KGRID[axis])[..., None] * fft(v))


def grad(v):
    return np.stack([deriv(v, j) for j in range(3)], axis=-1)


def curl(v):
    dv = [deriv(v, j) for j in range(3)]
    out = np.empty_like(v)
    out[..., 0] = dv[1][..., 2] - dv[2][..., 1]
    out[..., 1] = dv[2][..., 0] - dv[0][..., 2]
    out[..., 2] = dv[0][..., 1] - dv[1][..., 0]
    return out


def lap(v):
    return ifft((-K2)[..., None] * fft(v))


def advect(a, b):
    gb = grad(b)
    return np.einsum("...j,...ij->...i", a, gb)


def scaled(a, b, floor=1e-30):
    a = np.asarray(a)
    b = np.asarray(b)
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(a), np.linalg.norm(b), floor))


def build_physical_tensors(include_constants=False):
    B, labels = build_basis(include_constants)
    d = len(B)
    gram = np.einsum("axyzc,bxyzc->ab", B, B) / NPTS

    grads = [grad(B[j]) for j in range(d)]
    curls = [curl(B[j]) for j in range(d)]
    laps = [lap(B[j]) for j in range(d)]

    C = np.column_stack([coeffs(B, curls[j]) for j in range(d)])
    Lphys = np.column_stack([coeffs(B, laps[j]) for j in range(d)])
    curl_closure = max(norm_field(curls[j] - combine(B, C[:, j])) for j in range(d))

    # Direct projected material connection coefficients:
    # A[k,a,b] = <e_k, (e_a . grad)e_b>.  Since e_k is divergence-free,
    # this equals <e_k, P((e_a.grad)e_b)>.
    A = np.zeros((d, d, d))
    for a in range(d):
        ea = B[a]
        for b in range(d):
            raw = np.einsum("...j,...ij->...i", ea, grads[b])
            A[:, a, b] = coeffs(B, raw)

    # T[i,j,k] = <e_i, [e_j,e_k]>.
    T = A - np.swapaxes(A, 1, 2)

    # Koszul reconstruction from T alone.
    Gamma = np.zeros_like(A)
    for k in range(d):
        for a in range(d):
            for b in range(d):
                Gamma[k, a, b] = 0.5 * (T[k, a, b] - T[a, b, k] + T[b, k, a])

    return {
        "B": B, "labels": labels, "gram": gram, "C": C,
        "Lap": Lphys, "Aphys": A, "T": T, "Gamma": Gamma,
        "curl_closure": curl_closure,
    }


def conn_matrix(Gamma, v):
    # output k, input b
    return np.einsum("a,kab->kb", v, Gamma)


def bracket_coeff(T, a, b):
    return np.einsum("ijk,j,k->i", T, a, b)


def J_from_T(T, u):
    # <e_a,J_u e_b> = -<u,[e_a,e_b]>
    return -np.einsum("i,iab->ab", u, T)


def physical_J(data, u):
    B = data["B"]
    uf = combine(B, u)
    omega = curl(uf)
    d = len(B)
    out = np.zeros((d, d))
    for b in range(d):
        out[:, b] = coeffs(B, np.cross(B[b], omega))
    return out


def mother_tensor(Gamma, C):
    d = C.shape[0]
    cols = []
    Es = []
    for j in range(d):
        e = np.zeros(d); e[j] = 1.0
        D = conn_matrix(Gamma, e)
        E = D @ C - C @ D
        Es.append(E)
        cols.append(E.reshape(-1))
    return np.column_stack(cols), Es


def unique_eigs(C, tol=1e-9):
    vals = np.linalg.eigvalsh(0.5 * (C + C.T))
    out = []
    for v in vals:
        if not out or abs(v - out[-1]) > tol:
            out.append(float(v))
    return np.array(out)


def sign_cut(C, a):
    vals, vecs = np.linalg.eigh(0.5 * (C + C.T))
    s = np.sign(vals - a)
    if np.any(s == 0):
        raise RuntimeError("cut hit eigenvalue")
    return (vecs * s) @ vecs.T


def shifted_signature_map(Gamma, C):
    d = C.shape[0]
    roots = unique_eigs(C)
    cuts = [(float((l+r)/2), float(r-l)) for l, r in zip(roots[:-1], roots[1:])]
    blocks = []
    O_by_cut = []
    for a, width in cuts:
        H = sign_cut(C, a)
        cut_cols = []
        Os = []
        for j in range(d):
            v = np.zeros(d); v[j] = 1.0
            Dv = conn_matrix(Gamma, v)
            Av = Dv @ H - H @ Dv
            Hv = H @ v
            DHv = conn_matrix(Gamma, Hv)
            AHv = DHv @ H - H @ DHv
            O = H @ Av - AHv
            Os.append(O)
            cut_cols.append(O.reshape(-1))
        blocks.append(np.column_stack(cut_cols))
        O_by_cut.append((H, width, Os))
    return np.vstack(blocks), O_by_cut, roots


def layer_cake_from_O(v, O_by_cut):
    d = len(v)
    E = np.zeros((d, d))
    for H, width, Os in O_by_cut:
        O = sum(v[j] * Os[j] for j in range(d))
        skew = 0.5 * (O - O.T)
        Arec = H @ skew
        E += 0.5 * width * Arec
    return E


def reduced_coordinate_map(A, tol=1e-10):
    U, s, Vh = np.linalg.svd(A, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) and s[0] else 0
    Uq = U[:, :rank]
    M = Uq.T @ A
    return M, Uq, s, rank


def transported_structures(T, C, M):
    R = np.linalg.inv(M)
    G = R.T @ R
    # Tz[p,q,r] = <e_p,[e_q,e_r]>_G after coordinate transport z=M u.
    Tz = np.einsum("ip,jq,kr,ijk->pqr", R, R, R, T)
    Cz = M @ C @ R
    return R, G, Tz, Cz


def formation_from_structures(z, G, Tz, Cz, nu=NU):
    covJ = -np.einsum("i,iab->ab", z, Tz)
    Jz = np.linalg.solve(G, covJ)
    heat_cov = Cz.T @ G @ Cz
    Hz = np.linalg.solve(G, heat_cov)
    return Jz - nu * Hz, Jz, Hz


def rk4_step(f, y, h):
    k1 = f(y)
    k2 = f(y + 0.5*h*k1)
    k3 = f(y + 0.5*h*k2)
    k4 = f(y + h*k3)
    return y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)


def run_mean_zero_audit():
    data = build_physical_tensors(False)
    B, T, C, Gamma = data["B"], data["T"], data["C"], data["Gamma"]
    d = len(B)

    results = {}
    results["basis_orthonormal"] = scaled(data["gram"], np.eye(d))
    results["curl_self_adjoint"] = scaled(C, C.T)
    results["curl_closure"] = data["curl_closure"]
    results["c2_laplacian"] = scaled(C @ C, -data["Lap"])
    results["koszul_from_T"] = scaled(Gamma, data["Aphys"])

    # Core-only Poisson reconstruction against an independent physical b x omega implementation.
    u = RNG.normal(size=d)
    u /= np.linalg.norm(u)
    Jcore = J_from_T(T, u)
    Jphys = physical_J(data, u)
    results["poisson_from_T"] = scaled(Jcore, Jphys)

    # Mother map from core and direct physical connection.
    AE, Es = mother_tensor(Gamma, C)
    Ecore = sum(u[j] * Es[j] for j in range(d))
    Dphys = np.einsum("a,kab->kb", u, data["Aphys"])
    Ephys = Dphys @ C - C @ Dphys
    results["core_to_mother"] = scaled(Ecore, Ephys)

    AO, O_by_cut, roots = shifted_signature_map(Gamma, C)
    Elayer = layer_cake_from_O(u, O_by_cut)
    results["flag_to_mother_layercake"] = scaled(Ecore, Elayer)

    ME, UE, sE, rE = reduced_coordinate_map(AE)
    MO, UO, sO, rO = reduced_coordinate_map(AO)
    results["mother_rank"] = (rE, d)
    results["flag_rank"] = (rO, d)
    results["mother_cond"] = float(sE[0] / sE[d-1]) if rE == d else np.inf
    results["flag_cond"] = float(sO[0] / sO[d-1]) if rO == d else np.inf
    if rE != d or rO != d:
        return results

    # Reverse: mother/flag -> state -> state-dependent formation operator.
    uE = np.linalg.solve(ME, ME @ u)
    uO = np.linalg.solve(MO, MO @ u)
    results["mother_state_decode"] = scaled(uE, u)
    results["flag_state_decode"] = scaled(uO, u)
    LE = J_from_T(T, uE) - NU * (C @ C)
    LO = J_from_T(T, uO) - NU * (C @ C)
    L0 = Jcore - NU * (C @ C)
    results["mother_to_formation_operator"] = scaled(LE, L0)
    results["flag_to_formation_operator"] = scaled(LO, L0)

    # Direct linear functor E -> Poisson tensor, learned once from basis images.
    AJ = np.column_stack([J_from_T(T, np.eye(d)[j]).reshape(-1) for j in range(d)])
    R_EJ = AJ @ np.linalg.pinv(AE)
    J_from_E = (R_EJ @ (AE @ u)).reshape(d, d)
    results["linear_functor_E_to_J"] = scaled(J_from_E, Jcore)

    # Transport the *entire* formation core to mother-image and flag-image coordinates.
    for tag, M in (("mother", ME), ("flag", MO)):
        R, G, Tz, Cz = transported_structures(T, C, M)
        z = M @ u
        Lz, Jz, Hz = formation_from_structures(z, G, Tz, Cz)
        conj = M @ L0 @ R
        results[f"{tag}_formation_conjugacy"] = scaled(Lz, conj)
        results[f"{tag}_curl_selfadjoint_in_metric"] = scaled(Cz.T @ G, G @ Cz)
        results[f"{tag}_heat_conjugacy"] = scaled(Hz, M @ (C @ C) @ R)
        results[f"{tag}_induced_metric_condition"] = float(np.linalg.cond(G))
        # Negative control: pretending signature coordinates carry the identity Riesz metric.
        covJ_naive = -np.einsum("i,iab->ab", z, Tz)
        L_naive = covJ_naive - NU * (Cz.T @ Cz)
        results[f"{tag}_identity_metric_failure"] = scaled(L_naive, conj)

        # Dynamic commuting diagram: integrate full state and transported signature flow separately.
        def fu(v):
            return (J_from_T(T, v) - NU * (C @ C)) @ v

        def fz(zz):
            LL, _, _ = formation_from_structures(zz, G, Tz, Cz)
            return LL @ zz

        uu = u.copy(); zz = z.copy()
        h = 2e-3
        for _ in range(60):
            uu = rk4_step(fu, uu, h)
            zz = rk4_step(fz, zz, h)
        results[f"{tag}_trajectory_commutes"] = scaled(zz, M @ uu)

    # Direct mother <-> flag reduced coordinate map should be invertible.
    C_EO = MO @ np.linalg.inv(ME)
    C_OE = ME @ np.linalg.inv(MO)
    results["mother_flag_chart_inverse"] = scaled(C_OE @ C_EO, np.eye(d))

    # The mother and shifted flag are not only mutually invertible; their induced
    # metrics/curl operators are the same structure in different charts.
    RE, GE, TE, CE = transported_structures(T, C, ME)
    RO, GO, TO, CO = transported_structures(T, C, MO)
    results["mother_flag_metric_isometry"] = scaled(C_EO.T @ GO @ C_EO, GE)
    results["mother_flag_curl_conjugacy"] = scaled(C_EO @ CE, CO @ C_EO)

    # Formation-form invariance under both state-to-signature coordinate maps.
    aa = RNG.normal(size=d); bb = RNG.normal(size=d)
    ell_u = -float(u @ bracket_coeff(T, aa, bb)) - NU * float((C @ aa) @ (C @ bb))
    for tag, M, G, Tz, Cz in (("mother", ME, GE, TE, CE), ("flag", MO, GO, TO, CO)):
        za, zb, zu = M @ aa, M @ bb, M @ u
        bracket_cov = np.einsum("ijk,j,k->i", Tz, za, zb)
        brz = np.linalg.solve(G, bracket_cov)
        ell_z = -float(zu @ (G @ brz)) - NU * float((Cz @ za) @ (G @ (Cz @ zb)))
        results[f"{tag}_formation_form_invariant"] = abs(ell_z-ell_u)/max(abs(ell_u),abs(ell_z),1.0)

    # Arbitrary orthogonal basis changes must leave the core->mother construction tensorial.
    ortho_worst = 0.0
    for _ in range(5):
        Qm, _ = np.linalg.qr(RNG.normal(size=(d,d)))
        Tp = np.einsum("ia,jb,kc,ijk->abc", Qm, Qm, Qm, T, optimize=True)
        Cp = Qm.T @ C @ Qm
        # Koszul in the mixed basis.
        Gp = np.zeros_like(Tp)
        for k in range(d):
            for a in range(d):
                for b in range(d):
                    Gp[k,a,b] = 0.5*(Tp[k,a,b]-Tp[a,b,k]+Tp[b,k,a])
        up = Qm.T @ u
        Ep = conn_matrix(Gp, up) @ Cp - Cp @ conn_matrix(Gp, up)
        ortho_worst = max(ortho_worst, scaled(Ep, Qm.T @ Ecore @ Qm))
    results["orthogonal_basis_covariance"] = ortho_worst

    results["roots"] = roots
    return results


def run_galilean_kernel_audit():
    data = build_physical_tensors(True)
    T, C, Gamma = data["T"], data["C"], data["Gamma"]
    d = C.shape[0]
    AE, _ = mother_tensor(Gamma, C)
    AO, _, _ = shifted_signature_map(Gamma, C)
    sE = np.linalg.svd(AE, compute_uv=False)
    sO = np.linalg.svd(AO, compute_uv=False)
    tolE = 1e-10 * sE[0]
    tolO = 1e-10 * sO[0]
    rankE = int(np.sum(sE > tolE))
    rankO = int(np.sum(sO > tolO))

    u = RNG.normal(size=d); u[:3] = 0.0
    c = np.zeros(d); c[:3] = RNG.normal(size=3)
    # E and O should forget exactly the constant/Galilean sector.
    e_same = scaled(AE @ (u + c), AE @ u)
    o_same = scaled(AO @ (u + c), AO @ u)
    # Formation operator depends only on curl/vorticity, hence also invariant.
    Lu = J_from_T(T, u) - NU * C @ C
    Luc = J_from_T(T, u + c) - NU * C @ C
    lop_same = scaled(Luc, Lu)
    # But diagonal vector field changes by the same operator acting on the frame shift.
    Fu = Lu @ u
    Fuc = Luc @ (u + c)
    boost_law = scaled(Fuc - Fu, Lu @ c)
    return {
        "dim": d,
        "mother_rank": rankE,
        "flag_rank": rankO,
        "expected_rank": d - 3,
        "mother_boost_invariant": e_same,
        "flag_boost_invariant": o_same,
        "formation_operator_boost_invariant": lop_same,
        "diagonal_galilean_covariance": boost_law,
        "mother_tail_singulars": sE[-5:],
        "flag_tail_singulars": sO[-5:],
    }


def run_single_state_nonidentifiability():
    """Negative control: a single signature state cannot identify the universal T.

    This deliberately works at abstract metric-Lie tensor level.  It is not a second
    fluid model.  It shows why the correct unification statement must be fiberwise
    over a fixed formation core rather than `signature(u) determines T`.
    """
    d = 7
    C = np.diag(np.array([-3.0,-2.0,-1.0,0.5,1.0,2.0,4.0]))
    u = np.zeros(d); u[0] = 1.0

    # Core A: abelian.
    T0 = np.zeros((d,d,d))
    # Core B: e0 remains central, while e1,e2,e3 carry an so(3) bracket.
    T1 = np.zeros_like(T0)
    triples = [(1,2,3),(2,3,1),(3,1,2)]
    for out,a,b in triples:
        T1[out,a,b] = 1.0
        T1[out,b,a] = -1.0

    def gamma(T):
        G = np.zeros_like(T)
        for k in range(d):
            for a in range(d):
                for b in range(d):
                    G[k,a,b]=0.5*(T[k,a,b]-T[a,b,k]+T[b,k,a])
        return G
    G0,G1=gamma(T0),gamma(T1)
    E0=conn_matrix(G0,u)@C-C@conn_matrix(G0,u)
    E1=conn_matrix(G1,u)@C-C@conn_matrix(G1,u)
    # Same state signature, distinct global formation tensor and distinct response elsewhere.
    v=np.zeros(d); v[1]=1.0; v[2]=0.7
    J0=J_from_T(T0,v); J1=J_from_T(T1,v)
    return {
        "same_single_state_mother": scaled(E0,E1),
        "tensor_difference_norm": float(np.linalg.norm(T1-T0)),
        "other_state_poisson_difference": float(np.linalg.norm(J1-J0)),
    }


def main():
    mean = run_mean_zero_audit()
    print("=== mean-zero unification tribunal ===")
    for k, v in mean.items():
        if k == "roots":
            print(f"{k:40s} {np.array2string(v, precision=6)}")
        elif isinstance(v, tuple):
            print(f"{k:40s} {v[0]}/{v[1]}")
        elif isinstance(v, (float, np.floating)):
            print(f"{k:40s} {v:.3e}")
        else:
            print(f"{k:40s} {v}")

    gal = run_galilean_kernel_audit()
    print("\n=== Galilean-kernel tribunal ===")
    for k, v in gal.items():
        if isinstance(v, np.ndarray):
            print(f"{k:40s} {np.array2string(v, precision=3)}")
        elif isinstance(v, (float, np.floating)):
            print(f"{k:40s} {v:.3e}")
        else:
            print(f"{k:40s} {v}")

    neg = run_single_state_nonidentifiability()
    print("\n=== single-state non-identifiability negative control ===")
    for k,v in neg.items():
        print(f"{k:40s} {v:.3e}")

    # Hard gates.
    assert mean["mother_rank"] == mean["flag_rank"]
    assert mean["mother_rank"][0] == mean["mother_rank"][1]
    numerical_keys = [k for k,v in mean.items() if isinstance(v,(float,np.floating)) and "cond" not in k and "failure" not in k]
    worst = max(mean[k] for k in numerical_keys)
    gworst = max(gal[k] for k in (
        "mother_boost_invariant", "flag_boost_invariant",
        "formation_operator_boost_invariant", "diagonal_galilean_covariance"))
    assert gal["mother_rank"] == gal["expected_rank"]
    assert gal["flag_rank"] == gal["expected_rank"]
    assert mean["mother_identity_metric_failure"] > 1e-2
    assert mean["flag_identity_metric_failure"] > 1e-2
    assert neg["same_single_state_mother"] < 1e-12
    assert neg["tensor_difference_norm"] > 1.0 and neg["other_state_poisson_difference"] > 0.1
    if worst > 2e-9 or gworst > 2e-9:
        raise SystemExit(f"FAIL worst={worst:.3e} gal={gworst:.3e}")
    print(f"\nPASS unification: worst mean-zero residual={worst:.3e}, Galilean residual={gworst:.3e}")

if __name__ == "__main__":
    main()
