#!/usr/bin/env python3
"""Deliberate negative control: arbitrary Galerkin projection need not preserve
mother completeness or the Lie/Jacobi geometry. Microlocal strain probes do.
"""
from __future__ import annotations
import numpy as np
import metric_lie_spectral_unification as m
RNG=np.random.default_rng(20260821)
SETS={
 'axes3':[(1,0,0),(0,1,0),(0,0,1)],
 'axes_plus_pairs6':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)],
 'base7':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)],
 'two_shell10':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(2,0,0),(0,2,0),(0,0,2)],
}
dirs=np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,0,1],[0,1,1]],float); dirs[3:]/=np.sqrt(2)

def jacobi_defect(T,d,trials=80):
    worst=0
    for _ in range(trials):
        a,b,c=[RNG.normal(size=d) for i in range(3)]
        j=m.bracket_coeff(T,a,m.bracket_coeff(T,b,c))+m.bracket_coeff(T,b,m.bracket_coeff(T,c,a))+m.bracket_coeff(T,c,m.bracket_coeff(T,a,b))
        worst=max(worst,np.linalg.norm(j)/max(np.linalg.norm(a)*np.linalg.norm(b)*np.linalg.norm(c),1e-30))
    return worst

def microlocal_map(B):
    cols=[]
    for bj in B:
        A=m.grad(bj); S=.5*(A+np.swapaxes(A,-1,-2))
        q=np.stack([np.einsum('i,...ij,j->...',n,S,n) for n in dirs],axis=-1)
        cols.append(q.reshape(-1))
    return np.column_stack(cols)

def rank(A):
    s=np.linalg.svd(A,compute_uv=False); return int(np.sum(s>1e-10*s[0])),float(s[0]/s[-1]) if s[-1]>1e-14*s[0] else np.inf

def main():
    old=m.KS; results={}
    try:
      for name,ks in SETS.items():
        m.KS=list(ks); data=m.build_physical_tensors(False); d=len(data['C'])
        AE,_=m.mother_tensor(data['Gamma'],data['C']); AO,_,_=m.shifted_signature_map(data['Gamma'],data['C']); Q=microlocal_map(data['B'])
        rE,_=rank(AE); rO,_=rank(AO); rQ,cQ=rank(Q); jac=jacobi_defect(data['T'],d)
        results[name]=(d,rE,rO,rQ,cQ,jac)
    finally: m.KS=old
    print('Galerkin probe/Lie failure negative control')
    print('name d projected_mother projected_flag microlocal_q qcond Jacobi_defect')
    for name,x in results.items(): print(name,*x)
    # Continuum/microlocal state reader remains complete in every set.
    assert all(x[3]==x[0] for x in results.values())
    # At least two truncations lose projected-operator rank.
    assert sum(x[1]<x[0] or x[2]<x[0] for x in results.values())>=2
    # The base Galerkin bracket is emphatically non-Jacobi.
    assert results['base7'][5]>0.1
    print('PASS: arbitrary Galerkin projection can lose probes and Jacobi; full microlocal strain signature stays complete')
if __name__=='__main__': main()
