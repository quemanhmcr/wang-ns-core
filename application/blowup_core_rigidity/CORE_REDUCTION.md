# Full-State Core Reduction of the Blow-up Problem

## 1. Typed setting

Work first on smooth mean-zero divergence-free fields on a periodic/closed three-dimensional Euclidean domain, where

\[
C=\operatorname{curl},
\qquad
\Lambda=|C|,
\qquad
C=H\Lambda,
\qquad
H=\operatorname{sgn}C.
\]

The equation is formed by the single core datum

\[
\mathcal C_{NS}
=(\mathfrak g_\sigma,[\cdot,\cdot],\langle\cdot,\cdot\rangle,C)
\]

through

\[
\langle a,\mathcal J_ub\rangle=-\langle u,[a,b]\rangle,
\]

\[
B(u,u)=\mathcal J_uu,
\]

and

\[
\boxed{u_t=B(u,u)-\nu C^2u.}
\]

All application formulas below are derived from this full state; no lower-dimensional observer is substituted for \(u\).

## 2. Critical balance

Define

\[
K(u)=\langle u,\Lambda u\rangle
=\|\Lambda^{1/2}u\|_2^2.
\]

Then

\[
\frac12K'(t)
=\langle\Lambda u,B(u,u)\rangle
-\nu\langle\Lambda u,C^2u\rangle.
\]

Since \(C^2=\Lambda^2\) on the typed divergence-free block,

\[
\boxed{
\frac12K'
=W_c(u)-\nu\|\Lambda^{3/2}u\|_2^2,
\qquad
W_c(u)=\langle\Lambda u,B(u,u)\rangle.
}
\]

The same nonlinear term is

\[
W_c(u)=\frac12\langle u,[\Lambda,\mathcal J_u]u\rangle.
\]

Hence with

\[
z=\Lambda^{3/2}u,
\qquad
\mathscr R_u
=\frac12\Lambda^{-3/2}[\Lambda,\mathcal J_u]\Lambda^{-3/2},
\]

one obtains

\[
\boxed{
\frac12K'=
\langle z,(\mathscr R_u-\nu I)z\rangle.
}
\]

Because \(\Lambda^*=\Lambda\) and \(\mathcal J_u^*=-\mathcal J_u\),

\[
\boxed{\mathscr R_u^*=\mathscr R_u.}
\]

The identity is scale-critical: under Navier–Stokes dilation \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\), the normalized curvature operator is conjugated by the corresponding unitary \(L^2\) dilation, so its spectrum is dimensionless.

## 3. Chiral reduction of critical work

Helicity is a Casimir of the Euler Poisson structure:

\[
\boxed{\mathcal J_u(Cu)=0.}
\]

Let

\[
P_\pm=\frac{I\pm H}{2},
\qquad
u_\pm=P_\pm u,
\]

and

\[
A_u=P_+\mathcal J_uP_-.
\]

Since \(C=H\Lambda\), the Casimir identity gives

\[
\boxed{
W_c(u)
=\langle Cu,[H,\mathcal J_u]u\rangle
=2\operatorname{Re}\langle u_+,[\Lambda,A_u]u_-\rangle.
}
\]

Consequences:

1. a single helicity sheet cannot produce critical Euler growth by itself;
2. cross-helicity interaction is still insufficient if it commutes with \(\Lambda\);
3. the critical production is exactly a chiral-radial incompatibility of the same core operator \(\mathcal J_u\).

For a helical triad with signed curl eigenvalues

\[
x_0=-a,
\qquad
x_1=b,
\qquad
x_2=c,
\qquad a,b,c>0,
\]

the universal \(q(x)=|x|\) reader signature reduces to

\[
\boxed{2a(b-c).}
\]

Thus critical triad production requires both sign mixing and radial mismatch.

## 4. Spectral stress as a full-state renderer

Define

\[
\mathcal T_u(q)=\langle q(C)u,B(u,u)\rangle.
\]

The energy and helicity cancellations are

\[
\boxed{\mathcal T_u(1)=0,\qquad \mathcal T_u(x)=0.}
\]

Define

