#!/usr/bin/env python3
"""Negative-control tribunal: Bianchi/Jacobi do not by themselves close every K-blind case."""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)
P2=pathlib.Path(__file__).with_name('ek_higher_degree_completion.py');sp2=importlib.util.spec_from_file_location('hd',P2);hd=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(hd)
def abelian(n):return np.zeros((n,n,n))
def almost_abelian6():
 c=np.zeros((6,6,6));a=[1.2,.7,.1,-.5,-1.5]
 for j in range(1,6):c[j,0,j]=a[j-1];c[j,j,0]=-a[j-1]
 return c
def packdict(F):return np.concatenate([F[k].ravel() for k in sorted(F)]) if F else np.zeros(0)
def jacvec(Gs):
 c=ek.structure_from_gamma(Gs);d=len(Gs);vals=[]
 for i,j,k in itertools.combinations(range(d),3):
  v=np.zeros(d)
  for a in range(d):v += c[a,j,k]*c[:,i,a]+c[a,k,i]*c[:,j,a]+c[a,i,j]*c[:,k,a]
  vals.append(v)
 return np.concatenate(vals)
def sensors(Gs,C):
 E,K,R=ek.EK(Gs,C);DR=hd.Dform(R,2,Gs);return ek.flatten_K(K,len(Gs)),packdict(DR),jacvec(Gs)
def rank(A):
 s=np.linalg.svd(A,compute_uv=False);r=int(np.sum(s>1e-8*(s[0] if len(s) else 1)));return r,A.shape[1]-r,(s[0]/s[r-1] if r else np.inf)
def one(c,seed,roots):
 c=ek.randomize_metric(c,seed);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag(roots);E,K,R=ek.EK(Gs,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);x0=ek.coeffs_vertical(Gs,B,H).reshape(-1);d=len(Gs);q=len(H);h=2e-6
 mats=[[],[],[]]
 for j in range(len(x0)):
  xp=x0.copy();xm=x0.copy();xp[j]+=h;xm[j]-=h
  fp=sensors(ek.from_x(B,H,xp.reshape(d,q)),C);fm=sensors(ek.from_x(B,H,xm.reshape(d,q)),C)
  for z in range(3):mats[z].append((fp[z]-fm[z])/(2*h))
 A=[np.column_stack(x) for x in mats]
 return len(x0),rank(A[0]),rank(np.vstack([A[0],A[1]])),rank(np.vstack([A[0],A[2]])),np.linalg.norm(sensors(Gs,C)[1]),np.linalg.norm(sensors(Gs,C)[2])
def main():
 fam={'so3+so3':ek.direct_sum(ek.std_so3(),ek.std_so3()),'so3+R3':ek.direct_sum(ek.std_so3(),abelian(3)),'h3+R3':ek.direct_sum(ek.heisenberg3(),abelian(3)),'almostAb6':almost_abelian6()}
 print('Bianchi/Jacobi completion negative-control tribunal: curl multiplicity 5+1')
 out={}
 for name,c in fam.items():
  vals=[]
  for seed in range(3):
   o=one(c,9000+seed,[-1]*5+[2]);vals.append(o);print(name,seed,'K',o[1],'K+DR',o[2],'K+Jacobi',o[3])
  out[name]=vals
 assert all(o[2][1]==0 and o[3][1]==0 for name in ('so3+so3','so3+R3','almostAb6') for o in out[name])
 assert all(o[1][1]==11 and o[2][1]==11 and o[3][1]==7 for o in out['h3+R3'])
 print('PASS negative control: second Bianchi and Jacobi close several high-degeneracy K kernels, but the nilpotent+central h3+R3 case retains 11 directions under K+DR and 7 under K+Jacobi. No claim of universal degree-2 integrability closure is allowed.')
if __name__=='__main__':main()
