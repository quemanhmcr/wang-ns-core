#!/usr/bin/env python3
"""Tribunal for the Cartan-like interpretation of the complete curl mother.

The finite coordinate lab tests that u -> E_u is a fixed linear injective
operator-valued one-form (modulo the known Galilean kernel).  The full physical
pseudospectral side tests the structure/Bianchi equations without Galerkin
projection.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'curved_formation_signature'/'audits'))
import metric_lie_spectral_unification as m
sys.path.insert(0,str(ROOT/'core'/'metric_lie_hodge'/'audits'))
import formation_core_audit as f

RNG=np.random.default_rng(20260821)

def relv(a,b):
    return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)

# Fixed operator-valued one-form E in the finite physical coordinate lab.
data=m.build_physical_tensors(False)
AE,Es=m.mother_tensor(data['Gamma'],data['C'])
d=len(data['C'])
u=RNG.normal(size=d);v=RNG.normal(size=d); alpha=-0.731
Eu=sum(u[i]*Es[i] for i in range(d)); Ev=sum(v[i]*Es[i] for i in range(d))
Euv=sum((u+alpha*v)[i]*Es[i] for i in range(d))
linear=relv(Euv,Eu+alpha*Ev)
s=np.linalg.svd(AE,compute_uv=False); rank=int(np.sum(s>1e-10*s[0])); cond=s[0]/s[-1]

# Galilean extension: the only kernel should be the 3 constant directions.
dg=m.build_physical_tensors(True); AG,_=m.mother_tensor(dg['Gamma'],dg['C'])
sg=np.linalg.svd(AG,compute_uv=False); rankg=int(np.sum(sg>1e-10*sg[0])); nullg=AG.shape[1]-rankg

# Full physical structure equations.
def rf(seed):
    rng=np.random.default_rng(seed)
    x=f.project(f.lowpass(rng.standard_normal((f.N,f.N,f.N,3)),cutoff=1))
    return x/max(f.norm(x),1e-30)
def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def Theta(a,w): return nabla(a,f.curl(w))-f.curl(nabla(a,w))
def Curv(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)
def Tcurl(a,b,w): return Curv(a,b,f.curl(w))-f.curl(Curv(a,b,w))
def d1(A,a,b,w):
    return (nabla(a,A(b,w))-A(b,nabla(a,w))
           -nabla(b,A(a,w))+A(a,nabla(b,w))-A(br(a,b),w))
def d2(A,a,b,c,w):
    def D(x,y,z,ww): return nabla(x,A(y,z,ww))-A(y,z,nabla(x,ww))
    return (D(a,b,c,w)-D(b,a,c,w)+D(c,a,b,w)
           -A(br(a,b),c,w)+A(br(a,c),b,w)-A(br(b,c),a,w))
def RwTheta(a,b,c,w):
    def q(x,y,z,ww): return Curv(x,y,Theta(z,ww))-Theta(z,Curv(x,y,ww))
    return q(a,b,c,w)-q(a,c,b,w)+q(b,c,a,w)
def relf(a,b): return f.norm(a-b)/max(f.norm(a),f.norm(b),1e-30)

a,b,c,w=[rf(900+i) for i in range(4)]
structure=relf(d1(Theta,a,b,w),Tcurl(a,b,w))
first_bianchi=relf(d2(Tcurl,a,b,c,w),RwTheta(a,b,c,w))
second_bianchi=f.norm(d2(Curv,a,b,c,w))/max(f.norm(Curv(a,b,w)),f.norm(Curv(a,c,w)),f.norm(Curv(b,c,w)),1e-30)
jac=f.norm(br(a,br(b,c))+br(b,br(c,a))+br(c,br(a,b)))/max(f.norm(a)*f.norm(b)*f.norm(c),1e-30)

print('curl-solder Cartan structure tribunal')
print(f'linearity_of_Theta=u->E_u             {linear:.3e}')
print(f'mean_zero_rank                         {rank}/{d}')
print(f'mean_zero_condition                    {cond:.3e}')
print(f'Galilean_extended_nullity              {nullg}')
print(f'Jacobi_full_physical                    {jac:.3e}')
print(f'DTheta_equals_Tcurl=[R,C]              {structure:.3e}')
print(f'DTcurl_equals_R_wedge_Theta            {first_bianchi:.3e}')
print(f'DR_zero_second_Bianchi                 {second_bianchi:.3e}')
assert linear<1e-12 and rank==d and nullg==3
assert jac<2e-10 and structure<2e-10 and first_bianchi<5e-10 and second_bianchi<2e-10
print('PASS: the complete mother is a linear operator-valued soldering-type form; its covariant curl-torsion and formation curvature obey Cartan-like structure and Bianchi equations')
