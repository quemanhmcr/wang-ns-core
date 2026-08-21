# NEO Mother / Spectral-Flag Completeness Theorem
## Structural whole-Navier--Stokes coordinates on the smooth periodic state space

**Status.** Structural theorem on the smooth mean-zero divergence-free three-torus, with a Schwartz whole-space extension recorded separately.  This is **not** a regularity theorem, blow-up exclusion theorem, or weak-solution theorem.

This note closes the structural question left open by the two preceding records:

- `NEO_CURL_SPECTRAL_OBSTRUCTION_SIGNATURE.md` identified the full shifted spectral-flag signature;
- `NEO_CURL_SPECTRAL_SIGNATURE_COMPLETENESS.md` stress-tested injectivity, microlocal inversion, scaling, gauge, and NS-coordinate evolution.

The decisive simplification is that the full shifted family is a canonical spectral normal form of a smaller already-complete object:
\[
\boxed{
E_u:=[\nabla_u,C].
}
\]
Thus the final compiler is
\[
\boxed{
\mathscr O
\longleftrightarrow
E
\longrightarrow
\sigma_1(E)
\longleftrightarrow
S
\longleftrightarrow
u/\operatorname{Kill}
\longrightarrow
F_{NS}(u).
}
\]
Here \(C=\operatorname{curl}\), \(S=\frac12(\nabla u+\nabla u^T)\), and \(\nabla_vw=P[(v\cdot\nabla)w]\) is the intrinsic projected transport connection.

The result is a coordinate/completeness theorem for the homogeneous incompressible NS state geometry.  Regularity is a different later question.

Labels used below: **THEOREM**, **LEMMA**, **COROLLARY**, **AUDIT**, **CAUTION**, **OPEN EXTENSION**.

---

## 0. State space and conventions

Let
\[
\mathcal X_\infty
:=\left\{
 u\in C^\infty(\mathbb T^3;\mathbb R^3):
 \nabla\cdot u=0,
 \ \int_{\mathbb T^3}u\,dx=0
\right\}.
\]
On this space the periodic curl operator is self-adjoint and has no zero mode.  For every real threshold \(a\), define a spectral involution
\[
H_a:=\operatorname{sgn}(C-aI).
\]
If \(a\) lands exactly on a discrete curl eigenvalue, choose either one-sided value
\[
\operatorname{sgn}_\pm(0)=\pm1.
\]
Then \(H_a^2=I\).  The choice at the seam does not affect any \(a\)-integral below because the set of seams is countable and has Lebesgue measure zero.

For \(u\in\mathcal X_\infty\), define
\[
\Gamma_u:=\nabla_u,
\qquad
E_u:=[\Gamma_u,C],
\]
\[
A_a(u):=[\Gamma_u,H_a],
\]
and the shifted spectral-flag signature
\[
\boxed{
\mathscr O_a(u)
:=H_aA_a(u)-A_a(H_au).
}
\]
The physical zero-fold slice is \(\mathscr O_0=R_H\), but the theorem concerns the full operator-valued family \(a\mapsto\mathscr O_a\).

All identities are first stated on smooth trigonometric test fields; by smooth Fourier convergence they extend in the natural distribution/operator sense on \(\mathcal X_\infty\).

---

## 1. Reverse compiler from the signature to the cut connection -- LEMMA

For each \(a\) and \(u\),
\[
A_a(u)^*=A_a(u),
\qquad
H_aA_a(u)+A_a(u)H_a=0.
\]
The first identity follows from \(\Gamma_u^*=-\Gamma_u\) and \(H_a^*=H_a\); the second follows by differentiating the involution identity \(H_a^2=I\) along the metric connection.

Now
\[
\mathscr O_a(u)=H_aA_a(u)-A_a(H_au).
\]
The first summand is skew-adjoint and the second is self-adjoint.  Therefore
\[
\operatorname{skew}\mathscr O_a(u)=H_aA_a(u),
\]
so
\[
\boxed{
A_a(u)=H_a\operatorname{skew}\mathscr O_a(u).
}
\]
Thus no cut-connection information is lost in the tensor signature.

**CAUTION.** This statement is operator-valued.  Self-contractions such as \(\mathscr O_a(u)u\) and scalar works may have large kernels and are not complete coordinates.

---

## 2. Spectral layer-cake reconstructs the mother deformation -- LEMMA

