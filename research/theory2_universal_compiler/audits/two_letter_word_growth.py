#!/usr/bin/env python3
"""How quickly do noncommutative words in just C and one generic E_u span End(V)?"""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ek=load('ek','ek_exact_lie_reconstruction.py');mu=load('mu','metric_lie_spectral_unification.py')

def growth(C,E,tol=1e-9,maxdepth=100):
 n=C.shape[0];Q=[];mats=[];depths=[];queue=[]
 def add(A,dep):
  v=A.reshape(-1).astype(float);nv=np.linalg.norm(v)
  if nv<1e-14:return False
  v/=nv
  if Q:
   QQ=np.column_stack(Q)
   for _ in range(2):v-=QQ@(QQ.T@v)
  nv=np.linalg.norm(v)
  if nv<tol:return False
  v/=nv;Q.append(v);mats.append(v.reshape(n,n));depths.append(dep);queue.append(len(mats)-1);return True
 add(np.eye(n),0);add(C,1);add(E,1)
 qi=0;profile=[];last=-1
 while qi<len(queue) and len(mats)<n*n:
  idx=queue[qi];qi+=1;A=mats[idx];dep=depths[idx]
  if dep>=maxdepth:continue
  for G in (C,E): add(A@G,dep+1)
 profile=[(d,sum(x<=d for x in depths)) for d in range(max(depths)+1)]
 return profile,len(mats),max(depths)

def main():
 rng=np.random.default_rng(19000)
 c=ek.randomize_metric(ek.direct_sum(ek.std_so3(),ek.heisenberg3()),19001);G=ek.gamma_mats(ek.levi_from_structure(c));C=np.diag([-2,-2,0,0,3,3]);Es,_,_=ek.EK(G,C);a=rng.normal(size=6);E=sum(a[i]*Es[i] for i in range(6))
 p6,d6,m6=growth(C,E,tol=2e-10);print('exact6 word profile',p6,'final',d6,'maxdepth',m6)
 data=mu.build_physical_tensors(False);C28=data['C'];_,E28s=mu.mother_tensor(data['Gamma'],C28);a=rng.normal(size=28);E28=sum(a[i]*E28s[i] for i in range(28))
 p28,d28,m28=growth(C28,E28,tol=5e-9,maxdepth=80);print('physical28 word profile',p28,'final',d28,'target',28*28,'maxdepth',m28)
 assert d6==36 and d28==784
 # Require saturation well before the naive n^2 word length ceiling.
 assert m28<40
 print('PASS: just two operator letters, C and one generic mother E_u, generate the full matrix algebra by finite noncommutative words; the 28D physical lab saturates far below the n^2 dimension ceiling.')
if __name__=='__main__':main()
