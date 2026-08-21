#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, pathlib, numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py')
spec=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(spec);spec.loader.exec_module(ek)

def abelian(n):return np.zeros((n,n,n))
def almost_abelian6():
    d=6;c=np.zeros((d,d,d));a=np.array([1.2,.7,.1,-.5,-1.5]) # trace 0 on ideal
    for j in range(1,d):c[j,0,j]=a[j-1];c[j,j,0]=-a[j-1]
    return c

def rankcase(c,roots,seed):
    c=ek.randomize_metric(c,seed);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag(roots);E,K,R=ek.EK(Gs,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);y0,A=ek.codazzi_matrix(B,H,C)
    if A.shape[1]==0:return 0,0,1.0,np.linalg.norm(np.stack(E)),np.linalg.norm(ek.flatten_K(K,len(Gs)))
    s=np.linalg.svd(A,compute_uv=False);rank=int(np.sum(s>1e-10*s[0]));null=A.shape[1]-rank;cond=s[0]/s[rank-1] if rank else np.inf
    return A.shape[1],null,cond,np.linalg.norm(np.stack(E)),np.linalg.norm(ek.flatten_K(K,len(Gs)))

def main():
    fam={
      'so3+so3':ek.direct_sum(ek.std_so3(),ek.std_so3()),
      'so3+h3':ek.direct_sum(ek.std_so3(),ek.heisenberg3()),
      'so3+se2':ek.direct_sum(ek.std_so3(),ek.se2()),
      'h3+h3':ek.direct_sum(ek.heisenberg3(),ek.heisenberg3()),
      'se2+se2':ek.direct_sum(ek.se2(),ek.se2()),
      'h3+se2':ek.direct_sum(ek.heisenberg3(),ek.se2()),
      'so3+R3':ek.direct_sum(ek.std_so3(),abelian(3)),
      'h3+R3':ek.direct_sum(ek.heisenberg3(),abelian(3)),
      'almostAb6':almost_abelian6(),
    }
    pats={
      '2+1+1+1+1':[-2,-2,-1,0,1,3],
      '2+2+1+1':[-2,-2,0,0,1,3],
      '2+2+2':[-2,-2,0,0,3,3],
      '3+1+1+1':[-1,-1,-1,0,2,3],
      '3+2+1':[-1,-1,-1,2,2,4],
      '3+3':[-1,-1,-1,2,2,2],
      '4+2':[-1,-1,-1,-1,2,2],
      '5+1':[-1,-1,-1,-1,-1,2],
      '6':[-1]*6,
    }
    print('E+K geometric-completeness rank phase diagram')
    summary=[]
    for fn,c in fam.items():
      for pn,roots in pats.items():
        ns=[];conds=[];ens=[];kns=[];u=None
        for seed in range(6):
          unk,nul,cond,en,kn=rankcase(c,roots,3000+seed);u=unk;ns.append(nul);conds.append(cond);ens.append(en);kns.append(kn)
        summary.append((fn,pn,u,ns,conds,ens,kns))
        print(f'{fn:10s} {pn:11s} hidden={u:3d} null={ns} medcond={np.median(conds):8.2g} med||E||={np.median(ens):.2e} med||K||={np.median(kns):.2e}')
    nontriv=[x for x in summary if x[1]!='6']
    full=sum(all(n==0 for n in x[3]) for x in nontriv); total=len(nontriv)
    print('non_scalar_patterns_full_for_all_seeds',full,'/',total)
    bad=[x for x in nontriv if any(n>0 for n in x[3])]
    print('rank_deficient_non_scalar_count',len(bad))
    for x in bad:print('BAD',x[0],x[1],'hidden',x[2],'nulls',x[3],'medE',np.median(x[5]),'medK',np.median(x[6]))
    scalar=[x for x in summary if x[1]=='6'];assert all(all(n==x[2] for n in x[3]) for x in scalar)
    print('scalar_C_dark_controls',[(x[0],x[2],x[3][0]) for x in scalar])
    print('PASS phase diagram complete: non-scalar rank deficiencies, if any, are reported rather than suppressed; scalar curl is an exact fully-dark control.')
if __name__=='__main__':main()
