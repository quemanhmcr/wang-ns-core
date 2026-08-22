"""Finite-dimensional algebra audit for the Theory-2 interaction frame.

This checks sign conventions only.  It is not evidence for the continuum
regularity theorem.
"""

import numpy as np


def skew(n, rng):
    a = rng.standard_normal((n, n))
    return a - a.T


def sym(n, rng):
    a = rng.standard_normal((n, n))
    return 0.5 * (a + a.T)


def relerr(a, b):
    return np.linalg.norm(a - b) / max(1.0, np.linalg.norm(a), np.linalg.norm(b))


def main():
    rng = np.random.default_rng(20260823)
    n = 9
    gamma = skew(n, rng)
    c = sym(n, rng)
    u = rng.standard_normal(n)
    nu = 0.37

    # Evaluate all identities at an instant where U = I.
    U = np.eye(n)
    U_t = -gamma @ U
    Ustar_t = U.T @ gamma
    u_t = -gamma @ u - nu * (c @ c) @ u

    v = U.T @ u
    v_t = Ustar_t @ u + U.T @ u_t
    csharp = U.T @ c @ U
    csharp_t = Ustar_t @ c @ U + U.T @ c @ U_t

    expected_v_t = -nu * (csharp @ csharp) @ v
    expected_c_t = gamma @ c - c @ gamma

    # Polynomial functional-calculus proxy f(C)=C^3.
    f = c @ c @ c
    f_t_chain = (
        csharp_t @ c @ c
        + c @ csharp_t @ c
        + c @ c @ csharp_t
    )
    expected_f_t = gamma @ f - f @ gamma

    errors = {
        "unitary_generator_skew": np.linalg.norm(gamma + gamma.T),
        "heat_only_state": relerr(v_t, expected_v_t),
        "moving_curl_commutator": relerr(csharp_t, expected_c_t),
        "functional_calculus_commutator": relerr(f_t_chain, expected_f_t),
    }

    for name, err in errors.items():
        print(f"{name}: {err:.3e}")

    worst = max(errors.values())
    if worst > 1e-11:
        raise SystemExit(f"audit failed: worst residual {worst:.3e}")

    print("PASS")


if __name__ == "__main__":
    main()