For scalar spectral values \(x,y\),
\[
\frac12\int_{\mathbb R}
\big(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\big)\,da
=y-x.
\]
Hence, on curl spectral matrix elements,
\[
\frac12\int_{\mathbb R}[\Gamma_u,H_a]_{xy}\,da
=(y-x)(\Gamma_u)_{xy}
=[\Gamma_u,C]_{xy}.
\]
Therefore
\[
\boxed{
E_u
=\frac12\int_{\mathbb R}A_a(u)\,da
=\frac12\int_{\mathbb R}
H_a\operatorname{skew}\mathscr O_a(u)\,da.
}
\]
The identity is exact on trigonometric polynomials and hence on smooth states when interpreted against trigonometric test fields.

This is the precise statement that the full spectral flag is a tomography of the NEO mother deformation.

---

## 3. Exact local form of the mother -- LEMMA

Because \(P\) commutes with curl on the torus,
\[
E_uv=P[D_u,C]v.
\]
For smooth divergence-free fields,
\[
[D_u,C]v
=-\sum_{j=1}^3\nabla u_j\times\partial_jv.
\]
Hence
\[
\boxed{
E_uv
=-P\sum_j\nabla u_j\times\partial_jv.
}
\]
This is an exact first-order differential operator in the probe field \(v\), with coefficients determined by the first jet of \(u\).

---

## 4. Principal symbol reads exactly the strain quadratic form -- LEMMA

Let \(\xi\ne0\), \(b\perp\xi\), and let \(P_\xi\) be the Leray symbol.  The principal symbol of \(E_u\) is
\[
\sigma_1(E_u)(x,\xi)b
=-iP_\xi\big((\nabla u(x))^T\xi\times b\big).
\]
Write
\[
(\nabla u)^T\xi=\alpha\xi+r,
\qquad r\perp\xi.
\]
Since \(r,b\in\xi^\perp\), the vector \(r\times b\) is parallel to \(\xi\) and is annihilated by \(P_\xi\).  Moreover
\[
\alpha
=\frac{\xi^T\nabla u\,\xi}{|\xi|^2}
=\frac{\xi^TS\xi}{|\xi|^2},
\]
because the skew part of \(\nabla u\) has zero quadratic form.  Therefore
\[
\boxed{
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(x)\xi}{|\xi|^2}\,\xi\times b.
}
\]
For \(n\in S^2\), define
\[
q_u(x,n):=n^TS(x)n.
\]
Then the principal symbol is exactly the scalar strain reader \(q_u\) times the canonical quarter-turn \(J_n:b\mapsto n\times b\) on \(n^\perp\).

---

## 5. Direct extraction of the scalar strain reader from the signature -- LEMMA

Let
\[
e_1(x,n):=\sigma_1(E_u)(x,n)\big|_{n^\perp}.
\]
On the two-dimensional plane \(n^\perp\), \(J_n^*J_n=I\) and \(\operatorname{tr}_{n^\perp}I=2\).  Since
\[
e_1=-iq_uJ_n,
\]
one gets
\[
\boxed{
q_u(x,n)
=\frac{i}{2}
\operatorname{tr}_{n^\perp}
\big(J_n^*e_1(x,n)\big).
}
\]
Thus the full signature first reconstructs \(E_u\), then its principal symbol, then the complete family of quadratic strain readings \(q_u(x,n)\).

---

## 6. Spherical inversion reconstructs the full strain -- LEMMA

For a symmetric trace-free matrix \(S\), the standard spherical fourth-moment identity gives
\[
\fint_{S^2}n_in_jn_kn_l\,dn
=\frac1{15}
(\delta_{ij}\delta_{kl}
+\delta_{ik}\delta_{jl}
+\delta_{il}\delta_{jk}).
\]
Because \(\operatorname{tr}S=\nabla\cdot u=0\),
\[
\fint_{S^2}(n^TSn)n\otimes n\,dn
=\frac{2}{15}S.
\]
Hence
\[
\boxed{
S(x)
=\frac{15}{2}
\fint_{S^2}
q_u(x,n)n\otimes n\,dn.
}
\]
The inverse is explicit and linear.

---

## 7. Incompressibility reconstructs the velocity modulo Killing fields -- LEMMA

