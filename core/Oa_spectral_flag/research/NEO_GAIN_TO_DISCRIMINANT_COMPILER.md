# NEO Gain-to-Discriminant Compiler
## Convert compulsory positive radial under-gain into angular action or pure Hodge/heat spectral-shape action

**Purpose.** The Type-I sibling programme now supplies a finite Green-visible region with
\[
\delta=6a^2-g\ge\delta_+>0.
\]
The local Riccati audit shows that \(\delta\) itself is a poor propagation scalar: restricted Riccati dynamics damps it and the parabolic carré term has no sign.  This note compiles positive under-gain into two smaller owner classes:

1. angular defect \(b\), already owned by the vector/direction causal action;
2. velocity-gradient discriminant \(\mathcal V\), whose restricted Riccati contribution cancels identically, so any change is Hodge/heat-owned.

No new primitive is introduced.  Both are polynomial or curl-frame renderers of \(\nabla U\) and \(CU\).

Labels: **EXACT**, **CONDITIONAL TYPE-I DEDUCTION**, **AUDIT**, **OPEN**.

---

## 0. Invariants and minimal defects

Let
\[
g=\operatorname{tr}(A^2),
\qquad
r=\operatorname{tr}(A^3),
\]
and define the classical trace-free cubic discriminant renderer
\[
\boxed{
\mathcal V
:=r^2-\frac16g^3.
}
\]

On the curl-active set write
\[
Sn=an+b,
\qquad
\delta=6a^2-g.
\]
The exact cubic curl-frame factorization is
\[
r=-6a^3+\frac92a|b|^2+3b\cdot Db+\frac32a\delta.
\]

When \(b=0\),
\[
\boxed{
\mathcal V
=\frac1{12}\delta^2(2\delta-9a^2).
}
\]

Hence on the aligned set \(b=0\), zero discriminant means exactly
\[
\boxed{
\delta=0
\quad\vee\quad
\delta=\frac92a^2.
}
\]
The first branch is G3.  The second is the opposite repeated-eigenvalue branch.

---

## 1. The opposite aligned discriminant branch is spatially thin in the Type-I class -- CONDITIONAL TYPE-I DEDUCTION

Assume the Type-I terminal class has the two inputs already proved in the sibling rigidity worktree:

1. spatial real analyticity on each interior time slice;
2. one-sign Hodge rigidity
\[
g\ge0\text{ globally on a time slice}\Longrightarrow g\equiv0.
\]

Consider the exact aligned opposite branch on a set of positive spatial measure:
\[
b=0,
\qquad
\delta=\frac92a^2>0.
\]
Then
\[
g=6a^2-\delta=\frac32a^2.
\]
On \(\rho>0\), this relation is polynomialized by
\[
\boxed{
\Psi_-
:=2g|\omega|^4-3(\omega\cdot S\omega)^2=0.
}
\]

If the branch has positive measure, analyticity forces
\[
\Psi_-\equiv0
\]
on the whole slice.  Wherever \(\rho>0\),
\[
g=\frac32a^2\ge0.
\]
Where \(\rho=0\),
\[
g=|S|^2\ge0.
\]
Thus
\[
g\ge0\quad\text{globally}.
\]
The Type-I one-sign Hodge theorem gives \(g\equiv0\), contradicting \(\delta>0\) on the original positive-measure branch.

Therefore
\[
\boxed{
|\{b=0,\ \mathcal V=0,\ \delta>0\}|=0
}
\]
on every interior Type-I time slice.

This is not a new global regularity statement.  It is a zero-set exclusion inside the already-licensed Type-I class.

---

## 2. Quantitative gain-to-normal split -- CONDITIONAL COMPACTNESS DEDUCTION

Assume in addition the normalized Type-I class is locally smoothly compact, and suppose a fixed finite box contains a set \(E\) of positive volume on which
\[
\rho\ge\rho_+>0,
\qquad
\delta\ge\delta_+>0.
\]

Then there exist constants
\[
\varepsilon_N>0,
\qquad
\vartheta_N>0
\]
depending only on the normalized Type-I class and the positive-gain box data such that on a fixed positive fraction of \(E\),
\[
\boxed{
|b|\ge\varepsilon_N
\quad\vee\quad
|\mathcal V|\ge\varepsilon_N.
}
\]

### Compactness proof schema

If no such constants existed, take a sequence for which
\[
|b_k|+|\mathcal V_k|\to0
\]
on an asymptotically full fraction of the positive-\(\delta\) set.  Local smooth compactness gives a limit with, on a positive spacetime-measure set,
\[
\delta_\infty\ge\delta_+,
\qquad
b_\infty=0,
\qquad
\mathcal V_\infty=0.
\]
Fubini gives a time slice with positive spatial measure.  Section 0 then forces
\[
\delta_\infty=\frac92a_\infty^2>0
\]
on that set, contradicting Section 1.

Thus compulsory positive radial under-gain cannot remain simultaneously angularly coherent and arbitrarily close to the zero-discriminant gradient spectrum on almost all of its Green-visible region.

---

## 3. Angular branch is already causally owned -- DEDUCTION

On \(\rho\ge\rho_+\), a definite \(|b|\) lower bound is not a new species.

The direction-source compiler gives
\[
b=D_tn-\nu\mathcal K_n,
\]
so
\[
|b|\ge\varepsilon_N
\]
forces physical-time angular turning or square-angular curvature.

