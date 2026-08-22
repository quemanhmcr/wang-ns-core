#!/usr/bin/env python3
"""Scope the 28D closed-form selection polynomial using exact full helical E action, without Galerkin projection."""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
p=ROOT/'core'/'curved_formation_signature'/'audits'/'physical_helical_resonant_recovery.py';s=importlib.util.spec_from_file_location('ph',p);ph=importlib.util.module_from_spec(s);s.loader.exec_module(ph)
BASE=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def real_support(ps,seed):
 rng=np.random.default_rng(seed);U={}
 for pp in ps:
  p=np.array(pp,float);z=rng.normal(size=3)+1j*rng.normal(size=3);z=ph.projvec(p,z);z/=np.linalg.norm(z);z*=rng.normal()+1j*rng.normal();U[tuple(pp)]=z;U[tuple(-np.array(pp))]=np.conj(z)
 return U
def qpoly(x,y):return (x*x-1)*(y*y-1)*(x*x+y*y-5)
def signed_base():
 s=set()
 for k in BASE:s.add(tuple(k));s.add(tuple(-np.array(k)))
 return s
def window(R2):
 L=int(np.sqrt(R2))+1;return {k for k in itertools.product(range(-L,L+1),repeat=3) if k!=(0,0,0) and sum(a*a for a in k)<=R2}
def tribunal(Kset,U):
 vals=[];viol=[]
 for q in Kset:
  for sq in (+1,-1):
   F=ph.E(U,ph.mode(q,sq));lin=sq*ph.knorm(q)
   for r,a in F.items():
    if r not in Kset:continue
    for t in (+1,-1):
     amp=abs(ph.hcoef(r,t,a))
     if amp<1e-10:continue
     lout=t*ph.knorm(r);z=abs(qpoly(lout,lin));vals.append((amp,z,q,sq,r,t));viol.append(amp*z)
 scale=max([x[0] for x in vals],default=1);return vals,max(viol,default=0)/max(scale,1e-30)
def main():
 U=real_support(BASE,30100);Kb=signed_base();vb,rb=tribunal(Kb,U);print('exact helical base7 nodes',len(Kb)*2,'active transitions',len(vb),'selection_weighted_residual',rb,'max_q_on_active',max(x[1] for x in vb))
 K6=window(6);v6,r6=tribunal(K6,U);bad=sorted(v6,key=lambda x:x[0]*x[1],reverse=True)[:8];print('expanded R2<=6 nodes',len(K6)*2,'active transitions',len(v6),'same_polynomial_residual',r6,'worst_violations',[(x[2],x[3],x[4],x[5],x[0],x[1]) for x in bad])
 assert rb<1e-10 and r6>1e-2
 print('PASS scope correction: the closed-form polynomial selection law is already present in the exact full-helical action restricted to the base7 spectral window, so it is not caused by Galerkin projection. But the same fixed polynomial fails on a larger helical window. The robust object is the window-dependent spectral interaction-incidence ideal, not this particular polynomial as a continuum-universal law.')
if __name__=='__main__':main()
