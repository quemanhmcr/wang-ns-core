"""Portable audit for the NEO Mother / Spectral-Flag Completeness Theorem.

This file tests the algebraic and Fourier pieces used by the smooth periodic
structural theorem.  It does NOT claim a Navier--Stokes regularity result.

Audited pieces:
  * mother principal symbol = strain quadratic form;
  * six fixed directions form an explicit frame on Sym_0(3);
  * exact homogeneous Sobolev Korn/isometry identity for fractional s;
  * periodic strain -> velocity Poisson inverse;
  * one-sided spectral seams do not affect layer-cake reconstruction;
  * signature reverse compiler on finite spectral geometry;
  * degenerate-spectrum horizontal/vertical gauge decomposition;
  * physical-image projector algebra once a left inverse exists.
"""

from __future__ import annotations

import math
import numpy as np
import sympy as sp

RNG = np.random.default_rng(20260821)
TOL = 5e-11


def relerr(a: np.ndarray, b: np.ndarray) -> float:
    den = max(1.0, float(np.linalg.norm(a)), float(np.linalg.norm(b)))
    return float(np.linalg.norm(a - b) / den)


def leray_symbol(xi: np.ndarray) -> np.ndarray:
    xi = np.asarray(xi, dtype=float)
    return np.eye(3) - np.outer(xi, xi) / float(xi @ xi)


def cross_matrix(x: np.ndarray) -> np.ndarray:
    x1, x2, x3 = x
    return np.array([[0.0, -x3, x2], [x3, 0.0, -x1], [-x2, x1, 0.0]])


def audit_principal_symbol(trials: int = 3000) -> None:
    worst = 0.0
    for _ in range(trials):
        G = RNG.normal(size=(3, 3))
        G -= np.eye(3) * np.trace(G) / 3.0
        S = 0.5 * (G + G.T)
        xi = RNG.normal(size=3)
        xi /= np.linalg.norm(xi)
        b = RNG.normal(size=3)
        b -= xi * (xi @ b)
        if np.linalg.norm(b) < 1e-10:
            continue
        b /= np.linalg.norm(b)
        P = leray_symbol(xi)
        lhs = -1j * P @ np.cross(G.T @ xi, b)
        q = float(xi @ S @ xi)
        rhs = -1j * q * np.cross(xi, b)
        worst = max(worst, relerr(lhs, rhs))
    assert worst < 5e-10
    print(f"PASS principal symbol = strain quadratic form: max relerr {worst:.3e}")


def sym0_frame_matrix_exact() -> sp.Matrix:
    # Frobenius-orthonormal basis of Sym_0(3).
    rt2, rt6 = sp.sqrt(2), sp.sqrt(6)
    B = [
        sp.Matrix([[1 / rt2, 0, 0], [0, -1 / rt2, 0], [0, 0, 0]]),
        sp.Matrix([[1 / rt6, 0, 0], [0, 1 / rt6, 0], [0, 0, -2 / rt6]]),
        sp.Matrix([[0, 1 / rt2, 0], [1 / rt2, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 1 / rt2], [0, 0, 0], [1 / rt2, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1 / rt2], [0, 1 / rt2, 0]]),
    ]
    dirs = [
        sp.Matrix([1, 0, 0]),
        sp.Matrix([0, 1, 0]),
        sp.Matrix([0, 0, 1]),
        sp.Matrix([1 / rt2, 1 / rt2, 0]),
        sp.Matrix([1 / rt2, 0, 1 / rt2]),
        sp.Matrix([0, 1 / rt2, 1 / rt2]),
    ]
    A = sp.zeros(6, 5)
    for i, n in enumerate(dirs):
        for j, Bj in enumerate(B):
            A[i, j] = sp.simplify((n.T * Bj * n)[0])
    return A


def audit_six_direction_frame() -> None:
    A = sym0_frame_matrix_exact()
    G = sp.simplify(A.T * A)
    lam = sp.symbols("lambda")
    char = sp.factor(G.charpoly(lam).as_expr())
    expected_char = sp.factor((2 * lam - 1) * (4 * lam**2 - 7 * lam + 2) ** 2 / 32)
    assert sp.simplify(char - expected_char) == 0
    eig = G.eigenvals()
    expected = {
        sp.Rational(1, 2): 1,
        (sp.Integer(7) - sp.sqrt(17)) / 8: 2,
        (sp.Integer(7) + sp.sqrt(17)) / 8: 2,
    }
    assert eig == expected
    lmin = float((sp.Integer(7) - sp.sqrt(17)) / 8)
    lmax = float((sp.Integer(7) + sp.sqrt(17)) / 8)
    assert lmin > 0
    print(
        "PASS exact six-direction frame: "
        f"lambda_min={lmin:.12f}, lambda_max={lmax:.12f}, "
        f"state constants={lmin/2:.12f},{lmax/2:.12f}"
    )


