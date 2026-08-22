#!/usr/bin/env python3
"""Do p(C), Dp_C(E), and the physical selection law generate all word relations up to pre-saturation degree?"""
from __future__ import annotations
import importlib.util,itertools,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
ex=loadpath('ex',ROOT/'research'/'theory2_universal_compiler'/'audits'/'extract_degree7_new_relation.py')

def selection_relation():
 # (C^2-I)(C^2 E + E C^2 -5E)(C^2-I)
 r={}
 # expand as word dictionaries by explicit factors
 A={'CC':1,'':-1}; B={'CCE':1,'ECC':1,'E':-5}
 for a,ca in A.items():
  for b,cb in B.items():
   for c,cc in A.items():r[a+b+c]=r.get(a+b+c,0)+ca*cb*cc
 return {w:c for w,c in r.items() if abs(c)>0}

def all_base():return ex.base_rels()+[selection_relation()]
def ideal(L,labs,bases):
 ix={w:i for i,w in enumerate(labs)};cols=[]
 for r in bases:
  deg=max(len(w) for w in r);extra=L-deg
  if extra<0:continue
  for la in range(extra+1):
   for lb in range(extra-la+1):
    for aa in itertools.product('CE',repeat=la):
     a=''.join(aa)
     for bb in itertools.product('CE',repeat=lb):
      b=''.join(bb);v=np.zeros(len(labs))
      for t,c in r.items():v[ix[a+t+b]]+=c
      cols.append(v)
 return np.column_stack(cols) if cols else np.zeros((len(labs),0))
def rank(A,tol=1e-10):
 if A.size==0:return 0
 s=np.linalg.svd(A,compute_uv=False);return int(np.sum(s>tol*s[0]))
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);rng=np.random.default_rng(35000);bases=all_base();print('defining relations',bases)
 for seed in range(4):
  a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));print('seed',seed)
  for L in [6,7,8,9]:
   labs=ex.labels(L);W=ex.words(C,E,L);rw=rank(W);null=W.shape[1]-rw;I=ideal(L,labs,bases);ri=rank(I);res=np.linalg.norm(W@I)/max(np.linalg.norm(W)*np.linalg.norm(I),1e-30) if I.size else 0
   print(' degree',L,'words',W.shape[1],'rank',rw,'nullity',null,'three_relation_ideal_rank',ri,'unexplained',null-ri,'ideal_res',res)
   assert res<1e-12 and ri<=null
   if L<=8:assert ri==null
  # At saturation degree 9, finite 28D representation introduces additional relations.
  assert (ex.words(C,E,9).shape[1]-rank(ex.words(C,E,9)))>rank(ideal(9,ex.labels(9),bases))
 print('PASS: the three state-independent laws p(C)=0, Dp_C(E)=0 and the physical selection relation Q(C,E)=0 generate the entire noncommutative word-relation space through degree 8. New relations appear only at degree 9, exactly when the word algebra hits the finite M_28 representation ceiling.')
if __name__=='__main__':main()
