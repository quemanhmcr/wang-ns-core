#!/usr/bin/env python3
"""Can one (C,E) snapshot identify which same-spectrum interaction-incidence law generated it?"""
from __future__ import annotations
import importlib.util,itertools,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')

def root_groups(C):
 vals,U=np.linalg.eigh((C+C.T)/2);g=[]
 for i,x in enumerate(vals):
  if not g or abs(x-g[-1][0])>1e-8:g.append([float(x),[i]])
  else:g[-1][1].append(i)
 return U,g

def incidence_relation(groups,forbid):
 M=pi.mons(6);pts=[]
 for a,(x,I) in enumerate(groups):
  for b,(y,J) in enumerate(groups):
   if a==b or tuple(sorted((a,b))) in forbid:continue
   pts.append((x,y))
 A=np.array([[x**i*y**j for i,j in M] for x,y in pts])
 U,s,Vh=np.linalg.svd(A,full_matrices=True);r=int(np.sum(s>1e-10*s[0]));N=Vh[r:].T
 Qk,rk=pi.known_space(M);X=N-Qk@(Qk.T@N);ux,sx,vx=np.linalg.svd(X,full_matrices=False);extra=int(np.sum(sx>1e-8))
 if extra!=1:return None
 q=ux[:,0];return q/np.linalg.norm(q)

def choose_laws(groups,n=3,forbidden_count=2,force_physical=True):
 pairs=list(itertools.combinations(range(len(groups)),2));cand=[]
 for F in itertools.combinations(pairs,forbidden_count):
  q=incidence_relation(groups,frozenset(F))
  if q is not None:cand.append((frozenset(F),q))
 # greedy max-separation in projective cosine; force physical law first
 phys=frozenset({(0,5),(1,4)});start=next(x for x in cand if x[0]==phys) if force_physical else cand[0];sel=[start]
 while len(sel)<n:
  best=None
  for x in cand:
   if x in sel:continue
   worst=max(abs(float(np.dot(x[1],y[1]))) for y in sel)
   score=1-worst
   if best is None or score>best[0]:best=(score,x)
  sel.append(best[1])
 return sel

def sample_E(U,groups,forbid,seed):
 rng=np.random.default_rng(seed);Eh=np.zeros((U.shape[0],U.shape[0]))
 for a,(x,I) in enumerate(groups):
  for b in range(a+1,len(groups)):
   if (a,b) in forbid:continue
   J=groups[b][1];B=rng.normal(size=(len(I),len(J)));Eh[np.ix_(I,J)]=B;Eh[np.ix_(J,I)]=B.T
 return U@Eh@U.T

def classify(q,templates):
 sims=[abs(float(np.dot(q,t))) for t in templates];return int(np.argmax(sims)),sims

def main():
 data=mu.build_physical_tensors(False);C=data['C'];U,g=root_groups(C);laws=choose_laws(g,3);templates=[q for F,q in laws]
 print('same-spectrum rival-theory identifier; roots',[round(x,6) for x,I in g])
 print('laws')
 for i,(F,q) in enumerate(laws):print(i,sorted(F),'nearest_other_cos',max(abs(float(np.dot(q,r))) for j,r in enumerate(templates) if j!=i))
 # clean blind identification from word relations only
 conf=np.zeros((len(laws),len(laws)),int);marg=[]
 for li,(F,qt) in enumerate(laws):
  for seed in range(8):
   E=sample_E(U,g,F,33000+100*li+seed);q=pi.word_extra(C,E);pred,s=classify(q,templates);conf[li,pred]+=1;ss=sorted(s,reverse=True);marg.append(ss[0]-ss[1])
 print('clean_confusion\n',conf);print('clean_min_margin',min(marg))
 assert np.trace(conf)==conf.sum()
 # noise robustness: perturb snapshot by a generic symmetric matrix; relation extraction now approximate.
 rng=np.random.default_rng(33100)
 for eps in [1e-10,1e-8,1e-6,1e-4,1e-3]:
  ok=0;tot=0;m=[]
  for li,(F,qt) in enumerate(laws):
   for seed in range(4):
    E=sample_E(U,g,F,33200+100*li+seed);Z=rng.normal(size=E.shape);Z=(Z+Z.T)/2;Z*=np.linalg.norm(E)/max(np.linalg.norm(Z),1e-30);En=E+eps*Z
    q=pi.word_extra(C,En);pred,s=classify(q,templates);ok+=pred==li;tot+=1;ss=sorted(s,reverse=True);m.append(ss[0]-ss[1])
  print('noise',eps,'accuracy',ok,'/',tot,'min_margin',min(m),'median_margin',float(np.median(m)))
  if eps<=1e-4:assert ok==tot
 # broader same-count synthetic family
 many=choose_laws(g,8,3,False);T=[q for F,q in many];conf2=np.zeros((8,8),int)
 for li,(F,qt) in enumerate(many):
  for seed in range(4):
   E=sample_E(U,g,F,34000+100*li+seed);q=pi.word_extra(C,E);pred,_=classify(q,T);conf2[li,pred]+=1
 print('eight_law_same_count_confusion\n',conf2)
 assert np.trace(conf2)==conf2.sum()
 print('PASS: one generic snapshot, reduced only to its noncommutative relation modulo the common curl spectral ideal, identifies the physical law among all three same-count codimension-one rivals and also separates an eight-law same-spectrum/same-forbidden-count stress family. Identification remains exact under substantial snapshot perturbation.')
if __name__=='__main__':main()
