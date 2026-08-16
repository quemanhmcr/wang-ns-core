# Wang–NS Physical Core

A three-document distillation of the current Wang–Navier–Stokes no-escape programme.

Source programme: [`quemanhmcr/wang-ns-triad-diamond`](https://github.com/quemanhmcr/wang-ns-triad-diamond), read only from `main`.  The source baseline used for this distillation is `main@63178b0e7f9fabdfd8c344dab938a3d639639df5` (2026-08-13), whose latest upstream theorem state is the native material-service causal quotient.  This distill also records later **deductions obtained by composing already-certified upstream identities**; each such deduction is labelled explicitly.

There is **no claim of a proof of 3D Navier–Stokes global regularity**.  The remaining programme-level problems include mixed genuine-physics recurrence, a local degenerate HH seam, and the initial/singular-time interfaces.

## Repository invariant

This repository intentionally contains exactly **three tracked documents**:

1. `README.md` — map, status legend, historical purification, reading order.
2. `PHYSICAL_CORE.md` — the smallest current set of physical objects, exact identities, theorems and anti-theorems.
3. `MIXED_FRONTIER.md` — what has been quotiented away, what remains open, and what a valid next theorem is allowed to use.

No theorem implementation, regression code, result archive, PR history, packet scaffolding or CI transcript belongs here.  Those live in the source repository.  If a future edit makes these documents substantially longer without changing the frontier, compress before merging.

Target line budgets: `README <= 140`, `PHYSICAL_CORE <= 380`, `MIXED_FRONTIER <= 320`; total `<= 840` lines.

## How to read the three files

Read this file once, then `PHYSICAL_CORE.md` from top to bottom, then `MIXED_FRONTIER.md`.  A physicist should not need the source repository to understand the current theorem architecture; the source repository is needed only to inspect proofs, exact constants, certification evidence or historical derivations.

The key discipline is:

> **Observer may resolve Navier–Stokes physics, but may not manufacture Navier–Stokes physics.**

A projector may read a shell; it does not create the shell.  A cutoff may repartition nonlinear work; it does not create another work law.  A stopping rule may locate a first hit; it does not create the hit.  A normalization may compare scales; it does not create a finite resource.  Estimates quantify an already-identified physical object; they do not define its causal ontology.

## Status legend

- **EXACT** — analytic identity/theorem in the physical spine; CI/numerics are only certification evidence.
- **EXACT-CONDITIONAL** — exact implication once a stated physical entrance hypothesis is supplied; not a universal entrance theorem.
- **DISTILLED EXACT DEDUCTION** — new statement here obtained directly by composing upstream exact theorems, without a new estimate.
- **EVIDENCE** — finite-grid, Galerkin, FFT, randomized or CI checks; never a continuum proof.
- **OPEN / HYPOTHESIS** — research frontier; must not be quoted as theorem.

## Current physical picture

```text
full incompressible NS:  u_t + B(u,u) = nu Delta u
              |
              v
actual signed Fourier/helical nonlinear work dW
              |
          Hahn once
              v
canonical positive recipient work dW+  <--- donor provenance from dW-
              |
       mode-set continuity
              v
hard-shell/tail energy = earlier modal stock OR actual nonlinear boundary inflow
              |
       physical geometry/readout
              v
critical shell / hard tail / service / first-stop corridor
              |
     quotient observer depth
              v
strain/dissipation events <--> actual nonlinear work <--> source/derived-geometry events
              |
       mixed frontier remains
```

The square/service/shell layers are real physical observables, but a new observable is not automatically a new causal charge.

## How the programme arrived here

The historical movement is not “more abstraction”; it is repeated removal of abstractions that nature did not supply.

1. **Extremizer/rigidity stage.**  Young/Christ near-extremizers, Gaussian grains, Hodge/Bellman/entropy, affine geometry and sidebands were used to seek rigidity of dangerous transfer.
2. **Counterexamples disciplined the language.**  Full Mellin moments, fixed moat schedules, tree-growth counting, absolute-polarization intuition and affine-aspect penalties each failed in concrete models.  Correct inequalities were not enough if they forgot the wrong physical distinction.
3. **Duhamel causality was rejected.**  A scalar exact countermodel has normalized Duhamel mass `dt` but positive child-energy work `2t dt`; amplitude mass cannot be declared causal probability.
4. **Signed physical work became primitive.**  The programme reconstructed actual Leray/Fourier/helical work `dW` first and took one Hahn positive part `dW+` only afterward.
5. **Same-time provenance was separated from between-time stock.**  The cyclic donor kernel routes canonical negative work to positive recipients without cloning charge; modal energy continuity then shows that persistent stock lives on modes, not interaction cells.
6. **Scale motion became physical boundary crossing.**  Radial layer cake and hard-tail balance distinguish true low→high supply from high→high circulation; equiradial work has zero radial progress.
7. **Resolved contact and pure UV were split by exact Fourier geometry.**  Signed work is decomposed before positive restriction; contact is not interface work by definition.
8. **Critical-shell recurrence was cleaned.**  Hard shells are event readers, smooth carriers propagate, coefficient hits are locators, checkpoints do not reset, and full-natural service is a same-corridor witness.
9. **Representation owners were quotiented.**  Material rereading, selected-family switching, smooth skew relink, role/probe changes and same-carrier inherited stock no longer create generation depth merely by changing description.
10. **Two pure recurrence tails closed.**  Consecutive high strain is finite by exact scale descent plus the global gradient reservoir; consecutive signed-good generated HH is finite by exact parent-scale geometry plus parabolic backshift to `t=0`.
11. **The remaining problem became genuinely mixed.**  A hypothetical infinite lineage can switch physical mechanism before either pure telescope applies forever.
12. **Current distillation sharpens owner vs supplier.**  Shell/service is state/witness, not a fourth charge; exact mode-set continuity further says terminal hard-shell kinetic energy is supplied only by earlier modal stock or actual nonlinear inflow, regardless of which theorem exposed the shell.

The recurring lesson is: **complexity should be removed only after its physical type is known**.

## Current theorem status in one view

**EXACT physical spine:** signed helical edge registration; continuum signed edge measure; canonical positive routing; cyclic donor kernel; mode-set energy continuity; radial crossing; hard-tail true upward supply; resolved-contact binding; pure-UV first-shell route; exact first-stop/tie semantics; checkpoint quotient; conservative relink quotient; inherited-stock relay; material-service quotient; the two pure recurrence telescopes.

**EXACT-CONDITIONAL:** generic critical-shell/coherent-service reentry once a critical physical shell is supplied; same-carrier inherited-stock relay once its carrier/endpoint/residual-work hypotheses hold; signed-good local HH recurrence geometry once the signed-good generated branch is physically selected.

**DISTILLED EXACT DEDUCTIONS:** role/probe and shell/service readers mint no charge; hard-role energy is earlier stock or actual modal inflow; objective SGS has selector-free shell/tail handoff; local non-signed-good positive HH is terminal before Young while the only unresolved local good-HH limit is degenerate full-signed Christ margin; and parent-continuing high-strain / signed-good-HH alternation including exact ties has finite depth.

**EVIDENCE ONLY:** randomized helical triads, finite Galerkin/FFT NS probes, stress tests, CI certificates and master traces.

**OPEN:** nonlocal high-tail continuation; the degenerate full-signed Young/Christ seam (and only if genuinely needed, a separately proved positive coherent kernel); source-marked breaker coupling and broader Mixed recurrence; the initial-data and hypothetical-singular-time interfaces.

## Upstream proof lookup map

When a proof must be inspected, jump directly to these source-main modules: `physical_energy_causal_bridge.md` (Duhamel vs physical work); `helical_physical_edge_registration.md` + `continuum_helical_edge_measure_registration.md` (signed NS edge law); `cyclic_helical_triad_donor_kernel.md` (same-time donor provenance); `helical_mode_set_energy_continuity.md` (between-time stock); `radial_spectral_crossing_layer_cake.md` + `hard_tail_true_upward_supply.md` (true scale crossing/supply); `resolved_contact_native_binding.md` and the pure-UV natural-window theorem (upward support); `critical_shell_service_reentry.md` + `continuum_master_event_quotient.md` (shell/corridor/event semantics); `same_carrier_inherited_energy_relay.md` (stock); `native_material_service_causal_quotient.md` (material); `high_strain_descending_epoch_telescope.md` and `signed_good_generated_epoch_time_telescope.md` (the two finite pure tails).

The exact filename is more important than historical commit order; certification hashes and numerical referee evidence live inside the source theorem records.

## Non-negotiable audit questions

Before admitting any new quantity, event or edge, ask: What exact NS object is this?  What are its units?  Is it stock, signed work, flux, dissipation, geometry, provenance or representation?  If the observer changes while the physical solution is fixed, does the alleged event change?  Has Hahn already been taken?  Does the step preserve one physical charge?  What exact true-NS identity makes the step valid that an averaged/blow-up surrogate need not retain?  If the answer is only scaling, cancellation or a generic bilinear estimate, it is not yet a frontier closure.

The goal is not to make Navier–Stokes obey a convenient proof language.  The goal is to discover the smallest rigid grammar that Navier–Stokes already obeys.
