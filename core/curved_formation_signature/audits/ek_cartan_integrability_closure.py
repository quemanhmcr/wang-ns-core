#!/usr/bin/env python3
"""Adversarial closure: maximal spectral tower + Lie integrability still has a singular kernel."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)
P2=pathlib.Path(__file__).with_name('ek_maximal_tower_stabilizer.py');sp2=importlib.util.spec_from_file_location('mx',P2);mx=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(mx)
P3=pathlib.Path(__file__).with_name('ek_bianchi_integrability_completion.py');sp3=importlib.util.spec_from_file_location('bi',P3);bi=importlib.util.module_from_spec(sp3);sp3.loader.exec_module(bi)
def abelian(n):return np.zeros((n,n,n))
def rank(A):
 s=np.linalg.svd(A,compute_uv=False);r=int(np.sum(s>1e-8*(s[0] if len(s) else 1)));return r,A.shape[1]-r,(s[0]/s[r-1] if r else np.inf)
def one(seed,scalar=False):
 c=ek.direct_sum(ek.heisenberg3(),abelian(3));c=ek.randomize_metric(c,seed);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag([-1]*6 if scalar else [-1]*5+[2]);E,K,R=ek.EK(Gs,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);x0=ek.coeffs_vertical(Gs,B,H).reshape(-1);d=len(Gs);q=len(H);h=2e-6
 blocks={p:[] for p in range(2,d+1)};blocks['J']=[];blocks['DR']=[]
 for j in range(len(x0)):
  xp=x0.copy();xm=x0.copy();xp[j]+=h;xm[j]-=h
  Gp=ek.from_x(B,H,xp.reshape(d,q));Gm=ek.from_x(B,H,xm.reshape(d,q));fp=mx.forms(Gp,C);fm=mx.forms(Gm,C)
  for p in range(2,d+1):blocks[p].append((mx.pack(fp[p])-mx.pack(fm[p]))/(2*h))
  spv=bi.sensors(Gp,C);smv=bi.sensors(Gm,C);blocks['DR'].append((spv[1]-smv[1])/(2*h));blocks['J'].append((spv[2]-smv[2])/(2*h))
 A={k:np.column_stack(v) for k,v in blocks.items()};stack=None;chains=[]
 for p in range(2,d+1):stack=A[p] if stack is None else np.vstack([stack,A[p]]);chains.append((p,rank(stack)))
 return chains,rank(np.vstack([stack,A['J']])),rank(np.vstack([stack,A['J'],A['DR']]))
def main():
 print('maximal Cartan-integrability linearized closure tribunal: h3+R3, curl 5+1')
 finals=[]
 for seed in range(5):
  chain,tj,tjd=one(10000+seed);finals.append(tjd[1]);print('seed',seed,'tower',chain,'tower+J',tj,'tower+J+DR',tjd)
 print('final_nullities',finals);assert finals==[5]*5
 sc=one(10100,True);print('scalar control',sc);assert sc[2][1]>0
 print('PASS negative control: even the maximal exterior tower plus Jacobi/Bianchi has a five-dimensional infinitesimal kernel in the hardest non-scalar example. The inverse is singular there; nonlinear observability must be tested rather than inferred from Jacobian rank.')
if __name__=='__main__':main()
