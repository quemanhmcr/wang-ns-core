#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,math,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
SETS={
 'axes3':[(1,0,0),(0,1,0),(0,0,1)],
 'axes_plus_pairs6':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)],
 'base7':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)],
}

def growth(C,E,tol=5e-9,maxdepth=12):
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
 add(np.eye(n),0);add(C,1);add(E,1);qi=0
 while qi<len(queue) and len(mats)<n*n:
  idx=queue[qi];qi+=1;dep=depths[idx]
  if dep>=maxdepth:continue
  A=mats[idx]
  for G in (C,E):add(A@G,dep+1)
 profile=[sum(x<=d for x in depths) for d in range(max(depths)+1)]
 return profile,len(mats),max(depths)

def main():
 old=mu.KS;rng=np.random.default_rng(21000);rows=[]
 try:
  for name in ['axes3','axes_plus_pairs6','base7']:
   mu.KS=list(SETS[name]);data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);d=len(C);a=rng.normal(size=d);E=sum(a[i]*Es[i] for i in range(d));p,dim,L=growth(C,E,maxdepth=12);lower=math.ceil(math.log2(d*d+1))-1
   rows.append((name,d,dim,L,lower,p));print(name,'d',d,'target',d*d,'profile',p,'saturation_depth',L,'word_count_lower_bound',lower,'excess',L-lower)
 finally:mu.KS=old
 # The no-triad axes control must stay reducible; richer sets must saturate.
 assert rows[0][2] < rows[0][1]**2
 assert rows[1][2] == rows[1][1]**2 and rows[2][2] == rows[2][1]**2
 # The richest base7 lab reaches the exact information-theoretic lower bound; pairs6 is only two levels slower.
 assert rows[2][3] == rows[2][4]
 assert rows[1][3] - rows[1][4] == 2
 print('PASS: two-letter growth is interaction-dependent rather than automatic. The no-triad axes control stays reducible; the 24D connected set saturates two levels above the lower bound; the 28D base7 set saturates exactly at the information-theoretic minimum depth.')
if __name__=='__main__':main()
