#!/usr/bin/env python3
"""Finite-dimensional sign/scaling audit for the UV-conveyor note.

Checks:
1. antisymmetric spectral current and the 1/4 current-gap formula;
2. the critical dilation coefficient vanishes at sigma=1/2;
3. ordinary dyadic weights are only a surrogate for the exact Lambda stock.
"""

import numpy as np


def relerr(a, b):
    return abs(a - b) / max(1.0, abs(a), abs(b))


def current_audit(seed=7, n=9):
    rng = np.random.default_rng(seed)
    roots = np.sort(rng.uniform(0.3, 5.0, size=n))
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    gamma = z - z.conj().T
    u = rng.normal(size=n) + 1j * rng.normal(size=n)

    J = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            J[i, j] = 2.0 * np.real(np.conj(u[i]) * gamma[i, j] * u[j])

    anti = np.max(np.abs(J + J.T))
    N = -(gamma @ u)
    lhs = np.real(np.vdot(N, roots * u))
    rhs = 0.25 * np.sum((roots[None, :] - roots[:, None]) * J)
    assert anti < 1e-11
    assert relerr(lhs, rhs) < 1e-11
    return anti, relerr(lhs, rhs)


def scaling_audit():
    # Dilation contribution to (1/2)d||U||_{H^sigma}^2/ds is
    # beta*(2*sigma-1)/2 times the stock on the left-hand side convention.
    def coeff(sigma):
        return (2.0 * sigma - 1.0) / 2.0

    assert abs(coeff(0.5)) < 1e-15
    assert abs(coeff(0.0) + 0.5) < 1e-15
    assert abs(coeff(1.0) - 0.5) < 1e-15
    return coeff(0.5)


def dyadic_surrogate_audit():
    # Two radii in one octave: exact Lambda stock distinguishes them,
    # a piecewise-constant dyadic weight does not.
    radii = np.array([1.05, 1.90])
    mass = np.array([1.0, 1.0])
    exact = np.sum(radii * mass)
    dyadic = 1.0 * np.sum(mass)
    assert abs(exact - dyadic) > 0.5
    return exact, dyadic


if __name__ == "__main__":
    anti, current_err = current_audit()
    critical_coeff = scaling_audit()
    exact, dyadic = dyadic_surrogate_audit()
    print(f"PASS spectral-current antisymmetry: {anti:.3e}")
    print(f"PASS current-gap identity: relerr={current_err:.3e}")
    print(f"PASS critical dilation coefficient: {critical_coeff:.1f}")
    print(f"PASS dyadic-surrogate warning: exact={exact:.3f}, surrogate={dyadic:.3f}")
