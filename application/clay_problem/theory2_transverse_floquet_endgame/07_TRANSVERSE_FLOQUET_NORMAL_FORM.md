# 07 — Transverse Floquet normal form and the current exact frontier

## 1. Starting point: finite-viscosity normalized flow

On `R^3`, after the canonical double normalization

\[
E(v)=M(v)=1,
\]

we have

\[
\boxed{
v_\theta
=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv,
}
\]

with

\[
\boxed{
\beta=W_\Lambda-2\kappa(D_3-D_2).
}
\]

Insert the exact constrained-gradient decomposition

\[
N=\gamma G+T,
\]

\[
G=\Lambda(\Lambda-a-bC)v.
\]

Then

\[
\boxed{
v_\theta
=\mathcal A_\theta(C)v-\beta\mathcal Lv+T,
}
\]

where

\[
\boxed{
\mathcal A_\theta(C)
=(\gamma-\kappa)C^2
-\gamma b\,C\Lambda
-\gamma a\,\Lambda
+\kappa D_2I.
}
\]

All nontransverse terms except dilation are functions of the fixed curl operator.

---

## 2. Exact removal of dilation

Define

\[
B(\theta)=\int_0^\theta\beta(s)\,ds
\]

and

\[
w(\theta)=e^{B(\theta)\mathcal L}v(\theta).
\]

Using

\[
[C,\mathcal L]=C,
\qquad
[\Lambda,\mathcal L]=\Lambda,
\]

we have

\[
e^{B\mathcal L}Ce^{-B\mathcal L}=e^{-B}C,
\]

\[
e^{B\mathcal L}\Lambda e^{-B\mathcal L}=e^{-B}\Lambda.
\]

Therefore

\[
\boxed{
w_\theta
=\widetilde{\mathcal A}_\theta(C)w
+e^{B\mathcal L}T,
}
\]

where

\[
\boxed{
\begin{aligned}
\widetilde{\mathcal A}_\theta(C)
={}&e^{-2B}
\left[(\gamma-\kappa)C^2-\gamma b\,C\Lambda\right]
\\
&-e^{-B}\gamma a\,\Lambda
+\kappa D_2I.
\end{aligned}
}
\]

At different times these operators commute because each is a scalar function of the same fixed `C`.

Thus

\[
\boxed{
[\widetilde{\mathcal A}_{\theta_1}(C),
\widetilde{\mathcal A}_{\theta_2}(C)]=0.
}
\]

---

## 3. Complete integration of all nontransverse dynamics

Define

\[
\Phi(\theta,C)
=\int_0^\theta\widetilde{\mathcal A}_s(C)\,ds.
\]

Then exactly

\[
\boxed{
\frac d{d\theta}
\left[
e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}v(\theta)
\right]
=
e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}T(\theta).
}
\]

This is the central normal form.

After factoring:

- constrained-gradient Formation;
- true heat;
- normalization scalar;
- physical dilation;

**only `T` remains.**

No additional source species is introduced.

---

## 4. Exact one-cycle transverse Floquet equation

Assume an exact normalized period `P`:

\[
v(P)=v(0),
\qquad
\kappa(P)=\kappa(0).
\]

Critical neutrality over the normalized cycle gives

\[
\int_0^PW\,d\theta
=2\int_0^P\kappa D_3\,d\theta.
\]

Therefore

\[
\boxed{
B_*:=B(P)=2\int_0^P\kappa D_2\,d\theta>0.
}
\]

Let

\[
\Phi_*:=\Phi(P,C).
\]

The homogeneous nontransverse monodromy is

\[
\boxed{
\mathcal M_0=e^{-B_*\mathcal L}e^{\Phi_*(C)}.
}
\]

Duhamel yields the exact recurrence equation

\[
\boxed{
v_0=\mathcal M_0v_0+G_T,
}
\]

where

\[
\boxed{
G_T=\int_0^P\mathcal U_0(P,s)T(s)\,ds
}
\]

and `\mathcal U_0` is the explicit nontransverse propagator.

Equivalently,

\[
\boxed{(I-\mathcal M_0)v_0=G_T.}
\]

This is the exact finite-Reynolds transverse replenishment equation.

---

## 5. Helicity-sheet monodromy coefficients

On a helical sheet

\[
C=\sigma\rho,
\qquad\sigma=\pm1,
\]

the cycle exponent is quadratic in `ρ`:

\[
\boxed{
\Phi_{*,\sigma}(\rho)
=C_0-A\rho+Q_\sigma\rho^2,
}
\]

where

\[
\boxed{
C_0=\int_0^P\kappa D_2\,d\theta=\frac{B_*}{2},
}
\]

