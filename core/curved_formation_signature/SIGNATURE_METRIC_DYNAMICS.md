# Signature Metric and Dynamics

## 1. Why the naive metric fails

Mother and shifted-flag coordinates are complete state coordinates, but their raw Euclidean coordinate metric is not the formation \(L^2\) metric.  In the reduced finite-coordinate tribunal, replacing the transported Riesz metric by identity produced order-one formation-operator errors:

\[
0.626\quad\text{(mother coordinates)},
\qquad
0.983\quad\text{(flag coordinates)}.
\]

The correct image geometry must therefore transport the formation metric, not merely the state labels.

## 2. Exact strain-signature metric identities

Let

\[
q_u(x,n)=n^TS(u)(x)n,
\qquad n\in S^2.
\]

The spectral core proves the homogeneous Sobolev identity

\[
\|u\|_{\dot H^{s+1}}^2
=15\int\!\fint_{S^2}
|\Lambda^s q_u(x,n)|^2\,dn\,dx.
\]

Polarization at \(s=-1\) gives

\[
\boxed{
\langle u,v\rangle_{L^2}
=15\int\!\fint_{S^2}
(\Lambda^{-1}q_u)(\Lambda^{-1}q_v)\,dn\,dx.
}
\]

At \(s=0\), using \(\|Cu\|_2=\|\nabla u\|_2\) on the periodic divergence-free class,

\[
\boxed{
\langle Cu,Cv\rangle_{L^2}
=15\int\!\fint_{S^2}q_uq_v\,dn\,dx.
}
\]

Hence the two formation metric levels become

\[
\boxed{
 g^{\Sigma}_{\rm kinetic}=15\,\dot H^{-1},
\qquad
 g^{\Sigma}_{\rm Dirichlet}=15\,L^2
}
\]

on the strain-signature side.

## 3. Heat as the Riesz ratio of the two signature metrics

The Riesz operator taking the kinetic signature metric to the Dirichlet signature metric is

\[
\boxed{
(g^{\Sigma}_{\rm kinetic})^{-1}
 g^{\Sigma}_{\rm Dirichlet}
=\Lambda^2.
}
\]

This is the signature-side form of the Stokes/curl-square generator:

\[
C^2=\Lambda^2
\]

on the periodic divergence-free block.

Random Fourier bilinear audits gave residuals

\[
1.90\times10^{-14}
\]

for the kinetic metric identity,

\[
2.96\times10^{-15}
\]

for the Dirichlet identity, and

\[
5.92\times10^{-15}
\]

for the Riesz-ratio/heat relation.

For pure frequency shells \(m=1,2,3,5,7\), the audit recovered exactly

\[
\frac{\|q\|_{L^2}^2}{\|u\|_{L^2}^2}=m^2,
\qquad
\frac{\|\Lambda^{-1}q\|_{L^2}^2}{\|u\|_{L^2}^2}=1.
\]

## 4. Relation to the formation pencil

The formation bilinear form is

\[
\ell_{\nu,u}(a,b)
=-T(u,a,b)-\nu\langle Ca,Cb\rangle.
\]

After passing to complete signature coordinates, the skew Euler term must be evaluated with the transported kinetic metric, while the viscous term is exactly the Dirichlet metric at one higher signature derivative level.

Thus the formation theory and spectral theory are not related by a bare state bijection.  They are related by a metric hierarchy:

\[
\boxed{
\text{physical }L^2
\longleftrightarrow
\text{signature }\dot H^{-1},
\qquad
\text{physical curl-Dirichlet}
\longleftrightarrow
\text{signature }L^2.
}
\]

This is why the full dynamics conjugacy requires the induced Riesz geometry.

## 5. Pressure and stretching remain compatible readers

Once the signature reconstructs \(u\), it also reconstructs the two local quantities already identified in the formation core:

\[
-\Delta p
=|\nabla u|^2-|Cu|^2,
\]

and

\[
Q=\langle Cu,S(u)Cu\rangle.
\]

The independent six-direction microlocal reverse audit recovered the pressure-source field at relative residual \(3.13\times10^{-15}\) and the tested stretching contraction at roundoff.  These are consequences/readers of the recovered state geometry, not additional primitive coordinates.


## 6. Metric role in geometric reconstruction

The geometric-completeness campaign confirms that the transported metric is not merely needed to write the old formation operator correctly.  It is also required to define the new inverse problem itself.

The hidden connection decomposition is metric-skew, the curl spectral projectors are interpreted in the self-adjoint metric structure, and the Codazzi observability system is coordinate-covariant only when the transported Riesz metric is carried.

Non-orthogonal signature charts with condition numbers \(10\), \(100\), and \(1000\) recover the same connection after whitening by \(G_\Sigma\).  Treating the same charts as Euclidean gives order-one inverse errors.

Hence the canonical differential-signature datum is

\[
\boxed{
(g_\Sigma,C,E,K,\ldots),
}
\]

not an untyped list of matrices.  See [GEOMETRIC_COMPLETENESS.md](GEOMETRIC_COMPLETENESS.md).
