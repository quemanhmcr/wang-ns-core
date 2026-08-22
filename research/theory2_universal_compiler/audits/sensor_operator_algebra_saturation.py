#!/usr/bin/env python3
"""Do curl + a tiny number of mother matrices generate the full observable matrix algebra?"""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]

def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ek=load('ek','ek_exact_lie_reconstruction.py')
mu=load('mu','metric_lie_spectral_unification.py')

def closure_dim(gens,tol=2e-10,maxdim=None):
    n=gens[0].shape[0]; maxdim=maxdim or n*n
    Q=[]; mats=[]; queue=[]
    def add(A):
      v=np.asarray(A,float).reshape(-1).copy();nv=np.linalg.norm(v)
      if nv<1e-14:return False
      v/=nv
      if Q:
        QQ=np.column_stack(Q)
        for _ in range(2):v-=QQ@(QQ.T@v)
      nv=np.linalg.norm(v)
      if nv<tol:return False
      v/=nv;Q.append(v);mats.append(v.reshape(n,n));queue.append(len(mats)-1);return True
    add(np.eye(n))
    for g in gens:add(g)
    qi=0
    while qi<len(queue) and len(mats)<maxdim:
      A=mats[queue[qi]];qi+=1
      for g in gens:
        add(A@g)
        if len(mats)>=maxdim:break
    return len(mats)

def exact_case(seed=18000):
 c=ek.randomize_metric(ek.direct_sum(ek.std_so3(),ek.heisenberg3()),seed)
 G=ek.gamma_mats(ek.levi_from_structure(c));C=np.diag([-2,-2,0,0,3,3]);E,_,_=ek.EK(G,C)
 rng=np.random.default_rng(seed)
 coeffs=[rng.normal(size=6) for _ in range(4)]
 Er=[sum(a[i]*E[i] for i in range(6)) for a in coeffs]
 dims=[closure_dim([C])]
 for r in range(1,5):dims.append(closure_dim([C]+Er[:r]))
 # vertical-only control: commuting skew matrices cannot bridge curl blocks.
 _,_,_,H=ek.vertical_basis(C);V=sum((rng.normal()*h for h in H),start=np.zeros_like(C))
 vdim=closure_dim([C,V])
 return dims,vdim

def physical28(seed=18010):
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);d=C.shape[0];rng=np.random.default_rng(seed)
 Er=[]
 for _ in range(5):
   a=rng.normal(size=d);Er.append(sum(a[i]*Es[i] for i in range(d)))
 dims=[closure_dim([C],tol=5e-9,maxdim=d*d)]
 for r in range(1,6):dims.append(closure_dim([C]+Er[:r],tol=5e-9,maxdim=d*d))
 return d,dims

def main():
 print('sensor operator-algebra saturation tribunal')
 rows=[]
 for seed in range(5):
   dims,vd=exact_case(18000+seed);rows.append(dims);print('exact6 seed',seed,'dims C,+1E,+2E,+3E,+4E',dims,'vertical_control',vd)
 assert all(x[0]==3 for x in rows) # three distinct roots
 assert all(x[-1]==36 for x in rows)
 d,dims=physical28();print('physical28 dims C,+1E,+2E,+3E,+4E,+5E',dims,'target',d*d)
 assert dims[0]==6
 assert dims[-1]==d*d
 first_full=next((i for i,x in enumerate(dims) if x==d*d),None)
 print('physical28 first_full_after_random_mothers',first_full)
 print('PASS: the curl spectral algebra starts as a tiny commutative block algebra, but a handful of generic mother directions generate the full matrix observable algebra in both exact 6D and the 28D physical coordinate lab. This is algebraic irreducibility, not merely state injectivity.')
if __name__=='__main__':main()
