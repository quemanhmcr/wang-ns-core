# 02 — Stationary finite-viscosity theorem chain

This file contains the exact stationary reduction and the radial transfer theorem. The final saturation exclusion is **not** proved here.

---

## Hypothesis S

Let `v` be a nonzero smooth finite-energy normalized stationary candidate on `R^3` with

\[
E(v)=1,\qquad M(v)=1,\qquad \kappa>0,\qquad d(v)>0.
\]

All quantities below are evaluated at this fixed state.

---

## Theorem S1 — Stationary scalar identities

Stationarity of

\[
0=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv
\]

implies

\[
\boxed{W=2\kappa D_3,\qquad \beta=2\kappa D_2.}
\]

Hence

\[
\boxed{
N(v)=\kappa Y_v,
\qquad
Y_v=C^2v-D_2v+2D_2\mathcal Lv.
}
\]

Moreover the stationary helicity balance gives

\[
\boxed{H_3:=\langle \Lambda v,C\Lambda v\rangle=0.}
\]

### Proof

Critical normalization gives `M_θ=0`, hence `W=2κD_3`. Energy normalization gives `E_θ=0`, hence `β=2κD_2`. Substitution yields `N=κY`. The normalized helicity equation is

\[
h_\theta=-Wh+2\kappa(D_3h-H_3).
\]

Using stationarity and `W=2κD_3` gives `H_3=0`.

---

## Theorem S2 — Stationary regression algebra

Define

\[
Q=\langle v,C\Lambda v\rangle.
\]

The regression equations are

\[
D_2=a+bQ,
\qquad
H_3=aQ+bD_3.
\]

Since `H_3=0`,

\[
\boxed{
a=\frac{D_2D_3}{D_3-Q^2},
\qquad
b=-\frac{D_2Q}{D_3-Q^2}.
}
\]

Also

\[
\boxed{
d^2=D_3-aD_2,
\qquad
D_3-d^2=aD_2.
}
\]

For a nonzero stationary state both helicities are present, hence

\[
\boxed{|Q|<D_2,\qquad |b|<1.}
\]

### Proof

Solve the two linear regression equations in `a,b`. The formula for `d^2` follows from the orthogonal heat decomposition in Theorem 3 of `01_EXACT_THEOREMS_AND_PROOFS.md`. If `|Q|=D_2`, all `D_2` mass lies on one helicity sheet, contradicting `H_3=0` for a nonzero state.

---

## Theorem S3 — Exact stationary saturation identity

Set

\[
r=\frac{D_3}{d^2},
\qquad
R_{\rm fv}=Y_v-rG_v.
\]

Since

\[
\gamma=\frac{W}{2d^2}=\kappa\frac{D_3}{d^2}=\kappa r,
\]

and

\[
N=\gamma G+T=\kappa Y,
\]

we obtain

\[
\boxed{T=\kappa R_{\rm fv}.}
\]

More generally, for every scalar `μ`,

\[
\boxed{
\|N-\mu Y\|_{H^{-1/2}}^2
=
\|T-\mu R_{\rm fv}\|_{H^{-1/2}}^2
+
\frac{(W/2-\mu D_3)^2}{d^2}.
}
\]

### Proof

Use

\[
Y=rG+R_{\rm fv},
\qquad
N=\gamma G+T,
\]

and the `H^{-1/2}` orthogonality of `G` to the transverse space. The coefficient of `G` is `γ-μr`; multiplying its square by `d^2` gives the displayed scalar term.

---

## Theorem S4 — Raywise formula for `R_fv`

On helicity sheet `σ=±1`, write

\[
\widehat v_\sigma(\rho,\omega)=f_\sigma(\rho,\omega).
\]

Then

\[
\widehat G_\sigma
=
\rho\big((1-\sigma b)\rho-a\big)f_\sigma.
\]

Using

\[
\widehat{\mathcal Lf}
=-(\tfrac32+\rho\partial_\rho)f,
\]

one obtains

\[
\boxed{
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
\left(
[1-r(1-\sigma b)]\rho^2+ra\rho-4D_2
\right)f_\sigma.
}
\]

### Proof

Insert the Fourier expressions for `Y` and `G` into `R_fv=Y-rG` and collect the radial derivative and multiplier terms.

---

## Theorem S5 — `R_fv` has trivial finite-energy kernel

If

\[
R_{\rm fv}(v)=0
\]

for a finite-energy `v`, then

\[
\boxed{v=0.}
\]

### Proof

For each `(σ,ω)`, Theorem S4 gives a first-order ODE. Its nonzero homogeneous solutions are

\[
f_\sigma(\rho,\omega)
=C_\sigma(\omega)\rho^{-2}
\exp\left(
\frac{A_\sigma}{4D_2}\rho^2
+
\frac{ra}{2D_2}\rho
\right),
\]

where