\[
\boxed{
A=\int_0^P\gamma a\,e^{-B(\theta)}\,d\theta,
}
\]

and

\[
\boxed{
Q_\sigma
=\int_0^P
e^{-2B(\theta)}
\left[\gamma(1-\sigma b)-\kappa\right]
\,d\theta.
}
\]

Thus all nontransverse cycle complexity collapses to four real quantities

\[
B_*,\quad A,\quad Q_+,\quad Q_-.
\]

---

## 6. Critical log-frequency representation

Put

\[
\rho=e^s.
\]

For helical Fourier amplitude `f_σ(ρ,ω)`, define

\[
\boxed{
F_\sigma(s,\omega)=e^{2s}f_\sigma(e^s,\omega).
}
\]

Then the critical norm becomes

\[
\boxed{
M(v)
=\sum_{\sigma=\pm}
\int_{\mathbb R\times S^2}
|F_\sigma(s,\omega)|^2\,ds\,d\omega
}
\]

up to the fixed Fourier normalization convention.

In these coordinates the homogeneous monodromy is

\[
\boxed{
(\mathbb M_0F)_\sigma(s,\omega)
=w_\sigma(s)F_\sigma(s+B_*,\omega),
}
\]

with

\[
\boxed{
w_\sigma(s)
=\exp\left[
-Ae^{s+B_*}+Q_\sigma e^{2(s+B_*)}
\right].
}
\]

The scalar constant term cancels exactly because

\[
C_0=B_*/2.
\]

Therefore

\[
\boxed{
\lim_{s\to-\infty}w_\sigma(s)=1.
}
\]

The infrared characteristic is a pure critical translation

\[
F(s)\mapsto F(s+B_*).
\]

---

## 7. Exact no-go: no global critical Floquet gap

Because `w_σ(s)→1` as `s→-∞`, choose normalized smooth plateaux `F_L` supported increasingly far into negative `s` and with logarithmic length `L`.

Then

\[
\mathbb M_0F_L
\approx F_L(\cdot+B_*).
\]

For plateaux,

\[
\|F_L-F_L(\cdot+B_*)\|_2
=O\left(\sqrt{\frac{B_*}{L}}\right).
\]

Hence

\[
\boxed{
\inf_{\|F\|_M=1}
\|(I-\mathbb M_0)F\|_M=0.
}
\]

So no global critical coercive gap for `I-\mathbb M_0` can exist.

This is an exact structural no-go, not merely an estimate failure.

---

## 8. Relation to the forbidden `ρ^{-2}` branch

If `T=0`, recurrence requires

\[
F_\sigma(s)=w_\sigma(s)F_\sigma(s+B_*).
\]

At `s→-∞`,

\[
F_\sigma(s)\sim F_\sigma(s+B_*),
\]

so a nonzero homogeneous solution approaches a nondecaying / log-periodic critical amplitude.

Since

\[
f_\sigma(\rho)=\rho^{-2}F_\sigma(\log\rho),
\]

this reproduces

\[
\boxed{
f_\sigma(\rho)\sim\rho^{-2}\times\text{log-periodic factor}.}
\]

The previously derived non-`L^2` `T=0` profile is therefore the zero-frequency characteristic of the complete finite-step monodromy.

---

## 9. Actual normalized states cannot carry order-one critical mass at the characteristic

Because

\[
E(v)=1,
\]

for every `ρ_0>0`,

\[
\boxed{
M_{<\rho_0}
=\int_{|\xi|<\rho_0}|\xi||\hat v|^2
\le\rho_0E
=\rho_0.
}
\]

Similarly,

\[
\boxed{
M_{>R}\le\frac{D_2}{R}.
}
\]

Therefore if a recurrent normalized family has

\[
D_2\le D_*,
\]

then for each `ε>0`,

\[
\boxed{
M_{[\varepsilon,D_*/\varepsilon]}
\ge1-2\varepsilon.
}
\]

Thus the global operator gap fails, but a compact normalized recurrent family is critically tight away from the asymptotic characteristic.

This distinction is essential.

---

## 10. Compact recurrent family implies a transverse Floquet debt

Assume an exact periodic family with uniform bounds

\[
0<\kappa_0\le\kappa\le\kappa_1,
\]

\[
P\ge P_0>0,
\]

\[
D_2\le D_*.
\]

Then

\[
B_*=2\int_0^P\kappa D_2\,d\theta
\ge2\kappa_0P_0>0.
\]

Critical mass is concentrated in a finite log-frequency interval. Repeated homogeneous shifts by `B_*` leave that interval after finitely many iterations. On the finite enlarged interval the weights are uniformly controlled under the compactness hypotheses.

