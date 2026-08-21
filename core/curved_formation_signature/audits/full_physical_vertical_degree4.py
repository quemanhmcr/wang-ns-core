#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'metric_lie_hodge'/'audits'))
import formation_core_audit as f

def rf(seed):
    rng=np.random.default_rng(seed); return f.project(f.lowpass(rng.standard_normal((f.N,f.N,f.N,3)),cutoff=1))
def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def E(a,w): return nabla(a,f.curl(w))-f.curl(nabla(a,w))
def R(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)
def K(a,b,w): return R(a,b,f.curl(w))-f.curl(R(a,b,w))
def norm(v): return f.norm(v)
def rel(a,b): return norm(a-b)/max(norm(a),norm(b),1e-30)
rgrid=np.sqrt(f.K2); radii=np.unique(np.round(rgrid[rgrid>0],12))

def signed_component(v,r,sgn):
    vh=f.fft(v); ch=f.fft(f.curl(v)); shell=np.isclose(rgrid,r,rtol=0,atol=1e-10)
    H0=np.zeros_like(vh,dtype=complex); nz=shell&(rgrid>0); H0[nz]=ch[nz]/rgrid[nz,None]
    out=np.zeros_like(vh,dtype=complex); out[nz]=.5*(vh[nz]+sgn*H0[nz]); return f.ifft(out)
def comps(v,tol=2e-11):
    vh=f.fft(v); total=max(np.linalg.norm(vh),1e-30); nv=max(norm(v),1e-30); out=[]
    for r in radii:
      shell=np.isclose(rgrid,r,rtol=0,atol=1e-10)
      if np.linalg.norm(vh[shell])<=tol*total: continue
      for s in (+1,-1):
        q=signed_component(v,r,s)
        if norm(q)>tol*nv: out.append((s*r,q))
    return out
def Proot(v,lam): return signed_component(v,abs(lam),1 if lam>0 else -1)
def Rpar(a,b,w):
    out=np.zeros_like(w)
    for lam,q in comps(w): out += Proot(R(a,b,q),lam)
    return out
def Rperp(a,b,w): return R(a,b,w)-Rpar(a,b,w)
def cm(Rop,x,y,z,t,w): return Rop(x,y,K(z,t,w))-K(z,t,Rop(x,y,w))
def wedge4(Rop,a,b,c,d,w):
    pairs=[(a,b,c,d,1),(a,c,b,d,-1),(a,d,b,c,1),(b,c,a,d,1),(b,d,a,c,-1),(c,d,a,b,1)]
    out=np.zeros_like(w)
    for x,y,z,t,s in pairs: out += s*cm(Rop,x,y,z,t,w)
    return out

print('full physical vertical-curvature degree-4 tribunal')
rows=[]
for tr in range(3):
    a,b,c,d,w=[rf(500+10*tr+i) for i in range(5)]
    full=wedge4(R,a,b,c,d,w); par=wedge4(Rpar,a,b,c,d,w); perp=wedge4(Rperp,a,b,c,d,w)
    den=max(norm(full),1e-30); close=rel(full,par+perp)
    rows.append((norm(full),norm(par)/den,norm(perp)/den,close))
    print(f'trial {tr}: ||R_wedge_K||={rows[-1][0]:.3e} vertical/full={rows[-1][1]:.3f} horizontal/full={rows[-1][2]:.3f} closure={close:.3e}')
assert max(r[3] for r in rows)<1e-9
med=np.median([r[1] for r in rows]); print('median_vertical_fraction',med); assert med>0.03
print('PASS: full physical degree 4 also contains a substantial contribution from curvature commuting with curl at degree 2')
