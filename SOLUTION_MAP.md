# Solution Map: Clay Statement to the Remaining QED Arrow

This file is the shortest proof-location map.  It is not a proof by itself and it does **not** claim that the final arrow has been proved.
Methodological convention: every road below is first typed by the exact control-volume discipline in `CONTROL_VOLUME_METHOD.md`.

## 1. Clay target

For smooth divergence-free finite-energy data in the Clay class, prove that the maximal smooth 3D incompressible Navier--Stokes lifespan satisfies

`T_* = infinity`.

Primitive equation:

`u_t + B(u,u) = nu Delta u`, `div u=0`.

Full-state nonlinear acceleration:

`N=-P(u.grad u)=P(u x omega)`.

See: `PHYSICAL_CORE.md` §0--§1.

## 2. Finite singularity forces critical UV hard shells

Kenig--Koch plus the exact critical radial/hard-shell collision imply that if `T_*<infinity`, there are

`t_n -> T_*`, `M_n -> infinity`, `M_n E_(M_n)(t_n) >= c_nu`.

See: `PHYSICAL_CORE.md` §11 “Critical endpoint rigidity + UV-fresh shell gate” and `MIXED_FRONTIER.md` §10.2.

## 3. Exact first endpoint throat: `X vee Y`

Apply the native last-entry Kirchhoff identity on each terminal hard shell:

`T_*<infinity => X vee Y`,

where

- `X` = initial hard-shell stock;
- `Y` = actual canonical nonlinear boundary inflow into the terminal occupied corridor.

See: `PHYSICAL_CORE.md` §4 “Native hard-state last-entry theorem” and `MIXED_FRONTIER.md` §10.3.

## 4. Initial tail kills `X`

Because `u_0 in Hdot^(1/2)`,

`M E_M(0) -> 0` as `M->infinity`.

Therefore sufficiently large endpoint shells cannot be supplied by `X`:

`X => bot`.

Hence

`T_*<infinity => Y`.

See: `PHYSICAL_CORE.md` §11 and `MIXED_FRONTIER.md` §10.3.
## 5. `Y` is pushed to one fixed positive control volume
Use the same one-Hahn canonical positive work law.  Partition that existing `dW+` directly by exact triad geometry: `G` consists of positive child edges whose signed roots can be written `-r<d<c`, with `Z>0` and `3/5<d/c,r/c<5/8`; `B_bad` is the complementary restriction.  This `B_bad` is **not** the full-state `B_crit` of §8.  No extremizer or numerical threshold is used.

On `G`, the exact triad identities `sum T_i=0`, `sum x_iT_i=0` give

`T_(-r)=Z/[(d+r)(c+r)]`, `T_d=-Z/[(d+r)(c-d)]`, `T_c=Z/[(c+r)(c-d)]`,

so `W_side/W_child=(c-d)/(d+r)>3/10`; radial/helicity covering gives `N Phi_in,A>=c_nu/50`.  If instead `B_bad` carries at least half of `Y`, split the original child shell by its two helicities and obtain the stronger `N Phi_in,A>=c_nu/5`.  Thus either branch supplies a fixed control volume with at least the common `c_nu/50` inflow quantum.

`Y => fixed positive inflow cell => S vee V vee O`.

No new owner, optimizer, certificate or transfer wallet is introduced.

See: `PHYSICAL_CORE.md` §11 endpoint `G/B_bad` algebra and `MIXED_FRONTIER.md` §§10.5--10.6.

## 6. Exact second endpoint throat: `S vee V vee O`

Mode-set Kirchhoff on the helicity-resolved sidecar annulus gives

`Y => S vee V vee O`,

where

- `S`: terminal sidecar stock;
- `V`: genuine sidecar viscous loss;
- `O`: actual nonlinear outflow.

There is no fourth kinetic-energy fate.

See: `PHYSICAL_CORE.md` §11 “Critical endpoint rigidity + UV-fresh shell gate” and `MIXED_FRONTIER.md` §10.6.

## 7. Quotient `O` without inventing a new road

Embed the sidecar annulus in the low ball.  Sidecar outflow is exactly

`internal low-ball circulation vee true radial upward flux`.

Internal circulation cancels from the low-ball divergence.  True upward flux is already the canonical radial-supply mechanism.

See: `PHYSICAL_CORE.md` §11 and `MIXED_FRONTIER.md` “Bad-sidecar outflow quotient”.

## 8. Where `B` belongs

From this point onward `B` means `B_crit`, not the endpoint complement `B_bad`.  It is **not** a fourth `S/V/O` fate.  The exact heterochiral identity `sum_i rho_i T_i=2 rho_m T_m` shows that positive critical production is precisely positive minority-helicity work:

`positive nonlinear d/dt ||u||_Hdot^(1/2)^2 = positive minority-helicity B_crit work`.

Dangerous frontier-advancing true `O` atoms are exactly the opposite-helicity high-high-low positive-critical `B` arches.

See: `PHYSICAL_CORE.md` §11/§14 and `BSVO_FULL_STATE_FRONTIER.md`.

## 9. Return to the full state after the cubic quotient

The relative-translation witness proves that modal stocks + all active cubic works + `Q` do not determine `dot Q`.  Therefore the proof may not seek a missing traffic-to-material bridge; it must return to full `u/omega`.

