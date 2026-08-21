# NEO Provenance--Propagation Compiler
## Keep the curl-genetic core fixed; type how terminal information survives frame, scale, topology and causality

**Status:** research branch / candidate core extension.

This file does not enlarge the NEO primitive ontology.  The anchors remain
\[
\boxed{u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t.}
\]
The genetic Navier--Stokes equation remains
\[
\boxed{u_t=P[X_u,C]u-\nu C^2u.}
\]
The purpose of this module is different: reconstruction already tells us how many familiar NS objects descend from the same anchors.  The terminal programme now needs a compiler for the **survival and ownership** of those descendants under normalization, compactness and causal propagation.

The guiding distinction is
\[
\boxed{
\text{algebraic reconstructibility}
\neq
\text{terminal survivability}.
}
\]

---

## 1. Provenance type -- DEFINITION

For a terminal renderer \(Q[u]\), attach the provenance type
\[
\boxed{
\operatorname{ptype}(Q)
=(\mathfrak f,\mathfrak s,\mathfrak t,\mathfrak o),
}
\]
where:

1. \(\mathfrak f\) records frame behavior: absolute, Galilean invariant, or Galilean-quotiented;
2. \(\mathfrak s\) records the scale at which the renderer is normalized;
3. \(\mathfrak t\) records the topology in which it is stable under the extraction under consideration;
4. \(\mathfrak o\) records its owner: local contact, finite causal lag, separated companion scale, or nested micro-layer.

This tuple is metadata, not a new dynamical field.

**Protocol.** A terminal implication is legal only if every quantity used on the limiting object has a proved passage rule in the topology carried by its provenance type.

### Examples

- \(|Cu(0,0)|\): Galilean invariant and scale-local, but derivative-level point evaluation is not stable under state compactness below one full derivative.
- circulation \(\oint_\Gamma u\cdot d\ell\): Galilean invariant on a closed loop and potentially stable under strong local state convergence plus loop control.
- Galilean oscillation \(\inf_c\|u-c\|_{L^q(Q^c_r)}\): frame-quotiented and scale-local.
- a Type-I Duhamel source bubble: finite-lag causal owner, stable through the drift heat kernel once the kernel class is licensed.

The compiler must never silently replace one provenance type by another merely because the underlying algebraic object is the same.

---

## 2. The third compiler axis: square-anchor fate -- EXACT NORMALIZATION

Consider a space-time normalization
\[
V(y,s)=\frac1a\,u(x_0+\ell y,t_0+\tau s),
\qquad \tau=\frac\ell a.
\]
Then the normalized equation has the form
\[
\boxed{
V_s=P[X_V,C_y]V-\mu C_y^2V,
\qquad
\mu=\frac{\nu}{a\ell}.
}
\]
Thus the same square anchor has three terminal fates:
\[
\boxed{
\mu_k\to0,
\qquad
\mu_k\to\mu_*\in(0,\infty),
\qquad
\mu_k\to\infty.
}
\]
They correspond to Euler-degenerate, genuine parabolic, and square-dominated normalized equations.  These are not new mechanisms; they are three limits of the coefficient multiplying the existing anchor \(C^2\).

**Protocol.** Any terminal normal form must carry its square-anchor coefficient as part of its scale provenance.  Identities using viscous maximum principles, analyticity or parabolic smoothing cannot be transported into the \(\mu=0\) class without an independent argument.

---

## 3. Exact contact-action prism -- EXACT

