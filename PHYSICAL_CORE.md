# Physical Core

This file contains the smallest current theorem basis needed to stand at the mixed frontier.  It deliberately preserves physical type: stock is not work, work is not capacity, a witness is not a source, same-time redistribution is not between-time generation, and an observer coordinate is not a physical clock.
The reusable discipline behind these choices is stated in `CONTROL_VOLUME_METHOD.md`: begin from exact physical control-volume continuity, then use families of cuts as readers rather than inventing mechanisms.

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

For the already-used signed-good/bad **reader** on a forward edge, let `p_top=max(|x|,|y|)` and `ell_e=log_+(|z|/p_top)`.  Define the dimensionless geometric factor

`J_e=ell_e |s_x|x|-s_y|y|| |g_e|/|z|`,

the phase/orientation factor

`c_e=sign(s_x|x|-s_y|y|) Re[conj(a_z)conj(g_e)a_xa_y]/|g_e a_xa_ya_z|`

(with `c_e=0` on a zero interaction factor), and let `J_*` be the global sign-exhausted supremum of `J_e` on the admissible normalized edge geometry.  Then `m_e:=J_e/J_* in [0,1]`, `r_e:=m_ec_e`, and the physical edge formula above gives the exact registration identity

`T_e ell_e=A_e J_e c_e=A_e J_* r_e`.

Fix the repository reader threshold `eta0=10^-4`.  **Only after the one Hahn-positive law exists**, define its complementary measurable restrictions

`G={T_e>0, r_e>1-eta0}`,

`B_bad={T_e>0, r_e<=1-eta0}`.

Thus `dW+=dW+|_G+dW+|_(B_bad)` exactly.  `r_e,eta0` classify the already-existing physical positive edge law; they are not work, probability, owner, clock or NS-created threshold.  The symbol `B_bad` is reserved for this endpoint complement and is distinct from the later minority-helicity critical branch `B_crit`.

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

Consequently work elsewhere in a smooth envelope `Q` cannot continue the hard state merely because `QP=P`; it matters only when canonical inflow actually crosses into `P`.  For `P_M={M/2<|k|<=M}` with terminal `mu=M E_M(t)`, the occupied corridor satisfies `M E_M(r)>theta mu`; hence `M D_M[s_theta,t]>=(nu theta mu/2)M^2(t-s_theta)`.  For every natural length `ell=cM^-2`, partitioning only as a proof reader gives an actual interval `J subset [s_theta,t]`, `|J|<=ell`, with `M Phi_in,M(J)>=q_nat mu`, `q_nat=min(1-theta,nu theta c/4)>0`.  At a first contact of `M E_M=mu`, `M E_M<=mu` throughout the past.  **EXACT ANALYTIC ADDENDUM:** this next partition is a proof estimate, not part of the no-new-estimate distillation: split the positive recipient work on `J` by `K=max(|x|,|y|)` and fix `Lambda>2`.  If `K>=Lambda M` carries half the quantum, both parents are above `(Lambda-1)M` and canonical donor flow gives `A_down(J)>=(Lambda-2)q_nat mu/2`.  Otherwise `kappa<=2Lambda^2M^2`; with the edge-fiber mass `pi R`, `kappa/R>=|q|>=M/2` and `int_J E_M<=c mu/M^3`, Cauchy gives `int_J K2_edge^comp dt>=q_nat^2 mu/(64pi cLambda^2)`.  At `theta=1/5` the coarser last-entry alternative remains `M E_M(0)>mu/5` or `M Phi_in,M>=4mu/5`.  No window is promoted to an event, and no inflow atom is matched to terminal stock.

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

## 6. Resolved contact and symmetric-strain donor quotient — EXACT / DISTILLED EXACT

Let `V=S_(M/4)u`, choose the decomposition gauge `0<=q<=1` on the resolved parent, and write signed-first
\[
dW_{mixed}=q\,dW,\qquad dW_{HH}=(1-q)dW;
\]
only afterward inherit `dmu_mixed=q dW+`, `dmu_HH=(1-q)dW+`.  Thus contact may be 100% HH when `q=0`; no later Hahn is taken.

Now fix one closed helical triad with its unique resolved low root `p` and the two unresolved roots `k,l`.  Let `T_p+T_k+T_l=0` be the canonical root works.  The two physical mixed high-root works are `qT_k,qT_l`.  Their skew pair is antisymmetric and their symmetric pair is equal, hence
\[
\boxed{2S_{kl}=q(T_k+T_l)=-qT_p}.
\]
For a smooth square-role energy weight `eta=Q^2`, the same triad contributes
\[
S_{eta,tri}=-\alpha_{tri}T_p,\qquad
\alpha_{tri}=\tfrac q2(\eta(k)+\eta(l))\in[0,1].
\]
Therefore `[S_eta,tri]_+=alpha_tri[-T_p]_+`: fine positive symmetric strain work is a positive restriction of the **original canonical low-root `dW-`**, not a new Hahn law.  After any deterministic coarsening, `[pi#dS]_+<=pi#(alpha dW-)`; the cyclic donor kernel pushes that inherited restriction to existing canonical `dW+` at the same physical time.  Every such recipient is canonical bad work: if it is below the other unresolved root it is nonforward; otherwise its resolved interaction parent is `<1/2` of the child, contradicting the signed-good `3/5` lower bound.  Thus symmetric interface work adds no recursive owner; `K` remains zero-depth conservative relink and `S` reroutes to terminal bad-positive work.  Changing the resolved cutoff only repartitions the same `-Q B(u,u)`, so this quotient does not change the NS law.

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

This is proof-graph contraction, not event deletion.  Source/pressure/SGS remain exact geometry marks, but each exposed shell/tail obeys its own modal balance.  Local/pressure shells have `H<=N/4`; low/base SGS has `H<=2N`; high SGS is a tail above `N`.  If the state is inherited, generation depth is zero; bad/nonforward inflow terminates.  On any surviving good boundary inflow the donor lies below the shell lower face, so `N_next<=H/2`, while true tail inflow has donor `<=N`.  Hence every nonterminal source-state-work composite satisfies `N_next<=N_source`; source labels cannot mint a UV reset.

## 11. Pure recurrence theorems and the hard-state energy spine — EXACT / DISTILLED EXACT

### Consecutive high strain — EXACT

A high-strain event at scale `N_j` pays `D_j>=D_*`, exposes `M_j<=N_j/4`, and renews at `A_j=3M_j/4<=3N_j/16`.  Since `D_j<=N_jG_*`, `G_*=int||grad u||_2^2`, the geometric scale descent makes every consecutive high-strain epoch finite without treating `D_V` as a global reset.

### Consecutive signed-good generated HH — EXACT-CONDITIONAL

