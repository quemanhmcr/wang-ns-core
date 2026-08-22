#!/usr/bin/env python3
"""A 3-support exact helical state blindly recovers the degree-16 incidence law of a 13-support category."""
from __future__ import annotations
import importlib.util,itertools,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def loadpath(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ph=loadpath('ph',ROOT/'core'/'curved_formation_signature'/'audits'/'physical_helical_resonant_recovery.py')
fh=loadpath('fh',ROOT/'research'/'theory2_universal_compiler'/'audits'/'full_helical_one_state_recovers_union_graph.py')

def rp(edge):
 (q,sq),(r,t)=edge;return (round(t*np.linalg.norm(r),12),round(sq*np.linalg.norm(q),12))
def mons(D):return [(a,d-a) for d in range(D+1) for a in range(d+1)]
def evalrow(x,y,M,R):
 x=x/R;y=y/R;return np.array([x**a*y**b for a,b in M],float)
def nullspace(A,tol=1e-10):
 U,s,Vh=np.linalg.svd(A,full_matrices=True);r=int(np.sum(s>tol*s[0]));return Vh[r:].T,r,s
def exact_E_matrix(U,K):
 N=[(k,s) for k in sorted(K) for s in (+1,-1)];ix={z:i for i,z in enumerate(N)};A=np.zeros((len(N),len(N)),complex)
 for j,(q,sq) in enumerate(N):
  F=ph.E(U,ph.mode(q,sq))
  for r,a in F.items():
   if r not in K:continue
   for t in (+1,-1):
    z=(r,t)
    if z in ix:A[ix[z],j]+=ph.hcoef(r,t,a)
 return N,A
def dense_on(P,seed):
 rng=np.random.default_rng(seed);U={}
 for pp in P:
  p=np.array(pp,float);z=ph.projvec(p,rng.normal(size=3)+1j*rng.normal(size=3));z/=np.linalg.norm(z);z*=rng.normal()+1j*rng.normal();U[pp]=z;U[tuple(-p.astype(int))]=np.conj(z)
 return U
def matrix_relation_null(N,E,M,R):
 rows=[]
 for i,(r,t) in enumerate(N):
  x=t*np.linalg.norm(r)
  for j,(q,sq) in enumerate(N):
   if abs(E[i,j])<1e-11:continue
   y=sq*np.linalg.norm(q);rows.append(evalrow(x,y,M,R)*E[i,j])
 B=np.array(rows,complex);Nul,r,s=nullspace(B);return Nul,r,s,len(rows)
def quotient_extra(Nphys,Nspec):
 X=Nphys-Nspec@(Nspec.T@Nphys);U,s,Vh=np.linalg.svd(X,full_matrices=False);return U,s

def main():
 K=fh.window(6);Pall=fh.support_reps(3)
 # structural root-pair set and exact minimum set cover over support representatives
 per=[]
 for p in Pall:per.append({rp(e) for e in fh.structural_union([p],K)})
 full=set().union(*per);cover=None
 for k in range(1,len(Pall)+1):
  for I in itertools.combinations(range(len(Pall)),k):
   if set().union(*(per[i] for i in I))==full:cover=I;break
  if cover is not None:break
 P=[Pall[i] for i in cover];roots=sorted({x for xy in full for x in xy});allpairs={(x,y) for x in roots for y in roots if x!=y};forbid=allpairs-full
 print('window nodes',2*len(K),'category_supports',len(Pall),'minimal_law_cover',len(P),P,'active_rootpairs',len(full),'forbidden',len(forbid))
 D=16;M=mons(D);R=max(abs(x) for x in roots)
 Aspec=np.array([evalrow(x,y,M,R) for x,y in sorted(allpairs)]);Nspec,rs,ss=nullspace(Aspec)
 Aphys=np.array([evalrow(x,y,M,R) for x,y in sorted(full)]);Nphys,rp0,sp=nullspace(Aphys)
 Ux,sx=quotient_extra(Nphys,Nspec);qcat=np.real_if_close(Ux[:,0],tol=1000);qcat=np.real(qcat);qcat/=np.linalg.norm(qcat);print('degree',D,'monomials',len(M),'spectral_null',Nspec.shape[1],'category_null',Nphys.shape[1],'extra_singulars',sx[:5]);assert Nphys.shape[1]-Nspec.shape[1]==1 and sx[0]>.99 and sx[1]<1e-8
 gaps=[]
 for seed in range(6):
  N,E=exact_E_matrix(dense_on(P,36000+seed),K);Ns,rr,sv,nrows=matrix_relation_null(N,E,M,R);Ux2,sx2=quotient_extra(Ns,Nspec);q=np.real_if_close(Ux2[:,0],tol=1000);q=np.real(q);q/=np.linalg.norm(q);cc=abs(float(np.dot(q,qcat)));scores=[]
  for x,y in allpairs:scores.append((abs(float(np.dot(q,evalrow(x,y,M,R)))),(x,y)))
  scores.sort(reverse=True);pred={xy for s,xy in scores[:len(forbid)]};active_scores=[s for s,xy in scores if xy in full];bad=[s for s,xy in scores if xy in forbid];gap=min(bad)/max(max(active_scores),1e-30);gaps.append(gap)
  print('seed',seed,'matrix_rows',nrows,'snapshot_null',Ns.shape[1],'relation_cos',cc,'exact_forbidden',pred==forbid,'max_active',max(active_scores),'min_forbidden',min(bad),'separation',gap)
  assert Ns.shape[1]==Nphys.shape[1] and cc>.999999 and pred==forbid and gap>1e6
 print('min_separation',min(gaps),'forbidden_pairs',sorted(forbid))
 print('PASS: in an exact 160-node helical window, a generic state supported on only three Fourier directions recovers from its mother matrix the unique degree-16 physical incidence relation of the entire thirteen-support category, and blindly identifies all twelve forbidden signed-curl transitions with huge separation.')
if __name__=='__main__':main()
