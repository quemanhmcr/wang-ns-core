# NEO Finite Discriminant-Erasure Action
## A Green-visible gradient-shape defect cannot disappear at a terminal G3 contact for free

**Purpose.** Convert the `DISC` branch of `NEO_GAIN_TO_DISCRIMINANT_COMPILER.md` into an exact finite-lag action identity.  The discriminant is not a scalar maximum-principle barrier, but that failure is useful: squaring it and integrating against the positive adjoint kernel turns disappearance of a finite past defect into an exact normal-action cost.

No ancient-time summation is used.  No new primitive is introduced.

Labels: **EXACT**, **CONDITIONAL TYPE-I DEDUCTION**, **ACTION IDENTITY**, **OPEN**.

---

## 0. Input contract

Work on a curl-normalized smooth bounded ancient Type-I profile in the class used by the sibling causal programme.  Let
\[
L=\partial_t+U\cdot\nabla-\nu\Delta
\]
and let
\[
\Gamma(0,0;y,s)>0
\]
be the scalar adjoint fundamental solution supplied by the Type-I drift class.

The velocity-gradient discriminant is
\[
\boxed{
\mathcal V
=r^2-\frac16g^3,
\qquad
g=\operatorname{tr}(A^2),
\qquad r=\operatorname{tr}(A^3).
}
\]

Assume the `DISC` output of the gain-to-discriminant compiler: in a finite lagged box
\[
\mathcal B\subset B_R\times[-T,-\delta_t],
\]
there is a measurable set \(E\subset\mathcal B\) with
\[
|E|\ge m_E>0,
\qquad
|\mathcal V|\ge\varepsilon_V>0
\quad\text{on }E,
\]
and
\[
\Gamma(0,0;y,s)\ge\gamma_*>0
\quad\text{on }\mathcal B.
\]

At the distinguished terminal contact assume exact G3, hence
\[
\boxed{\mathcal V(0,0)=0.}
\]

---

## 1. A positive weighted discriminant slice exists -- DEDUCTION

By Fubini there is a time
\[
s_*\in[-T,-\delta_t]
\]
for which the spatial section
\[
E_{s_*}=\{y:(y,s_*)\in E\}
\]
has a definite positive measure depending only on the finite box and \(m_E\).  Therefore
\[
\begin{aligned}
H_*
&:=\int_{\mathbb R^3}
\Gamma(0,0;y,s_*)\mathcal V(y,s_*)^2\,dy\\
&\ge
\int_{E_{s_*}}
\Gamma\mathcal V^2\,dy\\
&\ge
\gamma_*\varepsilon_V^2|E_{s_*}|.
\end{aligned}
\]
Thus
\[
\boxed{H_*\ge h_*>0.}
\]

This converts a positive-volume `DISC` region into a one-time scalar datum suitable for exact Duhamel propagation.  It does not choose or track a material particle.

---

## 2. Exact square identity -- EXACT

For every smooth scalar \(q\),
\[
L(q^2)=2qLq-2\nu|\nabla q|^2.
\]
Taking \(q=\mathcal V\),
\[
\boxed{
L(\mathcal V^2)
=2\mathcal V L\mathcal V
-2\nu|\nabla\mathcal V|^2.
}
\]

The terminal Duhamel formula from time \(s_*\) to time zero gives
\[
\mathcal V(0,0)^2
=H_*
+2\int_{s_*}^{0}\!\int
\Gamma\,
\left(
\mathcal V L\mathcal V
-\nu|\nabla\mathcal V|^2
\right)\,dy\,ds.
\]
Since \(\mathcal V(0,0)=0\),
\[
\boxed{
\int_{s_*}^{0}\!\int
\Gamma\left[
\nu|\nabla\mathcal V|^2
-\mathcal V L\mathcal V
\right]dy\,ds
=\frac12H_*.
}
\]
Consequently
\[
\boxed{
\int_{s_*}^{0}\!\int
\Gamma\left[
\nu|\nabla\mathcal V|^2
-\mathcal V L\mathcal V
\right]
\ge\frac12h_*>0.
}
\]

This is the **finite discriminant-erasure action**.

---

## 3. Why this is stronger than a scalar barrier attempt -- DEDUCTION

`NEO_GAIN_TO_DISCRIMINANT_COMPILER.md` shows
\[
L\mathcal V
=g^2(A:H_0)-6r(A^2:H_0)+\nu\mathcal C_{\mathcal V}.
\]
The restricted/local Riccati self-dynamics has cancelled exactly.

Therefore the erasure action contains no hidden payment by the internally attracting Riccati backbone:
\[
\boxed{
\begin{aligned}
\mathscr A_V
={}&\int\Gamma\nu|\nabla\mathcal V|^2\\
&-\int\Gamma\mathcal V
\big[g^2(A:H_0)-6r(A^2:H_0)\big]\\
&-\nu\int\Gamma\mathcal V\mathcal C_{\mathcal V}.
\end{aligned}}
\]
and
\[
\boxed{\mathscr A_V=H_*/2\ge h_*/2.}
\]

