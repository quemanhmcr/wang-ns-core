#!/usr/bin/env python3
from __future__ import annotations
import itertools
import numpy as np

rng=np.random.default_rng(202608212128)

def rel(a,b): return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def comm(A,B): return A@B-B@A

def levi_from_structure(c):
    # c[k,i,j]=component k of [e_i,e_j], Euclidean metric.
    d=c.shape[0]; G=np.zeros((d,d,d)) # G[k,i,j] output k of nabla_i e_j
    for k in range(d):
      for i in range(d):
       for j in range(d):
        G[k,i,j]=.5*(c[k,i,j]-c[i,j,k]+c[j,k,i])
    return G

def gamma_mats(G): return [G[:,i,:].copy() for i in range(G.shape[1])]
def structure_from_gamma(Gs):
    d=len(Gs); c=np.zeros((d,d,d)); I=np.eye(d)
    for i in range(d):
      for j in range(d): c[:,i,j]=Gs[i]@I[j]-Gs[j]@I[i]
    return c

def curvature(Gs):
    d=len(Gs); c=structure_from_gamma(Gs); R={}
    for i,j in itertools.combinations(range(d),2):
      Gbr=sum(c[k,i,j]*Gs[k] for k in range(d))
      R[i,j]=comm(Gs[i],Gs[j])-Gbr
    return R

def EK(Gs,C):
    E=[comm(A,C) for A in Gs]; R=curvature(Gs); K={p:comm(A,C) for p,A in R.items()}; return E,K,R

def std_so3():
    c=np.zeros((3,3,3));
    c[0,1,2]=c[1,2,0]=c[2,0,1]=1
    c[0,2,1]=c[2,1,0]=c[1,0,2]=-1
    return c

def heisenberg3():
    c=np.zeros((3,3,3)); c[2,0,1]=1;c[2,1,0]=-1; return c

def se2():
    c=np.zeros((3,3,3)); # [r,x]=y, [r,y]=-x
    c[1,0,2]=-1;c[1,2,0]=1; c[2,0,1]=1;c[2,1,0]=-1; return c

def direct_sum(*cs):
    d=sum(c.shape[0] for c in cs); out=np.zeros((d,d,d));o=0
    for c in cs:
      n=c.shape[0];out[o:o+n,o:o+n,o:o+n]=c;o+=n
    return out

def transform_structure(c,S):
    # z coordinates, physical vector x=S z; bracket_z=S^-1 [S.,S.]
    Sinv=np.linalg.inv(S)
    return np.einsum('ka,aij,ib,jc->kbc',Sinv,c,S,S)

def randomize_metric(c,seed):
    rr=np.random.default_rng(seed);d=c.shape[0]
    Q,_=np.linalg.qr(rr.normal(size=(d,d))); scales=np.exp(rr.uniform(-.9,.9,size=d)); S=Q@np.diag(scales)
    return transform_structure(c,S)

def vertical_basis(C,tol=1e-10):
    vals,Q=np.linalg.eigh(C); blocks=[]; used=np.zeros(len(vals),bool)
    for i,x in enumerate(vals):
      if used[i]:continue
      ids=np.where(np.abs(vals-x)<tol)[0];used[ids]=True;blocks.append(ids)
    H=[]
    for ids in blocks:
      for aa in range(len(ids)):
       for bb in range(aa+1,len(ids)):
        M=np.zeros((len(vals),len(vals)));i,j=ids[aa],ids[bb];M[i,j]=1;M[j,i]=-1;H.append(Q@M@Q.T)
    return vals,Q,blocks,H

def B_from_E(E,C,tol=1e-10):
    vals,Q=np.linalg.eigh(C); out=[]
    for Ei in E:
      X=Q.T@Ei@Q;B=np.zeros_like(X)
      for a in range(len(vals)):
       for b in range(len(vals)):
        gap=vals[b]-vals[a]
        if abs(gap)>tol:B[a,b]=X[a,b]/gap
      out.append(Q@B@Q.T)
    return out

def coeffs_vertical(Gs,B,H):
    return np.array([[np.vdot(h,Gs[i]-B[i]).real/np.vdot(h,h).real for h in H] for i in range(len(Gs))])
def from_x(B,H,x):
    return [B[i]+sum((x[i,j]*H[j] for j in range(len(H))),start=np.zeros_like(B[i])) for i in range(len(B))]
def flatten_K(K,d): return np.concatenate([K[i,j].ravel() for i,j in itertools.combinations(range(d),2)])

def codazzi_matrix(B,H,C):
    d=len(B); q=len(H); _,K0,_=EK(B,C); y0=flatten_K(K0,d); cols=[]
    # Exact finite difference: K is affine-linear in vertical coefficients if the theory is right.
    for i in range(d):
      for a,h in enumerate(H):
        X=[z.copy() for z in B];X[i]=X[i]+h;_,K,_=EK(X,C);cols.append(flatten_K(K,d)-y0)
    return y0,np.column_stack(cols) if cols else np.zeros((len(y0),0))

def jacobi(c):
    d=c.shape[0];w=0
    for i,j,k in itertools.product(range(d),repeat=3):
      v=np.zeros(d)
      for a in range(d): v += c[a,j,k]*c[:,i,a]+c[a,k,i]*c[:,j,a]+c[a,i,j]*c[:,k,a]
      w=max(w,np.linalg.norm(v))
    return w

