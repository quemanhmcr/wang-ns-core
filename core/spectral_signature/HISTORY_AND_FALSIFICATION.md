# History and Falsification of the Spectral Signature

This file keeps only the failures that directly determined the final form of the whole-state signature.  The larger propagation/G3/scale history is intentionally omitted from the canonical core.

## 1. Scalar critical work was too small an object

The critical work reader
\[
W_\Lambda
\]
can vanish while the hard field remains nonzero.  Therefore a scalar production rate cannot be the whole obstruction/signature.

The information hierarchy begins
\[
\mathscr O_a
\longrightarrow
J_a=\frac14\mathscr O_a(u)u
\longrightarrow
W(a).
\]
Each contraction can enter a kernel while the parent tensor remains visible.

## 2. Self-contraction was still too small

Beltrami and other structured states can satisfy
\[
J_0=\frac14\mathscr O_0(u)u=0
\]
while \(\mathscr O_0(u)\) acts nontrivially on independent tangent directions.

This killed the idea that the diagonal self-action alone could represent the whole NS geometry.

## 3. The zero spectral fold was not the whole signature

States were found for which \(W(0)\) was tiny while a shifted cut \(a\neq0\) produced a much larger response.  The correct object therefore became the entire family
\[
a\mapsto\mathscr O_a,
\qquad
H_a=\operatorname{sgn}(C-aI),
\]
not only the physical zero fold.

The zero fold remains special for the critical reader \(|C|\), but it is only one slice of the full curl spectral flag.

## 4. Shifted tomography unified the family with the mother

The decisive identity was
\[
[D,C]
=\frac12\int_{\mathbb R}[D,H_a]\,da
=\frac12\int_{\mathbb R}H_a\operatorname{skew}\mathscr O_a\,da.
\]
This showed that the shifted family and the mother deformation carry the same first-order spectral information.

The apparently larger object \(\{\mathscr O_a\}\) is therefore a spectral decomposition of the smaller mother
\[
E=[\nabla,C].
\]

## 5. The entire curl functional calculus followed

For differentiable spectral readers,
\[
[\nabla_v,f(C)]
=\frac12\int_{\mathbb R}f'(a)
H_a\operatorname{skew}\mathscr O_a(v)\,da.
\]
Thus energy/helicity/enstrophy/critical spectral readers are not separate nonlinear species.  Their deformations are moments of one spectral-flag differential.

## 6. The curl commutant was a real falsification, not a nuisance

A tempting overclaim was
\[
\mathscr O=\text{the full connection}.
\]
This is false.

The connection contains a nonzero curl-commuting block.  In actual Fourier tests this block carried a substantial fraction of connection norm and self-advection.  It is real dynamics.

But it is vertical and isospectral:
\[
[\Gamma^\parallel,C]=0.
\]
It preserves every quadratic curl spectral reader.  The signature records the horizontal/off-spectral deformation; the recovered physical state fixes the vertical gauge.

## 7. Matching all quadratic spectra did not match the signature

Two states were constructed with the same complete signed-curl quadratic spectral measure.  Consequently all tested quantities
\[
\langle u,f(C)u\rangle
\]
agreed to machine precision.

Their operator-valued signatures were nevertheless order-one different, and so were their Euler vector fields.

Therefore the signature is not a disguised energy spectrum.  It carries phase/spatial compatibility information required by nonlinear NS evolution.

## 8. Full state recovery was stronger than rank tests

Random signature measurements reconstructed all nonconstant Galerkin state degrees of freedom at bandwidths tested.  More importantly, the recovered state reproduced
\[
u,\quad \omega,\quad S,\quad S\omega,\quad N(u),\quad p,\quad \nabla p,\quad \operatorname{Hess}p,\quad C^2u,\quad u_t
\]
to machine precision.

The NS trajectory itself was then integrated in signature coordinates and matched the state-coordinate trajectory.

## 9. Principal-symbol analysis replaced black-box inversion

The key continuum calculation was
\[
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(x)\xi}{|\xi|^2}\xi\times b.
\]
The signature therefore reads exactly the quadratic form of the strain tensor.

Only six fixed directions are needed to recover all five components of \(\mathrm{Sym}_0(3)\).  Incompressibility then gives
\[
\Delta u=2\operatorname{div}S.
\]
This turned numerical injectivity into an explicit structural inverse.

## 10. The exact kernel is geometric

If the full mother/signature vanishes, then
\[
S(u)=0.
\]
Hence \(u\) is an Euclidean Killing field
\[
u(x)=Ax+b,
\qquad A^T=-A.
\]
On the periodic mean-zero class, only the zero field remains.  Exact polynomial and Fourier kernel tests found no hidden nonlinear kernel.

## 11. The canonical norm is not ad hoc

The spherical identity
\[
\fint_{S^2}(n^TSn)^2\,dn
=\frac{2}{15}|S|^2
\]
combined with divergence-free Korn/Fourier geometry gives
\[
\|u\|_{\dot H^{s+1}}^2
=15\int\fint_{S^2}|\Lambda_x^sq_u|^2.
\]
Thus the microlocal signature norm is exactly the state Sobolev norm after normalization.

## 12. High-frequency probes exposed the difference between \(O_0\) and the full flag

The critical slice \(O_0\) remained injective in finite truncations, but its high-frequency response was lower order.  Moving cuts near the active curl frequency carried the principal radial/strain information.

This established the final distinction:
\[
\boxed{
\mathscr O=\{\mathscr O_a\}_{a\in\mathbb R}
\text{ is the whole spectral signature; }
\mathscr O_0\text{ is the critical slice.}
}
\]

## 13. Self-generated Krylov contractions still failed

Even families such as
\[
\mathscr O_a(u)C^m u
\]
for several \(m\) did not reconstruct the full Euler vector field.  This was a strong warning against compressing the operator slot prematurely.

The operator-valued tensor is irreducible at the level required for whole-state completeness.

## 14. Two implementation bugs became methodological rules

A physical/Fourier representation mismatch once created a false high-dimensional kernel.  Mishandling the zero curl block created another false geometry.  Both disappeared when operator types and spectral threshold conventions were corrected.

The resulting rule is strict:

> No kernel, rank, or new-geometry claim is trusted until physical/Fourier typing, zero modes, and threshold conventions have been audited.

## 15. Final compression

The discovery path grew from scalar work to hard field, tensor curvature, shifted spectral family, microlocal inversion, and gauge geometry.  The final canonical object became smaller again:
\[
\boxed{
E_u=[\nabla_u,C].
}
\]
The full shifted family is its canonical spectral-flag normal form:
\[
\boxed{
E
\longleftrightarrow
\{\mathscr O_a\}_a.
}
\]

This is the main lesson of the campaign: the whole-NS signature is not a new defect added to Navier--Stokes.  It is the curl-relative differential geometry already present in the physical connection.
