# `B/S/V/O` Full-State Frontier

This file contains only the remaining physical-road block after the representation frontier has been exhausted.  It does **not** claim `Y=>bot` or global regularity.

`B` here is the already-canonical minority-helicity positive-critical work branch.  It is not a fourth sidecar fate.  The exact sidecar fate theorem remains
`Y => S vee V vee O`.
The goal is to prove the still-open full-state statement
`No infinite critical full-state recycling`,
equivalently `Y=>bot` under the already-proved endpoint grammar.

## 1. Ontology guard

Physical state/fields:
`u`, `omega=curl u`, `S=sym grad u`, `p`, `N=-P(u.grad u)=P(u x omega)`, `G=curl N`.
Physical events/fates:
`S` = actual sidecar stock; `V` = genuine viscous loss; `O` = actual nonlinear outflow; minority-`B` = canonical positive-critical nonlinear work.
Exact readers only:
Fourier/helical amplitudes, signed roots, `Z_tau`, complex triad phase, stock polynomial `B_tau`, modal angular velocity, radial cuts.  They do not become owners, clocks, genealogies or budgets.

## 2. Critical action of the genuine nonlinear acceleration — EXACT IDENTITY

From
`N=u_t+nu Lambda^2u`,
apply `Lambda^(-1/2)` and square:
`||N||_Hdot^(-1/2)^2 = ||u_t||_Hdot^(-1/2)^2 + nu^2||u||_Hdot^(3/2)^2 + nu d||u||_Hdot^(1/2)^2/dt`.
Integrated on `[t0,t1]`:
`nu C_(1/2)(t1) + int||u_t||_Hdot^(-1/2)^2 + nu^2 int||u||_Hdot^(3/2)^2 = nu C_(1/2)(t0) + int||N||_Hdot^(-1/2)^2`.
For every fixed Fourier/helicity set `A`, the same identity holds after `P_A` because `P_A` commutes with `Lambda`, `Delta` and `partial_t`.
Sidecar `S` and `V` therefore occur as positive terms of one exact full-state identity.  The RHS is not declared a finite budget.

## 3. The common nonlinear vorticity acceleration — EXACT IDENTITY

Define
`G:=curl N`.
Curling momentum and comparing with vorticity gives
`G=omega_t-nu Delta omega=S omega-(u.grad)omega=[omega,u]`.
Hence the same field reads as

- curl of nonlinear velocity acceleration;
- nonlinear Eulerian vorticity tendency;
- vortex stretching minus vorticity transport.

Its exact PDE is
`G_t-nu Delta G = [G,u] + [omega,N] - 2nu sum_j[partial_j omega,partial_j u]`.
There is no independent pressure source in this equation.

## 4. Pressure is a modewise reflection — EXACT IDENTITY

Let
`A=grad u=S+Omega`, `g=-Delta p=|S|^2-|omega|^2/2`,
`M=S^2+Omega^2`, `R=M+Hess p=-(D_tS-nu Delta S)`.
Piola gives, for `q!=0`, `e=q/|q|`,
`Rhat(q)=Mhat(q)-2<Mhat(q),e tensor e>_F e tensor e`.
Therefore
`|Rhat(q)|_F=|Mhat(q)|_F`.
Pressure changes the longitudinal tensor component by exact reflection but does not create an independent forcing magnitude.
Equivalent integrated identity:
`2||D_tS-nu Delta S||_2^2 = ||S omega||_2^2 + ||Delta p||_2^2`.
This is structural rigidity, not an endpoint budget.

## 5. Sidecar roads in full-state language

`S`: actual modal state is present.  Its future obeys `u_t=N-nu Lambda^2u`; it can persist, be dissipated or participate in actual nonlinear work.
`V`: `-nu|k|^2 a_k` is radial damping in each complex modal plane.  Direct viscosity removes amplitude and does not directly rotate modal phase.  Differential damping changes stock ratios and enters the next nonlinear jet through the exact product commutator.

`O`: actual signed nonlinear work is `2 Re(conj(a_k)n_k)`.  Internal low-ball outflow is circulation; true outflow is radial crossing.  A true frontier-advancing interaction must be analyzed at the actual closed-triad/full-convolution level.

## 6. Closed-triad signed-curl law — EXACT IDENTITY

For distinct signed roots `alpha<beta<gamma`,
`T_alpha=c_alpha Z_tau`, `T_beta=c_beta Z_tau`, `T_gamma=c_gamma Z_tau`,
with
`c_alpha=1/[(beta-alpha)(gamma-alpha)]`,
`c_beta=-1/[(beta-alpha)(gamma-beta)]`,
`c_gamma=1/[(gamma-alpha)(gamma-beta)]`.
Thus `sum T_i=0`, `sum x_iT_i=0`, and `sum rho_i^2T_i=Z_tau`.
At fixed triad, every radial-cut flux is `Pi_tau(R)=Z_tau Psi_tau(R)`: the geometry of the traffic profile is fixed; only the scalar `Z_tau` changes.