\[
A_\sigma=1-r(1-\sigma b).
\]

Near `ρ=0`, every nonzero solution behaves as `C(ω)ρ^{-2}`, which is not `L^2(R^3)` and not `H^{-1/2}`. A distributional solution cannot start at a positive radius without a singular source. Therefore every ray coefficient vanishes.

Since `E(v)=1` in Hypothesis S, stationary normalized states satisfy

\[
\boxed{R_{\rm fv}\ne0.}
\]

---

## Theorem S6 — Strict radial stability on both helicity sheets

The exact identity

\[
\boxed{
1-|b|-\frac{d^2}{D_3}
=
\frac{D_2(D_2-|Q|)}{D_3-Q^2}
}
\]

holds. Because `|Q|<D_2`,

\[
1-|b|>\frac{d^2}{D_3}=\frac1r.
\]

Hence for both helicities

\[
\boxed{
\chi_\sigma:=r(1-\sigma b)-1>0.
}
\]

Therefore

\[
\boxed{
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
(-\chi_\sigma\rho^2+ra\rho-4D_2)f_\sigma.
}
\]

On a compact nonexceptional stationary class, `χ_σ` has a positive uniform lower bound.

### Proof

Substitute the formulas of Theorem S2 into `1-|b|-d^2/D_3` and simplify. The strict inequality follows from `|Q|<D_2`.

---

## Theorem S7 — Canonical finite-energy radial inverse

Fix one sheet `σ` and the frozen stationary coefficients. Define

\[
\mathscr R_\sigma
=-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2+ra\rho-4D_2.
\]

Let

\[
h_\sigma(\rho)
=
\rho^{-2}
\exp\left(
-\frac{\chi_\sigma}{4D_2}\rho^2
+
\frac{ra}{2D_2}\rho
\right).
\]

Then

\[
\mathscr R_\sigma h_\sigma=0.
\]

For smooth forcing `F` supported in an annulus `0<ρ_0<ρ<ρ_1`, define

\[
\boxed{
(\mathcal S_\sigma F)(\rho,\omega)
=
-\frac{h_\sigma(\rho)}{2\kappa D_2}
\int_0^\rho
\frac{F(s,\omega)}{s h_\sigma(s)}\,ds.
}
\]

Then

\[
\boxed{
\kappa\mathscr R_\sigma\mathcal S_\sigma F=F.
}
\]

`\mathcal S_σF` is the unique finite-energy radial solution: it vanishes below the forcing annulus and above the annulus is a Gaussian-decaying multiple of `h_σ`.

### Proof

Write `f=h_σc`. Since `\mathscr R_σh_σ=0`,

\[
\mathscr R_\sigma(h_\sigma c)
=-2D_2\rho h_\sigma c'.
\]

Integrate `c'` from `0` to `ρ`. The infrared homogeneous branch behaves as `ρ^{-2}` and is not finite energy, so its coefficient must vanish. The ultraviolet branch decays because `χ_σ>0`.

---

## Theorem S8 — Direct-product absorption lemma

For any finite family of companion edges `e`, define

\[
\mathcal R_\Gamma
=\bigoplus_e\kappa\mathscr R_{\sigma_e},
\qquad
\mathcal S_\Gamma
=\bigoplus_e\mathcal S_{\sigma_e}.
\]

Then

\[
\boxed{\mathcal R_\Gamma\mathcal S_\Gamma=I.}
\]

Thus every finite tuple of physically generated annular companion forcings has a unique finite-energy edgewise absorber, and the radial equations impose no compatibility relation between distinct edges.

### Proof

Apply Theorem S7 independently on each direct-sum component. Reality completion commutes with the real radial coefficients and merely adds conjugate solutions.

---

## Theorem S9 — The only currently forced finite multiplicative invariant

For rank-one incidences `Z_{ij}=A_iB_j`, every alternating finite cycle

\[
i_1-j_1-i_2-j_2-\cdots-i_N-j_N-i_1
\]

has

\[
\boxed{
\operatorname{Hol}^{Z}_\Gamma
:=
\prod_{\ell=1}^{N}
\frac{Z_{i_\ell j_\ell}}
{Z_{i_{\ell+1}j_\ell}}
=1,
\qquad i_{N+1}=i_1.
}
\]

This invariant contains no radial transfer information.

### Proof

Use `Z_{ij}=A_iB_j`; all `B` factors cancel immediately and the product of `A_{i_\ell}/A_{i_{\ell+1}}` telescopes to one.

---

## Exact stationary frontier

The stationary problem has therefore been reduced to the exact equality

\[
\boxed{T=\kappa R_{\rm fv}}
\]

together with a canonical, edgewise-solvable radial absorption operator. The next theorem cannot be a local range/gain obstruction: `R_fv` can absorb arbitrary smooth annular forcing edge by edge. The formal consequences are recorded in `03_NO_GO_THEOREMS.md`.