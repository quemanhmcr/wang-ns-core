#!/usr/bin/env python3
"""Near-minimal curvature measurements compile a large held-out geometry/dynamics zoo."""
from __future__ import annotations
import importlib.util,pathlib,itertools,numpy as np
from scipy.linalg import expm
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ek=load('ek','ek_exact_lie_reconstruction.py');hd=load('hd','ek_higher_degree_completion.py')

def abelian(n): return np.zeros((n,n,n))
def rel(a,b): return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def fC(C,kind,param):
 vals,U=np.linalg.eigh(C)
 if kind=='poly':
  co=param;fv=sum(co[k]*vals**k for k in range(len(co)))
 elif kind=='exp':fv=np.exp(param*vals)
 elif kind=='sin':fv=np.sin(param*vals)
 elif kind=='abs':fv=np.abs(vals-param)
 elif kind=='hinge':fv=np.maximum(vals-param,0)
 else:raise ValueError(kind)
 return (U*fv)@U.T
def conn(G,u): return sum(u[i]*G[i] for i in range(len(G)))
def Jof(c,u): return -np.einsum('i,ikb->kb',u,c)
def flow(c,C,nu,x): return (Jof(c,x)-nu*C@C)@x
def rk4(c,C,nu,x,dt,steps):
 x=x.copy()
 for _ in range(steps):
  k1=flow(c,C,nu,x);k2=flow(c,C,nu,x+.5*dt*k1);k3=flow(c,C,nu,x+.5*dt*k2);k4=flow(c,C,nu,x+dt*k3);x=x+dt*(k1+2*k2+2*k3+k4)/6
 return x
def pack_forms(G,C):
 E,K,R=ek.EK(G,C);F=K;out=[]
 for p in range(2,len(G)):
  F=hd.Dform(F,p,G);out.append(np.concatenate([F[k].ravel() for k in sorted(F)]))
 return out

def one(seed,ratio,noise=0.0):
 rng=np.random.default_rng(seed);c0=ek.direct_sum(ek.std_so3(),ek.std_so3(),abelian(2));c=ek.randomize_metric(c0,seed);G=ek.gamma_mats(ek.levi_from_structure(c));d=len(G);C=np.diag([-2]*3+[0]*3+[3]*2)
 E,K,R=ek.EK(G,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);xt=ek.coeffs_vertical(G,B,H).reshape(-1);y0,A=ek.codazzi_matrix(B,H,C);y=ek.flatten_K(K,d)-y0
 m=max(len(xt),int(np.ceil(ratio*len(xt))));P=rng.normal(size=(m,len(y)));P/=np.linalg.norm(P,axis=1,keepdims=True);M=P@A;obs=P@y
 if noise:
  z=rng.normal(size=m);obs=obs+noise*np.linalg.norm(obs)*z/np.linalg.norm(z)
 xr,*_=np.linalg.lstsq(M,obs,rcond=None);Gr=ek.from_x(B,H,xr.reshape(d,len(H)));cr=ek.structure_from_gamma(Gr);Rr=ek.curvature(Gr)
 # Compiler outputs: connection/bracket/curvature.
 errs=[rel(np.stack(Gr),np.stack(G)),rel(cr,c),rel(ek.flatten_K(Rr,d),ek.flatten_K(R,d))]
 # 40 held-out spectral connection/curvature readers.
 kinds=['poly','exp','sin','abs','hinge'];reader=[]
 for q in range(40):
  kind=kinds[q%len(kinds)];param=rng.normal(size=5) if kind=='poly' else rng.uniform(-2,2);F=fC(C,kind,param)
  u=rng.normal(size=d);i,j=sorted(rng.choice(d,2,replace=False));At=conn(G,u);Ar=conn(Gr,u)
  reader.append(rel(At@F-F@At,Ar@F-F@Ar)); reader.append(rel(R[i,j]@F-F@R[i,j],Rr[i,j]@F-F@Rr[i,j]))
 # Entire available higher tower.
 tf=pack_forms(G,C);rf=pack_forms(Gr,C);tower=[rel(a,b) for a,b in zip(tf,rf)]
 # 30 finite transport commutators, not part of fit.
 transports=[]
 for _ in range(30):
  u=rng.normal(size=d);v=rng.normal(size=d);eps=rng.uniform(.01,.2);A1=conn(G,u);B1=conn(G,v);A2=conn(Gr,u);B2=conn(Gr,v)
  H1=expm(eps*A1)@expm(eps*B1)@expm(-eps*A1)@expm(-eps*B1)
  H2=expm(eps*A2)@expm(eps*B2)@expm(-eps*A2)@expm(-eps*B2);transports.append(rel(H1,H2))
 # Frozen formation response/propagators for unseen u,nu.
 responses=[]
 for _ in range(30):
  u=rng.normal(size=d);nu=10**rng.uniform(-2,0);L=Jof(c,u)-nu*C@C;Lr=Jof(cr,u)-nu*C@C;t=rng.uniform(.01,.2)
  responses.append(rel(L,Lr));responses.append(rel(expm(t*L),expm(t*Lr)))
 # Nonlinear diagonal trajectories for unseen initial states and viscosities.
 traj=[]
 for _ in range(12):
  x=rng.normal(size=d);nu=10**rng.uniform(-2,0);traj.append(rel(rk4(c,C,nu,x,5e-4,120),rk4(cr,C,nu,x,5e-4,120)))
 s=np.linalg.svd(M,compute_uv=False);rank=int(np.sum(s>1e-10*s[0]));cond=s[0]/s[rank-1] if rank else np.inf
 return dict(unknown=len(xt),m=m,rank=rank,cond=cond,xerr=rel(xr,xt),base=max(errs),reader=max(reader),tower=max(tower),transport=max(transports),response=max(responses),traj=max(traj))

def main():
 print('compressed universal compiler tribunal: d=8 exact metric-Lie geometry, 56 E-hidden coefficients')
 rows=[]
 for ratio in [1.0,1.1,1.25,1.5,2.0]:
  vals=[one(20000+s,ratio) for s in range(3)];rows.extend(vals)
  print('ratio',ratio,'rows',[(v['m'],v['rank'],round(v['cond'],2),v['xerr'],v['reader'],v['tower'],v['transport'],v['response'],v['traj']) for v in vals])
 # Near-minimal square systems can be ill-conditioned but should generically identify; mild oversampling must be precise.
 good=[v for v in rows if v['m']>=int(1.25*v['unknown'])]
 assert all(v['rank']==v['unknown'] for v in good)
 assert max(v['reader'] for v in good)<1e-9 and max(v['tower'] for v in good)<1e-8 and max(v['transport'] for v in good)<1e-9 and max(v['response'] for v in good)<1e-9 and max(v['traj'] for v in good)<1e-8
 # Noise slope at 1.5x measurement budget.
 errs=[]
 for eps in [1e-10,1e-8,1e-6,1e-4]:
  v=one(20123,1.5,eps);errs.append((eps,v['xerr']));print('noise',eps,'xerr',v['xerr'],'reader',v['reader'],'traj',v['traj'])
 slope=np.polyfit(np.log10([x for x,y in errs]),np.log10([y for x,y in errs]),1)[0];print('noise_slope',slope);assert .8<slope<1.2
 print('PASS: roughly one scalar curvature equation per hidden connection coefficient, with mild oversampling, compiles a large held-out zoo: full curvature, higher jets, arbitrary spectral readers, finite transport commutators, frozen propagators and nonlinear trajectories. The compact data act as a geometry compiler, not a task-specific fit.')
if __name__=='__main__':main()
