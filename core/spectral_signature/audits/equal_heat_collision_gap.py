#!/usr/bin/env python3
"""Finite-lattice audit of the equal-heat diamond collision kernel.

For all nonzero lattice modes in |k_i|<=K, group unordered pairs by the same
momentum sum q and the same pair heat |p|^2+|m|^2.  On every group, measure the
variance of the pair sum eta_p+eta_m around its group mean.  This gives a
canonical positive semidefinite collision quadratic form, independent of a
chosen spanning tree of diamond relations.

The exact collision invariants 1,k_x,k_y,k_z,|k|^2 are always in the kernel.
This audit checks whether extra zero/soft modes appear for K=1,2,3.

This is an audit, not a continuum spectral-gap theorem.
"""

from collections import defaultdict

import numpy as np


def collision_gap(K: int):
    modes = [
        (i, j, k)
        for i in range(-K, K + 1)
        for j in range(-K, K + 1)
        for k in range(-K, K + 1)
        if (i, j, k) != (0, 0, 0)
    ]
    n = len(modes)
    groups = defaultdict(list)

    for ia, p in enumerate(modes):
        pa = np.asarray(p, dtype=int)
        for ib in range(ia, n):
            m = modes[ib]
            q = tuple(pa + np.asarray(m, dtype=int))
            if q == (0, 0, 0):
                continue
            heat = sum(x * x for x in p) + sum(x * x for x in m)
            groups[(q, heat)].append((ia, ib))

    L = np.zeros((n, n), dtype=float)
    relation_dimension = 0
    active_groups = 0

    for pairs in groups.values():
        g = len(pairs)
        if g < 2:
            continue
        active_groups += 1
        relation_dimension += g - 1

        # B sends modal values eta to pair sums eta_p+eta_m on this fiber.
        B = np.zeros((g, n), dtype=float)
        for row, (ia, ib) in enumerate(pairs):
            B[row, ia] += 1.0
            B[row, ib] += 1.0

        # Canonical group-variance quadratic form:
        # (1/g) sum_i |s_i - mean(s)|^2.
        P = np.eye(g) - np.ones((g, g)) / g
        L += (B.T @ P @ B) / g

    eigenvalues = np.linalg.eigvalsh(L)
    tol = 1.0e-9
    nullity = int(np.sum(eigenvalues < tol))
    gap = float(eigenvalues[nullity])

    invariants = np.asarray(
        [[1.0, *k, float(sum(x * x for x in k))] for k in modes]
    )
    invariant_rank = int(np.linalg.matrix_rank(invariants, tol=tol))

    # Exact inclusion check at floating arithmetic level: the canonical
    # collision quadratic annihilates the five known invariants to roundoff.
    residual = float(np.linalg.norm(L @ invariants, ord=np.inf))

    return {
        "K": K,
        "modes": n,
        "active_groups": active_groups,
        "relation_dimension": relation_dimension,
        "nullity": nullity,
        "invariant_rank": invariant_rank,
        "invariant_residual": residual,
        "gap": gap,
    }


def main():
    rows = [collision_gap(K) for K in (1, 2, 3)]
    for row in rows:
        assert row["nullity"] == 5
        assert row["invariant_rank"] == 5
        assert row["invariant_residual"] < 1.0e-9
        print(
            "K={K} modes={modes} groups={active_groups} rel_dim={relation_dimension} "
            "nullity={nullity} invariants={invariant_rank} residual={invariant_residual:.3e} "
            "first_positive={gap:.12g}".format(**row)
        )
    print("PASS canonical equal-heat collision-kernel audit")


if __name__ == "__main__":
    main()
