#!/usr/bin/env python3
"""Closed-form NS selection identity encoded by the C,E word algebra."""
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=loadpath('mu',ROOT/'core'/'curved_formation_signature'/'audits'/'metric_lie_spectral_unification.py')
pi=loadpath('pi',ROOT/'research'/'theory2_universal_compiler'/'audits'/'physical_incidence_explains_new_relation.py')
def law(C,E):
 C2=C@C;I=np.eye(C.shape[0]);return (C2-I)@(C2@E+E@C2-5*E)@(C2-I)
def rel0(A,E):return np.linalg.norm(A)/max(np.linalg.norm(E),1e-30)
def qclosed_vec():
 # q=(x^2-1)(y^2-1)(x^2+y^2-5)
 M=pi.mons(6);ix={ab:i for i,ab in enumerate(M)};q=np.zeros(len(M))
 # expand by evaluating coefficients manually via polynomial convolution
 terms={(0,0):1}
 for fac in [{(2,0):1,(0,0):-1},{(0,2):1,(0,0):-1},{(2,0):1,(0,2):1,(0,0):-5}]:
  out={}
  for (a,b),c in terms.items():
   for (i,j),d in fac.items():out[(a+i,b+j)]=out.get((a+i,b+j),0)+c*d
  terms=out
 for ab,c in terms.items():q[ix[ab]]=c
 return q/np.linalg.norm(q)
def main():
 data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C)
 basis_res=[rel0(law(C,E),E) for E in Es];print('closed-form selection law basis mother max/median',max(basis_res),np.median(basis_res))
 rng=np.random.default_rng(30000);rand=[];cos=[];qc=qclosed_vec()
 # compare extracted quotient relation to closed form modulo known spectral ideal by direct active-edge equivalence
 vals,U=np.linalg.eigh((C+C.T)/2);roots=[]
 for x in vals:
  if not roots or abs(x-roots[-1])>1e-8:roots.append(float(x))
 def evalq(q,x,y):return sum(q[k]*x**a*y**b for k,(a,b) in enumerate(pi.mons(6)))
 vc=np.array([evalq(qc,x,y) for x in roots for y in roots if abs(x-y)>1e-8])
 for s in range(8):
  a=rng.normal(size=28);E=sum(a[i]*Es[i] for i in range(28));rand.append(rel0(law(C,E),E));qw=pi.word_extra(C,E);vw=np.array([evalq(qw,x,y) for x in roots for y in roots if abs(x-y)>1e-8]);# both vanish active; compare after projecting to the forbidden signal vector
  cc=abs(np.dot(vc,vw)/(np.linalg.norm(vc)*np.linalg.norm(vw)));cos.append(cc)
 print('random_state law max',max(rand),'closed_vs_blind_edge_signal_cosines',cos)
 # Exact root table.
 table=[]
 for x in roots:
  for y in roots:
   if abs(x-y)>1e-8:
    table.append((round(x,6),round(y,6),evalq(qc,x,y)))
 nz=[z for z in table if abs(z[2])>1e-8];print('nonzero root-pair values',nz)
 # Same-spectrum all-offblock control must violate the physical law.
 groups=[]
 for i,x in enumerate(vals):
  if not groups or abs(x-groups[-1][0])>1e-8:groups.append([float(x),[i]])
  else:groups[-1][1].append(i)
 Eh=np.zeros_like(C)
 for i in range(len(groups)):
  for j in range(i+1,len(groups)):
   I,J=groups[i][1],groups[j][1];B=rng.normal(size=(len(I),len(J)));Eh[np.ix_(I,J)]=B;Eh[np.ix_(J,I)]=B.T
 Ec=U@Eh@U.T;ctrl=rel0(law(C,Ec),Ec);print('same_spectrum_full_offblock_control',ctrl)
 assert max(basis_res)<1e-11 and max(rand)<1e-11 and min(cos)>.999999999 and len(nz)==4 and ctrl>1e-2
 print('PASS: the physical 28D mother obeys the intrinsic polynomial identity (C^2-I)(C^2 E + E C^2 - 5E)(C^2-I)=0 for every state direction. The identity is exactly the blind one-snapshot forbidden-edge relation and fails on a same-spectrum generic offblock control.')
if __name__=='__main__':main()
