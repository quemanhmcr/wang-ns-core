#!/usr/bin/env python3
"""Negative control: one snapshot cannot identify the full polarized mother/connection one-form, even when it identifies the presentation category."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')
cl=loadpath('cl',ROOT/'research'/'theory2_universal_compiler'/'audits'/'closed_form_selection_law.py')

def inv_adC(H,C):
 vals,U=np.linalg.eigh((C+C.T)/2);X=U.T@H@U;A=np.zeros_like(X)
 for i,x in enumerate(vals):
  for j,y in enumerate(vals):
   if abs(y-x)>1e-10:A[i,j]=X[i,j]/(y-x)
 return U@A@U.T

def subspace_min_cos(A,B):
 Qa,_=np.linalg.qr(A);Qb,_=np.linalg.qr(B);return float(np.min(np.linalg.svd(Qa.T@Qb,compute_uv=False)))
def main():
 data=mu.build_physical_tensors(False);C=data['C'];Gamma=data['Gamma'];_,Es=mu.mother_tensor(Gamma,C);d=len(C);rng=np.random.default_rng(45000)
 # Build a random presentation-respecting mother direction H outside the physical 28D mother image.
 vals,U=np.linalg.eigh((C+C.T)/2);groups=[]
 for i,x in enumerate(vals):
  if not groups or abs(x-groups[-1][0])>1e-8:groups.append([float(x),[i]])
  else:groups[-1][1].append(i)
 Ehs=[U.T@E@U for E in Es];active=set()
 for a,(x,I) in enumerate(groups):
  for b,(y,J) in enumerate(groups):
   if a==b:continue
   if np.sqrt(sum(np.linalg.norm(Eh[np.ix_(I,J)])**2 for Eh in Ehs))>1e-10:active.add((a,b))
 Hh=np.zeros((d,d))
 for a,(x,I) in enumerate(groups):
  for b in range(a+1,len(groups)):
   if (a,b) not in active:continue
   J=groups[b][1];B=rng.normal(size=(len(I),len(J)));Hh[np.ix_(I,J)]=B;Hh[np.ix_(J,I)]=B.T
 H=U@Hh@U.T
 # project H off the physical mother image while staying inside the same active support linear space
 M=np.column_stack([E.reshape(-1) for E in Es]);coef=np.linalg.lstsq(M,H.reshape(-1),rcond=None)[0];H=(H.reshape(-1)-M@coef).reshape(d,d);H/=np.linalg.norm(H)
 Ah=inv_adC(H,C);comm=Ah@C-C@Ah;assert np.linalg.norm(comm-H)<1e-10 and np.linalg.norm(Ah+Ah.T)<1e-10
 # training state and a coefficient covector alpha orthogonal to it
 u0=rng.normal(size=d);alpha=rng.normal(size=d);alpha-=u0*np.dot(alpha,u0)/np.dot(u0,u0);alpha/=np.linalg.norm(alpha);delta=2.0
 Ealt=[Es[i]+delta*alpha[i]*H for i in range(d)]
 # modify the metric-compatible connection one-form consistently: E'_i=[Gamma'_i,C]
 Gs=[mu.conn_matrix(Gamma,np.eye(d)[i]) for i in range(d)];Galt=[Gs[i]+delta*alpha[i]*Ah for i in range(d)]
 train=sum(u0[i]*Es[i] for i in range(d));train2=sum(u0[i]*Ealt[i] for i in range(d));Gt=sum(u0[i]*Gs[i] for i in range(d));Gt2=sum(u0[i]*Galt[i] for i in range(d))
 print('training snapshot E collision',np.linalg.norm(train-train2),'connection collision',np.linalg.norm(Gt-Gt2))
 # both mother maps remain injective but are different polarized geometries
 A0=np.column_stack([E.reshape(-1) for E in Es]);A1=np.column_stack([E.reshape(-1) for E in Ealt]);r0=np.linalg.matrix_rank(A0);r1=np.linalg.matrix_rank(A1);csub=subspace_min_cos(A0,A1)
 print('mother ranks',r0,r1,'image_min_principal_cos',csub,'map_rel_difference',np.linalg.norm(A1-A0)/np.linalg.norm(A0))
 # same three-law presentation for random unseen directions, but order-one disagreement in actual mother/connection values
 ed=[];gd=[];nulls=[]
 for j in range(30):
  v=rng.normal(size=d);E0=sum(v[i]*Es[i] for i in range(d));E1=sum(v[i]*Ealt[i] for i in range(d));G0=sum(v[i]*Gs[i] for i in range(d));G1=sum(v[i]*Galt[i] for i in range(d));ed.append(np.linalg.norm(E1-E0)/max(np.linalg.norm(E0),1e-30));gd.append(np.linalg.norm(G1-G0)/max(np.linalg.norm(G0),1e-30));AA=C@C-np.eye(d);q=AA@(C@C@E1+E1@C@C-5*E1)@AA;assert np.linalg.norm(q)<1e-10
  W=loadpath('ex'+str(j),ROOT/'research'/'theory2_universal_compiler'/'audits'/'extract_degree7_new_relation.py').words(C,E1,8);s=np.linalg.svd(W,compute_uv=False);nulls.append(W.shape[1]-int(np.sum(s>1e-10*s[0])))
 print('unseen mother diff median/max',float(np.median(ed)),max(ed),'connection diff median/max',float(np.median(gd)),max(gd),'degree8_nullities',sorted(set(nulls)))
 assert np.linalg.norm(train-train2)<1e-12 and np.linalg.norm(Gt-Gt2)<1e-12 and r0==r1==d and csub<.999 and np.median(ed)>.05 and set(nulls)=={28}
 print('PASS negative control: one snapshot can determine the generator-relations category yet cannot determine the full polarized mother/connection one-form. Two distinct metric-compatible connection families share exactly the training (C,E_u,Gamma_u) snapshot and the same three-law presentation, but differ order-one on unseen directions. Polarized E,K data remain essential for formation-geometry coefficients.')
if __name__=='__main__':main()