## 7. Dangerous true `O` classification — EXACT ALGEBRAIC CONSEQUENCE

Take a true far-UV low donor with `rho_low<=N` and recipient `>2N`.  Triangle geometry forces the third root to be another comparable high mode.
If the two high roots have opposite helicity, the low root is the signed middle root.  Low donor work then forces
`Z_tau>0`, both high roots recipients, and `Pi_tau(R)>=0` for every radial cut.
The critical production is positive and equals the canonical minority-helicity `B` work.
If the high pair has the same helicity, the low root is a signed endpoint.  The other signed endpoint is a farther high donor, the high middle root is recipient, and the radial profile has a lower upward lobe plus a higher downward return.  Critical production is zero or negative.
Therefore an `O` recipient that is radially outermost in its own triad must lie on the opposite-high positive-critical `B` arch.

## 8. Complex silent gate — EXACT IDENTITY

Let `b_i^tau` be the selected triad contribution to full modal acceleration `n_i`.  There is one complex interaction amplitude
`mathfrak Z_tau=Z_tau+iJ_tau`
such that
`2 conj(a_i)b_i^tau=c_i mathfrak Z_tau`.
Define actual modal stocks `E_i=|a_i|^2` and the finite stock polynomial
`B_tau=c_alpha E_beta E_gamma+c_beta E_gamma E_alpha+c_gamma E_alpha E_beta`.
Writing algebraically `n_i=b_i^tau+r_i^tau`, exact differentiation gives
`dot Z_tau+nu Sigma_tau Z_tau = (|Lambda_tau|^2/2)B_tau + M_tau`,
`M_tau=2 sum_i c_i^(-1) Re(conj(r_i^tau)b_i^tau)`.
At `Z_tau=0`, direct viscosity has no sign-flip term.
If all roots are active, writing `a_i=sqrt(E_i) exp(i theta_i)` gives
`dot theta_i=Im(conj(a_i)n_i)/E_i`,
so direct linear viscosity does not rotate modal phase.  With
`Omega_tau=sum_i dot theta_i`,
the silent-gate law is
`dot Z_tau=J_tau Omega_tau`.

## 9. Self-braking and viscous preparation — EXACT ALGEBRAIC CONSEQUENCE

When all roots are active let
`chi_tau=c_alpha/E_alpha+c_beta/E_beta+c_gamma/E_gamma`,
so `B_tau=(E_alpha E_beta E_gamma)chi_tau`.
Selected triad work gives
`dot chi_self = -Z_tau sum_i c_i^2/E_i^2`.
Hence forward `Z_tau>0` self-drives its steering geometry toward smaller `chi`: the arch self-brakes.
At the dangerous opposite-high neutral surface `B_tau=0`, direct differential viscosity satisfies
`dot B_nu>0`.
Thus viscosity can prepare a stock geometry favorable to later self-forward opening while remaining genuine loss; dissipated kinetic energy is not recycled.
The selected viscous commutator is the same cross-effect viewed through the next source jet.  At the balanced active gate `Z_tau=B_tau=0`,
`J_tau dot Omega_comm = (|Lambda_tau|^2/2) dot B_nu`.
Do not count these as two independent mechanisms.

## 10. Three-root work rigidity — EXACT ALGEBRAIC CONSEQUENCE

Let a work vector `q=(q_alpha,q_beta,q_gamma)` on three distinct signed roots satisfy
`sum q_i=0`, `sum x_i q_i=0`.
Then
`q_i=lambda c_i`.
The coefficient is `lambda=sum rho_i^2q_i`.
The same result holds for every time derivative of the full nonlinear work as long as that work jet remains supported on those three signed roots.
Consequences:
- no nonzero closed two-root work exists;
- three-root energy/helicity-closed work has one direction only;
- a genuinely different radial compensation needs additional signed-root work support;
- energy/helicity do not control tangential phase steering.

## 11. Helical atoms versus the full geometric pair — EXACT IDENTITY

For active helical modes, the selected atom law is
`n_(p+q)^(p,q)=(x_q-x_p)P_(p+q)(u_p x u_q)`.
It is silent iff the signed curl eigenvalues agree.  This is an atomwise statement only.

