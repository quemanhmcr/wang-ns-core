#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
def word_frame(C,E,q,depth=4):
 levels=[[q/np.linalg.norm(q)]];allv=[levels[0][0]]
 for _ in range(depth):
  cur=[]
  for v in levels[-1]:
   for G in (C,E):
    z=G@v;n=np.linalg.norm(z);cur.append(z/n if n else z)
  levels.append(cur);allv.extend(cur)
 return np.column_stack(allv)
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);d=28;rng=np.random.default_rng(26000);ratios=[]
 for seed in range(5):
  a=rng.normal(size=d);E=sum(a[i]*Es[i] for i in range(d));p=rng.normal(size=d);q=rng.normal(size=d);P=word_frame(C,E,p);Q=word_frame(C,E,q);sp=np.linalg.svd(P,compute_uv=False);sq=np.linalg.svd(Q,compute_uv=False);print('seed',seed,'frames',P.shape,Q.shape,'rank',np.linalg.matrix_rank(P),np.linalg.matrix_rank(Q),'frame_cond',sp[0]/sp[-1],sq[0]/sq[-1])
  X=rng.normal(size=(d,d));Y=P.T@X@Q;Xr=np.linalg.pinv(P.T,rcond=1e-12)@Y@np.linalg.pinv(Q,rcond=1e-12);e0=np.linalg.norm(Xr-X)/np.linalg.norm(X);print(' noiseless',e0)
  assert e0<1e-10
  errs=[]
  for eps in [1e-10,1e-8,1e-6,1e-4]:
   z=rng.normal(size=Y.shape);Yn=Y+eps*np.linalg.norm(Y)*z/np.linalg.norm(z);Xn=np.linalg.pinv(P.T,rcond=1e-12)@Yn@np.linalg.pinv(Q,rcond=1e-12);ee=np.linalg.norm(Xn-X)/np.linalg.norm(X);errs.append((eps,ee))
  sl=np.polyfit(np.log10([x for x,y in errs]),np.log10([y for x,y in errs]),1)[0];ratios.append((max(x[1] for x in errs[:2]),sl));print(' noise',errs,'slope',sl)
 print('measurement_budget',31*31,'operator_unknowns',28*28,'oversampling_ratio',31*31/(28*28))
 assert all(.8<sl<1.2 for _,sl in ratios)
 print('PASS: the complete depth-4 two-letter word frames use only 31 left and 31 right states. Their 961 scalar bilinear readings (1.226x the 784 operator unknowns) reconstruct arbitrary operators exactly and remain linearly stable under noise. One generic mother plus one probe pair is a near-minimal operator-tomography port in this finite physical lab.')
if __name__=='__main__':main()