Iterating

\[
F=\mathbb M_0F+\mathbb G_T
\]

therefore gives a positive lower bound on the propagated transverse source required per recurrence:

\[
\boxed{
\|\mathbb G_T\|_{\rm relevant\ band}
\ge c_{\mathcal K}>0.
}
\]

This is a **DEDUCTION** from the exact Floquet equation plus compact critical spectral tightness.

It is mode-count independent.

---

## 11. Nonzero recurrence requires transverse ancestry to arbitrarily small normalized radii

Suppose for one helicity sheet the cycle source vanished below a finite log-frequency threshold:

\[
\mathbb G_{T,\sigma}(s,\omega)=0
\qquad(s<s_0).
\]

Then below that scale the recurrence is homogeneous:

\[
F_\sigma(s)=w_\sigma(s)F_\sigma(s+B_*).
\]

Finite energy eliminates the non-`L^2` homogeneous infrared branch, so `F_σ` vanishes sufficiently far left. Since `w_σ` never vanishes, the recurrence relation propagates this zero upward in increments of `B_*`.

Therefore

\[
\boxed{F_\sigma\equiv0.}
\]

Hence a nonzero recurrent finite-`κ` profile necessarily has transverse one-cycle ancestry at arbitrarily small normalized radii.

This does **not** imply order-one critical mass at those radii; `M_{<ρ}≤ρ` shows the mediators may have vanishing critical mass.

---

## 12. Hostile correction: full Formation can regularize the infrared branch

A stationary finite-`κ` normalized profile satisfies

\[
W=2\kappa D_3,
\qquad
\beta=2\kappa D_2.
\]

The stationary Fourier equation can be written

\[
\boxed{
\rho\partial_\rho f
+\left(2-\frac{\rho^2}{2D_2}\right)f
=-\frac{\widehat N}{2\kappa D_2}.
}
\]

The homogeneous solution is the forbidden `ρ^{-2}` branch.

Under sufficient regularity/decay for the physical convolution to admit the low-output expansion, the exact output-frequency null form gives

\[
\widehat N(\rho\omega)=O(\rho).
\]

Then the finite-energy particular solution satisfies

\[
\boxed{f(\rho,\omega)=O(\rho)}
\qquad(\rho\downarrow0).
\]

So full transverse Formation has exactly the correct low-frequency order to repair the forbidden homogeneous branch.

This is why the `T=0` nonexistence theorem cannot be perturbed directly to a `T\ne0` nonexistence theorem.

### Optional leading coefficient under stronger decay

If the Fourier convolution admits

\[
\widehat N(k)
=-iP_k(\mathsf Rk)+O(|k|^2),
\]

with

\[
\mathsf R=\int v\otimes v\,dx,
\]

then a stationary profile has

\[
f(\rho,\omega)=\rho A(\omega)+o(\rho)
\]

with

\[
\boxed{
A(\omega)
=\frac{i}{6\kappa D_2}
P_\omega(\mathsf R\omega)
}
\]

up to Fourier sign convention.

This is a conditional asymptotic refinement, not an unconditional finite-energy theorem.

---

## 13. Exact stationary helicity-sheet rigidity

Let

\[
h=\langle v,Cv\rangle
\]

and

\[
H_3=\langle v,C^3v\rangle=D_+-D_-.
\]

The normalized helicity equation is

\[
\boxed{
h_\theta=-Wh+2\kappa(D_3h-H_3).}
\]

At a stationary normalized finite-`κ` profile,

\[
h_\theta=0,
\qquad
W=2\kappa D_3,
\]

so

\[
\boxed{H_3=0.}
\]

Equivalently,

\[
\boxed{D_+=D_-=D_3/2.}
\]

This is a finite rigidity condition. It is not to be iterated into an infinite scalar moment hierarchy.

---

## 14. Current theorem target

The complete finite-Reynolds recurrence problem has now become

\[
\boxed{
F=\mathbb M_0[F]F+\mathbb G_T[F].
}
\]

Here

- `\mathbb M_0` is an explicit weighted log-frequency translation determined by four cycle integrals;
- `\mathbb G_T` is the one-cycle propagated actual transverse Formation source.

The remaining theorem is:

\[
\boxed{
\begin{aligned}
&\textbf{Transverse Floquet rigidity:}\\
&\text{the actual Theory-2 source }T(v)\text{ cannot solve the compact}\
&\text{finite-Reynolds recurrent fixed-point equation except on the}\
&\text{classified null/thin-shell/collinear limits or by genuine loss}\
&\text{of compactness in log-scale.}
\end{aligned}
}
\]

**Status: OPEN.**

This is the latest exact frontier.
