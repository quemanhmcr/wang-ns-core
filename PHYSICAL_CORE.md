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

### Native hard-state last-entry theorem — DISTILLED EXACT DEDUCTION

For every bounded measurable event-anchored Fourier/helicity role `P`, exact mode-set continuity is

\[
\boxed{E_P(t)+D_P[s,t]+\Phi_{out,P}[s,t]=E_P(s)+\Phi_{in,P}[s,t]}.
\]

This is Kirchhoff stock/flow continuity, not temporal identity of an energy token.  Fix `t>0`, `e_1=E_P(t)>0` and `0<theta<1`.  If `{r<t:E_P(r)<=theta e_1}` is empty, then `E_P(0)>theta e_1`.  Otherwise put

\[
s_\theta=\sup\{r<t:E_P(r)\le\theta e_1\}.
\]

Continuity gives `E_P(s_theta)=theta e_1` and `E_P(r)>theta e_1` for `s_theta<r<=t`; the exact balance then gives

\[
\boxed{\Phi_{in,P}[s_\theta,t]\ge(1-\theta)e_1}.
\]

Thus a terminal hard state has an exact **last-entry alternative**: either the same physical mode set is already occupied above the `theta` level back to `t=0`, or actual canonical nonlinear boundary inflow enters `P` during its final occupied corridor.  `s_theta` is only a control-volume boundary, never an event or clock.  No FIFO/LIFO/proportional matching is introduced, and no inflow atom is declared to be the terminal stock.

Equivalently, `F(s)=Phi_in,P[s,t]` is a monotone **physical inflow corridor**: from the same balance `E_P(s)>=E_P(t)-F(s)`, so before the closed face `F=(1-theta)E_P(t)` the fixed hard state still has `E_P(s)>theta E_P(t)`; if that face never occurs before `t=0`, the stock reaches the initial boundary.  The only advancing quantity here is inherited canonical boundary flow, not a proof clock.

Consequently work elsewhere in a smooth envelope `Q` cannot continue the hard state merely because `QP=P`; it matters only when canonical inflow actually crosses into `P`.  For `P_M={M/2<|k|<=M}` with `M E_M(t)>=mu_0`, `theta=1/5` gives either `M E_M(0)>mu_0/5` or `M Phi_in,M[s_theta,t]>=4mu_0/5`.  Pressure, SGS, strain or service may expose the state, but none is a third supplier.  A `dW+` recipient charge lives at its work event; between events the persistent object is modal stock, not that charge carried through time.

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

Thus smooth `K_phys` relink is a subset-boundary flux and has zero recursive generation depth.  The symmetric part remains actual strain/deformation.  On a complete hard event-role partition its pair matrix is symmetric and reconstructs the same full resolved strain work; `S` is therefore not a fifth interface/source currency.  Its ontology is closed even though its recurrence handoff into the native strain/`D_V` telescope is a separate theorem question.

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

Natural horizons and checkpoints remain analysis segmentation, not events.  They do not reset cumulative monitors, terminal coefficients or carriers.  Interior checkpoint Zeno either meets an existing native face or continues the same carrier; coefficient faces remain locators until physical energy/work reentry, and `t=0` is absorbing.

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

No selector `tau->r(tau)` is needed.  `nu_tau`, `(G_j)` and `H_inf^low-scale` are discarded after exposing the actual Fourier shell; they create no event, charge or scale progress.  The resulting shell/tail state then enters the Section 4 last-entry alternative (or the tail balance of Section 5): boundary stock or actual canonical inflow, with no temporal matching.  Material old/fresh/interface readings remain provenance unless an independent physical work/cost law exists.

A looser valid old-pool capacity bound can change `C_old>Y/8` without changing the field or realized service, so that threshold cannot define an event.  The historical old-pool half-life remains valid only on its separately supplied signed-good low-strain lineage and is not a generic source clock.


### Objective-source event -> physical-state relay — DISTILLED EXACT DEDUCTION

A source first hit remains a real event in the derived resolved-strain equation; its physical time and local/pressure/SGS/viscous provenance are not erased.  What changes is the **master leaf** attached to that event.

The exact source routing above is now exhaustive: local/viscous and resolved-pressure routes supply a hard shell; SGS supplies the hard tail or a material-free low/base hard shell; an independently present `Xi` cost may terminate.  The continuum master already distinguishes a certified **witness relay** from a new cause: a source law may imply shell mass with different units while creating neither a second causal charge nor a probability law.

Therefore a standalone historical

```text
RESOLVED_SOURCE -> RECURSE_CRITICAL
```

is no longer a canonical unresolved destination.  Keep the source event mark, then relay immediately to the certified terminal/shell/tail state.  If source ties with strain or actual work at the same physical time, keep the full joint cause set; the relay must not split or duplicate that event.

This is proof-graph contraction, not physical-event deletion.  Source/pressure/SGS remain exact geometry marks.  Their reader scale is not a causal parent scale: the exposed shell/tail must instead satisfy its own modal last-entry/tail balance, which yields boundary stock or actual nonlinear inflow without creating an edge from the source scale.  In the low-SGS frame `M_j=N2^j`, `j<=0`, the hard candidates are `M_j,2M_j`; the only candidate above `N` is exactly `P_(2N)={N<|k|<=2N}`, hence inherited tail stock or true `Phi_up`, while internal tail inflow is a separately typed hard-work event.  Source labels therefore mint no independent causal scale edge.

## 11. Pure recurrence theorems and the hard-state energy spine — EXACT / DISTILLED EXACT

### Consecutive high strain — EXACT

