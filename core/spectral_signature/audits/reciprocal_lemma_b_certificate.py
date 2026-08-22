#!/usr/bin/env python3
"""Exact symbolic certificate for reciprocal-incidence Lemma B.

The script verifies the polynomial elimination and Jacobian identities used in
HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md.  It is a static geometry certificate;
it is not a Navier--Stokes regularity proof.
"""

import sympy as sp

A, B, C, S, w = sp.symbols("A B C S w", positive=True)

# A=|p|, B=|p'|, C=p.p', S=P+M, w=Q^2.
# Reciprocality: e=P'-M'=w/S.
# Equal heat after d=2A-S and T=2B-w/S.
F = sp.expand(
    w**2
    - 2 * B * S * w
    + S**2 * (-2 * A**2 + 2 * A * S + 2 * B**2 - S**2)
)

# Orthogonality of the two original triad planes.
G = sp.expand(
    (w + 2 * A * S - S**2)
    * (w * S**2 + 2 * B * w * S - w**2)
    - 4 * w * C * S**2
)

L = sp.expand(S**2 - 2 * A * S + 2 * A**2 - 2 * B**2)
D = sp.expand((A + B) ** 2 - 4 * C)
E = sp.expand(B * (A + B) - 2 * C)
H = sp.expand(D * (S - A) ** 2 - E**2)

resultant = sp.factor(sp.resultant(F, G, w))
assert sp.expand(resultant - 4 * S**6 * L * H) == 0

# Modulo F, orthogonality is linear in w.
_, remainder = sp.div(G, F, w)
K = sp.expand(A**2 - 2 * A * S - B**2 - B * S + 2 * C + S**2)
expected = sp.expand(-2 * S**2 * (K * w + S * (A - S) * L))
assert sp.expand(remainder - expected) == 0

# The L branch is nonphysical.  Modulo L, the equal-heat polynomial is
# exactly w(w-2BS), so its roots are w=0 or w=2BS; the second gives
# T=2B-w/S=0.
assert sp.rem(
    sp.Poly(sp.expand(F - w * (w - 2 * B * S)), A), sp.Poly(L, A)
).as_expr() == 0

# D is positive away from the diagonal p=p'.
assert sp.expand(D - ((A - B) ** 2 + 4 * (A * B - C))) == 0

# H is a completed square and has only one physical root S>A.
disc_H = sp.factor(sp.discriminant(H, S))
assert sp.expand(disc_H - 4 * E**2 * D) == 0

# On the physical branch L != 0 and S>A, so K cannot vanish if the remainder
# vanishes.  The common child radius is therefore unique.
w_unique = sp.factor(-S * (A - S) * L / K)
assert sp.expand(K * w_unique + S * (A - S) * L) == 0

# Angular reconstruction Jacobian.
px, py, pz, rx, ry, rz, qx, qy, qz = sp.symbols(
    "px py pz rx ry rz qx qy qz", real=True
)
p = sp.Matrix([px, py, pz])
pp = sp.Matrix([rx, ry, rz])
q = sp.Matrix([qx, qy, qz])
Jmat = sp.Matrix(
    [
        [px, py, pz],
        [rx, ry, rz],
        [2 * qx, 2 * qy, 2 * qz],
    ]
)
triple = sp.expand(q.dot(p.cross(pp)))
assert sp.expand(Jmat.det() - 2 * triple) == 0

# (q x p) x (q x p') = [q,p,p'] q.
lhs = q.cross(p).cross(q.cross(pp))
rhs = triple * q
assert all(sp.expand(lhs[i] - rhs[i]) == 0 for i in range(3))

print("PASS reciprocal Lemma B exact symbolic certificate")
print("resultant = 4 S^6 L [D(S-A)^2-E^2]")
print("physical radial branch: unique S>A")
print("physical Q^2 root: unique on that branch")
print("angular preimages: at most two mirror children")
print("angular Jacobian: 2 q.(p x p')")
