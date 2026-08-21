"""Portable audit for curl spectral-flag completeness.

This file checks the algebraic/microlocal core of
research/NEO_CURL_SPECTRAL_SIGNATURE_COMPLETENESS.md.

It intentionally does not attempt to reproduce every large discovery experiment.
The portable checks are:

1. principal symbol of the mother commutator reads n^T S n;
2. six fixed directions reconstruct every symmetric trace-free strain;
3. periodic strain reconstructs the velocity through Delta u = 2 div S;
4. the Killing kernel contains only Euclidean rigid motions in exact polynomial tests;
5. every nonzero periodic Fourier mode is excluded from the Killing kernel;
6. actual high-frequency mother probes give a convergent six-direction state parametrix;
7. the reconstruction is covariant under integer NS scaling on the torus;
8. the spherical principal-symbol metric equals the predicted strain/enstrophy mass.

No regularity theorem is asserted here.
"""

from __future__ import annotations

import itertools
import math
from typing import Iterable

import numpy as np
import sympy as sp

RNG = np.random.default_rng(20260821)
TOL = 2e-10


def relerr(a: np.ndarray, b: np.ndarray) -> float:
    den = max(1e-14, float(np.linalg.norm(a)), float(np.linalg.norm(b)))
    return float(np.linalg.norm(a - b) / den)


def leray_vector(v: np.ndarray, xi: np.ndarray) -> np.ndarray:
    xi = np.asarray(xi, dtype=float)
    return v - xi * (np.dot(xi, v) / np.dot(xi, xi))


