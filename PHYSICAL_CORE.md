# Physical Core

This file contains the smallest current theorem basis needed to stand at the mixed frontier.  It deliberately preserves physical type: stock is not work, work is not capacity, a witness is not a source, same-time redistribution is not between-time generation, and an observer coordinate is not a physical clock.

## 1. Native PDE and ontology

On a smooth pre-singular interval write incompressible Navier–Stokes in Leray form

\[
\partial_t u+\mathcal B(u,u)=\nu\Delta u,\qquad \nabla\cdot u=0.
\]

Pressure is physical in the primitive equation and in strain/gradient dynamics, but after Leray projection it is not an independent global kinetic-energy source.  For divergence-free global probes, `⟨u,∇p⟩=0` exactly.  Localized pressure boundary work is a different object and must not be imported into global interscale causality by name.

The persistent state is the velocity field, equivalently its physical Fourier–helical modal amplitudes.  Derived objects—resolved strain, SGS stress, coherent service, shell mass, material labels, probes—may be exact and useful without becoming primitive state or causal currency.

## 2. Signed nonlinear work before Hahn — EXACT

For one unordered helical parent orbit `x+y=z`, direct Leray/curl evaluation equals the Waleffe registration.  The physical child-energy work has the exact form

\[
T_e=4(s_x|x|-s_y|y|)\operatorname{Re}\big[\overline{a_z}\,\overline{g_e}\,a_xa_y\big].
\]

The native modal interaction capacity `A_e=4|z||a_xa_ya_z|` obeys `|T_e|<=A_e`, but capacity is only a reference envelope.  It is never causal probability, work, reset budget or recurrence currency.

The continuum unordered-parent quotient reconstructs a locally Radon **signed** physical edge measure `dW`.  Only after signed reconstruction take the canonical Hahn decomposition

\[
dW=dW^+-dW^-.
\]

`dW+` is the canonical positive recipient-work law.  After this point every downstream good/bad, shell, donor, contact or service label must be a restriction or positive pushforward of the already-existing law.  Never replace `pi#(dW+)` by `[pi#dW]_+`.

### Duhamel anti-theorem — EXACT countermodel

For `c_dot=1`, `c(0)=0`, terminal adjoint `psi=1`, normalized Duhamel amplitude mass is `dGamma=dt`, while positive child-energy work is `dT=2t dt`.  Hence `Gamma([0,t])=t` but `T([0,t])=t^2`.  Duhamel may locate event support; it does not supply physical causal probability.

## 3. Closed triads and donor provenance — EXACT

For one closed triad let signed modal works satisfy

\[
T_0+T_1+T_2=0,
\qquad P_i=[T_i]_+,
\qquad N_i=[-T_i]_+,
\qquad Q=\sum_iP_i=\sum_iN_i.
\]

The canonical cyclic donor kernel is

\[
M(i\to j)=\frac{N_iP_j}{Q}.
\]

Its donor marginal is `dW-`; its recipient marginal is the already-canonical `dW+`.  Multiple donors may feed one recipient, but the recipient carries one physical charge.  Donors are provenance, not cloned causes.  Same-time donor cycles are real conservative redistribution and have zero generation depth.

Generic triads can have two energy donors.  The signed-good forward case has one energy donor but can still have a positive nonforward side recipient; that side work is real energy transfer, not dissipation and not a reset.

## 4. Modal stock and mode-set continuity — EXACT

Physical energy stock lives on helical modes `m=(k,s)`:

\[
E_m(t)=|a_{k,s}(t)|^2.
\]

Push the cyclic donor flow to modal nodes.  For any physical mode set `A`, let `Phi_in,A` and `Phi_out,A` be actual donor-flow crossings of its boundary.  Internal flow cancels only from the set divergence, not from the PDE.  The exact interval law is

\[
\boxed{E_A(t_1)+D_A+\Phi_{out,A}=E_A(t_0)+\Phi_{in,A}},
\]

where

