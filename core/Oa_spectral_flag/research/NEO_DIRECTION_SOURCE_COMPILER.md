# NEO Vorticity-Direction Source Compiler
## The angular defect is exactly the source of transported harmonic-map heat motion

**Purpose.** Compile the angular part of vorticity dynamics directly from the existing curl anchor.  The goal is not a new vorticity-direction mechanism.  It is to show that the minimal tangent defect
\[
b=P_{n^\perp}Sn
\]
is exactly the source term for the direction field once radial amplitude and the square anchor are separated.

Labels: **EXACT**, **DEDUCTION**, **TYPE RULE**, **LITERATURE CHECK**, **OPEN**.

---

## 0. Polar vorticity variables

On the curl-active set write
\[
\omega=\rho n,
\qquad
\rho=|\omega|>0,
\qquad
|n|=1.
\]
The vorticity equation is
\[
D_t\omega=S\omega+\nu\Delta\omega.
\]
Decompose
\[
Sn=an+b,
\qquad b\perp n.
\]

---

## 1. Exact radial equation -- EXACT

Using
\[
\Delta(\rho n)
=n\Delta\rho+2\nabla\rho\cdot\nabla n+\rho\Delta n
\]
and
\[
n\cdot\Delta n=-|\nabla n|^2,
\]
the radial projection gives
\[
\boxed{
(D_t-\nu\Delta)\rho
=a\rho-\nu\rho|\nabla n|^2.
}
\]

Equivalently,
\[
\boxed{
(D_t-\nu\Delta)\log\rho
=a-\nu|\nabla n|^2+\nu|\nabla\log\rho|^2.
}
\]

The scalar curl-amplitude law becomes the exact polar split
\[
\boxed{
(D_t-\nu\Delta)\frac{\rho^2}{2}
=\rho^2a
-\nu|\nabla\rho|^2
-\nu\rho^2|\nabla n|^2.
}
\]
Thus the familiar heat loss
\[
\nu|\nabla\omega|^2
\]
is already exactly
\[
\boxed{
\nu|\nabla\rho|^2
+\nu\rho^2|\nabla n|^2.
}
\]
It has a radial-amplitude face and an angular-direction face.

---

## 2. Exact angular equation -- EXACT

The tangential projection gives
\[
D_tn
=b+\frac\nu\rho P\Delta\omega.
\]
Since
\[
\frac1\rho P\Delta\omega
=P\Delta n+2\nabla\log\rho\cdot\nabla n
\]
and
\[
P\Delta n=\Delta n+|\nabla n|^2n,
\]
one obtains
\[
\boxed{
D_tn
-\nu\big(\Delta n+|\nabla n|^2n\big)
-2\nu\nabla\log\rho\cdot\nabla n
=b.
}
\]

Every term is tangent to the sphere.  Equivalently, with
\[
\mathscr L_\rho
:=D_t-\nu\Delta-2\nu\nabla\log\rho\cdot\nabla,
\]
\[
\boxed{
P\mathscr L_\rho n=b.
}
\]

This is the field-level form of the tangent contact-action identity.  The angular Riccati defect is exactly the source of a transported, amplitude-weighted harmonic-map heat equation for the vorticity direction.

No new primitive has appeared: \(n\) is the polar renderer of \(Cu\), and every square term comes from \(C^2\).

---

## 3. Positive-production boxes are legally curl-active -- DEDUCTION

On a Type-I causal production box one has
\[
\mathcal P_\omega
=\rho^2a-\nu|\nabla\omega|^2
\ge p_0>0.
\]
Therefore
\[
a\ge p_0
\]
under the normalization \(\rho\le1\).  If \(|S|\le K_A\), then
\[
\rho^2K_A\ge\rho^2a\ge p_0,
\]
so
\[
\boxed{\rho\ge\rho_0=(p_0/K_A)^{1/2}>0.}
\]

Hence \(n\), \(\nabla\log\rho\), and the angular equation of Section 2 are uniformly legal on the entire canonical production box.  There is no curl-zero seam there.

---

## 4. Finite angular ownership split -- EXACT / DEDUCTION

Define the square-angular renderer
\[
\mathcal K_n
:=P\Delta n+2\nabla\log\rho\cdot\nabla n
=\frac1\rho P\Delta\omega.
\]
Then
\[
\boxed{b=D_tn-\nu\mathcal K_n.}
\]

