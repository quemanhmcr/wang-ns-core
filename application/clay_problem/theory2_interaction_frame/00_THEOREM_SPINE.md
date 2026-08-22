# 00 — Theorem spine: complete state to moving heat geometry

## Status

**EXACT through Sections 1--6; OPEN only where explicitly labelled.** Work first on the smooth mean-zero divergence-free torus, with the Schwartz whole-space extension inherited from the Mother Completeness theorem.

## 1. Start from the complete Theory-2 state

Let

\[
C=\operatorname{curl},\qquad \Gamma_u=\nabla_u,
\qquad E_u=[\Gamma_u,C],
\]

and

\[
H_a=\operatorname{sgn}(C-aI),\qquad
A_a(u)=[\Gamma_u,H_a].
\]

The shifted signature satisfies the exact reverse compiler

\[
A_a(u)=H_a\operatorname{skew}\mathscr O_a(u),
\]

and layer cake gives

\[
\boxed{
E_u=\frac12\int_{\mathbb R}A_a(u)\,da.
}
\tag{1.1}
\]

Mother Completeness reconstructs strain from the principal symbol

\[
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(u)\xi}{|\xi|^2}\,\xi\times b,
\]

then reconstructs velocity by

\[
\Delta u=2\operatorname{div}S(u).
\]

Hence, on the normalized physical state class,

\[
\boxed{
\{\mathscr O_a(u)\}_a\longleftrightarrow E_u\longleftrightarrow u.
}
\tag{1.2}
\]

This equivalence is the spine. Every later contraction is subordinate to it.

## 2. Anchored material interaction frame — EXACT

The projected NS equation is

\[
 u_t+\Gamma_u u=-\nu C^2u,
 \qquad \Gamma_u^*=-\Gamma_u
\tag{2.1}
\]

on \(L^2_\sigma\). Fix \(t_0\) and solve

\[
\boxed{
U_t=-\Gamma_uU,\qquad U(t_0)=I.
}
\tag{2.2}
\]

Then \(U\) is unitary. Define

\[
 v=U^*u,
 \qquad
 C^\sharp=U^*CU,
 \qquad
 H_a^\sharp=U^*H_aU.
\tag{2.3}
\]

Direct differentiation gives

\[
\boxed{v_t=-\nu(C^\sharp)^2v,}
\tag{2.4}
\]

\[
\boxed{C^\sharp_t=U^*E_uU,}
\tag{2.5}
\]

and

\[
\boxed{(H_a^\sharp)_t=U^*A_a(u)U.}
\tag{2.6}
\]

Thus Euler has not disappeared physically. It has moved from the state equation into the isospectral motion of the curl/heat geometry.

If

\[
K=U^*\Gamma_uU,
\]

then equivalently

\[
C^\sharp_t=[K,C^\sharp],
\qquad
(H_a^\sharp)_t=[K,H_a^\sharp].
\tag{2.7}
\]

The spectrum of \(C^\sharp\) is fixed; only its eigenspaces move.

## 3. Critical metric law — EXACT

Let

\[
\Lambda^\sharp=|C^\sharp|.
\]

Because functional calculus is transported by the unitary frame,

\[
(\Lambda^\sharp)_t=[K,\Lambda^\sharp].
\]

Therefore

\[
\boxed{
\frac d{dt}\langle v,\Lambda^\sharp v\rangle
=
\langle v,[K,\Lambda^\sharp]v\rangle
-2\nu\langle v,(\Lambda^\sharp)^3v\rangle.
}
\tag{3.1}
\]

The second term is true critical heat dissipation. Hence every positive critical growth is exactly motion of the complete heat geometry against that dissipation.

## 4. Spectral-probability law — EXACT

Let

\[
M=\|v\|_2^2,
\qquad
 d\mu_t(\lambda)
 =\frac{d\langle v,1_{d\lambda}(C^\sharp)v\rangle}{M}.
\]

For every suitable real \(f\),

\[
\boxed{
\frac d{dt}\mathbb E_{\mu_t}f
=
\frac{\langle v,[K,f(C^\sharp)]v\rangle}{M}
-2\nu\operatorname{Cov}_{\mu_t}(f(\lambda),\lambda^2).
}
\tag{4.1}
\]

With \(\kappa=\lambda^2\) and \(\bar\kappa=\mathbb E_\mu\kappa\),

\[
\boxed{
\dot{\bar\kappa}
+2\nu\operatorname{Var}_\mu(\kappa)
=
\frac{\langle v,[K,(C^\sharp)^2]v\rangle}{M}.
}
\tag{4.2}
\]

This is the native moving-heat form of the old heat-normal identities. No source-ray or traffic ontology is needed.

## 5. Genuine physical owner — EXACT

Mother Sobolev isometry gives, after the universal normalization,

\[
\|E_u\|_{\mathfrak M_0}^2=\|u\|_{\dot H^1}^2.
\tag{5.1}
\]

The kinetic energy law therefore owns

\[
\boxed{
2\nu\int_0^T\|E_u(t)\|_{\mathfrak M_0}^2dt
\le \|u(t_0)\|_2^2.
}
\tag{5.2}
\]

This is a real finite quadratic action of the complete heat-geometry velocity. It is, however, subcritical for an infinite parabolic cascade: a critical packet at frequency \(K\) has \(\dot H^1\)-cost \(\sim K\), hence only \(\sim K^{-1}\) cost over one heat time \(K^{-2}\).

## 6. Exact half-derivative geometry

For a spectrally represented operator \(T\), the shifted-flag layer cake gives

\[
\boxed{
\frac14\int_{\mathbb R}\|[T,H_a]\|_{\rm edge}^2da
=
\sum_{x,y}|x-y||T_{xy}|^2
=
\big\||\operatorname{ad}_C|^{1/2}T\big\|_{\rm edge}^2.
}
\tag{6.1}
\]

The complete moving flag therefore contains exactly the historical missing half spectral derivative **before contraction**.

**Typing warning.** The edge norm in (6.1) is not automatically the same continuum norm as the viscously owned microlocal Mother norm in (5.2). Bridging them with the true 3D physical section is an analytic theorem, not a notation change.

## 7. Canonical analytic question — OPEN

The theorem-first problem is now:

\[
\boxed{
\text{Can true 3D heat plus complete flag motion force a uniform critical
one-step contraction, or else compactify into an exact harmless Mother kernel?}
}
\tag{7.1}
\]

This is a critical monodromy / compactness-rigidity problem on complete information. It is not a search for another observer.
