#!/usr/bin/env python3
"""Root-incidence laws are projectively consistent under exact helical window refinement."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
fh=loadpath('fh',ROOT/'research'/'theory2_universal_compiler'/'audits'/'full_helical_one_state_recovers_union_graph.py')
def rp(e):
 (q,sq),(r,t)=e;return (round(t*np.linalg.norm(r),12),round(sq*np.linalg.norm(q),12))
def main():
 P=fh.support_reps(3);wins=[3,4,5,6,8,9,10,12,14,16];sets={}
 for R2 in wins:
  A={rp(e) for e in fh.structural_union(P,fh.window(R2))};roots={x for xy in A for x in xy};sets[R2]=(A,roots);print('window',R2,'active',len(A),'roots',len(roots))
 for a,b in zip(wins[:-1],wins[1:]):
  A,ra=sets[a];B,rb=sets[b];restr={(x,y) for x,y in B if x in ra and y in ra};add=restr-A;lost=A-restr;print('refine',a,'->',b,'old',len(A),'restricted',len(restr),'added_old_root_edges',len(add),'lost',len(lost));assert not add and not lost
 print('PASS: exact helical interaction incidence forms a projectively consistent nested family from R^2=3 through 16: enlarging the observation window never changes any transition law among previously present signed-curl roots; only new roots bring new channels and new relations.')
if __name__=='__main__':main()