Consequently, at any point,
\[
|b|\ge\beta
\]
forces
\[
\boxed{
|D_tn|\ge\frac\beta2
\quad\vee\quad
\nu|\mathcal K_n|\ge\frac\beta2.
}
\]

This is the complete first-order angular owner split:

- **AT:** physical-time turning of the curl direction;
- **AH:** square-anchor angular curvature/inhomogeneity.

There is no third angular owner at this order.

---

## 5. The vector causal cost is already polar -- EXACT / DEDUCTION

For
\[
F=S\omega=\rho(an+b),
\]
the existing vector causal programme uses
\[
\mathfrak j=|F|-\omega\cdot F.
\]
In polar variables
\[
\boxed{
\mathfrak j
=\rho\sqrt{a^2+|b|^2}-\rho^2a.
}
\]

The kernel-weighted heat cost also splits exactly:
\[
\boxed{
\int\Gamma|\nabla\omega|^2
=
\int\Gamma|\nabla\rho|^2
+
\int\Gamma\rho^2|\nabla n|^2.
}
\]

Thus the exact causal coherence cost
\[
\nu\mathsf D+\mathsf J\ge\frac12
\]
is already a polar NEO action.  It charges only existing failures:

- radial curl-amplitude variation;
- angular direction variation;
- angular source tilt \(b\);
- amplitude deficit/compression encoded in \(\mathfrak j\).

This is a stronger reason not to invent another angular tensor descendant.

---

## 6. Canonical nesting preserves the direction equation -- EXACT

Under the Euler-degenerating normalized equation
\[
V_s=P[X_V,C]V-\mu C^2V
\]
and the exact Galilean nested field
\[
W(z,s)=\mu^{-1/2}\big(V(ds+\sqrt\mu z,s)-d\big),
\]
one has at corresponding points
\[
CW=CV,
\qquad
S_W=S_V.
\]
Therefore
\[
\rho_W=\rho_V,
\qquad
n_W=n_V,
\qquad
a_W=a_V,
\qquad
b_W=b_V.
\]

Moreover
\[
D_t^W n_W=D_t^Vn_V,
\]
while
\[
\Delta_z n_W=\mu\Delta_y n_V.
\]
The unit square coefficient of the nested field therefore exactly reproduces the outer coefficient \(\mu\).  Hence the direction-source equation commutes with canonical nesting.

**DEDUCTION.** Macro Euler degeneration does not create a new angular species.  Any angular activity invisible in the macro topology reappears at the canonical square-restoring NS layer with the same local contact coordinates.

---

## 7. Relation to geometric regularity literature -- LITERATURE CHECK / TYPE RULE

Classical geometric regularity results show that sufficient coherence of the vorticity direction can prevent singularity.  This makes \(n\) a historically meaningful geometric reader.

However those theorems do **not** license the converse shortcut
\[
\text{one local event with large }\nabla n
\Rightarrow
\text{singularity contradiction}.
\]
Nor do they automatically apply to an ancient terminal profile without checking their exact global/local hypotheses and scales.

NEO should therefore use the literature only as evidence that angular coherence is a high-value renderer.  The branch-local job is more precise: determine whether the compulsory causal/record geometry forces a coherence condition or an incoherence cost at the exact scale where an established criterion is legal.

---

## 8. Research consequence -- DEDUCTION

The Type-I causal programme now has a clean angular interpretation:

- if a compulsory defect region carries substantial \(b\), it must pay AT or AH;
- if it does not carry substantial \(b\), the remaining incompatibility is genuinely radial/Hodge and is represented by \(\delta\), not by an unnamed angular effect.

The endpoint-first programme has the same split at record scale:

- micro-circulation persistence is angularly coherent ownership;
- angular decoherence saturates the square-gradient scale;
- large remote strain enters the core only through the affine companion matrix.

These are not parallel mechanisms.  They are different scale renderings of the same tangent equation.

---

## 9. Next theorem target -- OPEN

A useful theorem must consume one of the two angular owners:
\[
\boxed{AT\vee AH.}
\]
Examples of legitimate targets are:

1. prove that persistent AT on a saturated/record-flat terminal class forces a forbidden time-visible branch;
2. prove that AH at the canonical micro radius forces a compactness-stable circulation or geometric-depletion condition;
3. derive an adjoint/vector propagation identity in which \(b\) enters with a nonnegative or controllable action.

Another derivative of \(n\) is not progress unless it closes one of these arrows.
