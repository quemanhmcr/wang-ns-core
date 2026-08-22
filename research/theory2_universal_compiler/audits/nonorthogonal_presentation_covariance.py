#!/usr/bin/env python3
"""Presentation extraction under badly conditioned non-orthogonal state charts."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')

def chart(d,cond,seed):
 rng=np.random.default_rng(seed);Q,_=np.linalg.qr(rng.normal(size=(d,d)));R,_=np.linalg.qr(rng.normal(size=(d,d)));sv=np.geomspace(1,cond,d);return Q@np.diag(sv)@R.T
def whiten(G):
 w,U=np.linalg.eigh((G+G.T)/2);return (U*np.sqrt(w))@U.T
def cos(a,b):return abs(float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))))
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(39000);a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));q0=pi.word_extra(C,E);rows=[]
 for cond in [1,10,100,1000,10000]:
  S=chart(28,cond,39100+int(np.log10(cond)));Si=np.linalg.inv(S);Cz=S@C@Si;Ez=S@E@Si;G=Si.T@Si
  # raw extraction uses ordinary Frobenius SVD in a non-orthogonal chart
  try:qraw=pi.word_extra(Cz,Ez);cr=cos(qraw,q0)
  except Exception:cr=0.0
  L=whiten(G);Li=np.linalg.inv(L);Cw=L@Cz@Li;Ew=L@Ez@Li;qw=pi.word_extra(Cw,Ew);cw=cos(qw,q0)
  metric_def=np.linalg.norm(Cz.T@G-G@Cz)/max(np.linalg.norm(G@Cz),1e-30)
  rows.append((cond,cr,cw,metric_def));print('cond',cond,'raw_relation_cos',cr,'metric_whitened_cos',cw,'G_selfadjoint_defect',metric_def)
 assert min(r[2] for r in rows)>.999999
 assert max(r[3] for r in rows)<1e-10
 print('PASS: the generator-relations presentation survives highly non-orthogonal coordinate charts when the transported metric is carried and used to whiten the representation. Raw Euclidean extraction is reported only as a numerical-conditioning control; the law belongs to the typed operator geometry, not to Fourier coordinates.')
if __name__=='__main__':main()
