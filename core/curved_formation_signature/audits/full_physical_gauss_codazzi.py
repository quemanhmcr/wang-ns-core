#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'metric_lie_hodge'/'audits'))
import formation_core_audit as f

def rf(seed):
    rng=np.random.default_rng(seed);q=f.project(f.lowpass(rng.standard_normal((f.N,f.N,f.N,3)),cutoff=1));return q/max(f.norm(q),1e-30)
def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def R(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)
def K(a,b,w): return R(a,b,f.curl(w))-f.curl(R(a,b,w))
def norm(x):return f.norm(x)
def rel(a,b):return norm(a-b)/max(norm(a),norm(b),1e-30)

rgrid=np.sqrt(f.K2); radii=np.unique(np.round(rgrid[rgrid>0],12))
def signed_component(v,r,sgn):
    vh=f.fft(v);ch=f.fft(f.curl(v));shell=np.isclose(rgrid,r,rtol=0,atol=1e-10);nz=shell&(rgrid>0)
    H0=np.zeros_like(vh,dtype=complex);H0[nz]=ch[nz]/rgrid[nz,None]
    out=np.zeros_like(vh,dtype=complex);out[nz]=.5*(vh[nz]+sgn*H0[nz]);return f.ifft(out)
def comps(v,tol=2e-11):
    vh=f.fft(v);total=max(np.linalg.norm(vh),1e-30);nv=max(norm(v),1e-30);out=[]
    for r in radii:
      shell=np.isclose(rgrid,r,rtol=0,atol=1e-10)
      if np.linalg.norm(vh[shell])<=tol*total:continue
      for s in (+1,-1):
        q=signed_component(v,r,s)
        if norm(q)>tol*nv:out.append((s*r,q))
    return out
def Proot(v,lam):return signed_component(v,abs(lam),1 if lam>0 else -1)
def Pvertical(op,w):
    out=np.zeros_like(w)
    for lam,q in comps(w):out+=Proot(op(q),lam)
    return out

def V(a,w):return Pvertical(lambda q:nabla(a,q),w)
def B(a,w):return nabla(a,w)-V(a,w)
def commop(A,Bop,w):return A(Bop(w))-Bop(A(w))

def Rpar(a,b,w):return Pvertical(lambda q:R(a,b,q),w)
def Rperp(a,b,w):return R(a,b,w)-Rpar(a,b,w)

def gauss(a,b,w):
    vv=commop(lambda q:V(a,q),lambda q:V(b,q),w)-V(br(a,b),w)
    bb=Pvertical(lambda q:commop(lambda z:B(a,z),lambda z:B(b,z),q),w)
    return vv+bb

def codazzi(a,b,w):
    x=(commop(lambda q:V(a,q),lambda q:B(b,q),w)
       +commop(lambda q:B(a,q),lambda q:V(b,q),w)
       +commop(lambda q:B(a,q),lambda q:B(b,q),w)-B(br(a,b),w))
    return x-Pvertical(lambda q:(commop(lambda z:V(a,z),lambda z:B(b,z),q)
       +commop(lambda z:B(a,z),lambda z:V(b,z),q)
       +commop(lambda z:B(a,z),lambda z:B(b,z),q)-B(br(a,b),q)),w)

def invadC_on_K(a,b,w):
    # Recover off-diagonal R from K blockwise: K_{mu<-lam}=(lam-mu)R.
    out=np.zeros_like(w)
    for lam,q in comps(w):
      rq=K(a,b,q)
      for mu,p in comps(rq):
        if abs(mu-lam)>1e-10:
          out += p/(lam-mu)
    return out

print('full physical helical Gauss-Codazzi tribunal')
rows=[]
for tr in range(3):
    a,b,w=[rf(1200+10*tr+i) for i in range(3)]
    rp=Rpar(a,b,w);ro=Rperp(a,b,w);g=gauss(a,b,w);c=codazzi(a,b,w);krec=invadC_on_K(a,b,w)
    row=(rel(rp,g),rel(ro,c),rel(ro,krec),norm(rp),norm(ro),rel(nabla(a,w),V(a,w)+B(a,w)))
    rows.append(row)
    print(f'trial {tr}: Gauss={row[0]:.3e} Codazzi={row[1]:.3e} Kinv={row[2]:.3e} ||Rpar||={row[3]:.3e} ||Rperp||={row[4]:.3e} split={row[5]:.3e}')
assert max(max(r[0],r[1],r[2],r[5]) for r in rows)<5e-9
assert min(r[3] for r in rows)>1e-5 and min(r[4] for r in rows)>1e-5
print('PASS: the full physical formation connection obeys the same helical-sheet Gauss/Codazzi splitting; K is exactly the gap-weighted off-sheet curvature action')
