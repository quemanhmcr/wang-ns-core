#!/usr/bin/env python3
from __future__ import annotations
import sympy as sp
x,y,z=sp.symbols('x y z', real=True); r2=x*x+y*y
h=sp.Matrix([-y/r2,x/r2,0])
c=sp.Matrix([1,0,0])
# Divergence-free polynomial probe chosen after an explicit probe-basis falsification pass.
# The earlier rotational probe (-y*z,x*z,0) was a false negative.
w=sp.Matrix([0,0,x])
coords=(x,y,z)
def adv(a,b):
    return sp.Matrix([sum(a[j]*sp.diff(b[i],coords[j]) for j in range(3)) for i in range(3)])
def curl(v):
    return sp.Matrix([sp.diff(v[2],y)-sp.diff(v[1],z),sp.diff(v[0],z)-sp.diff(v[2],x),sp.diff(v[1],x)-sp.diff(v[0],y)])
def div(v):return sum(sp.diff(v[i],coords[i]) for i in range(3))
def comm(a,b):return sp.simplify(adv(a,curl(b))-curl(adv(a,b)))
Eh=sp.simplify(comm(h,w)); Ec=sp.simplify(comm(c,w))
print('harmonic zero-mode signature tribunal')
print('div h =',sp.simplify(div(h)))
print('curl h =',list(map(sp.simplify,curl(h))))
print('circulation density field h nonconstant =',any(sp.diff(h[i],q)!=0 for i in range(3) for q in (x,y)))
print('[D_h,curl]w =',list(Eh))
print('[D_const,curl]w =',list(Ec))
pt={x:sp.Rational(3,2),y:sp.Rational(1,2),z:sp.Rational(4,5)}
val=[sp.N(q.subs(pt),16) for q in Eh]
print('sample annulus-point value =',val)
assert sp.simplify(div(h))==0 and all(sp.simplify(q)==0 for q in curl(h))
assert any(sp.simplify(q)!=0 for q in Eh)
assert all(sp.simplify(q)==0 for q in Ec)
print('PASS: a curl-free topological harmonic circulation can have nonzero mother deformation, while a constant Galilean zero mode is mother-dark; ker(curl) is not the signature gauge kernel')