def mother_symbol_direct(G: np.ndarray, xi: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Principal symbol from -P sum_j grad(u_j) x partial_j v."""
    raw = -1j * np.cross(G.T @ xi, b)
    return leray_vector(raw, xi)


def mother_symbol_strain(G: np.ndarray, xi: np.ndarray, b: np.ndarray) -> np.ndarray:
    S = 0.5 * (G + G.T)
    q = float(xi @ S @ xi / (xi @ xi))
    return -1j * q * np.cross(xi, b)


def random_tracefree_gradient() -> np.ndarray:
    G = RNG.normal(size=(3, 3))
    G -= np.eye(3) * np.trace(G) / 3.0
    return G


def audit_principal_symbol(trials: int = 3000) -> None:
    worst = 0.0
    for _ in range(trials):
        G = random_tracefree_gradient()
        xi = RNG.normal(size=3)
        while np.linalg.norm(xi) < 0.2:
            xi = RNG.normal(size=3)
        b = RNG.normal(size=3)
        b = leray_vector(b, xi)
        if np.linalg.norm(b) < 1e-8:
            continue
        b /= np.linalg.norm(b)
        lhs = mother_symbol_direct(G, xi, b)
        rhs = mother_symbol_strain(G, xi, b)
        worst = max(worst, relerr(lhs, rhs))
    assert worst < TOL
    print(f"PASS principal mother symbol: max relerr {worst:.3e}")


STRAIN_BASIS = np.array(
    [
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[1, 0, 0], [0, 0, 0], [0, 0, -1]],
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    ],
    dtype=float,
)

DIRECTIONS = np.array(
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    dtype=float,
)
DIRECTIONS /= np.linalg.norm(DIRECTIONS, axis=1, keepdims=True)
QMAT = np.array([[n @ B @ n for B in STRAIN_BASIS] for n in DIRECTIONS])
QPINV = np.linalg.pinv(QMAT)


def strain_from_coeff(c: np.ndarray) -> np.ndarray:
    return np.tensordot(c, STRAIN_BASIS, axes=(0, 0))


def recover_strain_from_q(q: np.ndarray) -> np.ndarray:
    return strain_from_coeff(QPINV @ q)


def audit_six_direction_strain(trials: int = 3000) -> None:
    rank = int(np.linalg.matrix_rank(QMAT))
    cond = float(np.linalg.cond(QMAT))
    assert rank == 5
    worst = 0.0
    for _ in range(trials):
        c = RNG.normal(size=5)
        S = strain_from_coeff(c)
        q = np.array([n @ S @ n for n in DIRECTIONS])
        Srec = recover_strain_from_q(q)
        worst = max(worst, relerr(S, Srec))
    assert worst < TOL
    print(f"PASS six-direction strain inverse: rank={rank}, cond={cond:.6f}, max relerr={worst:.3e}")


def fft_wavenumbers(N: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    k = np.fft.fftfreq(N) * N
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    k2 = kx * kx + ky * ky + kz * kz
    return kx, ky, kz, k2


def leray_hat(vh: np.ndarray) -> np.ndarray:
    N = vh.shape[0]
    kx, ky, kz, k2 = fft_wavenumbers(N)
    out = vh.copy()
    dot = kx * out[..., 0] + ky * out[..., 1] + kz * out[..., 2]
    nz = k2 > 0
    out[..., 0][nz] -= kx[nz] * dot[nz] / k2[nz]
    out[..., 1][nz] -= ky[nz] * dot[nz] / k2[nz]
    out[..., 2][nz] -= kz[nz] * dot[nz] / k2[nz]
    return out


def random_divfree_field(N: int, bandwidth: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(N, N, N, 3))
    xh = np.fft.fftn(x, axes=(0, 1, 2))
    kx, ky, kz, _ = fft_wavenumbers(N)
    mask = (np.abs(kx) <= bandwidth) & (np.abs(ky) <= bandwidth) & (np.abs(kz) <= bandwidth)
    xh *= mask[..., None]
    xh[0, 0, 0] = 0
    xh = leray_hat(xh)
    return np.fft.ifftn(xh, axes=(0, 1, 2)).real


def gradient_field(u: np.ndarray) -> np.ndarray:
    N = u.shape[0]
    uh = np.fft.fftn(u, axes=(0, 1, 2))
    kx, ky, kz, _ = fft_wavenumbers(N)
    ks = [kx, ky, kz]
    G = np.empty(u.shape[:3] + (3, 3), dtype=float)
    for i in range(3):
        for j in range(3):
            G[..., i, j] = np.fft.ifftn(1j * ks[j] * uh[..., i], axes=(0, 1, 2)).real
    return G


def strain_field(u: np.ndarray) -> np.ndarray:
    G = gradient_field(u)
    return 0.5 * (G + np.swapaxes(G, -1, -2))


def reconstruct_strain_field_from_directions(S: np.ndarray) -> np.ndarray:
    shape = S.shape[:3]
    q = np.empty(shape + (len(DIRECTIONS),), dtype=float)
    for j, n in enumerate(DIRECTIONS):
        q[..., j] = np.einsum("...ij,i,j->...", S, n, n)
    coeff = np.einsum("ab,...b->...a", QPINV, q)
    return np.einsum("...a,aij->...ij", coeff, STRAIN_BASIS)


def velocity_from_strain(S: np.ndarray) -> np.ndarray:
    N = S.shape[0]
    Sh = np.fft.fftn(S, axes=(0, 1, 2))
    kx, ky, kz, k2 = fft_wavenumbers(N)
    ks = [kx, ky, kz]
    divSh = np.zeros(S.shape[:3] + (3,), dtype=complex)
    for i in range(3):
        for j in range(3):
            divSh[..., i] += 1j * ks[j] * Sh[..., i, j]
    uh = np.zeros_like(divSh)
    nz = k2 > 0
    for i in range(3):
        uh[..., i][nz] = -2.0 * divSh[..., i][nz] / k2[nz]
    uh[0, 0, 0] = 0
    return np.fft.ifftn(uh, axes=(0, 1, 2)).real


def audit_periodic_field_inverse(trials: int = 5, N: int = 16) -> None:
    worst_S = 0.0
    worst_u = 0.0
    for t in range(trials):
        u = random_divfree_field(N, bandwidth=2, seed=100 + t)
        S = strain_field(u)
        Srec = reconstruct_strain_field_from_directions(S)
        urec = velocity_from_strain(Srec)
        worst_S = max(worst_S, relerr(S, Srec))
        worst_u = max(worst_u, relerr(u, urec))
    assert worst_S < 2e-9
    assert worst_u < 2e-9
    print(f"PASS periodic S->u inverse: max strain relerr={worst_S:.3e}, velocity relerr={worst_u:.3e}")


def monomials_upto(degree: int) -> list[tuple[int, int, int]]:
    out = []
    for total in range(degree + 1):
        for a in range(total + 1):
            for b in range(total - a + 1):
                c = total - a - b
                out.append((a, b, c))
    return out


def derivative_monomial(m: tuple[int, int, int], j: int):
    m = list(m)
    if m[j] == 0:
        return None
    coef = m[j]
    m[j] -= 1
    return coef, tuple(m)


def killing_matrix_exact(degree: int) -> sp.Matrix:
    mons = monomials_upto(degree)
    index = {(comp, mon): i for i, (comp, mon) in enumerate(itertools.product(range(3), mons))}
    row_keys = []
    for i in range(3):
        for j in range(i, 3):
            for mon in monomials_upto(max(0, degree - 1)):
                row_keys.append((i, j, mon))
    ridx = {key: r for r, key in enumerate(row_keys)}
    A = sp.zeros(len(row_keys), 3 * len(mons))
    for comp in range(3):
        for mon in mons:
            col = index[(comp, mon)]
            for i in range(3):
                for j in range(i, 3):
                    # Equation: partial_i u_j + partial_j u_i = 0.
                    if comp == j:
                        d = derivative_monomial(mon, i)
                        if d is not None:
                            coef, mout = d
                            A[ridx[(i, j, mout)], col] += coef
                    if comp == i:
                        d = derivative_monomial(mon, j)
                        if d is not None:
                            coef, mout = d
                            A[ridx[(i, j, mout)], col] += coef
    return A


def audit_exact_killing_kernel(max_degree: int = 5) -> None:
    results = []
    for d in range(max_degree + 1):
        A = killing_matrix_exact(d)
        nullity = A.cols - A.rank()
        expected = 3 if d == 0 else 6
        assert nullity == expected
        results.append((d, A.cols, A.rank(), nullity))
    print("PASS exact polynomial Killing kernel:", results)

    # Exact single Fourier mode algebra.  For a nonzero k, sym(k \otimes a)=0 has only a=0.
    for k in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, -1, 3), (5, 2, -4)]:
        kvec = sp.Matrix(k)
        cols = []
        for m in range(3):
            e = sp.eye(3)[:, m]
            T = kvec * e.T + e * kvec.T
            cols.append(sp.Matrix([T[0, 0], T[1, 1], T[2, 2], T[0, 1], T[0, 2], T[1, 2]]))
        M = sp.Matrix.hstack(*cols)
        assert M.rank() == 3
    print("PASS exact nonzero Fourier Killing kernel: rank 3 for all test modes")


def project_hat_field(vh: np.ndarray) -> np.ndarray:
    return leray_hat(vh)


def mother_apply_plane_wave(u: np.ndarray, kvec: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Apply E_u to the complex plane wave b exp(i k.x) using the exact local mother formula."""
    N = u.shape[0]
    G = gradient_field(u)
    coords = np.arange(N) * (2.0 * np.pi / N)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    phase = np.exp(1j * (kvec[0] * X + kvec[1] * Y + kvec[2] * Z))
    # sum_j grad(u_j) * k_j = G^T k.
    GTk = np.einsum("...ji,j->...i", G, kvec)
    raw = -1j * np.cross(GTk, b) * phase[..., None]
    rh = np.fft.fftn(raw, axes=(0, 1, 2))
    rh = project_hat_field(rh)
    return np.fft.ifftn(rh, axes=(0, 1, 2))


def perpendicular_unit(kvec: np.ndarray) -> np.ndarray:
    kvec = np.asarray(kvec, dtype=float)
    ref = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(ref, kvec) / np.linalg.norm(kvec)) > 0.8:
        ref = np.array([0.0, 1.0, 0.0])
    b = np.cross(kvec, ref)
    return b / np.linalg.norm(b)