On a supplied parent-continuing generated epoch, actual positive HH work has `3/5<N_p/N_c<5/8` and the exact chain `N_(c,j+1)=N_(p,j)`.  Parent lifetimes then grow by `>64/25` and the certified registration surfaces reach `t=0` in finite depth.  The spacetime law is the original `dW=C_FT(t,e)dt dlambda(e)` with one Hahn; signed-good restriction, unique donor, hard-parent self-probe and common-slice registration introduce no Gaussian causal mark.  The `5/8` control-volume theorem below removes that chain hypothesis from the hard-state energy-predecessor problem.

### Mixed `H/G` reduction — DISTILLED EXACT DEDUCTION

On each carried-root branch, after stock/source/interface/material quotients, the only depth-increasing interior edges are high strain `H` and signed-good work `G`.  Both reduce carried hard-state scale by at least the common factor `5/8` (`H` gives `3/16`).  Hence `#H D_*<=G_* sum_j N_j<= (8/3)N_0G_*`; exact ties retain both contracting branches.  Every infinite interior branch would therefore be eventually pure `G`.  No temporal identity of a work charge is used.

### Critical radial first moment + hard-shell collision — EXACT
On every compact smooth slab, `C_(1/2)=int |k||uhat|^2=||u||_Hdot^(1/2)^2` obeys `C_(1/2)(t)+2nu D_(3/2)+A_down=C_(1/2)(0)+A_up`, `D_(3/2)=int_0^t||u||_Hdot^(3/2)^2`.  A signed-good triad has `9/25 < P_G/(rho_c W_c+) < 5/12`, hence `(9/25)int rho_c dW_G<=C_(1/2)(t)+2nu D_(3/2)+A_(down,notG)`.  For one closed triad donor atom, `M_(d->r)<=min(|T_d|,|T_r|)` and `|T_i|<=4rho_i|a_0a_1a_2|`; triangle closure therefore gives `|rho_r-rho_d|M_(d->r)<=4LK|a_0a_1a_2|`, `L=min rho_i`, `K=max rho_i`, with at most two flows.  Dyadic annuli are proof readers only: the two high roots are comparable, low-root Fourier `L1` gives `(L/K)^2`, and the geometric kernel is summable.  Thus, with the physical radial concentration `mu_sh(t)=sup_(M>0) M||1_{M/2<|D|<=M}u(t)||_2^2`, `v_rad(t):=int|rho_r-rho_d|dM_t <= C_sh sqrt(mu_sh(t))||u(t)||_Hdot^(3/2)^2` for one universal `C_sh<infinity`.  Consequently `dC_(1/2)/dt+(2nu-C_sh sqrt(mu_sh))||u||_Hdot^(3/2)^2<=0`; whenever `dC_(1/2)/dt>0`, an actual hard shell satisfies `M||P_Mu||_2^2>(2nu/C_sh)^2`.  There is no separate helical-recycling ledger either.  Put `x=s|k|`.  The cyclic root formula also gives `sum_i x_iT_i=0`; donor-kernel marginals imply `sum_(d->r)(x_r-x_d)M=0`.  A nonzero triad has at most two flows, and all helicity-flip flows have one orientation, so their signed-radius displacement is balanced by same-helicity radial displacement.  Hence `V_x:=int|x_r-x_d|dM<=2V_rho`, `V_rho=int|rho_r-rho_d|dM`.  Same-helicity outflow is radial layer-cake traffic; helicity-flip outflow is signed-radius layer-cake traffic controlled by the same `V_rho`.  The critical stock itself has the exact grid-free shell layer cake `C_(1/2)(t)=int_0^infinity mu(R,t)dR/R`, `mu(R,t)=R||P_(R/2,R]u(t)||_2^2`, because each Fourier radius `rho` is counted for `R in [rho,2rho)`.  Its nonlinear production has an equally exact helical disintegration.  For a homochiral closed triad, signed-helicity conservation gives `sum rho_i T_i=0`.  For a heterochiral triad with minority-helicity root `m`, energy plus signed-helicity conservation gives `sum rho_i T_i=2 rho_m T_m`; hence `C_(1/2)(t)+2nu D_(3/2)=C_(1/2)(0)+2 W_min^signed[0,t]`.  If `T_m>0`, its two interaction parents have the same helicity, so the edge is never `G`.  More sharply its native efficiency obeys `r_e<=99/100`: outside the certified local stability rectangle `J/J_*<=99/100`, while inside `u=log(y/x)<=2/25` gives `(y-x)/(x+y)=tanh(u/2)<1/25` and `P_same/P_opp<3/25`.  Thus every positive creator of critical stock is a canonical minority-helicity `B_crit` edge with at least `1/100` physical efficiency deficit; if `C_(1/2)` blows up, the radius-weighted positive minority `B_crit` work must diverge.  The whole closed-triad radial/helicity law is one-dimensional in signed curl.  Put `x_i=s_i rho_i`, `Z_tri:=sum rho_i^2T_i`, and order distinct roots `alpha<beta<gamma`.  Exact cyclic work gives `Z_tri=R_tri(x_0-x_1)(x_0-x_2)(x_1-x_2)` and `T_alpha=Z_tri/[(beta-alpha)(gamma-alpha)]`, `T_beta=-Z_tri/[(beta-alpha)(gamma-beta)]`, `T_gamma=Z_tri/[(gamma-alpha)(gamma-beta)]`.  Hence the canonical donor graph is exactly the path `alpha--beta--gamma`; with `D=|Z_tri|/(gamma-alpha)`, `M_(alpha,beta)=D/(beta-alpha)` and `M_(beta,gamma)=D/(gamma-beta)`, so the two legs carry equal absolute signed-curl displacement `D`.  `Z_tri>0` orients median→extremes and `Z_tri<0` extremes→median; radial traffic is only the fold `rho=|x|`, giving exactly `V_(rho,tri)=D[||beta|-|alpha||/(beta-alpha)+||gamma|-|beta||/(gamma-beta)]`.  If two `x` coincide, the third work vanishes and any surviving exchange is same-helicity/equiradial with `Z_tri=V_(rho,tri)=0`.  This subsumes all four old low-recipient classes and all other radial donor fates.  Homochiral critical production is zero; heterochiral `sum rho_iT_i=2rho_mT_m` has the sign of `Z_tri`.  `Z_tri` is triad enstrophy production, not a new global ledger/reset currency; convex UV moments remain unbounded.  Full-convolution cancellation of that channel has a more primitive vector source object.  For fixed child `q` and same-helicity parents write `p=(q+r)/2`, `m=(q-r)/2`; `kappa=(|q|^2+|r|^2)/2`, so an equal-heat unordered fiber is the physical separation sphere `S^2/(r~-r)=RP^2`.  The unordered Leray vector orbit coefficient in `q^perp` has exact norm `||F_q(r)||=|q.r||qxr|sqrt((P+M)^2+Q^2)|a_pa_m|/[4PMQ(P+M)]`; hence its only nondegenerate geometric zeros are the equal-radius Beltrami equator and collinear shear pole.  Minority and spin-two majority source laws are only the two helical coordinates of this vector.  If `dF=xi d sigma`, `||xi||=1`, then `sigma(Omega)^2-||int dF||^2=(1/2)int int||xi-xi'||^2d sigma d sigma'`; every off-diagonal atom is an actual Fourier diamond.  Its geometric source line is `ell_q=[t_q+i h beta n]`, `beta=Q/(P+M)`, with exact projective separation `1-|<zhat,zhat'>|^2=[(beta-beta')^2cos^2psi+(1-beta beta')^2sin^2psi]/[(1+beta^2)(1+beta'^2)]`.  Thus the only generic nontrivial same-line heat-fiber pair is the planar cross-isospectral reflection rectangle.  If `r=u+Zqhat`, its two remaining non-Beltrami cross outputs `q+-u` satisfy `G_side/G_0=|Z|/sqrt(Q^2+U^2)*sqrt(((P+M)^2+Q^2+U^2)/((P+M)^2+Q^2))`; exact two-atom cancellation therefore leaks unless `Z=0`, where the original source itself is Beltrami-null.  Projective disintegration is exact: with `lambda=ell_#sigma`, conditional probability `nu_ell`, `b(ell)=int xi dnu_ell`, `S=sigma(Omega)`, one has `S^2-||F||^2=S int(1-||b||^2)d lambda+(1/2)int int||b-b'||^2d lambda d lambda'`, and the between-line term is bounded below by `(1/2)int int||b||||b'||D_proj d lambda d lambda'`.  This classifies actual vector-source cancellation but is not a new source/work law.  The downstream diamond incidence has an exact **analytic coarea on actual Fourier coordinates**; this is not a primitive NS source measure.  For two unordered same-output parent orbits and the `1/2` symmetry interchanging them, generic equal-heat incidence is `dXi=(1/8)dq dp dp' delta(kappa_q(p)-kappa_q(p'))`; because `kappa_q(p)-kappa_q(p')=2(p-p').(p+p'-q)`, coarea yields `dXi=dp dp' dH^2(y)/(16|p-p'|)`, `y perp(p-p')`, with modes `p,p',p'+y,p+y` and all four non-original pairings retained.  Do not Hahn-split the vector orbit source after helicity coarse-graining.  Its `RP^2` law above is source geometry only.  A helicity-resolved **derived source diagnostic** on the same pre-Hahn canonical edge is the edge-source square: if `f_e` is the child-helicity source amplitude of one unordered complete parent-helicity edge before Hahn, `S2_edge:=int|C_F f_e|^2dLambda_edge<=2C_F^2E||grad u||_2^2`, hence `int_0^T S2_edge dt<=C_F^2E_*^2/nu`.  For fixed child helical mode `(q,s)` and `kappa=(|q|^2+R^2)/2`, parent-helicity counting gives exact edge-fiber base mass `pi R`.  If `(S,F,L2)` are edge-source variation/resultant/square and `P,N` are the positive/negative parts of the same canonical signed edge work, pairwise complex-Hilbert variance gives `S^2-|F|^2>=PN/|a_(q,s)|^2` while Cauchy gives `S^2-|F|^2<=pi R L2`; hence `PN/(pi R|a_(q,s)|^2)<=L2_edge` (zero when `a_(q,s)=0`), and `F=0` implies `P=N`.  Thus persistent same-heat cancellation forces a lower bound on this **edge-source-square diagnostic**, with one Hahn only; it is not a new work/source currency.  The edge source itself has an exact PDE: for `f_e=C_ea_xa_y`, `(partial_t+nu kappa_e)f_e=g_e=C_e(n_xa_y+a_xn_y)`.  Hence `0.5 dS2_edge/dt+nu K2_edge=R_edge`, `K2_edge=int kappa_e|C_Ff_e|^2dLambda_edge`.  Exact source normalization gives `|C_e|^2/kappa_e<=2`; after child-helicity sum and unordered quotient, `G_(-1,edge):=int kappa_e^-1|C_Fg_e|^2dLambda_edge<=4C_F^2E||N||_2^2` for the full modal NS source `N=-P(u.grad u)=P(u x omega)`.  Rotational NS also gives the orthogonal split `u x omega=N+grad(p+|u|^2/2)`, with `<u,N>=0` and `<N,-Delta u>=int omega.S omega`; pressure is the gradient complement of the same Lamb vector, not another supplier.  Thus `0.5 dS2_edge/dt+(nu/2)K2_edge<=(2C_F^2E/nu)||N||_2^2`.  A natural window may have only `O(M^-2)` unweighted `S2_edge`; the first-contact Cauchy estimate forces an **order-one lower bound on the derived `K2_edge` diagnostic** on the comparable proof branch.  This is not native NS energy dissipation.  Transfer deficit/diamond variance is never declared dissipation or a finite budget.  The weak cross-pair faces have an intrinsic PDE description: for a same-helicity component `v_h`, `B=inf_K||(curl-hK)v_h||_2` and `S=inf_|e|=1[int(1-(k.e)^2/|k|^2)|vhat_h|^2]^(1/2)` vanish exactly on Beltrami eigenspheres and Fourier-line shears.  With `C_F=(2pi)^(-3/2)`, `N(v_h)=P(v_h x curl v_h)` obeys `sup_q|Nhat(q)|<=C_F||v_h||_2 B` and, on `|k|<=Kmax`, `sup_q|Nhat(q)|<=2C_F Kmax||v_h||_2 S`; surviving same-helicity source is therefore separated from both nonlinear-null manifolds.  For fixed child `q`, every parent source atom also obeys `(partial_t+nu kappa_q)f=C_q(N_p a_r+a_pN_r)`, `kappa_q=|p|^2+|r|^2`; absent parent forcing, persistent net cancellation on an interval is Laplace-unique and must occur fiberwise in `kappa`.  Source/state geometry is not promoted to `dW+`.  Bounded shell amplitude on bounded log-width still cannot blow up merely by translating to UV.
The signed triad field `Z_tri` integrates exactly to the primitive global enstrophy source; one triad contribution is not a second work law or global owner.  Let `Q(t)=int omega.S omega`.  Root-marking gives `C_F int Z_tri dLambda_tri=int rho_z^2 dW=2Q`.  For `A=grad u=S+Omega`, `Omega omega=0` and trace-free `3x3` algebra give pointwise `omega.S omega=4(det A-det S)`; Piola gives `3det A=div[(cof A)^T u]`, hence on the smooth finite-energy `R^3` state `Q=-4int det S=-(4/3)int tr(S^3)=4int lambda_1lambda_2(-lambda_3)`.  The exact `H1` stock law is `0.5||grad u(t)||_2^2+nu int_0^t||Delta u||_2^2=0.5||grad u_0||_2^2+int_0^tQ`; therefore every finite singular endpoint has `sup_(t<T*)int_0^tQ=+infinity`.  Instantaneous signed cancellation is nevertheless real: the isolated-dilate anti-theorem has `Z_L=-Z` with `V_(rho,L)>0`, and pure-UV upward atoms occur with both `Z_tri` signs.  Pressure itself has a sharper exact type.  Put `g=-Delta p=|S|^2-|omega|^2/2` and `H0=Hess p+(g/3)I`.  For `z!=0`, `H0hat(z)=(I/3-zhat tensor zhat)ghat(z)` and `ghat(z)=-C_F int(z.uhat(x))(z.uhat(z-x))dx`.  One unordered parent pair has bare `g_(x,y)=-2(z.u_x)(z.u_y)`; for helical parent modes its geometric magnitude is `|xxy|^2|a_xa_y|/(|x||y|)`, so nonzero-amplitude pressure pairs vanish only at collinearity.  Thus all pair tensors at fixed `z` share one tensor line; exact two-pair pressure cancellation can coexist with nonzero Leray source.  In real space `H0=(4pi)^-1 PV int_0^infinity dr/r int_(S^2)(3n tensor n-I)g(x-rn)dOmega`, an exact `l=2` quadrupole extraction.  The elliptic map alone has no sign rigidity: for every symmetric trace-free `M`, `(4pi)^-1 int_(S^2)(3n tensor n-I)(n.Mn)dOmega=(2/5)M`; what is NS-specific is that `g` is the quadratic source of the same `u`.  At `omega!=0`, set `xi=omega/|omega|`, `P=I-xi tensor xi`, `a=xi.Sxi`, `b=P S xi`, `D=P S P+(a/2)P`, `tau=xi.H0xi`.  Then `S=a xi xi+xi b+b xi-(a/2)P+D`, `|S|^2=3a^2/2+2|b|^2+|D|^2`, `D_t|omega|=a|omega|+nu xi.Deltaomega`, `D_txi=b+(nu/|omega|)P Deltaomega`, and `D_ta=-a^2/2+5|b|^2/3+|D|^2/3-|omega|^2/6-tau+nu[2b.Deltaomega/|omega|+xi.(Delta S)xi]`.  Same-helicity equal-radius pairs are gradient-only/Bernoulli nulls after Leray, whereas collinear shear has zero raw convective and pressure pair.  `H0,tau` are pressure geometry, never kinetic-energy suppliers, work laws or currencies.
### Pressure quotient retained after closure — DISTILLED EXACT DEDUCTION
Put `g=-Delta p=|S|^2-|omega|^2/2`, `H0=Hess p+(g/3)I`, and `N=-P(u.grad u)`.  For every `k!=0`, incompressibility gives `H0hat=(I/3-khat tensor khat)ghat`, `S_hat:H0_hat=0`, `|Hess(p)_hat|^2=|g_hat|^2`, `|H0_hat|^2=(2/3)|g_hat|^2`, while the projected PDE is `partial_t S=sym grad N+nu Delta S`.  Hence pressure is modewise orthogonal geometric redistribution, not a second modal `H^1` source; `||H0||_2^2=(2/3)||g||_2^2`, `<S,H0>=0`, and `0.5 d||S||_2^2/dt+nu||grad S||_2^2=0.5 int omega.S omega`.
At `omega!=0`, the actual vorticity frame splits strain and tidal pressure into `1+2+2` pieces `(a,b,D)` and `(tau,c,E)`, with `a=xi.Sxi`, `b=P S xi`, `D=P S P+(a/2)P`, `tau=xi.H0xi`, `c=P H0 xi`, `E=P H0 P+(tau/2)P`.  Exact pairing is `S:H0=3a tau/2+2b.c+D:E`, whose space integral is zero; pressure can reorient longitudinal/turning/transverse strain geometry but cannot mint total strain-square source.  The exact three-sine torus witness `psi=sin x+sin y-sin(x+y)`, `u=(psi_y,-psi_x,0)` has `u=grad u=S=omega=g=0` at the origin but `Hess p(0)=[[0,-1/5,0],[-1/5,0,0],[0,0,0]]`, so no pointwise `Hess p=F(S,omega)` or finite local first-jet pressure bound exists.  These facts are retained as geometry guards only; the dynamical closure below removes pressure from the state entirely.

