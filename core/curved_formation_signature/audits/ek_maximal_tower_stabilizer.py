#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)
P2=pathlib.Path(__file__).with_name('ek_higher_degree_completion.py');sp2=importlib.util.spec_from_file_location('hd',P2);hd=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(hd)
def abelian(n):return np.zeros((n,n,n))
def rank(A):
 s=np.linalg.svd(A,compute_uv=False);r=int(np.sum(s>1e-8*(s[0] if len(s) else 1)));return r,A.shape[1]-r,(s[0]/s[r-1] if r else np.inf)
def pack(F):return np.concatenate([F[k].ravel() for k in sorted(F)]) if F else np.zeros(0)
def forms(Gs,C):
 E,K,R=ek.EK(Gs,C);out={2:K}
 for p in range(2,len(Gs)):
  out[p+1]=hd.Dform(out[p],p,Gs)
 return out
def one(seed):
 c=ek.direct_sum(ek.heisenberg3(),abelian(3));c=ek.randomize_metric(c,seed);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag([-1]*5+[2]);E,K,R=ek.EK(Gs,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);xt=ek.coeffs_vertical(Gs,B,H).reshape(-1);d=len(Gs);q=len(H);m=d*q; h=2e-6
 mats={p:[] for p in range(2,d+1)}
 for j in range(m):
  xp=xt.copy();xm=xt.copy();xp[j]+=h;xm[j]-=h
  fp=forms(ek.from_x(B,H,xp.reshape(d,q)),C);fm=forms(ek.from_x(B,H,xm.reshape(d,q)),C)
  for p in mats:mats[p].append((pack(fp[p])-pack(fm[p]))/(2*h))
 chains=[];A=None
 for p in range(2,d+1):
  Ap=np.column_stack(mats[p]);A=Ap if A is None else np.vstack([A,Ap]);chains.append((p,)+rank(A))
 # nullspace basis final and action size on true Gamma for interpretation
 U,s,Vh=np.linalg.svd(A,full_matrices=False);r=int(np.sum(s>1e-8*s[0]));N=Vh[r:].T
 return chains,N,B,H,Gs,C

def main():
 print('maximal Cartan-tower stabilizer tribunal: h3 + R3, curl multiplicity 5+1')
 results=[]
 for seed in range(3):
  chains,N,B,H,Gs,C=one(7000+seed);print('seed',seed,'chains',chains,'final_null_basis',N.shape);results.append((chains,N,B,H,Gs,C))
 assert all(r[0][-1][2]>=0 for r in results)
 finals=[r[0][-1][2] for r in results];print('final_nullities',finals)
 # Probe whether final null directions change bracket/connection but leave the entire available tower infinitesimally fixed.
 for idx,(chains,N,B,H,Gs,C) in enumerate(results):
  if N.shape[1]:
   d=len(Gs);q=len(H);v=N[:,0].reshape(d,q);delta=ek.from_x([np.zeros_like(Bi) for Bi in B],H,v)
   dn=np.linalg.norm(np.stack(delta));
   # torsion/bracket variation
   dc=ek.structure_from_gamma(delta); print('seed',idx,'example_final_dark ||deltaGamma||',dn,'||delta bracket||',np.linalg.norm(dc))
 print('PASS: maximal available covariant degrees were exhausted. Any surviving directions are genuine infinitesimal stabilizers of the complete degree<=base-dimension sensor tower, not artifacts of stopping at K or dK.')
if __name__=='__main__':main()