Let
\[
\omega=Cu=\rho n,
\qquad \rho=|\omega|>0,
\qquad |n|=1.
\]
Write the strain action as
\[
Sn=an+b,
\qquad b=P_{n^\perp}Sn,
\qquad b\perp n.
\]
The vorticity equation is
\[
D_t\omega=S\omega+\nu\Delta\omega.
\]
Using
\[
D_t\omega=(D_t\rho)n+\rho D_tn,
\qquad n\cdot D_tn=0,
\]
its radial projection is
\[
\boxed{
D_t\rho=\rho a+\nu n\cdot\Delta\omega.
}
\]
Its tangential projection is
\[
\boxed{
\rho D_tn=\rho b+\nu P_{n^\perp}\Delta\omega.
}
\]
At a reference curl scale \(\Omega>0\), define dimensionless contact coordinates
\[
\alpha:=\frac a\Omega,
\qquad
\gamma:=\frac{D_t\rho}{\rho\Omega},
\qquad
\sigma:=-\frac{\nu n\cdot\Delta\omega}{\rho\Omega},
\]
\[
\beta:=\frac b\Omega,
\qquad
\theta:=\frac{D_tn}{\Omega},
\qquad
\kappa:=-\frac{\nu P_{n^\perp}\Delta\omega}{\rho\Omega}.
\]
Then
\[
\boxed{\alpha=\gamma+\sigma,}
\]
\[
\boxed{\beta=\theta+\kappa.}
\]
Equivalently,
\[
\boxed{
\frac{Sn}{\Omega}
=(\gamma+\sigma)n+(\theta+\kappa).
}
\]

This is the **contact-action prism**.  It is a renderer of the existing vorticity equation, not a new law.

### Interpretation

Radial strain action has only two owners:
\[
\boxed{
\text{radial stretching}
=\text{material amplitude growth}
+\text{square-anchor radial leakage}.
}
\]
Tangential strain action has only two owners:
\[
\boxed{
\text{angular strain action}
=\text{material direction turning}
+\text{square-anchor angular turning}.
}
\]
Thus record growth, viscous leakage, angular rotation and heat-induced turning are allocations of one first-jet action.  They should not be promoted to four independent mechanisms.

---

## 4. Finite owner alphabet -- CANDIDATE PRINCIPLE

The current terminal work suggests that an observable can fail to be locally owned in only a small number of structurally different ways:
\[
\boxed{
\mathsf O
\in
\{\mathrm{LOC},\ \mathrm{LAG},\ \mathrm{AFF},\ \mathrm{MIC}\}.
}
\]

- `LOC`: the normalized contact/core owns the quantity at the same scale and time.
- `LAG`: a finite backward causal region owns the terminal quantity through a propagator.
- `AFF`: a separated larger scale enters the core only through its finite affine first-jet imprint.
- `MIC`: a quantity lost by a macro topology reappears in the canonical nested micro-layer where the square anchor is restored.

This is an ownership alphabet, not a profile taxonomy.

**Candidate finite-ownership principle.** Before introducing a new terminal species, show that the obstruction cannot be represented by one of `LOC/LAG/AFF/MIC` using already-compiled anchors.

---

## 5. Propagation is a distinct compiler pass -- DEDUCTION

A higher derivative is legitimate only when it is used to propagate an already-owned defect, not merely to create a new local costume.

The required pattern is
\[
\boxed{
\text{existing defect }Z
\longmapsto
(\partial_t+D_u-\nu\Delta)Z
=\mathcal A Z+\mathcal F,
}
\]
followed by a propagation theorem for \(Z\) or a scalar renderer of \(Z\).

The anti-loop rule is therefore sharpened:

> Do not generate a new field because a local form survives.  First derive the propagation law of the smallest existing defect and test whether its owner can reach the terminal contact.

---

## 6. Scalar causal compiler -- STANDARD SCHEMA / DOMAIN DEPENDENT

Suppose an already-compiled scalar \(\Phi\) obeys
\[
L_u\Phi:=(\partial_t+u\cdot\nabla-\nu\Delta)\Phi=\mathcal S_\Phi.
\]
Whenever the drift class supplies a positive fundamental solution \(\Gamma\), one has schematically
\[
\boxed{
\Phi(z_0)
=\text{homogeneous memory}
+\iint\Gamma(z_0;z)\mathcal S_\Phi(z)\,dz.
}
\]
This converts a terminal value into an ownership statement about its causal source.

**Protocol.** The heat kernel is not a new NEO primitive.  It is an analytic propagation renderer whose use must be licensed by the drift class of the terminal object.

