#!/usr/bin/env python3
"""Three fixed Fourier support directions reveal the entire root-level category through 512-node windows."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
fh=loadpath('fh',ROOT/'research'/'theory2_universal_compiler'/'audits'/'full_helical_one_state_recovers_union_graph.py')
P3=[(0,0,1),(0,1,-1),(1,-1,-1)]
def rp(e):
 (q,sq),(r,t)=e;return (round(t*np.linalg.norm(r),12),round(sq*np.linalg.norm(q),12))
def main():
 Pall=fh.support_reps(3);wins=[3,4,5,6,8,9,10,12,14,16]
 for R2 in wins:
  K=fh.window(R2);full={rp(e) for e in fh.structural_union(Pall,K)};three={rp(e) for e in fh.structural_union(P3,K)};roots=sorted({x for xy in full for x in xy});allp={(x,y) for x in roots for y in roots if x!=y};assert three==full
  # actual generic dense state, not only union of three separate supports
  for seed in range(2):
   E={rp(e) for e in fh.edges_from_U(fh.real_dense(P3,47000+100*R2+seed),K)};assert E==full
  print('R2',R2,'nodes',2*len(K),'roots',len(roots),'active',len(full),'forbidden',len(allp-full),'three_direction_exact',True)
 print('PASS: the same three Fourier support directions, combined into one generic real state, realize the complete root-level mother interaction category in ten exact helical windows from 52 to 512 nodes, even as the number of forbidden signed-curl channels grows from 2 to 324.')
if __name__=='__main__':main()
