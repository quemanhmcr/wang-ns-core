# NEO Finite Two-Scale Closure Lab
## Euler macro state plus the canonical square-restoring NS micro-layer

**Status:** research lab.  The No Third Scale and macro--micro no-decoupling statements are open targets.

The aim is to prevent the Euler-degenerate terminal branch from becoming an unlimited profile cascade.

---

## 1. General normalized equation -- EXACT

Work with
\[
\boxed{
V_s=P[X_V,C_y]V-\mu C_y^2V,
\qquad 0<\mu\le1.
}
\]
When \(\mu\to0\), the macro state can converge to Euler while derivative-level curl contact is lost.

The missing information is therefore not another state field but a compactness-stable renderer of singular activity.

---

## 2. Exact Galilean nested layer -- EXACT

For a constant dimensionless Galilean velocity \(d\), set
\[
\widetilde V(y,s)=V(y+ds,s)-d.
\]
Then \(\widetilde V\) obeys the same equation.  Define
\[
\boxed{
W(z,s)=\mu^{-1/2}\widetilde V(\sqrt\mu z,s).
}
\]
The scaling rules are
\[
\partial_s\widetilde V\sim\sqrt\mu\,\partial_sW,
\qquad
P[X_{\widetilde V},C_y]\widetilde V
\sim\sqrt\mu\,P[X_W,C_z]W,
\]
\[
\mu C_y^2\widetilde V
\sim\sqrt\mu\,C_z^2W.
\]
Hence
\[
\boxed{W_s=P[X_W,C_z]W-C_z^2W.}
\]
Also
\[
\boxed{C_zW=C_yV(y+ds,s)|_{y=\sqrt\mu z}.}
\]
So curl is exactly order-preserved by the nested square-restoring zoom.

---

## 3. Circulation scaling -- EXACT

Let \(\Gamma_z\) be a closed loop in the micro variable and \(\Gamma_y=\sqrt\mu\,\Gamma_z\) its image in the macro variable.  Since
\[
\widetilde V=\sqrt\mu W,
\qquad
dy=\sqrt\mu\,dz,
\]
closed-loop circulation satisfies
\[
\boxed{
\oint_{\Gamma_y}\widetilde V\cdot dy
=\mu\oint_{\Gamma_z}W\cdot dz.
}
\]
The constant Galilean subtraction contributes zero on a closed loop.

Therefore a macro circulation of natural size \(O(\mu)\) on radius \(O(\sqrt\mu)\) is exactly order-one circulation in the nested NS field.

---

## 4. Canonical scale coincidence -- DEDUCTION FROM RECORD INPUT

Assume the outer normalization has length \(\ell\), velocity amplitude \(a\), and curl scale
\[
\Omega\sim a/\ell.
\]
Then
\[
\mu=\frac{\nu}{a\ell}
=\frac{\nu}{\Omega\ell^2}.
\]
The viscous record radius is
\[
r_\nu=\sqrt{\nu/\Omega},
\]
so in macro coordinates
\[
\boxed{
\frac{r_\nu}{\ell}=\sqrt\mu.
}
\]
Thus the analyticity/viscous record radius is exactly the scale at which the macro equation restores unit square-anchor strength under nesting.

If the record circulation theorem supplies
\[
R_c\gtrsim r_\nu,
\]
then
\[
\boxed{
R_c/\ell\gtrsim\sqrt\mu.
}
\]
A supporting circulation owner cannot hide at scales parametrically below the canonical square-restoring layer.

---

## 5. No Third Scale target -- OPEN

The desired theorem is not that all activity lives exactly at one radius.  It is the weaker finite statement:
\[
\boxed{
\text{record singular activity}
\Longrightarrow
\mathrm{MAC}
\vee
\mathrm{MIC},
}
\]
where

- `MAC`: a compactness-stable activity renderer remains nontrivial on an \(O(1)\) macro scale;
- `MIC`: after the \(\sqrt\mu\) nested zoom, a licensed renderer is quantitatively nontrivial in the unit-viscosity NS field \(W\).

