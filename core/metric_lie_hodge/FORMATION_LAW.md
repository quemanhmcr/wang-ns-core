# Formation Law

## 1. Core datum

Let

\[
\mathfrak g_\sigma
=
\{u:\nabla\cdot u=0\}
\]

on a smooth periodic/closed Euclidean setting, with vector-field Lie bracket

\[
[a,b]=(a\cdot\nabla)b-(b\cdot\nabla)a,
\]

\(L^2\) metric \(\langle\cdot,\cdot\rangle\), and oriented curl operator

\[
C=\operatorname{curl}.
\]

The metric Lie tensor is

\[
\boxed{T(a,b,c)=\langle a,[b,c]\rangle.}
\]

All formulas below are intrinsic on the divergence-free state space; ambient formulas involving the Leray projector \(P\) are renderings of the same Riesz constructions.

## 2. Levi–Civita and Poisson faces of the same metric Lie tensor

The \(L^2\) Levi–Civita connection is recovered from the Koszul formula

\[
\boxed{
2\langle\nabla_ab,c\rangle
=
\langle[a,b],c\rangle
-\langle[b,c],a\rangle
+\langle[c,a],b\rangle.
}
\]

For divergence-free vector fields this is

\[
\boxed{\nabla_ab=P((a\cdot\nabla)b).}
\]

The Lie–Poisson operator at state \(u\) is the Riesz representative of

\[
\boxed{
\langle a,\mathcal J_ub\rangle
=-\langle u,[a,b]\rangle.
}
\]

In vector calculus coordinates,

\[
\boxed{\mathcal J_ub=P(b\times\omega),\qquad\omega=Cu.}
\]

The Euler vector field has the equivalent geodesic and Hamiltonian forms

\[
\boxed{
N(u)=\mathcal J_uu=-\nabla_uu=-P((u\cdot\nabla)u).
}
\]

Thus \(\nabla\) and \(\mathcal J\) are not independent primitives: both are Riesz/slot constructions from \(T\) and the metric.

## 3. Metric non-invariance tensor and Euler formation

Define

\[
\boxed{
\mathfrak D(a;b,c)
=
\langle[a,b],c\rangle
+
\langle b,[a,c]\rangle.
}
\]

It measures failure of the \(L^2\) metric to be invariant under the adjoint action.  For smooth incompressible fields,

\[
\boxed{
\mathfrak D(a;b,c)
=-2\int b\cdot S(a)c\,dx,
}
\]

where

\[
S(a)=\frac12(\nabla a+\nabla a^T).
\]

Let \(\mathfrak D^\sharp\) denote the Riesz lift in the first slot.  The symmetric Euler bilinear product is

\[
\boxed{
B(b,c)=-\frac12\mathfrak D^\sharp(b,c)
=-\frac12P\bigl((b\cdot\nabla)c+(c\cdot\nabla)b\bigr),
}
\]

so

\[
\boxed{B(u,u)=N(u).}
\]

The vortex-stretching/Betchov source is another contraction of the same tensor:

\[
\boxed{
Q(u)
=\int\omega\cdot S(u)\omega\,dx
=-\frac12\mathfrak D(u;\omega,\omega).
}
\]

More generally, for any typed spectral reader \(q(C)\),

\[
\boxed{
2\langle q(C)u,N(u)\rangle
=-\mathfrak D(q(C)u;u,u).
}
\]

## 4. Curl as distinguished Killing endomorphism

The curl operator is self-adjoint on the periodic/closed realization and obeys the polarized Euler Killing identity

\[
\boxed{
\langle Ca,B(b,c)\rangle
+
\langle Cb,B(c,a)\rangle
+
\langle Cc,B(a,b)\rangle
=0.
}
\]

In particular,

\[
\boxed{
\mathfrak D(Cu;u,u)=0,
}
\]

which is the Euler helicity conservation law in formation-tensor form.

The kinetic Hamiltonian

\[
H(u)=\frac12\|u\|_2^2
\]

therefore generates Euler through the Lie–Poisson bracket

\[
\{F,G\}(u)=-\langle u,[\delta F,\delta G]\rangle,
\]

while helicity is a Casimir because

\[
\mathcal J_u(Cu)=0.
\]

## 5. Curl–Dirichlet metric and the full formation pencil

The symmetric positive form

\[
\boxed{G_C(a,b)=\langle Ca,Cb\rangle}
\]

has Riesz operator \(C^2\).  On the periodic divergence-free block,

\[
C^2=(-\Delta).
\]

Define the state-dependent non-symmetric formation form

\[
\boxed{
\ell_{\nu,u}(a,b)
=-\langle u,[a,b]\rangle
-\nu\langle Ca,Cb\rangle.
}
\]

Its Riesz operator is

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2.
}
\]

Taking the diagonal gives the Navier–Stokes vector field:

\[
\boxed{
\partial_tu
=
\mathcal L_{\nu,u}u
=
P(u\times\omega)-\nu C^2u.
}
\]

Equivalently,

\[
\boxed{
\dot F
=
\{F,H\}
-\nu(F,H)_C,
\qquad
(F,G)_C=\langle C\delta F,C\delta G\rangle.
}
\]

Thus the same kinetic Hamiltonian is read through an antisymmetric metric-Lie bracket and a symmetric curl-Dirichlet bracket.

## 6. Pressure is the ambient Hodge completion

The intrinsic equation lives on \(\mathfrak g_\sigma\).  Re-embedding it in ambient vector fields introduces the Hodge-normal reaction traditionally written as pressure.

At the local quadratic level,

\[
\boxed{
-\Delta p
=\operatorname{tr}(\nabla u)^2
=|\nabla u|^2-|\omega|^2.
}
\]

Globally on the periodic/decaying class,

\[
\boxed{
\int|\nabla u|^2=\int|\omega|^2,
\qquad
\int\Delta p=0.
}
\]

The common nonlinear production of these equal global masses is

\[
\boxed{
\langle C^2u,N\rangle
=\langle\omega,CN\rangle
=\langle\omega,S\omega\rangle.
}
\]

Hence pressure records local Hodge mismatch, while vortex stretching records common-mode nonlinear production; they are not independent forces in the intrinsic formation law.