For divergence-free \(u\),
\[
(\operatorname{div}S)_i
=\partial_jS_{ij}
=\frac12\Delta u_i.
\]
Thus
\[
\boxed{
\Delta u=2\operatorname{div}S.
}
\]
On \(\mathcal X_\infty\), the mean-zero condition makes \(\Delta^{-1}\) unique, and
\[
\boxed{
u=2\Delta^{-1}\operatorname{div}S.}
\]
The mother decoder is therefore
\[
\boxed{
R_E(E)
:=15\Delta^{-1}\operatorname{div}
\left[
\fint_{S^2}q_E(x,n)n\otimes n\,dn
\right],
}
\]
where \(q_E\) is extracted from the principal symbol of \(E\) by Section 5.  If
\[
T(\Sigma):=\frac12\int_{\mathbb R}H_a\operatorname{skew}\Sigma_a\,da,
\]
then the full-signature decoder is
\[
\boxed{R_{\mathscr O}:=R_E\circ T.}
\]
On the physical image,
\[
\boxed{R_E(E_u)=u,\qquad R_{\mathscr O}(\mathscr O(u))=u.}
\]

---

## 8. Mother / Spectral-Flag Completeness Theorem -- THEOREM

Let \(u,v\in\mathcal X_\infty\).  The following are equivalent:

\[
\boxed{
\mathscr O_a(u)=\mathscr O_a(v)
\quad\text{for a.e. }a\in\mathbb R,
}
\]
\[
\boxed{E_u=E_v,}
\]
\[
\boxed{S(u)=S(v),}
\]
\[
\boxed{u=v.}
\]

### Proof

Signature equality gives cut-connection equality by the reverse compiler.  Layer-cake gives \(E_u=E_v\).  Equality of mother operators gives equality of principal symbols, hence
\[
n^T(S(u)-S(v))n=0
\quad\forall n\in S^2,
\]
so \(S(u)=S(v)\).  Finally \(\Delta(u-v)=2\operatorname{div}(S(u)-S(v))=0\); the mean-zero periodic harmonic field is zero.  Therefore \(u=v\).

Without the mean-zero/periodic normalization, the kernel is precisely the Euclidean Killing sector satisfying
\[
\operatorname{sym}\nabla w=0.
\]
On \(\mathbb R^3\), smooth solutions of the Killing equation are
\[
w(x)=Ax+b,
\qquad A^T=-A.
\]
On the periodic torus only constants survive; on the mean-zero torus none survive.

**Interpretation.** The full operator-valued spectral flag is a faithful state coordinate modulo the exact geometric symmetry that leaves strain zero.

---

## 9. The mother is already complete -- COROLLARY

The proof above never needs the spectral flag after reconstructing \(E_u\).  Therefore the smaller map
\[
\boxed{
\mathcal M:u\mapsto E_u=[\nabla_u,C]
}
\]
is already injective on \(\mathcal X_\infty\), with explicit inverse obtained from its principal symbol.

Thus
\[
\boxed{
\mathscr O
\longleftrightarrow
E
}
\]
on the physical image, while \(\mathscr O\) supplies the canonical spectral-cut resolution of the already-complete mother tensor.

This is the strongest NEO compression exposed by the campaign:

> the compiler becomes smaller as it becomes stronger.

---

## 10. Exact homogeneous Sobolev isometry -- THEOREM

For every real \(s\) for which the homogeneous norms are finite,
\[
\boxed{
2\|S(u)\|_{\dot H^s}^2
=\|u\|_{\dot H^{s+1}}^2.
}
\]
Indeed, for each nonzero Fourier mode \(k\) with \(k\cdot\hat u(k)=0\),
\[
\left|\operatorname{sym}(ik\otimes\hat u(k))\right|^2
=\frac12|k|^2|\hat u(k)|^2.
\]
Multiplication by \(|k|^{2s}\) and summation yields the identity.

The spherical identity
\[
\fint_{S^2}(n^TSn)^2\,dn
=\frac{2}{15}|S|^2
\]
then gives
\[
\boxed{
\|u\|_{\dot H^{s+1}}^2
=15\int_{\mathbb T^3}
\fint_{S^2}
|\Lambda_x^sq_u(x,n)|^2\,dn\,dx.
}
\]
Equivalently, because
\[
\|\sigma_1(E_u)(x,n)\|_{HS(n^\perp)}^2
=2q_u(x,n)^2,
\]
\[
\boxed{
\|u\|_{\dot H^{s+1}}^2
=\frac{15}{2}
\int_{\mathbb T^3}
\fint_{S^2}
\|\Lambda_x^s\sigma_1(E_u)(x,n)\|_{HS(n^\perp)}^2
\,dn\,dx.
}
\]

Thus the canonical microlocal mother/signature norm is not merely equivalent to the state Sobolev norm: it is exactly isometric after the universal normalization above.

