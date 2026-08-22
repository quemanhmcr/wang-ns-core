#!/usr/bin/env python3
"""Check the three defining relations on an exact full-helical base7-window mother operator, without projected Lie brackets."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ph=loadpath('ph',ROOT/'core'/'curved_formation_signature'/'audits'/'physical_helical_resonant_recovery.py')
fg=loadpath('fg',ROOT/'research'/'theory2_universal_compiler'/'audits'/'full_helical_interaction_graph_percolation.py')

def reps():return [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def dense_real(seed):
 rng=np.random.default_rng(seed);U={}
 for pp in reps():
  p=np.array(pp,float);z=ph.projvec(p,rng.normal(size=3)+1j*rng.normal(size=3));z/=np.linalg.norm(z);z*=rng.normal()+1j*rng.normal();U[pp]=z;U[tuple(-p.astype(int))]=np.conj(z)
 return U
def nodes():
 K=set(reps())|{tuple(-np.array(k)) for k in reps()};return [(k,s) for k in sorted(K) for s in (+1,-1)]
def matrix_E(U,N):
 ix={z:i for i,z in enumerate(N)};M=np.zeros((len(N),len(N)),complex)
 for j,(q,sq) in enumerate(N):
  F=ph.E(U,ph.mode(q,sq))
  for r,a in F.items():
   for t in (+1,-1):
    z=(r,t)
    if z in ix:M[ix[z],j]+=ph.hcoef(r,t,a)
 return M
def pC(C):return np.linalg.matrix_power(C,6)-6*np.linalg.matrix_power(C,4)+11*C@C-6*np.eye(len(C))
def Dp(C,E):
 out=np.zeros_like(E)
 for n,c in [(6,1),(4,-6),(2,11)]:
  for j in range(n):out+=c*np.linalg.matrix_power(C,j)@E@np.linalg.matrix_power(C,n-1-j)
 return out
def Q(C,E):
 A=C@C-np.eye(len(C));return A@(C@C@E+E@C@C-5*E)@A
def rel(A,scale):return np.linalg.norm(A)/max(scale,1e-30)
def main():
 N=nodes();C=np.diag([s*ph.knorm(k) for k,s in N]).astype(complex);print('exact complex helical window dim',len(N),'roots',sorted(set(round(float(x.real),6) for x in np.diag(C))))
 rows=[]
 for seed in range(8):
  E=matrix_E(dense_real(35300+seed),N);sc=max(np.linalg.norm(E),1.0);a=rel(pC(C),max(np.linalg.norm(C)**6,1));b=rel(Dp(C,E),sc*max(np.linalg.norm(C)**5,1));q=rel(Q(C,E),sc*max(np.linalg.norm(C)**6,1));rows.append((a,b,q,np.linalg.norm(E)));print('seed',seed,'p',a,'Dp',b,'Q',q,'||E||',np.linalg.norm(E))
 assert max(max(r[:3]) for r in rows)<1e-12
 print('PASS: the exact full-helical mother operator restricted to the base7 spectral window obeys all three defining presentation laws p(C)=0, Dp_C(E)=0 and Q(C,E)=0 for eight generic real dense states. The three-law presentation is not created by the projected 28D Lie bracket.')
if __name__=='__main__':main()
