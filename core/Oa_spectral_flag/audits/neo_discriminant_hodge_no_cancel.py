"""Finite-Fourier anti-test: the discriminant Hodge source has no universal integral cancellation.

This is a torus algebraic audit, not a theorem about the Type-I whole-space class.
It constructs smooth low-frequency real divergence-free states, reconstructs g=-Delta p
and the trace-free pressure Hessian H0, then evaluates
    g^2 A:H0 - 6 r A^2:H0.
Both signs of its spatial mean occur.
"""
import numpy as np

N=12
ks=np.fft.fftfreq(N)*N
kx,ky,kz=np.meshgrid(ks,ks,ks,indexing='ij')
k=np.stack([kx,ky,kz],axis=-1)
k2=np.sum(k*k,axis=-1)
mask=k2>0
low=(np.sqrt(k2)<=2)[...,None]

def project(uh):
    out=uh.copy()
    dot=np.sum(out*k,axis=-1)
    out[mask]-=k[mask]*(dot[mask]/k2[mask])[...,None]
    out[~mask]=0
    return out

def hodge_source_mean(seed):
    rng=np.random.default_rng(seed)
    u=rng.normal(size=(N,N,N,3))
    uh=np.fft.fftn(u,axes=(0,1,2))
    uh=project(uh*low)

    A=np.zeros((N,N,N,3,3))
    for j in range(3):
        A[..., :, j]=np.fft.ifftn(1j*k[...,j,None]*uh,axes=(0,1,2)).real

    A2=np.einsum('...ik,...kj->...ij',A,A)
    A3=np.einsum('...ik,...kj->...ij',A2,A)
    g=np.trace(A2,axis1=-2,axis2=-1)
    r=np.trace(A3,axis1=-2,axis2=-1)

    gh=np.fft.fftn(g,axes=(0,1,2))
    ph=np.zeros_like(gh,dtype=complex)
    ph[mask]=gh[mask]/k2[mask]  # -Delta p=g

    H0=np.zeros_like(A)
    for i in range(3):
        for j in range(3):
            hij=np.fft.ifftn(-k[...,i]*k[...,j]*ph,axes=(0,1,2)).real
            if i==j:
                hij += g/3
            H0[...,i,j]=hij

    AH=np.einsum('...ij,...ij->...',A,H0)
    A2H=np.einsum('...ij,...ij->...',A2,H0)
    src=g*g*AH-6*r*A2H
    return float(src.mean()), float(np.mean(np.abs(src)))

vals=[hodge_source_mean(seed) for seed in range(12)]
means=np.array([x[0] for x in vals])
print('source means:',means)
print('mean absolute source range:',min(x[1] for x in vals),max(x[1] for x in vals))
assert means.min() < -1e-10
assert means.max() > 1e-10
print('PASS: discriminant Hodge source has no universal spatial-integral cancellation in the finite-Fourier audit')
