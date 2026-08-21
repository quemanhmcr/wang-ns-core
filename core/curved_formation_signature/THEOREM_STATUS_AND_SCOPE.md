# Theorem Status and Scope

This note separates exact identities, inherited theorems, standard differential geometry, executable evidence, and current interpretation.  The distinction matters because the deep campaign exposed several places where a numerically compelling statement was stronger than the theorem actually justified.

## 1. Exact algebraic / differential identities

Within a smooth typed setting where the indicated operators and covariant exterior derivatives are defined:

1. **Koszul reconstruction**
   \[
   (g,T)\Longrightarrow\nabla.
   \]
2. **Formation Riesz law**
   \[
   \mathcal L_{\nu,u}=\mathcal J_u-\nu C^2,
   \qquad
   u_t=\mathcal L_{\nu,u}u.
   \]
3. **Mother / spectral soldering form**
   \[
   \boxed{E=d_\nabla C,\qquad E_u=[\nabla_u,C].}
   \]
4. **Curvature-corrected mother bracket**
   \[
   E_{[u,v]}
   =[\nabla_u,E_v]-[\nabla_v,E_u]-[R(u,v),C].
   \]
5. **Covariant square**
   \[
   \boxed{d_\nabla^2C=[R,C].}
   \]
6. **Second Bianchi identity**
   \[
   \boxed{d_\nabla R=0.}
   \]
7. **Next covariant levels**
   \[
   d_\nabla[R,C]=R\wedge E,
   \qquad
   d_\nabla(R\wedge E)=R\wedge[R,C],
   \]
   with the usual graded conventions.
8. **Curvature functional calculus**
   \[
   [R,f(C)]_{xy}=f^{[1]}(x,y)[R,C]_{xy}
   \]
   whenever the functional calculus is typed.
9. **Shifted-cut curvature layer cake**
   \[
   \frac12\int[R,H_a]\,da=[R,C]
   \]
   in the corresponding spectral layer-cake sense.

These are identities of connection/curvature calculus once the NS formation data and distinguished curl operator are fixed.

## 2. Standard geometry versus NS-specific content

The relations

\[
d_\nabla^2Q=[R,Q],
\qquad
d_\nabla R=0
\]

for endomorphism-valued fields are standard differential geometry.  The third core does **not** claim the invention of a new Bianchi identity.

The NS-specific structural package is instead:

- the canonical formation datum \((\mathfrak g_\sigma,g,T,C)\);
- the physical choice \(C=\operatorname{curl}\);
- the completeness of \(E=d_\nabla C\) as a smooth-state sensor modulo the known Killing/Galilean sector;
- the spectral-flag tomography of \(E\) and the tested curvature action;
- the exact formation/signature metric bridge;
- the curl-spectral reduction of the formation connection and curvature.

This is the level at which novelty comparisons should be made.

## 3. Theorems inherited from the parent cores

The present core relies on, but does not duplicate, theorem statements in:

- [Metric–Lie / Hodge Formation Core](../metric_lie_hodge/README.md), especially the Riesz/Poisson/Dirichlet formation identities;
- [Mother / Spectral-Flag Completeness Theorem](../spectral_signature/MOTHER_COMPLETENESS_THEOREM.md), especially mother completeness modulo Killing symmetry, strain reconstruction, exact Sobolev signature identity, and signature-image conjugacy on the smooth periodic class.

The signature metric identities in this core follow by polarization of the established Sobolev identity at \(s=-1\) and \(s=0\).

## 4. Exact spectral reduction in a typed spectral frame

When curl admits the relevant orthogonal spectral decomposition, split the skew connection into the curl stabilizer and its orthogonal complement:

\[
\nabla=V+B,
\qquad [V,C]=0.
\]

Then

\[
\boxed{E=[B,C].}
\]

Decompose formation curvature as

\[
R=R_\parallel+R_\perp,
\qquad [R_\parallel,C]=0.
\]

The curvature mother satisfies

\[
\boxed{[R,C]=[R_\perp,C].}
\]

In the constant-base block model, the vertical curvature has the Gauss/Ricci form

\[
R_\parallel=[V,V]+\Pi_\parallel[B,B],
\]

while the off-sheet part has the corresponding Codazzi form.  The full physical helical audits independently verified these block identities on periodic divergence-free fields.

The splitting is reductive:

\[
[\mathfrak h_C,\mathfrak h_C]\subset\mathfrak h_C,
\qquad
[\mathfrak h_C,\mathfrak m_C]\subset\mathfrak m_C.
\]

