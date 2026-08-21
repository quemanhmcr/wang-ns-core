"""Symbolic sanity audit for the NEO contact-action prism.

This checks only the algebraic projection identities.  It is not a PDE theorem.
"""
import sympy as sp

rho, Om, nu = sp.symbols("rho Om nu", nonzero=True)
a = sp.symbols("a")
b1, b2 = sp.symbols("b1 b2")
rho_t = sp.symbols("rho_t")
th1, th2 = sp.symbols("th1 th2")
lap_r, lap_1, lap_2 = sp.symbols("lap_r lap_1 lap_2")

# Radial and tangent projections of D_t(rho n) = rho S n + nu Delta omega.
radial_equation = sp.Eq(rho_t, rho*a + nu*lap_r)
tangent_equations = [
    sp.Eq(rho*th1, rho*b1 + nu*lap_1),
    sp.Eq(rho*th2, rho*b2 + nu*lap_2),
]

alpha = a/Om
gamma = rho_t/(rho*Om)
sigma = -nu*lap_r/(rho*Om)

beta = sp.Matrix([b1/Om, b2/Om])
theta = sp.Matrix([th1/Om, th2/Om])
kappa = sp.Matrix([-nu*lap_1/(rho*Om), -nu*lap_2/(rho*Om)])

radial_residual = sp.simplify((alpha-gamma-sigma).subs(rho_t, rho*a+nu*lap_r))
subs_tan = {
    th1: b1 + nu*lap_1/rho,
    th2: b2 + nu*lap_2/rho,
}
tangent_residual = sp.simplify(beta - theta.subs(subs_tan) - kappa)

print("radial alpha-gamma-sigma =", radial_residual)
print("tangent beta-theta-kappa =", list(tangent_residual))
assert radial_residual == 0
assert tangent_residual == sp.zeros(2, 1)
print("PASS: contact-action prism")
