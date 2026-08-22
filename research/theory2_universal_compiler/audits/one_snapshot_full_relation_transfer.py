#!/usr/bin/env python3
"""Does the entire degree-8 relation space learned from one mother transfer to unseen physical mothers?"""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
ex=loadpath('ex',ROOT/'research'/'theory2_universal_compiler'/'audits'/'extract_degree7_new_relation.py')
ctrl=loadpath('ctrl',ROOT/'research'/'theory2_universal_compiler'/'audits'/'same_spectrum_support_control.py')

def nullspace(W,tol=1e-10):
 U,s,Vh=np.linalg.svd(W,full_matrices=False);r=int(np.sum(s>tol*s[0]));return Vh[r:].T,r

def subspace_cos(N1,N2):
 s=np.linalg.svd(N1.T@N2,compute_uv=False);return s

def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(35100);L=8
 a=rng.normal(size=28);E0=sum(a[i]*Es[i] for i in range(28));W0=ex.words(C,E0,L);N0,r0=nullspace(W0);print('train rank/nullity',r0,N0.shape[1]);assert N0.shape[1]==28
 relres=[];angles=[]
 for j in range(80):
  b=rng.normal(size=28);E=sum(b[i]*Es[i] for i in range(28));W=ex.words(C,E,L);N,r=nullspace(W);res=np.linalg.norm(W@N0)/max(np.linalg.norm(W)*np.linalg.norm(N0),1e-30);relres.append(res);cs=subspace_cos(N0,N);angles.append(np.min(cs))
 print('unseen80 transfer residual median/max',float(np.median(relres)),max(relres),'min_principal_cos',min(angles))
 # Same spectrum but generic full offblock matrix: only spectral relations should remain; physical extra relations fail.
 Ec=ctrl.full_offblock_control(C,35200);Wc=ex.words(C,Ec,L);Nc,rc=nullspace(Wc);cres=np.linalg.norm(Wc@N0)/max(np.linalg.norm(Wc)*np.linalg.norm(N0),1e-30)

 # isolate the four physical-specific relation directions modulo the 24D common spectral nullspace
 X=N0-Nc@(Nc.T@N0);Ux,sx,Vx=np.linalg.svd(X,full_matrices=False);extra=Ux[:,:4]
 extra_control=np.linalg.norm(Wc@extra)/max(np.linalg.norm(Wc)*np.linalg.norm(extra),1e-30)
 extra_phys=[]
 for j in range(12):
  b=rng.normal(size=28);E=sum(b[i]*Es[i] for i in range(28));W=ex.words(C,E,L);extra_phys.append(np.linalg.norm(W@extra)/max(np.linalg.norm(W)*np.linalg.norm(extra),1e-30))
 print('same_spectrum_control rank/nullity',rc,Nc.shape[1],'whole_train_relation_residual',cres,'extra_singulars',sx[:6],'physical_extra_control_residual',extra_control,'unseen_physical_extra_max',max(extra_phys),'separation',extra_control/max(max(extra_phys),1e-30))
 assert max(relres)<1e-11 and min(angles)>.999999999
 assert Nc.shape[1]==24 and sx[3]>.99 and sx[4]<1e-8 and extra_control/max(max(extra_phys),1e-30)>1e6
 print('PASS: the complete 28-dimensional degree-8 word-relation space learned numerically from one generic physical mother is identical across 80 unseen physical states, yet does not transfer to a same-spectrum generic offblock law. The snapshot reveals a state-independent presentation, not merely one selection polynomial.')
if __name__=='__main__':main()