\[
D_A=2\nu\int_{t_0}^{t_1}\sum_{(k,s)\in A}|k|^2E_{k,s}(t)\,dt.
\]

For the full mode set this reduces to the ordinary viscous energy balance.  The law gives aggregate stock/flow continuity only; it does not select FIFO, LIFO, oldest-first, newest-first or proportional temporal provenance.

### Gross-transfer anti-theorem

A closed triad wholly inside `A` has zero boundary flux but can carry nonzero internal donor/recipient flow.  Scaling amplitudes by `lambda` scales this gross work like `lambda^3` while boundary flux remains zero.  Therefore modal stock does not bound total gross nonlinear turnover, and neither `int dW+` nor `int dW-` is a finite reset budget.

### Native hard-role / hard-shell supply quotient — DISTILLED EXACT DEDUCTION

The same law applies to every bounded measurable event-anchored hard Fourier/helicity role `P`, not only a radial shell:

\[
\boxed{E_P(t)+D_P+\Phi_{out,P}=E_P(s)+\Phi_{in,P}}.
\]

Hence for every `0<theta<1`, either `E_P(s)>=theta E_P(t)` or `Phi_in,P>=(1-theta)E_P(t)`; exact equality keeps both.  The inflow is the restriction of the already-canonical physical edge law to recipient modes **inside `P`**.  Internal traffic cancels, while viscosity and outward flow are losses.

This is the master-facing energy rule for a hard role even when a smooth envelope `Q` with `QP=P` transports its coefficient between events.  Holding `P` fixed here is only Fourier control-volume bookkeeping, not material/packet persistence.  `Q^2` remains an exact carrier observable, but positive work elsewhere in `Q` cannot supply terminal `P` energy.  Indeed for disjoint hard roles `P,R` and `Q=P+R`, work entering only `R` can increase `E_Q` while `E_P` is unchanged.  A remote hard event is therefore separate unless its actual inflow crosses into `P`; smooth-envelope overlap cannot relaunch the ancestry of `P`.

For the radial shell `A_M={(k,s):M/2<|k|<=M}` and `M E_M(t)>=mu_0`, this gives the previous cover `M E_M(s)>=theta mu_0` or `M Phi_in,M>=(1-theta)mu_0`; at `theta=1/5` the faces are `mu_0/5` and `4mu_0/5`.  Pressure, SGS, strain or service may expose indispensable geometry, but none is a third supplier of the kinetic energy stored in the hard role.

## 5. Radial crossing and hard-tail supply — EXACT

Specialize the modal donor flow to Fourier radii.  A donor/recipient atom crosses every sphere whose radius lies strictly between the donor and recipient radii.  Integrating crossings against `dR/R` gives the clipped log-radius displacement.  Equiradial transfer has zero radial action, so physical work does not imply one dyadic step or any universal event-count clock.

For the hard tail `|k|>N`, exact continuity gives

\[
N E_{>N}(t_1)+2\nu D_{tail}+N\Phi_{down}
=N E_{>N}(t_0)+N\Phi_{up}.
\]

Hence

\[
\boxed{N E_{>N}(t_0)+N\Phi_{up}\ge2\nu D_{tail}.}
\]

Tail dissipation is covered only by inherited tail stock or true low→high nonlinear supply.  High→high circulation is internal, `Phi_down` is a drain, and gross positive tail work is too broad to be called fresh supply.

### True-upward support split — EXACT

Disintegrate `Phi_up` by recipient shell `M`.

**Pure UV.**  If both interaction parents are above `M/4`, an energy donor with radius `<=N` forces the first recipient shell `M=2N`; triad geometry makes both parents comparable to `M`.  On these parents the resolved cutoff vanishes and `h=u` exactly.  The output-scale concentration factor is one by support, not by an estimate.  Signed-edge total variation plus the clean Young bound gives the natural-window route.

**Resolved contact.**  If one parent is `<=M/4`, exactly one parent is resolved and the other lies in `(M/4,5M/4]`.  Any deep direct upward jump `M>=4N` necessarily has resolved-scale parent contact.

