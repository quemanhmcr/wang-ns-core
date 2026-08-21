# NEO Record-Scale Renormalization Semigroup
## Every curl-normalized owner scale nests to the same canonical viscous record core

**Purpose.** Replace the vague slogan `no third physical scale' by an exact statement that is both stronger and safer: at a fixed vorticity record, all curl-normalized spatial microscopes form a one-parameter renormalization semigroup, and canonical square restoration from any larger scale lands on the **same** unit-square record-core field.

Intermediate physical scales may exist.  They do not create independent normalized core states.

Labels: **EXACT**, **DEDUCTION**, **PROVENANCE RULE**, **PROGRAM**.

---

## 0. Physical record data

Fix a spacetime record point \((x_0,t_0)\) with
\[
\Omega=|\omega(x_0,t_0)|>0,
\qquad \omega=Cu.
\]
Define the viscous record radius and velocity
\[
\boxed{
r_\nu=\sqrt{\nu/\Omega},
\qquad
U_\nu=\Omega r_\nu=\sqrt{\nu\Omega}.
}
\]

The natural vorticity time is
\[
\boxed{\tau_\omega=\Omega^{-1}.}
\]

---

## 1. Curl-normalized microscope at an arbitrary owner scale -- EXACT

For every spatial scale \(R>0\), define
\[
\boxed{
V_R(y,s)
=\frac{u(x_0+Ry,t_0+s/\Omega)}{\Omega R}.
}
\]
Then
\[
C_yV_R
=\frac{Cu}{\Omega},
\]
so the curl scale is order one independently of \(R\).

Direct substitution into Navier--Stokes gives
\[
\boxed{
\partial_sV_R
=P[X_{V_R},C_y]V_R
-\mu_R C_y^2V_R,
}
\]
with
\[
\boxed{
\mu_R
=\frac{\nu}{\Omega R^2}
=\left(\frac{r_\nu}{R}\right)^2.
}
\]

Thus changing the owner scale changes only the coefficient of the existing square anchor.  The normalized convective time remains exactly \(s=\Omega(t-t_0)\).

---

## 2. Exact scale-transfer operator -- EXACT

For two scales \(0<R_1<R_2\), define
\[
\boxed{
(\mathcal N_{R_1\leftarrow R_2}V)(z,s)
:=\frac{R_2}{R_1}
V\!\left(\frac{R_1}{R_2}z,s\right).
}
\]
Then direct substitution gives
\[
\boxed{
V_{R_1}
=\mathcal N_{R_1\leftarrow R_2}V_{R_2}.
}
\]

The transfer operators obey the exact semigroup/cocycle law
\[
\boxed{
\mathcal N_{R_0\leftarrow R_1}
\mathcal N_{R_1\leftarrow R_2}
=\mathcal N_{R_0\leftarrow R_2}
}
\]
for \(R_0<R_1<R_2\).

There is no approximation and no compactness argument here.  This is simply the exact scaling group restricted to the record-curl normalization.

---

## 3. Canonical square restoration lands on one field -- EXACT

At scale \(R\),
\[
\sqrt{\mu_R}=\frac{r_\nu}{R}.
\]
The canonical nested square-restoring field is
\[
W_R(z,s)
=\mu_R^{-1/2}
V_R(\sqrt{\mu_R}z,s).
\]
Using Section 1,
\[
\begin{aligned}
W_R(z,s)
&=\frac{R}{r_\nu}
\frac{u(x_0+r_\nu z,t_0+s/\Omega)}{\Omega R}\\
&=\frac{u(x_0+r_\nu z,t_0+s/\Omega)}{\Omega r_\nu}.
\end{aligned}
\]
Hence
\[
\boxed{
W_R=V_{r_\nu}
\quad\text{for every }R>0.
}
\]

This is the key identity.

Canonical nesting does not merely produce an isomorphic unit-viscosity problem.  At a fixed physical record it produces the **same normalized record-core state** from every outer owner scale.

---

## 4. Galilean-covariant version -- EXACT

Fix one physical constant frame \(c\in\mathbb R^3\).  Its exact Galilean representative at scale \(R\) is
\[
\boxed{
V_R^{\,c}(y,s)
=\frac{
 u(x_0+Ry+(c/\Omega)s,t_0+s/\Omega)-c
}{\Omega R}.
}
\]
The dimensionless frame is
\[
d_R=\frac{c}{\Omega R}.
\]

The same transfer law holds:
\[
\boxed{
V_{R_1}^{\,c}
=\mathcal N_{R_1\leftarrow R_2}V_{R_2}^{\,c}.
}
\]
In particular,
\[
\boxed{
\mu_R^{-1/2}V_R^{\,c}(\sqrt{\mu_R}z,s)
=V_{r_\nu}^{\,c}(z,s).
}
\]

The frame weights obey
\[
\boxed{
d_{R_1}=\frac{R_2}{R_1}d_{R_2}.}
\]

**PROVENANCE RULE.** If each scale chooses its own optimizing Galilean constant independently, exact scale coherence is lost only through that choice of representative.  The physical state has not created a new scale species; the frame selector has changed.  Any optimized-scale argument must therefore control the frame cocycle rather than invent a new terminal profile.

---

## 5. First-jet contact geometry is scale-invariant -- EXACT

At corresponding physical points,
\[
\boxed{
\nabla_yV_R=\frac{\nabla_xu}{\Omega},
\qquad
C_yV_R=\frac\omega\Omega,
\qquad
S[V_R]=\frac S\Omega.
}
\]
Therefore the entire normalized first jet is independent of \(R\).

In particular, the contact coordinates
\[
a/\Omega,\qquad b/\Omega,\qquad g/\Omega^2,
\]
and every algebraic first-jet normal form such as C0/C1, middle-eigenvalue sign, or Riccati shape are the **same species at every record owner scale**.

For the square-action coordinates,
\[
\mu_R\Delta_y(C_yV_R)
=\frac{\nu\Delta_x\omega}{\Omega^2},
\]
so the full contact-action prism is also scale-invariant.

Thus
\[
\boxed{
\text{changing }R
\text{ changes owner provenance and }\mu_R,
\text{ not local contact species}.}
\]

---

## 6. Circulation transfer is exact -- EXACT

Let \(\Gamma_z\) be a closed loop in the \(R_1\)-scale variables and let its image in the \(R_2\)-variables be
\[
\Gamma_y=(R_1/R_2)\Gamma_z.
\]
The scale-transfer law gives
\[
\boxed{
\oint_{\Gamma_y}V_{R_2}\cdot dy
=\left(\frac{R_1}{R_2}\right)^2
\oint_{\Gamma_z}V_{R_1}\cdot dz.
}
\]

Taking \(R_1=r_\nu\),
\[
\boxed{
\oint_{\Gamma_y}V_R\cdot dy
=\mu_R
\oint_{\Gamma_z}V_{r_\nu}\cdot dz.
}
\]
This is the earlier macro--micro circulation law, now seen as one instance of the exact record-scale semigroup.

---

## 7. Supporting-circulation radius cannot be subcanonical -- DEDUCTION FROM RECORD INPUT

Suppose the record circulation theorem supplies
\[
R_c\ge c\,r_\nu.
\]
At any outer scale \(R\), its dimensionless radius is
\[
\chi_R=R_c/R.
\]
Since
\[
\sqrt{\mu_R}=r_\nu/R,
\]
we get
\[
\boxed{
\chi_R\ge c\sqrt{\mu_R}.}
\]

Therefore circulation ownership cannot hide at a scale smaller than the canonical square-restoring radius inside **any** record-curl microscope.

This is an exact provenance comparison, not a claim that there are no physical structures between \(r_\nu\) and \(R\).

---

## 8. Corrected finite-scale principle -- DEDUCTION

The original `No Third Scale' slogan is too strong if read literally.  The owner cage may contain many physical intermediate radii
\[
r_\nu\ll R_1\ll R_2\ll\ell_E.
\]

