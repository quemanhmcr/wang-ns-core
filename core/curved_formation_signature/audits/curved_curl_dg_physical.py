#!/usr/bin/env python3
"""Faithful full-pseudospectral curved curl DG/Bianchi tribunal.

Unlike the finite Galerkin tensor lab, no projection to a small mode basis is made.
All brackets/connections act on full grid fields. Initial support is cutoff 1 so the
nested products stay well below Nyquist through the tested degree.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'core' / 'metric_lie_hodge' / 'audits'))
import formation_core_audit as f


def rf(seed):
    rng=np.random.default_rng(seed)
    v=rng.standard_normal((f.N,f.N,f.N,3))
    return f.project(f.lowpass(v,cutoff=1))

def nabla(a,w): return f.project(f.advect(a,w))
def br(a,b): return f.project(f.advect(a,b)-f.advect(b,a))
def E(a,w): return nabla(a,f.curl(w))-f.curl(nabla(a,w))
def R(a,b,w): return nabla(a,nabla(b,w))-nabla(b,nabla(a,w))-nabla(br(a,b),w)
def comm_ops(A,B,w): return A(B(w))-B(A(w))

def K(a,b,w):
    # d_nabla E as End-valued 1-form
    return (nabla(a,E(b,w))-E(b,nabla(a,w))
           -nabla(b,E(a,w))+E(a,nabla(b,w))-E(br(a,b),w))

def RC(a,b,w): return R(a,b,f.curl(w))-f.curl(R(a,b,w))

def d2(F,a,b,c,w):
    # exterior covariant derivative of End-valued 2-form F
    def D(x,y,z,ww): return nabla(x,F(y,z,ww))-F(y,z,nabla(x,ww))
    return (D(a,b,c,w)-D(b,a,c,w)+D(c,a,b,w)
           -F(br(a,b),c,w)+F(br(a,c),b,w)-F(br(b,c),a,w))

def RwE(a,b,c,w):
    def cmR_E(x,y,z,ww): return R(x,y,E(z,ww))-E(z,R(x,y,ww))
    return cmR_E(a,b,c,w)-cmR_E(a,c,b,w)+cmR_E(b,c,a,w)

def L3(a,b,c,w): return d2(K,a,b,c,w)

def d3(F,a,b,c,d,w):
    xs=[a,b,c,d]
    out=np.zeros_like(w)
    for i,x in enumerate(xs):
        args=xs[:i]+xs[i+1:]
        val=nabla(x,F(*args,w))-F(*args,nabla(x,w))
        out += ((-1)**i)*val
    for i in range(4):
        for j in range(i+1,4):
            rest=[xs[k] for k in range(4) if k not in (i,j)]
            out += ((-1)**(i+j))*F(br(xs[i],xs[j]),*rest,w)
    return out

def RwK(a,b,c,d,w):
    pairs=[(a,b,c,d,1),(a,c,b,d,-1),(a,d,b,c,1),(b,c,a,d,1),(b,d,a,c,-1),(c,d,a,b,1)]
    out=np.zeros_like(w)
    for x,y,z,t,s in pairs:
        out += s*(R(x,y,K(z,t,w))-K(z,t,R(x,y,w)))
    return out

def rel(a,b): return f.norm(a-b)/max(f.norm(a),f.norm(b),1e-30)

def main():
    a,b,c,d,w=[rf(100+i) for i in range(5)]
    # Normalize to avoid tiny fields.
    a,b,c,d,w=[x/max(f.norm(x),1e-30) for x in (a,b,c,d,w)]
    jac=br(a,br(b,c))+br(b,br(c,a))+br(c,br(a,b))
    jacr=f.norm(jac)/max(f.norm(a)*f.norm(b)*f.norm(c),1e-30)
    rK=rel(K(a,b,w),RC(a,b,w))
    dR=d2(R,a,b,c,w)
    bianchi=f.norm(dR)/max(f.norm(R(a,b,w)),f.norm(R(b,c,w)),f.norm(R(c,a,w)),1e-30)
    dk=d2(K,a,b,c,w); rwe=RwE(a,b,c,w); r3=rel(dk,rwe)
    dl=d3(L3,a,b,c,d,w); rwk=RwK(a,b,c,d,w); r4=rel(dl,rwk)
    print('full physical curved-curl DG tribunal')
    print(f'Jacobi_full_bracket                 {jacr:.3e}')
    print(f'dE_equals_[R,C]                    {rK:.3e}')
    print(f'Bianchi_dR_zero                    {bianchi:.3e}')
    print(f'dK_equals_R_wedge_E                {r3:.3e}')
    print(f'd_dK_equals_R_wedge_K              {r4:.3e}')
    print(f'||E||                              {f.norm(E(a,w)):.3e}')
    print(f'||K||                              {f.norm(K(a,b,w)):.3e}')
    print(f'||dK||                             {f.norm(dk):.3e}')
    print(f'||d2K||                            {f.norm(dl):.3e}')
    assert jacr<2e-10 and rK<2e-10 and bianchi<2e-10 and r3<3e-10 and r4<1e-8
    print('PASS: on the full physical Lie geometry, curl generates the curved covariant tower d^2 = R-action')
if __name__=='__main__': main()
