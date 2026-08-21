# Formula Chain: Core to the Blow-up Rigidity Target

This file is a compact dependency chain.  Every arrow is either an exact construction/identity in the smooth typed setting or is explicitly marked as an open implication.

## A. Formation core

\[
\boxed{
\mathcal C_{NS}
=(\mathfrak g_\sigma,[\cdot,\cdot],\langle\cdot,\cdot\rangle_{L^2},C)
}
\]

\[
\boxed{T(a,b,c)=\langle a,[b,c]\rangle}
\]

\[
\boxed{
\langle a,\mathcal J_ub\rangle=-\langle u,[a,b]\rangle
}
\]

\[
\boxed{
B(u,u)=\mathcal J_uu
}
\]

\[
\boxed{
\ell_{\nu,u}(a,b)
=-\langle u,[a,b]\rangle-\nu\langle Ca,Cb\rangle
}
\]

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2
}
\]

\[
\boxed{
u_t=\mathcal L_{\nu,u}u=B(u,u)-\nu C^2u}
\]

## B. Critical core identity

\[
\boxed{\Lambda=|C|}
\]

\[
\boxed{K(u)=\|\Lambda^{1/2}u\|_2^2}
\]

\[
\boxed{
W_c(u)=\langle\Lambda u,B(u,u)\rangle
}
\]

\[
\boxed{
\frac12K'
=W_c(u)-\nu\|\Lambda^{3/2}u\|_2^2
}
\]

\[
\boxed{
W_c(u)=\frac12\langle u,[\Lambda,\mathcal J_u]u\rangle
}
\]

\[
\boxed{
\mathscr R_u
=\frac12\Lambda^{-3/2}[\Lambda,\mathcal J_u]\Lambda^{-3/2}
}
\]

\[
\boxed{
\frac12K'
=\langle\Lambda^{3/2}u,(\mathscr R_u-\nu I)\Lambda^{3/2}u\rangle
}
\]

## C. Helicity/curl constraint

\[
\boxed{\mathcal J_u(Cu)=0}
\]

\[
\boxed{C=H\Lambda,\qquad P_\pm=(I\pm H)/2}
\]

\[
\boxed{A_u=P_+\mathcal J_uP_-}
\]

\[
\boxed{
W_c(u)
=2\operatorname{Re}\langle u_+,[\Lambda,A_u]u_-\rangle
}
\]

Therefore

\[
\boxed{
\text{critical production}
=\text{helicity-sign mixing}\times\text{radial noncommutation}.
}
\]

## D. One spectral stress, not many mechanisms

\[
\boxed{
\mathcal T_u(q)=\langle q(C)u,B(u,u)\rangle
}
\]

\[
\boxed{\mathcal T_u(1)=\mathcal T_u(x)=0}
\]

\[
\boxed{
\Sigma_u(r)=\mathcal T_u((x-r)_+)
}
\]

\[
\boxed{
\mathcal T_u(q)=\int q''(r)\Sigma_u(r)\,dr
}
\]

\[
\boxed{W_c(u)=2\Sigma_u(0)}
\]

with

\[
\boxed{
\int q(x)\,d\mu_u(x)=\frac12\langle u,q(C)u\rangle
}
\]

and

\[
\boxed{
\partial_t\mu=\partial_x^2\Sigma-2\nu x^2\mu.
}
\]

For

\[
X_R=\int(|x|-R)_+\,d\mu,
\]

\[
\boxed{
\dot X_R+2\nu R^2X_R
\le\Sigma_u(R)+\Sigma_u(-R).
}
\]

Interpretation:

\[
\boxed{
\text{a singular trajectory must regenerate critical mass at unbounded scales on parabolic time scales.}
}
\]

## E. Full-state normalization on \(\mathbb R^3\) / a rescaled blow-up chart

\[
\boxed{E(u)=\|u\|_2^2}
\]

\[
\boxed{
A=\sqrt{K(u)},
\qquad
\rho=\frac{K(u)}{E(u)}
}
\]

\[
\boxed{
u=A S_\rho v,\qquad S_\rho f(x)=\rho f(\rho x)}
\]

\[
\boxed{
\|v\|_2^2=1,
\qquad
\|\Lambda^{1/2}v\|_2^2=1
}
\]

\[
\boxed{
\frac{d\tau}{dt}=A\rho^2
}
\]

\[
\boxed{
 v_\tau
 =B(v,v)-\frac\nu A C^2v-\alpha v-\beta Gv
}
\]

\[
\boxed{
\alpha=W-\frac\nu A M_3,
\qquad
\beta=2W-\frac{2\nu}{A}(M_3-M_2)
}
\]

where

\[
W=\langle\Lambda v,B(v,v)\rangle,
\quad
M_2=\|\Lambda v\|_2^2,
\quad
M_3=\|\Lambda^{3/2}v\|_2^2.
\]

## F. Candidate blow-up limit

If

\[
A\to\infty,
\]

then

\[
\frac\nu A\to0.
\]

The normalized candidate limit is

\[
\boxed{
 v_\tau
 =B(v,v)-2W(v)\left(x\cdot\nabla+\frac32\right)v.
}
\]

The removed variables satisfy

\[
\boxed{(\log A)_\tau=W(v)}
\]

\[
\boxed{(\log\rho)_\tau=2W(v)}
\]

and therefore

\[
\boxed{
\text{critical amplification}
\Longrightarrow
\int W(v(\tau))\,d\tau\to+\infty.
}
\]

## G. Helicity restriction on the normalized enemy

\[
\boxed{h(v)=\langle v,Cv\rangle}
\]

\[
\boxed{h_\tau=-2W(v)h}
\]

Thus a recurrent amplifying orbit must obey

\[
\boxed{h\equiv0.}
\]

A fixed point satisfies

\[
\boxed{
B(v,v)
=b\left(x\cdot\nabla+\frac32\right)v,
\qquad b=2W(v)>0,
}
\]

and necessarily

\[
\boxed{\langle v,Cv\rangle=0.}
\]

## H. Finite closure is harmless

For every fixed finite-dimensional \((T,C)\)-closed Galerkin subsystem,

\[
\boxed{
\frac12\frac d{dt}\|u_N\|_2^2=-\nu\|Cu_N\|_2^2
}
\]

and the bounded polynomial ODE is global.

Therefore

\[
\boxed{
\text{a singular orbit must escape every fixed finite core closure.}
}
\]

## I. Final open implication

The remaining theorem is not a pressure estimate, a local alignment criterion, or a pointwise spectral bound.

It is:

\[
\boxed{
\begin{array}{c}
\text{complete normalized full-core orbit}\\
+\;\text{genuine 3D infinite closure}\\
+\;\|v\|_2=\|\Lambda^{1/2}v\|_2=1\\
+\;\langle v,Cv\rangle=0
\end{array}
\quad\Longrightarrow\quad
\sup_T\int_0^T W(v(\tau))\,d\tau<\infty.
}
\]

This arrow is **open**.  Proving it would close the application reduction; the documents in this folder do not claim that it is currently proved.