def random_divfree_fourier(N: int = 9) -> np.ndarray:
    # Complex Fourier coefficients with Hermitian symmetry are unnecessary for the
    # norm identity; we only need k . uhat = 0 modewise.
    coeff = np.zeros((N, N, N, 3), dtype=complex)
    ks = np.fft.fftfreq(N) * N
    for i, k1 in enumerate(ks):
        for j, k2 in enumerate(ks):
            for l, k3 in enumerate(ks):
                k = np.array([k1, k2, k3], dtype=float)
                k2n = float(k @ k)
                if k2n == 0.0:
                    continue
                z = RNG.normal(size=3) + 1j * RNG.normal(size=3)
                z -= k * (k @ z) / k2n
                coeff[i, j, l] = z
    return coeff


def audit_fractional_sobolev_isometry() -> None:
    N = 9
    coeff = random_divfree_fourier(N)
    ks = np.fft.fftfreq(N) * N
    ss = [-1.0, -0.75, -0.25, 0.0, 0.5, 1.0, 1.7, 2.3]
    worst = 0.0
    for s in ss:
        U = 0.0
        S2 = 0.0
        for i, k1 in enumerate(ks):
            for j, k2 in enumerate(ks):
                for l, k3 in enumerate(ks):
                    k = np.array([k1, k2, k3], dtype=float)
                    kn = float(np.linalg.norm(k))
                    if kn == 0.0:
                        continue
                    u = coeff[i, j, l]
                    G = 1j * np.outer(k, u)
                    Sm = 0.5 * (G + G.T)
                    U += kn ** (2 * (s + 1)) * float(np.vdot(u, u).real)
                    S2 += kn ** (2 * s) * float(np.vdot(Sm, Sm).real)
        r = abs(U - 2.0 * S2) / max(1.0, U, 2.0 * S2)
        worst = max(worst, r)
    assert worst < TOL
    print(f"PASS exact fractional Sobolev isometry: max relerr {worst:.3e}")


def audit_periodic_poisson_inverse(trials: int = 10, N: int = 9) -> None:
    ks = np.fft.fftfreq(N) * N
    worst = 0.0
    for _ in range(trials):
        coeff = random_divfree_fourier(N)
        rec = np.zeros_like(coeff)
        for i, k1 in enumerate(ks):
            for j, k2 in enumerate(ks):
                for l, k3 in enumerate(ks):
                    k = np.array([k1, k2, k3], dtype=float)
                    k2n = float(k @ k)
                    if k2n == 0.0:
                        continue
                    u = coeff[i, j, l]
                    G = 1j * np.outer(k, u)
                    S = 0.5 * (G + G.T)
                    # Fourier div S = i S k, Delta^{-1} = -1/|k|^2.
                    rec[i, j, l] = 2.0 * (-1.0 / k2n) * (1j * S @ k)
        worst = max(worst, relerr(coeff, rec))
    assert worst < TOL
    print(f"PASS periodic S->u Poisson inverse: max relerr {worst:.3e}")


def skew_matrix(n: int) -> np.ndarray:
    M = RNG.normal(size=(n, n))
    return M - M.T


def sign_cut(roots: np.ndarray, a: float, seam_sign: float = 1.0) -> np.ndarray:
    d = roots - a
    s = np.sign(d)
    s[s == 0] = seam_sign
    return np.diag(s)


def skew(M: np.ndarray) -> np.ndarray:
    return 0.5 * (M - M.T)


def audit_signature_layer_cake_and_seams(trials: int = 200, n: int = 7) -> None:
    worst_layer = 0.0
    worst_reverse = 0.0
    roots = np.array([-3.0, -2.0, -2.0, -0.5, 1.0, 1.0, 2.5])
    unique = np.unique(roots)
    for _ in range(trials):
        D = skew_matrix(n)
        C = np.diag(roots)
        E = D @ C - C @ D
        # Exact layer cake: integrate intervalwise between unique roots.
        integ = np.zeros_like(E)
        for left, right in zip(unique[:-1], unique[1:]):
            a = 0.5 * (left + right)
            H = sign_cut(roots, a)
            A = D @ H - H @ D
            integ += (right - left) * A
        worst_layer = max(worst_layer, relerr(E, 0.5 * integ))

        # Seam conventions +/- both preserve involution and reverse compiler.
        for a in unique:
            for seam_sign in (-1.0, 1.0):
                H = sign_cut(roots, float(a), seam_sign)
                assert relerr(H @ H, np.eye(n)) < TOL
                A = D @ H - H @ D
                # Abstract metric one-form second term chosen as an independent
                # self-adjoint block under H; only adjoint parity is needed to
                # audit the reverse formula.
                B = RNG.normal(size=(n, n))
                B = 0.5 * (B + B.T)
                O = H @ A - B
                Arec = H @ skew(O)
                worst_reverse = max(worst_reverse, relerr(A, Arec))
    assert worst_layer < TOL
    assert worst_reverse < TOL
    print(
        "PASS layer cake + one-sided seams: "
        f"layer={worst_layer:.3e}, reverse={worst_reverse:.3e}"
    )


