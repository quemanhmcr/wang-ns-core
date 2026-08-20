# Wang–NS Physical Core

An eight-document distillation of the current Wang–Navier–Stokes physical-road exhaustion programme.

Source programme: [`quemanhmcr/wang-ns-triad-diamond`](https://github.com/quemanhmcr/wang-ns-triad-diamond), read only from `main`.  The source baseline used for this distillation is `main@63178b0e7f9fabdfd8c344dab938a3d639639df5` (2026-08-13), whose latest upstream theorem state is the native material-service causal quotient.  This distill also records later **deductions obtained by composing already-certified upstream identities**; each such deduction is labelled explicitly.

There is **no claim yet of a proof of 3D Navier–Stokes global regularity**.  The representation/owner frontier is exhausted and the endpoint/initial-data interfaces are already assembled.  The only remaining proof block is the direct full-state exclusion of infinite critical `B/S/V/O` recycling.  Here `B` means the already-canonical minority-helicity positive-critical work branch, not a fourth `S/V/O` fate: the endpoint control-volume theorem remains exactly `S vee V vee O`.

## Repository invariant

This repository intentionally contains exactly **eight tracked documents**:

1. `README.md` — map, status legend, historical purification, reading order.
2. `CONTROL_VOLUME_METHOD.md` — reusable methodology: exact control-volume families before mechanisms or estimates.
3. `PHYSICAL_CORE.md` — the primitive identities plus the self-contained Clay(A)-to-`Y`-to-`S/V/O` endpoint spine.
4. `MIXED_FRONTIER.md` — hostile-referee closure of measure/Hahn/support/sidecar seams and the exact remaining frontier.
5. `SOLUTION_MAP.md` — short Clay-to-QED proof graph with proof-location links.
6. `BSVO_FULL_STATE_FRONTIER.md` — the dedicated remaining `B/S/V/O` full-state proof block.
7. `NS_POLAR_COMPATIBILITY_ARCHITECTURE.md` — the full polar/Hodge/compatibility synthesis, with a compact mandatory NEO gateway.
8. `NEO_ANCHOR_COMPILER.md` — the dedicated anchor algebra, mother-jet compiler, selection rules, unit tests and NEO research protocol.

No theorem implementation, regression code, result archive, PR history, packet scaffolding or CI transcript belongs here.  If a future edit grows a core file without changing the frontier, compress before merging.

Target line budgets: `README <= 210`, `CONTROL_VOLUME_METHOD <= 100`, `PHYSICAL_CORE <= 700`, `MIXED_FRONTIER <= 520`, `SOLUTION_MAP <= 180`, `BSVO_FULL_STATE_FRONTIER <= 560`, `NS_POLAR_COMPATIBILITY_ARCHITECTURE <= 1800`, `NEO_ANCHOR_COMPILER <= 520`.

## How to read the eight files

For the shortest route, read `CONTROL_VOLUME_METHOD.md` first for the proof discipline, then `PHYSICAL_CORE.md` for the Clay(A)-to-`S/V/O` endpoint spine, `SOLUTION_MAP.md` for composition, and `BSVO_FULL_STATE_FRONTIER.md` for the remaining open block.  Read `MIXED_FRONTIER.md` when auditing why older owner/bridge routes are forbidden and why the endpoint Hahn/support/constant plumbing is exact. Read `NS_POLAR_COMPATIBILITY_ARCHITECTURE.md` for the geometric synthesis and use `NEO_ANCHOR_COMPILER.md` whenever proposing, classifying or estimating a new mechanism: NEO is the mandatory ontology audit before a new object may enter the architecture.  A physicist should not need a separate synthesis document to understand the current theorem architecture; the source repository is needed only to inspect upstream proofs, constants, implementation records or historical derivations.

The key discipline is:

> **Observer may resolve Navier–Stokes physics, but may not manufacture Navier–Stokes physics.**

A projector may read a shell; it does not create the shell.  A cutoff may repartition nonlinear work; it does not create another work law.  A stopping rule may locate a first hit; it does not create the hit.  A normalization may compare scales; it does not create a finite resource.  Estimates quantify an already-identified physical object; they do not define its causal ontology.

## Status legend

- **EXACT** — analytic identity/theorem in the physical spine; CI/numerics are only certification evidence.
- **EXACT-CONDITIONAL** — exact implication once a stated physical entrance hypothesis is supplied; not a universal entrance theorem.
- **DISTILLED EXACT DEDUCTION** — new statement here obtained directly by composing upstream exact theorems, without a new estimate.
- **EVIDENCE** — finite-grid, Galerkin, FFT, randomized stress or non-rigorous CI checks; never a continuum proof.
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
hard-state last-entry = t=0 stock OR actual modal inflow on its occupied corridor
              |
       physical geometry/readout
              v
critical shell / hard tail / service / first-stop corridor
              |
     quotient observer depth
              v
source/derived-geometry marks expose state; they mint no causal scale edge
              |
hard-state energy law = modal stock + canonical boundary flow + viscosity
              |
     exact 5/8 geometric-good boundary geometry
              |
              v
finite endpoint: X OR Y; initial Hdot^(1/2) tail kills X
              |
              v
Y -> exact geometric split -> fixed positive inflow cell -> S OR V OR O
              |
              v
full-state road: N, G=curl N, strain/vorticity, exact triad phase
              |
              v
OPEN: no infinite critical B/S/V/O full-state recycling
```


**Closed upstream endpoint contract.**  The Clay branch used here is only `R^3(A)`: `nu>0`, `f=0`, smooth divergence-free rapidly decaying data, hence `u_0 in dot H^(1/2)`.  Classical/mild uniqueness makes Kenig--Koch apply to the same maximal time `T_*`.  The hard-shell gate now records the complete dyadic proof of `v_high<=C_sh sqrt(mu_>)||u||_(dot H^(3/2))^2` and the low-root Gronwall term.  The endpoint `G/B_bad` split is now a direct Borel restriction of the one Hahn-positive work law: `G` is defined by the exact signed-root conditions `-r<d<c`, `Z>0`, `3/5<d/c,r/c<5/8`, and `B_bad` is its complement.  No extremizer/certificate input remains in the Clay-to-sidecar implication.  `Y -> S vee V vee O` uses the whole final occupied corridor; the optional `cM^-2` natural window keeps its own `q_nat=min(1-theta,nu theta c/4)` and is not used to manufacture the constants `2/5 -> 3/25 -> 1/50 -> 1/150`.

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
11. **The mixed owner frontier was exhausted.**  Pressure, SGS, material, relink, helicity and traffic/material rereadings were reduced to exact state/geometry readings and cannot mint a fourth kinetic-energy supplier.
12. **The endpoint was reduced to one physical-road block.**  Finite singularity gives `X vee Y`; the initial critical tail kills `X`; `Y` gives an exact geometric two-way inflow split and then the exact `S vee V vee O` trichotomy.
13. **The cubic quotient was proved dynamically incomplete.**  The relative-translation witness keeps stocks, all active cubic works and `Q` fixed while changing `dot Q`, so the proof must return to full `u/omega`.
14. **The current frontier is full-state control-volume curvature accounting.**  The mother law, fixed radial hinge family and exact Volterra heat-square family have collapsed phase/tangent, zero-stock, superlevel and higher-jet observer mechanisms back into the actual state/work laws.  Unbounded endpoint recycling now forces scale-amplified hinge growth, blow-up of the actual boundary-work square family and infinite cumulative `N/F_N` curvature input.  Fixed-projector triple-product identities cancel every internal nonlinear curvature source and identify the remaining cross-volume part as antisymmetric transfer; `Y=>bot` is still open only at this final true transfer/viscosity block.

The recurring lesson is: **complexity should be removed only after its physical type is known**.

## Current theorem status in one view

**EXACT physical spine:** signed helical edge registration; continuum signed edge measure; canonical positive routing; cyclic donor kernel; mode-set energy continuity; radial crossing; hard-tail true upward supply; resolved-contact binding; pure-UV first-shell route; exact first-stop/tie semantics; checkpoint quotient; conservative relink quotient; inherited-stock relay; material-service quotient; high-strain telescope; canonical radial-variation/hard-shell collision; viscous hard-corridor natural-window inflow; `t=0` as exact modal-stock boundary.

**EXACT-CONDITIONAL:** generic critical-shell/coherent-service reentry once a critical shell is supplied; same-carrier inherited-stock relay under its endpoint/residual-work hypotheses; the older geometric-good generated-HH time telescope on a supplied parent-continuing chain.

**DISTILLED EXACT DEDUCTIONS:** carried-root recursion reduces to `H/G` with finitely many `H`; low-ball Kirchhoff roots pure-`G` funding; the critical first-moment ledger gives the geometric-good `9/25` radial-production floor; and the radial-variation proof sharpens to `v_rad<=C_sh sqrt(mu_sh)||u||_Hdot^(3/2)^2`, so any actual increase of `C_(1/2)` exposes a hard shell above the fixed `(2nu/C_sh)^2` critical quantum.

**EVIDENCE ONLY:** randomized helical triads, finite Galerkin/FFT NS probes, stress tests, implementation certificates and master traces.  None is an input to the distilled Clay-to-`S/V/O` theorem.

**EXTERNAL EXACT ENDPOINT:** Kenig--Koch, arXiv:0908.3349, Theorem 0.1: a mild solution with `u_0 in Hdot^(1/2)` that stays bounded in `Hdot^(1/2)` on its maximal lifespan is global and smooth; hence finite-time singularity forces unbounded critical stock.

**EXACT ENDPOINT SHARPENING:** finite singularity forces `t_n->T_*`, `M_n->infinity`.  Large shells cannot be initial stock; their final occupied corridors contain an actual interval of length `<=cM_n^-2` carrying a fixed fraction `q_nat` of terminal critical mass as canonical inflow.  Thus UV rebirth is parabolically localized by stock persistence plus viscosity, not by an observer time bin.

**DISTILLED EXACT UV CONTROL-VOLUME SPLIT:** every large UV birth obeys an exact geometric two-way restriction of the same `dW+`.  On `G`, signed roots satisfy `-r<d<c`, `Z>0`, `3/5<d/c,r/c<5/8`, so exact triad invariants give the simultaneous side recipient and the safe `N Phi_in,A^side>=c_nu/50`.  On the complementary `B_bad` branch, splitting the original child shell only by helicity gives the stronger direct inflow `N Phi_in,A>=c_nu/5`.  Kirchhoff therefore forces `N E_A`, `N D_A`, or `N Phi_out,A` to be at least the common `c_nu/150`.  No auxiliary extremizer, transfer-loss wallet or second Hahn exists.

**DISTILLED EXACT FIRST-CONTACT LAW:** at `M E_M=mu_*`, differential Kirchhoff gives a fixed inflow-rate floor.  If `G` owns it, sharp whole-band work forces a lower interaction shell `R<=5M/8` with `R E_R>=2mu_*`, so finite state descent reaches initial stock or a `B_bad`-rate alternative; no donor genealogy is used.

**DISTILLED EXACT HELICITY QUOTIENT:** for signed radius `x=s|k|`, triad helicity conservation and the two-flow donor kernel give `V_x<=2V_rho`; helicity-flip sidecar outflow and same-helicity radial outflow therefore share the existing radial-variation ledger.

**DISTILLED EXACT SHELL LAYER CAKE:** `||u||_Hdot^(1/2)^2=int_0^infinity [R||P_(R/2,R]u||_2^2] dR/R`.  Therefore a bounded-amplitude shell of bounded log-width cannot blow up merely by translating to UV.

**EXACT FULL-CONVOLUTION STRESS TEST:** for a finite Fourier NS state, an absent mode `q=n+m` with a unique active parent pair is born immediately whenever its exact Leray pair-source is nonzero; viscosity cannot cancel an absent child.  This is state generation, not `dW+`.  Kishimoto--Yoneda Theorem 1.4 gives the corresponding zero-tolerance finite-mode Euler rigidity (stationary 2D-like/Beltrami only).

**DISTILLED EXACT SIGNED-CURL PATH LAW:** put `x_i=s_i rho_i` and `Z_tri:=sum rho_i^2T_i`.  The certified cyclic law gives `sum T_i=sum x_iT_i=0` and `Z_tri=R_tri(x_0-x_1)(x_0-x_2)(x_1-x_2)`.  For distinct `alpha<beta<gamma`, the entire canonical donor graph is the path `alpha--beta--gamma`: with `D=|Z_tri|/(gamma-alpha)`, the two edge masses are `M_(alpha,beta)=D/(beta-alpha)` and `M_(beta,gamma)=D/(gamma-beta)`, so both legs carry exactly the same signed-curl displacement `D`; `Z_tri>0` orients the path from median to both extremes, `Z_tri<0` from both extremes to median.  Radial traffic is only the exact fold `rho=|x|` of this path.  If two `x` coincide, only same-helicity/equiradial exchange can survive and `Z_tri=V_rho=0` although work may be nonzero.  Thus the former four low-recipient classes and every other donor/recipient radial fate are projections of one two-leg law; no fifth reuse owner or finite convex-moment reset exists.
**DISTILLED EXACT BETCHOV/ENSTROPHY-SOURCE BRIDGE:** with `Q(t)=int omega.S omega`, root-marking of the same closed-triad measure and the gradient-energy identity give `2Q=C_F int Z_tri dLambda_tri`.  Pointwise `omega.S omega=4(det grad u-det S)` and Piola gives `det grad u=(1/3)div[(cof grad u)^T u]`; hence on the smooth finite-energy `R^3` state `Q=-4 int det S=-(4/3)int tr(S^3)=4 int lambda_1 lambda_2(-lambda_3)` for ordered strain eigenvalues `lambda_1>=lambda_2>=lambda_3`.  This is the same global source scalar in three exact representations, not three currencies or measure-level identifications.  A finite-Fourier anti-theorem is exact: pair a nondegenerate triad with a spectrally isolated `L`-dilate, scale the dilated amplitudes by `L^-1` and flip one modal phase; then `Z_L=-Z` while `V_(rho,L)=V_rho/L>0`, so total stretching can cancel with nonzero radial turnover.  Instantaneous cancellation is genuine physics.  But `0.5||grad u(t)||_2^2+nu int_0^t||Delta u||_2^2=0.5||grad u_0||_2^2+int_0^t Q` forces `sup_(t<T*) int_0^t Q=+infinity` at any finite singular endpoint.  The local source itself obeys `D_t(omega.S omega)=|S omega|^2-omega.(Hess p)omega+nu[2(Delta omega).(S omega)+omega.(Delta S)omega]`, with `-Delta p=|S|^2-|omega|^2/2`; pressure Hessian is therefore the only inviscid counterterm to the nonnegative self-strain term, not an independent kinetic-energy supplier.
**EXACT VECTOR HEAT-SPHERE LAW:** at fixed child `q` and parent helicity, `r=2p-q` turns equal heat rate into the physical unordered sphere `S^2/(r~-r)=RP^2`.  The unordered Leray vector-orbit norm is `|q.r||qxr|sqrt((P+M)^2+Q^2)|a_pa_m|/[4PMQ(P+M)]`; its Leray zeros are the Beltrami equator and shear pole.  The pressure complement distinguishes them exactly: same-helicity equal-radius parents are a gradient-only/Bernoulli interaction with generally nonzero pressure pair, while collinear shear has zero raw convective pair and zero pressure source.  The projective source line is `ell_q=[t_q+i h beta n]`, `beta=Q/(P+M)`, with an exact Fubini--Study separation formula.  Its generic nontrivial double fiber is the planar cross-isospectral reflection rectangle; exact two-atom cancellation there forces source at the remaining `q+-u` outputs with explicit ratio `G_side/G_0`, vanishing only as the original atom reaches the Beltrami equator.  Minority/spin-two are just helical coordinates; no causal Hahn is introduced.
**DISTILLED EXACT MATERIAL-PAIR VORTICITY LAW:** pressure is downstream: `u=curl(-Delta)^-1 omega` and NS is equivalent to `partial_t omega+(u.grad)omega=(omega.grad)u+nu Delta omega`.  Biot--Savart gives `Q=int omega.S omega=(3/8pi)int int[((delta omega).h)((bar omega cross delta omega).h)]/|h|^5 dxdy`, `bar omega=(omega_x+omega_y)/2`; the two exact zero factors are longitudinal increment and vortex-pair chirality.  For material particles `x=X(a,t),y=X(b,t)`, put `Abar=int_0^1 grad u(x+theta h)dtheta`, `E_x=A_x-Abar`, `E_y=A_y-Abar`, `L=delta omega.h`, `C=(omega_x cross omega_y).h`, `K=LC/|h|^5`.  Then `hdot=Abar h`, `tr Abar=0`; common affine deformation cancels exactly from `Cdot`, while `E_x,E_y` are the weighted line-integrals of `(h.grad)grad u` and viscosity supplies the only other chirality term.  Common strain may still change `L` and `|h|`.  Thus chirality-null and longitudinal-null are physically different zero manifolds; no angular/chirality currency is introduced.
**DISTILLED EXACT TRAFFIC/MATERIAL ANTI-CORRESPONDENCE:** the earlier same-child opposite-`Z_tri` witness already forbids pushing UV inflow atomwise to `Q+`.  A stronger exact torus witness now fixes the entire instantaneous spectral quotient: two real divergence-free states have identical modal stocks, every active canonical cubic work, and normalized `Q=-980`, yet a relative half-period translation of one spectrally cubic-isolated triad family changes the true NS first time jet by `dot Q_delta-dot Q_0=87152/55`, independently of `nu`.  The reason is exact: no mixed closed triad survives, but a mixed quartet does.  Thus traffic/work data are not a closed dynamical state and cannot canonically own or predict material-pair geometry; relative phase information discarded by the cubic quotient reappears in the quartic NS time jet.  The representation frontier is exhausted: the remaining mathematical question is the specific direct full-state `B/S/V/O` exclusion recorded in `BSVO_FULL_STATE_FRONTIER.md`, not another traffic-to-chirality bridge, Hahn law, pressure/Lamb road, coherence budget or genealogy.

**EXACT FULL-STATE `B/S/V/O` FRONTIER — TOTAL CONTROL-VOLUME FAMILY FORM:** the canonical derivation is `BSVO_FULL_STATE_FRONTIER.md` §20.  The fixed hinge and Volterra families now collapse one level further when **all** radial cuts are summed: `L_tail J` is exactly twice the tail enstrophy-work, arbitrary cut weights give one full-field slot commutator `D_phi(N,u;omega)+(1/2)D_phi(u,u;G)`, and the adaptive reader `phi'_(alpha,J)=2R^alpha J` satisfies `4J_alpha=W_phi` with `dot J_alpha` equal to complementary work-rate transfer rather than a new curvature source.  The entire continuum of `kappa` fronts gives an exact coarea theorem forcing `int||Lambda^(-epsilon/2)N||^2dt=infinity` for every `epsilon<1` and a log-enhanced `H^-1/2` burden.  A general kernel lower bound proves this is the observer limit: any weight capable of seeing an unbounded front is at least critical `H^-1/2` (with slow strengthening), while kinetic energy supplies only the standard `N in L_t^(4/3)H^-1` control.  Therefore no extra front, norm, phase, zero-stock birth, radial `O`, clock, genealogy or wallet can close the branch.  The still-open theorem is genuinely full-convolution: exclude finite-endpoint persistence of the remaining `u/N/G/F_N` slot-commutator / antisymmetric work-rate transfer; equivalently `Y=>bot`.

## Upstream proof lookup map

When a proof must be inspected, jump directly to these source-main modules: `physical_energy_causal_bridge.md` (Duhamel vs physical work); `helical_physical_edge_registration.md` + `continuum_helical_edge_measure_registration.md` (signed NS edge law); `cyclic_helical_triad_donor_kernel.md` (same-time donor provenance); `helical_mode_set_energy_continuity.md` (between-time stock); `radial_spectral_crossing_layer_cake.md` + `hard_tail_true_upward_supply.md` (true scale crossing/supply); `resolved_contact_native_binding.md` and the pure-UV natural-window theorem (upward support); `critical_shell_service_reentry.md` + `continuum_master_event_quotient.md` (shell/corridor/event semantics); `same_carrier_inherited_energy_relay.md` (stock); `native_material_service_causal_quotient.md` (material); `high_strain_descending_epoch_telescope.md` and `signed_good_generated_epoch_time_telescope.md` (the two finite pure tails).

The exact filename is more important than historical commit order; certification hashes and numerical referee evidence live inside the source theorem records.

## Non-negotiable audit questions

Before admitting any new quantity, event or edge, ask: What exact NS object is this?  What are its units?  Is it stock, signed work, flux, dissipation, geometry, provenance or representation?  If the observer changes while the physical solution is fixed, does the alleged event change?  Has Hahn already been taken?  If a work charge exists, is it kept at its physical event rather than illegally carried through modal stock?  What exact true-NS identity makes the step valid that an averaged/blow-up surrogate need not retain?  If the answer is only scaling, cancellation or a generic bilinear estimate, it is not yet a frontier closure.

The goal is not to make Navier–Stokes obey a convenient proof language.  The goal is to discover the smallest rigid grammar that Navier–Stokes already obeys.
