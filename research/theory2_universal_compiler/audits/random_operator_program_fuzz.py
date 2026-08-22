#!/usr/bin/env python3
"""Semantic fuzzing: compressed E+K geometry must compile random held-out operator programs; E-only must fail."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
from scipy.linalg import expm
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ek=load('ek','ek_exact_lie_reconstruction.py')
def abelian(n):return np.zeros((n,n,n))
def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def conn(G,u):return sum(u[i]*G[i] for i in range(len(G)))
def fC(C,a):
 v,U=np.linalg.eigh(C);fv=np.exp(a[0]*v)+a[1]*np.sin(v)+a[2]*v*v+a[3];return (U*fv)@U.T
def normalize(A):return A/max(np.linalg.norm(A),1.0)
def setup(seed=27000,ratio=1.25):
 rng=np.random.default_rng(seed);c0=ek.direct_sum(ek.std_so3(),ek.std_so3(),abelian(2));c=ek.randomize_metric(c0,seed);G=ek.gamma_mats(ek.levi_from_structure(c));d=len(G);C=np.diag([-2]*3+[0]*3+[3]*2);E,K,R=ek.EK(G,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);xt=ek.coeffs_vertical(G,B,H).reshape(-1);y0,A=ek.codazzi_matrix(B,H,C);y=ek.flatten_K(K,d)-y0;m=int(np.ceil(ratio*len(xt)));P=rng.normal(size=(m,len(y)));P/=np.linalg.norm(P,axis=1,keepdims=True);xr=np.linalg.lstsq(P@A,P@y,rcond=None)[0];Gr=ek.from_x(B,H,xr.reshape(d,len(H)));return rng,C,G,Gr,B

def leaves(rng,C,G,n=12):
 d=len(G);R=ek.curvature(G);c=ek.structure_from_gamma(G);out=[]
 for _ in range(n):
  typ=rng.integers(4)
  if typ==0:out.append(normalize(conn(G,rng.normal(size=d))))
  elif typ==1:
   i,j=sorted(rng.choice(d,2,replace=False));out.append(normalize(R[i,j]))
  elif typ==2:
   u=rng.normal(size=d);out.append(normalize(-np.einsum('i,ikb->kb',u,c)))
  else:out.append(normalize(fC(C,rng.normal(size=4))))
 return out

def program(rng,L):
 A=L[rng.integers(len(L))]
 for _ in range(rng.integers(2,8)):
  B=L[rng.integers(len(L))];op=rng.integers(5)
  if op==0:A=normalize(A@B)
  elif op==1:A=normalize(A@B-B@A)
  elif op==2:A=normalize(A@B+B@A)
  elif op==3:A=normalize(.7*A-.3*B)
  else:A=normalize(expm(.08*A)@B)
 return A

def main():
 rng,C,G,Gr,B=setup();rng2=np.random.default_rng(27123)
 # Build paired leaves from identical random descriptions by saving RNG state.
 errs=[];abserrs=[];eonly=[];traceerrs=[]
 for t in range(1000):
  state=rng2.bit_generator.state;Lt=leaves(rng2,C,G,8);state_after_leaves=rng2.bit_generator.state
  rng2.bit_generator.state=state;Lr=leaves(rng2,C,Gr,8);rng2.bit_generator.state=state;Lb=leaves(rng2,C,B,8)
  # Same program random choices for all three evaluations.
  prog_state=state_after_leaves;rng2.bit_generator.state=prog_state;At=program(rng2,Lt);end_state=rng2.bit_generator.state
  rng2.bit_generator.state=prog_state;Ar=program(rng2,Lr);rng2.bit_generator.state=prog_state;Ab=program(rng2,Lb);rng2.bit_generator.state=end_state
  errs.append(rel(At,Ar));abserrs.append(np.linalg.norm(At-Ar));eonly.append(rel(At,Ab));traceerrs.append(abs(np.trace(At)-np.trace(Ar)))
 print('random operator program fuzz count',len(errs))
 print('E+K compiler rel median/p99/max',np.median(errs),np.quantile(errs,.99),max(errs),'abs_p99/max',np.quantile(abserrs,.99),max(abserrs),'trace_abs_max',max(traceerrs))
 print('E-only baseline median/p90/max',np.median(eonly),np.quantile(eonly,.9),max(eonly),'fraction_fail_gt_1e-3',np.mean(np.array(eonly)>1e-3))
 assert np.quantile(abserrs,.99)<1e-10 and max(abserrs)<1e-8
 assert np.median(eonly)>1e-2 and np.mean(np.array(eonly)>1e-3)>.7
 print('PASS: a near-minimal compressed E+K reconstruction semantically compiles 1000 regularized random unseen operator programs built from connection, curvature, Poisson, spectral functional calculus, products, commutators and exponentials. The E-only compiler fails broadly, so curvature supplies the missing grammar rather than merely improving a fitted target.')
if __name__=='__main__':main()
