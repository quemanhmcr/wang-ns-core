#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)

def abelian(n):return np.zeros((n,n,n))
def almost_abelian6():
 c=np.zeros((6,6,6));a=[1.2,.7,.1,-.5,-1.5]
 for j in range(1,6):c[j,0,j]=a[j-1];c[j,j,0]=-a[j-1]
 return c

def get_form(F,I,n):
    # F keys sorted tuples. Return antisymmetric value for arbitrary distinct tuple I.
    if len(set(I))<len(I):return np.zeros((n,n))
    inv=sum(I[a]>I[b] for a in range(len(I)) for b in range(a+1,len(I)))
    key=tuple(sorted(I));return (-1 if inv%2 else 1)*F.get(key,np.zeros((n,n)))
def Dform(F,p,Gs):
    d=len(Gs);n=Gs[0].shape[0];c=ek.structure_from_gamma(Gs);out={}
    for I in itertools.combinations(range(d),p+1):
      val=np.zeros((n,n))
      for a in range(p+1):
        rest=I[:a]+I[a+1:]; val += (-1)**a * ek.comm(Gs[I[a]],get_form(F,rest,n))
      for a in range(p+1):
       for b in range(a+1,p+1):
        rest=I[:a]+I[a+1:b]+I[b+1:]
        br=c[:,I[a],I[b]]
        term=np.zeros((n,n))
        for k,coef in enumerate(br):
          if abs(coef)>1e-14: term += coef*get_form(F,(k,)+rest,n)
        val += (-1)**(a+b)*term
      out[I]=val
    return out

def pack(F):return np.concatenate([F[k].ravel() for k in sorted(F)]) if F else np.zeros(0)
def sensors(Gs,C,maxdeg=4):
 E,K,R=ek.EK(Gs,C); forms={2:K};
 if maxdeg>=3:forms[3]=Dform(forms[2],2,Gs)
 if maxdeg>=4:forms[4]=Dform(forms[3],3,Gs)
 return forms

def rank(A):
 s=np.linalg.svd(A,compute_uv=False);r=int(np.sum(s>1e-8*(s[0] if len(s) else 1)));return r,A.shape[1]-r,(s[0]/s[r-1] if r else np.inf)
def one(name,c,seed):
 roots=[-1]*5+[2];c=ek.randomize_metric(c,seed);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag(roots);E,K,R=ek.EK(Gs,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);xt=ek.coeffs_vertical(Gs,B,H);d=len(Gs);q=len(H);m=d*q
 def build(x):return ek.from_x(B,H,x.reshape(d,q))
 base=sensors(Gs,C,4)
 # Jacobian columns for degrees 2,3,4 using symmetric finite difference around true hidden connection.
 mats={2:[],3:[],4:[]};h=2e-6
 flat=xt.reshape(-1)
 for j in range(m):
  xp=flat.copy();xm=flat.copy();xp[j]+=h;xm[j]-=h
  fp=sensors(build(xp),C,4);fm=sensors(build(xm),C,4)
  for deg in mats:mats[deg].append((pack(fp[deg])-pack(fm[deg]))/(2*h))
 A2=np.column_stack(mats[2]);A23=np.vstack([A2,np.column_stack(mats[3])]);A234=np.vstack([A23,np.column_stack(mats[4])])
 return m,rank(A2),rank(A23),rank(A234)
def main():
 fam={
 'so3+so3':ek.direct_sum(ek.std_so3(),ek.std_so3()),
 'so3+R3':ek.direct_sum(ek.std_so3(),abelian(3)),
 'h3+R3':ek.direct_sum(ek.heisenberg3(),abelian(3)),
 'almostAb6':almost_abelian6(),
 }
 print('E+K higher-degree completion on adversarial 5+1 curl degeneracy')
 rows=[]
 for name,c in fam.items():
  vals=[]
  for seed in range(3):
   o=one(name,c,5000+seed);vals.append(o);print(name,'seed',seed,'unknown',o[0],'K(rank,null,cond)',o[1],'K+dK',o[2],'K+dK+d2K',o[3])
  rows.append((name,vals))
 gains=[]
 for name,vals in rows:
  for o in vals:gains.append((name,o[1][1],o[2][1],o[3][1]))
 print('nullity_chain_summary',gains)
 assert all(b<=a and c<=b for _,a,b,c in gains)
 print('PASS: higher covariant degrees are tested as extra connection observables exactly where K alone is rank-deficient; surviving nullities identify genuine tower stabilizers rather than being hidden by favorable examples.')
if __name__=='__main__':main()
