#!/usr/bin/env python3
"""Canonical domain/topology audit for the typed Hodge/de Rham core."""
from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import leggauss


def cell_complex(nx=6, ny=6, holes=()):
    nodes = [(i, j) for j in range(ny + 1) for i in range(nx + 1)]
    node_id = {p: k for k, p in enumerate(nodes)}

    edges = []
    # horizontal, then vertical; orientation right/up
    for j in range(ny + 1):
        for i in range(nx):
            edges.append(((i, j), (i + 1, j)))
    for j in range(ny):
        for i in range(nx + 1):
            edges.append(((i, j), (i, j + 1)))
    edge_id = {e: k for k, e in enumerate(edges)}

    d0 = np.zeros((len(edges), len(nodes)))
    for e, (a, b) in enumerate(edges):
        d0[e, node_id[a]] = -1.0
        d0[e, node_id[b]] = 1.0

    hole_set = set(holes)
    faces = [(i, j) for j in range(ny) for i in range(nx) if (i, j) not in hole_set]
    d1 = np.zeros((len(faces), len(edges)))

    def oriented_edge(a, b):
        if (a, b) in edge_id:
            return edge_id[(a, b)], 1.0
        return edge_id[(b, a)], -1.0

    def boundary_vec(i, j):
        v = np.zeros(len(edges))
        loop = [((i, j), (i + 1, j)), ((i + 1, j), (i + 1, j + 1)),
                ((i + 1, j + 1), (i, j + 1)), ((i, j + 1), (i, j))]
        for a, b in loop:
            idx, s = oriented_edge(a, b)
            v[idx] += s
        return v

    for r, (i, j) in enumerate(faces):
        d1[r] = boundary_vec(i, j)

    return d0, d1, boundary_vec


def hodge_nullity(holes):
    d0, d1, boundary_vec = cell_complex(holes=holes)
    chain = np.linalg.norm(d1 @ d0)
    lap1 = d0 @ d0.T + d1.T @ d1
    evals, evecs = np.linalg.eigh(lap1)
    tol = 1e-10
    idx = np.where(evals < tol)[0]
    nullity = len(idx)
    harmonic = evecs[:, idx] if nullity else np.empty((lap1.shape[0], 0))
    closed = np.linalg.norm(d1 @ harmonic) if nullity else 0.0
    coclosed = np.linalg.norm(d0.T @ harmonic) if nullity else 0.0
    periods = []
    for hole in holes:
        bv = boundary_vec(*hole)
        periods.append(bv @ harmonic if nullity else np.array([]))
    return chain, nullity, closed, coclosed, np.array(periods)


def mode(params, x, y, z):
    m, n, p, A, B, C = params
    return np.stack([
        A * np.sin(m*x) * np.cos(n*y) * np.cos(p*z),
        B * np.cos(m*x) * np.sin(n*y) * np.cos(p*z),
        C * np.cos(m*x) * np.cos(n*y) * np.sin(p*z),
    ], axis=-1)


def curl_mode(params, x, y, z):
    m, n, p, A, B, C = params
    return np.stack([
        (p*B - n*C) * np.cos(m*x) * np.sin(n*y) * np.sin(p*z),
        (m*C - p*A) * np.sin(m*x) * np.cos(n*y) * np.sin(p*z),
        (n*A - m*B) * np.sin(m*x) * np.sin(n*y) * np.cos(p*z),
    ], axis=-1)


def gl_nodes(order=14):
    t, w = leggauss(order)
    x = 0.5 * np.pi * (t + 1.0)
    w = 0.5 * np.pi * w
    return x, w


def volume_inner(a, b, order=14):
    x, w = gl_nodes(order)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    W = w[:, None, None] * w[None, :, None] * w[None, None, :]
    av = a(X, Y, Z)
    bv = b(X, Y, Z)
    return float(np.sum(W * np.sum(av * bv, axis=-1)))


def boundary_pair(a, b, order=18):
    x, w = gl_nodes(order)
    total = 0.0
    # Each tuple: fixed axis, fixed coordinate, outward normal.
    faces = [(0, 0.0, np.array([-1., 0., 0.])), (0, np.pi, np.array([1., 0., 0.])),
             (1, 0.0, np.array([0., -1., 0.])), (1, np.pi, np.array([0., 1., 0.])),
             (2, 0.0, np.array([0., 0., -1.])), (2, np.pi, np.array([0., 0., 1.]))]
    U, V = np.meshgrid(x, x, indexing="ij")
    W2 = w[:, None] * w[None, :]
    for axis, val, normal in faces:
        coords = [None, None, None]
        free = [j for j in range(3) if j != axis]
        coords[axis] = np.full_like(U, val)
        coords[free[0]] = U
        coords[free[1]] = V
        av = a(*coords)
        bv = b(*coords)
        integrand = np.einsum("i,...i->...", normal, np.cross(av, bv))
        total += float(np.sum(W2 * integrand))
    return total


def boundary_green_audit():
    # Two divergence-free tangent modes; coefficients satisfy mA+nB+pC=0.
    candidates = []
    for m, n, p in [(1,1,1), (1,2,1), (2,1,1), (1,1,2), (2,2,1)]:
        candidates.append((m,n,p, float(n), float(-m), 0.0))
        candidates.append((m,n,p, float(p), 0.0, float(-m)))
    best = None
    for i, pa in enumerate(candidates):
        for pb in candidates[i+1:]:
            a = lambda x,y,z, p=pa: mode(p,x,y,z)
            b = lambda x,y,z, p=pb: mode(p,x,y,z)
            ca = lambda x,y,z, p=pa: curl_mode(p,x,y,z)
            cb = lambda x,y,z, p=pb: curl_mode(p,x,y,z)
            defect = volume_inner(ca, b) - volume_inner(a, cb)
            boundary = boundary_pair(a, b)
            magnitude = max(abs(defect), abs(boundary))
            if best is None or magnitude > best[0]:
                best = (magnitude, defect, boundary)
    _, defect, boundary = best
    residual = abs(defect - boundary) / max(abs(defect), abs(boundary), 1.0)
    return residual, defect, boundary


def main():
    cases = [([], 0), ([(2,2)], 1), ([(1,2),(4,3)], 2)]
    worst = 0.0
    print("typed Hodge/de Rham domain-topology audit")
    for holes, expected in cases:
        chain, nullity, closed, coclosed, periods = hodge_nullity(holes)
        print(f"holes={len(holes)} nullity={nullity} chain={chain:.2e} closed={closed:.2e} coclosed={coclosed:.2e}")
        if nullity != expected:
            raise SystemExit(f"FAIL: expected b1={expected}, observed {nullity}")
        worst = max(worst, chain, closed, coclosed)
        if holes and np.linalg.matrix_rank(periods, tol=1e-8) != expected:
            raise SystemExit("FAIL: harmonic period map does not resolve the hole classes")

    r_boundary, defect, boundary = boundary_green_audit()
    print(f"boundary Green defect={defect:.12g} boundary={boundary:.12g} residual={r_boundary:.3e}")
    worst = max(worst, r_boundary)
    tol = 5e-10
    if worst > tol:
        raise SystemExit(f"FAIL: worst residual {worst:.3e} > {tol:.1e}")
    print(f"PASS: worst residual {worst:.3e}")


if __name__ == "__main__":
    main()
