#!/usr/bin/env python3
"""C,E_u cyclicity: one generic probe, short words, full state/operator tomography."""
from __future__ import annotations
import importlib.util,pathlib,math,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')

def orbit(C,E,q,maxdepth=8,tol=1e-10):
 levels=[[q/np.linalg.norm(q)]];allv=[levels[0][0]];profile=[]
 for d in range(maxdepth+1):
  W=np.column_stack(allv);s=np.linalg.svd(W,compute_uv=False);r=int(np.sum(s>tol*s[0]));profile.append(r)
  if r==len(q):break
  cur=[]
  for v in levels[-1]:cur.extend([C@v,E@v])
  cur=[v/np.linalg.norm(v) for v in cur if np.linalg.norm(v)>1e-14];levels.append(cur);allv.extend(cur)
 # greedily select an independent basis from orbit vectors
 B=[];Q=[]
 for v in allv:
  z=v.copy()
  if Q:
   QQ=np.column_stack(Q);z-=QQ@(QQ.T@z)
  n=np.linalg.norm(z)
  if n>1e-9:Q.append(z/n);B.append(v.copy())
  if len(B)==len(q):break
 return profile,np.column_stack(B) if len(B)==len(q) else None

def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);d=len(C);rng=np.random.default_rng(25000);depths=[]
 print('single-probe cyclicity tribunal, d=',d)
 for seed in range(6):
  a=rng.normal(size=d);E=sum(a[i]*Es[i] for i in range(d));q=rng.normal(size=d);prof,Q=orbit(C,E,q,7);L=next(i for i,r in enumerate(prof) if r==d);lower=math.ceil(math.log2(d+1))-1;depths.append(L);print('seed',seed,'rank_by_depth',prof,'saturation',L,'lower_bound',lower,'basis_cond',np.linalg.cond(Q))
  assert Q is not None and L==lower
 print('depths',depths)
 # One fixed left and right probe; short-word orbit bases turn scalar bilinear readings into arbitrary operator tomography.
 a=rng.normal(size=d);E=sum(a[i]*Es[i] for i in range(d));p=rng.normal(size=d);q=rng.normal(size=d);_,P=orbit(C,E,p,7);_,Q=orbit(C,E,q,7);X=rng.normal(size=(d,d));Y=P.T@X@Q;Xr=np.linalg.solve(P.T,Y)@np.linalg.inv(Q);err=np.linalg.norm(Xr-X)/np.linalg.norm(X);print('arbitrary_operator_tomography_relerr',err,'Pcond',np.linalg.cond(P),'Qcond',np.linalg.cond(Q));assert err<1e-9
 # Noise ladder on the scalar bilinear measurement table Y.
 errs=[]
 for eps in [1e-10,1e-8,1e-6,1e-4]:
  z=rng.normal(size=Y.shape);Yn=Y+eps*np.linalg.norm(Y)*z/np.linalg.norm(z);Xn=np.linalg.solve(P.T,Yn)@np.linalg.inv(Q);ee=np.linalg.norm(Xn-X)/np.linalg.norm(X);errs.append((eps,ee));print('noise',eps,'operator_err',ee)
 sl=np.polyfit(np.log10([a for a,b in errs]),np.log10([b for a,b in errs]),1)[0];print('noise_slope',sl);assert .8<sl<1.2
 print('PASS: in the 28D physical coordinate lab, one generic probe is cyclic for the two-letter algebra (C,E_u) at the information-theoretic minimum depth 4. Left/right short-word probe orbits then tomograph an arbitrary 28x28 operator from scalar bilinear readings, with linear noise stability.')
if __name__=='__main__':main()
