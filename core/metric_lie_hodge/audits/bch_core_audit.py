#!/usr/bin/env python3
"""Canonical mixed Euler-heat BCH audit using only B and L=-C^2."""
from __future__ import annotations

from formation_core_audit import B, lap, norm, random_field, scaled_residual


def L(v):
    return lap(v)


def Q(a, b):
    return L(B(a, b)) - B(L(a), b) - B(a, L(b))


def E(u):
    return B(u, u)


def H(u):
    return L(u)


def A(u):  # [E,H] with convention [F,G]=DG F-DF G
    return Q(u, u)


def DA(u, v):
    return 2.0 * Q(u, v)


def DE(u, v):
    return 2.0 * B(u, v)


def B1(u):  # [E,A]
    return 2.0 * Q(u, E(u)) - 2.0 * B(u, A(u))


def DB1(u, v):
    return (
        2.0 * Q(v, E(u))
        + 2.0 * Q(u, DE(u, v))
        - 2.0 * B(v, A(u))
        - 2.0 * B(u, DA(u, v))
    )


def C1(u):  # [H,A]
    return 2.0 * Q(u, H(u)) - L(A(u))


def DC1(u, v):
    return 2.0 * Q(v, H(u)) + 2.0 * Q(u, L(v)) - L(DA(u, v))


def audit(seed=20260831):
    u = random_field(seed)

    # First mixed level from the definition of the vector-field commutator.
    first_direct = L(E(u)) - DE(u, H(u))
    first_tree = Q(u, u)
    r1 = scaled_residual(first_direct, first_tree)

    # One additional Euler insertion.
    second_direct = DA(u, E(u)) - DE(u, A(u))
    second_tree = B1(u)
    r2 = scaled_residual(second_direct, second_tree)

    # One additional heat insertion.
    heat_direct = DA(u, H(u)) - L(A(u))
    heat_tree = C1(u)
    r3 = scaled_residual(heat_direct, heat_tree)

    # Jacobi locking: [E,[H,A]]=[H,[E,A]].
    left = DC1(u, E(u)) - DE(u, C1(u))
    right = DB1(u, H(u)) - L(B1(u))
    r_jacobi = scaled_residual(left, right)

    results = {
        "first_mixed_Q": r1,
        "euler_after_mixed": r2,
        "heat_after_mixed": r3,
        "jacobi_route_lock": r_jacobi,
    }
    return results


def main():
    results = audit()
    tol = 5e-9
    print("Euler-heat BCH core audit")
    for name, value in results.items():
        print(f"{name:32s} {value:.3e}")
    worst = max(results.values())
    if worst > tol:
        raise SystemExit(f"FAIL: worst residual {worst:.3e} > {tol:.1e}")
    print(f"PASS: worst residual {worst:.3e}")


if __name__ == "__main__":
    main()
