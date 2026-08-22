#!/usr/bin/env python3
"""How far do p(C)=0 and Dp_C(E)=0 generate all word relations as a two-sided ideal?"""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
def all_strings(n):
 return [''.join(x) for k in range(n+1) for x in itertools.product('CE',repeat=k)]
def rels():
 r1={'':-6,'CC':11,'CCCC':-6,'CCCCCC':1};r2={}
 for n,co in [(6,1),(4,-6),(2,11)]:
  for j in range(n):r2['C'*j+'E'+'C'*(n-1-j)]=r2.get('C'*j+'E'+'C'*(n-1-j),0)+co
 return [r1,r2]
def ideal_matrix(L):
 labels=all_strings(L);ix={w:i for i,w in enumerate(labels)};cols=[]
 for r in rels():
  extra=L-6
  for la in range(extra+1):
   for lb in range(extra-la+1):
    for aa in itertools.product('CE',repeat=la):
     a=''.join(aa)
     for bb in itertools.product('CE',repeat=lb):
      b=''.join(bb);v=np.zeros(len(labels))
      for t,c in r.items():v[ix[a+t+b]]+=c
      cols.append(v)
 return np.column_stack(cols) if cols else np.zeros((len(labels),0)),labels
def word_matrix(C,E,L):
 mats=[np.eye(C.shape[0])];prev=[mats[0]]
 for _ in range(L):
  cur=[]
  for A in prev:cur.extend([A@C,A@E])
  mats.extend(cur);prev=cur
 return np.column_stack([A.reshape(-1) for A in mats])
def rank(A,tol=1e-10):
 s=np.linalg.svd(A,compute_uv=False);return int(np.sum(s>tol*s[0])) if len(s) and s[0]>0 else 0
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(29100);a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28))
 print('two-sided spectral-relation ideal growth')
 for L in [6,7,8,9]:
  W=word_matrix(C,E,L);rw=rank(W);null=W.shape[1]-rw;I,_=ideal_matrix(L);ri=rank(I);res=np.linalg.norm(W@I)/max(np.linalg.norm(W)*np.linalg.norm(I),1e-30) if I.size else 0
  print('degree',L,'words',W.shape[1],'word_rank',rw,'numeric_nullity',null,'spectral_ideal_generators',I.shape[1],'ideal_rank',ri,'ideal_residual',res,'unexplained_nullity',null-ri)
  assert res<1e-12 and ri<=null
  if L==6: assert ri==null
 # Physical interaction support creates an extra relation already at degree 7; the gap must then grow as path capacities saturate.
 gaps=[]
 for L in [7,8,9]:
  W=word_matrix(C,E,L);null=W.shape[1]-rank(W);ri=rank(ideal_matrix(L)[0]);gaps.append((L,null-ri))
 print('unexplained_relation_growth',gaps)
 assert gaps[0][1]==1 and all(gaps[i+1][1]>=gaps[i][1] for i in range(len(gaps)-1))
 print('PASS: p(C)=0 and Dp_C(E)=0 explain the complete relation space through degree 6 only. A first physical-incidence relation appears at degree 7, and additional relations accumulate as finite spectral-path channel capacities approach full M_28 saturation.')
if __name__=='__main__':main()