The exact theorem is instead:
\[
\boxed{
\text{there is no third independent record-core normalization}.}
\]
Every such scale belongs to the same semigroup and nests to \(V_{r_\nu}\).

What can remain different across scales is only:

1. the observation window;
2. the square coefficient \(\mu_R\);
3. the Galilean representative;
4. the outer low-frequency/affine imprint seen inside the core.

Those are provenance parameters, not new PDE species.

---

## 9. Interaction with the affine companion principle -- DEDUCTION

For \(R\gg r_\nu\),
\[
\mu_R\ll1.
\]
The outer state becomes Euler-degenerate at its own scale, but Section 3 says its canonical square-restored descendant is still the same \(V_{r_\nu}\).

Meanwhile the endpoint-first affine companion theorem says that owner geometry separated from the core by a fixed large factor enters the inner field, to first order, only through a finite matrix
\[
B_Ly+O(L^{-1}).
\]

Thus the correct first-order terminal architecture is
\[
\boxed{
\text{one unit-square record core}
+
\text{one affine companion imprint},
}
\]
not an infinite sequence of intermediate normalized profiles.

The macro Euler fields at larger radii remain useful carriers of provenance and tightness.  They are not additional local contact species.

---

## 10. New Type-II target -- PROGRAM

After exact scale collapse, the genuine Type-II problem is no longer
\[
\text{which of infinitely many microscopes owns the singularity?}
\]
It is
\[
\boxed{
\text{can the one viscous record core decouple from its admissible affine/Euler companion provenance?}
}
\]

A theorem should therefore couple

- compactness-stable activity in the record core (circulation is the leading candidate);
- the finite affine companion matrix or macro Euler carrier;
- the finite-energy owner cage \(r_\nu\lesssim R\lesssim\ell_E\).

No additional microscope is justified unless it detects information that provably disappears from both the common core and the affine companion renderer.

---

## 11. Audit consequence

`audits/neo_record_scale_semigroup.py` verifies:

1. \(\mu_R=(r_\nu/R)^2\);
2. exact composition of scale transfers;
3. canonical nesting from every \(R\) lands on the same \(r_\nu\) field;
4. first-jet and square-action weights are invariant;
5. circulation transforms with area weight \((R_1/R_2)^2\).