\[
\boxed{\Sigma_u(r)=\mathcal T_u((x-r)_+).}
\]

For a sufficiently regular scalar reader \(q\), its affine part is invisible to \(\mathcal T_u\), and the hinge representation yields

\[
\boxed{\mathcal T_u(q)=\int_{\mathbb R}q''(r)\Sigma_u(r)\,dr.}
\]

For \(q(x)=|x|\),

\[
q''=2\delta_0,
\]

so

\[
\boxed{W_c(u)=2\Sigma_u(0).}
\]

Define the signed-curl energy measure by

\[
\int q(x)\,d\mu_u(x)=\frac12\langle u,q(C)u\rangle.
\]

Then

\[
\boxed{
\partial_t\mu=\partial_x^2\Sigma-2\nu x^2\mu
}
\]

in distributions.

This equation is not closed in \(\mu\) alone; the stress \(\Sigma_u\) is reconstructed from the complete physical state.  The formulation therefore does not introduce a spectral closure assumption.

## 5. High-frequency critical excess

For \(R>0\), define

\[
q_R(x)=(|x|-R)_+,
\qquad
X_R(t)=\int q_R(x)\,d\mu_t(x).
\]

Since

\[
q_R''=\delta_R+\delta_{-R},
\]

one obtains

\[
\boxed{
\dot X_R
=
\Sigma_u(R)+\Sigma_u(-R)
-2\nu\int x^2q_R(x)\,d\mu_t(x).
}
\]

On the support of \(q_R\), \(x^2\ge R^2\).  Therefore

\[
\boxed{
\dot X_R+2\nu R^2X_R
\le
\Sigma_u(R)+\Sigma_u(-R).
}
\]

The corresponding Duhamel inequality is

\[
\boxed{
X_R(t)
\le
e^{-2\nu R^2(t-s)}X_R(s)
+
\int_s^t e^{-2\nu R^2(t-\tau)}
[\Sigma_u(R,\tau)+\Sigma_u(-R,\tau)]_+\,d\tau.
}
\]

Thus a dangerous high-frequency packet must be regenerated on the parabolic memory scale \((\nu R^2)^{-1}\).  A single finite locking episode cannot by itself create a singularity.

## 6. Why static barriers are insufficient

The quadratic core has spectral ancestry.  In Fourier variables, an output frequency is the sum of its two parents.  Therefore

\[
\boxed{
P_{>R}B(u,u)
=
P_{>R}\Bigl(
2B(u_{>R/2},u_{\le R/2})
+B(u_{>R/2},u_{>R/2})
\Bigr).
}
\]

A new high-frequency tail can be seeded from an already populated parent octave, even if the target tail is initially empty.  Consequently no proof based only on a static inequality involving the target tail can represent the full closure geometry.

For a packet localized near frequency \(R\) with critical mass

\[
M_R\sim R\|u_R\|_2^2,
\]

scaling gives

\[
|W_c(u_R)|\lesssim R^2M_R^{3/2},
\]

whereas viscous critical dissipation is

\[
\nu\|\Lambda^{3/2}u_R\|_2^2\sim\nu R^2M_R.
\]

Therefore super-viscous growth is compatible with the critical packet scale

\[
M_R\gtrsim c\nu^2.
\]

Neither finite energy nor the parabolic lifetime alone rules out an infinite octave genealogy.  The missing theorem must use the complete interaction geometry, not only dimensional budgets.

## 7. Amplitude–dilation normalization

This section is typed on \(\mathbb R^3\), or equivalently in a rescaled local blow-up coordinate chart where the Navier–Stokes dilation is available continuously.  On a fixed torus, continuous dilation is not an internal symmetry and this quotient must not be read literally without changing the domain.

Let

\[
A=\sqrt{K(u)},
\qquad
\rho=\frac{K(u)}{E(u)},
\qquad
E(u)=\|u\|_2^2.
\]

Write

\[
\boxed{u=A S_\rho v,\qquad (S_\rho f)(x)=\rho f(\rho x).}
\]

Because \(K\) is invariant under \(S_\rho\) and \(E(S_\rho v)=\rho^{-1}E(v)\), one obtains

