#!/usr/bin/env python3
"""Microlocal reverse bridge: six principal mother readings -> strain -> state -> formation.

No metric-Lie tensor/pseudoinverse of the formation map is used in the decoder.
The only state data supplied to the decoder are q_u(x,n)=n^T S(u)(x)n in six
fixed directions, i.e. the principal-symbol readings of the mother signature.
"""
from __future__ import annotations
import numpy as np

N=18
NU=0.137
RNG=np.random.default_rng(20260821)
ks=np.fft.fftfreq(N,d=1.0/N)
KX,KY,KZ=np.meshgrid(ks,ks,ks,indexing='ij')
K=(KX,KY,KZ)
K2=KX*KX+KY*KY+KZ*KZ

DIRS=np.array([
 [1,0,0],[0,1,0],[0,0,1],
 [1/np.sqrt(2),1/np.sqrt(2),0],
 [1/np.sqrt(2),0,1/np.sqrt(2)],
 [0,1/np.sqrt(2),1/np.sqrt(2)]],float)
rt2=np.sqrt(2.0); rt6=np.sqrt(6.0)
SYM0=np.array([
 [[1/rt2,0,0],[0,-1/rt2,0],[0,0,0]],
 [[1/rt6,0,0],[0,1/rt6,0],[0,0,-2/rt6]],
 [[0,1/rt2,0],[1/rt2,0,0],[0,0,0]],
 [[0,0,1/rt2],[0,0,0],[1/rt2,0,0]],
 [[0,0,0],[0,0,1/rt2],[0,1/rt2,0]],
],float)
FRAME=np.einsum('ri,aij,rj->ra',DIRS,SYM0,DIRS)
FRAME_PINV=np.linalg.pinv(FRAME)


def fft(v): return np.fft.fftn(v,axes=(0,1,2))
def ifft(vh): return np.fft.ifftn(vh,axes=(0,1,2)).real

def project(v):
    vh=fft(v); dot=KX*vh[...,0]+KY*vh[...,1]+KZ*vh[...,2]
    nz=K2>0
    for j,kj in enumerate(K): vh[...,j][nz]-=kj[nz]*dot[nz]/K2[nz]
    vh[0,0,0]=0
    return ifft(vh)

def lowpass(v,cut=2):
    vh=fft(v); mask=(abs(KX)<=cut)&(abs(KY)<=cut)&(abs(KZ)<=cut)
    vh*=mask[...,None]; vh[0,0,0]=0
    return ifft(vh)
def rand(seed): return project(lowpass(np.random.default_rng(seed).normal(size=(N,N,N,3))))
def deriv(v,j): return ifft((1j*K[j])[...,None]*fft(v))
def grad(v): return np.stack([deriv(v,j) for j in range(3)],axis=-1)
def curl(v):
    d=[deriv(v,j) for j in range(3)]
    o=np.empty_like(v); o[...,0]=d[1][...,2]-d[2][...,1]; o[...,1]=d[2][...,0]-d[0][...,2]; o[...,2]=d[0][...,1]-d[1][...,0]; return o
def c2(v): return curl(curl(v))
def adv(a,b): return np.einsum('...j,...ij->...i',a,grad(b))
def J(u,b): return project(np.cross(b,curl(u)))
def inner(a,b): return float(np.mean(np.sum(a*b,axis=-1)))
def norm(a): return float(np.sqrt(max(inner(a,a),0.0)))
def rel(a,b): return norm(a-b)/max(norm(a),norm(b),1e-30)

def strain(v):
    A=grad(v); return 0.5*(A+np.swapaxes(A,-1,-2))

def readings(S): return np.einsum('ri,...ij,rj->...r',DIRS,S,DIRS)

def decode_strain(q):
    coeff=np.einsum('ar,...r->...a',FRAME_PINV,q)
    return np.einsum('...a,aij->...ij',coeff,SYM0)