The theorem should exclude a third branch in which all macro activity vanishes while the singular owner lives at \(o(\sqrt\mu)\) and is not seen by \(W\).

The record circulation lower bound is strong evidence for this target but is not by itself a complete proof for every possible activity renderer.

---

## 6. Why point curl is the wrong bridge -- EXACT TYPING

The macro extraction may have strong convergence of \(V_k\) below one derivative while
\[
|C V_k(0,0)|=1
\]
fails to pass to the limit.  A shrinking curl spike can disappear in the macro state topology.

By contrast, the nested field satisfies
\[
C_zW_k=C_yV_k
\]
at the corresponding micro points.  Thus point curl is naturally a `MIC` renderer, not necessarily a `MAC` renderer, on the Euler-degenerate branch.

The correct bridge should be based on a quantity whose provenance determines which topology is legal rather than forcing one renderer to survive every normalization.

---

## 7. Macro--micro activity split candidates -- PROGRAM

### 7.1 Circulation

Advantages:

- exact Galilean invariance on closed loops;
- Stokes relation to curl flux;
- exact viscous Kelvin evolution;
- natural scaling at \(\sqrt\mu\).

Target:
\[
Q_{\rm circ}^{\rm singular}\ge c
\Longrightarrow
Q_{\rm circ}^{\rm macro}\ge c_1
\vee
Q_{\rm circ}^{\rm micro}\ge c_2.
\]

### 7.2 Galilean oscillation

Advantages:

- directly tied to pressure-free epsilon regularity;
- quotients the constant ancient-profile degeneracy;
- can be measured on tilted cylinders.

Difficulty: on the macro Euler scale the lower bound may shrink with \(\mu\), so the renderer must be renormalized at the canonical microtube before passing to \(W\).

### 7.3 Scale-integrated curl activity

A Morrey/Besov-style local curl flux may be compactness-stable even when point curl is not.  Any candidate must be generated from the curl anchor and must come with an explicit passage theorem.

---

## 8. Affine companion coupling -- DEDUCTION / PROGRAM

Scales larger than a fixed multiple of the viscous record core enter the inner variables through a first-order Taylor renderer
\[
\boxed{B_L(s)z+O(L^{-1})}
\]
for fixed large \(L\), after Galilean subtraction.  Therefore the first-order two-scale terminal object should be
\[
\boxed{
(\text{NS micro core }W,\ \text{finite affine companion }B_L),
}
\]
not a countable collection of outer profiles.

If \(B_L\) is bounded, it becomes a finite matrix parameter in the micro equation.  If it diverges, the existing strain/time/square escape compiler should absorb it before a new outer profile is introduced.

---

## 9. Kelvin bridge target -- OPEN

For a material loop \(\Gamma_s\) in the nested field,
\[
\frac{d}{ds}\oint_{\Gamma_s}W\cdot dz
\]
is governed by the unit square anchor.  At macro scale the limiting Euler circulation is conserved along sufficiently regular material loops.

The desired bridge is a quantitative decomposition showing that singular circulation provenance cannot be lost simultaneously in both limits:
\[
\boxed{
\mathcal C_{\rm physical}
=\mathcal C_{\rm macro}
+\mu\,\mathcal C_{\rm micro}^{\rm ren}
+o(\text{natural scale})
}
\]
in an appropriately defined matched loop family.

This formula is schematic; defining the matched material loops and controlling their deformation is part of the theorem problem.

---

## 10. Falsification models

Any No Third Scale proof strategy should be tested against:

1. a shrinking vorticity core plus remote kinetic-energy owner;
2. a benign steady Euler macro profile with a localized nested NS perturbation;
3. an affine companion strain acting on a micro vortex core;
4. a circulation packet whose vector vorticity direction decoheres while scalar amplitude remains bounded;
5. widely separated annular strain owners producing only a logarithmic first-jet accumulation.

A valid theorem must use genuine NS provenance; finite energy plus a point curl normalization alone is already known to permit profile-splitting anti-models.