These are support theorems about actual Fourier interactions; they do not create another work law or shell-dependent causal unit.  The common unit remains the parent-scale `N dW`.  Downstream, pure UV enters its first-shell natural window; resolved contact enters existing `K/S` or its bounded-parent HH natural window.  Thus internal nonlocal high→high traffic remains real modal redistribution but cannot survive as an independent **fresh tail-supply** recursion edge.

## 6. Resolved contact and interface work — EXACT

Let `V=S_{M/4}u`, `h=u-V`, and let `q` be a smooth low-parent cutoff.  Decompose the **signed** work first:

\[
dW=q\,dW+(1-q)dW=dW_{mixed}+dW_{HH}.
\]

Only then restrict the already-canonical positive cause:

\[
d\mu_{mixed}=q\,dW^+,
\qquad d\mu_{HH}=(1-q)dW^+.
\]

Contact is therefore not synonymous with interface work: a contact event may have `q=0` and be entirely HH.

For the mixed resolved operator, split signed-first into skew and symmetric parts `I=K+S`.  Then

\[
[I]_+\le[K]_++[S]_+.
\]

The skew part is same-event conservative role-to-role flux; the symmetric part is existing strain/deformation.  No proportional `K/S` owner matching is permitted.

## 7. Smooth carrier energy and observer quotient — EXACT

For a self-adjoint scalar Fourier analysis operator `A(t,D)`, put `eta=A^2`.  Direct differentiation gives

\[
\boxed{\frac d{dt}\|Au\|_2^2+2\nu\|\nabla Au\|_2^2
=\langle u,\dot\eta u\rangle-2\operatorname{Re}\langle\eta u,\mathcal B(u,u)\rangle.}
\]

With `V=S_{N/4}u`, `h=u-V`, the nonlinear term repartitions exactly into low-low, HH and the resolved linearized/interface operator.  On the selected outer support the low-low term vanishes by the support moat.

If the common analysis roles are transported by a certified skew generator `G`, require

\[
\dot A+[G,A]=0.
\]

That observer motion contributes zero channel-energy source.  After quotienting it, write the actual resolved skew operator as `K=G+K_phys`.  For synthesis roles `eta_a=A_a^2`,

\[
T^{phys}_{ab}=-2\operatorname{Re}\langle\eta_a u,K_{phys}\eta_bu\rangle,
\qquad T^{phys}_{ab}=-T^{phys}_{ba}.
\]

Thus smooth `K_phys` relink is a subset-boundary flux and has zero recursive generation depth.  The symmetric part remains actual strain/deformation.

An arbitrary time-dependent partition can move analysis-channel energy while `u` is fixed.  Therefore unbound role motion is observer motion, not a Navier–Stokes source.

## 8. Critical shell and physical first stops — EXACT-CONDITIONAL

Given an actual critical hard shell

\[
M\|P_Mu(t)\|_2^2\ge\mu_0>0,
\]

set `A=3M/4` and choose a smooth carrier `Q_A=1` on the shell.  With the normalized shell state as terminal probe,

\[
A|z(t)|^2\ge\frac34\mu_0.
\]

This theorem is supplier-independent: it does not know whether the shell was exposed by dissipation, fresh service, pressure structure, inherited stock or nonlinear supply.  It also does not invent supplier-relative scale progress.

Before assigning materiality, inspect only three backward monitors: renewed strain action, a role-interface coefficient obstruction, and an HH-regeneration coefficient obstruction.  Coefficient hits are **locators**, not work.  They must reenter the exact physical energy/work gate before inheritance, strain/interface work or HH generation gets an owner.

If no hit occurs over the full natural corridor, the same smooth carrier persists with a quantitative lower and yields actual bounded own-scale increment/heat service.  That service lives on the corridor already traversed; reading it adds zero recursion depth.  Material OO/ON/NN is read only afterward from the positive service law.

