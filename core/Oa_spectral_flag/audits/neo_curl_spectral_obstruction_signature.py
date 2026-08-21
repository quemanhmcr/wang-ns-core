"""Portable algebra audit for the NEO curl spectral-obstruction signature.

The audit is intentionally finite-dimensional.  It checks identities that are purely
algebraic once a metric state-space connection, a self-adjoint curl operator and its
spectral cuts are supplied:

  1. O_H(v) = H [D_v,H] - [D_{Hv},H] reverse-compiles the whole cut connection;
  2. ||O||^2 summed over directions is exactly twice ||[D,H]||^2;
  3. Euler torsion and Nijenhuis defect are the symmetric/antisymmetric
     polarizations of the same O;
  4. the shifted family O_a tomographically reconstructs [D,C];
  5. every first spectral reader [D,f(C)] is a weighted moment of the same signature;
  6. the kernel of the full shifted-cut map is exactly the skew curl commutant;
  7. the shifted family carries the exact layer-cake crossing metric;
  8. nested spectral commutator towers are shifted-flag tomographies at all tested orders;
  9. scalar/self contractions can be blind while the operator signature is nonzero.

This is not a continuum regularity proof.  It is a canonical-syntax / ontology audit.
"""

from __future__ import annotations

import numpy as np


RNG = np.random.default_rng(20260821)
TOL = 5e-11


def skew_matrix(n: int) -> np.ndarray:
    m = RNG.normal(size=(n, n))
    return m - m.T


def sign_cut(roots: np.ndarray, a: float) -> np.ndarray:
    s = np.sign(roots - a)
    if np.any(s == 0):
        raise ValueError("audit threshold landed on a spectral root")
    return np.diag(s)


def connection_value(conn: list[np.ndarray], v: np.ndarray) -> np.ndarray:
    return sum(float(v[i]) * conn[i] for i in range(len(conn)))


def A_of(conn: list[np.ndarray], H: np.ndarray, v: np.ndarray) -> np.ndarray:
    Dv = connection_value(conn, v)
    return Dv @ H - H @ Dv


def O_of(conn: list[np.ndarray], H: np.ndarray, v: np.ndarray) -> np.ndarray:
    Av = A_of(conn, H, v)
    AHv = A_of(conn, H, H @ v)
    return H @ Av - AHv


def sym(m: np.ndarray) -> np.ndarray:
    return 0.5 * (m + m.T)


def skew(m: np.ndarray) -> np.ndarray:
    return 0.5 * (m - m.T)


def relerr(a: np.ndarray, b: np.ndarray) -> float:
    den = max(1.0, np.linalg.norm(a), np.linalg.norm(b))
    return float(np.linalg.norm(a - b) / den)


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def nested_ad(ds: list[np.ndarray], x: np.ndarray) -> np.ndarray:
    out = x
    for d in reversed(ds):
        out = commutator(d, out)
    return out


def skew_basis(n: int) -> list[np.ndarray]:
    out: list[np.ndarray] = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n))
            m[i, j] = 1.0
            m[j, i] = -1.0
            out.append(m)
    return out


def spectral_matrix(roots: np.ndarray, f) -> np.ndarray:
    return np.diag(np.array([f(float(x)) for x in roots], dtype=float))


