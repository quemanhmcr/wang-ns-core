# 02 — Complete reduction chain

Tài liệu này ghi reduction chain cần được coi như “proof map”.  New chat không được bắt đầu lại từ đầu.

## 1. Complete spectral state

Core object:

\[
E_u=[\nabla_u,C],
\qquad
H_a=\operatorname{sgn}(C-aI),
\]

\[
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a].
\]

Mother completeness cho equivalence/tomography giữa `E` và full shifted signature ở typed smooth setting.

## 2. Hard torsion is a contraction, not a new species

\[
J_a=\frac14 T_{H_a}(u,u)=\frac14\mathscr O_a(u)u,
\]

và

\[
W(a)=4\langle |C-a|u,J_a\rangle.
\]

Hierarchy:

\[
\mathscr O_a\to J_a\to W(a)
\]

mỗi mũi tên sau là information-losing contraction.

## 3. Moving flag recovers the historical missing half derivative

Một hard edge có

\[
p+m=q,
\qquad
P=|p|,\ M=|m|,\ Q=|q|,
\qquad
\kappa=P^2+M^2.
\]

Shifted selector support length

\[
d_e=Q+\min(P,M),
\]

và

\[
\frac1{\sqrt2}\sqrt\kappa
\le d_e\le
\frac3{\sqrt2}\sqrt\kappa.
\]

Do đó

\[
\frac1{\sqrt2}G_{-1/2}
\le
\int_{\mathbb R}G_{-1}^{\rm flag}(a)\,da
\le
\frac3{\sqrt2}G_{-1/2}.
\]

Kết luận: half derivative không thiếu khỏi geometry; zero-cut reader đã bỏ parent-side sweep.

## 4. Static reciprocal seam is closed

Reciprocal Lemma A:

\[
\boxed{
\frac{Q\,\chi_{\rm geom}^2}{|p-p'|}
\ge\frac{\sqrt6}{8}.
}
\]

Lemma B:

\[
\boxed{
\#\{\text{nondegenerate reciprocal preimages of one canonical role}\}\le2.
}
\]

Điều này đóng aligned static multiplicity seam, nhưng **không** tạo finite time-rate owner.

## 5. Equal-heat kernel and heat calibration

Equal-heat collision equation giữ kernel

\[
\eta(k)=\alpha+\beta\cdot k+\gamma|k|^2.
\]

Physical rate

\[
r_k=\eta_k-\nu|k|^2
\]

loại quadratic heat mode.  Nếu same-output rates synchronize trên connected non-null continuum domain,

\[
\delta_\Diamond r=0
\]

thì

\[
\boxed{r(k)=\sigma+b\cdot k.}
\]

Reality giảm `b` về translation phase direction; terminal state chỉ amplitude/translation/monochromatic-safe class.

## 6. Scalar polar cross-term route is exhausted

Critical stock `\mathcal U` và work `W` thỏa

\[
\mathcal U'=W.
\]

Tại Codazzi hinge,

\[
W'=\langle\Lambda u,Z_{\rm Cod}\rangle+\mathcal C_{\rm compat}.
\]

Do đó

\[
\boxed{
\mathcal U\langle\Lambda u,Z_{\rm Cod}\rangle
=(\mathcal U W)'-W^2-\mathcal U\mathcal C_{\rm compat}.
}
\]

Nếu `F(\mathcal U,W)` phải absorb Codazzi qua `W'`, coefficient matching ép

\[
\partial_WF=\mathcal U
\Rightarrow
F=\mathcal U W+\phi(\mathcal U).
\]

Và `F'` sinh đúng `+W^2`, triệt good square.  Vì vậy không còn scalar local hypocoercive cross term nào trong `(\mathcal U,W)` để tìm.

## 7. All-three-roots UV excision

Mọi fixed smooth/low-frequency background có finite action.  Endpoint divergence buộc

\[
\int_0^{T_*}\|P_{>L}J_{\rm flip}(P_{>L}u)\|_2^2dt=\infty
\]

cho mọi finite `L`.

Tức final defect là genuinely all-UV.

## 8. Comparable/deep scale split

Positive heterochiral critical creation obeys exact triad majorant

\[
\boxed{P_{\rm crit}^+\le V_\rho.}
\]

Trên dangerous far-UV arch có equality.  Radial traffic có deep-separation gain `(L/K)^2`, nên arbitrarily deep low--high--high separation không phải free endpoint mechanism.

Còn lại là normalized comparable-scale active packets hoặc degeneration vào null geometry.

## 9. Fixed-window incidence richness

Trên normalized compact annulus `\Omega`, quadratic convolution cho

\[
\|J_{\rm flip}\|_2
\le C_\Omega
|\operatorname{supp}\widehat u|^{1/2}\|u\|_2^2.
\]

Nontrivial resultant => positive effective Fourier volume.

Positive-volume amplitude stratum `A` tạo same-output diamonds bởi additive energy:

\[
F=1_A*1_A,
\qquad
\int|F|^2
\ge\frac{|A|^4}{|\Omega+\Omega|}.
\]

Away khỏi shear/Beltrami source-null algebraic sets, compactness cho quantitative non-null incidence.

## 10. Final primitive

True edge source:

\[
f_e=C_ea_pa_m,
\qquad
h_e=\dot f_e.
\]

Projective defect:

\[
\Omega_{e,e'}=f_{e'}h_e-f_eh_{e'}.
\]

Division-free identity:

\[
\boxed{
\Omega_{e,e'}
=f_{e'}g_e-f_eg_{e'}
-\nu(\kappa_e-\kappa_{e'})f_ef_{e'}.
}
\]

Đây là cánh cửa cuối: dynamic control hoặc terminal rigidity cho **cùng object này**.
