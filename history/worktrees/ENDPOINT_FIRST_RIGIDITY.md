# Endpoint-First Rigidity Worktree
## Record vorticity, C0/C1 contact, finite terminal alphabets and backward-rigid exits

**Historical branch:** `research/endpoint-first-rigidity`
**Recorded HEAD:** `38dba6f` — `research: compress R0 repayment and terminal kill classes`

This was the largest branch devoted to the idea that a hypothetical singular endpoint should be compressed into a **small terminal alphabet** rather than followed through a full trajectory history.

Its opening rule was
\[
\boxed{
T_*<\infty
\to
\text{smallest admissible singular survivor}
\to
\text{exact contact}
\to
\text{finite normal forms}
\to
\text{rigidity}.
}
\]

## 1. The first normalized contact

On the positive-viscosity ancient branch, the target normalization was
\[
|\omega(x,t)|\le1,
\qquad
|\omega(0,0)|=1,
\qquad
U(0,0)=0.
\]

The scalar vorticity equation gives
\[
(\partial_t+U\cdot\nabla-\nu\Delta)\frac{|\omega|^2}{2}
=
\omega\cdot S\omega-
u|\nabla\omega|^2.
\]

This produced the first terminal split
\[
\boxed{
\mathrm{C0}:\ \omega\cdot S\omega=0,
\qquad
\mathrm{C1}:\ \omega\cdot S\omega>0.
}
\]

C0 initially looked like the easier branch because the maximum principle forces strong flatness at the contact.

## 2. C0 was much flatter than expected — and still not rigid

At a normalized C0 contact the programme obtained
\[
\nabla\omega=0,
\qquad
\partial_t|\omega|^2=0,
\qquad
D_x^2|\omega|^2=0,
\]
and later still stronger scalar-contact flatness.

The velocity Hessian collapsed to a symmetric trace-free rank-three sector. This looked promising: perhaps repeated contact differentiation would eventually force the curl field to be constant.

It did not.

`C0_LOCAL_POLAR_NORMAL_FORM.md` and the arbitrary-angular-order audit showed that the direction of vorticity can begin varying at arbitrarily high finite order while the amplitude remains locally saturated.

That was one of the first decisive anti-history results:

\[
\boxed{
\text{more scalar contact derivatives}
\ne
\text{less angular freedom}.
}
\]

The branch explicitly demoted further scalar C0 differentiation as a research strategy.

## 3. Scale geometry replaced jet prolongation

The branch then moved from higher jets to finite spatial scales.

Several scales appeared:

- Galilean velocity-oscillation scale;
- viscous record radius
  \[
  r_\nu=\sqrt{\nu/\Omega};
  \]
- energy--curl outer scale
  \[
  \ell_E=E^{1/5}\Omega^{-2/5};
  \]
- supporting-circulation radii;
- bounded velocity/curl microscopes;
- gradient and balanced Euler microscopes.

The important correction was conceptual. These were not declared new mechanisms. They were attempts to identify **where existing curl/strain geometry could hide** under extraction.

## 4. Type-I and non-Type-I had to separate

The literature audit showed that Type-I singularity has a better extraction contract than a general singular endpoint. On the Type-I branch, known results provide a bounded nonconstant ancient profile with a finite scale ledger; nonzero constants are excluded by that ledger.

The non-Type-I/Type-II regime required a different microscope.

The branch therefore introduced a square-anchor coefficient and separated limits where viscosity survives, degenerates, or dominates. One major warning emerged:

> Never import viscous C0 equality into an Euler terminal microscope.

The local normal form depends on the fate of the square anchor `C^2`.

## 5. Record selection changed the terminal alphabet

Later the branch organized the geometry around running vorticity records. The final terminal compiler distinguished broad owner types such as:

- time-owned C1;
- square-owned C1;
- C0 record corner;
- mesoscopic strain/Hodge modifiers.

The important progress measure became **the number of surviving terminal forms**, not the number of derived identities.

The `TERMINALITY_LEDGER.md` explicitly rejected any new reader that did not remove or reduce one row of the terminal table.

## 6. C0 repayment and nearby C1

A major later correction was that C0 need not be treated as an isolated eternal state. Backward heat/Duhamel arguments showed that a saturated C0 contact must be “repaid” by genuine positive stretching in a finite backward spacetime region.

This led to the idea that C0 is not closed by higher local flatness. It must be linked to a **finite propagation-ready relation**.

The branch searched for exact terminal relations that could be fed into backward uniqueness or Liouville theorems.

## 7. Backward-rigid kill classes

The strongest finite exits were relations such as:

- curl-null bounded ancient field → Galilean-null;
- one fixed directional curl derivative vanishing on a thick terminal set → translation symmetry → 2D3C → Liouville;
- fixed vorticity direction on a thick set → translation symmetry → 2D3C;
- exact nonlinear equilibrium with a positive curl-square eigenvalue → explicit ancient orbit incompatible with boundedness;
- Beltrami/curl eigenfields as a special explicit-orbit case.

This was a genuine success of the endpoint-first philosophy: an **exact relation** could sometimes be promoted into a global terminal kill without another jet hierarchy.

## 8. Why this branch did not become the final core

The branch accumulated many scale owners, microscopes and terminal modifiers. They were carefully typed, but the programme was still trying to close singularity by selecting the right finite terminal geometry.

The later C0-rigidity worktree showed a deeper issue. Pressure/Hodge, Riccati defects, helicity torsion and spectral readers repeatedly appeared as different faces of the same material-curl deformation. The problem was no longer simply to find the right terminal row. The ontology itself could be compressed further.

The endpoint-first branch nevertheless contributed three permanent lessons:

1. local contact rigidity is weaker than it first appears;
2. finite-scale geometry is preferable to an infinite derivative tower;
3. an exact terminal relation is valuable only if it feeds a known rigidity mechanism.

## 9. Selected historical source coordinates

The branch contained many files. The most useful landmarks were:

- `ENDPOINT_FIRST_PROGRAM.md`;
- `research/EXTRACTION_CONTRACT.md`;
- `research/C0_CONTACT_AUDIT.md`;
- `research/C0_LOCAL_POLAR_NORMAL_FORM.md`;
- `research/CURL_CONTACT_STOKES_POLAR_SPLIT.md`;
- `research/RECORD_TERMINAL_COMPILER.md`;
- `research/TERMINALITY_LEDGER.md`;
- `research/R0_BACKWARD_FINITE_RADIUS_REPAYMENT.md`;
- `research/TERMINAL_DIRECTIONAL_CURL_DERIVATIVE_KILL.md`;
- `research/TERMINAL_FIXED_DIRECTION_KILL.md`;
- `research/TERMINAL_EXPLICIT_ORBIT_KILL.md`.

Several later classifier/kill experiments remained untracked at the recorded worktree HEAD. They are branch archaeology, not canonical main content.
