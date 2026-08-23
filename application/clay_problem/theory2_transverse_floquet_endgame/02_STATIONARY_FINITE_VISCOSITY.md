# 02 — Stationary finite-viscosity reduction

All statements in this file are **EXACT** on the normalized stationary finite-\(\kappa\) class from `00_DEFINITIONS_AND_HYPOTHESES.md`.

---

## Theorem 1 — Stationary scalar constraints

For a normalized stationary candidate,

\[
\boxed{W=2\kappa D_3.}
\]

Let

\[
Q:=\langle v,C\Lambda v\rangle.
\]

Then the regression coefficients satisfy

\[
D_2=a+bQ,\qquad 0=aQ+bD_3,
\]

hence

\[
\boxed{
a=\frac{D_2D_3}{D_3-Q^2},
\qquad
b=-\frac{D_2Q}{D_3-Q^2}.
}
\]

Consequently

\[
\boxed{D_3-d^2=aD_2.}
\]

On a nonzero mixed-helicity stationary state, \(|Q|<D_2\), so \(|b|<1\).

---

## Theorem 2 — Exact stationary transverse saturation

Define

\[
Y=\Lambda^2v-D_2v+2D_2\mathcal Lv,
\qquad
r=\frac{D_3}{d^2},
\qquad
R_{\rm fv}=Y-rG.
\]

Then the stationary equation is equivalent to

\[
\boxed{N=\kappa Y.}
\]

Since on the stationary scalar stratum

\[
\gamma=\kappa r,
\]

and \(N=\gamma G+T\), one obtains

\[
\boxed{T=\kappa R_{\rm fv}.}
\]

### Proof

Substitute

\[
N=\kappa Y,
\qquad
Y=rG+R_{\rm fv},
\qquad
N=\gamma G+T,
\]

and use \(W=2\kappa D_3\), so

\[
\gamma=\frac{W}{2d^2}=\kappa\frac{D_3}{d^2}=\kappa r.
\]

The \(G\)-components agree, leaving \(T=\kappa R_{\rm fv}\). ∎

---

## Theorem 3 — Residual Pythagorean identity

For every scalar \(\lambda\),

\[
N-\lambda Y
=(\gamma-\lambda r)G+(T-\lambda R_{\rm fv}).
\]

The two summands are orthogonal in \(H^{-1/2}\). Therefore

\[
\boxed{
\|N-\lambda Y\|_{H^{-1/2}}^2
=
\|T-\lambda R_{\rm fv}\|_{H^{-1/2}}^2
+
\frac{(W/2-\lambda D_3)^2}{d^2}.
}
\]

Hence

\[
T=\lambda R_{\rm fv}
\quad\Longrightarrow\quad
N=\lambda Y
\iff
W=2\lambda D_3.
\]

In particular, stationarity tests the single gain

\[
\boxed{\lambda=\kappa,}
\]

not arbitrary positive alignment.

---

## Theorem 4 — Helicity-ray form of \(R_{\rm fv}\)

On helicity sheet \(\sigma=\pm1\), write \(\widehat v_\sigma=f_\sigma(\rho,\omega)\). Then

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

Define

\[
\chi_\sigma:=r(1-\sigma b)-1.
\]

Using the stationary regression identities,

\[
1-|b|-\frac{d^2}{D_3}
=
\frac{D_2(D_2-|Q|)}{D_3-Q^2}>0.
\]

Thus on every nonzero nonexceptional stationary state,

\[
\boxed{\chi_\sigma>0\qquad(\sigma=\pm1).}
\]

---

## Theorem 5 — Canonical finite-energy inverse

Fix one helicity sheet and write

\[
\mathscr R_\sigma
:=-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2+ra\rho-4D_2.
\]

Let

\[
h_\sigma(\rho)
=
\rho^{-2}
\exp\!\left(
-\frac{\chi_\sigma}{4D_2}\rho^2
+\frac{ra}{2D_2}\rho
\right).
\]

Then

\[
\mathscr R_\sigma h_\sigma=0.
\]

For smooth forcing \(F\) supported in an annulus

\[
0<\rho_0<\rho<\rho_1<\infty,
\]

the equation

\[
\kappa\mathscr R_\sigma f=F
\]

has the unique finite-\(H^{-1/2}\)-energy solution

\[
\boxed{
(\mathcal S_\sigma F)(\rho,\omega)
=
-\frac{h_\sigma(\rho)}{2\kappa D_2}
\int_0^\rho
\frac{F(s,\omega)}{s h_\sigma(s)}\,ds.
}
\]

It vanishes below the forcing annulus and has Gaussian ultraviolet decay.

### Proof

Set \(f=h_\sigma c\). Since \(\mathscr R_\sigma h_\sigma=0\),

\[
\mathscr R_\sigma(h_\sigma c)
=-2D_2\rho h_\sigma c'.
\]

Integrating gives the displayed formula. Any two finite-energy solutions differ by \(C(\omega)h_\sigma\). Since \(h_\sigma\sim \rho^{-2}\) as \(\rho\downarrow0\),

\[
\int_0^\varepsilon \rho|h_\sigma|^2\,d\rho=\infty,
\]

so the finite-energy homogeneous coefficient is zero. ∎

---

## Corollary 6 — Trivial finite-energy kernel

\[
\boxed{
\mathscr R_\sigma f=0,\quad f\in H^{-1/2}
\Longrightarrow f=0.
}
\]

Hence

\[
\boxed{R_{\rm fv}(v)=0\Longrightarrow v=0.}
\]

Since \(E(v)=1\), every normalized stationary candidate satisfies

\[
\boxed{R_{\rm fv}(v)\neq0.}
\]

---

## Theorem 7 — High-frequency coercivity is a resolvent estimate

For compactly supported \(f\),

\[
\operatorname{Re}\langle f,\mathscr R_\sigma f\rangle_{H^{-1/2}}
=
\int \rho\left(-\chi_\sigma\rho^2+ra\rho-2D_2\right)|f|^2\,d\rho d\omega.
\]

On a compact coefficient class with \(\chi_\sigma\ge\chi_K>0\), sufficiently high fixed-ratio annuli satisfy

\[
\boxed{
\|f\|_{H^{-1/2}}
\le C_K\rho_*^{-2}
\|\mathscr R_\sigma f\|_{H^{-1/2}}.
}
\]

This controls the size of an absorber. It does **not** obstruct existence of the absorber; Theorem 5 constructs it explicitly.

---

## Exact endpoint of the stationary reduction

The stationary problem has been reduced to excluding

\[
\boxed{T(v)=\kappa(v)R_{\rm fv}(v)}
\]

on the normalized nonexceptional compact class. The remaining obstruction is not radial solvability; it is the missing finite physical state-incidence compatibility analyzed next.