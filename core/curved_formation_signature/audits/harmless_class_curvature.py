#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'metric_lie_hodge'/'audits'))
import formation_core_audit as f

def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def E(a,w): return nabla(a,f.curl(w))-f.curl(nabla(a,w))
def R(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)
def K(a,b,w): return R(a,b,f.curl(w))-f.curl(R(a,b,w))
def unit(v):
    n=f.norm(v); return v/max(n,1e-30)

def field2d(seed):
    rng=np.random.default_rng(seed)
    psi=rng.standard_normal((f.N,f.N,f.N,1))
    # force independent z and low x,y modes
    ph=np.fft.fftn(psi,axes=(0,1,2)); mask=(np.abs(f.KX)<=2)&(np.abs(f.KY)<=2)&(f.KZ==0); ph*=mask[...,None]
    psi=np.fft.ifftn(ph,axes=(0,1,2)).real[...,0]
    # u=(d_y psi,-d_x psi,0)
    scalar=psi[...,None]
    u=np.zeros((f.N,f.N,f.N,3)); u[...,0]=f.deriv(scalar,1)[...,0]; u[...,1]=-f.deriv(scalar,0)[...,0]
    return unit(u)

def shear():
    z=np.arange(f.N)*2*np.pi/f.N
    Z=np.broadcast_to(z,(f.N,f.N,f.N))
    u=np.zeros((f.N,f.N,f.N,3)); u[...,0]=np.sin(Z)+.35*np.sin(2*Z)
    return unit(u)

def beltrami():
    z=np.arange(f.N)*2*np.pi/f.N
    Z=np.broadcast_to(z,(f.N,f.N,f.N))
    u=np.zeros((f.N,f.N,f.N,3)); u[...,0]=np.sin(Z); u[...,1]=np.cos(Z)
    return unit(u)

def generic(seed): return unit(f.random_field(seed))

def measure(name,u,v,w):
    N=f.J(u,u)
    selfE=E(u,u); probeE=E(u,w); kval=K(u,v,w)
    print(f'{name:10s} ||N||={f.norm(N):.3e} ||E_u u||={f.norm(selfE):.3e} ||E_u w||={f.norm(probeE):.3e} ||K(u,v)w||={f.norm(kval):.3e}')
    return f.norm(N),f.norm(selfE),f.norm(probeE),f.norm(kval)

print('harmless-class ambient-curvature tribunal')
w=generic(100); v2=field2d(101)
r2=measure('2D',field2d(102),v2,w)
rb=measure('Beltrami',beltrami(),generic(103),w)
rs=measure('shear',shear(),generic(104),w)
# 2D self stretching should vanish, while full mother and ambient curvature remain visible.
assert r2[1] < 2e-11 and r2[2] > 1e-4 and r2[3] > 1e-4
# Beltrami/shear Euler diagonal is harmless/zero to roundoff, but operator geometry is not zero.
assert rb[0] < 2e-11 and rb[1] < 2e-11 and rb[2] > 1e-4 and rb[3] > 1e-4
assert rs[0] < 2e-11 and rs[1] < 2e-11 and rs[2] > 1e-4 and rs[3] > 1e-4
print('PASS: nonzero mother/curvature is ambient structural geometry, not a blow-up or nonlinear-self-stretching signal')
