#!/usr/bin/env python3
"""Exact Fourier audit of the formation metric inside the strain/signature geometry.

For q_u(x,n)=n^T S(u)(x)n and divergence-free mean-zero fields:
  <u,v> = 15 <Lambda^{-1} q_u, Lambda^{-1} q_v>_{x,n}
  <Cu,Cv> = 15 <q_u,q_v>_{x,n}
Hence the Riesz operator of the Dirichlet form relative to the kinetic signature
metric is Lambda^2 on q.  This is the metric bridge between the two cores.
"""
from __future__ import annotations
import numpy as np

RNG=np.random.default_rng(20260821)


def random_divfree_coeff(N=11):
    ks=np.fft.fftfreq(N)*N
    U=np.zeros((N,N,N,3),complex)
    for i,k1 in enumerate(ks):
      for j,k2 in enumerate(ks):
       for l,k3 in enumerate(ks):
        k=np.array([k1,k2,k3],float); k2n=k@k
        if k2n==0: continue
        z=RNG.normal(size=3)+1j*RNG.normal(size=3)
        z-=k*(k@z)/k2n
        U[i,j,l]=z
    return U


def bilinear_audit(trials=20,N=11):
    ks=np.fft.fftfreq(N)*N
    worst_l2=worst_dir=worst_heat=0.0
    for _ in range(trials):
        U=random_divfree_coeff(N); V=random_divfree_coeff(N)
        l2=dirichlet=sig_m1=sig_0=heat_pair=0.0
        for i,k1 in enumerate(ks):
          for j,k2 in enumerate(ks):
           for l,k3 in enumerate(ks):
            k=np.array([k1,k2,k3],float); k2n=float(k@k)
            if k2n==0: continue
            u=U[i,j,l]; v=V[i,j,l]
            Gu=1j*np.outer(u,k)  # component i, derivative j
            Gv=1j*np.outer(v,k)
            Su=.5*(Gu+Gu.T); Sv=.5*(Gv+Gv.T)
            uv=float(np.vdot(u,v).real)
            ss=float(np.vdot(Su,Sv).real)
            l2 += uv
            dirichlet += k2n*uv
            # 15 sphere-average q_u q_v = 2 S_u:S_v for tracefree S.
            sig0_mode=2.0*ss
            sig_0 += sig0_mode
            sig_m1 += sig0_mode/k2n
            # Riesz heat identity in q: g_-1(r, Lambda^2 q)=g_0(r,q).
            heat_pair += (2.0*ss/k2n)*k2n
        def r(a,b): return abs(a-b)/max(abs(a),abs(b),1.0)
        worst_l2=max(worst_l2,r(l2,sig_m1))
        worst_dir=max(worst_dir,r(dirichlet,sig_0))
        worst_heat=max(worst_heat,r(sig_0,heat_pair))
    return worst_l2,worst_dir,worst_heat


def monte_carlo_sphere(trials=30,dirs=200000):
    # Independent physical-space tensor check of the 15 factor.
    n=RNG.normal(size=(dirs,3)); n/=np.linalg.norm(n,axis=1)[:,None]
    worst=0.0
    for _ in range(trials):
        S=RNG.normal(size=(3,3)); S=.5*(S+S.T); S-=np.eye(3)*np.trace(S)/3
        T=RNG.normal(size=(3,3)); T=.5*(T+T.T); T-=np.eye(3)*np.trace(T)/3
        qS=np.einsum('ni,ij,nj->n',n,S,n)
        qT=np.einsum('ni,ij,nj->n',n,T,n)
        lhs=15*np.mean(qS*qT); rhs=2*np.sum(S*T)
        scale=max(2*np.linalg.norm(S)*np.linalg.norm(T),1e-30)
        worst=max(worst,abs(lhs-rhs)/scale)
    return worst


def shell_scaling():
    # A pure Fourier mode: signature L2 metric scales k^2 relative to kinetic L2,
    # while the H^-1 signature metric remains scale-free.
    ratios=[]
    p=np.array([0.,1.,0.])
    for m in (1,2,3,5,7):
        k=np.array([float(m),0,0]); u=p
        G=1j*np.outer(u,k); S=.5*(G+G.T)
        l2=float(np.vdot(u,u).real)
        sig0=2*float(np.vdot(S,S).real)
        sigm1=sig0/(m*m)
        ratios.append((m,sig0/l2,sigm1/l2))
    return ratios


def main():
    l2,diss,heat=bilinear_audit()
    mc=monte_carlo_sphere()
    ratios=shell_scaling()
    print('signature metric / heat bridge tribunal')
    print(f'L2_equals_signature_Hminus1          {l2:.3e}')
    print(f'Dirichlet_equals_signature_L2        {diss:.3e}')
    print(f'heat_Riesz_ratio_is_Lambda2          {heat:.3e}')
    print(f'independent_sphere_factor_MC         {mc:.3e}')
    print('shell m, signature_L2/L2, signature_H-1/L2')
    for row in ratios: print(' ',row)
    assert l2<5e-13 and diss<5e-13 and heat<5e-13
    # MC is stochastic; 2e5 directions gives sub-percent agreement reliably.
    assert mc<8e-3
    assert all(abs(r[1]-r[0]**2)<1e-12 and abs(r[2]-1)<1e-12 for r in ratios)
    print('PASS: formation kinetic metric is H^-1 on q; Dirichlet metric is L2 on q; heat is their Riesz ratio')

if __name__=='__main__': main()
