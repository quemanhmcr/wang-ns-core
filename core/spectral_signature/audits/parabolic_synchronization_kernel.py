#!/usr/bin/env python3
"""Parabolic source-synchronization kernel audit for the Theory-2 endgame.

This audit tests the anti-loop prediction suggested by the Polar--Korn frontier.

1. Kinematic same-output pair synchronization for the *physical logarithmic
   rates* r_k has exactly the affine kernel 1,k_x,k_y,k_z on lattice boxes.
   The quadratic heat invariant has disappeared because it has already been
   calibrated by r_k = eta_k - nu |k|^2.

2. On finite helical windows, restrict synchronization constraints to parent
   pairs whose full Leray vector source is physically nonzero.  The activity
   test uses the exact source zero set from BSVO_FULL_STATE_FRONTIER (20.85):

       q x (p-m) = 0,

   or, for same-helicity parents, |p|=|m|.  Conditional on neither exact null,
   the source is active.  Once the physical interaction category is rich enough
   (R^2 >= 3 in the tested windows), the synchronization kernel is exactly the
   four affine directions.  R^2=2 is retained as a negative control: the
   interaction category is too poor and two extra kernel directions survive.

The physical synchronization matrix has integer entries.  Four affine columns
are annihilated identically, while an exact finite-field rank n-4 proves there
is no further rational/integer kernel on the tested windows.

This is not a Navier--Stokes regularity proof.  It isolates the finite-window
kernel of the parabolic synchronization operator that a final quantitative
Polar--Korn theorem would need to control.
"""
from __future__ import annotations

from collections import defaultdict
import itertools

import numpy as np

PRIME = 1_000_003


def window(R2: int):
    lim = int(np.sqrt(R2)) + 1
    return sorted(
        k
        for k in itertools.product(range(-lim, lim + 1), repeat=3)
        if k != (0, 0, 0) and sum(a * a for a in k) <= R2
    )


def kinematic_collision_matrix(K: int):
    modes = [
        (i, j, k)
        for i in range(-K, K + 1)
        for j in range(-K, K + 1)
        for k in range(-K, K + 1)
        if (i, j, k) != (0, 0, 0)
    ]
    n = len(modes)
    groups = defaultdict(list)
    arr = [np.asarray(k, dtype=int) for k in modes]
    for ia, p in enumerate(arr):
        for ib in range(ia, n):
            q = tuple(p + arr[ib])
            if q != (0, 0, 0):
                groups[q].append((ia, ib))

    L = np.zeros((n, n), dtype=float)
    for pairs in groups.values():
        g = len(pairs)
        if g < 2:
            continue
        B = np.zeros((g, n), dtype=float)
        for row, (ia, ib) in enumerate(pairs):
            B[row, ia] += 1.0
            B[row, ib] += 1.0
        P = np.eye(g) - np.ones((g, g)) / g
        L += (B.T @ P @ B) / g

    eigenvalues = np.linalg.eigvalsh(L)
    nullity = int(np.sum(eigenvalues < 1.0e-9))
    affine = np.asarray([[1.0, *k] for k in modes])
    residual = float(np.linalg.norm(L @ affine, ord=np.inf))
    return len(modes), nullity, float(eigenvalues[nullity]), residual


def full_vector_source_active(p, hp, m, hm):
    """Exact zero/nonzero test from the full Leray-vector source law (20.85)."""
    p = np.asarray(p, dtype=int)
    m = np.asarray(m, dtype=int)
    q = p + m
    r = p - m
    # Collinear shear pole: q x r = 0.
    if np.all(np.cross(q, r) == 0):
        return False
    # Same-helicity equal-radius Beltrami equator.
    if hp == hm and int(np.dot(p, p)) == int(np.dot(m, m)):
        return False
    return True


def physical_sync_rows(R2: int):
    K = window(R2)
    Kset = set(K)
    nodes = [(k, s) for k in K for s in (+1, -1)]
    index = {x: i for i, x in enumerate(nodes)}
    rows = []

    for q in K:
        atoms = []
        for p, hp in nodes:
            m = tuple(np.asarray(q) - np.asarray(p))
            for hm in (+1, -1):
                if m not in Kset:
                    continue
                if index[(p, hp)] > index[(m, hm)]:
                    continue
                if full_vector_source_active(p, hp, m, hm):
                    atoms.append(((p, hp), (m, hm)))
        if len(atoms) < 2:
            continue
        base = atoms[0]
        for atom in atoms[1:]:
            row = {}
            for x in atom:
                j = index[x]
                row[j] = row.get(j, 0) + 1
            for x in base:
                j = index[x]
                row[j] = row.get(j, 0) - 1
            rows.append({j: c for j, c in row.items() if c})
    return nodes, rows


def modular_rank(rows, prime: int = PRIME):
    basis = {}
    for row in rows:
        v = {j: (c % prime) for j, c in row.items() if c % prime}
        while v:
            pivot = min(v)
            if pivot not in basis:
                inv = pow(v[pivot], prime - 2, prime)
                basis[pivot] = {j: (c * inv) % prime for j, c in v.items()}
                break
            b = basis[pivot]
            fac = v[pivot]
            for j, c in b.items():
                nv = (v.get(j, 0) - fac * c) % prime
                if nv:
                    v[j] = nv
                elif j in v:
                    del v[j]
    return len(basis)


def exact_affine_inclusion(nodes, rows):
    for row in rows:
        if sum(row.values()) != 0:
            return False
        for d in range(3):
            if sum(c * nodes[j][0][d] for j, c in row.items()) != 0:
                return False
    return True


def main():
    print("kinematic parabolic same-output kernel")
    for K in (1, 2, 3, 4):
        n, nullity, gap, residual = kinematic_collision_matrix(K)
        assert nullity == 4
        assert residual < 1.0e-9
        print(
            f"K={K} modes={n} nullity={nullity} "
            f"first_positive={gap:.12g} affine_residual={residual:.3e}"
        )

    print("physical full-vector synchronization kernel")
    negative_seen = False
    for R2 in (2, 3, 5, 6):
        nodes, rows = physical_sync_rows(R2)
        rank = modular_rank(rows)
        nullity = len(nodes) - rank
        affine_ok = exact_affine_inclusion(nodes, rows)
        assert affine_ok
        if R2 == 2:
            assert nullity > 4
            negative_seen = True
        else:
            # Four exact affine directions are in the kernel.  A modular rank of
            # n-4 therefore proves the rational/integer incidence rank is n-4.
            assert rank == len(nodes) - 4
        print(
            f"R2={R2} helical_nodes={len(nodes)} rows={len(rows)} "
            f"rank_mod_{PRIME}={rank} nullity={nullity} affine_exact={affine_ok}"
        )
    assert negative_seen
    print(
        "PASS: after physical heat calibration the tested full-vector source "
        "synchronization kernel collapses to the four affine amplitude/translation "
        "directions on every interaction-rich helical window; the deliberately poor "
        "R2=2 window retains extra kernel and serves as a negative control."
    )


if __name__ == "__main__":
    main()
