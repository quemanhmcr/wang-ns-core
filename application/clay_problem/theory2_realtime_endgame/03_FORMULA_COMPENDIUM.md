# 03 — Formula compendium

Đây là cheat sheet để new chat không phải săn công thức qua history.

## A. Curl / flag primitives

\[
C=\operatorname{curl},
\qquad
H=\operatorname{sgn}C,
\qquad
\Lambda=|C|,
\qquad
C=H\Lambda.
\]

\[
E_u=[\nabla_u,C].
\]

\[
H_a=\operatorname{sgn}(C-aI),
\qquad
\mathscr O_a(v)=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a].
\]

\[
J_a=\frac14\mathscr O_a(u)u.
\]

## B. First polar decomposition

\[
A_u=[\nabla_u,H],
\qquad
L_u=[\nabla_u,\Lambda],
\]

\[
\boxed{E_u=A_u\Lambda+HL_u.}
\]

Cross-helicity spectral slot `x=a>0`, `y=-b<0`:

\[
A_{xy}=\frac{2E_{xy}}{a+b},
\qquad
L_{xy}=\frac{a-b}{a+b}E_{xy},
\]

\[
\boxed{|E_{xy}|^2=|L_{xy}|^2+ab|A_{xy}|^2.}
\]

## C. Critical work / hard torsion

\[
J_{\rm flip}=\frac14T_H(u,u),
\]

\[
\boxed{W_\Lambda=4\langle\Lambda u,J_{\rm flip}\rangle.}
\]

Native PDE:

\[
(\partial_t+\nu\Lambda^2)J_{\rm flip}=S_J,
\]

\[
S_J=Y_{\rm flip}-2\nu\sum_jJ_{\rm flip}(\partial_ju).
\]

## D. Variational Leibniz defect

\[
R_\Lambda
=\Lambda N-P(\Lambda u\times\omega)-\operatorname{curl}(u\times\Lambda u).
\]

\[
\boxed{
R_\Lambda
=2\Lambda J_{\rm flip}
+2[DJ_{\rm flip}[u]]^*\Lambda u.
}
\]

## E. Moving flag half derivative

\[
d_e=Q+\min(P,M),
\]

\[
\frac1{\sqrt2}\sqrt\kappa\le d_e\le\frac3{\sqrt2}\sqrt\kappa.
\]

\[
\boxed{
\int G_{-1}^{\rm flag}(a)da\asymp G_{-1/2}.
}
\]

## F. Reciprocal geometry

\[
\boxed{
\frac{Q\chi_{\rm geom}^2}{|p-p'|}\ge\frac{\sqrt6}{8}.
}
\]

Canonical reciprocal multiplicity:

\[
\boxed{\#\text{preimages}\le2.}
\]

## G. Parabolic rate

For active Fourier coefficient:

\[
\eta_k=\frac{N_k}{a_k},
\qquad
\boxed{r_k=\frac{\dot a_k}{a_k}=\eta_k-\nu|k|^2.}
\]

Same-output defect:

\[
\boxed{
\delta_\Diamond r
=r_p+r_m-r_{p'}-r_{m'}.
}
\]

Zero kernel:

\[
\delta_\Diamond r=0
\Rightarrow
\boxed{r(k)=\sigma+b\cdot k.}
\]

## H. Division-free source geometry

\[
f_e=C_ea_pa_m,
\qquad
(\partial_t+\nu\kappa_e)f_e=g_e.
\]

\[
h_e:=\dot f_e=g_e-\nu\kappa_ef_e.
\]

\[
\Sigma_{e,e'}=f_{e'}h_e+f_eh_{e'}=\partial_t(f_ef_{e'}),
\]

\[
\Omega_{e,e'}=f_{e'}h_e-f_eh_{e'}.
\]

\[
\boxed{
\Omega_{e,e'}
=f_{e'}g_e-f_eg_{e'}
-\nu(\kappa_e-\kappa_{e'})f_ef_{e'}.
}
\]

Pythagoras:

\[
|\Sigma|^2+|\Omega|^2
=2(|f_{e'}h_e|^2+|f_eh_{e'}|^2).
\]

## I. Projective Fisher identity

\[
\mathcal P(f,h)
=\|f\|^2\|h\|^2-|\langle f,h\rangle|^2
=\frac12\iint|f_eh_{e'}-h_ef_{e'}|^2.
\]

Với `d\mu=|f|^2/\|f\|^2` và `h=\lambda f`:

\[
\boxed{
\frac{\mathcal P(f,h)}{\|f\|^4}
=\operatorname{Var}_\mu(\lambda).
}
\]

Heat-normal identity:

\[
\boxed{
\dot{\bar\kappa}
+2\nu\operatorname{Var}_\mu(\kappa)
=2\operatorname{Re}\operatorname{Cov}_\mu(\kappa,\eta).
}
\]

## J. Radial/polar scalar no-go

\[
\mathcal U'=W,
\qquad
W'=\langle\Lambda u,Z_{\rm Cod}\rangle+\mathcal C_{\rm compat}.
\]

\[
\boxed{
\mathcal U\langle\Lambda u,Z_{\rm Cod}\rangle
=(\mathcal UW)'-W^2-\mathcal U\mathcal C_{\rm compat}.
}
\]

## K. Normalized endpoint equations

Whole-space amplitude/dilation normalization:

\[
A=\sqrt{K(u)},
\qquad
\rho=\frac{K(u)}{E(u)},
\qquad
u=A S_\rho v,
\]

\[
\|v\|_2^2=\|\Lambda^{1/2}v\|_2^2=1,
\qquad
\varepsilon=\frac\nu A.
\]

Define

\[
D=W-\varepsilon M_3.
\]

Then

\[
\boxed{(\log A)_\tau=D,}
\qquad
\boxed{\varepsilon_\tau=-\varepsilon D.}
\]

Hypothetical unbounded critical amplification requires

\[
\boxed{\int D\,d\tau=+\infty.}
\]

## L. Positive critical triad vs radial traffic

For heterochiral positive critical creation,

\[
\boxed{P_{\rm crit}^+\le V_\rho.}
\]

On the dangerous far-UV low-donor arch equality holds.

Deep-separated blocks inherit the radial `(L/K)^2` gain; therefore the final hard packet must be comparable-scale after normalization or degenerate to a null geometry.
