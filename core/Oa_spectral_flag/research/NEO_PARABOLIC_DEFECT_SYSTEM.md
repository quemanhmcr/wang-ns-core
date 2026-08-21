# NEO Parabolic Minimal-Defect System
## Second derivatives cancel, but the surviving carré geometry has no scalar sign

**Purpose.** Upgrade the material Riccati-defect equations to the true drift-diffusion operator
\[
L=\partial_t+U\cdot\nabla-\nu\Delta.
\]
The useful fact is that explicit second derivatives cancel from the principal defect equations.  The bad fact is equally important: the resulting first-gradient carré terms are sign-indefinite even on physically admissible second velocity jets.  Therefore neither \(|b|^2\) nor \(\delta\) supplies a free scalar maximum-principle barrier.

Labels: **EXACT**, **AUDIT**, **NO-GO**, **PROGRAM**.

---

## 0. Curl-frame notation

On \(\rho=|\omega|>0\), write
\[
\omega=\rho n,
\qquad
Sn=an+b,
\qquad b\perp n,
\]
and
\[
S=a\,n\otimes n+n\otimes b+b\otimes n-\frac a2P+D.
\]
Put
\[
H_0=\nabla^2p+\frac g3I,
\qquad
r_j=\partial_j\log\rho.
\]

---

## 1. Tangent defect: second-order cancellation -- EXACT

From `NEO_RICCATI_NORMAL_ATTRACTION.md`,
\[
P D_tb
=-2ab-PH_0n
+\nu\left[P(\Delta S)n+\left(D-\frac32aP\right)h_\omega\right],
\]
where
\[
h_\omega=P\Delta n+2r_j\partial_jn.
\]

The product rule for \(b=Sn-an\) gives
\[
\begin{aligned}
P\Delta b
={}&P(\Delta S)n
+2P\big((\partial_jS)(\partial_jn)\big)\\
&+\left(D-\frac32aP\right)P\Delta n
-|\nabla n|^2b
-2(\partial_ja)(\partial_jn).
\end{aligned}
\]
Subtracting \(\nu P\Delta b\) cancels both \(P(\Delta S)n\) and the tangential \(P\Delta n\) term.  Hence
\[
\boxed{
\begin{aligned}
P Lb
={}&-2ab-PH_0n+\nu|\nabla n|^2b\\
&+2\nu\sum_j\Big[
(\partial_ja)(\partial_jn)
-P\big((\partial_jS)(\partial_jn)\big)\\
&\hspace{28mm}
+\left(D-\frac32aP\right)r_j\partial_jn
\Big].
\end{aligned}}
\]

This is a genuine parabolic closure at **first spatial-gradient level** plus the existing Hodge-normal forcing.  No explicit \(\Delta S\), \(\Delta n\), or new second-jet field survives.

---

## 2. Squared tangent defect has the generic bad diffusion sign -- EXACT

Since \(b\) is tangent,
\[
b\cdot Lb=b\cdot PLb.
\]
Therefore
\[
\boxed{
L|b|^2
=2b\cdot PLb-2\nu|\nabla b|^2.
}
\]

At an exact G3 point, \(b=0\), so regardless of the Hodge value,
\[
\boxed{
L|b|^2=-2\nu|\nabla b|^2\le0.
}
\]

Thus \(|b|^2\) is not a nonnegative supersolution at its zero set unless the spatial defect gradient also vanishes.  A pointwise G3 condition gives no such gradient vanishing.

---

## 3. Radial gain: drift-diffusion equation -- EXACT

The scalar radial strain satisfies
\[
\boxed{
\begin{aligned}
La
={}&a^2+|b|^2-\frac\delta3-\tau\\
&+\nu\Big[
4r_j(\partial_jn\cdot b)
+2a|\nabla n|^2\\
&\hspace{15mm}
-4(\partial_jn)\cdot(\partial_jS)n
-2(\partial_jn)\cdot S(\partial_jn)
\Big].
\end{aligned}}
\]

For
\[
g=\operatorname{tr}(A^2),
\]
the matrix equation gives
\[
\boxed{
Lg
=-2\operatorname{tr}(A^3)-2S:H_0
-2\nu\sum_j\operatorname{tr}\big((\partial_jA)^2\big).
}
\]

Using
\[
\delta=6a^2-g
\]
and the cubic factorization yields
\[
\boxed{
L\delta
=21a|b|^2+6b\cdot Db-a\delta
-12a\tau+2S:H_0
+\nu\mathcal C_\delta,
}
\]
where the complete first-gradient carré term is
\[
\boxed{
\begin{aligned}
\mathcal C_\delta
={}&48a\sum_j r_j(\partial_jn\cdot b)
+24a^2|\nabla n|^2\\
&-48a\sum_j(\partial_jn)\cdot(\partial_jS)n\\
&-24a\sum_j(\partial_jn)\cdot S(\partial_jn)\\
&-12|\nabla a|^2
+2\sum_j\operatorname{tr}\big((\partial_jA)^2\big).
\end{aligned}}
\]

