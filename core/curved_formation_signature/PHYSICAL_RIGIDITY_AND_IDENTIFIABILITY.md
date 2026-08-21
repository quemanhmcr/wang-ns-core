# Physical Rigidity and Identifiability

## 1. What the full signature-side operator field determines

Let \(z\) be complete mother or shifted-flag coordinates, with transported kinetic metric \(G_\Sigma\), transported curl \(C_\Sigma\), and full state-dependent formation operator

\[
\mathcal L_\Sigma(z)
=\mathcal J_\Sigma(z)-\nu C_\Sigma^2.
\]

The covariant Poisson matrix is linear in state:

\[
\boxed{
G_\Sigma\mathcal J_\Sigma(z)
=-\sum_i z_i(T_\Sigma)_i.
}
\]

Therefore the **full operator field** over enough independent states is a linear inverse problem for the transported metric-Lie tensor \(T_\Sigma\).

In the 28-dimensional tribunal, \(d+5\) generic states reconstructed \(T_\Sigma\) with residuals

\[
2.21\times10^{-15}\quad\text{(mother)},
\qquad
2.26\times10^{-15}\quad\text{(flag)}.
\]

Using only \(d-1\) independent states left exactly one null state direction.  From the recovered \((G_\Sigma,T_\Sigma)\), the Levi–Civita connection and curvature were rebuilt and matched the transported formation curvature at \(3.22\times10^{-15}\) and \(3.69\times10^{-15}\).

Thus the full signature-side **operator field**, not a single snapshot, identifies the transported formation geometry in the tested model.

## 2. Exact dark-sector collision: snapshot and diagonal dynamics are insufficient abstractly

A stronger statement is false in an arbitrary abstract metric-Lie category.

Take

\[
C=\operatorname{diag}(1,1,1,2,2,2).
\]

Core A is abelian.  Core B carries the standard \(so(3)\) metric Lie bracket on the first three-dimensional curl eigenspace and is abelian on the second.

Because curl is scalar on the nonabelian block,

\[
[\nabla_u,C]=0
\]

for internal motions.  Because the metric is bi-invariant, the Euler self-spray vanishes:

\[
\mathcal J_u u=0.
\]

Hence the two distinct cores have, for every state,

\[
\boxed{
\text{same mother}=0,
\qquad
\text{same shifted flag}=0,
\qquad
\text{same diagonal flow}=-\nu C^2u.
}
\]

Yet

\[
\|T_B-T_A\|=2.449,
\]

and their generic full Poisson operators differ by order one, with measured maximum about \(3.98\).

A separate totally antisymmetric metric three-form construction leaves the Euler diagonal spray unchanged for every state while changing the full Poisson operator by about \(5.01\).

Therefore

\[
\boxed{
\text{signature snapshot + diagonal PDE trajectory}
\not\Rightarrow
\text{arbitrary abstract background core}.
}
\]

This negative result is part of the canonical theory, not an exception to be hidden.

## 3. Why the physical NS category removes the ambiguity

The dark-sector collision uses abstract metric-Lie structures that are not local Euclidean vector-field brackets.

Consider the general constant-coefficient isotropic first-order antisymmetric bilinear law.  Imposing the scalar derivation law

\[
[a,fb]=f[a,b]+a(f)b
\]

on random jets produces a full-rank affine system whose unique normalized solution is

\[
\boxed{
[a,b]=(a\cdot\nabla)b-(b\cdot\nabla)a.
}
\]

The coefficient error in the tribunal was \(5.32\times10^{-16}\); a representative fake isotropic law had normalized derivation defect \(1.44\).

Independently, the space of first-order \(SO(3)\)-equivariant rank-three tensors is one-dimensional in the tested classification, aligned with the Levi-Civita tensor \(\varepsilon_{ijk}\) at residual \(4.07\times10^{-17}\).  This selects curl up to scale and orientation.

Thus in the local oriented Euclidean fluid category, the bracket and curl are not arbitrary hidden parameters.  Locality/derivation and equivariance rigidify the background formation core.

## 4. Galerkin projection is not a faithful category change

A separate negative control changed the retained Fourier mode family and measured completeness of the projected mother \(P_V[\nabla_u,C]P_V\), the projected shifted flag, and the six-direction microlocal strain signature.

