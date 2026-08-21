import sympy as s

# Physical Hessian-compatible divergence-free second velocity jets.
vars=[]
for i in range(3):
    for j in range(3):
        for k in range(j,3):
            vars.append((i,j,k))
C=s.zeros(3,len(vars))
for kk in range(3):
    for q,(i,j,k) in enumerate(vars):
        if (j,k)==(min(i,kk),max(i,kk)):
            C[kk,q]=1
Z=C.nullspace()
assert len(Z)==15

a=s.Rational(1,3)
rho=s.Integer(1)
d=s.sqrt(2)
S=s.diag(-a/2+d/2,-a/2-d/2,a)
R=s.Matrix([[0,-rho/2,0],[rho/2,0,0],[0,0,0]])
A=S+R
g=s.simplify(s.trace(A*A))
r=s.simplify(s.trace(A*A*A))
assert s.simplify(g-6*a*a)==0
assert s.simplify(r+6*a**3)==0

def build(coeff):
    x=s.zeros(len(vars),1)
    for c,z in zip(coeff,Z): x += c*z
    T=[[[s.Integer(0) for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for val,(i,j,k) in zip(x,vars):
        T[i][j][k]=val
        T[i][k][j]=val
    return T

def Bmat(T,j):
    return s.Matrix([[T[i][k][j] for k in range(3)] for i in range(3)])

def carre(T):
    out=0
    for j in range(3):
        B=Bmat(T,j)
        assert s.trace(B)==0
        dg=2*s.trace(A*B)
        dr=3*s.trace(A*A*B)
        out += (-12*r*s.trace(A*B*B)
                +g**2*s.trace(B*B)
                -2*dr**2
                +g*dg**2)
    return s.factor(out)

pos_coeff=[1,2,1,1,2,2,-1,-1,2,1,2,-1,-2,1,0]
neg_coeff=[2,2,-1,-2,0,-1,1,0,2,2,-1,2,-2,-2,1]
pos=carre(build(pos_coeff))
neg=carre(build(neg_coeff))
assert s.simplify(pos-s.Rational(2,3)*(38-13*s.sqrt(2)))==0
assert s.simplify(neg+(13+12*s.sqrt(2))/6)==0
assert pos>0 and neg<0

# Restricted Riccati scalar-invariant cancellation.
gs,rs=s.symbols('g r', real=True)
gt=-2*rs
rt=-gs**2/s.Integer(2)
V=rs**2-gs**3/s.Integer(6)
assert s.simplify(s.diff(V,gs)*gt+s.diff(V,rs)*rt)==0

print('PASS: restricted Riccati discriminant derivative is exactly zero')
print('physical second-jet nullity =',len(Z))
print('positive discriminant carre =',pos)
print('negative discriminant carre =',neg)
print('PASS: parabolic discriminant carre is sign-indefinite on physical second jets')
