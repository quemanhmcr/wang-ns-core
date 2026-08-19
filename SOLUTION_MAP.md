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
13. dangerous outermost `O` atoms are opposite-high positive-critical `B` arches;
14. full-polarization pair Pythagoras and reality-companion leakage exclude local active-triad closure;
15. passive inter-heat cancellation is fiberwise by Laplace uniqueness; unequal-heat persistence needs true parent radial work;
16. affine synchronized repair, under its explicit connectivity hypothesis, collapses to regular monochromatic translation/decay.

See `BSVO_FULL_STATE_FRONTIER.md` for the canonical statement/derivation map.  `PHYSICAL_CORE.md` §14 now keeps only the primitive entry identities and links here rather than duplicating the frontier.

## 11. The only missing proof block

The remaining theorem is:

`No infinite critical full-state recycling`.

It must show, using only true NS identities, that repeated late UV critical regeneration cannot keep rebuilding the forced neutral-tail radial sorter `[H/(2S)](Lambda-mu)U` through the moment-orthogonal `N_perp/F_N` freedom at unbounded scales.  The older same-heat non-affine cancellation loophole survives precisely inside this remainder; unequal-heat passive cancellation, local active-triad closure and globally affine synchronized repair are already routed to exact work/UV leakage or regular terminal physics.

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
