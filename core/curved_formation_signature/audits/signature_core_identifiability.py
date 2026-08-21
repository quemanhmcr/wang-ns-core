#!/usr/bin/env python3
"""Strong inverse/negative-control tribunal for Formation--Signature Geometry.

Questions:
1. Does the *full signature-side operator field* recover the transported formation tensor?
2. Does curvature reconstructed only from transported (G,T,C) match the formation side?
3. Can signature snapshots + diagonal dynamics identify an arbitrary background core?

The last answer is deliberately tested with an exact vertical dark-sector collision.
"""
from __future__ import annotations

import numpy as np

from metric_lie_spectral_unification import (
    NU, RNG, build_physical_tensors, mother_tensor, shifted_signature_map,
    reduced_coordinate_map, transported_structures, formation_from_structures,
    J_from_T, scaled,
)


def koszul_from_lowered_T(G: np.ndarray, T: np.ndarray) -> np.ndarray:
    """Gamma[k,a,b] in arbitrary coordinates, from metric G and lowered T[k,a,b]."""
    d = G.shape[0]
    lower = np.zeros_like(T)
    for k in range(d):
        for a in range(d):
            for b in range(d):
                lower[k,a,b] = 0.5*(T[k,a,b] - T[a,b,k] + T[b,k,a])
    # raise output slot
    return np.einsum('lk,kab->lab', np.linalg.inv(G), lower)


