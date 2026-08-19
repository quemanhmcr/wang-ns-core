# Solution Map: Clay Statement to the Remaining QED Arrow

This file is the shortest proof-location map.  It is not a proof by itself and it does **not** claim that the final arrow has been proved.

## 1. Clay target

For smooth divergence-free finite-energy data in the Clay class, prove that the maximal smooth 3D incompressible Navier--Stokes lifespan satisfies

`T_* = infinity`.

Primitive equation:

`u_t + B(u,u) = nu Delta u`, `div u=0`.

Full-state nonlinear acceleration:

`N=-P(u.grad u)=P(u x omega)`.

See: `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex`, Sections “Problem statement” and “Primitive Navier--Stokes equation”.

## 2. Finite singularity forces critical UV hard shells

Kenig--Koch plus the exact critical radial/hard-shell collision imply that if `T_*<infinity`, there are

`t_n -> T_*`, `M_n -> infinity`, `M_n E_(M_n)(t_n) >= c_nu`.

See: `PHYSICAL_CORE.md` §11 and `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “Critical endpoint rigidity and UV hard shells”.

## 3. Exact first endpoint throat: `X vee Y`

Apply the native last-entry Kirchhoff identity on each terminal hard shell:

`T_*<infinity => X vee Y`,

where

- `X` = initial hard-shell stock;
- `Y` = actual canonical nonlinear boundary inflow into the terminal occupied corridor.

See: `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “The exact disjunction `T_*<infinity => X vee Y`”.

## 4. Initial tail kills `X`

Because `u_0 in Hdot^(1/2)`,

`M E_M(0) -> 0` as `M->infinity`.

Therefore sufficiently large endpoint shells cannot be supplied by `X`:

`X => bot`.

Hence

`T_*<infinity => Y`.

See: `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “Exclusion of `X`”.

## 5. `Y` is pushed to one bad-positive sidecar

Use the same one-Hahn canonical positive work law.  The signed-good `G` branch has a simultaneous bad side recipient; a `B`-dominant birth is already bad-positive.  After the hard-annulus/helicity covering:

`Y => universal bad-positive sidecar`.

No new owner or transfer wallet is introduced.

See: `PHYSICAL_CORE.md` §11 and `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “The `Y` branch” and “Universal bad-positive sidecar”.

## 6. Exact second endpoint throat: `S vee V vee O`

Mode-set Kirchhoff on the helicity-resolved sidecar annulus gives

`Y => S vee V vee O`,

where

- `S`: terminal sidecar stock;
- `V`: genuine sidecar viscous loss;
- `O`: actual nonlinear outflow.

There is no fourth kinetic-energy fate.

See: `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “The second throat” and `MIXED_FRONTIER.md` §10.

## 7. Quotient `O` without inventing a new road

Embed the sidecar annulus in the low ball.  Sidecar outflow is exactly

`internal low-ball circulation vee true radial upward flux`.

Internal circulation cancels from the low-ball divergence.  True upward flux is already the canonical radial-supply mechanism.

See: `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “Outflow and recycling quotient”.

## 8. Where `B` belongs

`B` is **not** a fourth sidecar fate.  It is the canonical minority-helicity bad-work branch that creates positive critical stock:

`positive nonlinear d/dt ||u||_Hdot^(1/2)^2 = positive minority-helicity B work`.

Dangerous frontier-advancing true `O` atoms are exactly the opposite-helicity high-high-low positive-critical `B` arches.

See: `PHYSICAL_CORE.md` §11/§14 and `BSVO_FULL_STATE_FRONTIER.md`.

## 9. Return to the full state after the cubic quotient

The relative-translation witness proves that modal stocks + all active cubic works + `Q` do not determine `dot Q`.  Therefore the proof may not seek a missing traffic-to-material bridge; it must return to full `u/omega`.

Exact full-state fields:

`N=u_t+nu Lambda^2u`,

`G=curl N=omega_t-nu Delta omega=S omega-(u.grad)omega`.

See: `PHYSICAL_CORE.md` §14 and `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` “The final quartic phase law”.

## 10. Exact laws already proved inside the remaining `B/S/V/O` block

Current laws include:

1. critical-action Kirchhoff for `N`, including fixed-set sidecar form;
2. pressure-free `G` evolution;
3. Piola/pressure modewise reflection for material strain forcing;
4. complex triad silent-gate law and stock polynomial `B_tau`;
5. self-braking of forward dangerous `O/B` geometry;
6. differential-viscous preparation at the opposite-high neutral gate;
7. three-root energy/helicity work rigidity;
8. full-polarization pair Pythagoras and exact shear/equiradial null geometry;
9. universal outward reality-companion acceleration for every fully active closed geometric triad;
10. corrected one-triad closure: nonlinear-silent planar-shear / monochromatic `2D3C`, not only Beltrami;
11. heat-fiber Laplace rigidity for passive cancellation;
12. exact pair-source repair synchronization `dot F_e=(r_p+r_q)F_e`;
13. viscosity-free Riccati steering `dot eta=(F_N/a)-eta^2`;
14. affine synchronized repair, under its explicit connectivity hypothesis, collapses to regular monochromatic translation/decay.

See: `BSVO_FULL_STATE_FRONTIER.md` for the dedicated statement/derivation map.

## 11. The only missing proof block

The remaining theorem is:

`No infinite critical full-state recycling`.

It must show, using only true NS identities, that the surviving continuum **same-heat, non-affine, dynamically `F_N/G`-repaired cancellation** cannot sustain an infinite sequence of critical minority-`B` / `S` / `V` / `O` re-entry toward a finite endpoint.  Unequal-heat passive cancellation, local active-triad closure and globally affine synchronized repair are already routed to exact work/UV leakage or regular terminal physics.

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

That final composition is already rigorous and is written conditionally in `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex`.

## 13. One-line status

**Everything from the Clay endpoint down to the `B/S/V/O` full-state frontier is assembled; the only missing mathematical arrow is the exact exclusion of infinite critical full-state `B/S/V/O` recycling.  Proving that arrow completes `Y=>bot` and turns the conditional final composition into QED.**
