# 03 — Renormalized critical current, triadic curvature, and live side channels

## Status

This note records exact critical-production identities and the finite-band coercivities they imply.  Pair-source geometry is kept separate from closed-triad critical work.

## 1. Pair source is not critical production

For a Fourier pair `a+b=s`, the projected source

\[
P_s\mathcal B(a,b)
\]

says what the two parent modes try to generate at output `s`.  It does **not** by itself give critical production.  The exact critical work is the closed cubic quantity

\[
\boxed{
\mathcal T(u)
=\operatorname{Re}\langle N,|C|u\rangle
=\frac12\operatorname{Re}\langle u,[\Gamma_u,|C|]u\rangle.
}
\tag{1.1}
\]

The output must already carry amplitude and phase for the source to perform work.

## 2. Affine spectral defect of `|C|` — EXACT identity

Euler energy and helicity conservation give

\[
\operatorname{Re}\langle N,u\rangle=0,
\qquad
\operatorname{Re}\langle N,Cu\rangle=0.
\]

Hence for every real `alpha,beta`,

\[
\boxed{
\mathcal T(u)
=\operatorname{Re}\left\langle
N,(|C|-\alpha-\beta C)u
\right\rangle.
}
\tag{2.1}
\]

Consequences:

- if `u` is homochiral, `|C|=+/- C` on the state and `T=0`;
- if the signed-curl spectral support lies on a single absolute radius, `|C|=rI` on the state and `T=0`.

On a normalized finite frequency window, after remote forcing is put into a controlled error and the localized nonlinear source is uniformly bounded, a fixed production floor implies the coercive locator

\[
\boxed{
\inf_{\alpha,\beta}
\|(|C|-\alpha-\beta C)U\|_2
\ge c(\delta,M,L)>0.
}
\tag{2.2}
\]

The scalar in (2.2) is not a state.  Spectrally it is the least-squares error of fitting the V-shaped graph `lambda -> |lambda|` by one affine line on the signed-curl spectral measure of `U`.

Because an affine line fits any two signed spectral points, a quantitative defect in a compact normalized interval forces three quantitatively separated signed-curl sectors carrying nontrivial mass.  In particular both helicities are present and at least one helicity sign has radial multiplicity.

## 3. Exact heterochiral closed-triad curvature

Consider one isolated helical Euler triad with signed curl eigenvalues

\[
\lambda_i=\sigma_i k_i,
\qquad k_i=|\xi_i|,
\qquad \xi_1+\xi_2+\xi_3=0.
\]

Let `e_i` be the modal kinetic-energy rates.  Energy and helicity conservation give

\[
e_1+e_2+e_3=0,
\qquad
\lambda_1e_1+\lambda_2e_2+\lambda_3e_3=0.
\tag{3.1}
\]

When these constraints are independent,

\[
(e_1,e_2,e_3)
=\mathcal A
(\lambda_2-\lambda_3,
 \lambda_3-\lambda_1,
 \lambda_1-\lambda_2).
\tag{3.2}
\]

The critical-norm contribution is

\[
\dot Q_{\rm triad}
=\sum_i|\lambda_i|e_i.
\]

With the convention (3.2),

\[
\boxed{
\dot Q_{\rm triad}
=-\mathcal A
\det
\begin{pmatrix}
1&1&1\\
\lambda_1&\lambda_2&\lambda_3\\
|\lambda_1|&|\lambda_2|&|\lambda_3|
\end{pmatrix}.
}
\tag{3.3}
\]

This is the exact discrete curvature of the function `|lambda|` against the two conserved affine functions `1` and `lambda`.

For a `++-` triad

\[
\lambda_1=\alpha>0,
\qquad
\lambda_2=\beta>0,
\qquad
\lambda_3=-\gamma<0,
\]

one gets

\[
\boxed{
\dot Q_{\rm triad}
=2\gamma(\alpha-\beta)\mathcal A.
}
\tag{3.4}
\]

Moreover

\[
e_3=(\alpha-\beta)\mathcal A,
\]

so

