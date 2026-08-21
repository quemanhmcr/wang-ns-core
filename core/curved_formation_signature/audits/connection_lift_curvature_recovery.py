#!/usr/bin/env python3
import itertools,numpy as np
rng=np.random.default_rng(20260901)

def comm(A,B):return A@B-B@A
def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def vbasis(r):
 B=[];n=len(r)
 for i in range(n):
  for j in range(i+1,n):
   if r[i]==r[j]:
    M=np.zeros((n,n));M[i,j]=1;M[j,i]=-1;B.append(M)
 return B
def vertical(A,r):
 P=np.zeros_like(A)
 for i,x in enumerate(r):
  for j,y in enumerate(r):
   if x==y:P[i,j]=A[i,j]
 return P
def fromE(E,r):
 D=np.zeros_like(E)
 for i,x in enumerate(r):
  for j,y in enumerate(r):
   if y!=x:D[i,j]=E[i,j]/(y-x)
 return D

def run(roots,m,noise=0,vertical_only=False):
 roots=np.array(roots,float);n=len(roots);C=np.diag(roots);VB=vbasis(list(roots));q=len(VB)
 D=[]
 for _ in range(m):
  X=rng.normal(size=(n,n));X=X-X.T
  if vertical_only:X=vertical(X,roots)
  D.append(X)
 E=[comm(X,C) for X in D];Dp=[fromE(X,roots) for X in E]
 pairs=list(itertools.combinations(range(m),2))
 K={(i,j):comm(comm(D[i],D[j]),C) for i,j in pairs}
 K0={(i,j):comm(comm(Dp[i],Dp[j]),C) for i,j in pairs}
 target=np.concatenate([(K[p]-K0[p]).ravel() for p in pairs])
 if noise:
  z=rng.normal(size=target.shape);target += noise*max(np.linalg.norm(target),1)*z/max(np.linalg.norm(z),1e-30)
 cols=[]
 for slot in range(m):
  for B in VB:
   out=[]
   for i,j in pairs:
    Vi=B if i==slot else np.zeros((n,n));Vj=B if j==slot else np.zeros((n,n))
    dR=comm(Vi,Dp[j])+comm(Dp[i],Vj);out.append(comm(dR,C).ravel())
   cols.append(np.concatenate(out))
 A=np.column_stack(cols) if cols else np.zeros((len(target),0))
 if A.shape[1]==0:return 0,0,0,0,0
 s=np.linalg.svd(A,compute_uv=False);rank=int(np.sum(s>1e-10*(s[0] if len(s) else 1)));null=A.shape[1]-rank;x,*_=np.linalg.lstsq(A,target,rcond=None)
 true=np.concatenate([vertical(X,roots).ravel() for X in D]);rec=[]
 for slot in range(m):
  V=np.zeros((n,n))
  for j,B in enumerate(VB):V+=x[slot*q+j]*B
  rec.append(V.ravel())
 err=rel(np.concatenate(rec),true);cond=s[0]/s[rank-1] if rank else np.inf
 return q,A.shape[1],null,err,cond

cases=[('2+1+2+1',[-2,-2,-1,1,1,3],6),('3+3',[-1,-1,-1,2,2,2],6),('2+2+2',[-2,-2,0,0,3,3],6),('4+4',[-1]*4+[2]*4,8)]
print('connection vertical-lift recovery from E+K')
out={}
for name,r,m in cases:
 q,u,n,e,c=run(r,m);out[name]=(q,u,n,e,c);print(f'{name:10s} vertical_per_direction={q:2d} unknown={u:3d} nullity={n:3d} relerr={e:.3e} cond={c:.2e}')
# generic cases should be fully identified in these tests
assert all(v[2]==0 and v[3]<3e-12 for v in out.values())
print('noise ladder 3+3')
errs=[]
for eps in [1e-10,1e-8,1e-6,1e-4]:
 q,u,n,e,c=run(cases[1][1],6,noise=eps);errs.append((eps,e));print(eps,e)
sl=np.polyfit(np.log10([x for x,y in errs]),np.log10([y for x,y in errs]),1)[0];print('noise_slope',sl);assert .7<sl<1.3
q,u,n,e,c=run(cases[1][1],6,vertical_only=True);print('vertical-only dark control',q,u,n,e,c);assert n==u
print('PASS: E fixes the horizontal connection quotient; K generically reconstructs the missing curl-commuting connection lift. A connection living entirely in the spectral commutant remains genuinely invisible.')