Equivalently,
\[
2\sum_j\operatorname{tr}((\partial_jA)^2)
=2|\nabla S|^2-|\nabla\omega|^2.
\]

Again, no explicit second spatial derivative survives.  The square anchor has compiled into a quadratic first-gradient form.

---

## 4. The carré term is sign-indefinite even at exact G3 -- AUDIT / NO-GO

At G3,
\[
b=0,\qquad\delta=0,
\]
but the second velocity jet remains free subject to its genuine compatibility conditions.

A physical second velocity jet is
\[
T_{ijk}=\partial_j\partial_kU_i,
\qquad T_{ijk}=T_{ikj},
\]
with differentiated incompressibility
\[
\sum_iT_{iik}=0.
\]
This space has dimension fifteen.

`audits/neo_parabolic_delta_carre.py` restricts \(\mathcal C_\delta\) to this exact physical jet space at the canonical G3 first jet \(a=1/3,\rho=1\).  It produces Hessian-compatible divergence-free examples with
\[
\boxed{
\mathcal C_\delta=36-24\sqrt2>0
}
\]
and another with
\[
\boxed{
\mathcal C_\delta=-96<0.
}
\]

Therefore
\[
\boxed{
\mathcal C_\delta\text{ has no algebraic sign even on exact G3 and physical second jets.}
}
\]

This is stronger than a random-matrix anti-test: the compatibility conditions of an actual velocity Hessian are enforced.

---

## 5. Consequence: scalar gain propagation is structurally blocked -- NO-GO

At an exact G3 point,
\[
L\delta
=-12a\tau+2S:H_0+\nu\mathcal C_\delta.
\]
The Hodge part has no fixed sign, and Section 4 shows the square/carré part has no fixed sign either.

Thus neither
\[
L\delta\ge-C|\delta|
\]
nor
\[
L\delta\le C|\delta|
\]
can follow from local algebra alone.

Likewise, squaring \(\delta\) only restores the generic negative gradient term described in `NEO_NORMAL_ACTION_NO_GO.md`.

Hence the positive causal under-gain theorem cannot be closed by a local scalar maximum principle for \(\delta\).

---

## 6. What the cancellation does buy -- DEDUCTION

The failure of sign is not failure of structure.

The parabolic compiler has reduced all explicit second derivatives to four already-owned categories:

\[
\boxed{
\begin{array}{ll}
\text{Riccati drift}:&-2ab,\ -a\delta+O(b^2),\\[1mm]
\text{Hodge normal}:&PH_0n,\ -12a\tau+2S:H_0,\\[1mm]
\text{angular/radial first gradients}:&\nabla n,\nabla a,\nabla S,\nabla\rho,\\[1mm]
\text{defect diffusion}:&-2\nu|\nabla b|^2\text{ after scalarization}.
\end{array}}
\]

No higher local tensor species is justified.

---

## 7. Interaction with existing causal costs -- PROGRAM

The vector causal identity already owns
\[
\nu\int\Gamma|\nabla\omega|^2.
\]
The polar compiler splits this into
\[
\nu\int\Gamma|\nabla\rho|^2
+\nu\int\Gamma\rho^2|\nabla n|^2.
\]

However \(\mathcal C_\delta\) also contains \(|\nabla S|^2\) and mixed strain-direction terms.  Therefore the present Type-I ledger does **not** yet obviously own the full square cost needed to erase radial gain defect.

This exposes the exact next analytic seam:
\[
\boxed{
\text{Can the Hodge/strain-gradient terms in }L\delta
\text{ be reduced to the existing vector heat cost,}
}
\]
\[
\boxed{
\text{or must they be controlled through pressure reconstruction / a first-gradient system estimate?}
}
\]

That is a concrete propagation question.  Differentiating \(\delta\) again would only manufacture an unowned higher-order cost.

---

## 8. Valid next routes -- PROGRAM

After this audit there are three plausible routes:

1. **vector system route:** propagate a coupled first-gradient state in which the indefinite pieces become a controlled matrix quadratic form;
2. **Hodge reconstruction route:** use \(g=-\Delta p\) and the exact trace-free Hessian reader to pair the Hodge term against the same adjoint kernel;
3. **terminal trace route:** obtain a thick zero/phase relation first, then apply an established backward-uniqueness/unique-continuation theorem with verified hypotheses.

The scalar-distance route is demoted.
