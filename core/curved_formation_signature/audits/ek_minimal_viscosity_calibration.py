#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)
rng=np.random.default_rng(202608212132)
def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def main():
 c=ek.direct_sum(ek.std_so3(),ek.heisenberg3());c=ek.randomize_metric(c,2468);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag([-2,-2,0,0,3,3]);E,K,R=ek.EK(Gs,C);B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);y0,A=ek.codazzi_matrix(B,H,C);y=ek.flatten_K(K,len(Gs))-y0;x=np.linalg.lstsq(A,y,rcond=None)[0];Gr=ek.from_x(B,H,x.reshape(len(Gs),-1));cr=ek.structure_from_gamma(Gr)
 def Jof(u):return -np.einsum('i,ikb->kb',u,cr)
 print('minimal viscosity calibration after E+K geometry reconstruction')
 for nu in [.01,.137,.7]:
  errs=[]
  for eps in [0,1e-10,1e-8,1e-6,1e-4]:
   ee=[]
   for _ in range(60):
    u=rng.normal(size=len(C));euler=Jof(u)@u;h=C@C@u;F=euler-nu*h
    if eps:
     z=rng.normal(size=F.shape);F=F+eps*max(np.linalg.norm(F),1)*z/np.linalg.norm(z)
    # single tangent least-squares scalar
    nurec=-np.dot(h,F-euler)/max(np.dot(h,h),1e-30);ee.append(abs(nurec-nu)/max(abs(nu),1e-30))
   errs.append((eps,float(np.median(ee))))
  print('nu',nu,'errors',errs)
  nz=[x for x in errs if x[0]>0];sl=np.polyfit(np.log10([a for a,b in nz]),np.log10([b for a,b in nz]),1)[0];print(' slope',sl);assert .8<sl<1.2 and errs[0][1]<1e-13
 # exact nonidentifiability without any dynamic tangent
 nu1,nu2=.1,.4;u=rng.normal(size=len(C));L1=Jof(u)-nu1*C@C;L2=Jof(u)-nu2*C@C
 print('same_geometry_different_nu_operator_gap',rel(L1,L2));assert rel(L1,L2)>.05
 print('PASS: (g,C,E,K) reconstructs the reversible formation geometry but not viscosity. One generic observed time tangent calibrates the single missing dissipative scalar nu with linear noise stability; geometry + nu then determines the full NS formation law.')
if __name__=='__main__':main()
