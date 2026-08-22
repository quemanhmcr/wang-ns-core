#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[3]
def load(name,file):
 p=ROOT/'core'/'curved_formation_signature'/'audits'/file;s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
mu=load('mu','metric_lie_spectral_unification.py')
SETS={
 'axes3':[(1,0,0),(0,1,0),(0,0,1)],
 'plus_xy4':[(1,0,0),(0,1,0),(0,0,1),(1,1,0)],
 'plus_xz5':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1)],
 'pairs6':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)],
 'base7':[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)],
}
def comm_matrix(A):
 n=A.shape[0];I=np.eye(n)
 # vec(XA-AX) = (A^T kron I - I kron A) vec(X), column-major convention.
 return np.kron(A.T,I)-np.kron(I,A)
def nullity(*As):
 M=np.vstack([comm_matrix(A) for A in As]);s=np.linalg.svd(M,compute_uv=False);r=int(np.sum(s>1e-10*s[0])) if len(s) and s[0]>0 else 0;return M.shape[1]-r,(s[r-1]/s[0] if r else 0)
def main():
 old=mu.KS;rng=np.random.default_rng(24000);rows=[]
 try:
  for name,ks in SETS.items():
   mu.KS=list(ks);data=mu.build_physical_tensors(False);C=data['C'];_,Es=mu.mother_tensor(data['Gamma'],C);d=len(C);a=rng.normal(size=d);E=sum(a[i]*Es[i] for i in range(d));nC,_=nullity(C);nCE,gap=nullity(C,E);rows.append((name,d,nC,nCE,gap,np.linalg.norm(E)));print(name,'d',d,'commutant(C)',nC,'commutant(C,E_u)',nCE,'last_nonzero_rel_singular',gap,'||E||',np.linalg.norm(E))
 finally:mu.KS=old
 assert rows[0][3]>1
 assert rows[-1][3]==1
 assert all(r[3]>=1 for r in rows)
 print('PASS: as Fourier interaction richness increases, one generic mother collapses the full operator commutant of curl down to the scalar identity. The richest physical coordinate lab has no nontrivial linear symmetry commuting with both C and E_u.')
if __name__=='__main__':main()
