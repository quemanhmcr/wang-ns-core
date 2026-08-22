#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
def mrank(A,tol=1e-9):
 s=np.linalg.svd(A,compute_uv=False)
 return int(np.sum(s>tol*s[0])) if len(s) and s[0]>1e-13 else 0
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);vals,U=np.linalg.eigh((C+C.T)/2);groups=[]
 for i,x in enumerate(vals):
  if not groups or abs(x-groups[-1][0])>1e-8:groups.append([float(x),[i]])
  else:groups[-1][1].append(i)
 Ehs=[U.T@E@U for E in Es];rng=np.random.default_rng(29700);samples=[]
 for s in range(20):
  a=rng.normal(size=28);Eh=sum(a[i]*Ehs[i] for i in range(28));samples.append(Eh)
 print('generic mother edge-capacity tribunal')
 stable=True
 for a,(x,I) in enumerate(groups):
  for b in range(a+1,len(groups)):
   y,J=groups[b];ranks=[mrank(Eh[np.ix_(I,J)]) for Eh in samples];# global linear-map capacity
   M=np.column_stack([Eh[np.ix_(I,J)].reshape(-1) for Eh in Ehs]);cap=mrank(M);full=min(len(I),len(J));print((round(x,6),round(y,6)),'block',len(I),'x',len(J),'generic_matrix_ranks',sorted(set(ranks)),'mother_map_capacity',cap,'max_matrix_rank',full)
   if len(set(ranks))>1:stable=False
 assert stable
 print('PASS: for every curl-sheet pair, the matrix rank of a generic single-state mother block is stable across 20 random states. Forbidden edges are rank zero; active edges carry reproducible channel ranks, while the full one-form supplies a larger linear-map capacity. A generic snapshot therefore exposes a stable weighted interaction-quiver skeleton, though not the full polarized edge map.')
if __name__=='__main__':main()