Exact full-state fields:

`N=u_t+nu Lambda^2u`,

`G=curl N=omega_t-nu Delta omega=S omega-(u.grad)omega`.

See: `PHYSICAL_CORE.md` §§11,14, `MIXED_FRONTIER.md` §12, and `BSVO_FULL_STATE_FRONTIER.md`.

## 10. Exact laws already proved inside the remaining `B/S/V/O` block

The dedicated frontier is now organized from one mother law rather than from a cancellation taxonomy:

`N=u_t+nu Lambda^2u`.

Current exact consequences include:
1. modewise and fixed-set force-triangle / Kirchhoff action identity;
2. signed-curl boundary-work profile `F`, hinge potential `Psi`, and quadratic action profile `A=2nu Psi`;
3. height/slope/curvature readings: critical source / actual cut flux / actual modal work, with `Q` the profile area;
4. closed-triad triangular Green profile and divided-difference law as the atomic signed-curl model;
5. on smooth finite-energy `R^3`, positive critical production forces a kinetic-work-neutral but helicity/critical-positive single-helicity tail;
6. nondegenerate neutral tails have a shallower-donor / deeper-recipient same-helicity flux reversal;
7. exact neutral-tail decomposition `PN=[H/(2S)](Lambda-mu)U+N_perp`, where `N_perp` is orthogonal to both kinetic and critical radial moments;
8. viscosity decomposes on the same radial-shape direction, giving exact nonlinear hardening versus viscous softening of mean tail radius;
9. moving neutral fronts obey an exact excess-radius stock identity;
10. actual work curvature obeys `(partial_t+2nu|k|^2)T_k=2|N_k|^2+2Re(conj(u_k)(F_N)_k)`;
11. `G=curl N` and `F_N` are the genuine fields governing all non-affine reshaping/repair;
12. Piola pressure reflection remains Hodge/strain completion, not a second supply road;
13. dangerous outermost `O` atoms are opposite-high positive-critical `B_crit` arches;
14. full-polarization pair Pythagoras and reality-companion leakage exclude local active-triad closure;
15. passive inter-heat cancellation is fiberwise by Laplace uniqueness; unequal-heat persistence needs true parent radial work;
16. affine synchronized repair, under its explicit connectivity hypothesis, collapses to regular monochromatic translation/decay;
17. the folded radial family gives one fixed endpoint hinge front `K_rad(R_kappa,t)=kappa` with unbounded UV limsup but a genuine finite viscous `L^1_t` radius/mis-centering budget;
18. the `g_tail=partial_tE_(>R)` family exhausts superlevel/front observer calculus and the Volterra work-square family.  Summing **all** physical radial cuts with `phi'` gives one multiplier law: the Volterra heat term is exactly twice tail enstrophy-work, the nonlinear curvature sum is the full-field slot commutator `D_phi(N,u;omega)+(1/2)D_phi(u,u;G)`, and the adaptive reader `phi'_(alpha,J)=2R^alpha J` satisfies `4J_alpha=W_phi` with `dot J_alpha` equal to pure complementary work-rate transfer.  The whole `kappa`-front family also forces `int||Lambda^(-epsilon/2)N||^2dt=infinity` for every `epsilon<1` and a log-enhanced `H^-1/2` forcing burden; a general coarea lower bound proves no unbounded observer primitive can descend to the energy-class `L_t^(4/3)H^-1` control.  See `BSVO_FULL_STATE_FRONTIER.md` §20.

See `BSVO_FULL_STATE_FRONTIER.md` for the canonical statement/derivation map.  `PHYSICAL_CORE.md` §14 now keeps only the primitive entry identities and links here rather than duplicating the frontier.

## 11. The only missing proof block

The remaining theorem is:
`No infinite critical full-state recycling`.

It must show, using only true NS identities, that one fixed positive critical-hinge level `K_rad(R_kappa,t)=kappa` cannot make unbounded UV excursions.  The observer hierarchy is now provably exhausted: inverse fronts, growth cells and `J_alpha` are only coordinate/readout transforms of actual state/work, while all-front coarea already extracts the strongest forcing burden obtainable from unbounded observer motion and stops at critical-plus `H^-1/2` scale rather than the energy-funded `H^-1` level.  Summing the physical cut family returns the remaining dynamics to one full-field `u/N/G` slot commutator; internal UV nonlinear curvature and second-order suppliers cancel exactly, and adaptive work-square growth is only complementary work-rate redistribution plus known viscosity.  The open theorem is therefore genuinely full-convolution: rule out finite-endpoint persistence of that commutator/transfer, not invent another front, norm, clock or wallet.

Equivalent required implication:

`Y => bot`.

This is **OPEN**.

## 12. Final composition once the block is proved

Once `Y=>bot` is proved:

```text
T_* < infinity
   => X vee Y
   => bot vee bot
   => bot.
```

Therefore

`T_* = infinity`.

That final composition is the direct conditional composition of the displayed arrows; no separate synthesis file is required.
## 13. One-line status

**Everything from the Clay endpoint down to the `B/S/V/O` full-state frontier is assembled; the only missing mathematical arrow is the exact exclusion of infinite critical full-state `B/S/V/O` recycling.  Proving that arrow completes `Y=>bot` and turns the conditional final composition into QED.**