### Pressure-free vorticity closure + Biot--Savart two-point geometry — DISTILLED EXACT DEDUCTION
On a smooth sufficiently decaying incompressible `R^3` state,
\[
u[\omega]=\nabla\times(-\Delta)^{-1}\omega,
\qquad
S[\omega]=\operatorname{sym}\nabla\nabla\times(-\Delta)^{-1}\omega,
\]
and Navier--Stokes is equivalent to the pressure-free closed equation
\[
\partial_t\omega+(u[\omega]\!\cdot\nabla)\omega
=(\omega\!\cdot\nabla)u[\omega]+\nu\Delta\omega
=S[\omega]\omega+\nu\Delta\omega.
\]
Conversely this vorticity equation reconstructs the momentum law, with pressure only the longitudinal Hodge completion.  Before curl, if `R:=-(u.grad)u`, then `Rhat=Nhat+ik ghat/|k|^2` and `|Rhat|^2=|Nhat|^2+|ghat|^2/|k|^2`; `sym grad` preserves the orthogonal split.  Pressure is therefore a dependent reconstruction, never a second source road.
For one physical particle, if `F=grad_a X` then `Fdot=A(X,t)F`, `det F=1`, and the exact Cauchy-defect law is `d[F^-1 omega(X,t)]/dt=nu F^-1 Delta omega(X,t)`: inviscid vorticity is carried by volume-preserving deformation and viscosity is the sole frozen-in defect.

