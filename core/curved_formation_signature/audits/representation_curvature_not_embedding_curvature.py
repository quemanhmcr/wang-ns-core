#!/usr/bin/env python3
import sys,numpy as np
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'curved_formation_signature'/'audits'))
import metric_lie_spectral_unification as m
import signature_core_identifiability as sci
# Exact Lie algebra so(3), Euclidean bi-invariant metric.
d=3;T=np.zeros((d,d,d));T[0,1,2]=T[1,2,0]=T[2,0,1]=1;T[0,2,1]=T[2,1,0]=T[1,0,2]=-1
G=np.eye(d);C=np.diag([-1.,.5,2.]);Gamma=sci.koszul_from_lowered_T(G,T)
AE,_=m.mother_tensor(Gamma,C);M,_,s,r=m.reduced_coordinate_map(AE);assert r==3
Rdec,Gz,Tz,Cz=m.transported_structures(T,C,M);R0=sci.curvature_matrices(G,T);Rz=sci.curvature_matrices(Gz,Tz)
rng=np.random.default_rng(20260904);a,b,c=[rng.normal(size=d) for _ in range(3)];za,zb,zc=M@a,M@b,M@c
phys=np.einsum('klab,a,b,l->k',R0,a,b,c);sig=np.einsum('klab,a,b,l->k',Rz,za,zb,zc)
# The signature image is a linear d-plane with constant metric Gz: its ordinary coordinate LC Christoffels are zero.
naive=np.zeros_like(sig)
print('representation curvature versus embedding curvature tribunal')
print('mother_rank',r,'induced_metric_condition',np.linalg.cond(Gz))
print('formation_curvature_norm',np.linalg.norm(phys),'transported_match',np.linalg.norm(sig-M@phys)/max(np.linalg.norm(sig),1e-30))
print('naive_linear_image_curvature_norm',np.linalg.norm(naive),'relative_miss',np.linalg.norm(sig-naive)/max(np.linalg.norm(sig),1e-30))
assert np.linalg.norm(phys)>1e-3 and np.linalg.norm(sig-M@phys)/np.linalg.norm(sig)<1e-13 and np.linalg.norm(sig-naive)/np.linalg.norm(sig)>.99
print('PASS: the signature image is linearly embedded and flat as an ordinary constant-metric vector subspace; the nonzero curvature is the transported right-invariant metric-Lie connection of the fluid configuration group. "Curved representation" means representation of curved formation geometry, not a curved embedding.')
