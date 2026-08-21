import sympy as s

# Curl frame n=e3.  D is the tangent trace-free strain block and rho is curl amplitude.
a,b1,b2,d1,d2,rho=s.symbols('a b1 b2 d1 d2 rho', real=True)
S=s.Matrix([
    [-a/s.Integer(2)+d1, d2, b1],
    [d2, -a/s.Integer(2)-d1, b2],
    [b1,b2,a],
])
R=s.Matrix([[0,-rho/s.Integer(2),0],[rho/s.Integer(2),0,0],[0,0,0]])
A=S+R
b=s.Matrix([b1,b2])
D=s.Matrix([[d1,d2],[d2,-d1]])

g=s.expand(s.trace(A*A))
delta=s.expand(6*a*a-g)
r=s.expand(s.trace(A*A*A))
r_claim=s.expand(-6*a**3+s.Rational(9,2)*a*b.dot(b)+3*b.dot(D*b)+s.Rational(3,2)*a*delta)
assert s.simplify(r-r_claim)==0

# Restricted/local Riccati matrix ODE.
At=s.simplify(-A*A+g/s.Integer(3)*s.eye(3))
St=s.simplify((At+At.T)/2)
Rt=s.simplify((At-At.T)/2)
n=s.Matrix([0,0,1])
P=s.diag(1,1,0)
nt=s.Matrix([b1,b2,0])  # omega_t=S omega => n_t=b in the no-heat model
at=s.expand((nt.T*S*n)[0]+(n.T*St*n)[0]+(n.T*S*nt)[0])
bt=s.simplify(P*(St*n+S*nt-at*n-a*nt))
for i in range(2):
    assert s.simplify(bt[i]+2*a*b[i])==0

gt=s.expand(2*s.trace(A*At))
deltat=s.expand(12*a*at-gt)
qdelta=s.expand(21*a*b.dot(b)+6*b.dot(D*b)-a*delta)
assert s.simplify(deltat-qdelta)==0

# Aligned b=0 discriminant bridge.
r0=s.simplify(r.subs({b1:0,b2:0}))
g0=s.simplify(g.subs({b1:0,b2:0}))
d0=s.simplify(delta.subs({b1:0,b2:0}))
V0=s.factor(r0**2-g0**3/s.Integer(6))
assert s.simplify(V0-d0**2*(2*d0-9*a**2)/12)==0

# Closed aligned (a,delta) system and exact first integral.
y=s.symbols('y', real=True)
ap=a**2-y/s.Integer(3)
yp=-a*y
I=y**2*(2*y-9*a**2)
assert s.simplify(s.diff(I,a)*ap+s.diff(I,y)*yp)==0

print('PASS: cubic curl-frame factorization')
print('PASS: restricted Riccati tangent defect rate P D_t b = -2 a b')
print('PASS: restricted Riccati gain defect rate D_t delta = 21 a |b|^2 + 6 b.Db - a delta')
print('PASS: aligned discriminant V = delta^2 (2 delta - 9 a^2) / 12')
print('PASS: aligned first integral delta^2 (2 delta - 9 a^2)')
print('G3 normal linear rates: -2a, -2a, -a')