The Type-I positive-production representation is the model example: the source is already the vorticity-amplitude production
\[
\mathcal P_\omega
=\omega\cdot S\omega-\nu|\nabla\omega|^2.
\]
The next target is not another production descendant; it is a propagation bridge from a compulsory off-involution producer to terminal incompatibility.

---

## 7. Defect propagation target -- OPEN

For a C1 state, write
\[
a=n\cdot Sn,
\qquad
b=P_{n^\perp}Sn,
\qquad
g=\operatorname{tr}(\nabla u)^2,
\qquad
\delta=6a^2-g.
\]
On the positive-\(g\) C1 block, exact Riccati contact is represented by
\[
\boxed{b=0,\qquad\delta=0.}
\]
The research target is to find a polynomially typed scalar \(\Phi_{\rm Ric}\), vanishing exactly on the appropriate Riccati sheet, whose evolution has a sign/coercivity structure of the form
\[
\boxed{
L_u\Phi_{\rm Ric}
\ge c\,\mathfrak d_{\rm producer}
-C\Phi_{\rm Ric}-\mathcal E_{\rm owned},
}
\]
where \(\mathcal E_{\rm owned}\) is controlled by quantities already licensed in the terminal class.

No such inequality is claimed here.

### Falsification protocol

Before theorem work, candidate \(\Phi_{\rm Ric}\) must survive:

1. affine C0 rotating anti-models;
2. Burgers/Burgers-layer coherent profiles;
3. finite-Fourier G3/Hodge freedom tests;
4. heterochiral active states;
5. exact Riccati first-jet configurations with independently tunable higher data.

A failed low-degree scalar barrier is useful information: it means the terminal contradiction must use nonlocal scale ownership or a vector/system propagation theorem.

---

## 8. Canonical nested square restoration -- EXACT

For a normalized field
\[
V_s=P[X_V,C]V-\mu C^2V,
\qquad 0<\mu\ll1,
\]
introduce a constant Galilean frame \(d\).  The exact Galilean representative is
\[
\widetilde V(y,s):=V(y+ds,s)-d,
\]
which satisfies the same normalized Navier--Stokes equation.  Define the nested field
\[
\boxed{
W(z,s)=\mu^{-1/2}\widetilde V(\sqrt\mu z,s)
=\mu^{-1/2}\big(V(ds+\sqrt\mu z,s)-d\big).
}
\]
Then the spatial derivatives satisfy
\[
C_zW=C_yV(ds+\sqrt\mu z,s),
\]
and direct scaling gives
\[
\boxed{
W_s=P[X_W,C_z]W-C_z^2W.
}
\]
Thus the nested field has unit square-anchor coefficient.  The spatial Galilean tilt is essential; subtracting \(d\) without translating by \(ds\) would not preserve the equation.

Thus
\[
\boxed{
\text{macro }\mu\to0\text{ Euler degeneration}
\quad\leftrightarrow\quad
\text{micro radius }\sqrt\mu\text{ restoring }\mu=1.
}
\]
This is an exact two-scale consequence of the same anchor coefficient.

---

## 9. Finite two-scale closure target -- OPEN

The endpoint programme supplies a natural candidate scale renderer: a supporting circulation radius \(R_c\).  At record times the currently derived lower bound has the form
\[
R_c\gtrsim\sqrt{\nu/\Omega}.
\]
If the outer normalization has spatial scale \(\ell\), amplitude \(a\), and curl normalization \(a/\ell\sim\Omega\), then
\[
\mu=\frac{\nu}{a\ell}
=\frac{\nu}{\Omega\ell^2},
\]
so
\[
\boxed{
\frac{\sqrt{\nu/\Omega}}{\ell}=\sqrt\mu.
}
\]
Therefore the record circulation lower scale coincides with the canonical nested NS scale.

This motivates the **No Third Scale target**:
\[
\boxed{
\text{singular curl ownership at a record}
\Longrightarrow
\text{macro activity}
\ \vee\ 
\text{activity captured at the canonical }\sqrt\mu\text{ NS layer}.
}
\]
A proof would turn the Euler-degenerate terminal branch into a genuinely finite macro--micro problem.  No such theorem is claimed here.

---

## 10. Macro--micro no-decoupling target -- OPEN

