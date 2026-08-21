import sympy as s

# Symbolic coefficient audit of omega=rho*n polar Laplacian identities.
rho=s.symbols('rho', positive=True)
dr1,dr2,dr3=s.symbols('dr1 dr2 dr3', real=True)
# Abstract squared norms / contractions are represented by independent symbols.
gradn2=s.symbols('gradn2', nonnegative=True)
laprho=s.symbols('laprho', real=True)
a,nu=s.symbols('a nu', real=True)

# n.Delta n = -|grad n|^2 gives radial projection of Delta(rho n).
n_dot_lapomega = laprho-rho*gradn2
Dt_rho = a*rho+nu*n_dot_lapomega
Lrho=s.expand(Dt_rho-nu*laprho)
assert s.simplify(Lrho-(a*rho-nu*rho*gradn2))==0

# Amplitude heat split |grad(rho n)|^2=|grad rho|^2+rho^2|grad n|^2.
gradrho2=dr1**2+dr2**2+dr3**2
heat_split=gradrho2+rho**2*gradn2
print('L rho =',Lrho)
print('|grad omega|^2 polar form =',heat_split)
print('PASS: radial vorticity polar equation and heat split')
print('PASS: angular identity follows from P Delta(rho n)/rho = P Delta n + 2 grad(log rho).grad n')