def decode_velocity(S):
    Sh=np.fft.fftn(S,axes=(0,1,2))
    rhs=np.zeros((N,N,N,3),complex)
    for i in range(3):
        rhs[...,i]=1j*(Sh[...,i,0]*KX+Sh[...,i,1]*KY+Sh[...,i,2]*KZ)
    uh=np.zeros_like(rhs); nz=K2>0
    uh[nz]=(-2.0/K2[nz,None])*rhs[nz]
    uh[0,0,0]=0
    return ifft(uh)


def lowpass_cut(v,cut=4):
    vh=fft(v); mask=(abs(KX)<=cut)&(abs(KY)<=cut)&(abs(KZ)<=cut)
    vh*=mask[...,None]; vh[0,0,0]=0
    return ifft(vh)

def F_galerkin(v):
    return lowpass_cut(-project(adv(v,v)) - NU*c2(v), 4)

def q_of_velocity(v): return readings(strain(v))

def decode_q(q): return decode_velocity(decode_strain(q))

def F_q(q): return q_of_velocity(F_galerkin(decode_q(q)))

def rk4(f,y,h):
    k1=f(y); k2=f(y+0.5*h*k1); k3=f(y+0.5*h*k2); k4=f(y+h*k3)
    return y+(h/6)*(k1+2*k2+2*k3+k4)

def dynamic_commuting_test():
    u=rand(777); q=q_of_velocity(u)
    h=5e-4
    worst=0.0
    for _ in range(80):
        u=rk4(F_galerkin,u,h)
        q=rk4(F_q,q,h)
        qtrue=q_of_velocity(u)
        worst=max(worst,float(np.linalg.norm(q-qtrue)/max(np.linalg.norm(q),np.linalg.norm(qtrue),1e-30)))
    u_from_q=decode_q(q)
    return worst, rel(u_from_q,u)

def audit(trials=12):
    worst={k:0.0 for k in ['strain','state','vorticity','poisson_action','formation_rhs','pressure_source','stretching']}
    for t in range(trials):
        u=rand(100+t); S=strain(u); q=readings(S); Sr=decode_strain(q); ur=decode_velocity(Sr)
        worst['strain']=max(worst['strain'],float(np.linalg.norm(S-Sr)/max(np.linalg.norm(S),1e-30)))
        worst['state']=max(worst['state'],rel(u,ur)); worst['vorticity']=max(worst['vorticity'],rel(curl(u),curl(ur)))
        for j in range(3):
            b=rand(1000+10*t+j)
            worst['poisson_action']=max(worst['poisson_action'],rel(J(u,b),J(ur,b)))
        Fu=J(u,u)-NU*c2(u); Fr=J(ur,ur)-NU*c2(ur)
        worst['formation_rhs']=max(worst['formation_rhs'],rel(Fu,Fr))
        A=grad(u); Ar=grad(ur)
        g=np.einsum('...ij,...ji->...',A,A); gr=np.einsum('...ij,...ji->...',Ar,Ar)
        worst['pressure_source']=max(worst['pressure_source'],float(np.linalg.norm(g-gr)/max(np.linalg.norm(g),1e-30)))
        w=curl(u); wr=curl(ur)
        Q=float(np.mean(np.einsum('...i,...ij,...j->...',w,S,w)))
        Qr=float(np.mean(np.einsum('...i,...ij,...j->...',wr,Sr,wr)))
        worst['stretching']=max(worst['stretching'],abs(Q-Qr)/max(abs(Q),abs(Qr),1.0))
    return worst

def main():
    r=audit(); print('six-direction mother -> formation microlocal tribunal')
    for k,v in r.items(): print(f'{k:28s} {v:.3e}')
    dyn,state=dynamic_commuting_test()
    print(f"{'trajectory_commutes':28s} {dyn:.3e}")
    print(f"{'trajectory_state_decode':28s} {state:.3e}")
    w=max(max(r.values()),dyn,state)
    if w>2e-10: raise SystemExit(f'FAIL {w:.3e}')
    print(f'PASS: worst residual {w:.3e}')
if __name__=='__main__': main()
