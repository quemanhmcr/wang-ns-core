#!/usr/bin/env python3
"""Exact block tribunal for the curl spectral splitting.

In a C-eigenbasis a metric connection matrix A decomposes into a stabilizer
(block-diagonal) part V and a sheet-mixing part B.  The mother reads B, the
curvature mother reads the off-diagonal/Codazzi curvature, while the diagonal
Gauss/Ricci sector commutes with C.
"""
from __future__ import annotations
import numpy as np
rng=np.random.default_rng(20260904)

def comm(A,B): return A@B-B@A

def rel(a,b): return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)

def vert(A,roots):
    out=np.zeros_like(A)
    for i,x in enumerate(roots):
      for j,y in enumerate(roots):
        if x==y:out[i,j]=A[i,j]
    return out

def invadC(E,roots):
    B=np.zeros_like(E)
    for i,x in enumerate(roots):
      for j,y in enumerate(roots):
        if x!=y:B[i,j]=E[i,j]/(y-x)
    return B

roots=np.array([-2,-2,-1,1,1,3.],float); C=np.diag(roots); n=len(roots); m=5
A=[]
for _ in range(m):
    X=rng.normal(size=(n,n));A.append(X-X.T)
V=[vert(X,roots) for X in A];B=[A[i]-V[i] for i in range(m)]
E=[comm(A[i],C) for i in range(m)]
Brec=[invadC(E[i],roots) for i in range(m)]
rB=max(rel(B[i],Brec[i]) for i in range(m))

rgauss=rcod=rk=rr=0.; vertical_sizes=[]; horizontal_sizes=[]
for i in range(m):
  for j in range(i+1,m):
    R=comm(A[i],A[j]); Rp=vert(R,roots); Ro=R-Rp
    # Exact block structure for an abelian base / constant connection lab.
    gauss=comm(V[i],V[j])+vert(comm(B[i],B[j]),roots)
    cod=(comm(V[i],B[j])+comm(B[i],V[j])+comm(B[i],B[j]))
    cod=cod-vert(cod,roots)
    rgauss=max(rgauss,rel(Rp,gauss)); rcod=max(rcod,rel(Ro,cod))
    K=comm(R,C); Rorec=invadC(K,roots); rk=max(rk,rel(Ro,Rorec))
    rr=max(rr,np.linalg.norm(comm(Rp,C))/max(np.linalg.norm(Rp),1e-30))
    vertical_sizes.append(np.linalg.norm(Rp));horizontal_sizes.append(np.linalg.norm(Ro))

# Pure mixing B: vertical curvature can be nonzero but is completely determined by E.
Bp=[]
for _ in range(2):
    X=rng.normal(size=(n,n));X=X-X.T;Bp.append(X-vert(X,roots))
R_B=comm(Bp[0],Bp[1]); RBv=vert(R_B,roots); RBh=R_B-RBv
EB=[comm(X,C) for X in Bp]
B2=[invadC(x,roots) for x in EB]
RBv_from_E=vert(comm(B2[0],B2[1]),roots)

# Pure stabilizer V: use a nonabelian 3+3 stabilizer so intrinsic vertical
# curvature can be nonzero while E=K=0.
rootsV=np.array([-1,-1,-1,2,2,2.],float); CV=np.diag(rootsV)
Vp=[]
for _ in range(2):
    X=rng.normal(size=(n,n));X=X-X.T;Vp.append(vert(X,rootsV))
R_V=comm(Vp[0],Vp[1]); EV=[comm(X,CV) for X in Vp]; KV=comm(R_V,CV)

print('spectral Gauss-Codazzi-Ricci splitting tribunal')
print(f'E_recovers_sheet_mixing_B                 {rB:.3e}')
print(f'Gauss_Ricci_vertical_block_identity       {rgauss:.3e}')
print(f'Codazzi_horizontal_block_identity          {rcod:.3e}')
print(f'K_recovers_offdiagonal_curvature           {rk:.3e}')
print(f'vertical_curvature_commutes_with_C          {rr:.3e}')
print(f'generic_vertical_curvature_median           {np.median(vertical_sizes):.3e}')
print(f'generic_horizontal_curvature_median         {np.median(horizontal_sizes):.3e}')
print(f'pure_B_vertical_curvature_norm              {np.linalg.norm(RBv):.3e}')
print(f'pure_B_vertical_curvature_from_E             {rel(RBv,RBv_from_E):.3e}')
print(f'pure_B_horizontal_curvature_norm             {np.linalg.norm(RBh):.3e}')
print(f'pure_V_E_norm                                {max(np.linalg.norm(x) for x in EV):.3e}')
print(f'pure_V_K_norm                                {np.linalg.norm(KV):.3e}')
print(f'pure_V_intrinsic_curvature_norm              {np.linalg.norm(R_V):.3e}')
assert max(rB,rgauss,rcod,rk,rr)<1e-12
assert np.linalg.norm(RBv)>1e-3 and rel(RBv,RBv_from_E)<1e-12
assert max(np.linalg.norm(x) for x in EV)<1e-12 and np.linalg.norm(KV)<1e-12 and np.linalg.norm(R_V)>1e-3
print('PASS: E is the gap-weighted spectral second fundamental form; K is the gap-weighted Codazzi/off-sheet curvature; the commuting Gauss/Ricci sector splits into an E-induced part and a genuinely intrinsic stabilizer curvature')
