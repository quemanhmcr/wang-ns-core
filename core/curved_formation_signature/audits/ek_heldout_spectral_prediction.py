#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)
P2=pathlib.Path(__file__).with_name('ek_higher_degree_completion.py');sp2=importlib.util.spec_from_file_location('hd',P2);hd=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(hd)
rng=np.random.default_rng(202608212133)
def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def fmat(C,f):
 vals,Q=np.linalg.eigh(C);return (Q*np.array([f(x) for x in vals]))@Q.T
def main():
 c=ek.direct_sum(ek.std_so3(),ek.heisenberg3());c=ek.randomize_metric(c,97531);G=ek.levi_from_structure(c);Gt=ek.gamma_mats(G);C=np.diag([-2,-2,0,0,3,3]);E,K,R=ek.EK(Gt,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);y0,A=ek.codazzi_matrix(B,H,C);x=np.linalg.lstsq(A,ek.flatten_K(K,len(C))-y0,rcond=None)[0];Gr=ek.from_x(B,H,x.reshape(len(C),-1));Rr=ek.curvature(Gr)
 print('held-out spectral prediction after E+K reconstruction')
 readers={
 'x2':lambda x:x*x,
 'x3':lambda x:x**3,
 'exp':lambda x:np.exp(.17*x),
 'sin':lambda x:np.sin(.4*x),
 'abs':abs,
 'hinge':lambda x:abs(x-.37),
 }
 worst=0
 for name,f in readers.items():
  F=fmat(C,f);e1=[];e2=[]
  for i in range(len(C)):e1.append(rel(ek.comm(Gt[i],F),ek.comm(Gr[i],F)))
  for p in R:e2.append(rel(ek.comm(R[p],F),ek.comm(Rr[p],F)))
  a=max(e1);b=max(e2);worst=max(worst,a,b);print(name,'connection_reader',a,'curvature_reader',b)
 # shifted cuts at held-out thresholds
 vals=np.linalg.eigvalsh(C);cuts=[-2.5,-1.1,.4,1.7,3.5]
 for a in cuts:
  Hc=fmat(C,lambda x: 1 if x>a else -1);er=max(rel(ek.comm(Gt[i],Hc),ek.comm(Gr[i],Hc)) for i in range(len(C)));kr=max(rel(ek.comm(R[p],Hc),ek.comm(Rr[p],Hc)) for p in R);worst=max(worst,er,kr);print('cut',a,'Ecut',er,'Kcut',kr)
 # Higher Bianchi form prediction, not used in fit.
 Kt=K;Kr={p:ek.comm(Rr[p],C) for p in Rr};dKt=hd.Dform(Kt,2,Gt);dKr=hd.Dform(Kr,2,Gr);higher=rel(np.concatenate([dKt[k].ravel() for k in sorted(dKt)]),np.concatenate([dKr[k].ravel() for k in sorted(dKr)]));worst=max(worst,higher);print('heldout_dK',higher)
 # E-only negative control: B misses hidden vertical connection and should fail at least one held-out object.
 Rb=ek.curvature(B);neg=max(rel(ek.comm(R[p],fmat(C,readers['exp'])),ek.comm(Rb[p],fmat(C,readers['exp']))) for p in R);print('E_only_curvature_reader_failure',neg)
 assert worst<2e-11 and neg>.05
 print('PASS: fitting only E and K recovers the generator of the entire tested curl functional calculus, shifted flags, curvature readers and a higher Bianchi level. E alone fails the held-out curvature prediction by order one.')
if __name__=='__main__':main()