def case(name,c,roots,seed,noise=0):
    c=randomize_metric(c,seed);G=levi_from_structure(c);Gs=gamma_mats(G);d=len(Gs)
    # sanity
    skew=max(np.linalg.norm(A+A.T) for A in Gs); jac=jacobi(c)
    C=np.diag(np.array(roots,float));E,K,R=EK(Gs,C);B=B_from_E(E,C);vals,Q,blocks,H=vertical_basis(C)
    xt=coeffs_vertical(Gs,B,H).reshape(-1)
    y0,A=codazzi_matrix(B,H,C);y=flatten_K(K,d)-y0
    # affine-linearity adversarial superposition test
    lin=0.0
    if len(xt):
      x1=rng.normal(size=xt.shape);x2=rng.normal(size=xt.shape)
      def kv(x): return flatten_K(EK(from_x(B,H,x.reshape(d,-1)),C)[1],d)-y0
      lin=rel(kv(x1+x2),kv(x1)+kv(x2))
    if noise and len(y):
      z=rng.normal(size=y.shape);y=y+noise*max(np.linalg.norm(y),1.0)*z/np.linalg.norm(z)
    if A.shape[1]:
      s=np.linalg.svd(A,compute_uv=False); rank=int(np.sum(s>1e-10*s[0])); null=A.shape[1]-rank; cond=s[0]/s[rank-1] if rank else np.inf
      xr,*_=np.linalg.lstsq(A,y,rcond=None)
    else: rank=null=0;cond=1;xr=np.zeros(0)
    Grec=from_x(B,H,xr.reshape(d,-1) if len(H) else np.zeros((d,0)))
    gerr=rel(np.stack(Grec),np.stack(Gs));
    # descendants: bracket/T, R, random J/L and trajectory
    crec=structure_from_gamma(Grec); terr=rel(crec,c); Rrec=curvature(Grec); rerr=rel(flatten_K({p:Rrec[p] for p in Rrec},d),flatten_K(R,d))
    u=rng.normal(size=d);b=rng.normal(size=d);nu=.173
    # J_u defined by <a,J_u b>=-<u,[a,b]>, so J[k,b] = -sum_i u_i c[i,k,b]? output k via test a=e_k
    def Jof(cc,u): return -np.einsum('i,ikb->kb',u,cc)
    J=Jof(c,u);Jr=Jof(crec,u); jerr=rel(Jr,J)
    L=J-nu*C@C;Lr=Jr-nu*C@C;lerr=rel(Lr,L)
    # RK4 diagonal formation flow
    def flow(cc,x): return (Jof(cc,x)-nu*C@C)@x
    x=u.copy();z=u.copy();dt=1e-3
    for _ in range(80):
      def step(cc,q):
       k1=flow(cc,q);k2=flow(cc,q+.5*dt*k1);k3=flow(cc,q+.5*dt*k2);k4=flow(cc,q+dt*k3);return q+dt*(k1+2*k2+2*k3+k4)/6
      x=step(c,x);z=step(crec,z)
    traj=rel(z,x)
    return dict(name=name,d=d,q=len(H),unknown=A.shape[1],rank=rank,null=null,cond=cond,skew=skew,jac=jac,lin=lin,gerr=gerr,terr=terr,rerr=rerr,jerr=jerr,lerr=lerr,traj=traj)

def main():
    families=[
      ('so3+so3',direct_sum(std_so3(),std_so3()),[-1,-1,-1,2,2,2]),
      ('so3+h3',direct_sum(std_so3(),heisenberg3()),[-2,-2,0,0,3,3]),
      ('so3+se2',direct_sum(std_so3(),se2()),[-1,-1,-1,1,1,1]),
      ('h3+se2',direct_sum(heisenberg3(),se2()),[-2,-2,-1,1,2,2]),
    ]
    rows=[]
    for name,c,r in families:
      for seed in range(4): rows.append(case(name,c,r,100+seed))
    print('E+K exact metric-Lie reconstruction tribunal')
    print('family d hidden rank null cond linearity Gamma bracket R J L traj')
    for x in rows:
      print(f"{x['name']:10s} {x['d']} {x['unknown']:3d} {x['rank']:3d} {x['null']:2d} {x['cond']:7.2f} {x['lin']:.1e} {x['gerr']:.1e} {x['terr']:.1e} {x['rerr']:.1e} {x['jerr']:.1e} {x['lerr']:.1e} {x['traj']:.1e}")
    # report rather than assume all families identifiable; generic theorem must survive adversarial algebras.
    full=[x for x in rows if x['null']==0]
    print('full_rank_cases',len(full),'/',len(rows))
    if full:
      print('worst_full_rank_Gamma',max(x['gerr'] for x in full),'worst_traj',max(x['traj'] for x in full))
    # noise ladder on a full-rank representative, if available
    base=None
    for fam,c,r in families:
      t=case(fam,c,r,777)
      if t['null']==0: base=(fam,c,r);break
    if base:
      errs=[]
      print('noise ladder',base[0])
      for eps in [1e-10,1e-8,1e-6,1e-4]:
        x=case(base[0],base[1],base[2],777,noise=eps);errs.append((eps,x['gerr']));print(eps,x['gerr'])
      sl=np.polyfit(np.log10([a for a,b in errs]),np.log10([b for a,b in errs]),1)[0];print('noise_slope',sl)
      assert .65<sl<1.35
    assert max(x['skew'] for x in rows)<1e-10 and max(x['jac'] for x in rows)<1e-10
    assert max(x['lin'] for x in rows)<1e-10
    assert full and max(x['gerr'] for x in full)<1e-9 and max(x['traj'] for x in full)<1e-8
    print('PASS: K is affine-linear in the E-hidden stabilizer connection; whenever the Codazzi map has full rank, (g,C,E,K) reconstructs connection, bracket, curvature, Poisson/formation operators and trajectories. Rank-deficient cases are retained as genuine obstructions.')
if __name__=='__main__':main()
