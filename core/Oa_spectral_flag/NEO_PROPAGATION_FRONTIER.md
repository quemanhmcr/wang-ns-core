# NEO Propagation Frontier
## Branch-local programme: make singular terminal geometry unable to hide across time, scale or compactness

**Branch:** `research/neo-provenance-propagation`

**Isolation contract:** this frontier is developed in its own worktree.  It does not modify, merge into, or push `main`.

---

## 1. Core remains frozen

The primitive anchors remain
\[
\boxed{u(t),\ P,\ C=\operatorname{curl},\ C^2=(-\Delta)P,\ t}
\]
and the genetic equation remains
\[
\boxed{u_t=P[X_u,C]u-\nu C^2u.}
\]
This branch does not attempt to enlarge the NEO ontology.

The new problem is:
\[
\boxed{
\text{given a compiled terminal observable, who owns it and can that ownership reach the contact?}
}
\]

---

## 2. New branch-local compiler layers

### A. Provenance typing

Every terminal renderer is tracked by
\[
(\text{frame},\text{scale},\text{passage topology},\text{owner}).
\]
This prevents pointwise derivative normalizations from being treated as compactness invariants when the extraction topology does not carry one full derivative.

### B. Square-anchor fate

The normalized coefficient
\[
\mu=\nu/(a\ell)
\]
is promoted to a terminal compiler axis:
\[
\mu\to0,
\quad
\mu\to\mu_*\in(0,\infty),
\quad
\mu\to\infty.
\]
These are three fates of the same anchor \(C^2\), not three mechanisms.

### C. Contact-action prism

For \(\omega=\rho n\) and \(Sn=an+b\),
\[
\boxed{\alpha=\gamma+\sigma,\qquad\beta=\theta+\kappa.}
\]
Radial strain action is allocated between material amplitude growth and square leakage.  Tangential strain action is allocated between material direction turning and square turning.

### D. Finite owner alphabet

Working owner types:
\[
\boxed{\mathrm{LOC}\vee\mathrm{LAG}\vee\mathrm{AFF}\vee\mathrm{MIC}.}
\]
They mean local contact owner, finite causal-lag owner, separated affine companion, and canonical nested micro owner.

---

## 3. Exact result: canonical nesting preserves local contact species

For the Euler-degenerate normalized equation
\[
V_s=P[X_V,C]V-\mu C^2V,
\]
perform the exact Galilean transform
\[
\widetilde V(y,s)=V(y+ds,s)-d
\]
and nested zoom
\[
W(z,s)=\mu^{-1/2}\widetilde V(\sqrt\mu z,s).
\]
Then
\[
W_s=P[X_W,C]W-C^2W.
\]
At corresponding points,
\[
\nabla W=\nabla V,
\qquad
CW=CV,
\qquad
D_t^W=D_t^V,
\]
while
\[
\Delta_z\omega_W=\mu\Delta_y\omega_V.
\]
Therefore
\[
\boxed{
(\alpha,\beta,\gamma,\sigma,\theta,\kappa)_W
=(\alpha,\beta,\gamma,\sigma,\theta,\kappa)_V.
}
\]

**Consequence.** Square-anchor degeneration changes the owner scale but not the local contact classifier.  Type-I/viscous contact algebra and the nested Type-II NS micro-layer should share one local normal-form compiler.

---

## 4. Exact scale coincidence driving the Type-II programme

If the macro scale is \(\ell\), curl scale is \(\Omega\sim a/\ell\), and
\[
\mu=\frac{\nu}{\Omega\ell^2},
\]
then the viscous record radius
\[
r_\nu=\sqrt{\nu/\Omega}
\]
satisfies
\[
\boxed{r_\nu/\ell=\sqrt\mu.}
\]
Thus the canonical record/analytic radius coincides exactly with the nested scale that restores unit square-anchor strength.

This motivates the branch's main Type-II target:
\[
\boxed{\text{No Third Scale}.}
\]
Singular curl ownership should be forced either into a macro-stable renderer or into the canonical \(\sqrt\mu\) nested NS layer, rather than an unlimited hidden subscale cascade.

---

## 5. Negative design result for Type-I propagation

At a G3A contact the minimal Riccati defects satisfy
\[
D_tb=P_{n^\perp}Zn,
\qquad
D_t\delta=d\,W_\lambda:Z,
\qquad
Z=-H_0+\nu\Delta A.
\]
The branch-local rank audit shows that the map from symmetric trace-free \(Z\) to
\[
(D_tb_1,D_tb_2,D_t\delta)
\]
has rank three.

