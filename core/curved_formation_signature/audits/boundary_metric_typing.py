#!/usr/bin/env python3
import numpy as np
rng=np.random.default_rng(20260903)

def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def adj(A,G):return np.linalg.solve(G,A.T@G)
def symG(A,G):return .5*(A+adj(A,G))
def skewG(A,G):return .5*(A-adj(A,G))
def conn(conn,v):return sum(float(v[i])*conn[i] for i in range(len(conn)))
def O(conn,H,v):
 D=conn_apply(conn,v);A=D@H-H@D;Hv=H@v;DH=conn_apply(conn,Hv);AH=DH@H-H@DH;return H@A-AH,A,AH
def conn_apply(L,v):return sum(float(v[i])*L[i] for i in range(len(L)))

def transformed_case(n=6):
 H0=np.diag([1.]*(n//2)+[-1.]*(n-n//2));K=[]
 for _ in range(n):X=rng.normal(size=(n,n));K.append(X-X.T)
 Q1,_=np.linalg.qr(rng.normal(size=(n,n)));Q2,_=np.linalg.qr(rng.normal(size=(n,n)));S=Q1@np.diag(np.geomspace(1,20,n))@Q2.T;R=np.linalg.inv(S);G=R.T@R;H=S@H0@R
 # transform connection one-form including input slot
 L=[]
 for i in range(n):
  Ki=sum(R[j,i]*K[j] for j in range(n));L.append(S@Ki@R)
 v=rng.normal(size=n);o,A,AH=O(L,H,v)
 Ag=H@skewG(o,G);AHg=-symG(o,G)
 Ae=H@(.5*(o-o.T));AHe=-.5*(o+o.T)
 return rel(H.T,H),rel(adj(H,G),H),rel(A,Ag),rel(AH,AHg),rel(A,Ae),rel(AH,AHe)

print('metric/domain typing tribunal')
r=transformed_case();print('nonorthogonal chart: H_Euclid_asym, H_G_selfadj, G_reverse_A, G_reverse_AH, wrong_E_A, wrong_E_AH=',r)
assert r[1]<1e-12 and r[2]<1e-12 and r[3]<1e-12 and r[4]>.05 and r[5]>.05
# Fixed-L2 nonnormal curl analog: real diagonalizable but its sign cut is not L2 self-adjoint.
n=6;Q1,_=np.linalg.qr(rng.normal(size=(n,n)));Q2,_=np.linalg.qr(rng.normal(size=(n,n)));S=Q1@np.diag(np.geomspace(1,30,n))@Q2.T;R=np.linalg.inv(S);roots=np.array([-3,-2,-1,1,2,3.]);C=S@np.diag(roots)@R;H=S@np.diag(np.sign(roots))@R
L=[]
for _ in range(n):X=rng.normal(size=(n,n));L.append(X-X.T)
v=rng.normal(size=n);o,A,AH=O(L,H,v);Ae=H@(.5*(o-o.T));AHe=-.5*(o+o.T)
Stokes=C.T@C
print('fixed L2 nonnormal analog: H_selfadj_defect',rel(H,H.T),'reverse_A_failure',rel(A,Ae),'reverse_AH_failure',rel(AH,AHe),'Stokes_symmetry',rel(Stokes,Stokes.T),'Stokes_min_eig',np.min(np.linalg.eigvalsh(Stokes)))
assert rel(H,H.T)>.05 and rel(A,Ae)>.05 and rel(AH,AHe)>.05 and rel(Stokes,Stokes.T)<1e-13 and np.min(np.linalg.eigvalsh(Stokes))>0
print('PASS: reverse spectral compiler is metric/domain typed. Non-self-adjoint raw curl in the physical L2 metric breaks the canonical adjoint-parity formulas, while the positive Stokes/Dirichlet form survives. Boundary extension therefore needs an L2-compatible self-adjoint curl realization or a typed Hodge/form reformulation.')