### First-stop semantics — EXACT

A physical first stop is the first physical time at which a named cause is met.  Exact simultaneous causes remain one joint cause set and one physical charge.  No lexicographic winner, fractional synthetic time or magnitude-based tie split is allowed.

Natural horizons and checkpoints are analysis segmentation, not events.  They do not reset cumulative monitors, terminal coefficients or carriers.  Interior checkpoint Zeno either meets an already-existing physical face or continues the same carrier; `t=0` is absorbing.

## 9. Inherited stock and material provenance — EXACT-CONDITIONAL / EXACT

For one event-anchored carrier/dual, suppose there is no named first stop, the earlier endpoint is a certified non-event slice, `E0>=E1/5`, and classified residual positive physical work is strictly below its own `E1/5` owner face.  Then the inherited component is between-time physical stock with zero generation depth.  It performs no later Hahn split and no temporal deposit matching.

A crucial historical correction is built into the hypothesis: large `E0` may coexist with simultaneous residual physical work.  The stock component must not erase that work owner.

Material ownership is downstream provenance.  Holding a positive service law fixed while changing only intrinsic old/new membership can change OO/ON/NN masses without changing total service.  Therefore material rereading creates neither work nor service.

For a selected-family update,

\[
R_{switch}=\sum_{C\in S_{old}\triangle S_{new}}E_C
\]

can be positive while the physical state and all cell increments are unchanged.  It is a boundary/bookkeeping quantity, not `dW`, stock, coefficient impulse or generation depth.

Raw names such as `material_relink` or `new_coherent_ancestry` are pre-owner locators.  They require independent native PDE evidence before recursion.

## 10. Source/SGS and pressure: exact derived physics, not automatic energy currencies

For a smooth spectral filter, the standard SGS transfer density is

\[
\Pi_t^{SGS}(x)=-\nabla\bar u:\tau_t(u,u).
\]

On the periodic/global divergence-free setting,

\[
\int\Pi_t^{SGS}(x)dx
=-\frac d{dt_{phys}}\frac12\|\bar u\|_2^2\Big|_{NL}
=\Pi^\delta(t),
\]

so the space-average SGS transfer is exactly the graded spectral nonlinear flux.  It is not a second transfer currency beside `dW`.

Changing the resolved cutoff repartitions the same full nonlinear law.  For a fixed smooth outer role, the reconstructed nonlinear forcing is `-Q B(u,u)` independent of which admissible resolved field was used to split it.

Differentiated SGS and pressure-Hessian terms are nevertheless real sources in **derived resolved-strain/gradient equations**.  They may control geometry, locate critical shells or break a recurrence regime.  “Source of a derived observable” must not be silently identified with “independent generator of global kinetic energy.”  This distinction is central to the current Mixed audit.


### Native objective-source state exhaustion — DISTILLED EXACT DEDUCTION

Current source routes expose only physical states already typed elsewhere: local/viscous source -> `D_V` -> hard shell; resolved pressure pair -> hard shell; SGS high service -> hard tail; SGS low service -> hard shell; independently certified interface/work cost may terminate.  ON/material labels and `old_pool_not_yet_eroded` are not events.

The low-SGS route needs no measurable choice of displacement.  For the already-fixed convolution filter set

\[
d\mu_G=|G(r)|dr/g_1,\quad g_1=\|G\|_1,\quad a(\tau,r)=\|\delta_ru(\tau)\|_3,\quad A(\tau)=\int a^3d\mu_G=Q(\tau)/g_1.
\]

On the smooth interval `(tau,r)->a` is Borel.  If `m_1=int a dmu_G>0`, put

\[
d\nu_\tau=(a/m_1)d\mu_G,
\]

and use `mu_G` when `m_1=0`.  `nu_tau` is a measurable reader kernel, not a causal probability.  With `S_j=M_j||delta_r u_j||_2^2`, pointwise LP/Bernstein and `m_1<=A^(1/3)` give

