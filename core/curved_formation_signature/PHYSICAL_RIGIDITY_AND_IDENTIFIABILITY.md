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
