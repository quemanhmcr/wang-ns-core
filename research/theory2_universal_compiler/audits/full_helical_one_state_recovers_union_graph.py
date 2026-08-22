#!/usr/bin/env python3
"""In a finite helical window, does one generic dense state realize the full structural mother transition graph?"""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
p=ROOT/'core'/'curved_formation_signature'/'audits'/'physical_helical_resonant_recovery.py';s=importlib.util.spec_from_file_location('ph',p);ph=importlib.util.module_from_spec(s);s.loader.exec_module(ph)
def window(R2):
 L=int(np.sqrt(R2))+1;return {k for k in itertools.product(range(-L,L+1),repeat=3) if k!=(0,0,0) and sum(a*a for a in k)<=R2}
def positive_rep(k):
 for x in k:
  if x>0:return True
  if x<0:return False
 return False
def support_reps(R2):return sorted([k for k in window(R2) if positive_rep(k)])
def real_dense(ps,seed):
 rng=np.random.default_rng(seed);U={}
 for pp in ps:
  p=np.array(pp,float);z=ph.projvec(p,rng.normal(size=3)+1j*rng.normal(size=3));z/=np.linalg.norm(z);z*=rng.normal()+1j*rng.normal();U[pp]=z;U[tuple(-p.astype(int))]=np.conj(z)
 return U
def edges_from_U(U,K):
 N=[(k,s) for k in sorted(K) for s in (+1,-1)];idx=set(N);E=set()
 for q,sq in N:
  F=ph.E(U,ph.mode(q,sq))
  for r,a in F.items():
   if r not in K:continue
   for t in (+1,-1):
    if abs(ph.hcoef(r,t,a))>1e-9:E.add(((q,sq),(r,t)))
 return E
def structural_union(ps,K):
 E=set()
 for p in ps:
  for su in (+1,-1):
   U=ph.mode(p,su)
   E |= edges_from_U(U,K)
   U2=ph.mode(tuple(-np.array(p)),su);E |= edges_from_U(U2,K)
 return E
def main():
 K=window(6);P=support_reps(3);print('helical window nodes',2*len(K),'dense-state support representatives',len(P),P)
 full=structural_union(P,K);print('structural_union_edges',len(full));rng=[]
 for seed in range(6):
  one=edges_from_U(real_dense(P,31000+seed),K);missing=full-one;extra=one-full;rng.append((len(one),len(missing),len(extra)));print('seed',seed,'one_state_edges',len(one),'missing_from_union',len(missing),'extra',len(extra),'coverage',len(one&full)/len(full))
 assert all(m==0 and e==0 for n,m,e in rng)
 print('PASS: in the exact |k|^2<=6 helical observation window, one generic dense state supported on all |p|^2<=3 directions realizes exactly the same mother-transition graph as the union over every support direction and helicity. Generic one-state incidence therefore recovers the full structural graph of that finite support category.')
if __name__=='__main__':main()
