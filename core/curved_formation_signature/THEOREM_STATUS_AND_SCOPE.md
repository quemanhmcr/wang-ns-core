# Theorem Status and Scope

This note separates exact identities and inherited theorems from executable evidence and open structural conjecture.

## 1. Exact algebraic / differential identities

Within the smooth typed setting where the indicated operators are defined:

1. **Koszul reconstruction** of the Levi–Civita connection from the metric and Lie tensor:
   \[
   (g,T)\Longrightarrow\nabla.
   \]
2. **Formation Riesz law**:
   \[
   \mathcal L_{\nu,u}=\mathcal J_u-\nu C^2,
   \qquad
   u_t=\mathcal L_{\nu,u}u.
   \]
3. **Mother definition**:
   \[
   E=d_\nabla C,
   \qquad E_u=[\nabla_u,C].
   \]
4. **Curvature-corrected mother bracket**:
   \[
   E_{[u,v]}
   =[\nabla_u,E_v]-[\nabla_v,E_u]-[R(u,v),C].
   \]
5. **Covariant square relation**:
   \[
   d_\nabla^2C=[R,C].
   \]
6. **Bianchi identity**:
   \[
   d_\nabla R=0.
   \]
7. **Spectral layer-cake commutation with curvature** whenever the layer-cake representation is typed:
   \[
   \frac12\int[R,H_a]\,da=[R,C].
   \]

These are structural identities, not numerical discoveries.

## 2. Theorems inherited from the canonical parent cores

The present core relies on, but does not duplicate, the theorem statements in:

- [Metric–Lie / Hodge Formation Core](../metric_lie_hodge/README.md), especially the Riesz/Poisson/Dirichlet formation identities;
- [Mother / Spectral-Flag Completeness Theorem](../spectral_signature/MOTHER_COMPLETENESS_THEOREM.md), especially mother completeness modulo Killing symmetry, strain reconstruction, exact Sobolev signature identity, and signature-image conjugacy on the smooth periodic class.

The exact signature metric bridge in this core is obtained by polarizing that established Sobolev identity at \(s=-1\) and \(s=0\).

## 3. Canonical executable evidence added by this core

The canonical audits verify, among other things:

- blind reconstruction of the formation connection/mother/flag from \((T,C)\) on a physical Galerkin test space;
- complete mean-zero rank and exact three-dimensional Galilean kernel in the selected model;
- reconstruction of the full state-dependent formation operator from mother/flag coordinates;
- independent six-direction microlocal reconstruction of state and formation dynamics;
- trajectory-level commuting diagrams;
- exact necessity of the induced Riesz metric;
- full-operator-field recovery of the transported formation tensor;
- exact abstract dark-sector non-identifiability of snapshot/diagonal data;
- local derivation/isotropy rigidity of the physical bracket and curl direction;
- full physical Jacobi, Bianchi and curved-covariant identities on low-frequency pseudospectral states;
- full physical shifted-cut tomography of \([R,C]\);
- deliberate Galerkin completeness/Jacobi failures as negative controls.

Residuals for exact numerical identities are generally between \(10^{-15}\) and \(10^{-13}\), except the finite-step holonomy convergence tests whose error scales with the loop size as predicted.

## 4. Strongest current canonical interpretation

The evidence supports the following structural synthesis:

\[
\boxed{
\text{the spectral-signature theory is a complete curved representation theory of the canonical physical formation core.}
}
\]

More concretely:

- the formation core generates \(\nabla\), \(\mathcal J\), \(C^2\), and the NS flow;
- the mother \(E=d_\nabla C\) is a complete state representation modulo the known Killing sector on the smooth periodic class;
- the full shifted spectral flag is the spectral normal form/tomography of the mother;
- the formation metric, curl, bracket and curvature transport to the signature image;
- the induced bracket is curved/covariant rather than the naive operator commutator;
- the first curvature level is \([R,C]\), measurable as curl holonomy and tomographed by the shifted spectral cuts.

## 5. Open scope

The following are **not** claimed as completed theorems here:

1. a fully typed infinite-dimensional curved-module theorem on an optimal Sobolev or Fréchet scale, with every unbounded composition/domain closed explicitly;
2. the corresponding boundary/manifold theorem when curl is represented by a Hodge/Stokes form complex rather than a self-adjoint velocity endomorphism;
3. a final cohomology/quotient definition of the obstruction tower;
4. a theorem that nontrivial \([R,C]\), or any finite level of the curved tower, characterizes blow-up;
5. global regularity or exclusion of finite-time singularity;
6. novelty relative to all existing geometric hydrodynamics, metriplectic, gauge/connection, or Hodge-theoretic formulations.

The core should therefore be read as a **canonical structural synthesis with exact identities and unusually strong adversarial evidence**, not as a completed solution of the Navier–Stokes regularity problem.