---

## 11. Stop rule against infinite microscopes

A third microscope is not licensed merely because a quantity vanishes in both currently chosen renderers.  Before introducing one, prove one of:

1. supporting circulation can lie at \(o(\sqrt\mu)\) despite the record heat/analyticity lower bound;
2. the nested unit-viscosity field can still lose the singular provenance under its available compactness;
3. the affine companion remainder, rather than its finite matrix term, is the actual obstruction.

Without such a theorem, further nesting is branch proliferation rather than progress.

---

## 12. Concrete next theorem targets

**T1 -- No Third Circulation Scale.**  At a running vorticity record, prove that every supporting circulation crossing occurs at normalized radius \(\gtrsim\sqrt\mu\), with enough persistence to pass into either the macro renderer or the nested NS field.

**T2 -- Matched Kelvin Persistence.**  Build a family of material loops whose circulation charge survives for a fixed normalized time unless the affine companion/strain branch becomes active.

**T3 -- Macro--Micro Non-Decoupling.**  Show that singular provenance forces a quantitative activity lower bound in at least one member of the finite pair \((V_{Euler},W_{NS})\).

If these close, the Euler-degenerate endpoint is a finite two-scale normal form rather than an open-ended cascade.

---

## 13. Contact-action prism commutes with canonical nesting -- EXACT

The nested zoom does not create a new local contact geometry.  For
\[
W(z,s)=\mu^{-1/2}\widetilde V(\sqrt\mu z,s),
\]
one has at corresponding points
\[
\boxed{
\nabla_zW=\nabla_y\widetilde V,
\qquad
C_zW=C_y\widetilde V.
}
\]
Hence
\[
S_W=S_V,
\qquad
\omega_W=\omega_V,
\qquad
\rho_W=\rho_V,
\qquad
n_W=n_V.
\]
Moreover the material derivatives agree:
\[
\boxed{
(\partial_s+W\cdot\nabla_z)F_W
=(\partial_s+\widetilde V\cdot\nabla_y)F_V
}
\]
for any dimensionless scalar/vector renderer pulled back by the nesting.  Finally,
\[
\Delta_z\omega_W=\mu\Delta_y\omega_V.
\]
The macro vorticity equation has square coefficient \(\mu\), while the nested equation has coefficient one, so the actual heat action is identical:
\[
\boxed{
\Delta_z\omega_W
=\mu\Delta_y\omega_V.
}
\]
Consequently every dimensionless coordinate of the contact-action prism is invariant:
\[
\boxed{
(\alpha,\beta,\gamma,\sigma,\theta,\kappa)_W
=(\alpha,\beta,\gamma,\sigma,\theta,\kappa)_V.
}
\]

This gives a strong compiler rule:
\[
\boxed{
\text{canonical macro--micro nesting changes owner scale, not local contact species.}
}
\]
Therefore the C0/C1/Riccati/contact classifier should be written once and reused on both sides of square-anchor degeneration.  A separate `Euler-micro local taxonomy' would double-count the same geometry.

---

## 14. Correction after the record-scale semigroup audit -- EXACT / STRATEGIC UPDATE

`NEO_RECORD_SCALE_SEMIGROUP.md` proves a sharper exact statement than the original `No Third Scale' slogan.

At one fixed physical vorticity record, every curl-normalized microscope at scale \(R\) belongs to an exact scale-transfer semigroup, and its canonical \(\sqrt{\mu_R}\) nested field is literally the same \(r_\nu\)-normalized state.  Therefore this lab should no longer attempt to prove that intermediate physical owner radii do not exist.

The correct target is
\[
\boxed{
\textbf{No Third Independent Core State:}
\quad
\text{all record owner scales share one canonical unit-square core.}
}
\]

The remaining information at intermediate/outer scales is provenance:

- observation window;
- Galilean representative;
- square coefficient;
- affine/Euler companion imprint.

Accordingly, future Type-II work should attack **core--companion decoupling**, not generate another nested microscope.