---

## 11. Six fixed directions give uniform observability -- THEOREM

The full spherical family is not needed for a quantitative inverse.  Let
\[
n_1=e_1,
\quad n_2=e_2,
\quad n_3=e_3,
\]
\[
n_4=\frac{e_1+e_2}{\sqrt2},
\quad
n_5=\frac{e_1+e_3}{\sqrt2},
\quad
n_6=\frac{e_2+e_3}{\sqrt2}.
\]
The frame map
\[
\mathrm{Sym}_0(3)\ni S
\mapsto
(n_r^TSn_r)_{r=1}^6
\]
has Gram eigenvalues
\[
\boxed{
\frac{7-\sqrt{17}}8
\quad(\text{multiplicity }2),
\qquad
\frac12,
\qquad
\frac{7+\sqrt{17}}8
\quad(\text{multiplicity }2).
}
\]
Therefore for every real \(s\),
\[
\boxed{
\frac{7-\sqrt{17}}{16}
\|u\|_{\dot H^{s+1}}^2
\le
\sum_{r=1}^6
\|\Lambda_x^sq_u(\cdot,n_r)\|_2^2
\le
\frac{7+\sqrt{17}}{16}
\|u\|_{\dot H^{s+1}}^2.
}
\]
The constants are explicit, bandwidth independent, and scale covariant.

This is a deterministic six-probe observability theorem for the physical state modulo the zero/Killing sector.

---

## 12. Exact signature-image projector -- THEOREM / COORDINATE GEOMETRY

Let
\[
\mathcal S:u\mapsto\mathscr O(u)
\]
be the full signature map and let \(R_{\mathscr O}\) be the explicit decoder above, defined on an ambient class of signature families for which the reconstruction operations make sense.  On the physical image,
\[
R_{\mathscr O}\mathcal S=I.
\]
Define
\[
\boxed{
\Pi_{\mathscr O}:=\mathcal S R_{\mathscr O}.
}
\]
Then
\[
\Pi_{\mathscr O}^2=\Pi_{\mathscr O},
\]
and
\[
\boxed{
\operatorname{Im}\mathcal S
=\operatorname{Fix}\Pi_{\mathscr O}.
}
\]
Thus the physical signature families form a linear retract of the ambient signature space selected by the compatibility conditions encoded in \(R_{\mathscr O}\) and \(\mathcal S\).

**CAUTION.** Characterizing this image by a minimal intrinsic list of equations, without explicitly invoking \(R_{\mathscr O}\), is a separate normal-form problem.  The projector characterization is already exact but not necessarily minimal syntax.

---

## 13. Navier--Stokes is exactly conjugate to a flow on the signature image -- THEOREM

The projected homogeneous NS vector field is
\[
F_\nu(u)
=P[X_u,C]u-\nu C^2u.
\]
For \(\Sigma\in\operatorname{Im}\mathcal S\), define
\[
\boxed{
\mathcal F_{\mathscr O,\nu}(\Sigma)
:=\mathcal S\big(F_\nu(R_{\mathscr O}\Sigma)\big).
}
\]
Then
\[
\boxed{
u_t=F_\nu(u)
\iff
\Sigma_t=\mathcal F_{\mathscr O,\nu}(\Sigma),
\qquad
\Sigma=\mathcal S(u).
}
\]
Moreover
\[
\Pi_{\mathscr O}\mathcal F_{\mathscr O,\nu}(\Sigma)
=\mathcal F_{\mathscr O,\nu}(\Sigma),
\]
so the vector field is tangent to the physical signature image.

This is an exact coordinate conjugacy.  It does **not** by itself make the regularity problem easier; it establishes that the signature carries the whole smooth NS dynamics without missing state information.

---

## 14. Horizontal / vertical gauge reconstruction -- THEOREM ON THE PERIODIC CURL SPECTRUM

Let \(\Gamma_u=\nabla_u\).  In the spectral decomposition of \(C\), for eigenvalues \(x,y\),
\[
(E_u)_{xy}
=(y-x)(\Gamma_u)_{xy}.
\]
Hence the off-spectral/horizontal connection is determined directly by the mother:
\[
\boxed{
(\Gamma_u^\perp)_{xy}
=\frac{(E_u)_{xy}}{y-x},
\qquad x\ne y.
}
\]
The remaining diagonal-in-curl blocks satisfy
\[
[\Gamma_u^\parallel,C]=0
\]
and form the vertical isospectral gauge sector.