Biot--Savart gives
\[
S(x)=\frac{3}{8\pi}\,PV\!\int
\frac{(h\times\omega(x+h))\otimes h+h\otimes(h\times\omega(x+h))}{|h|^5}\,dh.
\]
For `W=|omega(x)|>0`, `xi=omega/W`, `n=h/|h|`, the longitudinal strain is the pure Cartesian `l=2` angular readout `a=(3/4pi)PV int (xi.n)((xi cross n).omega(x+h))|h|^-3 dh`.  After integrating and symmetrizing,
\[
Q:=\int\omega\!\cdot S\omega\,dx
=\frac{3}{8\pi}\iint
\frac{[(\omega_y-\omega_x)\!\cdot h][(\omega_x\times\omega_y)\!\cdot h]}{|h|^5}\,dx\,dy.
\]
Both numerator factors are `O(|h|^2)` near the diagonal.  With `deltaomega=omega_y-omega_x`, `baromega=(omega_x+omega_y)/2`, this pair integrand is exactly `|h|^-3 (deltaomega.n)[(baromega cross deltaomega).n]`: one zero manifold is longitudinal-increment null, the other is vortex-pair coplanarity/chirality null.  This is the same global scalar as `(C_F/2)int Z_tri`, not a triad-to-spatial-pair matching or a new Hahn law.

