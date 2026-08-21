# NEO Riccati Normal-Invariant Pair
## Angular alignment and gradient spectral shape have no restricted-Riccati source

**Purpose.** Replace the minimal defects by two polynomial normal-action meters whose restricted/local Riccati self-dynamics cancels exactly:
\[
\boxed{
\mathcal J:=\omega\times A\omega,
\qquad
\mathcal V:=r^2-\frac16g^3.
}
\]
Here \(\mathcal J\) detects angular/eigenline misalignment and \(\mathcal V\) detects repeated-spectrum departure.  They are not new primitives: both are polynomial renderers of \(A=\nabla U\) and \(\omega=CU\).

Labels: **EXACT**, **AUDIT**, **CONDITIONAL TYPE-I DEDUCTION**, **ACTION IDENTITY**, **OPEN**.

---

## 0. Relation to the minimal curl-frame defects -- EXACT

On \(\rho=|\omega|>0\), write
\[
\omega=\rho n,
\qquad
Sn=an+b.
\]
Because the antisymmetric part of \(A\) annihilates \(\omega\),
\[
A\omega=S\omega=\rho(an+b).
\]
Hence
\[
\boxed{
\mathcal J
=\omega\times A\omega
=\rho^2n\times b,
}
\]
and therefore
\[
\boxed{|
\mathcal J|^2=\rho^4|b|^2.}
\]
This is exactly the polynomial angular renderer already used in the Type-I zero-set arguments, now retained as a vector rather than immediately squared.

For
\[
g=\operatorname{tr}(A^2),\qquad
r=\operatorname{tr}(A^3),
\]
put
\[
\boxed{\mathcal V=r^2-g^3/6.}
\]
When \(b=0\),
\[
\boxed{
\mathcal V
=\frac1{12}\delta^2(2\delta-9a^2),
\qquad
\delta=6a^2-g.
}
\]

Thus \(\mathcal J\) is the polynomial angular normal meter and \(\mathcal V\) is the polynomial spectral-shape normal meter.

---

## 1. Restricted Riccati preserves the angular polynomial exactly -- EXACT

Consider the restricted/local velocity-gradient dynamics
\[
\boxed{
D_tA=-A^2+\frac g3I.
}
\]
For trace-free \(A\), its skew part gives the vorticity law
\[
\boxed{D_t\omega=A\omega.}
\]
Then
\[
\begin{aligned}
D_t(A\omega)
&=(D_tA)\omega+A(D_t\omega)\\
&=\left(-A^2+\frac g3I\right)\omega+A^2\omega\\
&=\frac g3\omega.
\end{aligned}
\]
Therefore
\[
\boxed{
D_t\mathcal J
=D_t(\omega\times A\omega)=0.
}
\]

`audits/neo_angular_invariant.py` verifies this identity symbolically for a completely general trace-free \(3\times3\) matrix.

This is stronger than the curl-frame statement
\[
P D_tb=-2ab.
\]
The apparent Riccati damping of \(b\) is exactly compensated by the growth and turning of the vorticity factors in the polynomial invariant \(\rho^2n\times b\).

---

## 2. Restricted Riccati preserves the discriminant exactly -- EXACT

The same local matrix dynamics gives
\[
D_tg=-2r,
\qquad
D_tr=-\frac12g^2.
\]
Hence
\[
\boxed{
D_t\mathcal V
=2rD_tr-\frac12g^2D_tg=0.
}
\]

Thus the pair
\[
\boxed{(\mathcal J,\mathcal V)}
\]
contains **no restricted-Riccati source at all**.

This is the central advantage over \((b,\delta)\): the latter are geometrically minimal coordinates, while \((\mathcal J,\mathcal V)\) are better action meters because the internally coherent amplifier has already been quotiented out dynamically.

---

## 3. Zero set of the pair -- EXACT / TYPE-I BRANCH CARE

On a curl-active point,
\[
\mathcal J=0
\]
means \(\omega\) is an eigenvector of \(A\), equivalently of \(S\).

If also
\[
\mathcal V=0,
\]
the trace-free cubic characteristic polynomial has a repeated eigenvalue.  Relative to the vorticity eigenline there are two aligned repeated-spectrum possibilities:
\[
\boxed{
\delta=0
\quad\vee\quad
\delta=\frac92a^2.
}
\]

The first is G3.  The second is the opposite repeated-tangential-eigenvalue branch.

Therefore the pair is not by itself a unique algebraic coordinate chart for G3.  In the Type-I positive-under-gain setting, however, `NEO_GAIN_TO_DISCRIMINANT_COMPILER.md` shows that the opposite branch cannot occupy positive spatial measure.  This is exactly enough for the causal compactness split; no third polynomial defect is needed merely to distinguish the two sheets pointwise.

---

## 4. Full material equation for the angular invariant -- EXACT

For full Navier--Stokes,
\[
D_t\omega=A\omega+\nu\Delta\omega,
\]
\[
D_tA=-A^2+\frac g3I-H_0+\nu\Delta A.
\]
As before,
\[
\begin{aligned}
D_t(A\omega)
&=\frac g3\omega-H_0\omega\\
&\quad+\nu\big[(\Delta A)\omega+A\Delta\omega\big].
\end{aligned}
\]
Therefore the exact material law is
\[
\boxed{
\begin{aligned}
D_t\mathcal J
={}&-\omega\times H_0\omega\\
&+\nu\Big[
\Delta\omega\times A\omega
+\omega\times((\Delta A)\omega+A\Delta\omega)
\Big].
\end{aligned}}
\]

