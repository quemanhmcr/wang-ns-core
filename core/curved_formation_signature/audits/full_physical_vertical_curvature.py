#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'metric_lie_hodge'/'audits'))
import formation_core_audit as f

def rf(seed):
    rng=np.random.default_rng(seed)
    return f.project(f.lowpass(rng.standard_normal((f.N,f.N,f.N,3)),cutoff=1))
def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def E(a,w): return nabla(a,f.curl(w))-f.curl(nabla(a,w))
def R(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)
def norm(v): return f.norm(v)
def rel(a,b): return norm(a-b)/max(norm(a),norm(b),1e-30)

rgrid=np.sqrt(f.K2)
radii=np.unique(np.round(rgrid[rgrid>0],12))

def signed_component(v,r,sgn):
    vh=f.fft(v); ch=f.fft(f.curl(v)); shell=np.isclose(rgrid,r,rtol=0,atol=1e-10)
    H0=np.zeros_like(vh,dtype=complex); nz=shell & (rgrid>0)
    H0[nz]=ch[nz]/rgrid[nz,None]
    out=np.zeros_like(vh,dtype=complex)
    out[nz]=0.5*(vh[nz]+sgn*H0[nz])
    return f.ifft(out)

def components(v,tol=2e-11):
    out=[]; nv=max(norm(v),1e-30)
    # support-adaptive shell scan
    vh=f.fft(v); energy_shell=[]
    for r in radii:
        shell=np.isclose(rgrid,r,rtol=0,atol=1e-10)
        e=np.linalg.norm(vh[shell])
        if e>tol*np.linalg.norm(vh):
            for s in (+1,-1):
                q=signed_component(v,r,s)
                if norm(q)>tol*nv: out.append((s*r,q))
    return out

def Proot(v,lam): return signed_component(v,abs(lam),1 if lam>0 else -1)

def Rpar(a,b,w):
    out=np.zeros_like(w)
    for lam,q in components(w):
        out += Proot(R(a,b,q),lam)
    return out

def Rperp(a,b,w): return R(a,b,w)-Rpar(a,b,w)

def commRE(Rop,a,b,c,w): return Rop(a,b,E(c,w))-E(c,Rop(a,b,w))
def wedge(Rop,a,b,c,w):
    return commRE(Rop,a,b,c,w)-commRE(Rop,a,c,b,w)+commRE(Rop,b,c,a,w)

print('full physical vertical-curvature degree-3 tribunal')
rows=[]
for t in range(4):
    a,b,c,w=[rf(300+10*t+j) for j in range(4)]
    full=wedge(R,a,b,c,w); par=wedge(Rpar,a,b,c,w); perp=wedge(Rperp,a,b,c,w)
    # typed decomposition checks on independent probe
    x=rf(900+t)
    dec=rel(R(a,b,x),Rpar(a,b,x)+Rperp(a,b,x))
    commute=rel(f.curl(Rpar(a,b,x)),Rpar(a,b,f.curl(x)))
    close=rel(full,par+perp)
    den=max(norm(full),1e-30)
    row=(norm(full),norm(par)/den,norm(perp)/den,close,commute,dec,len(components(E(c,w))))
    rows.append(row)
    print(f'trial {t}: ||dK||={row[0]:.3e} vertical/full={row[1]:.3f} horizontal/full={row[2]:.3f} closure={close:.3e} [Rpar,C]={commute:.3e} decomp={dec:.3e} active_roots={row[6]}')
assert max(r[3] for r in rows)<5e-10
assert max(r[4] for r in rows)<5e-10
assert max(r[5] for r in rows)<5e-10
med=np.median([r[1] for r in rows])
print('median_vertical_fraction',med)
assert med>0.05
print('PASS: degree 3 contains an order-one contribution from curl-commuting curvature that degree-2 K=[R,C] cannot see directly')
