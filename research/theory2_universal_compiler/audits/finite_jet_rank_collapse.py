#!/usr/bin/env python3
"""Does the infinite local curl-spectral jet add generic connection DOF beyond E+K?"""
from __future__ import annotations
import importlib.util, itertools, pathlib, numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]

def load(name,file):
    p=ROOT/'core'/'curved_formation_signature'/'audits'/file
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ek=load('ek','ek_exact_lie_reconstruction.py')
hd=load('hd','ek_higher_degree_completion.py')


def so_basis(d):
    H=[]
    for a in range(d):
      for b in range(a+1,d):
        M=np.zeros((d,d));M[a,b]=1;M[b,a]=-1;H.append(M/np.sqrt(2))
    return H

def coeffs(G,H): return np.array([[np.vdot(h,A).real for h in H] for A in G])
def from_x(x,H):
    d=x.shape[0];return [sum((x[i,a]*H[a] for a in range(len(H))),start=np.zeros_like(H[0])) for i in range(d)]
def packdict(F): return np.concatenate([F[k].ravel() for k in sorted(F)]) if F else np.zeros(0)
def packE(E): return np.concatenate([x.ravel() for x in E])
def forms(G,C):
    E,K,R=ek.EK(G,C); out={'E':packE(E),'K':ek.flatten_K(K,len(G))};F=K
    for p in range(2,len(G)):
        F=hd.Dform(F,p,G);out[f'D{p-1}K']=packdict(F)
    return out

def rank(A):
    s=np.linalg.svd(A,compute_uv=False)
    if not len(s): return 0,0,np.inf
    r=int(np.sum(s>1e-8*s[0]));return r,A.shape[1]-r,(s[0]/s[r-1] if r else np.inf)

def jacobian(G,C):
    d=len(G);H=so_basis(d);x0=coeffs(G,H);m=x0.size;h=2e-6
    base=forms(G,C);keys=list(base); cols={k:[] for k in keys}
    flat=x0.ravel()
    for j in range(m):
      xp=flat.copy();xm=flat.copy();xp[j]+=h;xm[j]-=h
      fp=forms(from_x(xp.reshape(x0.shape),H),C);fm=forms(from_x(xm.reshape(x0.shape),H),C)
      for k in keys: cols[k].append((fp[k]-fm[k])/(2*h))
    return {k:np.column_stack(v) for k,v in cols.items()},m

def family():
    z=np.zeros((3,3,3))
    return {
      'so3+so3':ek.direct_sum(ek.std_so3(),ek.std_so3()),
      'so3+h3':ek.direct_sum(ek.std_so3(),ek.heisenberg3()),
      'h3+se2':ek.direct_sum(ek.heisenberg3(),ek.se2()),
      'h3+R3':ek.direct_sum(ek.heisenberg3(),z),
    }

def main():
    pats={
      '2+2+2':[-2,-2,0,0,3,3],
      '3+3':[-1,-1,-1,2,2,2],
      '4+2':[-1,-1,-1,-1,2,2],
      '5+1':[-1,-1,-1,-1,-1,2],
      'scalar':[-1]*6,
    }
    print('finite-jet rank collapse tribunal: full metric-compatible connection has 90 coefficients')
    rows=[]
    for fn,c0 in family().items():
      for pn,roots in pats.items():
        c=ek.randomize_metric(c0,17000+sum(map(ord,fn+pn)))
        G=ek.gamma_mats(ek.levi_from_structure(c)); C=np.diag(roots)
        J,m=jacobian(G,C);stack=None;chain=[]
        for k in J:
          stack=J[k] if stack is None else np.vstack([stack,J[k]])
          chain.append((k,)+rank(stack))
        rows.append((fn,pn,chain))
        print(f'{fn:9s} {pn:6s}',chain)
        assert m==90
    generic=[r for r in rows if r[1] in ('2+2+2','3+3','4+2')]
    assert all(next(x for x in chain if x[0]=='K')[1]==90 for _,_,chain in generic)
    assert all(all(x[1]==90 for x in chain[1:]) for _,_,chain in generic)
    # Scalar C is completely blind to the pure curl-commutator tower.
    assert all(all(x[1]==0 for x in chain) for _,pn,chain in rows if pn=='scalar')
    # At least one 5+1 case must be singular at E+K, so the generic claim is not faked.
    singular=[]
    for fn,pn,chain in rows:
      if pn=='5+1': singular.append((fn,next(x for x in chain if x[0]=='K')[2],chain[-1][2]))
    print('5+1 nullity K -> maximal tower',singular)
    assert any(a>0 for _,a,b in singular)
    print('PASS: at generic spectral points the Jacobian rank saturates at E+K and every higher covariant curl jet adds zero local connection rank. High-degeneracy strata remain singular and are reported explicitly.')
if __name__=='__main__':main()