There is an exact anti-theorem against any **atomwise first-contact -> positive-stretching** map.  In the homochiral closed spectrum `1<sqrt(2)<sqrt(3)`, take the radial cut `R=6/5` and any crossing mass `m>0`.  Choosing `Z_A=-(sqrt(2)-1)(sqrt(3)-1)m` gives a canonical upward donor atom `1 -> sqrt(2)` of mass `m` with `Z_A<0`.  Dilate the same nondegenerate triad by `lambda=sqrt(2/3)` and choose `Z_B=(sqrt(2)-sqrt(2/3))(sqrt(2)-2/sqrt(3))m>0`; then `2/sqrt(3) -> sqrt(2)` crosses the **same** cut with the **same** mass and `Z_B>0`.  An `SO(3)` rotation identifies the second `sqrt(2)` child wavevector/helicity with the first, and the nonzero Waleffe coefficient plus amplitude/phase scaling realizes either signed `Z`.  Thus even exact child mode, cut and positive boundary-inflow amount do not determine the sign of triad stretching or of `Q`.

The two-point source nevertheless has an exact **material** dynamics.  Let `x=X(a,t)`, `y=X(b,t)`, `h=y-x`, `r=|h|`, `n=h/r`, `omega_x=omega(x,t)`, `omega_y=omega(y,t)`, and define
\[
L=(\omega_y-\omega_x)\!\cdot h,
\qquad C=(\omega_x\times\omega_y)\!\cdot h,
\qquad K=LC/r^5.
\]
Put the actual secant gradient `Abar=int_0^1 grad u(x+theta h)dtheta`, `Sbar=sym Abar`.  Fundamental calculus and incompressibility give `hdot=Abar h`, `tr Abar=0`, and `rdot/r=n.Sbar n`.  The endpoint deviations are not new defects/currencies but exact curvature readings,
\[
E_x:=A_x-Abar=-\int_0^1(1-\theta)(h\!\cdot\nabla)A(x+\theta h)d\theta,
\quad
E_y:=A_y-Abar=\int_0^1\theta(h\!\cdot\nabla)A(x+\theta h)d\theta.
\]
Using `D_t omega=A omega+nu Delta omega` and the trace-free determinant identity gives
\[
\dot C=\det(E_x\omega_x,\omega_y,h)+\det(\omega_x,E_y\omega_y,h)
+\nu[\det(\Delta\omega_x,\omega_y,h)+\det(\omega_x,\Delta\omega_y,h)],
\]
\[
\dot L=2(\omega_y-\omega_x)\!\cdot Sbar h+(E_y\omega_y-E_x\omega_x)\!\cdot h
+\nu(\Delta\omega_y-\Delta\omega_x)\!\cdot h,
\qquad
\dot K=r^{-5}(C\dot L+L\dot C)-5(n\!\cdot Sbar n)K.
\]
Thus a common incompressible affine deformation can change the longitudinal factor and separation metric but cancels **exactly** from `dot C`; departure from the chirality-null manifold can only come from actual velocity-gradient curvature along the material segment or from viscosity.  By contrast the longitudinal-null manifold can be left by common strain.  These are two physically different zeros of the same primitive source.

Because `det grad_a X=1`, the global source is also exactly material:
\[
Q(t)=\frac{3}{8\pi}\iint K(a,b,t)\,da\,db.
\]
At a finite singular endpoint, smoothness before `T_*` and the `H^1` stock identity imply for **every** `t_0<T_*`, `sup_(t_0<t<T_*) int_(t_0)^t Q(s)ds=+infinity`.  Hence after every arbitrarily late UV first contact there is unbounded future cumulative signed material-pair source along a subsequence, but the same-child opposite-`Z` anti-theorem forbids assigning that source atomwise to the contact.

### Relative-translation anti-correspondence — DISTILLED EXACT DEDUCTION
The remaining proposed `traffic -> material-pair spacetime` bridge is itself not a canonical NS object.  An exact finite-Fourier torus witness makes the information loss explicit.  Let the real divergence-free active support be the signed copies of
\[
A=\{(-1,-1,-1),(0,1,1),(1,0,0)\},\qquad
B=\{(-7,1,-3),(3,0,2),(4,-1,1)\},
\]
with positive representatives `u_k=(k_2,-k_1,0)` on the first two roots of each family and `i(k_2,-k_1,0)` on the third, and `u_(-k)=conj(u_k)`.  The only active zero-sum triples are `+-A` and `+-B`; there is no mixed closed triad.  Translate **only** family `B` by `delta=(pi,0,0)`, i.e. `u_k -> (-1)^(k_1)u_k` on `B`.  Modal stocks are unchanged, and every active cubic modal work is unchanged exactly because each surviving work triple is internal and its translation phases multiply to one.  Hence the normalized global stretching source `Qbar=(2pi)^(-3)int_(T^3) omega.S omega` is the same in both states; in this normalization `Qbar=-980`.

Nevertheless the true Navier--Stokes first temporal jet is different.  The supports have the mixed quartet
\[
(1,0,0)+(0,-1,-1)+(3,0,2)+(-4,1,-1)=0,
\]
whose `B` subtotal has odd translation parity.  Exact rational Fourier algebra for arbitrary `nu>=0` gives
\[
\dot Qbar_0=88032\nu+\frac{2313812704337343896}{175710969288855},\qquad
\dot Qbar_\delta=88032\nu+\frac{235658282866142488}{15973724480805},
\]
so
\[
\boxed{\dot Qbar_\delta-\dot Qbar_0=\frac{87152}{55}\ne0}
\]
independently of viscosity.  Thus even **full instantaneous modal stock + all active canonical work + the scalar `Q`** do not determine the next stretching-source derivative: cubic traffic has quotiented away relative phase geometry that the quartic NS time jet still sees.  Spatial `q(x)`, pair `K(a,b)` and segment-curvature readings can likewise change under the same relative translation while the entire instantaneous traffic law is fixed.

Therefore there is no missing canonical contact/traffic-to-material-pair bridge to discover.  Both are exact readings of the full primitive state `u`/`omega`, but neither is a sufficient state for the other or for the next NS time jet.  The representation frontier is **exhausted**: any further regularity theorem must act directly on the full pressure-free vorticity PDE (equivalently the full NS state and its exact material/Biot--Savart laws), not manufacture a new owner, budget, coherence coordinate, or genealogy linking two lossy quotients.

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

