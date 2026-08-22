#!/usr/bin/env python3
"""Noise stability of degree-16 law archaeology in the exact 160-node helical window."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
fh=loadpath('fh',ROOT/'research'/'theory2_universal_compiler'/'audits'/'full_helical_one_state_recovers_union_graph.py')
hg=loadpath('hg',ROOT/'research'/'theory2_universal_compiler'/'audits'/'exact_helical_sparse_state_law_holography.py')
P3=[(0,0,1),(0,1,-1),(1,-1,-1)]
def rp(e):
 (q,sq),(r,t)=e;return (round(t*np.linalg.norm(r),12),round(sq*np.linalg.norm(q),12))
def complement(N):
 U,s,Vh=np.linalg.svd(N.T,full_matrices=True);return Vh[N.shape[1]:].T
def tangent_noise(N,seed):
 rng=np.random.default_rng(seed);lam=np.array([s*np.linalg.norm(k) for k,s in N]);Z=rng.normal(size=(len(N),len(N)))+1j*rng.normal(size=(len(N),len(N)));Z=(Z+Z.conj().T)/2
 Z[np.abs(lam[:,None]-lam[None,:])<1e-10]=0;return Z
def extract_q(N,E,M,R,Nspec):
 # weighted one-E polynomial least singular direction modulo all-spectrum relations
 Qc=complement(Nspec);G=np.zeros((len(M),len(M)),complex)
 lam=np.array([s*np.linalg.norm(k) for k,s in N])
 # aggregate by root pair for speed
 weights={}
 for i,x in enumerate(lam):
  for j,y in enumerate(lam):
   w=abs(E[i,j])**2
   if w>0:weights[(round(float(x),12),round(float(y),12))]=weights.get((round(float(x),12),round(float(y),12)),0.0)+w
 for (x,y),w in weights.items():
  v=hg.evalrow(x,y,M,R).astype(complex);G+=w*np.outer(v.conj(),v)
 H=Qc.conj().T@G@Qc;ev,V=np.linalg.eigh((H+H.conj().T)/2);q=Qc@V[:,0];q=np.real_if_close(q,tol=1000);q=np.real(q);q/=np.linalg.norm(q);return q,ev[:5]
def main():
 K=fh.window(6);Pall=fh.support_reps(3);full={rp(e) for e in fh.structural_union(Pall,K)};roots=sorted({x for z in full for x in z});allp={(x,y) for x in roots for y in roots if x!=y};forbid=allp-full;D=16;M=hg.mons(D);R=max(abs(x) for x in roots)
 As=np.array([hg.evalrow(x,y,M,R) for x,y in sorted(allp)]);Nspec,rs,ss=hg.nullspace(As);Ap=np.array([hg.evalrow(x,y,M,R) for x,y in sorted(full)]);Nphys,rp0,sp=hg.nullspace(Ap);Ux,sx=hg.quotient_extra(Nphys,Nspec);qcat=np.real(Ux[:,0]);qcat/=np.linalg.norm(qcat)
 N,E=hg.exact_E_matrix(hg.dense_on(P3,38000),K);Z=tangent_noise(N,38100);Z*=np.linalg.norm(E)/np.linalg.norm(Z)
 rng=[]
 for eps in [0,1e-10,1e-8,1e-6,1e-5,1e-4,1e-3,1e-2,3e-2,1e-1,3e-1,1.0]:
  q,ev=extract_q(N,E+eps*Z,M,R,Nspec);cc=abs(float(np.dot(q,qcat)));scores=[(abs(float(np.dot(q,hg.evalrow(x,y,M,R)))),(x,y)) for x,y in allp];scores.sort(reverse=True);pred={xy for s,xy in scores[:len(forbid)]};active=[s for s,xy in scores if xy in full];bad=[s for s,xy in scores if xy in forbid];gap=min(bad)/max(max(active),1e-30);rng.append((eps,cc,pred==forbid,gap,ev[0],ev[1] if len(ev)>1 else np.nan));print('eps',eps,'relation_cos',cc,'forbidden_exact',pred==forbid,'separation',gap,'eig0/eig1',ev[:2])
 assert all(ok for eps,cc,ok,g,e0,e1 in rng if eps<=1e-4)
 assert min(cc for eps,cc,ok,g,e0,e1 in rng if eps<=1e-4)>.999
 print('PASS: exact-helical law archaeology is stable under orbit-tangent perturbations. The degree-16 physical relation remains aligned and identifies all twelve forbidden root transitions through relative noise 1e-4; higher noise levels are reported rather than hidden.')
if __name__=='__main__':main()