For two spectral blocks it is symmetric-space type, \([\mathfrak m_C,\mathfrak m_C]\subset\mathfrak h_C\); for three or more blocks, off-sheet two-hop mixing may occur.

## 5. Canonical executable evidence

The combined canonical audit suite verifies, among other things:

- blind reconstruction of the formation connection/mother/flag from \((T,C)\) in a physical coordinate lab;
- complete mean-zero state rank and exact Galilean kernel in the selected model;
- independent six-direction microlocal reconstruction of state and formation dynamics;
- trajectory-level commuting diagrams;
- necessity of the transported Riesz metric;
- full-operator-field recovery of the transported formation tensor;
- local physical rigidity of the vector-field bracket and curl direction;
- full physical Jacobi/Bianchi/covariant identities;
- shifted-cut tomography of \([R,C]\);
- mother as tangent velocity on the curl isospectral orbit;
- spectral stabilizer splitting and Gauss–Codazzi–Ricci decomposition;
- full physical helical verification of that decomposition;
- generic recovery of the hidden curl-commuting connection lift from \((E,K)\);
- order-one vertical-curvature contribution to higher Bianchi degrees;
- blind reversible/irreversible parity separation on signature coordinates;
- orientation double-cover behavior under \(C\mapsto-C\);
- topology and boundary negative controls;
- deliberate examples where curvature is nonzero on harmless 2D/Beltrami/shear states;
- the distinction between represented formation curvature and naive embedding curvature.

Exact numerical identities generally lie between \(10^{-15}\) and \(10^{-13}\).  Finite-step holonomy tests have the predicted discretization error instead of roundoff residuals.

## 6. Strongest current canonical interpretation

The strongest supported synthesis is

\[
\boxed{
\textbf{Navier–Stokes formation geometry admits a canonical curl-spectral reduction.}
}
\]

More explicitly:

- formation data generate \(\nabla\), \(R\), \(\mathcal J\), \(C^2\), and the NS flow;
- curl decomposes the connection into within-sheet and cross-sheet parts;
- the complete mother \(E=d_\nabla C\) is the canonical degree-one state soldering into a distinguished distribution of the curl isospectral orbit;
- formation curvature decomposes into within-sheet Gauss/Ricci and cross-sheet Codazzi sectors;
- \([R,C]\) is the curvature mother for the first curl functional calculus of the cross-sheet sector;
- higher Bianchi degrees can couple curl-commuting curvature back to visible sensors;
- the full signature-side operator field carries the transported formation dynamics autonomously;
- the signature image itself need not be a curved embedding.

This is stronger and more precise than the earlier slogan “the two cores are compatible”, while being narrower than an unrestricted equivalence of all abstract metric-Lie cores.

## 7. Explicit nonclaims and corrections

The canonical core does **not** claim:

1. that the standard identities \(d_\nabla^2=[R,\cdot]\) or \(d_\nabla R=0\) are novel;
2. that the signature image is intrinsically or extrinsically curved merely because it carries a curved formation connection;
3. that \([R,C]\), \(E\), or any tested higher covariant level is a blow-up indicator;
4. that the entire curl commutant is a final physical gauge;
5. that \(\ker C\) may be blindly quotiented on topologically nontrivial domains;
6. that \([\nabla,C]\) is the only possible complete state sensor;
7. that Euler–heat BCH descendants are identical to formation curl curvature;
8. that arbitrary Galerkin truncation preserves Jacobi, Bianchi, or continuum mother completeness;
9. that the periodic reverse compiler applies unchanged to arbitrary boundary conditions;
10. that every higher covariant degree necessarily adds independent connection information.

These corrections are part of the theory, not disclaimers added after the fact.

## 8. Open scope

The following remain open:

1. a fully typed infinite-dimensional theorem for the curl-spectral reduction on an optimal Sobolev/Fréchet scale;
2. a publish-grade boundary/manifold version using the correct Hodge/Stokes realization and harmonic cohomology;
3. a canonical definition of the final dark/stabilizer quotient generated by the whole covariant sensor algebra;
4. a theorem characterizing when \((E,K)\) globally determines the compatible formation connection rather than only generically in finite spectral models;
5. an optimal formulation of the higher-degree observability filtration;
6. a comparison theorem with established geometric hydrodynamics, adjoint-orbit, gauge/Higgs, Cartan-reduction and Hodge formulations;
7. any regularity theorem linking this structural geometry to a priori control of 3D NS.

The core is therefore a **canonical structural synthesis with exact identities, inherited completeness theorems, and strong adversarial evidence**.  It is not a completed solution of the Navier–Stokes regularity problem.
