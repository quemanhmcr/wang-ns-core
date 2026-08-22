#!/usr/bin/env python3
"""Across growing exact helical windows, three support directions recover the whole root-incidence relation space."""
from __future__ import annotations
import importlib.util,itertools,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
fh=loadpath('fh',ROOT/'research'/'theory2_universal_compiler'/'audits'/'full_helical_one_state_recovers_union_graph.py')
hg=loadpath('hg',ROOT/'research'/'theory2_universal_compiler'/'audits'/'exact_helical_sparse_state_law_holography.py')
P3=[(0,0,1),(0,1,-1),(1,-1,-1)]
def rp(e):
 (q,sq),(r,t)=e;return (round(t*np.linalg.norm(r),12),round(sq*np.linalg.norm(q),12))
def ranknull(pts,D,R):
 M=hg.mons(D);A=np.array([hg.evalrow(x,y,M,R) for x,y in sorted(pts)]);N,r,s=hg.nullspace(A);return N,r,s,M
def first_extra(full,allp,R):
 for D in range(1,24):
  Ns,rs,ss,M=ranknull(allp,D,R);Np,rp0,sp,_=ranknull(full,D,R)
  if Np.shape[1]>Ns.shape[1]:return D,Ns,Np,Np.shape[1]-Ns.shape[1],M
 raise RuntimeError('no extra relation')
def qspace(Np,Ns):
 X=Np-Ns@(Ns.T@Np);U,s,Vh=np.linalg.svd(X,full_matrices=False);e=int(np.sum(s>1e-8));return U[:,:e],s,e
def main():
 Pall=fh.support_reps(3);rows=[]
 for R2 in [3,4,5,6,8,9]:
  K=fh.window(R2);full={rp(e) for e in fh.structural_union(Pall,K)};roots=sorted({x for xy in full for x in xy});allp={(x,y) for x in roots for y in roots if x!=y};R=max(abs(x) for x in roots)
  D,Ns,Np,extra,M=first_extra(full,allp,R);Qcat,sc,ec=qspace(Np,Ns);assert ec==extra
  # fixed three-direction state; for R2=3 it is redundant but still valid.
  for seed in range(2):
   N,E=hg.exact_E_matrix(hg.dense_on(P3,37000+100*R2+seed),K);Ne,rr,sv,nrows=hg.matrix_relation_null(N,E,M,R);Qs,ss,es=qspace(Ne,Ns);cos=np.linalg.svd(Qcat.T@Qs,compute_uv=False);mincos=float(np.min(cos)) if len(cos) else 1.0
   # root-pair support check only for audit transparency, not relation extraction.
   one=set()
   for i,(r,t) in enumerate(N):
    for j,(q,sq) in enumerate(N):
     if abs(E[i,j])>1e-10:one.add((round(t*np.linalg.norm(r),12),round(sq*np.linalg.norm(q),12)))
   rows.append((R2,len(N),len(roots),len(full),len(allp-full),D,extra,nrows,Ne.shape[1],mincos,len(full-one),len(one-full)))
  print('R2',R2,'nodes',len(N),'roots',len(roots),'active',len(full),'forbidden',len(allp-full),'first_degree',D,'extra_dim',extra,'snapshot_rows',nrows,'relation_null',Ne.shape[1],'min_extra_cos',mincos,'missing/extra_edges',len(full-one),len(one-full))
 assert all(r[-2]==0 and r[-1]==0 and r[-3]>.999999 for r in rows)
 print('PASS: one fixed three-direction generic state recovers the full root-level interaction graph and the entire first physical quotient-relation space across six exact helical windows from 52 to 244 nodes. Presentation degree grows with scale, but the support complexity needed to reveal the law stays bounded by three in this tested category.')
if __name__=='__main__':main()
