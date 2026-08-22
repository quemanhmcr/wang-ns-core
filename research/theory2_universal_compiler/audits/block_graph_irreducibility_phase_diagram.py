#!/usr/bin/env python3
"""Phase diagram for when a curl-sheet interaction graph collapses the common centralizer to scalars."""
from __future__ import annotations
import itertools,numpy as np
m=[2,6,6,6,6,2];n=len(m);edges=list(itertools.combinations(range(n),2))
def connected(F):
 A=[set() for _ in range(n)]
 for i,j in F:A[i].add(j);A[j].add(i)
 seen={0};st=[0]
 while st:
  i=st.pop()
  for j in A[i]:
   if j not in seen:seen.add(j);st.append(j)
 return len(seen)==n
def offsets():
 o=[0]
 for z in m:o.append(o[-1]+z*z)
 return o
def centralizer_nullity(F,seed,rank1=False):
 rng=np.random.default_rng(seed);o=offsets();rows=[]
 # unknowns are vec(X_i) for block-diagonal X commuting with C.
 for i,j in F:
  if rank1:
   B=np.outer(rng.normal(size=m[i]),rng.normal(size=m[j]))
  else:B=rng.normal(size=(m[i],m[j]))
  # equation X_i B - B X_j = 0, one row per (a,b)
  for a in range(m[i]):
   for b in range(m[j]):
    r=np.zeros(o[-1])
    # (X_i B)[a,b]=sum_c X_i[a,c] B[c,b]
    for c in range(m[i]):r[o[i]+a*m[i]+c]+=B[c,b]
    # (B X_j)[a,b]=sum_d B[a,d] X_j[d,b]
    for d in range(m[j]):r[o[j]+d*m[j]+b]-=B[a,d]
    rows.append(r)
 A=np.array(rows);s=np.linalg.svd(A,compute_uv=False);rank=int(np.sum(s>1e-10*s[0])) if len(s) and s[0]>0 else 0;return o[-1]-rank

def random_graph(k,rng):return tuple(sorted(rng.choice(len(edges),size=k,replace=False)))
def main():
 rng=np.random.default_rng(40000);print('curl-block multiplicities',m,'commutant(C)_dim',sum(x*x for x in m),'possible_edges',len(edges))
 summaries=[]
 for k in range(5,16):
  vals=[];conn=0;scalar=0
  trials=80
  for t in range(trials):
   idx=random_graph(k,rng);F=[edges[z] for z in idx]
   if connected(F):conn+=1
   nu=centralizer_nullity(F,41000+1000*k+t);vals.append(nu);scalar+=nu==1
  summaries.append((k,conn,scalar,min(vals),int(np.median(vals)),max(vals)))
  print('edges',k,'connected',conn,'/',trials,'scalar_commutant',scalar,'/',trials,'nullity_min/median/max',min(vals),int(np.median(vals)),max(vals))
 # exhaustive trees: connected 5-edge graphs on 6 vertices
 trees=[]
 for F in itertools.combinations(edges,5):
  if connected(F):trees.append(F)
 tree_nu=[centralizer_nullity(F,42000+i) for i,F in enumerate(trees)]
 print('all_labeled_trees',len(trees),'scalar',sum(x==1 for x in tree_nu),'nullity_range',min(tree_nu),max(tree_nu),'median',float(np.median(tree_nu)))
 # Rank-one edge maps are an adversarial control on the complete graph.
 r1=[centralizer_nullity(edges,43000+i,rank1=True) for i in range(20)]
 full=[centralizer_nullity(edges,44000+i,rank1=False) for i in range(20)]
 print('complete_graph_full_blocks',full,'rank1_blocks',r1)
 assert all(x==1 for x in full)
 assert max(r1)>1
 print('PASS: sheet-graph connectivity alone is not the whole story. Generic full block couplings rapidly collapse the curl commutant, while low-rank edge maps retain hidden symmetry even on the complete graph. Algebraic universality depends on both graph percolation and channel richness.')
if __name__=='__main__':main()
