# Formation–Signature Equivalence on a Fixed Physical Core

## 1. Formation background

Work first on the smooth mean-zero divergence-free periodic state space, with

\[
\mathcal C_{NS}
=(\mathfrak g_\sigma,g,T,C),
\qquad
g(a,b)=\langle a,b\rangle_{L^2},
\qquad
T(a,b,c)=\langle a,[b,c]\rangle.
\]

The Koszul formula reconstructs the Levi–Civita connection from \((g,T)\):

\[
2g(\nabla_ab,c)
=g([a,b],c)-g([b,c],a)+g([c,a],b).
\]

The state-dependent Poisson operator is the Riesz representative

\[
g(a,\mathcal J_ub)=-T(u,a,b),
\]

and the full formation operator is

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2.
}
\]

Navier–Stokes is its diagonal flow:

\[
\boxed{u_t=\mathcal L_{\nu,u}u.}
\]

These are exact identities of the formation core; see the parent [formation core](../metric_lie_hodge/FORMATION_LAW.md).

## 2. Forward functor to the mother and shifted flag

Once \(\nabla\) and the distinguished curl \(C\) are fixed, define

\[
\boxed{E_u=[\nabla_u,C].}
\]

For the shifted involutions

\[
H_a=\operatorname{sgn}(C-aI),
\]

the spectral-signature core defines the shifted operator-valued family \(\mathscr O_a(u)\).  Its reverse compiler reconstructs \([\nabla_u,H_a]\), and the spectral layer cake reconstructs

\[
\boxed{
E_u
=\frac12\int_{\mathbb R}[\nabla_u,H_a]\,da.
}
\]

Therefore, on the typed smooth periodic setting,

\[
\boxed{
(g,T,C,u)
\longrightarrow
\nabla_u
\longrightarrow
E_u
\longleftrightarrow
\{\mathscr O_a(u)\}_a.
}
\]

The first arrow is formation geometry; the second is a commutator representation; the last equivalence is the existing spectral tomography theorem.

## 3. Reverse bridge to state and formation operator

The spectral core proves that the principal symbol of \(E_u\) is the strain quadratic form times the canonical quarter-turn on each transverse plane.  Writing

\[
q_u(x,n)=n^TS(u)(x)n,
\]

spherical or finite-frame inversion reconstructs \(S(u)\), and incompressibility gives

\[
\Delta u=2\operatorname{div}S(u).
\]

Thus, modulo the Euclidean Killing sector and uniquely on the mean-zero periodic class,

\[
\boxed{
E_u\Longrightarrow u,
\qquad
\{\mathscr O_a(u)\}\Longrightarrow u.
}
\]

Because the physical formation core is fixed, state reconstruction immediately gives

\[
\boxed{
E_u\Longrightarrow\mathcal J_u\Longrightarrow\mathcal L_{\nu,u},
}
\]

and the same for the full shifted flag.

An independent six-direction microlocal audit avoided the finite-dimensional core pseudoinverse entirely.  It used only six values of \(q_u(x,n_r)\), reconstructed

\[
q\to S\to u\to Cu\to\mathcal J_u\to\mathcal L_{\nu,u},
\]

and obtained worst residual \(3.13\times10^{-15}\) across the tested periodic states.

## 4. The complete formation geometry transports to the signature image

Let \(M\) be an invertible reduced coordinate map from physical state coordinates \(u\) to mother or shifted-flag coordinates \(z=Mu\).  With \(R=M^{-1}\), the transported metric is

\[
\boxed{G_\Sigma=R^T R.}
\]

The transported curl is

\[
\boxed{C_\Sigma=MCR,}
\]

and the metric-lowered Lie tensor is

\[
\boxed{
(T_\Sigma)_{pqr}
=R_{ip}R_{jq}R_{kr}T_{ijk}.
}
\]

The state-dependent Poisson tensor is then recovered by the Riesz equation

\[
G_\Sigma\mathcal J_\Sigma(z)
=-\sum_i z_i(T_\Sigma)_i.
\]

Consequently

\[
\boxed{
\mathcal L_\Sigma(z)
=\mathcal J_\Sigma(z)-\nu C_\Sigma^2
=M\mathcal L_{\nu,u}M^{-1}.
}
\]

The 28-dimensional blind tribunal reconstructed the complete formation operator from both mother and full flag coordinates at residuals \(2.24\times10^{-16}\) and \(3.25\times10^{-16}\), respectively.

## 5. Dynamic commuting diagram

The representation is not only snapshot-complete.  Let

\[
F(u)=\mathcal L_{\nu,u}u.
\]

Transport it to signature coordinates:

\[
F_\Sigma(z)=M F(M^{-1}z).
\]

Then the diagram

\[
\begin{array}{ccc}
u(t)&\xrightarrow{\ \text{NS flow}\ }&u(t+h)\\
\downarrow M&&\downarrow M\\
z(t)&\xrightarrow{\ \text{signature flow}\ }&z(t+h)
\end{array}
\]

commutes exactly at the algebraic level.  Independent RK4 integrations in the audit agreed at \(1.45\times10^{-15}\) for mother coordinates, \(9.11\times10^{-16}\) for full-flag reduced coordinates, and \(2.07\times10^{-15}\) for the independent six-direction microlocal signature evolution.

## 6. Exact Galilean kernel

When the three constant modes are restored, both mother and full shifted flag lose exactly three ranks:

\[
31\longrightarrow28.
\]

The kernel is the Galilean/Killing sector.  The intrinsic formation operator remains invariant under a constant frame shift,

\[
\boxed{\mathcal L_{\nu,u+c}=\mathcal L_{\nu,u},}
\]

while diagonal evaluation transforms by

\[
\boxed{
F(u+c)-F(u)=\mathcal L_{\nu,u}c.
}
\]

The corresponding audit residuals are at \(10^{-15}\)–\(10^{-16}\) scale.

## 7. Status of the word “equivalence”

The correct statement is **fiberwise equivalence of state/dynamics over a fixed canonical physical core**.  It is not a claim that one signature snapshot determines every possible abstract metric-Lie bracket.  That stronger claim is explicitly false; see [PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md](PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md).