Abstractly \(E_u\) does not record this vertical block.  Physically, however, the decoder reconstructs \(u\), and the physical connection is fixed by that state.  Therefore
\[
\boxed{
\Gamma_u^\parallel
=\Pi_{\mathrm{comm}(C)}\nabla_{R_E(E_u)}.
}
\]
Consequently
\[
\boxed{
\nabla_u
=\operatorname{ad}_{C,\perp}^{-1}(E_u)
+\Pi_{\mathrm{comm}(C)}\nabla_{R_E(E_u)}.
}
\]
Thus the vertical commutant is real dynamics but not an independent primitive.  It is the isospectral gauge chosen by the recovered physical state.

---

## 15. Native NS faces are corollaries of completeness -- COROLLARY

Once \(u=R_{\mathscr O}(\mathscr O(u))\) is known, every native deterministic NS field generated by the anchor grammar is recovered, including
\[
\omega=Cu,
\qquad
S=\operatorname{sym}\nabla u,
\qquad
S\omega,
\]
\[
N(u)=P(u\times Cu),
\qquad
C^2u,
\qquad
u_t=F_\nu(u).
\]
The pressure/Hodge face is reconstructed from
\[
-\Delta p=\operatorname{tr}(\nabla u)^2
\]
with the standard mean-zero normalization, hence so are \(\nabla p\) and \(\operatorname{Hess}p\).

Therefore the signature is not merely complete for spectral observables.  It is complete for the full smooth homogeneous NS state because it determines the state itself.

---

## 16. Why the critical slice is not the theorem object -- CAUTION

The full operator \(\mathscr O_0\) may be injective on finite Galerkin truncations, but high-frequency tests show its response is lower order compared with the moving-cut family.  For pure high-frequency helical probes, the zero-fold connection behaves approximately as
\[
\|[\nabla_u,H]v_q\|\sim q^{-1},
\]
while cuts with \(a\sim q\) carry the principal radial information needed to reconstruct \(E_u\).

Thus the stable continuum theorem belongs to
\[
\boxed{
\text{full spectral flag }\{\mathscr O_a\}_a
\quad\text{or equivalently the mother }E_u,
}
\]
not to the zero-fold critical slice alone.

The zero fold remains distinguished for critical helicity work.  It should not be promoted into the whole-state coordinate merely because it is physically important at the critical reader.

---

## 17. Why self-contractions are not the theorem object -- CAUTION

The campaign falsified the possibilities
\[
\{J_a\}_a
\quad\text{and}\quad
\{\mathscr O_a(u)C^mu\}_{a,m\le4}
\]
as complete decoders of the Euler forcing: relative reconstruction errors remained order one.

This is structural evidence that completeness is genuinely tensor/operator-valued.  The input slot cannot be collapsed to a short list of state-generated probes without losing whole-NS information.

---

## 18. Schwartz whole-space extension -- COROLLARY / FUNCTIONAL-ANALYTIC PACKAGING

For \(u\in\mathcal S(\mathbb R^3;\mathbb R^3)\) divergence free, the local mother formula, principal-symbol identity, spherical strain inverse, and Poisson reconstruction are unchanged.  Decay excludes nonzero Euclidean Killing fields.  Thus
\[
E_u=E_v\Longrightarrow u=v
\]
and the same Sobolev isometry holds whenever the homogeneous norms are finite.

The shifted spectral family \(H_a=\operatorname{sgn}(C-a)\) is defined by the Fourier/helical spectral calculus.  Threshold surfaces have Fourier Lebesgue measure zero.  The layer-cake identity is read weakly on Schwartz test fields.

The **mother completeness**, strain inversion, Killing-kernel statement, and Sobolev identities therefore extend directly to this Schwartz class.  The equivalence with the full shifted family uses the weak layer-cake spectral integral just described.  A publish-grade whole-space treatment should spell out that operator topology explicitly; no new algebraic obstruction appears in the audit.

---

## 19. What has actually been proved structurally

On the smooth mean-zero periodic state space:

1. the full spectral flag reconstructs the mother \(E_u\);
2. the mother principal symbol reconstructs the entire strain tensor;
3. incompressibility reconstructs the velocity uniquely;
4. the resulting inverse is explicit and linear;
5. the canonical microlocal signature norm is exactly the velocity Sobolev norm after universal normalization;
6. six fixed directional readings give explicit uniform observability constants;
7. the physical signature image has an exact projector \(\mathcal SR\);
8. NS is exactly conjugate to an autonomous vector field on that image;
9. the horizontal connection is recovered directly from \(E\), and the vertical commutant is recovered from the state selected by the same signature.