Therefore there is no hidden algebraic collapse of the three normal defect-creation rates to a single signed direction.  Any Type-I barrier must control the Hodge/heat forcing analytically, propagate it causally, or exploit scale ownership.  Local G3 algebra alone cannot supply the missing sign.

---

## 6. Current finite theorem targets

### Type I: Causal defect propagation

Input shape:
\[
\text{saturated contact}
\leftarrow
\text{finite-lag positive-production bubble}
\leftarrow
\text{quantitative off-involution defect}.
\]
Target:
\[
\boxed{
\text{derive and propagate the minimal defect system }Z=(b,\delta)
\text{ to terminal incompatibility}.}
\]

### Type II: No Third Scale

Target:
\[
\boxed{
\text{singular activity}
\Longrightarrow
\mathrm{MAC}\vee\mathrm{MIC}
}
\]
with `MIC` living at the exact \(\sqrt\mu\) square-restoring scale.

### Type II: Macro--micro no-decoupling

Find a compactness-stable renderer \(Q\), preferably circulation or Galilean oscillation, such that
\[
\boxed{
Q_{\rm singular}\ge c
\Longrightarrow
Q_{\rm macro}\ge c_1
\vee
Q_{\rm micro}\ge c_2.
}
\]

---

## 7. Files in this branch programme

- `research/NEO_PROVENANCE_PROPAGATION_COMPILER.md` -- provenance types, owner alphabet, contact-action prism, causal compiler and terminal signature.
- `research/NEO_CAUSAL_DEFECT_PROPAGATION_LAB.md` -- minimal Riccati defect propagation programme and falsification rules.
- `research/NEO_FINITE_TWO_SCALE_CLOSURE_LAB.md` -- exact nested scaling, circulation scaling, contact covariance and No Third Scale programme.
- `audits/neo_contact_action_prism.py` -- exact radial/tangential projection sanity check.
- `audits/neo_two_scale_scaling.py` -- square restoration, circulation scaling, record-radius coincidence and contact covariance.
- `audits/neo_g3_defect_rate_rank.py` -- rank-three G3 normal defect-rate audit.

---

## 8. Promotion rule

Nothing in this branch becomes canonical merely because it is internally consistent.

Promotion requires:

1. exact algebra audited independently;
2. every imported PDE theorem rechecked in its exact function-space contract;
3. hostile anti-model battery passed;
4. at least one terminal branch removed, one extraction seam closed, or one previously independent escape axis rigorously coupled to another.

The metric remains
\[
\boxed{\text{number of surviving singular terminal forms},}
\]
not the number of NEO descendants generated.

---

## 9. Long-run research update: classification coordinates are not propagation meters

The first propagation campaign changes the branch strategy materially.

The minimal C1/Riccati coordinates
\[
\boxed{b=P_{n^\perp}Sn,\qquad \delta=6a^2-g}
\]
remain the correct **local classifier**.  But they are not the best propagation variables.

`NEO_RICCATI_NORMAL_ATTRACTION.md` proves that the restricted/local Riccati backbone has normal linear rates
\[
\boxed{-2a,-2a,-a}
\]
at G3.  Thus normalized off-involution geometry is locally attracted toward the coherent sheet.  A past defect is not automatically a contradiction.

`NEO_PARABOLIC_DEFECT_SYSTEM.md` then shows that the true drift-diffusion equations for \(b\) and \(\delta\) contain only first-gradient carré terms after second-derivative cancellation, but those terms have no scalar sign.  Exact Hessian-compatible divergence-free second-jet audits exhibit both signs even at G3.

Therefore the scalar maximum-principle route for a local distance-to-G3 is demoted.

The better propagation renderers are the polynomial normal-invariant pair
\[
\boxed{
\mathcal J=\omega\times A\omega,
\qquad
\mathcal V=r^2-\frac16g^3.
}
\]
Both obey
\[
\boxed{D_t\mathcal J=0,\qquad D_t\mathcal V=0}
\]
under the restricted/local Riccati dynamics.  Their full NS evolution is therefore **pure Hodge/square normal action** after the coherent self-dynamics is quotiented out.

This yields a new compiler rule:
\[
\boxed{
\text{use minimal coordinates for classification; use self-dynamics-quotiented renderers for propagation}.}
\]

## 10. Type-I causal chain after the normal-action audit

Using the current sibling Type-I results only as an explicit research input contract, the finite causal chain now reads
\[
\boxed{
\text{saturated curl contact}
\to
\text{positive radial under-gain }\delta>0
\to
\mathrm{ANG}\vee\mathrm{DISC}.
}
\]