A high-strain event at scale `N_j` pays `D_j>=D_*`, exposes `M_j<=N_j/4`, and renews at `A_j=3M_j/4<=3N_j/16`.  Since `D_j<=N_jG_*`, `G_*=int||grad u||_2^2`, the geometric scale descent makes every consecutive high-strain epoch finite without treating `D_V` as a global reset.

### Consecutive signed-good generated HH — EXACT-CONDITIONAL

On a supplied parent-continuing generated epoch, actual positive HH work has `3/5<N_p/N_c<5/8` and the exact chain `N_(c,j+1)=N_(p,j)`.  Parent lifetimes then grow by `>64/25` and the certified registration surfaces reach `t=0` in finite depth.  The spacetime law is the original `dW=C_FT(t,e)dt dlambda(e)` with one Hahn; signed-good restriction, unique donor, hard-parent self-probe and common-slice registration introduce no Gaussian causal mark.  The `5/8` control-volume theorem below removes that chain hypothesis from the hard-state energy-predecessor problem.

### `5/8` signed-good boundary-crossing theorem — DISTILLED EXACT DEDUCTION

No temporal chain `next child = previous donor` is permitted.  Refine any supplied finite hard state by the deterministic radial control-volume grid
\[
R_{m+1}=\frac58R_m,
\qquad C_m=\{R_{m+1}<|k|\le R_m\},
\]
intersecting the first/last cell with the supplied state when necessary.  This partition is only a reader of modal stock and boundary flow.

For every signed-good positive-work atom whose recipient lies in `C_m`, the certified triad theorem gives its unique same-time energy donor
\[
\frac35|k_c|<|k_d|<\frac58|k_c|\le R_{m+1}.
\]
Hence signed-good work into `C_m` can never be internal traffic: it is actual nonlinear boundary inflow.  Since `|k_c|>R_(m+1)`, also `|k_d|>3R_m/8>R_(m+3)`, so donor support lies only in `C_(m+1)` or `C_(m+2)`.  Bad/nonforward positive work remains on its existing terminal transfer-loss route.

This is a support theorem for the **same physical work event**.  The donor kernel adds provenance to canonical `dW+` with zero recursion depth; it does not turn the donor cell into a temporal ancestor, assign inflow atoms to terminal stock, or create a Markov/particle genealogy.  Multiple donor pieces are all retained; no winner, probability or re-Hahn is introduced.

Lift this same-time kernel by physical `dt`, restrict recipients to actual boundary inflow, and push donors to deterministic hard cells.  The resulting positive work-valued state-support law creates no charge/depth; for almost every donor event under that law the donor hard role is nonzero (otherwise its edge-work density vanishes).  Each such simultaneous donor state may therefore start its own fixed-mode inflow corridor from the same physical time, with no deposit matching.

Together with exact mode-set continuity, this yields the absolute kinetic-energy grammar for every fixed hard control volume:
\[
\boxed{
\text{final modal stock}+\text{viscous loss}+\text{outflow}
=\text{earlier modal stock}+\text{canonical boundary inflow}.
}
\]
Pressure/SGS source marks, high strain, symmetric strain work, service, material marks and conservative relink may all occur physically, but none can mint a third modal-energy supplier.  Internal nonlinear circulation remains real and cancels only from the control-volume divergence.

The same-time donor pushforward is only a **zero-depth state handoff**; temporal progress occurs only on the donor state's subsequent modal corridor.  This closes state rerooting but not Mixed no-escape: one must still prove that every surviving branch satisfies the native physical-time hypotheses, especially across genuine symmetric strain/deformation geometry.

## 12. Core anti-theorems and permanent guards

Do not use raw Duhamel mass as causal probability.  Do not carry a `dW+` charge through modal stock or infer temporal deposit matching from mode-set balance.  Do not re-Hahn after coarse-graining.  Do not use interaction cells as wallets.  Do not call high→high circulation fresh tail supply.  Do not infer a dyadic step from positive work.  Do not promote checkpoints to events or reset cumulative monitors.  Do not treat inherited stock as generation.  Do not treat material rereading or `R_switch` as source.  Do not treat smooth skew relink as generation.  Do not treat OO/ON/NN as generators of their service law.  Do not promote optional coherent-analysis thresholds—Gaussian aspect/radius, holonomy, flatness, sideband or reuse coordinates—to hard-lineage events: their actual consequences are existing strain/dissipation, modal state/work, terminal analysis cost, or no-hit continuation.  Do not split simultaneous causes by a synthetic clock.  Do not turn normalized critical quantities into finite additive reset budgets.  Do not exchange entropy coordinates from different underlying measures as if they were one currency.

For every proposed frontier lemma ask: **what exact true Navier–Stokes structure makes this true that a generic averaged/bilinear model need not preserve?**  If the answer is only scaling, cancellation or a generic norm inequality, the physical mechanism has probably not yet been isolated.

## 13. What is theorem, what is not

The identities and structural laws above are exact or exact-conditional as labelled.  Randomized triads, Galerkin/FFT probes, CI runs and stress tests in the source repository are evidence against implementation mistakes, not mathematical substitutes for the continuum proofs.

The hard-state **kinetic-energy layer** is exact: earlier modal stock and canonical boundary inflow are the only suppliers; viscosity/outflow are losses.  The `5/8` grid further proves that every signed-good positive inflow atom is a true boundary crossing whose same-time donor lies in one of the next two lower radial cells.  Donor provenance has zero recursion depth, so this is not yet a temporal no-escape theorem.  Full Mixed temporal/geometry assembly and the initial/singular-time interfaces remain open.  Degenerate Young/Christ remains only an auxiliary analysis seam.  See `MIXED_FRONTIER.md`.
