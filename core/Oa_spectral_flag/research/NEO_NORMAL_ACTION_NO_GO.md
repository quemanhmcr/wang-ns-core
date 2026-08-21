# NEO Normal-Action No-Go and Adjoint Balance Template
## Why a squared distance-to-terminal-sheet is the wrong scalar barrier

**Purpose.** Record a generic parabolic obstruction that applies before any expensive Riccati defect computation.  A nonnegative squared local distance to a terminal manifold usually has the wrong diffusion sign for backward rigidity from a single zero.  The correct object is an action balance that explicitly charges normal forcing and defect-gradient dissipation.

Labels: **EXACT**, **ANTI-MODEL**, **DEDUCTION**, **PROGRAM**.

---

## 1. Generic square identity -- EXACT

Let
\[
L=\partial_t+U\cdot\nabla-\nu\Delta
\]
and let \(F\) be any smooth vector/tensor defect.  Then
\[
\boxed{
L|F|^2
=2F:LF-2\nu|\nabla F|^2.
}
\]

At a zero of the defect,
\[
F(z_0)=0,
\]
one has
\[
\boxed{
L|F|^2(z_0)
=-2\nu|\nabla F(z_0)|^2\le0.
}
\]

Thus a generic squared distance to a terminal sheet is naturally a **subsolution at its zero set**, not the nonnegative supersolution required for a strong-minimum backward-rigidity argument.

---

## 2. Local anti-model -- ANTI-MODEL

Even for the pure heat operator, take locally
\[
F(x,t)=x_1.
\]
Then
\[
(\partial_t-\nu\Delta)F=0,
\]
but
\[
\Phi=F^2=x_1^2\ge0
\]
vanishes on the plane \(x_1=0\) while
\[
(\partial_t-\nu\Delta)\Phi=-2\nu<0.
\]

Therefore a local zero of a nonnegative defect square carries no backward uniqueness by itself.  Diffusion can maintain an exact zero while the defect is nonzero arbitrarily nearby.

This anti-model is intentionally elementary: it kills the proof architecture before any Navier--Stokes-specific complication is introduced.

---

## 3. Consequence for Riccati barrier search -- DEDUCTION

Candidates such as
\[
|b|^2+\delta^2,
\qquad
|\mathcal E_\lambda|^2,
\qquad
|\omega\times S\omega|^2+\Phi_{gain}^2
\]
all inherit the same structural diffusion term.

A theorem of the schematic form
\[
L\Phi\ge-C\Phi,
\qquad
\Phi\ge0,
\qquad
\Phi(0,0)=0
\]
cannot hold for a generic local squared distance unless additional equations force \(\nabla F=0\) on the zero set or a compensating positive source dominates the square-gradient loss.

Hence low-degree scalar barrier search must not be the default Type-I strategy.

---

## 4. Correct linear-system template -- EXACT

Suppose instead the defect satisfies a genuine parabolic system
\[
\boxed{LF=MF+G,}
\]
where

- \(M\) is the internal linearized geometry, including Riccati attraction;
- \(G\) is external normal Hodge/square forcing.

Then
\[
\boxed{
L|F|^2
=F:(M+M^*)F+2F:G-2\nu|\nabla F|^2.
}
\]

Let \(\Gamma(z_0;z)\) be the positive adjoint kernel of the scalar drift operator.  On a finite backward slab, formal adjoint integration gives
\[
\boxed{
\begin{aligned}
|F(z_0)|^2
={}&\int\Gamma(z_0;y,-T)|F(y,-T)|^2dy\\
&+\int_{-T}^{0}\!\int\Gamma\,
F:(M+M^*)F\\
&+2\int_{-T}^{0}\!\int\Gamma\,F:G\\
&-2\nu\int_{-T}^{0}\!\int\Gamma|\nabla F|^2.
\end{aligned}}
\]
whenever the integrations are licensed.

This is the right causal object: a **normal-action balance**.

---

## 5. What a terminal zero really demands -- DEDUCTION

If
\[
F(z_0)=0
\]
but the past contains definite defect mass, then the identity of Section 4 says that the past defect must be removed by a combination of

1. internal attracting drift \(M+M^*\);
2. normal forcing work \(F:G\);
3. defect-gradient dissipation.

For the G3 normal variables, Section `NEO_RICCATI_NORMAL_ATTRACTION.md` shows that the first item is already negative in the extensional directions:
\[
-2a,-2a,-a.
\]
Therefore a proof cannot count all decay of the defect as an anomalous cost.  Some decay is the legal local Riccati dynamics.

The useful remainder is the part that cannot be supplied by bounded internal attraction over the available finite causal lag.

---

## 6. Finite-lag principle -- PROGRAM

On a normalized Type-I causal box all first derivatives are uniformly bounded and the lag from the compulsory producer to the terminal contact is finite.

For a scalar ODE
\[
f'=-Kf,
\qquad K<\infty,
\]
nonzero \(f\) cannot reach exact zero in finite time.  The same elementary fact motivates the PDE target:

> after factoring the bounded internally attracting Riccati propagator, quantify the amount of Hodge/square forcing or defect diffusion required to turn a definite finite-lag defect region into an exact terminal zero.

The PDE difficulty is precisely that diffusion allows spatial defect mass to move and cancel at a point.  That is why the action balance must retain the gradient term instead of hiding it in a maximum-principle slogan.

---

## 7. Interaction with the vector causal identity -- DEDUCTION

The existing Type-I vector causal identity already provides a nonnegative square-anchor action
\[
\nu\int\Gamma|\nabla\omega|^2
\]
and a nonnegative source/state incoherence action.

The normal-action programme should try to show that erasing the compulsory positive radial under-gain requires a definite portion of exactly those already-owned actions, or of a Hodge-normal action that can be reconstructed from the same state.

If successful, the two currently separate Type-I facts
\[
\mathrm{CV}
\qquad\text{and}\qquad
\mathrm{CG}^+
\]
would become coupled rather than merely simultaneous.

---

## 8. Stop condition -- PROGRAM

Do not promote a new scalar defect because its zero set is prettier.

A candidate is useful only if at least one holds:

- its parabolic system closes with controlled coefficients;
- its adjoint action has a coercive coupling to an already-owned finite quantity;
- its diffusion term can be related to the existing vector heat cost;
- its terminal zero is thick enough for a genuine backward-uniqueness theorem, not just a point zero.

Otherwise the squared-distance route is structurally blocked.
