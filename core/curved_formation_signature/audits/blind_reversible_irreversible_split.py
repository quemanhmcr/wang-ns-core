#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'curved_formation_signature'/'audits'))
import metric_lie_spectral_unification as m
import signature_core_identifiability as sci
rng=np.random.default_rng(20260829)

def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
data=m.build_physical_tensors(False);T,C,Gam=data['T'],data['C'],data['Gamma'];d=len(C)
AO,_,_=m.shifted_signature_map(Gam,C);M,_,_,rank=m.reduced_coordinate_map(AO);assert rank==d
R,G,Tz,Cz=m.transported_structures(T,C,M);H=np.linalg.solve(G,Cz.T@G@Cz);nu_true=.173

def L(z):return m.formation_from_structures(z,G,Tz,Cz,nu=nu_true)[0]
Z=rng.normal(size=(d+8,d))
print('blind reversible/irreversible split tribunal')
for noise in [0.,1e-10,1e-8,1e-6,1e-4]:
    evens=[];odds=[]
    for z in Z:
      Lp,Lm=L(z),L(-z)
      if noise:
        for X in (Lp,Lm):
          N=rng.normal(size=X.shape);X += noise*np.linalg.norm(X)*N/max(np.linalg.norm(N),1e-30)
      evens.append(.5*(Lp+Lm));odds.append(.5*(Lp-Lm))
    Drec=-np.mean(evens,axis=0) # nu H
    # Estimate nu by G-Hilbert/Frobenius projection onto known H.
    nu=float(np.vdot(H,Drec).real/np.vdot(H,H).real)
    even_scatter=max(rel(E,-Drec) for E in evens)
    # Reconstruct T from odd J field only: G J(z)=-sum z_i T_i.
    Y=np.stack([G@J for J in odds]);X,*_=np.linalg.lstsq(Z,-Y.reshape(len(Z),-1),rcond=None);Tr=X.reshape(d,d,d)
    # held-out prediction
    zh=rng.normal(size=d);Lpred=m.formation_from_structures(zh,G,Tr,Cz,nu=nu)[0];errL=rel(Lpred,L(zh));errT=rel(Tr,Tz)
    print(f'noise={noise:.1e} nu={nu:.10f} nu_err={abs(nu-nu_true):.3e} even_scatter={even_scatter:.3e} T_err={errT:.3e} heldout_L={errL:.3e}')
    if noise==0:
      assert abs(nu-nu_true)<1e-13 and even_scatter<1e-13 and errT<2e-12 and errL<2e-12
    else:
      assert abs(nu-nu_true)<20*noise and errL<30*noise
# Adversarial even nonlinear contamination must be detected by nonconstant even part.
eps=.03; ev=[]
A=rng.normal(size=(d,d));A=.5*(A+A.T)
for z in Z:
    contam=eps*(z@z)*A
    ev.append(.5*((L(z)+contam)+(L(-z)+contam)))
scatter=max(rel(E,np.mean(ev,axis=0)) for E in ev)
print('adversarial_even_nonlinearity_scatter',scatter)
assert scatter>1e-2
print('PASS: signature-side z<->-z parity blindly separates the reversible Lie-Poisson pencil from constant Stokes dissipation, and flags extra even nonlinear physics')
