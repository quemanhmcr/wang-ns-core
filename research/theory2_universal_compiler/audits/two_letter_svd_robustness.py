#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')

def all_words(C,E,depth):
 levels=[[np.eye(C.shape[0])]]; allm=[levels[0][0]]
 for d in range(1,depth+1):
  prev=levels[-1];cur=[]
  for A in prev:
   cur.extend([A@C,A@E])
  levels.append(cur);allm.extend(cur)
 cols=[]
 for A in allm:
  v=A.reshape(-1).astype(float);n=np.linalg.norm(v)
  cols.append(v/n if n>0 else v)
 return np.column_stack(cols)

def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(19100)
 ratios=[];ranks=[]
 for seed in range(4):
  a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));W=all_words(C,E,9)
  s=np.linalg.svd(W,compute_uv=False);rank=int(np.sum(s>1e-10*s[0]));ratio=s[783]/s[0];ratios.append(ratio);ranks.append(rank)
  print('seed',seed,'shape',W.shape,'rank@1e-10',rank,'s784/s1',ratio,'s1',s[0],'s784',s[783],'spectrum_tail',s[779:784])
 assert ranks==[784]*4
 assert min(ratios)>1e-7
 print('PASS: the full 784-dimensional word span is not a loose Gram-Schmidt artifact; across four generic physical states the 784th singular direction remains quantitatively separated from zero.')
if __name__=='__main__':main()