\[
\boxed{
\dot Q_{\rm triad}=2\gamma e_{\rm minority}.
}
\tag{3.5}
\]

Thus positive critical production in a heterochiral triad is equivalent to kinetic-energy gain of the unique minority-helicity leg.  Nonzero production also requires radial asymmetry between the two same-helicity legs.

Homochiral triads give zero critical production because `|lambda|` is affine on one helicity half-line.

## 4. Exact physical-space heterochiral production

Write

\[
u=u_++u_-,
\qquad
Cu=\Lambda u_+-\Lambda u_-,
\qquad
\Lambda u=\Lambda u_++\Lambda u_-.
\]

Using the rotational Euler form and scalar triple products,

\[
\boxed{
\mathcal T(u)
=2\int_{\mathbb R^3}
u\cdot
(\Lambda u_+\times\Lambda u_-)\,dx
}
\tag{4.1}
\]

up to the globally fixed sign convention.

This immediately gives, on a normalized finite band,

\[
|\mathcal T|
\lesssim
\|P(u_+\times\Lambda u_+)\|_2\|\Lambda u_-\|_2
+
\|P(u_-\times\Lambda u_-)\|_2\|\Lambda u_+\|_2.
\tag{4.2}
\]

Hence a fixed production floor forces

\[
\boxed{
\max_{\sigma=\pm}
\|P(u_\sigma\times\Lambda u_\sigma)\|_2
\ge c(\delta,M,L).
}
\tag{4.3}
\]

An efficient state is therefore separated, in at least one helicity sector, from single-radius Beltrami-by-helicity geometry.

## 5. Single-pair output polarization — EXACT

For pure-helicity parent modes `(a,sigma)` and `(b,tau)`, let

\[
\alpha=|a|,
\qquad
\beta=|b|,
\qquad
s=a+b.
\]

In the triad plane basis, the projected source has shape

\[
P_s\mathcal B(a,b)
\propto
\sin\theta
\left[
\frac{\beta^2-\alpha^2}{|s|}t_s
+i(\beta\tau-\alpha\sigma)n
\right]AB.
\tag{5.1}
\]

For every nonzero noncollinear interaction, both output helicities are nonzero.  A one-helicity output can occur only at a source-null triangle degeneration; equal-radius homochiral parents give the familiar complete null.

The ratio between weaker and stronger child-helicity amplitudes is controlled exactly by triangle defects.  These pairwise facts are source geometry, not yet closed-triad work.

## 6. Productive triad forces a comparable reality-difference source

Take the two same-helicity majority legs `k,p` of a quantitatively productive heterochiral triad.  By (3.4),

\[
|k|\ne|p|.
\]

Reality supplies the mode `-p` with the same helicity label.  The pair `(k,-p)` outputs

\[
d=k-p.
\]

It is a same-helicity, unequal-radius, noncollinear pair, so (5.1) gives a nonzero source with both child helicities.  It cannot use the equal-radius homochiral null.

If a coarse productive channel carries a fixed fraction of normalized critical production and parent scale ratios stay in a compact interval, the amplitude bounds force quantitative separation from both radial-equality and collinearity.  Consequently

\[
\boxed{|d|\simeq K}
\tag{6.1}
\]

for the front scale `K`, and the difference source has fixed nonzero strength.

For

\[
s=k+p,
\qquad d=k-p,
\]

one has the exact geometry

\[
\boxed{s\cdot d=|k|^2-|p|^2.}
\tag{6.2}
\]

The orthogonal equal-radius twin mechanism occurs only when the critical triad leverage vanishes.  Therefore a productive triad forces a genuinely comparable **live side source channel**.  This does not yet prove that the resulting child participates nontrivially in the next generation; further polarization/network geometry is required.

## 7. Equal-radius heterochiral reality twin — EXACT special case

For a source pair with

\[
|a|=|b|=r,
\qquad \tau=-\sigma,
\]

reality supplies outputs

\[
s=a+b,
\qquad d=a-b,
\]

with

\[
\boxed{s\cdot d=0.}
\tag{7.1}
\]