For the low ball `L_R={|k|<=R}`, exact continuity gives `E_<=R(t)+D_<=R+Phi_up=E_<=R(0)+Phi_down`; hence any signed-good layer crossing `R` obeys `mu_G<=Phi_up<=E_<=R(0)+Phi_down`.  Since `Phi_down` is nonforward positive child-work into `|k|<=R`, continuum variation yields `Phi_down[0,t]<=4sqrt(2)C_F t E_*^(3/2)sqrt(4pi/5)R^(5/2)`, and, because `E_<=R(0)->0` for `u_0 in L^2(R^3)`, `Phi_up(R;[0,t])->0` as `R->0`, with `E_*=||u_0||_2^2`.  This is IR funding/extinction, not a budget that may be charged once per cut.

Together with exact mode-set continuity, this yields the absolute kinetic-energy grammar for every fixed hard control volume:
\[
\boxed{
\text{final modal stock}+\text{viscous loss}+\text{outflow}
=\text{earlier modal stock}+\text{canonical boundary inflow}.
}
\]
Pressure/SGS source marks, high strain, symmetric strain work, service, material marks and conservative relink may all occur physically, but none can mint a third modal-energy supplier.  Internal nonlinear circulation remains real and cancels only from the control-volume divergence.

The same-time donor pushforward is only a **zero-depth state handoff**; no temporal token is created.  Radial-cut funding and the total-variation collision control the resulting traffic directly.

### Endpoint `G/B_bad` notation + exact side-recipient algebra — EXACT

Recall the exact same-Hahn restrictions `G,B_bad` from §2.  The endpoint complement `B_bad` is not the final full-state `B`: reserve `B_crit` for the positive minority-helicity critical branch determined by the exact identity `sum_i rho_i T_i=2 rho_m T_m` on a heterochiral triad (and `sum_i rho_iT_i=0` on a homochiral triad).  Thus the `G/B_bad` split and the later `B_crit/S/V/O` frontier are different classifications of the same native work law.

For a signed-good positive atom, after reversing all helicity signs simultaneously if necessary, order the signed roots as `alpha=-r<beta=d<gamma=c`, where `c` is the main positive recipient, `d` the unique donor and `r` the opposite-helicity side recipient.  The endpoint proof uses only the certified physical support `3/5<d/c,r/c<5/8` and the two exact triad invariants `sum T_i=0`, `sum x_iT_i=0`.  With `Z=sum x_i^2T_i>0`, these give exactly

`T_(-r)=Z/[(d+r)(c+r)]`,

`T_d=-Z/[(d+r)(c-d)]`,

`T_c=Z/[(c+r)(c-d)]`.

Hence `d` is the unique donor and

`W_side/W_child=T_(-r)/T_c=(c-d)/(d+r)>3/10`.

Writing `D=d/c`, `S=r/c`, the same exact invariants give the critical-production ratio

`P_G/(c W_child)=2S(1-D)/(D+S)`,

and monotonicity on `3/5<D,S<5/8` gives the sharper bounds `18/49<P_G/(c W_child)<20/49`, hence the coarser core bounds `9/25<P_G/(c W_child)<5/12`.

No new Hahn split or temporal ancestry enters these identities.  The reader `r_e,eta0` is used only to make the exact same-Hahn `G/B_bad` restriction in §2; once on `G`, the endpoint `X/Y -> S/V/O` argument uses only the certified physical support and these signed-root identities.

### First-contact good-birth fertility — DISTILLED EXACT DEDUCTION
For any fixed `P_M={M/2<|k|<=M}`, let `tau>0` be the first contact of the actual stock level `M E_M=mu0`.  This is a state locator, not a new cause.  Smoothness gives `dot E_M(tau)>=0`; differentiating the exact mode-set law gives `phi_in,M(tau)>=2nu||grad P_Mu||_2^2>=nu M mu0/2`.  Hence endpoint-complement `B_bad` inflow rate is `>=nu M mu0/4`, or `G` rate is.  In the latter case signed-good support puts both interaction parents in `U_M={3M/10<|k|<=5M/8}`.  The direct sharp work bound on the whole bands, with `C_Y=3sqrt(3)/2`, gives `phi_G<=(15sqrt(pi)/8) M sqrt(mu0) mu_U`, `mu_U=M||P_Uu||_2^2`; thus `mu_U>=2nu sqrt(mu0)/(15sqrt(pi))`.  Covering `U_M` by the two hard shells at `5M/8,5M/16` yields one required interaction shell `R<=5M/8` with `R E_R(tau)>=nu sqrt(mu0)/(36sqrt(pi))`.  Put `mu_*=min(c_nu/2,nu^2/(5184pi))`: at a `mu_*` contact the `G` alternative therefore forces `R E_R(tau)>=2mu_*`.  Either `R E_R(0)>=mu_*`, or continuity gives a strictly earlier `mu_*` contact of that lower shell.  Repeating only the `G` alternative has finite depth because scales contract by `<=5/8` while every contacted shell has `R>=mu_*/E_*`.  Thus every such state-contact descent ends at initial stock or a genuine `B_bad`-rate alternative; no energy-token parent is asserted.
### Critical endpoint rigidity + UV-fresh shell gate — EXACT / EXTERNAL EXACT
Fix `R_0>0` and split canonical radial variation by the smallest triad radius `L`.  For `L<=R_0`, the atom law `|rho_r-rho_d|M_(d->r)<=4LK|a_0a_1a_2|`, comparability of the two high roots, and Cauchy give `v_(L<=R0)(t)<=C_lo R_0^(5/2)E_*^(1/2) C_(1/2)(t)`, `E_*=||u_0||_2^2`; this is the actual band-limited low-root transport, not a recurrence edge.  For `L>R_0`, the shell proof gives `v_(L>R0)<=C_sh sqrt(mu_>(R_0,t))||u||_Hdot^(3/2)^2`, `mu_>=sup_(M>R_0)M||P_(M/2,M]u||_2^2`.  Hence if `mu_><=(2nu/C_sh)^2` on a final interval, `C_(1/2)` satisfies a finite Gronwall bound there.  Kenig--Koch, arXiv:0908.3349, Theorem 0.1 therefore implies: finite `T_*` forces, for every `R_0` and every `t_0<T_*`, some `t>t_0`, `M>R_0` with `M E_M(t)>c_nu:=(2nu/C_sh)^2`.  Thus one may extract `t_n->T_*`, `M_n->infinity`.  Since `u_0 in Hdot^(1/2)` gives `M E_M(0)->0`, the hard-state last-entry theorem eventually rules out initial stock and forces `M_n Phi_(in,M_n)>=4c_nu/5`; canonical good/bad restriction then gives at least `2c_nu/5` in one of the two actual inflow sublaws.  This bifurcation collapses further: a `B_bad`-dominant birth already carries positive endpoint-complement work, while every `G` atom has the certified simultaneous nonforward side recipient with `W_side/W_child>3/10`; hence every sufficiently large UV birth carries a canonical bad-positive sublaw with child-scale amount at least `3c_nu/25`.  `TRANSFER_WORK_LOSS` is only its forward-recursion fate.  More sharply, the bad sidecar is always a **mode-set boundary inflow**: a `B_bad`-dominant birth already crosses the hard shell boundary; on a `G` birth the side recipient has opposite helicity to the unique donor, so after covering its radii `(3M/10,5M/8]` by the two hard annuli at `M/2,M`, let `q=max_A N_A Phi_(in,A)^side` over the four cells from the two radial annuli and two helicities.  The lower cells have `N_A=M/2`, the upper cells `N_A=M`, so `M Phi_side<=6q`; since the `G` side law has `M Phi_side>=3c_nu/25`, one gets the safe universal `q>=c_nu/50`.  The `B_bad` branch is stronger after only a two-helicity split.  Exact mode-set continuity then forces `N E_A(t_1)>=c_nu/150` or `N D_A>=c_nu/150` or `N Phi_(out,A)>=c_nu/150`, ties retained.  These are stock, viscosity and actual outflow; the recipient energy never disappears into a transfer-loss wallet.  The outflow is not a new owner either: embed the helicity annulus `A_N` in the full low ball `L_(2N)`.  Recipient radius `<=2N` is internal donor traffic of `L_(2N)` and cancels from its divergence; recipient radius `>2N` is a restriction of the already-canonical true upward crossing `Phi_up(2N)`.  More quantitatively, reading the donor root as the low child in the certified UV-locality proof gives `N Phi_(A->>2N)<=3sqrt(pi/2)sqrt(mu_A^*)D_>N^(N)`, `mu_A^*=sup_I N E_A`; no recipient Hahn or helicity-action currency is introduced.  The initial boundary itself is exact modal stock at `t=0`.
## 12. Core anti-theorems and permanent guards

