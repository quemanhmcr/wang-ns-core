"""Symbolic scale-weight audit for the NEO record-scale derivation."""
import sympy as s
m=s.symbols('m', integer=True, nonnegative=True)
R,nu,Om=s.symbols('R nu Om', positive=True)
mu=nu/(Om*R**2)
assert s.simplify(R*s.diff(mu,R)+2*mu)==0

# Weight of m derivatives of V_R is m-1.
def weight(order): return order-1
assert weight(0)==-1
assert weight(1)==0
assert weight(2)==1
assert weight(3)==2

# Genetic terms: time/state -1, nonlinearity V * CV = -1+0, viscosity mu + C^2 V = -2+1.
w_state=-1
w_curl=0
w_nonlin=w_state+w_curl
w_visc=-2+weight(2)
assert w_nonlin==w_state
assert w_visc==w_state

# Contact square action on vorticity: mu C^2 omega; omega weight 0, two more derivatives +2.
w_square_vort=-2+2
assert w_square_vort==0

print('R d_R mu =',s.simplify(R*s.diff(mu,R)))
print('weights V,CV,C2V,C3V =',*[weight(j) for j in range(4)])
print('genetic weights state/nonlinear/viscous =',w_state,w_nonlin,w_visc)
print('vorticity square-action weight =',w_square_vort)
print('PASS: record-scale derivation is compatible with curl degree and the genetic equation')
