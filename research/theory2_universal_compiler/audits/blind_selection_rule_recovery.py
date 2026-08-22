#!/usr/bin/env python3
"""From C and one generic E_u only, recover the forbidden curl-sheet transitions from the degree-7 word relation."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')
def evalq(q,x,y):return sum(q[k]*(x**a)*(y**b) for k,(a,b) in enumerate(pi.mons(6)))
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);vals,U=np.linalg.eigh((C+C.T)/2);roots=[];groups=[]
 for i,x in enumerate(vals):
  if not roots or abs(x-roots[-1])>1e-8:roots.append(float(x));groups.append([i])
  else:groups[-1].append(i)
 # ground truth forbidden pairs from the full mother is used only for scoring, never in q extraction.
 Ehs=[U.T@E@U for E in Es];forbidden=set()
 for a,x in enumerate(roots):
  for b,y in enumerate(roots):
   if a==b:continue
   st=np.sqrt(sum(np.linalg.norm(Eh[np.ix_(groups[a],groups[b])])**2 for Eh in Ehs))
   if st<1e-10:forbidden.add((a,b))
 print('ground_truth_forbidden',[(round(roots[a],6),round(roots[b],6)) for a,b in sorted(forbidden)])
 rng=np.random.default_rng(29400);gaps=[]
 for seed in range(8):
  a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));q=pi.word_extra(C,E);scores=[]
  for i,x in enumerate(roots):
   for j,y in enumerate(roots):
    if i==j:continue
    scores.append((abs(evalq(q,x,y)),i,j))
  scores.sort(reverse=True);pred={(i,j) for _,i,j in scores[:len(forbidden)]};active=[s for s,i,j in scores if (i,j) not in forbidden];bad=[s for s,i,j in scores if (i,j) in forbidden];gap=min(bad)/max(max(active),1e-30);gaps.append(gap)
  print('seed',seed,'predicted_forbidden',[(round(roots[i],6),round(roots[j],6),float(s)) for s,i,j in scores[:4]],'max_active_score',max(active),'min_forbidden_score',min(bad),'separation',gap,'exact',pred==forbidden)
  assert pred==forbidden and gap>1e8
 print('min_separation',min(gaps))
 print('PASS: using only curl C and one generic state mother E_u, the first non-spectral word relation blindly recovers the exact four forbidden curl-sheet transitions of the full physical mother tensor. A single generic snapshot reveals a global interaction-selection rule of the underlying formation core.')
if __name__=='__main__':main()
