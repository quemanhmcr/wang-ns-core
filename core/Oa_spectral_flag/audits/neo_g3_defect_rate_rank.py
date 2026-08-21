"""Linear-algebra audit of G3 normal forcing -> minimal defect creation rates.

At a G3A contact the active Type-I compiler gives
    D_t b = P_perp Z n,
    D_t delta = d * (W_lambda : Z),
for a symmetric trace-free correction Z.
This audit checks that these three scalar rates are algebraically independent.
It does NOT assert that every Z is realized by a genuine global NS solution.
"""
import sympy as sp

lam, rho = sp.symbols('lam rho', positive=True)
d = sp.sqrt(9*lam**2 + rho**2)

# n=e3, tangent basis e1,e2. Symmetric trace-free Z coordinates:
# Z=[[z11,z12,z13],[z12,z22,z23],[z13,z23,-z11-z22]]
z11,z22,z12,z13,z23 = sp.symbols('z11 z22 z12 z13 z23')
Z = sp.Matrix([[z11,z12,z13],[z12,z22,z23],[z13,z23,-z11-z22]])

# E0=n⊗n - 1/2 P_perp = diag(-1/2,-1/2,1)
# E2=e1⊗e1-e2⊗e2 = diag(1,-1,0)
E0 = sp.diag(sp.Rational(-1,2),sp.Rational(-1,2),1)
E2 = sp.diag(1,-1,0)
W = (6*lam/d)*E0 - E2
fro = lambda A,B: sp.trace(A.T*B)

rates = sp.Matrix([
    z13,
    z23,
    sp.simplify(d*fro(W,Z)),
])
vars_ = sp.Matrix([z11,z22,z12,z13,z23])
J = rates.jacobian(vars_)

print('rate map [Dtb1,Dtb2,Dtdelta] =')
sp.pprint(rates)
print('Jacobian rank =', J.rank())
print('Jacobian =')
sp.pprint(J)
assert J.rank() == 3

# Exhibit independent controls.
for label, sub in [
    ('mixed-1',{z13:1,z23:0,z11:0,z22:0,z12:0}),
    ('mixed-2',{z13:0,z23:1,z11:0,z22:0,z12:0}),
    ('shape',{z13:0,z23:0,z11:1,z22:1,z12:0}),
]:
    r=sp.simplify(rates.subs(sub))
    print(label, list(r))

print('PASS: G3 normal forcing has three independent minimal-defect rate directions')
