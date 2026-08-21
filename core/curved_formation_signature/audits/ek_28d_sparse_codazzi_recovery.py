#!/usr/bin/env python3
from __future__ import annotations
import sys,pathlib,numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import lsqr, svds
ROOT=pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'core'/'curved_formation_signature'/'audits'))
import metric_lie_spectral_unification as m
import signature_core_identifiability as sci
rng=np.random.default_rng(202608212130)

def rel(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)
def comm(A,B):return A@B-B@A

def main():
 data=m.build_physical_tensors(False);T,C,G=data['T'],data['C'],data['Gamma'];Gs=[G[:,i,:] for i in range(len(C))];d=len(C)
 E=[comm(A,C) for A in Gs]
 # spectral B and vertical basis
 vals,Q=np.linalg.eigh(C);B=[]
 for Ei in E:
  X=Q.T@Ei@Q;Y=np.zeros_like(X)
  for a in range(d):
   for b in range(d):
    gap=vals[b]-vals[a]
    if abs(gap)>1e-9:Y[a,b]=X[a,b]/gap
  B.append(Q@Y@Q.T)
 blocks=[];used=np.zeros(d,bool)
 for i,x in enumerate(vals):
  if used[i]:continue
  ids=np.where(np.abs(vals-x)<1e-8)[0];used[ids]=True;blocks.append(ids)
 H=[]
 for ids in blocks:
  for aa in range(len(ids)):
   for bb in range(aa+1,len(ids)):
    Z=np.zeros((d,d));i,j=ids[aa],ids[bb];Z[i,j]=1;Z[j,i]=-1;H.append(Q@Z@Q.T)
 q=len(H);unknown=d*q
 xt=np.array([[np.vdot(h,Gs[i]-B[i]).real/np.vdot(h,h).real for h in H] for i in range(d)]).reshape(-1)
 # observed K and B-only K from torsion-free connection geometry
 Kobs=sci.curvature_matrices(np.eye(d),T)
 Kobs={(i,j):comm(Kobs[:,:,i,j],C) for i in range(d) for j in range(i+1,d)}
 # B-induced structure/curvature
 cb=sci.bracket_from_GT # unused
 def curv_from(Glist,i,j):
  ei=np.eye(d)[i];ej=np.eye(d)[j];cij=Glist[i]@ej-Glist[j]@ei;Gbr=sum(cij[k]*Glist[k] for k in range(d));return comm(Glist[i],Glist[j])-Gbr
 K0={(i,j):comm(curv_from(B,i,j),C) for i in range(d) for j in range(i+1,d)}
 # randomized scalar measurements per pair; sparse because pair (i,j) depends only on V_i,V_j.
 rproj=12; rows=[];cols=[];dat=[];y=[];row=0
 pairs=[(i,j) for i in range(d) for j in range(i+1,d)]
 for i,j in pairs:
  Fs=[]
  for _ in range(rproj):
   F=rng.normal(size=(d,d));F=(F+F.T)/2;F/=np.linalg.norm(F);Fs.append(F)
  target=Kobs[i,j]-K0[i,j]
  for F in Fs:
   y.append(np.vdot(F,target).real)
   for a,h in enumerate(H):
    # slot i variation
    cv=h@np.eye(d)[j]
    D=comm(h,B[j])-sum(cv[k]*B[k] for k in range(d));coef=np.vdot(F,comm(D,C)).real
    if abs(coef)>1e-13:rows.append(row);cols.append(i*q+a);dat.append(coef)
    # slot j variation
    cv=-h@np.eye(d)[i]
    D=comm(B[i],h)-sum(cv[k]*B[k] for k in range(d));coef=np.vdot(F,comm(D,C)).real
    if abs(coef)>1e-13:rows.append(row);cols.append(j*q+a);dat.append(coef)
   row+=1
 A=coo_matrix((dat,(rows,cols)),shape=(row,unknown)).tocsr();y=np.array(y)
 sol=lsqr(A,y,atol=1e-13,btol=1e-13,iter_lim=10000);xr=sol[0];err=rel(xr,xt);res=np.linalg.norm(A@xr-y)/np.linalg.norm(y)
 print('28D sparse Codazzi recovery coordinate tribunal')
 print('curl root multiplicities',[len(x) for x in blocks],'vertical_per_slot',q,'unknowns',unknown,'measurements',A.shape[0],'nnz',A.nnz)
 print('lsqr istop,iters,acond',sol[1],sol[2],sol[6],'hidden_connection_relerr',err,'measurement_residual',res)
 print('measurement-density phase diagram')
 phase=[]
 npairs=len(pairs)
 for rp in [2,3,4,5,6,8,10,12]:
  idx=np.concatenate([np.arange(pp*rproj,pp*rproj+rp) for pp in range(npairs)])
  As=A[idx]; ys=y[idx]; ss=lsqr(As,ys,atol=1e-12,btol=1e-12,iter_lim=10000); ee=rel(ss[0],xt); rr=np.linalg.norm(As@ss[0]-ys)/max(np.linalg.norm(ys),1e-30); phase.append((rp,len(idx),ee,ss[6],rr)); print(' projections_per_pair',rp,'rows',len(idx),'unknown_ratio',len(idx)/unknown,'err',ee,'acond',ss[6],'res',rr)
 # reconstruct Gamma and T/bracket/J/L
 Gr=[B[i]+sum((xr[i*q+a]*H[a] for a in range(q)),start=np.zeros((d,d))) for i in range(d)]
 Gerr=rel(np.stack(Gr),np.stack(Gs)); cr=np.zeros((d,d,d));
 for i in range(d):
  for j in range(d):cr[:,i,j]=Gr[i]@np.eye(d)[j]-Gr[j]@np.eye(d)[i]
 # true projected bracket tensor c from T by raising output with identity: T[k,i,j]
 cerr=rel(cr,T);u=rng.normal(size=d);nu=.137
 def Jof(cc,u):return -np.einsum('i,ikb->kb',u,cc)
 J=Jof(T,u);Jr=Jof(cr,u);jerr=rel(Jr,J);lerr=rel(Jr-nu*C@C,J-nu*C@C)
 print('Gamma',Gerr,'bracket_T',cerr,'J',jerr,'L',lerr)
 # noise ladder reuse same A
 errs=[]
 for eps in [1e-10,1e-8,1e-6,1e-4]:
  z=rng.normal(size=y.shape);yn=y+eps*np.linalg.norm(y)*z/np.linalg.norm(z);ss=lsqr(A,yn,atol=1e-12,btol=1e-12,iter_lim=10000);ee=rel(ss[0],xt);errs.append((eps,ee));print('noise',eps,'err',ee)
 slope=np.polyfit(np.log10([a for a,b in errs]),np.log10([b for a,b in errs]),1)[0];print('noise_slope',slope)
 assert err<2e-8 and Gerr<2e-8 and cerr<2e-8 and jerr<2e-8 and .7<slope<1.3
 print('NOTE: this 28D object is a coordinate stress lab, not a faithful finite Lie algebra; full-physical evidence is provided separately by the exact helical resonant tribunal.')
 print('PASS: only 12 random curvature projections per state pair recover all 1,736 E-hidden connection coefficients and hence the projected formation tensor/operator, with linear noise stability.')
if __name__=='__main__':main()