def q_from_probe_response(Ev: np.ndarray, kvec: np.ndarray, b: np.ndarray) -> np.ndarray:
    N = Ev.shape[0]
    coords = np.arange(N) * (2.0 * np.pi / N)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    phase_conj = np.exp(-1j * (kvec[0] * X + kvec[1] * Y + kvec[2] * Z))
    c = np.cross(kvec, b)
    demod = Ev * phase_conj[..., None]
    # E ~ -i q c exp(ikx), hence q ~ Re(i E e^-ikx . c / |c|^2).
    return np.real(1j * np.einsum("...i,i->...", demod, c) / np.dot(c, c))


def reconstruct_from_actual_probes(u: np.ndarray, base_k: int) -> np.ndarray:
    qfields = []
    int_dirs = [
        np.array([1, 0, 0]),
        np.array([0, 1, 0]),
        np.array([0, 0, 1]),
        np.array([1, 1, 0]),
        np.array([1, 0, 1]),
        np.array([0, 1, 1]),
    ]
    for d in int_dirs:
        kvec = base_k * d
        b = perpendicular_unit(kvec)
        Ev = mother_apply_plane_wave(u, kvec, b)
        qfields.append(q_from_probe_response(Ev, kvec, b))
    q = np.stack(qfields, axis=-1)
    coeff = np.einsum("ab,...b->...a", QPINV, q)
    Srec = np.einsum("...a,aij->...ij", coeff, STRAIN_BASIS)
    return velocity_from_strain(Srec)