This justifies the structural statement
\[
\boxed{
\mathscr O
\longleftrightarrow
E
\longleftrightarrow
S
\longleftrightarrow
u
\longleftrightarrow
\text{entire smooth homogeneous NS dynamics}.
}
\]

---

## 20. What this theorem does not prove

It does **not** prove:

- global smoothness of 3D NS;
- nonexistence of finite-time singularities;
- a priori control of the signature norm at critical scaling;
- compactness of the full signature under the bounded-ancient extraction used by the terminal programme;
- a theorem for arbitrary weak solutions, boundaries, forcing, or variable-coefficient geometries;
- that signature coordinates make the nonlinear estimates required for regularity easier.

The theorem is a **completeness / coordinate theorem**, not a regularity estimate.

This distinction should remain explicit in every later use.

---

## 21. Methodological lessons from the theoremization

### 21.1 The largest-looking object was not the final compiler

The discovery path moved through
\[
R_H\to\mathscr O_a\to E_u.
\]
The full spectral family was necessary to expose the invariant structure, but the mother \(E_u\) is the smaller complete object.  This is a concrete instance of the NEO rule:

> stronger compilers should become smaller, not accumulate mechanisms.

### 21.2 Quotient information can still identify a physical state

Abstractly \([\Gamma,C]\) forgets the curl commutant of \(\Gamma\).  This does not contradict state completeness because physical connections are not arbitrary points in the quotient: they lie on the section \(u\mapsto\nabla_u\).  The horizontal signature identifies \(u\); the state then fixes the vertical block.

### 21.3 Tensor typing is essential

Completeness belongs to the operator-valued one-form.  Scalar work, self-contractions, a few Krylov leaves, and pointwise norm collapses can all enter large kernels.  Do not infer a property of \(\mathscr O\) from one of its contracted readers.

### 21.4 Principal-symbol completeness and critical importance are different questions

Moving cuts carry the principal whole-state information.  The zero fold is lower order in the UV but is singled out by the critical reader \(|C|\).  “Whole-state coordinate” and “critical dynamical slice” must remain different labels.

### 21.5 Type errors can mimic geometry

The completeness campaign found false kernels caused by physical/Fourier representation errors and by mishandling the zero curl block.  Any future rank, kernel, or coercivity claim must first pass representation typing and threshold conventions.

### 21.6 Structural completeness is not dynamical control

Knowing that a coordinate contains the whole state does not supply a favorable estimate for its evolution.  The regularity problem begins after completeness, not before it.

---

## 22. Compact theorem statement

For smooth mean-zero divergence-free periodic velocity fields, define
\[
\mathcal S(u)=\{\mathscr O_a(u)\}_{a\in\mathbb R}.
\]
Then there exists an explicit linear decoder \(R_{\mathscr O}\), constructed by
\[
\mathcal S(u)
\xrightarrow{\text{reverse + layer cake}}
E_u
\xrightarrow{\sigma_1}
q_u(x,n)
\xrightarrow{\text{spherical frame}}
S(u)
\xrightarrow{2\Delta^{-1}\operatorname{div}}
u,
\]
such that
\[
\boxed{R_{\mathscr O}\mathcal S=I.}
\]
Moreover, for every real \(s\),
\[
\boxed{
\|u\|_{\dot H^{s+1}}^2
=15\int\fint_{S^2}|\Lambda_x^sq_u(x,n)|^2\,dn\,dx,
}
\]
and six fixed directions obey the explicit two-sided frame estimate
\[
\boxed{
\frac{7-\sqrt{17}}{16}\|u\|_{\dot H^{s+1}}^2
\le
\sum_{r=1}^6\|\Lambda_x^sq_u(\cdot,n_r)\|_2^2
\le
\frac{7+\sqrt{17}}{16}\|u\|_{\dot H^{s+1}}^2.
}
\]
Therefore the full mother/spectral-flag signature is a faithful, quantitatively stable coordinate of the entire smooth homogeneous incompressible Navier--Stokes state, modulo exactly the Euclidean Killing symmetry before normalization.

The NS flow is exactly conjugate to a flow on the physical signature image by \(\mathcal S\) and \(R_{\mathscr O}\).

That is the structural whole-NS theorem.  Blow-up is not part of its statement.