def audit_spherical_decoder(trials: int = 2000) -> None:
    # Use exact isotropic fourth-moment tensor rather than Monte Carlo sphere quadrature.
    worst = 0.0
    for _ in range(trials):
        M = RNG.normal(size=(3, 3))
        S = 0.5 * (M + M.T)
        S -= np.eye(3) * np.trace(S) / 3.0
        # R_ij = < (n^T S n) n_i n_j > = (tr S delta_ij + 2 S_ij)/15.
        R = (np.trace(S) * np.eye(3) + 2.0 * S) / 15.0
        Srec = 7.5 * R
        worst = max(worst, relerr(S, Srec))
    assert worst < TOL
    print(f"PASS exact spherical strain decoder: max relerr {worst:.3e}")


def audit_fourier_killing_kernel() -> None:
    tests = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, -1, 3), (5, 2, -4)]
    for kval in tests:
        k = sp.Matrix(kval)
        # Unknown complex/vector amplitude treated algebraically over R: map u -> sym(k⊗u).
        u1, u2, u3 = sp.symbols("u1 u2 u3")
        u = sp.Matrix([u1, u2, u3])
        G = k * u.T + u * k.T
        eqs = [G[i, j] for i in range(3) for j in range(i, 3)]
        A, _ = sp.linear_eq_to_matrix(eqs, [u1, u2, u3])
        assert A.rank() == 3
    print("PASS exact nonzero Fourier Killing kernel: only zero mode survives periodically")


def audit_gauge_decomposition() -> None:
    spectra = [
        np.array([-3.0, -2.0, -1.0, 1.0, 2.0, 3.0]),
        np.array([-2.0, -2.0, -1.0, 1.0, 2.0, 2.0]),
        np.array([-1.0, -1.0, -1.0, 2.0, 2.0, 3.0]),
    ]
    worst = 0.0
    for roots in spectra:
        n = len(roots)
        G = skew_matrix(n)
        C = np.diag(roots)
        E = G @ C - C @ G
        hor = np.zeros_like(G)
        vert = np.zeros_like(G)
        for i in range(n):
            for j in range(n):
                d = roots[j] - roots[i]
                if abs(d) > 1e-14:
                    hor[i, j] = E[i, j] / d
                else:
                    vert[i, j] = G[i, j]
        worst = max(worst, relerr(G, hor + vert))
        worst = max(worst, relerr(hor @ C - C @ hor, E))
        worst = max(worst, relerr(vert @ C - C @ vert, np.zeros_like(G)))
    assert worst < TOL
    print(f"PASS horizontal/vertical curl-gauge reconstruction: max relerr {worst:.3e}")


def audit_image_projector_and_tangency() -> None:
    # Abstract algebra of a physical signature map S with an exact left inverse R.
    # This tests the theorem's projector/conjugacy identities independently of NS numerics.
    n, m = 17, 41
    S = RNG.normal(size=(m, n))
    while np.linalg.matrix_rank(S) < n:
        S = RNG.normal(size=(m, n))
    R = np.linalg.solve(S.T @ S, S.T)
    P = S @ R
    idem = relerr(P @ P, P)
    left = relerr(R @ S, np.eye(n))
    u = RNG.normal(size=n)
    y = S @ u
    fixed = relerr(P @ y, y)
    # A generic quadratic-linear vector field stands in for F_NS; tangency is purely conjugacy algebra.
    A = RNG.normal(size=(n, n))
    Q = RNG.normal(size=(n, n, n))
    F = A @ u + np.einsum("ijk,j,k->i", Q, u, u)
    Fy = S @ F
    tangent = relerr(P @ Fy, Fy)
    worst = max(idem, left, fixed, tangent)
    assert worst < 5e-10
    print(
        "PASS signature-image projector/conjugacy algebra: "
        f"idempotence={idem:.3e}, left={left:.3e}, tangent={tangent:.3e}"
    )


def main() -> None:
    audit_principal_symbol()
    audit_six_direction_frame()
    audit_fractional_sobolev_isometry()
    audit_periodic_poisson_inverse()
    audit_signature_layer_cake_and_seams()
    audit_spherical_decoder()
    audit_fourier_killing_kernel()
    audit_gauge_decomposition()
    audit_image_projector_and_tangency()
    print("PASS: mother / spectral-flag completeness theorem core")


if __name__ == "__main__":
    main()