Every non-viscous restricted-Riccati term has cancelled.

---

## 5. Parabolic angular equation has only first-gradient square remainder -- EXACT

Let
\[
L=D_t-\nu\Delta.
\]
Using
\[
\Delta(\omega\times A\omega)
=\Delta\omega\times A\omega
+2\partial_j\omega\times\partial_j(A\omega)
+\omega\times\Delta(A\omega),
\]
and
\[
\Delta(A\omega)
=(\Delta A)\omega
+2(\partial_jA)(\partial_j\omega)
+A\Delta\omega,
\]
all explicit second derivatives cancel.  One obtains
\[
\boxed{
\begin{aligned}
L\mathcal J
={}&-\omega\times H_0\omega\\
&-2\nu\sum_j\Big[
\partial_j\omega\times\partial_j(A\omega)\\
&\hspace{21mm}
+\omega\times((\partial_jA)(\partial_j\omega))
\Big].
\end{aligned}}
\]

Thus the angular normal meter is sourced only by

- Hodge-normal pressure action;
- square-anchor first-gradient carré geometry.

No higher local tensor species survives the compiler.

---

## 6. Full discriminant equation -- EXACT

From `NEO_GAIN_TO_DISCRIMINANT_COMPILER.md`,
\[
\boxed{
L\mathcal V
=g^2(A:H_0)-6r(A^2:H_0)
+\nu\mathcal C_{\mathcal V},
}
\]
where \(\mathcal C_{\mathcal V}\) is a first-gradient carré expression.

Again the restricted Riccati source is exactly absent.

Hence
\[
\boxed{
\text{both normal meters change only by Hodge + square action}.}
\]

---

## 7. Finite erasure action for the angular branch -- ACTION IDENTITY

Suppose a finite lagged Type-I causal region contains a positive-volume set with
\[
|\mathcal J|\ge\varepsilon_J>0
\]
and the scalar adjoint kernel obeys a positive lower bound there.  Fubini produces a time \(s_*<0\) such that
\[
H_J(s_*)
:=\int\Gamma(0,0;y,s_*)|\mathcal J(y,s_*)|^2dy
\ge h_J>0.
\]

At a terminal G3 contact,
\[
\mathcal J(0,0)=0.
\]
Since
\[
L|\mathcal J|^2
=2\mathcal J\cdot L\mathcal J
-2\nu|\nabla\mathcal J|^2,
\]
the finite-time Duhamel formula yields
\[
\boxed{
\int_{s_*}^{0}\!\int
\Gamma\left[
\nu|\nabla\mathcal J|^2
-\mathcal J\cdot L\mathcal J
\right]
=\frac12H_J(s_*)
\ge\frac12h_J.
}
\]

Thus the angular defect also has a definite **finite normal-erasure action**.

Because \(L\mathcal J\) has only Hodge and square sources, no part of this payment can be assigned to the restricted Riccati backbone.

---

## 8. Unified Type-I normal-action split -- CONDITIONAL DEDUCTION

The sibling positive-gain theorem plus `NEO_GAIN_TO_DISCRIMINANT_COMPILER.md` gives on a fixed positive fraction of the causal under-gain geometry
\[
|\mathcal J|\ge c_J
\quad\vee\quad
|\mathcal V|\ge c_V,
\]
because \(|\mathcal J|=\rho^2|b|\) and \(\rho\) is bounded below on the causal production class.

Therefore a terminal G3 contact must pay at least one of two finite erasure actions:
\[
\boxed{
\mathscr A_J>0
\quad\vee\quad
\mathscr A_V>0.
}
\]

Both actions are sourced exclusively by Hodge and square geometry after restricted-Riccati cancellation.

This compresses the Type-I compatibility problem to
\[
\boxed{
\text{Can the admissible Type-I Hodge/square ledger pay the compulsory }
(\mathcal J,\mathcal V)\text{ normal-erasure action?}
}
\]

That is substantially sharper than asking whether some off-involution point exists.

---

## 9. Relation to the three-dimensional normal bundle -- INTERPRETATION

Near G3, \(\mathcal J\) reads the two angular normal directions linearly:
\[
\mathcal J=\rho^2n\times b.
\]
The discriminant reads the remaining repeated-spectrum departure at higher algebraic order; its first variation vanishes on the trace-free G3 sheet, reflecting the familiar quadratic vanishing of a polynomial discriminant at eigenvalue collision.

Thus \((\mathcal J,\mathcal V)\) should be regarded as a pair of **normal action meters**, not a smooth coordinate chart.

The minimal pair \((b,\delta)\) remains the right local coordinate system.  The polynomial pair \((\mathcal J,\mathcal V)\) is the right restricted-dynamics quotient for propagation.

This distinction is quintessentially NEO:
\[
\boxed{
\text{one geometry can need different renderers for local classification and causal action}.}
\]

---

## 10. Next theorem target -- OPEN

A useful closing theorem would show that at least one of
\[
\mathscr A_J,\qquad\mathscr A_V
\]
forces a definite amount of an already-owned positive quantity, preferably
\[
\nu\mathsf D+\mathsf J_{causal}
\]
or a Type-I Hodge companion norm.

Do not search for another Riccati defect before exhausting this pair.  The coherent self-dynamics has already been factored out exactly.
