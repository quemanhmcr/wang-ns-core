#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')

def labels(L):return [''.join(x) for k in range(L+1) for x in itertools.product('CE',repeat=k)]
def words(C,E,L):
 mats=[np.eye(C.shape[0])];prev=[mats[0]]
 for _ in range(L):
  cur=[]
  for A in prev:cur.extend([A@C,A@E])
  mats.extend(cur);prev=cur
 return np.column_stack([A.reshape(-1) for A in mats])
def base_rels():
 r1={'':-6,'CC':11,'CCCC':-6,'CCCCCC':1};r2={}
 for n,co in [(6,1),(4,-6),(2,11)]:
  for j in range(n):r2['C'*j+'E'+'C'*(n-1-j)]=r2.get('C'*j+'E'+'C'*(n-1-j),0)+co
 return [r1,r2]
def ideal(L,labs):
 ix={w:i for i,w in enumerate(labs)};cols=[]
 for r in base_rels():
  for la in range(L-6+1):
   for lb in range(L-6-la+1):
    for aa in itertools.product('CE',repeat=la):
     for bb in itertools.product('CE',repeat=lb):
      a=''.join(aa);b=''.join(bb);v=np.zeros(len(labs))
      for t,c in r.items():v[ix[a+t+b]]+=c
      cols.append(v)
 return np.column_stack(cols)
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(29200)
 for seed in range(3):
  a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));L=7;labs=labels(L);W=words(C,E,L);U,s,Vh=np.linalg.svd(W,full_matrices=False);r=int(np.sum(s>1e-10*s[0]));N=Vh[r:].T;I=ideal(L,labs);Ui,si,Vhi=np.linalg.svd(I,full_matrices=False);ri=int(np.sum(si>1e-10*si[0]));Qi=Ui[:,:ri]
  # project numerical nullspace off the known ideal; extract dominant extra direction
  X=N-Qi@(Qi.T@N);ux,sx,vx=np.linalg.svd(X,full_matrices=False);z=ux[:,0];z/=np.max(np.abs(z));res=np.linalg.norm(W@z)/max(np.linalg.norm(W)*np.linalg.norm(z),1e-30);orth=np.linalg.norm(Qi.T@z)
  top=sorted([(abs(z[i]),z[i],labs[i]) for i in range(len(labs))],reverse=True)[:30]
  byE={k:0.0 for k in range(8)}
  for i,w in enumerate(labs):byE[w.count('E')]+=z[i]**2
  print('seed',seed,'word_rank',r,'nullity',N.shape[1],'ideal_rank',ri,'extra_singulars',sx[:5],'relation_res',res,'ideal_orth',orth,'mass_by_E_count',byE)
  print(' top',[(w,float(c)) for _,c,w in top])
  if seed==0: zref=z.copy()
  else:
   cc=abs(float(np.dot(zref,z)/(np.linalg.norm(zref)*np.linalg.norm(z))));print(' cross_seed_relation_cosine',cc);assert cc>.999999999
  assert r==246 and N.shape[1]==9 and ri==8 and sx[0]>.999 and sx[1]<1e-8 and res<1e-12 and orth<1e-10
  total=sum(byE.values());assert byE[1]/total>.999999999
 print('PASS: after quotienting the spectral two-sided ideal, degree 7 contains exactly one additional universal relation. Across random physical states it is state-independent up to sign and is purely linear in E, identifying a structural interaction-incidence law rather than a nonlinear state accident.')
if __name__=='__main__':main()
