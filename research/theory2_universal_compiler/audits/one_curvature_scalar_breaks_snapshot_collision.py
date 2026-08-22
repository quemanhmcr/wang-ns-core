#!/usr/bin/env python3
"""A single generic curvature scalar resolves a continuous geometry ambiguity invisible to one snapshot."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')

def inv_adC(H,C):
 vals,U=np.linalg.eigh((C+C.T)/2);X=U.T@H@U;A=np.zeros_like(X)
 for i,x in enumerate(vals):
  for j,y in enumerate(vals):
   if abs(y-x)>1e-10:A[i,j]=X[i,j]/(y-x)
 return U@A@U.T

def comm(A,B):return A@B-B@A
def Gof(Gs,x):return sum(x[i]*Gs[i] for i in range(len(Gs)))
def Kpair(Gs,C,u,v):
 Gu=Gof(Gs,u);Gv=Gof(Gs,v);br=Gu@v-Gv@u;R=comm(Gu,Gv)-Gof(Gs,br);return comm(R,C)
def build(seed=46000):
 data=mu.build_physical_tensors(False);C=data['C'];Gamma=data['Gamma'];_,Es=mu.mother_tensor(Gamma,C);d=len(C);rng=np.random.default_rng(seed);Gs=[mu.conn_matrix(Gamma,np.eye(d)[i]) for i in range(d)]
 vals,U=np.linalg.eigh((C+C.T)/2);groups=[]
 for i,x in enumerate(vals):
  if not groups or abs(x-groups[-1][0])>1e-8:groups.append([float(x),[i]])
  else:groups[-1][1].append(i)
 Ehs=[U.T@E@U for E in Es];active=set()
 for a,(x,I) in enumerate(groups):
  for b,(y,J) in enumerate(groups):
   if a!=b and np.sqrt(sum(np.linalg.norm(Eh[np.ix_(I,J)])**2 for Eh in Ehs))>1e-10:active.add((a,b))
 Hh=np.zeros((d,d))
 for a,(x,I) in enumerate(groups):
  for b in range(a+1,len(groups)):
   if (a,b) not in active:continue
   J=groups[b][1];B=rng.normal(size=(len(I),len(J)));Hh[np.ix_(I,J)]=B;Hh[np.ix_(J,I)]=B.T
 H=U@Hh@U.T;M=np.column_stack([E.reshape(-1) for E in Es]);coef=np.linalg.lstsq(M,H.reshape(-1),rcond=None)[0];H=(H.reshape(-1)-M@coef).reshape(d,d);H/=np.linalg.norm(H);A=inv_adC(H,C)
 u=rng.normal(size=d)
 # alpha orthogonal to u and A u => curvature along (u,v) is affine in delta, with no delta^2 term.
 alpha=rng.normal(size=d);B=np.column_stack([u,A@u]);alpha-=B@np.linalg.lstsq(B,alpha,rcond=None)[0];alpha/=np.linalg.norm(alpha)
 assert abs(alpha@u)<1e-12 and abs(alpha@(A@u))<1e-12
 def fam(delta):return [Gs[i]+delta*alpha[i]*A for i in range(d)]
 return C,Gs,fam,u,rng

def main():
 C,G0,fam,u,rng=build();d=len(C)
 # snapshot is independent of delta
 snap=[Gof(fam(x),u) for x in [-2,-.5,0,1,3]];print('snapshot_connection_spread',max(np.linalg.norm(A-snap[0]) for A in snap));assert max(np.linalg.norm(A-snap[0]) for A in snap)<1e-11
 # Find generic scalar probes with adequate sensitivity, then use one scalar to estimate delta.
 trials=[]
 for t in range(80):
  for _ in range(100):
   v,w,z=[rng.normal(size=d) for j in range(3)];K0=Kpair(fam(0),C,u,v);K1=Kpair(fam(1),C,u,v);a=float(z@(K0@w));b=float(z@((K1-K0)@w))
   if abs(b)>1e-2:break
  delta=rng.uniform(-2,2);Kt=Kpair(fam(delta),C,u,v);y=float(z@(Kt@w));dh=(y-a)/b;aff=abs(float(z@((Kpair(fam(2),C,u,v)-2*K1+K0)@w)))/max(abs(b),1e-30);trials.append((abs(dh-delta),abs(b),aff))
 print('80 one-scalar recoveries median/max err',float(np.median([x[0] for x in trials])),max(x[0] for x in trials),'min sensitivity',min(x[1] for x in trials),'max affine defect',max(x[2] for x in trials))
 assert max(x[0] for x in trials)<1e-10 and max(x[2] for x in trials)<1e-10
 # Noise ladder on one fixed scalar channel.
 v,w,z=[rng.normal(size=d) for j in range(3)];K0=Kpair(fam(0),C,u,v);K1=Kpair(fam(1),C,u,v);a=float(z@(K0@w));b=float(z@((K1-K0)@w));
 if abs(b)<1e-3: raise RuntimeError('unlucky scalar channel')
 delta=.73;true=a+b*delta;rows=[]
 for eps in [1e-10,1e-8,1e-6,1e-4]:
  ee=[]
  for j in range(200):
   y=true+eps*max(abs(true),1.0)*rng.normal();ee.append(abs((y-a)/b-delta))
  rows.append((eps,float(np.median(ee))))
 slope=np.polyfit(np.log10([x for x,y in rows]),np.log10([y for x,y in rows]),1)[0];print('noise',rows,'slope',slope);assert .9<slope<1.1
 print('PASS: a continuous family of metric-compatible connections is exactly invisible at the chosen (C,E_u,Gamma_u) snapshot, yet one generic scalar curvature polarization recovers the hidden geometry parameter in 80/80 trials, with linear noise stability.')
if __name__=='__main__':main()