Do not use raw Duhamel mass as causal probability.  Do not carry a `dW+` charge through modal stock or infer temporal deposit matching from mode-set balance.  Do not re-Hahn after coarse-graining.  Do not use interaction cells as wallets.  Do not call high→high circulation fresh tail supply.  Do not infer a dyadic step from positive work.  Do not promote checkpoints to events or reset cumulative monitors.  Do not treat inherited stock as generation.  Do not treat material rereading or `R_switch` as source.  Do not treat smooth skew relink as generation.  Do not treat OO/ON/NN as generators of their service law.  Do not promote optional coherent-analysis thresholds—Gaussian aspect/radius, holonomy, flatness, sideband or reuse coordinates—to hard-lineage events: their actual consequences are existing strain/dissipation, modal state/work, terminal analysis cost, or no-hit continuation.  Do not split simultaneous causes by a synthetic clock.  Do not turn normalized critical quantities into finite additive reset budgets.  Do not exchange entropy coordinates from different underlying measures as if they were one currency.  Do not infer that deep high-high→low radial action is small from separation alone: its gap may be `O(K)`; the genuine suppression appears only after the canonical donor bound is paired with critical `Hdot^(3/2)` activity.  Do not infer the sign or orientation of `Hess p` from the scalar Poisson trace: only its isotropic part is local, while the trace-free tidal part is an exact `l=2` quadrupole of the same-field source.  Do not rename a pressure pair or `tau=xi.H0xi` as kinetic-energy work, owner or currency.  Do not call `H0` an independent `H^1` source: it is modewise orthogonal to incompressible strain, while `partial_t S=sym grad N+nu Delta S` carries the actual modal source.  Do not infer any finite pointwise pressure-Hessian bound from the local first jet `(S,omega)`; the exact three-sine torus anti-theorem forbids it.  Do not Hahn-split the Biot--Savart two-point stretching integrand into causal spatial-pair owners or call its positive part a chirality currency: it is an exact signed disintegration of the already-native enstrophy source `Q`, not kinetic-energy transfer.
Do not push a canonical UV boundary-inflow atom to `Q+` or to a positive spatial-pair owner: the exact same-child/same-cut/same-crossing-mass opposite-`Z_tri` witness forbids any such atomwise map.  Do not treat the full instantaneous traffic ledger as a closed dynamical state: the relative-translation witness keeps modal stocks, all active works and `Q` fixed while changing `dot Q` by exactly `87152/55`.

For every proposed frontier lemma ask: **what exact true Navier–Stokes structure makes this true that a generic averaged/bilinear model need not preserve?**  If the answer is only scaling, cancellation or a generic norm inequality, the physical mechanism has probably not yet been isolated.
## 13. What is theorem, what is not
The identities and structural laws above are exact or exact-conditional as labelled.  Randomized triads, Galerkin/FFT probes, CI runs and stress tests in the source repository are evidence against implementation mistakes, not mathematical substitutes for the continuum proofs.
The hard-state **kinetic-energy layer** is exact: earlier modal stock and canonical boundary inflow are the only suppliers; viscosity/outflow are losses.  Signed-good inflow has the `5/8` donor geometry; same-time donor reroot has zero depth; and the resolved `K/S` split adds no recursive owner—`K` is conservative relink while fine `S+` is an inherited low-root `dW-` restriction whose recipient pushforward is canonical bad work.  Pure-`G` funding is radial-cut rooted and total radial variation collides with actual hard-shell concentration `mu_sh`; no independent inward-reuse currency remains.  Finite singularity forces arbitrarily late UV-fresh first contacts and, independently, unbounded cumulative signed enstrophy source after every late time.  Signed-curl/Betchov and Biot--Savart/material-pair formulas are exact representations of the same primitive state/source, not owners of one another.  The opposite-`Z_tri` witness forbids atomwise sign transfer, while the exact relative-translation witness is stronger: identical modal stocks, all active cubic works and `Q` can have different `dot Q`, because mixed quartic phase geometry survives after the traffic quotient has forgotten it.  Hence the proposed late-traffic/material-pair spacetime bridge is a **false frontier created by quotienting the full state too early**.  No nonredundant representation/ontology frontier remains in this architecture.  The unresolved mathematical problem is now the specific direct full-state `B/S/V/O` exclusion: prove that the exact stock/viscosity/outflow grammar cannot recycle critically through the minority-`B_crit` full-state gate to a finite singular endpoint.  The frontier is not another bridge, reader, Hahn split, budget or genealogy.  See `BSVO_FULL_STATE_FRONTIER.md` and `MIXED_FRONTIER.md`.

