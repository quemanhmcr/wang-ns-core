#!/usr/bin/env python3
"""Identify the first two relations in the C,E word algebra with p(C)=0 and [A,p(C)]=Dp_C(E)=0."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
def words(C,E,depth=6):
 mats=[np.eye(C.shape[0])];labels=[''];prev=[(mats[0],'')]
 for _ in range(depth):
  cur=[]
  for A,l in prev:
   cur.append((A@C,l+'C'));cur.append((A@E,l+'E'))
  for A,l in cur:mats.append(A);labels.append(l)
  prev=cur
 return mats,labels
def coeff(labels):return {l:i for i,l in enumerate(labels)}
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(29000)
 for seed in range(4):
  a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));mats,labels=words(C,E,6);W=np.column_stack([A.reshape(-1) for A in mats]);U,s,Vh=np.linalg.svd(W,full_matrices=False);rank=int(np.sum(s>1e-10*s[0]));N=Vh[rank:].T;ix=coeff(labels);r1=np.zeros(len(labels));r2=np.zeros(len(labels))
  # p(x)=x^6-6x^4+11x^2-6
  for lab,co in [('',-6),('CC',11),('CCCC',-6),('CCCCCC',1)]:r1[ix[lab]]=co
  # Dp_C(E) = sum C^j E C^(5-j) - 6 sum C^j E C^(3-j) + 11(EC+CE)
  for n,co in [(6,1),(4,-6),(2,11)]:
   for j in range(n):r2[ix['C'*j+'E'+'C'*(n-1-j)]]+=co
  R=np.column_stack([r1/np.linalg.norm(r1),r2/np.linalg.norm(r2)]);Qr,_=np.linalg.qr(R);Qn,_=np.linalg.qr(N)
  res1=np.linalg.norm(W@r1)/max(np.linalg.norm(W)*np.linalg.norm(r1),1e-30);res2=np.linalg.norm(W@r2)/max(np.linalg.norm(W)*np.linalg.norm(r2),1e-30);span=np.linalg.norm(Qn-Qr@(Qr.T@Qn))
  sv=np.linalg.svd(Qr.T@Qn,compute_uv=False)
  print('seed',seed,'words',len(labels),'rank',rank,'nullity',len(labels)-rank,'pC_res',res1,'Dp_res',res2,'known_vs_numeric_null_span_res',span,'principal_cosines',sv,'s_tail',s[-5:])
  assert rank==125 and N.shape[1]==2 and res1<1e-13 and res2<1e-13 and span<1e-8 and min(sv)>.999999
 print('PASS: the first two noncommutative word relations of (C,E_u) are exactly the curl minimal polynomial p(C)=0 and its first commutator/covariant derivative Dp_C(E_u)=0. Up through degree 6, no extra relation appears beyond the spectral law and its mother derivative.')
if __name__=='__main__':main()