Both source vectors are pure-normal and have equal raw magnitude

\[
\boxed{|F_s|=|F_d|=r\sin\theta\,|AB|}
\tag{7.2}
\]

up to the common normalization convention.  This is a useful leakage lemma, but because equal-radius same-helicity critical leverage is zero it is not itself the geometry of a productive closed critical triad.

## 8. Exact finite-scale increment current on `R^3`

For smooth decaying divergence-free fields, the fractional-Laplacian representation and transport symmetrization give

\[
\boxed{
\mathcal T(u)
=c
\iint
\frac{
[(u(x)-u(y))\cdot(x-y)]
|u(x)-u(y)|^2
}{|x-y|^6}
\,dx\,dy
}
\tag{8.1}
\]

up to a universal sign/normalization constant.

Writing `y=x+r omega`, define

\[
\Phi_u(r)
=r^{-2}
\int_{\mathbb R^3}\int_{S^2}
[\delta_{r,\omega}u(x)\cdot\omega]
|\delta_{r,\omega}u(x)|^2
\,d\omega dx.
\]

Then

\[
\mathcal T(u)=c\int_0^\infty\Phi_u(r)\frac{dr}{r}.
\tag{8.2}
\]

Incompressibility gives the exact spherical cancellation

\[
\boxed{
\int_{S^2}\delta_{r,\omega}u(x)\cdot\omega\,d\omega=0.
}
\tag{8.3}
\]

Critical transfer therefore requires correlation between radial increment sign and increment energy; isotropic radial compression alone cannot produce it.  Equation (8.1) is an exact finite-scale identity, not a principal-symbol approximation.

## 9. Arbitrary moving scale — EXACT

Let

\[
u(x,t)=\lambda(t)U(y,s),
\qquad
y=\lambda(t)(x-x_c(t)),
\qquad
\frac{ds}{dt}=\lambda^2.
\]

Put

\[
\beta=\frac{\lambda_t}{\lambda^3},
\qquad
\gamma=\frac{x_c'}{\lambda}.
\]

Then

\[
U_s+\beta(U+y\cdot\nabla U)-\gamma\cdot\nabla U+\Gamma_UU
=-\nu C^2U.
\tag{9.1}
\]

For

\[
X_\sigma=\|U\|_{\dot H^\sigma}^2,
\]

\[
\boxed{
\frac12X_\sigma'
+\frac{2\sigma-1}{2}\beta X_\sigma
+\nu X_{\sigma+1}
=\mathcal N_\sigma(U).
}
\tag{9.2}
\]

At `sigma=1/2` the dilation drift vanishes for **every** dynamic choice of scale:

\[
\boxed{
\frac12X_{1/2}'+\nu X_{3/2}=\mathcal T(U).
}
\tag{9.3}
\]

This is why the critical norm is the correct moving-front metric.

## 10. Renormalized complete Mother cocycle — EXACT pathwise

Let `M(U)=E_U` and `R_E` be the Theory-2 decoder.  Applying the linear Mother map to (9.1) gives

\[
\boxed{
E_s
=\mathcal M\!\left(
-\Gamma_UU-\nu C^2U
-\beta(U+y\cdot\nabla U)
+\gamma\cdot\nabla U
\right),
\qquad U=R_EE.
}
\tag{10.1}
\]

The full shifted signature is reconstructed from the same physical state.  Hence renormalization changes coordinates but does not replace the complete Theory-2 state by the critical current.

## 11. What these identities do and do not prove

They prove that a productive finite-density front must simultaneously carry:

- both helicities;
- non-affine signed-curl radial structure;
- same-helicity radial multiplicity;
- a fixed homochiral self-interaction field in at least one sign;
- exact finite-scale increment anisotropy;
- comparable side-source channels forced by productive triads.

They do **not** prove that a broadband state must generate new Fourier support: a full annulus may already contain every side output.  The remaining enemy can therefore be a genuinely continuous mixed-helicity interaction medium.  `04`--`05` address the causal compactification and the self-generated recurrent mixer problem for that broadband case.