## 14. Full-state mother law and current `B/S/V/O` frontier — EXACT / CURRENT FRONTIER

The representation frontier is closed.  The canonical remaining derivation is now organized in `BSVO_FULL_STATE_FRONTIER.md` from the true mother law
`N=u_t+nu Lambda^2u`,
not from a cancellation taxonomy.  This core keeps only the primitive identities needed to enter that file.

### Fixed-set force triangle + Kirchhoff — EXACT

For every fixed Fourier/helicity projector `P`, with actual net nonlinear boundary work
`W_P=2<Pu,PN>=phi_(in,P)-phi_(out,P)`,

`nu W_P=||Lambda^-1PN||_2^2-||Lambda^-1Pu_t||_2^2+nu^2||Lambda Pu||_2^2`,

and

`d||Pu||_2^2/dt+2nu||Lambda Pu||_2^2=W_P`.

The usual critical-action law is the radial layer-cake of this fixed-set identity.  Sidecar stock and viscosity are therefore terms of one true control-volume law, not independent currencies.  See `BSVO_FULL_STATE_FRONTIER.md` §§2--4.

### Signed-curl action profile — EXACT

Put `x=s|k|` and push actual modal work to `dW_t(x)`.  Energy/helicity give
`int dW=int x dW=0`.
Define
`F(a)=int_(x>a)dW`,
`Psi(a)=int(x-a)_+dW`,
and with `C=curl`, `M_a=|C-a|`,

`A(a):=||M_a^(1/2)Lambda^-1N||^2-||M_a^(1/2)Lambda^-1u_t||^2+nu^2||M_a^(1/2)Lambda u||^2`.

Then

`A(a)=2nu Psi(a)`,
`F(a)=-(1/(2nu))A_a(a)`,
`dW=(1/(2nu))A_(aa)` distributionally.

Also
`P_(1/2)^NL=2Psi(0)` and `Q=int Psi(a)da`.
Thus critical production, radial/signed-curl traffic and vortex stretching are readings of one actual work/action profile.  This profile is not dynamically closed; its time curvature uses the true `F_N`.  See `BSVO_FULL_STATE_FRONTIER.md` §§3--5 and §11.

### Neutral-helicity hardening tail — EXACT on smooth finite-energy `R^3`

If `P_(1/2)^NL>0`, continuity of the signed-radius cumulative work profile gives a positive maximum `a_*` with `F(a_*)=0`.  Choosing the corresponding single-helicity tail `P_(sigma,R_*)` yields, with `U=Pu`,

`2<U,PN>=0`,
`H:=2<Lambda U,PN>>=P_(1/2)^NL/2>0`.

Thus the tail has zero nonlinear kinetic-energy source but positive helicity/critical transfer.  At a nondegenerate maximum, a shallower same-helicity tail is net donor while a deeper one is net recipient.  On torus/discrete signed radii retain the sign/equal-moment statement rather than asserting a continuous zero.  See `BSVO_FULL_STATE_FRONTIER.md` §§6--7.

### Forced radial sorter versus moment-orthogonal complexity — EXACT

On that frozen neutral tail set
`E=||U||^2`, `mu=<Lambda U,U>/E`, `V=(Lambda-mu)U`, `S=||V||^2`.
Then `S>0` and

`PN=[H/(2S)]V+N_perp`,
`N_perp perp U,V`, hence `<Lambda U,N_perp>=0`.

The first term is the unique full-state component carrying all kinetic-neutral / critical-positive hardening; modewise its work is
`T_sort=(H/S)(rho-mu)|U|^2`, donor below `mu` and recipient above.  All phase, polarization, same-heat and higher-shape freedom that is invisible to the first two radial moments is isolated in `N_perp`.

Writing
`Lambda^2U=(D_2/E)U+beta V+Z`, `Z perp U,V`,
`beta=(D_3-mu D_2)/S>2R_*`,
true NS gives

`U_t=-nu(D_2/E)U+[H/(2S)-nu beta]V+[N_perp-nu Z]`.

Thus nonlinearity hardens and viscosity softens along the **same actual radial-shape direction**.  See `BSVO_FULL_STATE_FRONTIER.md` §§8--10.

### Full radial control-volume fold — EXACT / CURRENT SHARPENING
The canonical derivation is now kept only in `BSVO_FULL_STATE_FRONTIER.md` §20.  In short: `partial_tK_rad+2nu L_rad=Psi_rad`; any fixed `K_rad=kappa` endpoint front has unbounded UV limsup but the genuine viscous budget `8nu kappa int R_kappa dt+2nu int int(rho-2R_kappa)^2de dt<=E(0)`; the `g_tail=partial_tE_(>R)` level family yields stationary-stock hardening cells or one-sided UV growth corridors, reconstructs radial state/work motion exactly, and leaves only the next true stock jet / `F_N/G` as the open regeneration dynamics.  No `O`, phase/tangent repair, or first-contact clock is an independent road.
### True curvature/repair field — EXACT
For every fixed mode
`(partial_t+2nu|k|^2)T_k=2|N_k|^2+2Re(conj(u_k)(F_N)_k)`.
For every fixed set
`dot W_P+4nu<Lambda Pu,Lambda PN>=2||PN||^2+2<Pu,PF_N>`.
Therefore persistent donor curvature, neutral-front drift and hump-height regeneration are exact `F_N` projection conditions.  There is no unnamed repair mechanism.

The same true source is read through
`G=curl N=omega_t-nu Delta omega=S omega-(u.grad)omega`,
`G_t-nu Delta G=[G,u]+[omega,N]-2nu sum_j[partial_j omega,partial_j u]`.
See `BSVO_FULL_STATE_FRONTIER.md` §§11--13.

### Microscopic convolution guard and exact remaining theorem
The full-polarization pair Pythagoras, reality-companion outward leak, corrected nonlinear-silent one-triad terminal class, heat-fiber Laplace rigidity, pair-rate synchronization and the conditional affine-rigidity theorem remain exact.  They now serve to constrain the refined `N_shape/N_fib/F_N` freedom rather than define a parallel proof architecture.  See `BSVO_FULL_STATE_FRONTIER.md` §§15--20.

These laws still do **not** prove `Y=>bot`.  The precise open block is now to exclude unbounded excursions of one fixed `K_rad=kappa` front while its true viscous budget remains finite.  At every outward UV state the full growth family forces either a wholly-UV stationary-stock hardening cell or a monotone UV state-growth corridor; radial state/work shape is already reconstructed, and the remaining tangent freedom is not a separate work-curvature mechanism.  What is still open is whether the next true stock jet / `F_N/G` can keep re-forming those states on `L^1_t`-thin UV excursions.  Equivalently: **No infinite critical full-state recycling.**  See `BSVO_FULL_STATE_FRONTIER.md` §20.
