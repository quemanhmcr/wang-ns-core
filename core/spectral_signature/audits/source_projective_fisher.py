#!/usr/bin/env python3
"""Exact finite-dimensional audit of the source-projective Fisher identity.

For an existing edge-source field f_e with multiplicative physical rate
    dot f_e = lambda_e f_e,
the Fubini--Study/projective speed of f is exactly the pair-rate variance
    Var_mu(lambda) = 1/2 int int |lambda-lambda'|^2 dmu dmu',
where dmu=|f|^2/||f||^2.

Writing lambda = eta_pair - nu*kappa gives the heat-normal identity
    d/dt mean_mu(kappa) + 2 nu Var_mu(kappa)
      = 2 Re Cov_mu(kappa, eta_pair).

The same variables also give the scale-critical logarithmic migration identity
    d/dt log(mean_mu(kappa))
      = 2 Re Cov_mu(kappa, lambda) / mean_mu(kappa),
and therefore
    |d/dt log(mean_mu(kappa))|
      <= [Var_mu(kappa)+Var_mu(lambda)]/mean_mu(kappa).

These are algebraic identities for the already-existing physical source field;
they are not a regularity estimate and do not assign a new finite budget.
"""
from __future__ import annotations

import numpy as np

rng = np.random.default_rng(202608221412)


def weighted_stats(f, z):
    w = np.abs(f) ** 2
    M = float(np.sum(w))
    mu = w / M
    mean = np.sum(mu * z)
    var = float(np.sum(mu * np.abs(z) ** 2) - np.abs(mean) ** 2)
    return mu, mean, var


def main():
    max_fisher = 0.0
    max_pair = 0.0
    max_heat = 0.0
    max_split = 0.0
    max_log = 0.0
    max_log_violation = 0.0
    for n in (3, 5, 11, 29):
        for _ in range(100):
            f = rng.normal(size=n) + 1j * rng.normal(size=n)
            # Avoid an accidental tiny norm.
            f += (0.3 + 0.2j)
            eta = rng.normal(size=n) + 1j * rng.normal(size=n)
            kappa = 0.2 + rng.random(size=n) * 7.0
            nu = 0.1 + rng.random() * 1.7
            lam = eta - nu * kappa

            mu, mean_lam, var_lam = weighted_stats(f, lam)
            M = float(np.sum(np.abs(f) ** 2))
            fdot = lam * f

            # Complex projective/Fubini--Study numerator.
            lhs_num = M * float(np.vdot(fdot, fdot).real) - abs(np.vdot(f, fdot)) ** 2
            rhs_num = M * M * var_lam
            err = abs(lhs_num - rhs_num) / max(1.0, abs(rhs_num))
            max_fisher = max(max_fisher, err)

            pair = 0.0
            for i in range(n):
                for j in range(n):
                    pair += 0.5 * mu[i] * mu[j] * abs(lam[i] - lam[j]) ** 2
            err = abs(pair - var_lam) / max(1.0, abs(var_lam))
            max_pair = max(max_pair, err)

            # Heat-normal identity.  The normalized source weights obey
            # mu_dot = 2 (Re lambda - mean Re lambda) mu.
            kbar = float(np.sum(mu * kappa))
            mudot = 2.0 * (np.real(lam) - float(np.sum(mu * np.real(lam)))) * mu
            kbar_dot = float(np.sum(mudot * kappa))
            kvar = float(np.sum(mu * (kappa - kbar) ** 2))
            etabar = np.sum(mu * eta)
            cov_k_eta = np.sum(mu * (kappa - kbar) * (eta - etabar))
            rhs = 2.0 * float(np.real(cov_k_eta)) - 2.0 * nu * kvar
            err = abs(kbar_dot - rhs) / max(1.0, abs(rhs))
            max_heat = max(max_heat, err)

            # Tangent/normal variance split for lambda=eta-nu*kappa.
            _, _, var_eta = weighted_stats(f, eta)
            cov_eta_k = np.sum(mu * (eta - etabar) * (kappa - kbar))
            split = var_eta + nu * nu * kvar - 2.0 * nu * float(np.real(cov_eta_k))
            err = abs(var_lam - split) / max(1.0, abs(var_lam))
            max_split = max(max_split, err)

            # Scale-critical logarithmic source-heat migration.
            cov_k_lam = np.sum(mu * (kappa - kbar) * (lam - mean_lam))
            logdot_cov = 2.0 * float(np.real(cov_k_lam)) / kbar
            logdot_direct = kbar_dot / kbar
            err = abs(logdot_cov - logdot_direct) / max(1.0, abs(logdot_direct))
            max_log = max(max_log, err)
            critical_action_density = (kvar + var_lam) / kbar
            max_log_violation = max(
                max_log_violation, abs(logdot_direct) - critical_action_density
            )

    assert max_fisher < 2e-12
    assert max_pair < 2e-12
    assert max_heat < 2e-12
    assert max_split < 2e-12
    assert max_log < 2e-12
    assert max_log_violation < 2e-12
    print(f"PASS source projective Fisher numerator: max relerr {max_fisher:.3e}")
    print(f"PASS pair-rate variance identity: max relerr {max_pair:.3e}")
    print(f"PASS source heat-normal identity: max relerr {max_heat:.3e}")
    print(f"PASS tangent/normal variance split: max relerr {max_split:.3e}")
    print(f"PASS logarithmic heat migration identity: max relerr {max_log:.3e}")
    print(
        "PASS scale-critical log-speed bound: "
        f"max violation {max_log_violation:.3e}"
    )


if __name__ == "__main__":
    main()
