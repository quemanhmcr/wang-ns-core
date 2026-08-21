#!/usr/bin/env python3
"""Full-field shifted-helicity tomography of the formation curvature action."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'core' / 'metric_lie_hodge' / 'audits'))
import formation_core_audit as f


def rf(seed):
    rng=np.random.default_rng(seed)
    return f.project(f.lowpass(rng.standard_normal((f.N,f.N,f.N,3)),cutoff=1))
def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def R(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)

def Hshift(v,a):
    """sign(C-a) on mean-zero divergence-free Fourier fields."""
    vh=f.fft(v); ch=f.fft(f.curl(v))
    r=np.sqrt(f.K2)
    nz=r>0
    out=np.zeros_like(vh,dtype=complex)
    sp=np.sign(r-a); sm=np.sign(-r-a)
    alpha=.5*(sp+sm); beta=.5*(sp-sm)
    # H0 v = C v / |k| on transverse nonzero modes
    H0=np.zeros_like(vh,dtype=complex)
    H0[nz]=ch[nz]/r[nz,None]
    out = alpha[...,None]*vh + beta[...,None]*H0
    # mean zero inputs/operators throughout this audit
    out[~nz]=0
    return f.ifft(out)

def rel(a,b): return f.norm(a-b)/max(f.norm(a),f.norm(b),1e-30)

def main():
    a,b,w=[rf(700+i) for i in range(3)]
    a,b,w=[x/max(f.norm(x),1e-30) for x in (a,b,w)]
    Rw=R(a,b,w)
    target=R(a,b,f.curl(w))-f.curl(Rw)
    # All signed curl eigenvalues on the discrete grid, including zero seam.
    radii=np.unique(np.round(np.sqrt(f.K2).ravel(),12))
    roots=np.unique(np.concatenate((-radii[::-1],radii)))
    roots.sort()
    layer=np.zeros_like(w)
    active=0
    for left,right in zip(roots[:-1],roots[1:]):
        aa=.5*(left+right); width=right-left
        Hw=Hshift(w,aa); HRw=Hshift(Rw,aa)
        comm=R(a,b,Hw)-HRw
        if f.norm(comm)>1e-10: active+=1
        layer += .5*width*comm
    err=rel(layer,target)
    # Independent layer-cake C itself on w.
    Cw_layer=np.zeros_like(w)
    for left,right in zip(roots[:-1],roots[1:]):
        aa=.5*(left+right); Cw_layer += .5*(right-left)*Hshift(w,aa)
    cerr=rel(Cw_layer,f.curl(w))
    print('full physical curvature / shifted-flag tomography tribunal')
    print('number signed roots                  ',len(roots))
    print('active curvature cuts                ',active)
    print(f'layercake_C_on_probe                  {cerr:.3e}')
    print(f'layercake_[R,H]_to_[R,C]             {err:.3e}')
    print(f'||[R,C]w||                           {f.norm(target):.3e}')
    assert cerr<2e-12 and err<2e-11 and f.norm(target)>1e-4
    print('PASS: full physical shifted spectral cuts tomographically reconstruct formation curl curvature')
if __name__=='__main__': main()