\[
\sum_j\int S_jd\nu_\tau
\ge\frac{A/m_1}{(C_{LP}C_B)^2}
\ge\frac{A^{2/3}}{(C_{LP}C_B)^2}
\ge C_Y\rho_R(\tau),
\qquad C_Y=\frac{380}{g_1(1+g_1)(C_{LP}C_B)^2},
\]

where the last step is exactly the certified SGS collision plus Germano bound.  The high-band estimate is pointwise in `r`, hence

\[
\sum_{j\ge1}\int S_jd\nu_\tau\le2d_{high}(\tau).
\]

Integrating scaled physical time,

\[
G_j:=\int\!\int S_jd\nu_\tau d\tau,\qquad Y_{tot}=C_Y\Sigma_R,
\qquad \boxed{\sum_{j\le0}G_j\ge Y_{tot}-2D_{high}}.
\]

Thus either `D_high>=Y_tot/4` and the physical hard-tail route applies, or total low service is at least `Y_tot/2`.  For `p_j=G_j/sum_(k<=0)G_k`, the pointwise capacity `S_j<=4M_j||u_j||_2^2`, time averaging and the two-hard-shell cover give at an actual time

\[
\boxed{\mu_{hard}\ge G_{j_*}/(6c)\ge p_{max}Y_{tot}/(12c)}.
\]

No selector `tau->r(tau)` is needed.  `nu_tau`, `(G_j)` and `H_inf^low-scale` are discarded after exposing the actual Fourier shell; they create no event, charge or scale progress.  Shell/tail energy then reroots by Sections 4--5 to earlier modal stock or actual nonlinear boundary inflow.  Material old/fresh/interface readings remain provenance unless an independent physical work/cost law exists.

A looser valid old-pool capacity bound can change `C_old>Y/8` without changing the field or realized service, so that threshold cannot define an event.  The historical old-pool half-life remains valid only on its separately supplied signed-good low-strain lineage and is not a generic source clock.


### Objective-source event -> physical-state relay — DISTILLED EXACT DEDUCTION

A source first hit remains a real event in the derived resolved-strain equation; its physical time and local/pressure/SGS/viscous provenance are not erased.  What changes is the **master leaf** attached to that event.

The exact source routing above is now exhaustive: local/viscous and resolved-pressure routes supply a hard shell; SGS supplies the hard tail or a material-free low/base hard shell; an independently present `Xi` cost may terminate.  The continuum master already distinguishes a certified **witness relay** from a new cause: a source law may imply shell mass with different units while creating neither a second causal charge nor a probability law.

Therefore a standalone historical

```text
RESOLVED_SOURCE -> RECURSE_CRITICAL
```

is no longer a canonical unresolved destination.  Keep the source event mark, then relay immediately to the certified terminal/shell/tail state.  If source ties with strain or actual work at the same physical time, keep the full joint cause set; the relay must not split or duplicate that event.

This is proof-graph contraction, not physical-event deletion.  Source/pressure/SGS remain exact geometry marks.  Their reader scale is not a causal parent scale: modal continuity reroots the exposed shell/tail to earlier stock or actual nonlinear inflow.  In the low-SGS frame `M_j=N2^j`, `j<=0`, the hard candidates are `M_j,2M_j`; the only candidate above `N` is exactly `P_(2N)={N<|k|<=2N}`, hence inherited tail stock or true `Phi_up`, while internal tail inflow is a separately typed hard-work event.  Source labels therefore mint no independent causal scale edge.

## 11. Pure tails and the first mixed subalphabet — EXACT / DISTILLED EXACT

### Consecutive high strain — EXACT

A high-strain event at scale `N_j` pays `D_j>=D_*`, exposes `M_j<=N_j/4`, and renews at `A_j=3M_j/4<=3N_j/16`.  Since `D_j<=N_jG_*`, `G_*=int||grad u||_2^2`, the geometric scale descent makes every consecutive high-strain epoch finite without treating `D_V` as a global reset.

