#!/usr/bin/env python3
"""Exact rational Bernstein certificate for reciprocal Lemma A.

Certifies, on the full nondegenerate canonical reciprocal domain,

    A^2 + B^2 >= 3 R^2 / 32,

which implies

    Q * chi_geom^2 / |p-p'| >= sqrt(6) / 8.

All positivity checks use exact SymPy rationals.  This is a static geometry
certificate, not a Navier--Stokes regularity proof.
"""

from math import comb

import sympy as sp

S, d, T = sp.symbols("S d T", positive=True, real=True)

# Q=1 normalization and reciprocal parametrization.
P = (S + d) / 2
M = (S - d) / 2
Pp = (T + 1 / S) / 2
Mp = (T - 1 / S) / 2

# The two original reciprocal triad planes are orthogonal.  Cross-orbit input
# dot products are therefore products of their longitudinal components.
zp = (1 + S * d) / 2
zm = (1 - S * d) / 2
zpp = (1 + T / S) / 2
zmm = (1 - T / S) / 2


def G2(A, B, dot, h1, h2):
    """Square of the exact helical geometric coefficient for Q=|a+b|."""
    C2 = sp.factor(A * A + B * B + 2 * dot)
    cross2 = sp.factor(A * A * B * B - dot * dot)
    return sp.factor(
        (h2 * B - h1 * A) ** 2
        * cross2
        * ((h1 * A + h2 * B) ** 2 + C2)
        / (4 * A * A * B * B * C2)
    )


# Four companion source coefficients squared.
g_pp = G2(P, Pp, zp * zpp, 1, 1)
g_mm = G2(M, Mp, zm * zmm, 1, -1)
g_pm = G2(P, Mp, zp * zmm, 1, -1)
g_mp = G2(M, Pp, zm * zpp, 1, 1)

# Original reciprocal aligned pair coefficients squared.
Gss2 = sp.factor(
    d**2 * (S**2 - 1) * (S**2 + 1) * (1 - d**2) / (S**2 - d**2) ** 2
)
Gmix2 = sp.factor(
    T**2 * (S**4 - 1) * (T**2 - 1) / (S**2 * T**2 - 1) ** 2
)

# A and B are product ratios.  These are A^2 and B^2.
A2 = sp.factor(g_pp * g_mm / (Gss2 * Gmix2))
B2 = sp.factor(g_pm * g_mp / (Gss2 * Gmix2))
R2 = S**2 + d**2 - 1

# Target: A^2+B^2 >= 3 R^2/32.
F = sp.together(A2 + B2 - sp.Rational(3, 32) * R2)
num, den = sp.fraction(F)

# Equal-heat reciprocal relation T^2=S^2+d^2-S^{-2}.
rel = S**2 * T**2 - S**4 - S**2 * d**2 + 1
red = sp.rem(sp.Poly(sp.expand(num), T), sp.Poly(rel, T)).as_expr()

# On S>1, T>1, 0<d<1, the denominator is negative because its only sign
# factor is (d-1)(d+1).  Therefore F>=0 iff -red>=0.
signexpr = sp.together(-red)
signnum, signden = sp.fraction(signexpr)
assert sp.factor(signden) == S**4

