#!/usr/bin/env python3
"""Restricted local-Euclidean rigidity tribunal for the formation core.

This does not classify every conceivable fluid bracket.  It tests the full isotropic
constant-coefficient first-order antisymmetric bilinear tensor family and asks which
members act as the ordinary derivation of scalar multiplication.
"""
from __future__ import annotations
import numpy as np

RNG=np.random.default_rng(20260821)


def family(c,a,b,Ga,Gb):
    """Three isotropic delta contractions, antisymmetrized in (a,b).
    Ga[i,j]=partial_j a_i, Gb likewise.
    """
    c1,c2,c3=c
    diva=np.trace(Ga); divb=np.trace(Gb)
    term1=a*divb-b*diva
    term2=Gb@a-Ga@b
    term3=Gb.T@a-Ga.T@b
    return c1*term1+c2*term2+c3*term3


def derivation_matrix(samples=500):
    """Linear constraints from B(a,f b)=f B(a,b)+(a.grad f)b.
    Normalization is included by the coefficient 1 of a(f)b.
    We solve affine A c = y, not a homogeneous nullspace.
    """
    rows=[]; rhs=[]
    for _ in range(samples):
        a=RNG.normal(size=3); b=RNG.normal(size=3)
        Ga=RNG.normal(size=(3,3)); Gb=RNG.normal(size=(3,3))
        f=float(RNG.normal()); gf=RNG.normal(size=3)
        # gradient of f b: partial_j(f b_i)=b_i gf_j + f Gb[i,j]
        Gfb=np.outer(b,gf)+f*Gb
        target=(a@gf)*b
        base=[]
        for j in range(3):
            e=np.zeros(3); e[j]=1
            base.append(family(e,a,f*b,Ga,Gfb)-f*family(e,a,b,Ga,Gb))
        D=np.stack(base,axis=1) # output component x coefficient
        rows.append(D); rhs.append(target)
    return np.vstack(rows),np.concatenate(rhs)


def homogeneous_extra_freedom(samples=500):
    """After subtracting the ordinary bracket, test whether any isotropic perturbation
    obeys zero scalar derivation defect.  Kernel should be zero.
    """
    A,_=derivation_matrix(samples)
    return np.linalg.svd(A,compute_uv=False)


def curl_equivariant_pseudotensor_rank(rotations=30):
    """SO(3)-equivariant rank-3 pseudotensors A_ijk. Expected one-dimensional epsilon span."""
    # Unknown flattened 27 tensor. Constraint R_iα A_αβγ = A_ijk R_jβ R_kγ.
    mats=[]
    for _ in range(rotations):
        Q,_=np.linalg.qr(RNG.normal(size=(3,3)))
        if np.linalg.det(Q)<0: Q[:,0]*=-1
        M=np.zeros((27,27))
        def idx(i,j,k): return 9*i+3*j+k
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    row=idx(i,j,k)
                    # (R A)_{ijk}
                    for alpha in range(3):
                        M[row,idx(alpha,j,k)] += Q[i,alpha]
                    # -(A R R)_{ijk}
                    for beta in range(3):
                        for gamma in range(3):
                            M[row,idx(i,beta,gamma)] -= Q[beta,j]*Q[gamma,k]
        mats.append(M)
    A=np.vstack(mats)
    s=np.linalg.svd(A,compute_uv=False)
    rank=np.sum(s>1e-10*s[0])
    nullity=27-rank
    # explicit epsilon residual
    eps=np.zeros((3,3,3))
    eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1
    eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1
    er=np.linalg.norm(A@eps.reshape(-1))/max(np.linalg.norm(A)*np.linalg.norm(eps),1e-30)
    return nullity,er,s


def main():
    A,y=derivation_matrix(800)
    c,*_=np.linalg.lstsq(A,y,rcond=None)
    res=np.linalg.norm(A@c-y)/np.linalg.norm(y)
    s=np.linalg.svd(A,compute_uv=False)
    rank=np.sum(s>1e-12*s[0])
    nullity=3-rank

    # Direct bracket coefficient target is c=(0,1,0).
    target=np.array([0.,1.,0.])
    coeff_err=np.linalg.norm(c-target)
    dark=np.array([1.,0.,1.])
    dark_def=np.linalg.norm(A@dark-y)/np.linalg.norm(y)

    cnull,epsres,cs=curl_equivariant_pseudotensor_rank()

    print('physical-axiom rigidity tribunal')
    print(f'derivation_rank                         {rank}/3')
    print(f'derivation_affine_nullity               {nullity}')
    print(f'recovered_coefficients                  {c}')
    print(f'coefficient_error                       {coeff_err:.3e}')
    print(f'derivation_residual                     {res:.3e}')
    print(f'fake_isotropic_law_residual             {dark_def:.3e}')
    print(f'curl_equivariant_tensor_nullity         {cnull}')
    print(f'epsilon_tensor_residual                 {epsres:.3e}')

    assert rank==3 and nullity==0
    assert coeff_err<1e-13 and res<1e-13
    assert dark_def>0.1
    assert cnull==1 and epsres<1e-14
    print('PASS: scalar derivation fixes the vector-field bracket; SO(3) equivariance fixes curl direction up to scale/orientation')

if __name__=='__main__': main()
