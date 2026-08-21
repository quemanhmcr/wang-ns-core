import sympy as s

# Physical second velocity jets T[i,j,k]=d_j d_k u_i are symmetric in (j,k)
# and obey differentiated incompressibility sum_i T[i,i,k]=0.
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

# Exact G3 first jet, n=e3, a=1/3, rho=1.
a=s.Rational(1,3)
rho=s.Integer(1)
d=s.sqrt(2)  # sqrt(9a^2+rho^2)
S=s.diag(-a/2+d/2,-a/2-d/2,a)

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

def domega(B):
    return s.Matrix([B[2,1]-B[1,2], B[0,2]-B[2,0], B[1,0]-B[0,1]])

def carre(T):
    out=0
    for j in range(3):
        B=Bmat(T,j)
        assert s.trace(B)==0
        dS=(B+B.T)/2
        dw=domega(B)
        dn=s.Matrix([dw[0],dw[1],0])/rho
        da=dS[2,2]
        out += (24*a*a*dn.dot(dn)
                -48*a*dn.dot(dS[:,2])
                -24*a*dn.dot(S*dn)
                -12*da*da
                +2*s.trace(B*B))
    return s.factor(out)

# Integer nullspace coefficients found by adversarial search, then frozen here.
pos_coeff=[0,-1,1,-2,-2,2,-2,0,2,-2,2,-1,-2,-2,1]
neg_coeff=[1,2,1,0,0,-1,-1,-1,-2,2,0,2,1,0,1]
pos=carre(build(pos_coeff))
neg=carre(build(neg_coeff))
assert s.simplify(pos-(36-24*s.sqrt(2)))==0
assert s.simplify(neg+96)==0
assert pos>0 and neg<0

print('physical second-jet nullity =',len(Z))
print('positive G3 carre example =',pos)
print('negative G3 carre example =',neg)
print('PASS: L delta first-gradient carre is sign-indefinite on physical Hessian-compatible divergence-free jets')
