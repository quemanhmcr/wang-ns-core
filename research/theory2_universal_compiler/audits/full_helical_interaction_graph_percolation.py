#!/usr/bin/env python3
"""Exact helical Fourier action of E_u: interaction-graph percolation without using a projected Lie bracket."""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
p=ROOT/'core'/'curved_formation_signature'/'audits'/'physical_helical_resonant_recovery.py'
s=importlib.util.spec_from_file_location('ph',p);ph=importlib.util.module_from_spec(s);s.loader.exec_module(ph)
SUP=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def real_support(ps,seed):
 rng=np.random.default_rng(seed);U={}
 for pp in ps:
  p=np.array(pp,float);z=rng.normal(size=3)+1j*rng.normal(size=3);z=ph.projvec(p,z);z/=np.linalg.norm(z);a=rng.normal()+1j*rng.normal();z*=a
  U[tuple(pp)]=z;U[tuple(-np.array(pp))]=np.conj(z)
 return U
def nodes(R2=6):
 ks=[]
 lim=int(np.sqrt(R2))+1
 for k in itertools.product(range(-lim,lim+1),repeat=3):
  if k==(0,0,0):continue
  n=sum(x*x for x in k)
  if n<=R2:ks.append(k)
 return [(k,s) for k in ks for s in (+1,-1)]
def comps(adj):
 seen=set();sizes=[]
 for x in range(len(adj)):
  if x in seen:continue
  stack=[x];seen.add(x);n=0
  while stack:
   a=stack.pop();n+=1
   for b in adj[a]:
    if b not in seen:seen.add(b);stack.append(b)
  sizes.append(n)
 return sorted(sizes,reverse=True)
def root(k,s):return round(s*np.sqrt(sum(x*x for x in k)),8)
def main():
 N=nodes(6);idx={x:i for i,x in enumerate(N)};print('full helical exact-mother interaction graph nodes',len(N),'signed curl roots',len(set(root(*x) for x in N)))
 rows=[]
 for m in range(1,len(SUP)+1):
  U=real_support(SUP[:m],23000+m);adj=[set() for _ in N];root_edges=set();edges=0
  for j,(q,sq) in enumerate(N):
   F=ph.E(U,ph.mode(q,sq))
   for r,a in F.items():
    for t in (+1,-1):
     key=(r,t)
     if key not in idx:continue
     amp=abs(ph.hcoef(r,t,a))
     if amp>1e-9:
      k=idx[key];adj[j].add(k);adj[k].add(j);edges+=1;ra,rb=root(q,sq),root(r,t)
      if ra!=rb:root_edges.add(tuple(sorted((ra,rb))))
  cs=comps(adj);frac=cs[0]/len(N);isol=sum(1 for x in cs if x==1);rows.append((m,edges,len(cs),cs[0],isol,len(root_edges),frac));print('support',m,SUP[:m],'edges',edges,'components',len(cs),'largest',cs[0],'fraction',frac,'isolated',isol,'cross_root_edges',len(root_edges),'top_components',cs[:8])
 # Require a genuine trend, not universal connectivity from one mode.
 assert rows[0][2]>1 and rows[-1][3]>rows[0][3]
 assert rows[-1][6]>.85
 print('PASS: using the exact full helical Fourier action of E_u (no projected Lie bracket), increasing physical support causes a sharp collapse of interaction components and a large connected curl-spectral mixing network. The operator-algebra percolation has a direct full-Fourier support-level counterpart.')
if __name__=='__main__':main()