def B_of(conn: list[np.ndarray], p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return -0.5 * (connection_value(conn, p) @ q + connection_value(conn, q) @ p)


def bracket_of(conn: list[np.ndarray], p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return connection_value(conn, p) @ q - connection_value(conn, q) @ p


def torsion(conn: list[np.ndarray], H: np.ndarray, p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return (
        B_of(conn, H @ p, H @ q)
        - H @ B_of(conn, H @ p, q)
        - H @ B_of(conn, p, H @ q)
        + B_of(conn, p, q)
    )


def nijenhuis(conn: list[np.ndarray], H: np.ndarray, p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return (
        bracket_of(conn, H @ p, H @ q)
        - H @ bracket_of(conn, H @ p, q)
        - H @ bracket_of(conn, p, H @ q)
        + bracket_of(conn, p, q)
    )


def audit_reverse_and_norm(trials: int = 400, n: int = 6) -> None:
    max_reverse = 0.0
    max_sym = 0.0
    max_norm = 0.0

    H = np.diag([1.0] * (n // 2) + [-1.0] * (n - n // 2))
    basis = np.eye(n)

    for _ in range(trials):
        conn = [skew_matrix(n) for _ in range(n)]

        lhs_norm = 0.0
        rhs_norm = 0.0
        for e in basis:
            A = A_of(conn, H, e)
            O = O_of(conn, H, e)
            Arec = H @ skew(O)
            AHrec = -sym(O)

            max_reverse = max(max_reverse, relerr(A, Arec))
            max_sym = max(max_sym, relerr(A_of(conn, H, H @ e), AHrec))
            lhs_norm += np.linalg.norm(O) ** 2
            rhs_norm += 2.0 * np.linalg.norm(A) ** 2

        max_norm = max(max_norm, abs(lhs_norm - rhs_norm) / max(1.0, lhs_norm, rhs_norm))

    assert max_reverse < TOL
    assert max_sym < TOL
    assert max_norm < TOL
    print(f"PASS reverse O->A: max relerr {max_reverse:.3e}")
    print(f"PASS symmetric part of O: max relerr {max_sym:.3e}")
    print(f"PASS sum ||O||^2 = 2 sum ||A||^2: max relerr {max_norm:.3e}")


def audit_torsion_nijenhuis(trials: int = 400, n: int = 6) -> None:
    H = np.diag([1.0] * (n // 2) + [-1.0] * (n - n // 2))
    max_t = 0.0
    max_n = 0.0
    max_r = 0.0
    max_self = 0.0

    for _ in range(trials):
        conn = [skew_matrix(n) for _ in range(n)]
        p = RNG.normal(size=n)
        q = RNG.normal(size=n)

        Opq = O_of(conn, H, p) @ q
        Oqp = O_of(conn, H, q) @ p
        T = torsion(conn, H, p, q)
        N = nijenhuis(conn, H, p, q)

        max_t = max(max_t, relerr(T, 0.5 * (Opq + Oqp)))
        max_n = max(max_n, relerr(N, Oqp - Opq))
        max_r = max(max_r, relerr(Opq, T - 0.5 * N))

        self_O = O_of(conn, H, p) @ p
        self_T = torsion(conn, H, p, p)
        max_self = max(max_self, relerr(self_O, self_T))

    assert max_t < TOL
    assert max_n < TOL
    assert max_r < TOL
    assert max_self < TOL
    print(f"PASS torsion polarization: max relerr {max_t:.3e}")
    print(f"PASS Nijenhuis polarization: max relerr {max_n:.3e}")
    print(f"PASS O = T - N/2: max relerr {max_r:.3e}")
    print(f"PASS self contraction O(u)u = T(u,u): max relerr {max_self:.3e}")


def audit_shifted_tomography(trials: int = 300, n: int = 6) -> None:
    max_A_tomo = 0.0
    max_O_tomo = 0.0
    max_point_reverse = 0.0

    for _ in range(trials):
        roots = np.sort(RNG.uniform(-3.0, 3.0, size=n))
        if np.min(np.diff(roots)) < 2e-2:
            continue
        C = np.diag(roots)
        conn = [skew_matrix(n) for _ in range(n)]
        v = RNG.normal(size=n)
        Dv = connection_value(conn, v)
        E = Dv @ C - C @ Dv

        int_A = np.zeros_like(E)
        int_O = np.zeros_like(E)
        for left, right in zip(roots[:-1], roots[1:]):
            a = 0.5 * (left + right)
            width = right - left
            H = sign_cut(roots, a)
            A = A_of(conn, H, v)
            O = O_of(conn, H, v)
            Arec = H @ skew(O)
            max_point_reverse = max(max_point_reverse, relerr(A, Arec))
            int_A += width * A
            int_O += width * (H @ skew(O))

        max_A_tomo = max(max_A_tomo, relerr(E, 0.5 * int_A))
        max_O_tomo = max(max_O_tomo, relerr(E, 0.5 * int_O))

    assert max_A_tomo < TOL
    assert max_O_tomo < TOL
    assert max_point_reverse < TOL
    print(f"PASS E = 1/2 int [D,H_a] da: max relerr {max_A_tomo:.3e}")
    print(f"PASS E = 1/2 int H_a skew(O_a) da: max relerr {max_O_tomo:.3e}")
    print(f"PASS shifted pointwise O_a->A_a: max relerr {max_point_reverse:.3e}")


def audit_blindness_examples() -> None:
    # H has a three-dimensional + sheet and a three-dimensional - sheet.
    n = 6
    H = np.diag([1.0, 1.0, 1.0, -1.0, -1.0, -1.0])
    Lambda = np.diag([1.0, 1.5, 2.0, 1.2, 1.8, 2.4])
    u = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Pure-sheet scalar blindness: choose D_u coupling u to the opposite sheet.
    conn = [np.zeros((n, n)) for _ in range(n)]
    D0 = np.zeros((n, n))
    D0[0, 3] = 1.0
    D0[3, 0] = -1.0
    conn[0] = D0
    O = O_of(conn, H, u)
    J = 0.25 * (O @ u)
    W = float((Lambda @ u) @ (O @ u))
    second = 4.0 * float(J @ (Lambda @ J))

    assert abs(W) < TOL
    assert np.linalg.norm(J) > 1e-6
    assert second > 0.0
    print(f"PASS pure-sheet blindness: W={W:.3e}, ||J||={np.linalg.norm(J):.3e}, square={second:.3e}")

    # Self-contraction blindness: keep O nonzero on an independent block, but O(u)u=0.
    conn2 = [np.zeros((n, n)) for _ in range(n)]
    D1 = np.zeros((n, n))
    D1[1, 4] = 1.0
    D1[4, 1] = -1.0
    conn2[0] = D1
    O2 = O_of(conn2, H, u)
    J2 = 0.25 * (O2 @ u)
    probe = np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0])

    assert np.linalg.norm(J2) < TOL
    assert np.linalg.norm(O2 @ probe) > 1e-6
    print(
        "PASS self-contraction blindness: "
        f"||O(u)u||={np.linalg.norm(O2 @ u):.3e}, "
        f"||O(u)probe||={np.linalg.norm(O2 @ probe):.3e}"
    )


def audit_universal_readers(trials: int = 250, n: int = 6) -> None:
    readers = [
        ("x", lambda x: x),
        ("x2", lambda x: x * x),
        ("cubic", lambda x: x**3 - 0.7 * x),
        ("exp", lambda x: np.exp(0.13 * x)),
        ("sinpoly", lambda x: np.sin(0.4 * x) + 0.2 * x * x),
        ("smoothabs", lambda x: np.sqrt(x * x + 0.31)),
    ]
    worst = {name: 0.0 for name, _ in readers}

    for _ in range(trials):
        roots = np.sort(RNG.uniform(-3.0, 3.0, size=n))
        if np.min(np.diff(roots)) < 2e-2:
            continue
        C = np.diag(roots)
        conn = [skew_matrix(n) for _ in range(n)]
        v = RNG.normal(size=n)
        D = connection_value(conn, v)

        for name, f in readers:
            F = spectral_matrix(roots, f)
            direct = commutator(D, F)
            rec = np.zeros_like(D)
            for left, right in zip(roots[:-1], roots[1:]):
                a = 0.5 * (left + right)
                H = sign_cut(roots, a)
                O = O_of(conn, H, v)
                # Integral of f'(a) over one interval is exactly f(right)-f(left).
                rec += (f(float(right)) - f(float(left))) * (H @ skew(O))
            rec *= 0.5
            worst[name] = max(worst[name], relerr(direct, rec))

    assert max(worst.values()) < TOL
    for name in worst:
        print(f"PASS universal reader {name}: max relerr {worst[name]:.3e}")


def audit_commutant_kernel_and_metric() -> None:
    spectra = [
        np.array([-3.0, -2.0, -1.0, 1.0, 2.0, 3.0]),
        np.array([-2.0, -2.0, -1.0, 1.0, 2.0, 2.0]),
        np.array([-1.0, -1.0, -1.0, 2.0, 2.0, 3.0]),
        np.array([1.0, 1.0, 1.0, 1.0, 2.0, 2.0]),
    ]
    for roots in spectra:
        n = len(roots)
        basis = skew_basis(n)
        cuts = [0.5 * (x + y) for x, y in zip(np.unique(roots)[:-1], np.unique(roots)[1:])]
        cols = []
        for D in basis:
            pieces = []
            for a in cuts:
                H = sign_cut(roots, float(a))
                pieces.append(commutator(D, H).ravel())
            cols.append(np.concatenate(pieces) if pieces else np.zeros(1))
        M = np.stack(cols, axis=1)
        rank = int(np.linalg.matrix_rank(M, tol=1e-10))
        nullity = len(basis) - rank

        _, counts = np.unique(roots, return_counts=True)
        predicted = int(sum(int(m) * (int(m) - 1) // 2 for m in counts))
        assert nullity == predicted
        print(f"PASS commutant kernel spectrum={roots.tolist()}: nullity={nullity}")

    max_metric = 0.0
    for _ in range(300):
        roots = np.sort(RNG.uniform(-3.0, 3.0, size=6))
        if np.min(np.diff(roots)) < 2e-2:
            continue
        D = skew_matrix(6)
        lhs = 0.0
        for left, right in zip(roots[:-1], roots[1:]):
            H = sign_cut(roots, 0.5 * (left + right))
            lhs += (right - left) * np.linalg.norm(commutator(D, H)) ** 2
        rhs = 0.0
        for i, x in enumerate(roots):
            for j, y in enumerate(roots):
                rhs += 4.0 * abs(float(x - y)) * abs(float(D[i, j])) ** 2
        max_metric = max(max_metric, abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs)))
    assert max_metric < TOL
    print(f"PASS layer-cake crossing metric: max relerr {max_metric:.3e}")


def audit_all_order_flag_tomography(trials: int = 160, n: int = 6, max_order: int = 4) -> None:
    readers = [
        ("exp", lambda x: np.exp(0.17 * x)),
        ("sinpoly", lambda x: np.sin(0.37 * x) + 0.11 * x * x),
        ("smoothabs", lambda x: np.sqrt(x * x + 0.43)),
    ]
    worst: dict[tuple[str, int], float] = {}

    for _ in range(trials):
        roots = np.sort(RNG.uniform(-2.5, 2.5, size=n))
        if np.min(np.diff(roots)) < 2e-2:
            continue
        ds_all = [skew_matrix(n) for _ in range(max_order)]
        for name, f in readers:
            F = spectral_matrix(roots, f)
            for order in range(1, max_order + 1):
                ds = ds_all[:order]
                direct = nested_ad(ds, F)
                rec = np.zeros_like(F)
                for left, right in zip(roots[:-1], roots[1:]):
                    H = sign_cut(roots, 0.5 * (left + right))
                    rec += (f(float(right)) - f(float(left))) * nested_ad(ds, H)
                rec *= 0.5
                key = (name, order)
                worst[key] = max(worst.get(key, 0.0), relerr(direct, rec))

    assert max(worst.values()) < TOL
    for name, _ in readers:
        vals = [worst[(name, order)] for order in range(1, max_order + 1)]
        print("PASS all-order flag", name, "orders 1..4:", " ".join(f"{x:.3e}" for x in vals))


def main() -> None:
    audit_reverse_and_norm()
    audit_torsion_nijenhuis()
    audit_shifted_tomography()
    audit_universal_readers()
    audit_commutant_kernel_and_metric()
    audit_all_order_flag_tomography()
    audit_blindness_examples()
    print("PASS: curl spectral-obstruction signature core algebra")


if __name__ == "__main__":
    main()