### Consecutive signed-good generated HH — EXACT

After `Q^2` energy reentry selects actual positive HH work, the actual hard Fourier parent/child radii satisfy

\[
3/5<N_p/N_c<5/8.
\]

Parent natural lifetimes grow by more than `64/25`; the certified registration surfaces therefore backshift geometrically to absorbing `t=0`.  Local positive HH outside signed-good edge geometry is already on the canonical bad/transfer-loss route; the remaining local pre-generation seam is full-signed Young/Christ, not a separate “generic HH” owner.

### Parent-continuing high-strain / signed-good alternation, including exact ties — DISTILLED EXACT DEDUCTION

Start from a physical hard shell

\[
P_M:\quad M/2<|k|\le M,
\qquad A=3M/4,
\]

and its registered smooth `A`-carrier.  Consider the hard-shell ancestry whose genuine recursive events are high strain or **parent-continuing** signed-good generated HH; source-marked state handoffs, true-upward tail state relays / genuine hard-lineage switches, and the still-degenerate full-signed HH margin remain outside this subalphabet.

A high-strain continuation at carrier scale `A` renews at `<=3A/16`.  If the shell energy is instead genuinely supplied by signed-good nonlinear inflow, hard-role modal causality restricts that owner to actual recipient modes inside `P_M`.  Hence the physical HH child has `N_c<=M=4A/3`, and its signed-good parent satisfies

\[
N_p<\frac58N_c\le\frac58\frac43A=\frac56A.
\]

This remains true at an exact high-strain/HH tie.  The joint event is never split or ordered: the high-strain continuation is `<=3A/16`, while every signed-good continuation that actually supplies the carried shell has parent `<5A/6`.  Positive HH work elsewhere in the smooth envelope is a different physical event and cannot relaunch this shell ancestry merely by overlap with `Q`.

Therefore successive high-strain carrier scales satisfy

\[
A_{j+1}\le\frac56A_j.
\]

Since each high-strain event has `D_j>=D_*` and `D_j<=A_jG_*`,

\[
\#H\,D_*\le G_*\sum_jA_j\le 6A_0G_*.
\]

Thus only finitely many high-strain vertices occur even with arbitrary parent-continuing signed-good layers and exact H/HH ties.  After the last one, an infinite remaining tail would be consecutive signed-good generated HH and the existing parabolic registration theorem reaches absorbing `t=0` in finite depth.  Hence this shell-anchored parent-continuing two-mechanism alphabet has no infinite interior lineage.  No common mixed currency or synthetic clock is introduced.

## 12. Core anti-theorems and permanent guards

Do not use raw Duhamel mass as causal probability.  Do not re-Hahn after coarse-graining.  Do not use interaction cells as wallets.  Do not call high→high circulation fresh tail supply.  Do not infer a dyadic step from positive work.  Do not promote checkpoints to events or reset cumulative monitors.  Do not treat inherited stock as generation.  Do not treat material rereading or `R_switch` as source.  Do not treat smooth skew relink as generation.  Do not treat OO/ON/NN as generators of their service law.  Do not split simultaneous causes by a synthetic clock.  Do not turn normalized critical quantities into finite additive reset budgets.  Do not exchange entropy coordinates from different underlying measures as if they were one currency.

For every proposed frontier lemma ask: **what exact true Navier–Stokes structure makes this true that a generic averaged/bilinear model need not preserve?**  If the answer is only scaling, cancellation or a generic norm inequality, the physical mechanism has probably not yet been isolated.

## 13. What is theorem, what is not

The identities and structural laws above are exact or exact-conditional as labelled.  Randomized triads, Galerkin/FFT probes, CI runs and stress tests in the source repository are evidence against implementation mistakes, not mathematical substitutes for the continuum proofs.

Nothing here closes generic mixed recurrence, the degenerate full-signed Young/Christ seam, the remaining source/strain geometry-breaker coupling, or the initial/singular-time interfaces.  Those belong to `MIXED_FRONTIER.md`.
