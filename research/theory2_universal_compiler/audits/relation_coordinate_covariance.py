#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(29900);a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));q0=pi.word_extra(C,E);cos=[]
 for seed in range(10):
  Q,_=np.linalg.qr(rng.normal(size=(28,28)));Ct=Q.T@C@Q;Et=Q.T@E@Q;q=pi.word_extra(Ct,Et);cc=abs(np.dot(q0,q));cos.append(cc);print('chart',seed,'relation_cosine',cc)
 assert min(cos)>.999999999
 print('PASS: the extracted non-spectral word relation is invariant under arbitrary orthogonal changes of the 28D state chart (up to sign). The recovered interaction law belongs to the operator pair (C,E_u), not to the Fourier coordinate representation used to display it.')
if __name__=='__main__':main()