def audit_actual_probe_parametrix(N: int = 64) -> None:
    u = random_divfree_field(N, bandwidth=1, seed=777)
    ks = [6, 10, 14, 18]
    errs = []
    for k in ks:
        urec = reconstruct_from_actual_probes(u, k)
        errs.append(relerr(u, urec))
    # Require strict convergence and approximately quadratic improvement in the resolved regime.
    assert all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
    scaled = [e * k * k for e, k in zip(errs, ks)]
    assert max(scaled[1:]) / min(scaled[1:]) < 2.5
    print("PASS actual six-probe parametrix:", [(k, float(e)) for k, e in zip(ks, errs)])


def fourier_scale_integer(u: np.ndarray, lam: int) -> np.ndarray:
    """u_lam(x)=lam u(lam x) on a periodic grid, for integer lam and low-band u."""
    N = u.shape[0]
    uh = np.fft.fftn(u, axes=(0, 1, 2))
    out = np.zeros_like(uh)
    kx, ky, kz, _ = fft_wavenumbers(N)
    # Direct sparse remap of nonzero Fourier coefficients.
    for i in range(N):
        for j in range(N):
            for l in range(N):
                k = np.array([int(kx[i, j, l]), int(ky[i, j, l]), int(kz[i, j, l])])
                if np.any(k != 0):
                    target = lam * k
                    if np.any(np.abs(target) >= N // 2):
                        continue
                    ti = tuple((target % N).astype(int))
                    out[ti] += lam * uh[i, j, l]
    return np.fft.ifftn(out, axes=(0, 1, 2)).real


def audit_scaling_covariance(N: int = 64) -> None:
    base = random_divfree_field(N, bandwidth=1, seed=991)
    base_k = 6
    errs = []
    for lam in [1, 2, 3]:
        u = fourier_scale_integer(base, lam)
        urec = reconstruct_from_actual_probes(u, lam * base_k)
        errs.append(relerr(u, urec))
    spread = max(errs) - min(errs)
    assert spread < 5e-10
    print("PASS NS scaling covariance of parametrix:", errs)


def audit_spherical_metric(trials: int = 50, samples: int = 20000) -> None:
    ratios = []
    for _ in range(trials):
        S = strain_from_coeff(RNG.normal(size=5))
        n = RNG.normal(size=(samples, 3))
        n /= np.linalg.norm(n, axis=1, keepdims=True)
        q = np.einsum("ni,ij,nj->n", n, S, n)
        lhs = float(np.mean(2.0 * q * q))
        rhs = float(np.sum(S * S))
        ratios.append(lhs / rhs)
    med = float(np.median(ratios))
    assert abs(med - 4.0 / 15.0) < 5e-3
    print(f"PASS spherical signature metric: median ratio={med:.8f}, expected={4/15:.8f}")


def main() -> None:
    audit_principal_symbol()
    audit_six_direction_strain()
    audit_periodic_field_inverse()
    audit_exact_killing_kernel()
    audit_spherical_metric()
    audit_actual_probe_parametrix()
    audit_scaling_covariance()
    print("PASS: curl spectral-flag completeness core")


if __name__ == "__main__":
    main()
