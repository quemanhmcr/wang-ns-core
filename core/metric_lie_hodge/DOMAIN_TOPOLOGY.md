# Domain and Topology

The compact formula with a self-adjoint curl endomorphism is canonical on periodic/closed or suitably decaying Euclidean settings.  On domains with boundary or nontrivial topology, the correct primitive is a typed oriented Hodge/de Rham realization rather than the formal symbol `curl` alone.

## 1. Boundary Green form

For smooth vector fields on a bounded domain,

\[
\boxed{
\langle Ca,b\rangle-\langle a,Cb\rangle
=
\int_{\partial\Omega}n\cdot(a\times b)\,dS.
}
\]

Therefore tangent/free-slip divergence-free fields do not automatically give a self-adjoint curl realization.  The boundary pairing

\[
\mathcal B_\partial(a,b)
=\int_{\partial\Omega}n\cdot(a\times b)\,dS
\]

is a genuine skew boundary sector.  A symmetric/self-adjoint realization requires a compatible domain choice; the differential expression alone does not determine it.

## 2. No-slip refinement

For no-slip divergence-free velocity fields, the quadratic identity

\[
\boxed{
\|\nabla u\|_2^2=\|Cu\|_2^2
}
\]

still gives the Dirichlet/Stokes dissipation, while \(Cu\) need not satisfy the same no-slip boundary condition.  Thus the domain-robust primitive is naturally the curl/Hodge quadratic-form complex, even when a single curl endomorphism is not available on the velocity domain.

## 3. Harmonic cohomology is physical state data

On a domain with nontrivial first cohomology, curl-null fields need not be gauge or constants.  A standard annular example is

\[
\boxed{h=e_\theta/r,}
\]

which satisfies

\[
\nabla\cdot h=0,
\qquad
Ch=0,
\qquad
\oint h\cdot dl=2\pi.
\]

Such harmonic modes can couple to the Lie tensor through \([h,u]\), even though the curl-Dirichlet form does not damp them directly.  Hence one must not quotient \(\ker C\) blindly.

Discrete de Rham audits reproduce the same statement algebraically: for planar cell complexes with zero, one, and two holes, the harmonic one-cochain dimensions are respectively

\[
0,1,2,
\]

matching \(b_1\).

## 4. Domain-complete core

The domain-robust formation datum is therefore better written schematically as

\[
\boxed{
\text{oriented metric Lie algebra}
+
\text{typed Hodge/de Rham complex},
}
\]

including as appropriate:

- operator/form domain;
- boundary trace pairing;
- harmonic cohomology;
- Hodge/Leray decomposition;
- Stokes or self-adjoint realizations when available.

On \(\mathbb T^3\) and the decaying whole-space setting, these data collapse to the simpler self-adjoint curl notation used in [FORMATION_LAW.md](FORMATION_LAW.md).

Topology and boundary typing add geometric/domain data, but the current audits have not found a third local dynamical generator beyond Euler and Stokes heat.