For the full Fourier coefficients `U=uhat(p)`, `V=uhat(q)`, `K=p+q`, sum both helicities before drawing a state conclusion.  In the pair-plane frame, write
`U=A n+B(be-at)`, `V=C n+D(be+(|K|-a)t)`.
Then
`|N_K^(p,q)|^2=|p x q|^2[|BC+DA|^2+((|q|^2-|p|^2)^2/|K|^2)|BD|^2]`.
This is a full-polarization Pythagoras.  If `|p|!=|q|`, the pair is silent iff both full velocity vectors are parallel to the common normal `p x q`.  If `|p|=|q|`, the exact null condition is the wider manifold `BC+DA=0`.  Thus equiradial helical cancellation can preserve a genuine relative phase and does not determine low-root critical-work sign.

## 12. Universal active-triad outward leak — EXACT ALGEBRAIC CONSEQUENCE

Let `k_1+k_2+k_3=0` be nondegenerate and suppose all three full Fourier coefficients are nonzero.  If at least one of the three internal full pair accelerations is nonzero, then for some `i!=j` the reality companion pair `(k_i,-k_j)` has nonzero full acceleration at
`K_out=k_i-k_j`,
with
`|K_out|>max_l |k_l|`.
For unequal radii this follows from the common-normal silence theorem plus the parallelogram identity.  The equilateral case requires the full phase algebra: if all three difference pairs were silent, the three polarization ratios would coincide and be purely imaginary, which also kills every internal pair.  Therefore a genuinely active closed geometric triad cannot be locally UV-closed.

There is no universal multiplicative jump: when the low root is much smaller than an equal high pair, the outward radius can be only `sqrt(H^2+2 ell^2)`.  No scale-jump budget is inferred.

## 13. Correct one-triad terminal class — EXACT ALGEBRAIC CONSEQUENCE

For a real finite-Fourier state supported only on one closed triad and its reality copies, full nonlinear closure forces all difference outputs to vanish.  By Section 12 the internal triad must therefore be nonlinear-silent: `N=0`.

Correction of the older helical-only wording: closure is not restricted to homochiral Beltrami.  Non-equilateral closure is common-normal planar shear.  Equilateral closure is the monochromatic `2D3C` family
`u=n x grad psi+c rho psi n`, `-Delta psi=rho^2 psi`, `c real`,
for which `P(u.grad u)=0`; Beltrami is only a subfamily.  Under viscosity these states heat-decay exactly and are regular terminal physics.

## 14. Empty output and higher birth jets — EXACT IDENTITY

At an empty mode `a_K=0`, current nonlinear work is zero.  If `N_K!=0`, then
`dot E_K=0`, `ddot E_K=2|N_K|^2>0`.
If also `N_K=0` but `(F_N)_K!=0`, then
`E_K^(r)=0` for `r<4`, while `E_K^(4)=6|(F_N)_K|^2>0`.
More generally, if the first nonzero state derivative is `a_K^(m)`, then the first nonzero stock derivative is order `2m` and equals `binom(2m,m)|a_K^(m)|^2`.
These are state jets, not genealogy or event counting.

## 15. Physical heat fibers — EXACT / EXACT ANALYTIC CONSEQUENCE

For a fixed child `K`, every parent pair `p+q=K` has the physical product heat rate
`kappa=|p|^2+|q|^2`.
Freeze the current state and evolve it only by the true linear heat semigroup.  If `dmu_K(kappa)` is the pushforward of the full pair-source vector measure by `kappa`, then
`N_K[e^(nu tau Delta)u]=int exp(-nu kappa tau)dmu_K(kappa)`.
Whenever this vector measure has finite variation, vanishing for `tau` in a nontrivial interval implies by Laplace-transform uniqueness
`dmu_K(kappa)=0`.
Thus direct viscosity cannot preserve a cancellation across distinct heat rates unless each heat-fiber resultant already vanishes; otherwise actual nonlinear parent dynamics must repair the cancellation.
If fiberwise resultants vanish for every output, the heat orbit itself has `N=0` for all times and is an exact regular NS heat trajectory.

## 16. Pair-source repair synchronization — EXACT IDENTITY

For one helical pair atom write
`F_e=C_e a_p a_q`,
where the geometric vector `C_e` is fixed.  On active parents define
`r_k=dot a_k/a_k=n_k/a_k-nu|k|^2`.
Then
`dot F_e=(r_p+r_q)F_e`.
The atom's projective source line is fixed; dynamics only dilates and rotates its complex coefficient.

For two nonzero cancelling atoms `F_1+F_2=0`, first-order persistence is equivalent to
`r_p+r_q=r_r+r_s`.
Its real part is
`w_p/E_p+w_q/E_q-w_r/E_r-w_s/E_s=nu(kappa_1-kappa_2)`;
its imaginary part is equality of the two parent phase-rate sums.  Hence unequal-heat cancellation necessarily requires genuine nonlinear radial work at its parents.  Pure phase repair can occur only in the same-heat case.

