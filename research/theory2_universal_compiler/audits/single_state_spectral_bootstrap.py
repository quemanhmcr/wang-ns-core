#!/usr/bin/env python3
"""Can one generic mother E_u*, with C, serve as an algebraic frame for the whole formation core?"""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
def add_basis(Q,A,tol=5e-9):
 v=A.reshape(-1).astype(float);n=np.linalg.norm(v)
 if n<1e-14:return False,Q
 v/=n
 if Q.size:
  for _ in range(2):v-=Q@(Q.T@v)
 n=np.linalg.norm(v)
 if n<tol:return False,Q
 v/=n;return True,np.column_stack([Q,v])
def target_res(Q,targets):
 Y=np.column_stack([A.reshape(-1) for A in targets]);norm=np.linalg.norm(Y,axis=0);R=Y-Q@(Q.T@Y);e=np.linalg.norm(R,axis=0)/np.maximum(norm,1e-30);return float(np.median(e)),float(np.max(e))
def one(seed):
 data=mu.build_physical_tensors(False);C=data['C'];Gamma=data['Gamma'];T=data['T'];_,Es=mu.mother_tensor(Gamma,C);d=28;rng=np.random.default_rng(seed);a=rng.normal(size=d);E0=sum(a[i]*Es[i] for i in range(d));Gs=[Gamma[:,i,:] for i in range(d)];Js=[]
 for i in range(d):
  u=np.zeros(d);u[i]=1;Js.append(mu.J_from_T(T,u))
 Rs=[]
 for i,j in itertools.combinations(range(d),2):
  Gbr=sum(T[k,i,j]*Gs[k] for k in range(d));Rs.append(Gs[i]@Gs[j]-Gs[j]@Gs[i]-Gbr)
 targets={'E_all':Es,'Gamma_all':Gs,'J_all':Js,'R_all':Rs}
 Q=np.zeros((d*d,0));words=[(np.eye(d),0),(C,1),(E0,1)];levels={0:[np.eye(d)],1:[C,E0]};profiles=[]
 # process depth 0 then recursively all words; keep independent orthonormal span.
 ok,Q=add_basis(Q,np.eye(d)); profiles.append((0,Q.shape[1],{k:target_res(Q,v) for k,v in targets.items()}))
 prev=[np.eye(d)]
 for dep in range(1,10):
  cur=[]
  for A in prev:cur.extend([A@C,A@E0])
  for A in cur:
   _,Q=add_basis(Q,A)
  profiles.append((dep,Q.shape[1],{k:target_res(Q,v) for k,v in targets.items()}));prev=cur
 return profiles

def main():
 print('single-state spectral bootstrap tribunal: C + one generic E_u* as an algebraic frame for the whole 28D formation core')
 for seed in [28000,28001,28002]:
  p=one(seed);print('seed',seed)
  for dep,dim,res in p: print(' depth',dep,'word_span',dim,'Gamma max',res['Gamma_all'][1],'J max',res['J_all'][1],'R max',res['R_all'][1],'Eall max',res['E_all'][1])
  assert p[-1][1]==784
  assert max(p[-1][2][k][1] for k in p[-1][2])<1e-8
 print('PASS: after a single generic state chooses the two-letter alphabet (C,E_u*), short noncommutative words form an algebraic frame in which every mother direction, every connection direction, every Poisson direction and every tested curvature operator can be represented. One state does not identify the coefficients, but it supplies a universal operator language for the entire finite formation core.')
if __name__=='__main__':main()
