# Clay-problem applications

Thư mục này chứa các proof programmes dùng Wang--NS Core để nghiên cứu bài toán Clay. Tài liệu ở đây **không tự động là proof của Clay problem**; theorem-status luôn phải tách rõ.

## Navier--Stokes

### Theory-2 interaction frame / finite-density causal similarity architecture

[theory2_interaction_frame/](theory2_interaction_frame/) là canonical architecture rộng nhất cho finite-shell-density branch. Nó bắt đầu trực tiếp từ

\[
\Sigma(u)\longleftrightarrow E_u\longleftrightarrow u
\]

và anchored interaction frame

\[
v_t=-\nu(C^\sharp)^2v,
\qquad
C^\sharp_t=U^*E_uU.
\]

Bản hiện tại phân biệt rõ `E=[Gamma,C]` với critical operator `F=[Gamma,|C|]`, dùng full bipolar flag family để đọc radial transport, và retype finite-density programme thành

\[
\boxed{
\text{historical leading-edge barrier}
\to
\text{complete causal Type-I ray}
\to
\text{backward-similar open core + IR boundary}
\to
\text{self-generated convolutional recurrent mixer}.
}
\]

Frontier mới nhất thêm một coercive Track-B subproblem trong **causal-node frame**: với

\[
W=P_+V,
\qquad
z=P_-V,
\qquad
S=P_-\Gamma_WW,
\]

exact source/catalyst recycling kết hợp với historical Gaussian UV edge được dùng để target một finite-order complete time-jet estimate. Conditional on that jet theorem and the work-local profile lift, Landau--Kolmogorov interpolation excludes the sharp catalytic asymptotic

\[
A/\nu\to\infty,
\qquad
\delta/\nu=O(1).
\]

This does **not** assert comparable helicity masses and does not close the fully mixed broadband branch. It is recorded in [`06_FINITE_STEP_RECYCLING_AND_CATALYST_RIGIDITY.md`](theory2_interaction_frame/06_FINITE_STEP_RECYCLING_AND_CATALYST_RIGIDITY.md).

Global critical compactness không được giả định; old generations được giữ như một complete outgoing IR boundary defect. Folder này **không claim regularity**.

### Theory-2 transverse Floquet endgame

[theory2_transverse_floquet_endgame/](theory2_transverse_floquet_endgame/) là specialized downstream dossier cho normalized stationary/periodic finite-Reynolds branches. Nó chứa các exact transverse normal forms, common-ray Poisson-depth identities/coercivity, terminal scaling, transverse saturation, companion nonconcentration, và anti-repacking criteria.

Các theorem trong dossier này vẫn canonical khi hypotheses stationary/Floquet tương ứng đã được đạt tới. Chúng không thay thế causal compactness/IR-boundary layer ở `theory2_interaction_frame`, vì một hypothetical finite-density enemy có thể là một open recurrent core chứ không phải fixed point hay exact cycle.

### Theory-2 realtime endgame

[theory2_realtime_endgame/](theory2_realtime_endgame/) giữ provenance của late-stage realtime reduction và các historical branches đã được compile/falsify. Dùng nó để hiểu nguồn gốc theorem, không để override canonical state/frontier trong hai folders trên.
