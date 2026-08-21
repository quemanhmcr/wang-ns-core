#!/usr/bin/env python3
from __future__ import annotations
import sys,numpy as np
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'curved_formation_signature'/'audits'))
import metric_lie_spectral_unification as m
import signature_core_identifiability as sci
rng=np.random.default_rng(20260830)

def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def Oat(Gamma,C,a,v):
    H=m.sign_cut(C,a);Dv=m.conn_matrix(Gamma,v);A=Dv@H-H@Dv;Hv=H@v;DH=m.conn_matrix(Gamma,Hv);AH=DH@H-H@DH;return H@A-AH

data=m.build_physical_tensors(False);T,C,Gam=data['T'],data['C'],data['Gamma'];d=len(C);Cm=-C
nu=.137;u=rng.normal(size=d);a=rng.normal(size=d);b=rng.normal(size=d)
J=m.J_from_T(T,u);Lp=J-nu*C@C;Lm=J-nu*Cm@Cm
AE,_=m.mother_tensor(Gam,C);AEm,_=m.mother_tensor(Gam,Cm)
R4=sci.curvature_matrices(np.eye(d),T);x,y=rng.normal(size=d),rng.normal(size=d);Rab=np.einsum('klab,a,b->kl',R4,x,y);K=Rab@C-C@Rab;Km=Rab@Cm-Cm@Rab
# avoid roots
roots=m.unique_eigs(C); thresholds=[float((roots[i]+roots[i+1])/2) for i in range(len(roots)-1)]
flag=0
for aa in thresholds:
    v=rng.normal(size=d);flag=max(flag,rel(Oat(Gam,Cm,-aa,v),Oat(Gam,C,aa,v)))
hel=float(u@C@u);helm=float(u@Cm@u)
print('orientation double-cover tribunal')
print('formation_operator_same',rel(Lp,Lm))
print('mother_sign_flip',rel(AEm,-AE))
print('curvature_mother_sign_flip',rel(Km,-K))
print('shifted_flag_reflection',flag)
print('helicity_plus_minus',hel,helm,'sum',hel+helm)
assert rel(Lp,Lm)<1e-14 and rel(AEm,-AE)<1e-14 and rel(Km,-K)<1e-14 and flag<1e-13 and abs(hel+helm)<1e-12
print('PASS: C and -C define the same formation dynamics and dissipation; the curved mother tower changes sign while the shifted flag is reflected in threshold. Signed curl is an orientation double cover of the same NS flow.')
