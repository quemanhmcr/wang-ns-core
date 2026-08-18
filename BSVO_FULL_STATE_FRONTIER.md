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

## 11. Helical pair-silence law — EXACT ALGEBRAIC CONSEQUENCE

For active noncollinear helical modes `p,q` with signed curl eigenvalues `x_p=s_p|p|`, `x_q=s_q|q|`, their unordered pair contribution to `N` at `r=p+q` is
`n_r^(p,q)=(x_q-x_p)P_r(u_p x u_q)`.
For a nondegenerate helical pair the projected cross product is nonzero.  Therefore
`n_r^(p,q)=0 iff x_p=x_q`.
This is the pair-level Beltrami silence mechanism.

## 12. Farther-UV mirror output — EXACT ALGEBRAIC CONSEQUENCE

In a real dangerous opposite-high high-high-low triad,
`k_alpha+k_beta+k_gamma=0`.
Reality supplies the conjugate high mode `-k_gamma`, hence the simultaneous mirror pair `(k_alpha,-k_gamma)` at
`k_Delta=k_alpha-k_gamma`.
Parallelogram geometry gives
`rho_Delta^2=2rho_alpha^2+2rho_gamma^2-rho_beta^2`.
Since both highs exceed the low radius,
`rho_Delta>max(rho_alpha,rho_gamma)`.
The high helicities are opposite, so the signed curl mismatch of the mirror pair is `rho_alpha+rho_gamma`; by the pair-silence law its selected acceleration at `k_Delta` is nonzero.

Thus every dangerous opposite-high triad carries a simultaneous selected nonlinear acceleration channel farther outward than both highs.

## 13. One-triad full-state closure — EXACT ALGEBRAIC CONSEQUENCE

Consider a real nondegenerate finite-Fourier state supported only on one closed triad and its reality copies.  Difference outputs such as `k_1-k_2` lie outside that six-mode support.  Instantaneous full nonlinear closure would force each such pair contribution to vanish.  Pair-silence then gives
`x_1=x_2=x_3`.
Hence all three helicities coincide and all three radii coincide; the wavevector triangle is equilateral and the state is Beltrami:
`omega=lambda u`, `N=0`.
Therefore the only real nondegenerate one-triad full-NS closure is nonlinear silence.  A dangerous opposite-high `O/B` junction cannot live in an autonomous three-mode full state.

## 14. Empty farther output and birth curvature — EXACT IDENTITY

If the farther mirror output is empty at an instant,
`a_Delta=0`,
then its current nonlinear work is zero regardless of `n_Delta`.  But
`dot E_Delta=0`,
`ddot E_Delta=2|n_Delta|^2`.
So if the full acceleration there is nonzero, farther-UV stock birth begins with strictly positive curvature.  This is a concrete physical meaning of the quartic action: it detects acceleration on a road before cubic traffic exists there.

## 15. Exact cancellation alternative at the farther output

The selected mirror acceleration need not equal the full output acceleration:
`n_Delta=n_Delta^mirror+sum_other n_Delta^e`.
If `n_Delta=0`, the other simultaneous parent channels must vectorially cancel the nonzero mirror contribution.  Any cancelling parent pair `p+q=k_Delta` satisfies
`max(|p|,|q|)>=rho_Delta/2`.
This is same-time UV structure, not ancestry.

The unresolved point is that in the continuum many pair channels on the same output can interfere, and the complex two-dimensional output plane permits phase cancellation.

## 16. Radial and tangential escape are different

At a dangerous balanced gate, radial counterwork confined to the same three signed roots is forced by energy/helicity to have the canonical cyclic direction.  To obtain another radial work pattern, actual support must leave the three-root set.

Tangential countersteering is different.  At a silent gate the selected contribution is purely tangential, and the mixed term can be written
`M_tau=J_tau Omega_tau^other`.
Energy and helicity constrain only real work projections; they do not determine `Omega_tau^other`.  This is exactly why the quartic relative-translation witness survives after the cubic traffic quotient is fixed.

## 17. What is already ruled out

The remaining proof may not use any of the following as if they were closure:
- `S=>bot`, `V=>bot`, or `O=>bot` as raw local events;
- an `O(1)` normalized dissipation/event budget;
- positive quartic action as a monotone resource;
- `Q+`, Lamb action or `D_(3/2)` divergence without an exact contradiction theorem;
- a traffic-to-material bridge;
- genealogy, token, event counting, entropy, Hodge owner, pressure owner or material owner;
- a claim that every mirror/UV atom survives full same-output cancellation.

## 18. Exact remaining theorem — OPEN

What remains is not an ontology question.  It is the following full-state theorem:
> **No infinite critical full-state recycling.**  A smooth true 3D incompressible NS trajectory on a finite interval cannot repeatedly realize the stock/viscosity/outflow grammar, through the minority-helicity positive-critical `B` gates required for UV critical regeneration, at unbounded scales while satisfying all exact full-state convolution, phase, pressure/strain and viscosity identities above.
Equivalent endpoint implication:
`Y=>bot`.
The current exact laws narrow the only surviving freedom to continuum same-output vector cancellation and full-state tangential phase reorientation around the dangerous `B/O` gates.  They do not yet prove that those mechanisms cannot sustain infinite critical re-entry.

## 19. QED hook

Once the open theorem is proved, the rest is already assembled:
`T_*<infinity => X vee Y`,
`X=>bot`,
`Y=>bot`,
therefore
`T_*<infinity => bot`, hence `T_*=infinity`.
See `SOLUTION_MAP.md` and the conditional final theorem in `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex`.