The lack of a sign for \(L\mathcal V\) is no longer an obstruction to writing an exact theorem.  It becomes the statement that the mandatory positive erasure cost may be distributed among:

1. discriminant-gradient diffusion;
2. Hodge-normal work;
3. square/carré work.

Those are already typed owners.

---

## 4. Finite-lag provenance matters -- DEDUCTION

The identity is deliberately finite in time.  It uses only the interval
\[
[s_*,0]
\]
with \(-s_*\) uniformly bounded above and below by the causal construction.

Hence no assumption of ancient-time integrability is needed, and no repeated-event wallet is created.  This avoids the historical mistake of trying to sum a local Type-I Morrey cost over all negative times.

The theorem says only:
\[
\boxed{
\text{a definite finite-lag gradient-shape defect}
\to
\text{a definite finite-lag normal erasure action}.}
\]

---

## 5. Gradient part does not automatically require a new budget -- DEDUCTION / PROGRAM

On a normalized Type-I class with a uniform first-jet bound
\[
|A|\le K_A,
\]
\(\mathcal V\) is a degree-six polynomial in \(A\).  Therefore
\[
\boxed{|
abla\mathcal V|
\le C(K_A)|\nabla A|.}
\]

For a divergence-free field, \(A=\nabla U\) and \(\omega=CU\) are first-order Hodge-equivalent.  On the whole space the unweighted Fourier symbols give the same homogeneous second-derivative size; locally, standard div--curl/interior estimates reduce \(\nabla A\) to \(\nabla\omega\) plus lower-order cutoff terms on an enlarged finite ball.

This suggests that the first positive term in \(\mathscr A_V\) may be reducible to the already-owned vector heat action
\[
\nu\int\Gamma|\nabla\omega|^2
\]
plus finite Type-I cutoff errors.

**OPEN.** The kernel-weighted local estimate must be proved with the actual Aronson weight; it is not licensed merely by the unweighted whole-space Fourier identity.

---

## 6. The Hodge term is a genuine owner -- AUDIT / NO CANCELLATION CLAIM

The Hodge work is
\[
\boxed{
\mathscr H_V
:=\int\Gamma\mathcal V
\big[g^2(A:H_0)-6r(A^2:H_0)\big].
}
\]
There is no algebraic reason for it to vanish.

The historical local theory already gives both signs for pressure action on gradient-shape variables.  A separate periodic finite-Fourier audit in `audits/neo_discriminant_hodge_no_cancel.py` also finds nonzero spatial averages of the unweighted Hodge source with both signs on smooth divergence-free states.

Thus pressure/Hodge cannot be silently deleted from the erasure ledger.

---

## 7. Exact G3 boundary degeneracy -- EXACT

At exact G3,
\[
A^2=-aA+2a^2I,
\quad g=6a^2,
\quad r=-6a^3.
\]
Then
\[
g^2A-6rA^2
=72a^5I.
\]
Since \(H_0\) is trace free,
\[
\boxed{
 g^2(A:H_0)-6r(A^2:H_0)=0
\quad\text{on exact G3}.}
\]

Thus Hodge does not change the scalar discriminant to first order **at the sheet itself**, even though it can steer the full tensor normal directions and can act on \(\mathcal V\) away from the sheet.

This is another reason the finite erasure problem is inherently nonlocal in spacetime: the required normal action is paid during approach, not by a pointwise terminal kick.

---

## 8. Coupling target -- OPEN

The sibling Type-I programme already owns
\[
\boxed{
\nu\mathsf D+\mathsf J\ge\frac12,
}
\]
with
\[
\mathsf D=\int\Gamma|\nabla\omega|^2
\]
and nonnegative source/state incoherence \(\mathsf J\).

The present compiler owns, on the `DISC` side,
\[
\boxed{\mathscr A_V\ge h_*/2.}
\]

The high-value theorem is now a **coupling theorem**, not another defect theorem:
\[
\boxed{
\text{does a definite discriminant-erasure action force a definite portion of}
\quad
\nu\mathsf D+\mathsf J
\quad\text{or a controlled Hodge action?}
}
\]

If yes, the two simultaneous causal facts cease to be parallel observations and become one constrained normal-action ledger.

---

## 9. Stop line

Do not differentiate \(\mathcal V\) again merely to make the action look more local.

The next useful work is one of:

1. kernel-weighted Hodge estimate for \(\nabla A\) versus \(\nabla\omega\);
2. a bound on \(\mathscr H_V\) through the Type-I pressure/Hodge ledger;
3. a stochastic/matrix propagator that absorbs bounded Riccati attraction and identifies the remaining normal work pathwise or in expectation.

Anything else risks recreating an unowned higher-derivative wallet.