def bracket_from_GT(G: np.ndarray, T: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    cov = np.einsum('ijk,j,k->i', T, a, b)
    return np.linalg.solve(G, cov)


def curvature_matrices(G: np.ndarray, T: np.ndarray) -> np.ndarray:
    """R[:,:,a,b] = operator R(e_a,e_b)."""
    Gamma = koszul_from_lowered_T(G, T)
    d = G.shape[0]
    R = np.zeros((d,d,d,d))
    eye = np.eye(d)
    for a in range(d):
        Ga = np.einsum('i,kib->kb', eye[a], Gamma)
        for b in range(d):
            Gb = np.einsum('i,kib->kb', eye[b], Gamma)
            br = bracket_from_GT(G, T, eye[a], eye[b])
            Gbr = np.einsum('i,kib->kb', br, Gamma)
            R[:,:,a,b] = Ga @ Gb - Gb @ Ga - Gbr
    return R


def reconstruct_T_from_operator_samples(G, C, zs, Ls, nu=NU):
    """Recover lowered T from full L(z), knowing transported metric and curl."""
    heat_cov = C.T @ G @ C
    H = np.linalg.solve(G, heat_cov)
    # G J(z) = - sum_i z_i T_i
    Y = np.stack([G @ (L + nu*H) for L in Ls], axis=0)  # ns,d,d
    Z = np.asarray(zs)
    # solve Z X = -Y for X[i,a,b]
    X, *_ = np.linalg.lstsq(Z, -Y.reshape(len(Z), -1), rcond=None)
    return X.reshape(Z.shape[1], G.shape[0], G.shape[0])


def inverse_core_tribunal(tag: str, T, C, M):
    R, G, Tz, Cz = transported_structures(T, C, M)
    d = len(M)
    # Deliberately use random signature states, not basis probes.
    Z = RNG.normal(size=(d+5,d))
    while np.linalg.matrix_rank(Z) < d:
        Z = RNG.normal(size=(d+5,d))
    Ls = [formation_from_structures(z,G,Tz,Cz)[0] for z in Z]
    Trec = reconstruct_T_from_operator_samples(G,Cz,Z,Ls)
    rT = scaled(Trec,Tz)

    # Identifiability threshold: d-1 generic states cannot determine all state-slot contractions.
    Zm = Z[:d-1]
    rank_minus = np.linalg.matrix_rank(Zm)
    state_nullity = d-rank_minus

    # Curvature reconstructed only from signature-side G,T versus conjugated original curvature.
    Rz = curvature_matrices(G,Tz)
    R0 = curvature_matrices(np.eye(d),T)
    # Compare as multilinear operator: for random a,b,c, Rz(Ma,Mb)Mc = M R0(a,b)c.
    rworst=0.0
    for _ in range(30):
        a,b,c = (RNG.normal(size=d) for __ in range(3))
        za,zb,zc = M@a,M@b,M@c
        lhs = np.einsum('klab,a,b,l->k', Rz, za, zb, zc)
        rhs0 = np.einsum('klab,a,b,l->k', R0, a,b,c)
        rworst=max(rworst,scaled(lhs,M@rhs0))

    return {
        f'{tag}_T_from_full_operator_field': rT,
        f'{tag}_d_minus_1_state_nullity': state_nullity,
        f'{tag}_curvature_reconstruction': rworst,
        f'{tag}_T_norm': float(np.linalg.norm(Tz)),
    }


def vertical_dark_sector_collision():
    """Exact abstract collision hidden from signature + diagonal flow.

    Core 0: abelian R^6.
    Core 1: so(3) on the first 3D eigenspace of C, abelian on the second.
    The Euclidean metric is Ad-invariant on so(3), hence B(u,u)=0 there.
    Since C is scalar on that eigenspace, [nabla_u,C]=0 as well.
    Therefore both the entire mother/flag map and diagonal formation flow coincide,
    while the full Poisson operator field differs.
    """
    d=6
    G=np.eye(d)
    C=np.diag([1.,1.,1.,2.,2.,2.])
    T0=np.zeros((d,d,d))
    T1=np.zeros_like(T0)
    # epsilon_{ijk} on first block; T[out,a,b] = <e_out,[e_a,e_b]>.
    eps = np.zeros((3,3,3))
    eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1.
    eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1.
    T1[:3,:3,:3]=eps

    Gam0=koszul_from_lowered_T(G,T0)
    Gam1=koszul_from_lowered_T(G,T1)

    def mother_map(Gam):
        cols=[]
        for j in range(d):
            D=Gam[:,j,:]
            cols.append((D@C-C@D).reshape(-1))
        return np.column_stack(cols)
    M0,M1=mother_map(Gam0),mother_map(Gam1)

    # Full shifted flag: only one nontrivial cut between eigenvalues 1 and 2.
    H=np.diag([-1.,-1.,-1.,1.,1.,1.])
    def flag_map(Gam):
        cols=[]
        for j in range(d):
            v=np.eye(d)[j]
            D=Gam[:,j,:]
            A=D@H-H@D
            Hv=H@v
            DH=np.einsum('a,kab->kb',Hv,Gam)
            AH=DH@H-H@DH
            O=H@A-AH
            cols.append(O.reshape(-1))
        return np.column_stack(cols)
    O0,O1=flag_map(Gam0),flag_map(Gam1)

    # Diagonal vector field for every u is pure heat in both cores.
    fw=0.0; jw=0.0
    for _ in range(50):
        u=RNG.normal(size=d)
        J0=J_from_T(T0,u); J1=J_from_T(T1,u)
        F0=(J0-NU*C@C)@u
        F1=(J1-NU*C@C)@u
        fw=max(fw,scaled(F0,F1))
        jw=max(jw,float(np.linalg.norm(J1-J0)))

    return {
        'dark_mother_map_collision': scaled(M0,M1),
        'dark_flag_map_collision': scaled(O0,O1),
        'dark_diagonal_flow_collision': fw,
        'dark_core_tensor_difference': float(np.linalg.norm(T1-T0)),
        'dark_poisson_operator_difference_max': jw,
    }


def three_form_spray_ambiguity():
    """Show diagonal Euler spray forgets the totally antisymmetric metric-Lie component."""
    d=3
    T0=np.zeros((d,d,d))
    T1=np.zeros_like(T0)
    eps=np.zeros_like(T0)
    eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1.
    eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1.
    T1=eps
    spray=0.0; op=0.0
    for _ in range(50):
        u=RNG.normal(size=d)
        J0=J_from_T(T0,u); J1=J_from_T(T1,u)
        spray=max(spray,float(np.linalg.norm(J1@u-J0@u)))
        op=max(op,float(np.linalg.norm(J1-J0)))
    return {
        'three_form_euler_spray_difference': spray,
        'three_form_poisson_operator_difference_max': op,
        'three_form_tensor_difference': float(np.linalg.norm(T1-T0)),
    }


def main():
    data=build_physical_tensors(False)
    T,C,Gamma=data['T'],data['C'],data['Gamma']
    AE,_=mother_tensor(Gamma,C)
    AO,_,_=shifted_signature_map(Gamma,C)
    ME,_,_,rE=reduced_coordinate_map(AE)
    MO,_,_,rO=reduced_coordinate_map(AO)
    assert rE==rO==len(C)

    out={}
    out.update(inverse_core_tribunal('mother',T,C,ME))
    out.update(inverse_core_tribunal('flag',T,C,MO))
    out.update(vertical_dark_sector_collision())
    out.update(three_form_spray_ambiguity())

    print('signature/core identifiability tribunal')
    for k,v in out.items():
        if isinstance(v,(int,np.integer)):
            print(f'{k:46s} {v}')
        else:
            print(f'{k:46s} {v:.3e}')

    assert out['mother_T_from_full_operator_field'] < 5e-12
    assert out['flag_T_from_full_operator_field'] < 5e-12
    assert out['mother_curvature_reconstruction'] < 5e-11
    assert out['flag_curvature_reconstruction'] < 5e-11
    assert out['mother_d_minus_1_state_nullity'] == 1
    assert out['flag_d_minus_1_state_nullity'] == 1
    assert out['dark_mother_map_collision'] < 1e-13
    assert out['dark_flag_map_collision'] < 1e-13
    assert out['dark_diagonal_flow_collision'] < 1e-13
    assert out['dark_core_tensor_difference'] > 1.0
    assert out['dark_poisson_operator_difference_max'] > 0.1
    assert out['three_form_euler_spray_difference'] < 1e-13
    assert out['three_form_poisson_operator_difference_max'] > 0.1
    print('PASS: full operator field identifies transported core; snapshot/diagonal data do not in abstract dark sectors')


if __name__=='__main__':
    main()
