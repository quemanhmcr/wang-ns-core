#!/usr/bin/env python3
"""Canonical periodic audit for the metric-Lie/Hodge NS formation core."""
from __future__ import annotations

import numpy as np

N = 16
TWOPI = 2.0 * np.pi
AXES = (0, 1, 2)


def _kgrid(n: int = N):
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.meshgrid(k, k, k, indexing="ij")


KX, KY, KZ = _kgrid()
KS = (KX, KY, KZ)
K2 = KX * KX + KY * KY + KZ * KZ


def fft(v):
    return np.fft.fftn(v, axes=(0, 1, 2))


def ifft(vh):
    return np.fft.ifftn(vh, axes=(0, 1, 2)).real


def project(v):
    vh = fft(v)
    dot = KX * vh[..., 0] + KY * vh[..., 1] + KZ * vh[..., 2]
    nz = K2 > 0
    for j, kj in enumerate(KS):
        vh[..., j][nz] -= kj[nz] * dot[nz] / K2[nz]
    return ifft(vh)


def lowpass(v, cutoff=2):
    vh = fft(v)
    mask = (np.abs(KX) <= cutoff) & (np.abs(KY) <= cutoff) & (np.abs(KZ) <= cutoff)
    vh *= mask[..., None]
    return ifft(vh)


def random_field(seed: int):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal((N, N, N, 3))
    return project(lowpass(v))


def deriv(v, axis):
    vh = fft(v)
    return ifft((1j * KS[axis])[..., None] * vh)


def lap(v):
    return ifft((-K2)[..., None] * fft(v))


def grad(v):
    # grad[..., i, j] = partial_j v_i
    return np.stack([deriv(v, j) for j in AXES], axis=-1)


def curl(v):
    dv = [deriv(v, j) for j in AXES]
    out = np.empty_like(v)
    out[..., 0] = dv[1][..., 2] - dv[2][..., 1]
    out[..., 1] = dv[2][..., 0] - dv[0][..., 2]
    out[..., 2] = dv[0][..., 1] - dv[1][..., 0]
    return out


def c2(v):
    return curl(curl(v))


def advect(a, b):
    db = [deriv(b, j) for j in AXES]
    out = np.zeros_like(b)
    for j in AXES:
        out += a[..., j, None] * db[j]
    return out


def bracket(a, b):
    return project(advect(a, b) - advect(b, a))


def B(a, b):
    return -0.5 * project(advect(a, b) + advect(b, a))


def J(u, b):
    return project(np.cross(b, curl(u)))


def inner(a, b):
    return float(np.mean(np.sum(a * b, axis=-1)))


def norm(a):
    return float(np.sqrt(max(inner(a, a), 0.0)))


def scaled_residual(a, b, eps=1e-30):
    if np.isscalar(a) and np.isscalar(b):
        return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), 1.0, eps)
    return norm(a - b) / max(norm(a), norm(b), eps)


def metric_defect(a, b, c):
    return inner(bracket(a, b), c) + inner(b, bracket(a, c))


def strain(a):
    A = grad(a)
    return 0.5 * (A + np.swapaxes(A, -1, -2))


def strain_contraction(a, b, c):
    S = strain(a)
    val = np.einsum("...i,...ij,...j->...", b, S, c)
    return float(-2.0 * np.mean(val))


def pressure_source(u):
    A = grad(u)
    grad_mass = np.sum(A * A, axis=(-2, -1))
    omega = curl(u)
    vort_mass = np.sum(omega * omega, axis=-1)
    g_difference = grad_mass - vort_mass
    g_trace = np.einsum("...ij,...ji->...", A, A)
    return g_difference, g_trace


def audit(seed=20260821, nu=0.137):
    u = random_field(seed)
    a = random_field(seed + 1)
    b = random_field(seed + 2)
    c = random_field(seed + 3)

    omega = curl(u)

    # Metric-Lie Riesz / Poisson identity.
    lhs = inner(a, J(u, b))
    rhs = -inner(u, bracket(a, b))
    r_poisson = scaled_residual(lhs, rhs)

    # Formation pencil.
    Lb = J(u, b) - nu * c2(b)
    ell = -inner(u, bracket(a, b)) - nu * inner(curl(a), curl(b))
    r_form = scaled_residual(inner(a, Lb), ell)

    # Diagonal flow equals ordinary projected NS.
    rhs_core = J(u, u) - nu * c2(u)
    rhs_ns = -project(advect(u, u)) + nu * lap(u)
    r_diag = scaled_residual(rhs_core, rhs_ns)

    # Metric non-invariance tensor equals strain contraction.
    r_defect = scaled_residual(metric_defect(a, b, c), strain_contraction(a, b, c))

    # Euler bilinear is the Riesz lift of the metric defect.
    r_B = scaled_residual(inner(a, B(b, c)), -0.5 * metric_defect(a, b, c))

    # Curl is a Killing direction of the Euler product / helicity null.
    killing = metric_defect(omega, u, u)
    killing_scale = max(abs(metric_defect(a, u, u)), abs(metric_defect(b, u, u)), 1.0)
    r_killing = abs(killing) / killing_scale

    # Vortex stretching is another contraction of the same defect tensor.
    S = strain(u)
    Q = float(np.mean(np.einsum("...i,...ij,...j->...", omega, S, omega)))
    Q_def = -0.5 * metric_defect(u, omega, omega)
    r_Q = scaled_residual(Q, Q_def)

    # Local dual-metric difference is exactly tr((grad u)^2), the pressure source.
    g1, g2 = pressure_source(u)
    g_scale = max(float(np.sqrt(np.mean(g1 * g1))), float(np.sqrt(np.mean(g2 * g2))), 1e-30)
    r_g = float(np.sqrt(np.mean((g1 - g2) ** 2))) / g_scale
    mean_g = abs(float(np.mean(g1))) / max(float(np.sqrt(np.mean(g1 * g1))), 1.0)

    results = {
        "poisson_riesz": r_poisson,
        "formation_pencil": r_form,
        "diagonal_ns": r_diag,
        "metric_defect_strain": r_defect,
        "euler_bilinear_riesz": r_B,
        "curl_killing": r_killing,
        "stretching_defect": r_Q,
        "pressure_source_difference": r_g,
        "pressure_source_mean_zero": mean_g,
    }
    return results


def main():
    results = audit()
    tol = 2e-10
    print("metric-Lie/Hodge formation audit")
    for name, value in results.items():
        print(f"{name:32s} {value:.3e}")
    worst = max(results.values())
    if worst > tol:
        raise SystemExit(f"FAIL: worst residual {worst:.3e} > {tol:.1e}")
    print(f"PASS: worst residual {worst:.3e}")


if __name__ == "__main__":
    main()