For a nondegenerate minimal three-atom cancellation circuit in the complex two-dimensional child plane, the same argument forces all three pair-rate sums to be equal.  In a larger block, if `F` is the child-source matrix, current and first-jet cancellation are exactly
`F 1=0`, `F zeta=0`,
with `zeta_e=r_(p_e)+r_(q_e)`.  Higher-dimensional kernel freedom is the genuine many-channel loophole.

## 17. The repair rate is governed by `F_N/G` — EXACT IDENTITY

Let `eta_k=n_k/a_k` on an active mode and `h_k=(F_N)_k`, where
`F_N=N_t-nu Delta N`.
Then direct linear viscosity cancels from the logarithmic nonlinear-rate equation:
`dot eta_k=h_k/a_k-eta_k^2`.
Thus maintaining a non-affine cancellation requires exact `F_N` steering of the parent rates.  There is no unnamed repair mechanism; in physical fields
`F_N=-B(N,u)-B(u,N)+2nu sum_j B(partial_j u,partial_j u)`,
and equivalently
`G_t-nu Delta G=[G,u]+[omega,N]-2nu sum_j[partial_j omega,partial_j u]`.

## 18. Affine synchronized repair is terminal regular physics — EXACT CONDITIONAL RIGIDITY

Assume explicitly that overlapping cancellation circuits on a connected active set force the same logarithmic law across the connected helicity sectors,
`r_(k,s)=sigma(t)+i v(t).k`.
Then the full field has fixed shape up to amplitude and translation:
`u(t,x)=A(t)U(x+delta(t))`.
True viscous NS plus the energy identity forces `A'/A=-nu rho_*^2`, every active mode to satisfy `|k|=rho_*`, and
`N[U]=(v_0.grad)U`.
Hence every nonlinear modal work is zero.  On a torus/finite-Fourier setting this is a smooth monochromatic decaying traveling relative equilibrium.  For finite-energy `R^3`, exact nonzero `L^2` Fourier support on one sphere is impossible, so the synchronized state is trivial.
This theorem does **not** assert that every cancellation network becomes affine; non-affine same-heat synchronization is precisely the remaining hard phase geometry.

## 19. Radial and phase escape after the new reductions

At the dangerous `B/O` gate, radial counterwork confined to the same three signed roots remains locked to the canonical cyclic direction by energy/helicity.  A fully active geometric triad also cannot stop locally: it creates an outward reality-companion pair acceleration.  If the resulting full child is cancelled, inter-heat cancellation must be repaired by actual parent radial work, while same-heat cancellation may use phase synchronization.

Affine/global synchronization is regular by Section 18.  Therefore the genuinely dangerous remainder is narrower:
`same-heat + non-affine + dynamically F_N/G-repaired cancellation`,
together with the continuum possibility of large same-output cancellation kernels.  This is a description of the surviving freedom, not a proved contradiction.

## 20. What is already ruled out

The remaining proof may not use any of the following as if they were closure:
- `S=>bot`, `V=>bot`, or `O=>bot` as raw local events;
- an `O(1)` normalized dissipation/event budget;
- positive quartic action as a monotone resource;
- `Q+`, Lamb action or `D_(3/2)` divergence without an exact contradiction theorem;
- a traffic-to-material bridge, genealogy, token, entropy or new owner;
- a claim that every selected mirror atom survives full helicity/pair cancellation;
- the obsolete statement that one-triad closure is only Beltrami;
- the claim that equiradial mirror cancellation fixes critical-work sign;
- a claim that the affine synchronization theorem applies without its connectivity hypothesis.

## 21. Exact remaining theorem — OPEN

What remains is still:
> **No infinite critical full-state recycling.**  A smooth true 3D incompressible NS trajectory on a finite interval cannot repeatedly realize the stock/viscosity/outflow grammar, through the minority-helicity positive-critical `B` gates required for UV critical regeneration, at unbounded scales while satisfying all exact full-state convolution, phase, pressure/strain, heat-fiber and repair identities above.
Equivalent endpoint implication: `Y=>bot`.
The new laws exclude local active-triad closure, passive inter-heat cancellation and globally affine synchronized repair as dangerous mechanisms.  They do **not** yet exclude continuum same-heat non-affine `F_N/G`-repaired cancellation.

## 22. QED hook

Once the open theorem is proved, the rest is already assembled:
`T_*<infinity => X vee Y`,
`X=>bot`,
`Y=>bot`,
therefore
`T_*<infinity => bot`, hence `T_*=infinity`.
See `SOLUTION_MAP.md` and the conditional final theorem in `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex`.
