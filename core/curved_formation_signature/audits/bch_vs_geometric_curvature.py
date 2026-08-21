#!/usr/bin/env python3
from __future__ import annotations
import sys,numpy as np
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'metric_lie_hodge'/'audits'))
import formation_core_audit as f

def nabla(a,b):return f.project(f.advect(a,b))
def B(a,b):return -.5*(nabla(a,b)+nabla(b,a))
def C2(a):return f.c2(a)
def L(a):return -C2(a)
def Q(a,b):return L(B(a,b))-B(L(a),b)-B(a,L(b))
def M(a,w):return nabla(a,f.curl(w))-f.curl(nabla(a,w))
def commC2(a,w):return M(a,f.curl(w))+f.curl(M(a,w))
def J(u,b):return f.J(u,b)
def Kp(u,b):return f.curl(J(u,b))-J(u,f.curl(b)) # [C,J_u]
def R(a,b,w):return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(f.bracket(a,b),w)
def Kg(a,b,w):return R(a,b,f.curl(w))-f.curl(R(a,b,w))
def rel(a,b):return f.norm(a-b)/max(f.norm(a),f.norm(b),1e-30)
def unit(x):return x/max(f.norm(x),1e-30)
def beltrami():
 z=np.arange(f.N)*2*np.pi/f.N;Z=np.broadcast_to(z,(f.N,f.N,f.N));u=np.zeros((f.N,f.N,f.N,3));u[...,0]=np.sin(Z);u[...,1]=np.cos(Z);return unit(u)
def shear():
 z=np.arange(f.N)*2*np.pi/f.N;Z=np.broadcast_to(z,(f.N,f.N,f.N));u=np.zeros((f.N,f.N,f.N,3));u[...,0]=np.sin(Z)+.3*np.sin(2*Z);return unit(u)

rng=np.random.default_rng(20260905)
a,b=[f.random_field(600+i) for i in range(2)]
q=Q(a,b)
mat=-.5*(commC2(a,b)+commC2(b,a)+nabla(C2(a),b)+nabla(C2(b),a))
print('BCH versus geometric-curvature tribunal')
print('general bilinear material-mother formula',rel(q,mat))
assert rel(q,mat)<2e-11
u=f.random_field(610);qd=Q(u,u)
# Poisson formula J_{C2 u}u - [C2,J_u]u.  [C2,J]=C Kp + Kp C.
po=J(C2(u),u) - (f.curl(Kp(u,u))+Kp(u,f.curl(u)))
print('diagonal Poisson-mother formula',rel(qd,po))
assert rel(qd,po)<2e-11
# Harmless diagonal dynamics can kill BCH while ambient geometric curvature remains nonzero.
w=f.random_field(620);v=f.random_field(621)
for name,x in [('Beltrami',beltrami()),('shear',shear())]:
    dyn=Q(x,x);geo=Kg(x,v,w)
    print(name,'||Euler-heat BCH||',f.norm(dyn),'||[R,C](x,v)w||',f.norm(geo))
    assert f.norm(dyn)<2e-11 and f.norm(geo)>1e-4
print('PASS: Euler-heat BCH and formation curl curvature are distinct descendants of the same (T,C) core: BCH is a diagonal/symmetric C^2 defect, while [R,C] is covariant antisymmetric holonomy. Neither should be renamed as the other.')
