#!/usr/bin/env python3
"""Nonlinear tribunal for the five-dimensional linearized blind kernel.

The hardest tested non-scalar case (h3 + R3 with curl multiplicity 5+1)
retains a five-dimensional Jacobian kernel after stacking the maximal exterior
curl tower with Jacobi.  This audit builds that kernel directly, then checks
whether finite perturbations inside it remain dark or become visible at higher
nonlinear order.
"""
from __future__ import annotations

import importlib.util
import pathlib
import numpy as np

HERE = pathlib.Path(__file__).parent

def load(name: str, module_name: str):
    path = HERE / name
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

ek = load('ek_exact_lie_reconstruction.py', 'ek')
mx = load('ek_maximal_tower_stabilizer.py', 'mx')
bi = load('ek_bianchi_integrability_completion.py', 'bi')


def abelian(n: int):
    return np.zeros((n, n, n))


def packall(Gs, C):
    fs = mx.forms(Gs, C)
    tower = np.concatenate([mx.pack(fs[p]) for p in range(2, len(Gs) + 1)])
    return np.concatenate([tower, bi.jacvec(Gs)])


def nullspace(A, rtol=1e-8):
    U, s, Vh = np.linalg.svd(A, full_matrices=False)
    r = int(np.sum(s > rtol * (s[0] if len(s) else 1.0)))
    return Vh[r:].T


def setup(seed: int):
    c = ek.direct_sum(ek.heisenberg3(), abelian(3))
    c = ek.randomize_metric(c, seed)
    G = ek.levi_from_structure(c)
    Gs = ek.gamma_mats(G)
    C = np.diag([-1] * 5 + [2])
    E, K, R = ek.EK(Gs, C)
    B = ek.B_from_E(E, C)
    _, _, _, H = ek.vertical_basis(C)
    d, q = len(Gs), len(H)
    x0 = ek.coeffs_vertical(Gs, B, H).reshape(-1)
    s0 = packall(Gs, C)

    h = 2e-6
    cols = []
    for j in range(len(x0)):
        xp, xm = x0.copy(), x0.copy()
        xp[j] += h
        xm[j] -= h
        Gp = ek.from_x(B, H, xp.reshape(d, q))
        Gm = ek.from_x(B, H, xm.reshape(d, q))
        cols.append((packall(Gp, C) - packall(Gm, C)) / (2 * h))
    A = np.column_stack(cols)
    N = nullspace(A)
    return Gs, C, B, H, x0, N, s0


def main():
    print('nonlinear observability on the 5D tower+Jacobi singular kernel')
    slopes = []
    for seed in [13000, 13001]:
        Gs, C, B, H, x0, N, s0 = setup(seed)
        d, q = len(Gs), len(H)
        rr = np.random.default_rng(seed)
        scale = max(np.linalg.norm(s0), 1e-30)
        print('seed', seed, 'Ndim', N.shape[1])
        assert N.shape[1] == 5

        # Along a genuinely first-order blind direction, quadratic visibility
        # should appear as residual ~ t^2 if the nonlinear map is locally
        # separating the perturbation.
        for tr in range(3):
            y = rr.normal(size=5)
            y /= np.linalg.norm(y)
            vals = []
            for t in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3]:
                Gt = ek.from_x(B, H, (x0 + t * N @ y).reshape(d, q))
                res = np.linalg.norm(packall(Gt, C) - s0) / scale
                vals.append((t, res))
            sl = np.polyfit(
                np.log10([a for a, b in vals[:4]]),
                np.log10([b for a, b in vals[:4]]),
                1,
            )[0]
            slopes.append(sl)
            print(' dir', tr, 'slope', sl, 'vals', vals)

        # Random finite sphere scans are not a proof of injectivity, but are a
        # strong collision search: no sampled nonzero perturbation should stay
        # at machine-zero sensor residual.
        for rad in [.02, .05, .1, .2]:
            vals = []
            for _ in range(160):
                y = rr.normal(size=5)
                y *= rad / np.linalg.norm(y)
                Gt = ek.from_x(B, H, (x0 + N @ y).reshape(d, q))
                vals.append(np.linalg.norm(packall(Gt, C) - s0) / scale)
            print(' radius', rad, 'min/median/max', min(vals), np.median(vals), max(vals))
            assert min(vals) > 1e-8 * rad * rad

    print('slopes', slopes)
    assert min(slopes) > 1.7 and max(slopes) < 2.3
    print('PASS: the remaining five infinitesimal blind directions are quadratically visible to the nonlinear maximal-tower+Jacobi map. Random finite scans find no machine-zero collision. High-degeneracy reconstruction is singular at first order but remains strongly consistent with local nonlinear injectivity.')


if __name__ == '__main__':
    main()
