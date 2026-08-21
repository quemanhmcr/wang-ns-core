#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,pathlib,numpy as np
P=pathlib.Path(__file__).with_name('ek_exact_lie_reconstruction.py');sp=importlib.util.spec_from_file_location('ek',P);ek=importlib.util.module_from_spec(sp);sp.loader.exec_module(ek)
rng=np.random.default_rng(202608212131)
def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def transport(Gs,C,M):
 R=np.linalg.inv(M);d=len(Gs);Gz=R.T@R;Cz=M@C@R;Gzlist=[]
 for i in range(d): Gzlist.append(M@sum(R[j,i]*Gs[j] for j in range(d))@R)
 return Gz,Gzlist,Cz
def transform_forms(E,K,S,to_y=True):
 # z=S y. to y: S^-1 E_{S e_i} S ; two-form analog.
 T=np.linalg.inv(S) if to_y else S
 U=S if to_y else np.linalg.inv(S)
 d=len(E);Ey=[]
 for i in range(d):Ey.append(T@sum(S[a,i]*E[a] for a in range(d))@U)
 Ky={}
 for i in range(d):
  for j in range(i+1,d):
   X=np.zeros_like(E[0])
   for a in range(d):
    for b in range(d):
     if a==b:continue
     p=(min(a,b),max(a,b));sg=1 if a<b else -1
     X+=S[a,i]*S[b,j]*sg*K[p]
   Ky[i,j]=T@X@U
 return Ey,Ky
def inverse_orthonormal(E,C,K):
 B=ek.B_from_E(E,C);_,_,_,H=ek.vertical_basis(C);d=len(C);q=len(H);y0,A=ek.codazzi_matrix(B,H,C);y=ek.flatten_K(K,d)-y0
 x,*_=np.linalg.lstsq(A,y,rcond=None);Gs=ek.from_x(B,H,x.reshape(d,q) if q else np.zeros((d,0)));return Gs
def main():
 c=ek.direct_sum(ek.std_so3(),ek.heisenberg3());c=ek.randomize_metric(c,1337);G=ek.levi_from_structure(c);Gs=ek.gamma_mats(G);C=np.diag([-2,-2,0,0,3,3]);E,K,R=ek.EK(Gs,C);d=len(C)
 print('metric-covariant E+K reconstruction tribunal')
 for cond in [1,10,100,1000]:
  Q1,_=np.linalg.qr(rng.normal(size=(d,d)));Q2,_=np.linalg.qr(rng.normal(size=(d,d)));sv=np.geomspace(1,cond,d);M=Q1@np.diag(sv)@Q2.T
  Gz,Gzl,Cz=transport(Gs,C,M);Ez,Kz,_=ek.EK(Gzl,Cz)
  # whiten using only observed metric Gz. z=S y with S=G^-1/2.
  lam,U=np.linalg.eigh(Gz);S=U@np.diag(lam**-.5)@U.T
  Cy=np.linalg.inv(S)@Cz@S;Ey,Ky=transform_forms(Ez,Kz,S,True);Gyr=inverse_orthonormal(Ey,Cy,Ky)
  # back y -> z connection
  Sz_inv=np.linalg.inv(S);Gzr=[]
  for a in range(d):
   # Gamma_z,a = S Gamma_y,(S^-1 e_a) S^-1
   coeff=Sz_inv[:,a];Gzr.append(S@sum(coeff[i]*Gyr[i] for i in range(d))@Sz_inv)
  err=rel(np.stack(Gzr),np.stack(Gzl))
  # wrong control: pretend z metric identity; symmetrize C just to make naive spectral inversion runnable.
  Cwrong=(Cz+Cz.T)/2
  Ewrong=[ek.comm(A,Cwrong) for A in Gzl];Kwrong=ek.EK(Gzl,Cwrong)[1]
  try: Gw=inverse_orthonormal(Ewrong,Cwrong,Kwrong);wrong=rel(np.stack(Gw),np.stack(Gzl))
  except Exception:wrong=np.inf
  metricdef=max(np.linalg.norm(A.T@Gz+Gz@A) for A in Gzl)
  print('cond',cond,'metric_compat',metricdef,'correct_recovery',err,'naive_Euclidean_failure',wrong)
  assert err<2e-7*max(1,cond/100)
  if cond>=10:assert wrong>.1
 print('PASS: geometric completeness is coordinate-covariant only after carrying the transported Riesz metric. Whitening from G reconstructs the same connection through highly non-orthogonal charts; Euclideanizing the signature chart fails by order one.')
if __name__=='__main__':main()
