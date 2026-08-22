#!/usr/bin/env python3
"""Extract q from one E_u*, then test q(C_L,C_R)E_v=0 on unseen states v."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')
def applyq(C,E,q):
 out=np.zeros_like(E)
 for coeff,(a,b) in zip(q,pi.mons(6)):
  if abs(coeff)>1e-15:out+=coeff*np.linalg.matrix_power(C,a)@E@np.linalg.matrix_power(C,b)
 return out
def rel(a,b=0):
 if np.isscalar(b):return np.linalg.norm(a)/max(np.linalg.norm(a)+0,1.0)
 return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(29800)
 # One training snapshot only.
 a=rng.normal(size=28);Etrain=sum(a[i]*Es[i] for i in range(28));q=pi.word_extra(C,Etrain)
 train=np.linalg.norm(applyq(C,Etrain,q))/max(np.linalg.norm(Etrain),1e-30);errs=[]
 for _ in range(200):
  b=rng.normal(size=28);Ev=sum(b[i]*Es[i] for i in range(28));errs.append(np.linalg.norm(applyq(C,Ev,q))/max(np.linalg.norm(Ev),1e-30))
 print('one-snapshot structural-law generalization')
 print('train_residual',train,'unseen_count',len(errs),'median',np.median(errs),'p99',np.quantile(errs,.99),'max',max(errs))
 # Compare a generic all-offblock mother that obeys only spectral relations but violates the physical selection relation.
 vals,U=np.linalg.eigh((C+C.T)/2);groups=[]
 for i,x in enumerate(vals):
  if not groups or abs(x-groups[-1][0])>1e-8:groups.append([float(x),[i]])
  else:groups[-1][1].append(i)
 Eh=np.zeros_like(C)
 for i in range(len(groups)):
  for j in range(i+1,len(groups)):
   I,J=groups[i][1],groups[j][1];B=rng.normal(size=(len(I),len(J)));Eh[np.ix_(I,J)]=B;Eh[np.ix_(J,I)]=B.T
 Ectrl=U@Eh@U.T;ctrl=np.linalg.norm(applyq(C,Ectrl,q))/np.linalg.norm(Ectrl);print('same_spectrum_full_offblock_control_residual',ctrl)
 assert max(errs)<1e-11 and ctrl>1e-3
 print('PASS: a noncommutative relation learned from one generic mother snapshot annihilates 200 unseen physical mother states at machine precision, yet rejects a same-spectrum generic offblock control. One state reveals a state-independent interaction law of the whole finite physical core.')
if __name__=='__main__':main()
