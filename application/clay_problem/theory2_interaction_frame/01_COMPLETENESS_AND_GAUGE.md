# 01 — Completeness preservation and gauge discipline

## Status

**EXACT structural statement + mandatory anti-loop warning.**

## 1. What Theory 2 already proves

On the normalized smooth physical state class,

\[
\Sigma(u)=\{\mathscr O_a(u)\}_a
\longleftrightarrow
E_u
\longleftrightarrow
u.
\tag{1.1}
\]

Consequently no two distinct physical states have the same complete signature. Every native state functional is therefore determined by \(\Sigma\).

This removes the historical pathology in which scalar stock/work traffic identified distinct states whose next NS jets differed.

## 2. The anchored interaction frame is information preserving

Given a true smooth trajectory \(u(t)\), the initial-value problem

\[
U_t=-\Gamma_uU,\qquad U(t_0)=I
\tag{2.1}
\]

has a unique unitary frame. Since

\[
v=U^*u,
\]

we recover

\[
\boxed{u=Uv.}
\tag{2.2}
\]

Thus the anchored trajectory-level transform

\[
 u(\cdot)
 \mapsto
 (U(\cdot),v(\cdot),C^\sharp(\cdot))
\tag{2.3}
\]

loses no state information.

A closed equivalent system may be written in \((U,v)\):

\[
\boxed{
\begin{cases}
U_t=-\Gamma_{Uv}U,\\
v_t=-\nu(U^*CU)^2v,
\end{cases}
\qquad U(t_0)=I.
}
\tag{2.4}
\]

The physical state is always \(u=Uv\). The interaction frame is therefore a coordinate choice, not a quotient.

## 3. Why \((v,C^\sharp)\) alone must not be called complete

The identity

\[
C^\sharp=U^*CU
\]

does not determine \(U\) uniquely. If \(D\) is unitary and

\[
[D,C]=0,
\]

then \(U\) and \(DU\) produce the same conjugated curl after the corresponding ambient state rotation. This is the curl-commutant / vertical gauge already identified by the Mother theorem.

Therefore

\[
\boxed{
(v,C^\sharp)\text{ is an exact pathwise renderer, but its standalone
completeness requires an additional gauge-reconstruction theorem.}
}
\tag{3.1}
\]

No such theorem is silently assumed here.

## 4. Safe ontology

The application keeps

\[
\boxed{
\text{physical state: }u\leftrightarrow E_u\leftrightarrow\Sigma(u)
}
\]

and uses

\[
\boxed{
\text{interaction frame: }U,v,C^\sharp,H_a^\sharp
}
\]

only to expose heat geometry.

If a scalar reader becomes blind, the proof returns to \(u/E/\Sigma\). It does not differentiate the reader to invent a replacement state.

## 5. What “Theory-2 preserving” means

A blow-up argument in this directory is Theory-2 preserving iff:

1. the master state remains injective on the physical image;
2. every frame transformation is anchored/invertible or its gauge is explicitly retained;
3. every contraction is labelled as information losing;
4. no dynamical conclusion is inferred from a reader kernel as though it were a physical-state kernel;
5. compactness loss under translation/dilation is treated as genuine critical noncompactness, not as observer blindness.

This is the structural safeguard against recreating the old information-reconstruction loop.