\[
\boxed{
\|v\|_2^2=1,
\qquad
\|\Lambda^{1/2}v\|_2^2=1.
}
\]

Let

\[
\frac{d\tau}{dt}=A\rho^2,
\qquad
G=I+x\cdot\nabla.
\]

Differentiating \(u=A S_\rho v\) and using the scaling of \(B\) and \(C^2\) gives

\[
\boxed{
 v_\tau
 =B(v,v)-\varepsilon C^2v-\alpha v-\beta Gv,
 \qquad
 \varepsilon=\frac\nu A.
}
\]

Define

\[
W(v)=\langle\Lambda v,B(v,v)\rangle,
\]

\[
M_2(v)=\|\Lambda v\|_2^2,
\qquad
M_3(v)=\|\Lambda^{3/2}v\|_2^2.
\]

The normalization constraints imply

\[
\boxed{\alpha=W-\varepsilon M_3,}
\]

\[
\boxed{\beta=2W-2\varepsilon(M_3-M_2).}
\]

Hence

\[
\boxed{
 v_\tau
 =B(v,v)-\varepsilon C^2v
 -(W-\varepsilon M_3)v
 -\bigl(2W-2\varepsilon(M_3-M_2)\bigr)Gv.
}
\]

This is an exact full-state equation as long as the smooth solution and the normalization are defined.

## 8. Core END Flow

On a hypothetical critical blow-up sequence \(A\to\infty\), so \(\varepsilon=\nu/A\to0\).  The candidate limiting normalized flow is

\[
\boxed{
 v_\tau=B(v,v)-2W(v)\mathcal Sv,
 \qquad
 \mathcal S=x\cdot\nabla+\frac32.
}
\]

The reconstructed amplitude and scale obey

\[
\boxed{(\log A)_\tau=W(v),}
\]

\[
\boxed{(\log\rho)_\tau=2W(v).}
\]

Therefore a normalized limiting orbit capable of supporting blow-up must satisfy

\[
\boxed{
\int_0^T W(v(\tau))\,d\tau\to+\infty.
}
\]

This is the final scalar drift extracted from the complete normalized state.  The state itself is never replaced by that scalar.

## 9. Helicity under the normalized flow

Let

\[
h(v)=\langle v,Cv\rangle.
\]

Because physical Euler helicity is conserved and the Navier–Stokes dilation leaves helicity scale-invariant,

\[
\mathcal H(u)=A^2h(v).
\]

In the inviscid normalized limit,

\[
\boxed{h_\tau=-2W(v)h.}
\]

Hence

\[
\boxed{
h(\tau)=h(0)\exp\!\left(-2\int_0^\tau W(v(s))\,ds\right).
}
\]

Any recurrent normalized orbit with positive mean critical drift must therefore have

\[
\boxed{h\equiv0.}
\]

This is a core consequence, not an imposed alignment hypothesis.

## 10. Fixed points and dilation-relative profiles

A fixed point of the Core END Flow satisfies

\[
B(v,v)=2W(v)\mathcal Sv.
\]

Writing

\[
b=2W(v)>0
\]

gives

\[
\boxed{
B(v,v)=b\left(x\cdot\nabla+\frac32\right)v.
}
\]

Pairing with \(Cv\) and using the helicity Casimir yields

\[
\boxed{\langle v,Cv\rangle=0.}
\]

This is the exact zero-helicity dilation-lock equation.  Its nonexistence in the relevant finite-energy three-dimensional class would exclude exact fixed-point/self-similar normalized enemies, but not all recurrent or noncompact normalized dynamics.

## 11. What remains after all observer loss is removed

After amplitude and scale normalization, a singular scenario can no longer hide in a diverging scalar magnitude or a drifting characteristic frequency.  The unresolved possibility is genuine infinite-dimensional noncompactness of the complete normalized state:

- concentration;
- profile splitting;
- oscillatory interaction defects;
- recurrent migration through ever-new \((T,C)\)-closure sectors.

This is not observer blindness.  It is a real compactness problem in the full critical state space.

The application therefore reduces the regularity question to a single full-core rigidity target rather than to a list of separate mechanisms.