The desired renderer \(Q\) should satisfy three conditions:

1. **provenance:** singular extraction forces \(Q\) to remain nontrivial at some physical scale;
2. **compactness:** \(Q\) passes either to the macro Euler state or to the nested NS microfield;
3. **finite split:** if the macro contribution vanishes, the micro contribution has a quantitative lower bound, and conversely.

The ideal statement is
\[
\boxed{
Q_{\rm singular}\ge c
\Longrightarrow
Q_{\rm macro}\ge c_1
\quad\vee\quad
Q_{\rm micro}\ge c_2.
}
\]
Circulation and Galilean oscillation are the first candidate renderers because they are less fragile than pointwise curl under derivative-losing compactness.

---

## 11. Endpoint defect coupling -- CANDIDATE PROGRAM

Finite energy and record analyticity already suggest that temporal record flatness and spatial macro--micro separation cannot degenerate independently.  NEO should search systematically for relations of the form
\[
\boxed{
\mathcal D_1\,\mathcal D_2\not\to0
\quad\text{or}\quad
\int \mathscr F(\mathcal D_1,\mathcal D_2)<\infty,
}
\]
where \(\mathcal D_j\) are dimensionless terminal defects such as record-growth rate, square-anchor coefficient, circulation concentration, or affine-owner size.

These are **endpoint defect coupling laws**.  Their purpose is to shrink the number of independent terminal escape axes, not to create new currencies.

---

## 12. Proposed terminal signature -- WORKING SYNTAX

A terminal object may be tracked by a finite signature
\[
\boxed{
\mathfrak T
=(\mu,\ \mathcal A,\ \mathcal R,\ \mathfrak d,\ \mathfrak o),
}
\]
where

- \(\mu\): square-anchor fate;
- \(\mathcal A\): licensed compactness-stable activity renderer;
- \(\mathcal R\): record-time class (growing, flat, eternal/saturated);
- \(\mathfrak d\): smallest local algebraic defect coordinates;
- \(\mathfrak o\): owner class `LOC/LAG/AFF/MIC`.

This signature is not asserted canonical.  Its purpose is to make illegal branch proliferation visible: a new branch is justified only if it changes one of these finite coordinates in a way not already rendered by the core.

---

## 13. Research priorities

1. **Causal defect propagation:** derive and adversarially test evolution laws for the minimal Riccati defects; search for a scalar/vector propagation theorem converting finite-lag quantitative off-involution production into terminal incompatibility.
2. **Contact-action prism:** use the exact radial/tangential allocation to merge record, C0/C1, heat, angular and Hodge escape branches before introducing any new jet.
3. **Finite two-scale closure:** prove or falsify the No Third Scale target using circulation or another compactness-stable curl renderer.
4. **Macro--micro no-decoupling:** force singular provenance to survive in the Euler macro state or the canonical nested NS layer.
5. **Endpoint defect coupling:** find inequalities showing time-flatness, square degeneration and owner separation cannot all degenerate independently.

---

## 14. Anti-loop rules

- Do not add a primitive because a renderer changes frame, tensor type, scale or topology.
- Do not use a pointwise derivative normalization as a compactness invariant without a proved derivative passage.
- Do not differentiate a surviving local normal form unless the derivative enters a propagation equation for an already-defined defect.
- Do not create an outer-profile hierarchy before proving the affine first-jet remainder is genuinely insufficient.
- Do not create a sub-micro hierarchy before disproving canonical \(\sqrt\mu\) square restoration as the unique needed nested scale.
- Do not sum finite causal bubbles over ancient time without a disjointness or recurrence theorem.

---

## 15. Success criterion for this compiler extension

The extension succeeds if it converts the current terminal programme from
\[
\text{many locally meaningful descendants}
\]
into
\[
\boxed{
\text{finite contact types}
\times
\text{finite owner types}
\times
\text{finite square-anchor fates},
}
\]
and every surviving combination is linked by a legal propagation theorem to either an already-excluded normal form or a contradiction.

The desired endpoint is not a larger NEO language.  It is a smaller hiding space for singularity.