The Type-I vector causal inefficiency
\[
\mathfrak j
=\rho\sqrt{a^2+|b|^2}-\rho^2a
\]
also gives a quantitative positive cost from \(b\) whenever strain is uniformly bounded in the normalized class.

Therefore the `b` side of Section 2 is already owned by the existing vector causal action.  No angular descendant is needed.

---

## 4. Discriminant has no restricted-Riccati source -- EXACT

For full Navier--Stokes,
\[
D_tA=-A^2-H_0+\frac g3I+\nu\Delta A.
\]
The two scalar invariants satisfy
\[
\boxed{
D_tg
=-2r-2A:H_0+2\nu\operatorname{tr}(A\Delta A),
}
\]
\[
\boxed{
D_tr
=-\frac12g^2-3A^2:H_0
+3\nu\operatorname{tr}(A^2\Delta A).
}
\]
Therefore
\[
\boxed{
\begin{aligned}
D_t\mathcal V
={}&g^2(A:H_0)-6r(A^2:H_0)\\
&+\nu\Big[
6r\operatorname{tr}(A^2\Delta A)
-g^2\operatorname{tr}(A\Delta A)
\Big].
\end{aligned}}
\]

The restricted/local Riccati terms cancel exactly.

Thus \(\mathcal V\) is a canonical **normal-action meter** for gradient spectral shape:
\[
\boxed{
\text{restricted Riccati self-dynamics does not change }\mathcal V.
}
\]
Any material change in \(\mathcal V\) is owned by Hodge pressure or the square anchor.

This is stronger for propagation bookkeeping than \(\delta\), whose own equation contains the internal damping term \(-a\delta\).

---

## 5. Parabolic discriminant equation -- EXACT

Let
\[
L=D_t-\nu\Delta.
\]
Then
\[
Lg=-2r-2A:H_0
-2\nu\sum_j\operatorname{tr}((\partial_jA)^2),
\]
while
\[
Lr=-\frac12g^2-3A^2:H_0
-6\nu\sum_j\operatorname{tr}\big(A(\partial_jA)^2\big).
\]
Applying the scalar chain rule gives
\[
\boxed{
L\mathcal V
=g^2(A:H_0)-6r(A^2:H_0)
+\nu\mathcal C_{\mathcal V},
}
\]
where
\[
\boxed{
\begin{aligned}
\mathcal C_{\mathcal V}
={}&-12r\sum_j\operatorname{tr}\big(A(\partial_jA)^2\big)
+g^2\sum_j\operatorname{tr}((\partial_jA)^2)\\
&-2|\nabla r|^2
+g|\nabla g|^2.
\end{aligned}}
\]

Again, all explicit second derivatives cancel.  The price is an indefinite first-gradient carré term.

---

## 6. The discriminant is an action meter, not a scalar barrier -- AUDIT / NO-GO

At exact G3,
\[
A^2=-aA+2a^2I,
\qquad
g=6a^2,
\qquad
r=-6a^3.
\]
The Hodge coefficient in Section 5 vanishes at the exact sheet because
\[
g^2A-6rA^2
=36a^3(aA+A^2)
=72a^5I,
\]
and \(H_0\) is trace free.

However the carré term has no fixed sign on physical second velocity jets.  `audits/neo_discriminant_action.py` gives Hessian-compatible divergence-free examples at \(a=1/3,\rho=1\) with
\[
\boxed{
\mathcal C_{\mathcal V}
=\frac{2}{3}(38-13\sqrt2)>0
}
\]
and
\[
\boxed{
\mathcal C_{\mathcal V}
=-\frac{13+12\sqrt2}{6}<0.
}
\]

Therefore \(\mathcal V\) is not a maximum-principle barrier either.

Its advantage is different and more precise:

> unlike \(\delta\), its local Riccati self-dynamics has been removed exactly.  Every change is Hodge/square normal action.

---

## 7. New compatibility compression -- DEDUCTION

Combining the sibling causal-gain input with Sections 2--6 gives the branch-local finite split
\[
\boxed{
\mathrm{CG}^+
\Longrightarrow
\mathrm{ANG}
\quad\vee\quad
\mathrm{DISC},
}
\]
where

- `ANG`: a Green-visible region carries definite angular defect \(b\), already charged by the vector/direction causal action;
- `DISC`: a Green-visible region carries definite \(|\mathcal V|\), and any evolution of that gradient spectral-shape defect is purely Hodge/square-owned after restricted Riccati cancellation.

This is a real reduction of the Type-I compatibility problem.  The unknown part is no longer arbitrary positive \(\delta\).  It is a pure normal-action problem for the discriminant branch after the angular part has been stripped away.

---

## 8. What remains open

The following are **not** proved:

1. a sign for \(L\mathcal V\);
2. an ancient-time summable discriminant budget;
3. an upper bound forcing the Green-visible discriminant action to contradict Type-I;
4. a theorem that `DISC` is regularizing.

The next useful attack is instead:
\[
\boxed{
\text{can the Hodge/square action required to erase a finite-lag }\mathcal V\text{ defect}
}
\]
\[
\boxed{
\text{be paired with the already-owned vector heat cost or Type-I Hodge companion law?}
}
\]

That is a coupling problem between two existing causal coordinates, not a request for another local tensor.
