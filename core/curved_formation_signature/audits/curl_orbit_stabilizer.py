#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'curved_formation_signature'/'audits'))
import metric_lie_spectral_unification as m

def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def block_vertical(A,C,tol=1e-9):
    vals,U=np.linalg.eigh((C+C.T)/2); Ah=U.T@A@U; Vh=np.zeros_like(Ah)
    for i,x in enumerate(vals):
      for j,y in enumerate(vals):
        if abs(x-y)<tol:Vh[i,j]=Ah[i,j]
    return U@Vh@U.T

data=m.build_physical_tensors(False);C=data['C'];Gamma=data['Gamma'];d=len(C)
rng=np.random.default_rng(20260905);u=rng.normal(size=d);A=m.conn_matrix(Gamma,u)
E=A@C-C@A
V=block_vertical(A,C);B=A-V
# Orthogonal conjugacy orbit curve C(t)=Q C Q^T, Q=e^{tA}; derivative [A,C].
errs=[]; eigerrs=[]
for h in [1e-2,5e-3,2.5e-3,1.25e-3]:
    Q=expm(h*A);Ct=Q@C@Q.T;fd=(Ct-C)/h
    errs.append(rel(fd,E));eigerrs.append(np.max(np.abs(np.linalg.eigvalsh(Ct)-np.linalg.eigvalsh(C))))
# Orbit/stabilizer dimensions from multiplicities.
vals=np.linalg.eigvalsh((C+C.T)/2);groups=[]
for x in vals:
    if not groups or abs(x-groups[-1][0])>1e-8:groups.append([x,1])
    else:groups[-1][1]+=1
stab=sum(k*(k-1)//2 for _,k in groups);skewdim=d*(d-1)//2;orbit=skewdim-stab
AE,_=m.mother_tensor(Gamma,C); rank=np.linalg.matrix_rank(AE,tol=1e-10*np.linalg.svd(AE,compute_uv=False)[0])
# Tangent and stabilizer checks.
symE=rel(E,E.T); vertical_invisible=np.linalg.norm(V@C-C@V)/max(np.linalg.norm(V),1e-30)
EfromB=rel(E,B@C-C@B)
# First-order spectral invariants vanish: tr(C^k E)=0.
invariants=[]
for k in range(5):
    invariants.append(abs(np.trace(np.linalg.matrix_power(C,k)@E))/max(np.linalg.norm(E),1.0))
print('curl isospectral orbit / stabilizer tribunal')
print('root multiplicities',[(round(float(x),6),k) for x,k in groups])
print(f'skew_connection_dim={skewdim} stabilizer_dim={stab} orbit_tangent_dim={orbit} physical_state_image_rank={rank}')
print('orbit finite-difference errors',errs)
print('eigenvalue drift',eigerrs)
print(f'E_selfadjoint_tangent                 {symE:.3e}')
print(f'vertical_connection_commutes_C        {vertical_invisible:.3e}')
print(f'E_depends_only_on_sheet_mixing_B       {EfromB:.3e}')
print('spectral_invariant_first_variations',invariants)
assert errs[-1]<2e-3 and errs[-1]<errs[0]
assert max(eigerrs)<2e-12 and symE<1e-12 and vertical_invisible<1e-12 and EfromB<1e-12
assert max(invariants)<1e-11 and rank==d and orbit>rank
print('PASS: E_u is the tangent velocity of curl along its orthogonal isospectral orbit; the physical state space is injectively soldered into a special low-dimensional distribution inside that orbit, while the curl commutant is the orbit stabilizer')