The two outputs are
\[
\mathrm{ANG}:\quad |\mathcal J|>0,
\]
\[
\mathrm{DISC}:\quad |\mathcal V|>0,
\]
on a fixed positive fraction of a finite Green-visible causal region.  The exact aligned branch on which \(\delta>0\) but \(\mathcal J=\mathcal V=0\) is spatially thin in the licensed Type-I analytic/Hodge class.

At a terminal G3 contact
\[
\mathcal J(0,0)=\mathcal V(0,0)=0.
\]
Each nonzero past branch therefore yields an exact finite erasure action:
\[
\boxed{
\mathscr A_J
=\int\Gamma[\nu|\nabla\mathcal J|^2-\mathcal J\cdot L\mathcal J]>0,
}
\[
\boxed{
\mathscr A_V
=\int\Gamma[\nu|\nabla\mathcal V|^2-\mathcal V L\mathcal V]>0.
}
\]

The research problem has therefore compressed again:
\[
\boxed{
\text{Can the Type-I Hodge/square ledger pay the compulsory normal-erasure action?}
}
\]

Do not return to CP/QCP taxonomies or higher local Riccati jets.

## 11. Type-II correction: no third independent core normalization

`NEO_RECORD_SCALE_SEMIGROUP.md` corrects the earlier informal `No Third Scale' target.

At a fixed vorticity record, every curl-normalized scale \(R\) has
\[
\boxed{
\mu_R=\frac{\nu}{\Omega R^2}=\left(\frac{r_\nu}{R}\right)^2
}
\]
and the exact scale-transfer law
\[
\boxed{
V_{R_1}=\mathcal N_{R_1\leftarrow R_2}V_{R_2}.
}
\]
Canonical square restoration from **every** \(R\) lands on the same field:
\[
\boxed{
\mu_R^{-1/2}V_R(\sqrt{\mu_R}z,s)=V_{r_\nu}(z,s).
}
\]

Hence the safe exact statement is not `intermediate physical scales do not exist'.  It is
\[
\boxed{
\text{intermediate owner scales do not create independent record-core states}.}
\]

Combined with the affine companion principle, the first-order terminal architecture is
\[
\boxed{
\text{one unit-square record core}
+
\text{one affine companion imprint},
}
with larger Euler-degenerate windows used only as provenance carriers.

This is a stronger anti-profile-cascade rule than the original two-scale slogan while avoiding a false physical no-intermediate-scale claim.

## 12. New core-level research principles

The branch now proposes four research principles for eventual promotion, subject to theorem audit.

### P1. Renderer by task

One geometry may require different legal renderers for
\[
\boxed{
\text{classification},\quad
\text{compactness},\quad
\text{propagation}.}
\]
Do not demand one variable perform all three jobs.

### P2. Quotient coherent self-dynamics before charging a defect

If a local normal form has an internal coherent flow, propagation should first factor that flow out.  Only the residual Hodge/square action is a legitimate incompatibility cost.

### P3. Scale histories are not terminal states

At a record, the exact scale semigroup already relates all curl-normalized windows.  A new scale variable is justified only if it carries information absent from both the common viscous core and the affine companion renderer.

### P4. Erasure action replaces pointwise barrier

When diffusion prevents a scalar maximum-principle barrier, use the exact adjoint identity
\[
\boxed{
\text{past weighted defect mass}
=
2\times\text{finite erasure action}
+
\text{terminal mass}.}
\]
A terminal zero is then an action requirement, not a backward pointwise rigidity slogan.

## 13. Immediate frontier after this campaign

The highest-value next arrows are now:

1. **Type-I action coupling:** control \(\mathscr A_J\) or \(\mathscr A_V\) by the already-owned vector heat/incoherence cost and the Type-I Hodge ledger.
2. **Kernel-weighted Hodge estimate:** determine whether \(\nabla A\) and discriminant-gradient action can be localized against the actual Aronson kernel using only \(\nabla\omega\), enstrophy and finite cutoff errors.
3. **Stochastic angular bridge:** use a bounded matrix Feynman--Kac/stochastic-Lagrangian propagator to factor the \(-2a\) tangent attraction and charge only directional cancellation plus Hodge/square forcing.
4. **Record core--companion coupling:** after exact scale-semigroup collapse, prove that the unit-square record core cannot decouple from its admissible finite-energy affine/Euler companion provenance.
5. **R0 one-sided propagation:** respect the endpoint-first correction that two-sided C1 closure does not localize backward repayment; seek a genuinely parabolic backward co-location/thickening theorem rather than reclassifying arbitrary nearby C1 points as record contacts.

These are propagation/ownership problems.  Additional local descendants are currently disfavored.