\[
\begin{array}{c|c|c|c}
\text{state dimension}&
\operatorname{rank}(P_VEP_V)&
\operatorname{rank}(\text{projected flag})&
\operatorname{rank}(q_{6\rm dir})\\
\hline
12&12&12&12\\
24&18&24&24\\
28&28&28&28\\
40&28&28&40
\end{array}
\]

The physical microlocal signature remained complete, with condition numbers between \(1\) and \(2.83\), while arbitrary operator projection lost state directions.

The same projected brackets had Jacobi defects approximately

\[
0.43,\quad0.64,\quad0.41
\]

on representative 24D, 28D and 40D truncations.  Therefore an arbitrary Galerkin truncation can destroy both the probe geometry and the base Lie geometry.

Deep curvature/Bianchi claims in this core are consequently checked again on full pseudospectral divergence-free fields rather than inferred from a projected Galerkin algebra.

## 5. Correct identifiability statement

The supported statement is

\[
\boxed{
\text{On the canonical physical NS core, complete signature data provide a faithful curved state/dynamics representation.}
}
\]

The unsupported and falsified statement is

\[
\boxed{
\text{A signature snapshot uniquely determines every possible abstract metric-Lie core.}
}
\]

Keeping this distinction explicit is essential to the theory.

---

## 6. From first-order stabilizer to stratified geometric identifiability

At degree one, the mother forgets connection components that commute with curl:

\[
E=[\nabla,C]=[B,C]
\]

for the spectral splitting \(\nabla=V+B\) with \([V,C]=0\).  This makes \(V\) invisible to the mother and identifies \(\operatorname{comm}(C)\) as a **first-order stabilizer**.

The newest inverse campaign shows what happens next.  Once \(B\) is reconstructed from \(E\), the curvature mother has the exact finite metric-Lie form

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V),
}
\]

with \(\mathcal A_{C,E}\) linear in the hidden stabilizer connection.  When this Codazzi observability map is injective, \((g,C,E,K)\) reconstructs the complete formation connection and hence the bracket, curvature and Poisson geometry.

This is generic in the tested finite campaign, but not universal.  A rank phase diagram over 9 Lie-algebra families, 9 curl multiplicity patterns and 6 randomized metrics found full rank for every tested seed in 68 of 72 non-scalar family/pattern combinations.  All persistent failures were concentrated at the highly degenerate pattern \(5+1\).

Higher covariant degrees reduce several such kernels.  In the hardest tested example the linearized nullity decreases

\[
11\to9\to6,
\]

and the maximal tower plus Jacobi/Bianchi leaves a five-dimensional first-order kernel.  Nonlinear probing shows that this remaining kernel is quadratically visible rather than demonstrably dark.

Thus the safe identifiability hierarchy is

\[
\boxed{
\operatorname{comm}(C)
=\text{first-order stabilizer},
}
\]

followed by a stratified differential-spectral inverse problem.  A true physical gauge must remain invisible to the full nonlinear differential geometry, not merely to \(E\) or to the Jacobian of a finite sensor tower.

For the complete reconstruction statement and negative controls, see [GEOMETRIC_COMPLETENESS.md](GEOMETRIC_COMPLETENESS.md).

## 7. Zero curl is not a gauge criterion

The periodic Galilean kernel can tempt one to identify \(\ker C\) with gauge.  That is false on more general topological sectors.

For the annular harmonic circulation

\[
h=
\left(
-\frac{y}{x^2+y^2},
\frac{x}{x^2+y^2},
0
\right),
\]

one has \(Ch=0\), yet a divergence-free probe can satisfy \([D_h,C]w\neq0\).  An independent algebraic control likewise produced two zero-curl directions, one mother-visible and one truly central/mother-dark.

Hence

\[
\boxed{
\ker C
\neq
\ker(u\mapsto E_u)
}
\]

in general.  Harmonic circulation belongs to physical topology/cohomology and must not be silently quotiented with Galilean constants.

## 8. Boundary/domain identifiability is typed

The periodic reverse compiler uses the correct \(L^2\)-adjoint and spectral realization of curl.  A non-self-adjoint raw curl analog in a fixed physical metric breaks the adjoint-parity reverse formulas by order one, while the positive Stokes/Dirichlet form remains well-defined.

Therefore bounded-domain extension requires the typed Hodge/Stokes data of the formation core: operator/form domains, boundary trace pairing, harmonic sector and the selected self-adjoint or otherwise correctly typed realization.  Identifiability statements from the periodic operator model are not automatically boundary theorems.