# signnum is even in S and d.  Put X=S^2, Y=d^2.
X, Y = sp.symbols("X Y", positive=True, real=True)
poly = sp.Poly(sp.expand(signnum), S, d)
PXY = 0
for (i, j), coeff in poly.terms():
    assert i % 2 == 0 and j % 2 == 0
    PXY += coeff * X ** (i // 2) * Y ** (j // 2)
PXY = sp.expand(PXY / 32)  # remove one harmless positive constant

# Compactify by x=1/X=S^{-2}.
x = sp.symbols("x", positive=True, real=True)
degX = sp.degree(PXY, X)
Pbar = sp.expand(x**degX * PXY.subs(X, 1 / x))
assert degX == 17
assert sp.degree(Pbar, Y) == 8


def bernstein_coeffs_2d(poly, xv, yv, xrange, yrange):
    """Exact tensor Bernstein coefficients on a rational rectangle."""
    u, v = sp.symbols("u v")
    a, b = xrange
    c, e = yrange
    p = sp.Poly(
        sp.expand(poly.subs({xv: a + (b - a) * u, yv: c + (e - c) * v})),
        u,
        v,
    )
    nx, ny = p.degree(u), p.degree(v)
    monomial = [
        [sp.Rational(0) for _ in range(ny + 1)] for _ in range(nx + 1)
    ]
    for (i, j), coeff in p.terms():
        monomial[i][j] = coeff

    tmp = [[sp.Rational(0) for _ in range(ny + 1)] for _ in range(nx + 1)]
    for I in range(nx + 1):
        for j in range(ny + 1):
            tmp[I][j] = sum(
                monomial[k][j] * sp.Rational(comb(I, k), comb(nx, k))
                for k in range(I + 1)
            )

    bernstein = [
        [sp.Rational(0) for _ in range(ny + 1)] for _ in range(nx + 1)
    ]
    for I in range(nx + 1):
        for J in range(ny + 1):
            bernstein[I][J] = sum(
                tmp[I][k] * sp.Rational(comb(J, k), comb(ny, k))
                for k in range(J + 1)
            )
    return bernstein


# Chart I: 0<=x<=5/8, 0<=Y<=1.
B1 = bernstein_coeffs_2d(
    Pbar, x, Y, (sp.Rational(0), sp.Rational(5, 8)), (0, 1)
)
v1 = [coeff for row in B1 for coeff in row]
assert all(coeff >= 0 for coeff in v1)

# Chart II: physical condition h=1-x+xY-x^2>0.  On 5/8<=x<1 put
# z=h/(1-x^2), so 0<z<1 and solve for Y.
z = sp.symbols("z", real=True)
Yphys = (x + x**2 - 1 + (1 - x**2) * z) / x
P2 = sp.together(Pbar.subs(Y, Yphys))
P2num, P2den = sp.fraction(P2)
assert sp.factor(P2den) == x**2
B2cert = bernstein_coeffs_2d(
    sp.expand(P2num), x, z, (sp.Rational(5, 8), 1), (0, 1)
)
v2 = [coeff for row in B2cert for coeff in row]
assert all(coeff >= 0 for coeff in v2)

# Sharpness along the deep-fiber / near-Beltrami sequence S=eps^-2, d=eps.
eps = sp.symbols("eps", positive=True)
Sseq = eps**-2
dseq = eps
Tseq = sp.sqrt(Sseq**2 + dseq**2 - Sseq**-2)
D2 = sp.factor(P**2 + Pp**2 - 2 * zp * zpp)  # |p-p'|^2
limA = sp.limit((A2 / D2).subs({S: Sseq, d: dseq, T: Tseq}), eps, 0, dir="+")
limB = sp.limit((B2 / D2).subs({S: Sseq, d: dseq, T: Tseq}), eps, 0, dir="+")
limDR = sp.limit((D2 / R2).subs({S: Sseq, d: dseq, T: Tseq}), eps, 0, dir="+")
assert limA == sp.Rational(3, 32)
assert limB == sp.Rational(3, 32)
assert limDR == sp.Rational(1, 2)

print("PASS reciprocal Lemma A exact rational certificate")
print(
    "chart I: total=%d positive=%d zero=%d"
    % (len(v1), sum(1 for c in v1 if bool(c > 0)), sum(1 for c in v1 if c == 0))
)
print(
    "chart II: total=%d positive=%d zero=%d"
    % (len(v2), sum(1 for c in v2 if bool(c > 0)), sum(1 for c in v2 if c == 0))
)
print("certified: A^2+B^2 >= 3 R^2/32")
print("hence: Q*chi_geom^2/|p-p'| >= sqrt(6)/8")
print("sharpness: equality approached at the deep-fiber / Beltrami corner")
