# Wang–Navier–Stokes Core

Repository này chứa ba structural cores liên kết nhau cho smooth homogeneous incompressible Navier–Stokes. `core/metric_lie_hodge/` mô tả formation law của chính phương trình; `core/spectral_signature/` mô tả whole-state encoding qua mother curl deformation và shifted spectral flags; `core/curved_formation_signature/` là core hợp nhất, mô tả spectral signature như một **curved representation geometry** của formation core. `core/NEO/` được giữ riêng như compiler/workbench discovery.

Trong spectral-signature core, object trung tâm là

\[
\boxed{
E_u=[\nabla_u,C],
\qquad C=\operatorname{curl},
}
\]

và family shifted spectral cuts

\[
\boxed{
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a],
\qquad
H_a=\operatorname{sgn}(C-aI).
}
\]

Cấu trúc canonical hiện tại là

\[
\boxed{
E=[\nabla,C]
\quad\longleftrightarrow\quad
\{\mathscr O_a\}_{a\in\mathbb R}
\quad\longrightarrow\quad
\mathscr O_0
\quad\longrightarrow\quad
J_0
\quad\longrightarrow\quad
W_0.
}
\]

Mũi tên đầu là equivalence qua spectral tomography. Các mũi tên sau là contractions/readers làm mất information.

## Metric–Lie / Hodge formation core

Core bổ sung tại [core/metric_lie_hodge/README.md](core/metric_lie_hodge/README.md) bắt đầu từ datum

\[
\boxed{
\mathcal C_{NS}
=
(\mathfrak g_\sigma,[\cdot,\cdot],\langle\cdot,\cdot\rangle_{L^2},C).
}
\]

Đặt

\[
\boxed{
\ell_{\nu,u}(a,b)
=-\langle u,[a,b]\rangle
-\nu\langle Ca,Cb\rangle.
}
\]

Nếu \(\mathcal L_{\nu,u}\) là Riesz operator của form này thì

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2,
\qquad
\partial_tu=\mathcal L_{\nu,u}u.
}
\]

Claim của core này là structural formation: projected Euler/geodesic/Lie–Poisson part và Stokes/Dirichlet part được sinh từ cùng oriented metric-Lie/Hodge datum.  Nó không thay thế spectral-signature completeness theorem và không phải regularity theorem.

## Core 3 — Curl-Spectral Differential Observability

Core thứ ba tại [core/curved_formation_signature/README.md](core/curved_formation_signature/README.md) đã trưởng thành thêm một cấp.

Ban đầu Core 3 chỉ trả lời:

> formation core sinh ra phương trình, còn spectral signature có thật sự mang cùng state/dynamics geometry hay chỉ là một bộ tọa độ hoàn chỉnh?

Câu trả lời đầu tiên là state-level equivalence trên fixed physical core.  Campaign tiếp theo nhìn ra curl spectral sheets và curvature split.  Campaign mới nhất hỏi câu mạnh hơn:

\[
\boxed{
(g_\Sigma,C,E,K)
\stackrel{?}{\Longrightarrow}
\nabla
\stackrel{?}{\Longrightarrow}
T,R,\mathcal J.
}
\]

Core 3 hiện phân biệt ba cấp completeness:

\[
\boxed{
\textbf{state completeness}
}
\]

\[
E_u=[\nabla_u,C]\Longleftrightarrow u
\]

trên smooth mean-zero periodic physical core, modulo Killing/Galilean symmetry;

\[
\boxed{
\textbf{differential spectral geometry}
}
\]

\[
C
\xrightarrow{d_\nabla}
E
\xrightarrow{d_\nabla}
K=[R,C]
\xrightarrow{d_\nabla}
R\wedge E
\to\cdots;
\]

và candidate mới:

\[
\boxed{
\textbf{formation-geometry completeness}
}
\]

ở generic spectral strata.

Trong curl spectral frame,

\[
\boxed{
\nabla=V+B,
\qquad
[V,C]=0,
\qquad
E=[B,C].
}
\]

Do đó degree one reconstruct cross-sheet connection \(B\).  Phần còn thiếu \(V\) quay bên trong cùng curl eigensheets.

Newest exact finite metric-Lie mechanism là

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V),
}
\]

với \(\mathcal A_{C,E}\) là một **Codazzi observability map** tuyến tính theo hidden within-sheet connection trong typed left-invariant torsion-free model.  Nếu map này injective modulo true stabilizer, thì

\[
\boxed{
(g,C,E,K)
\Longrightarrow
\nabla
\Longrightarrow
T,R,\mathcal J.
}
\]

Exact Lie tribunals cho full-rank reconstruction ở 16/16 generic cases, worst connection error \(3.97\times10^{-15}\), và independent 80-step trajectories match tới \(5.02\times10^{-16}\).

Quan trọng hơn, full physical helical tribunal cố tình chọn một same-signed-curl Fourier transition mà mother \(E\) **mù tuyệt đối**.  Cross-sheet curvature loop \(K\) recover hidden connection coefficient đó trên 80 resonant triads với median error

\[
\boxed{9.56\times10^{-16}}
\]

và noise slope \(1.0004\).

Nhưng campaign cũng falsify phiên bản quá mạnh.  Phase diagram 9 Lie families × 9 curl multiplicity patterns × 6 random metrics cho 68/72 non-scalar family/pattern combinations full rank ở mọi tested seed; persistent failures tập trung ở high-degeneracy pattern

\[
\boxed{5+1}.
\]

Ở hardest case, higher tower giảm linearized nullity

\[
\boxed{11\to9\to6},
\]

và maximal tower + Jacobi/Bianchi vẫn còn 5 first-order blind directions.  Nonlinear test cho chính 5 directions đó lại thấy

\[
\boxed{
\text{sensor residual}\sim t^2
}
\]

với fitted slopes \(2.0000000000\).  Tức Jacobian singular không đồng nghĩa finite non-uniqueness.

Do đó strongest current wording không phải “\(E+K\) always complete”, mà là:

\[
\boxed{
\textbf{Core 3 is a curl-spectral differential observability geometry for the formation core.}
}
\]

Generic tested spectral strata reconstruct formation geometry ở degree two; highly symmetric strata có thể cần higher/nonlinear data.

Viscosity \(\nu\) không nằm trong reversible geometry này.  Sau khi geometry được reconstruct, một generic time tangent đủ calibrate \(\nu\) trong finite tribunal.  Architecture hiện tại là

\[
\boxed{
\text{differential spectral geometry}+\nu
=\text{full formation law}.
}
\]

Đọc [GEOMETRIC_COMPLETENESS.md](core/curved_formation_signature/GEOMETRIC_COMPLETENESS.md) cho campaign mới nhất, [CURL_SPECTRAL_REDUCTION.md](core/curved_formation_signature/CURL_SPECTRAL_REDUCTION.md) cho spectral-sheet geometry, và [HISTORY_AND_FALSIFICATION.md](core/curved_formation_signature/HISTORY_AND_FALSIFICATION.md) cho toàn bộ các formulation đã bị experiments giết.

## Kết quả structural chính

Trên smooth mean-zero divergence-free fields trên \(\mathbb T^3\), principal symbol của mother là

\[
\boxed{
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(u)(x)\xi}{|\xi|^2}\,\xi\times b,
\qquad b\perp\xi,
}
\]

với

\[
S(u)=\frac12(\nabla u+\nabla u^T).
\]

Do đó mother/signature đọc trực tiếp quadratic strain form

\[
q_u(x,n)=n^TS(u)(x)n.
\]

Spherical inversion cho

\[
\boxed{
S(u)(x)
=\frac{15}{2}\fint_{S^2}q_u(x,n)n\otimes n\,dn,
}
\]

và incompressibility cho

\[
\boxed{
\Delta u=2\operatorname{div}S(u).
}
\]

Vì vậy

\[
\boxed{
\mathscr O
\longleftrightarrow
E
\longleftrightarrow
S
\longleftrightarrow
u/\operatorname{Kill}
\longrightarrow
F_{NS}(u).
}
\]

Ở đây `u/\operatorname{Kill}` nghĩa là velocity modulo Euclidean Killing symmetry trước normalization; trên mean-zero periodic class, state được xác định duy nhất.

Canonical Sobolev identity là

\[
\boxed{
\|u\|_{\dot H^{s+1}}^2
=15\int_{\mathbb T^3}\fint_{S^2}
|\Lambda_x^sq_u(x,n)|^2\,dn\,dx.
}
\]

Tức microlocal signature norm, sau universal normalization, chính là Sobolev norm của physical state.

## Đọc từ đâu

- [Core_signature.md](Core_signature.md) — narrative chung: Mục I giới thiệu formation core, Mục II giữ lịch sử spectral-signature, Mục III kể quá trình hai theory hợp nhất thành curved formation–signature geometry.
- [core/curved_formation_signature/README.md](core/curved_formation_signature/README.md) — cửa vào core hợp nhất và current structural claim.
- [core/curved_formation_signature/GEOMETRIC_COMPLETENESS.md](core/curved_formation_signature/GEOMETRIC_COMPLETENESS.md) — newest core result: state-vs-geometry completeness, Codazzi inverse map, generic rank, singular strata, nonlinear observability và viscosity calibration.
- [core/curved_formation_signature/FORMATION_SIGNATURE_EQUIVALENCE.md](core/curved_formation_signature/FORMATION_SIGNATURE_EQUIVALENCE.md) — forward/reverse bridge và dynamical conjugacy trên fixed physical core.
- [core/curved_formation_signature/CURL_SPECTRAL_REDUCTION.md](core/curved_formation_signature/CURL_SPECTRAL_REDUCTION.md) — curl isospectral orbit, spectral-sheet splitting, Gauss–Codazzi–Ricci và Cartan/Bianchi geometry.
- [core/curved_formation_signature/DEEP_GEOMETRY_LESSONS.md](core/curved_formation_signature/DEEP_GEOMETRY_LESSONS.md) — falsifications, topology/boundary typing, BCH distinction, harmless controls và kinh nghiệm tránh overclaim.
- [core/curved_formation_signature/CURVED_CURL_MODULE.md](core/curved_formation_signature/CURVED_CURL_MODULE.md) — curvature-corrected bracket, holonomy, Bianchi tower và shifted-cut curvature tomography.
- [core/curved_formation_signature/SIGNATURE_METRIC_DYNAMICS.md](core/curved_formation_signature/SIGNATURE_METRIC_DYNAMICS.md) — exact metric/heat bridge giữa formation và signature geometry.
- [core/metric_lie_hodge/README.md](core/metric_lie_hodge/README.md) — cửa vào formation theory: metric Lie tensor, Riesz operator pencil, domain/topology typing và Euler–heat descendant algebra.
- [core/metric_lie_hodge/FORMATION_LAW.md](core/metric_lie_hodge/FORMATION_LAW.md) — exact formation identities và công thức \(u_t=\mathcal L_{\nu,u}u\).
- [core/metric_lie_hodge/COMPATIBILITY_GEOMETRY.md](core/metric_lie_hodge/COMPATIBILITY_GEOMETRY.md) — relation giữa material/Poisson mothers, pressure/common mode và BCH compatibility.
- [core/spectral_signature/README.md](core/spectral_signature/README.md) — cửa vào whole-state spectral-signature theory.
- [core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md](core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md) — definition, reverse compiler, tomography, functional calculus, quotient và readers.
- [core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md](core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md) — adversarial completeness campaign và falsification record.
- [core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md](core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md) — structural completeness theorem và explicit decoder.
- [core/spectral_signature/HISTORY_AND_FALSIFICATION.md](core/spectral_signature/HISTORY_AND_FALSIFICATION.md) — các failure trực tiếp quyết định hình dạng cuối của theory.

NEO compiler/workbench được giữ riêng tại [core/NEO/](core/NEO/). Nó là phương pháp dẫn tới discovery, không phải subject chính của spectral-signature theory.

Lịch sử các proof programmes/worktrees trước whole-state signature nằm tại [history/README.md](history/README.md), đặc biệt [history/worktrees/README.md](history/worktrees/README.md).

## Reproduce canonical audits

Metric–Lie/Hodge formation core:

```bash
python core/metric_lie_hodge/audits/formation_core_audit.py
python core/metric_lie_hodge/audits/bch_core_audit.py
python core/metric_lie_hodge/audits/domain_topology_audit.py
```

Spectral-signature core:

```bash
python core/spectral_signature/audits/spectral_flag_signature.py
python core/spectral_signature/audits/spectral_flag_completeness.py
python core/spectral_signature/audits/mother_completeness_theorem.py
```

Curved Formation–Signature core:

```bash
python core/curved_formation_signature/audits/metric_lie_spectral_unification.py
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_core_identifiability.py
python core/curved_formation_signature/audits/physical_axiom_rigidity.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/galerkin_probe_lie_failure.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/physical_curvature_flag_tomography.py
python core/curved_formation_signature/audits/curl_solder_cartan_structure.py
python core/curved_formation_signature/audits/curl_orbit_stabilizer.py
python core/curved_formation_signature/audits/spectral_gauss_codazzi_ricci.py
python core/curved_formation_signature/audits/full_physical_gauss_codazzi.py
python core/curved_formation_signature/audits/connection_lift_curvature_recovery.py
python core/curved_formation_signature/audits/full_physical_vertical_curvature.py
python core/curved_formation_signature/audits/full_physical_vertical_degree4.py
python core/curved_formation_signature/audits/blind_reversible_irreversible_split.py
python core/curved_formation_signature/audits/orientation_double_cover.py
python core/curved_formation_signature/audits/bch_vs_geometric_curvature.py
python core/curved_formation_signature/audits/harmless_class_curvature.py
python core/curved_formation_signature/audits/harmonic_zero_mode_signature.py
python core/curved_formation_signature/audits/boundary_metric_typing.py
python core/curved_formation_signature/audits/representation_curvature_not_embedding_curvature.py
python core/curved_formation_signature/audits/ek_exact_lie_reconstruction.py
python core/curved_formation_signature/audits/physical_helical_resonant_recovery.py
python core/curved_formation_signature/audits/ek_rank_phase_diagram.py
python core/curved_formation_signature/audits/ek_higher_degree_completion.py
python core/curved_formation_signature/audits/ek_maximal_tower_stabilizer.py
python core/curved_formation_signature/audits/ek_bianchi_integrability_completion.py
python core/curved_formation_signature/audits/ek_cartan_integrability_closure.py
python core/curved_formation_signature/audits/ek_nonlinear_singular_observability.py
python core/curved_formation_signature/audits/ek_metric_covariant_reconstruction.py
python core/curved_formation_signature/audits/ek_28d_sparse_codazzi_recovery.py
python core/curved_formation_signature/audits/ek_heldout_spectral_prediction.py
python core/curved_formation_signature/audits/ek_minimal_viscosity_calibration.py
```

Ba audit suites phục vụ ba tầng claim khác nhau: formation/core geometry ở `metric_lie_hodge`, whole-state signature/completeness ở `spectral_signature`, và curl-spectral reduction / transported formation geometry ở `curved_formation_signature`.  Deep suite cố ý giữ cả negative controls: harmless curvature, topology zero-mode, boundary typing, BCH-vs-curvature và flat-image-vs-curved-connection.

## Scope

Repository hiện có hai theorem-level parent structures và một canonical synthesis core. Spectral-signature state completeness được theoremize trên smooth mean-zero periodic state space; formation identities là exact trên typed periodic setting. Core thứ ba hiện được sharpen thành **curl-spectral differential observability of formation geometry**: nó có một exact conditional Codazzi reconstruction mechanism và rất mạnh executable evidence cho generic formation-geometry completeness, nhưng continuum injectivity/singular-strata theorem vẫn open.

Nó **không** tự động chứng minh:

- global regularity của 3D Navier–Stokes;
- nonexistence của finite-time singularity;
- a priori boundedness của critical signature norm;
- arbitrary weak-solution, boundary, forcing hoặc variable-coefficient extensions.

Thông điệp structural là:

\[
\boxed{
\text{the full physical NS state is encoded by the mother/spectral-flag signature,}
}
\]

không phải:

\[
\boxed{
\text{the regularity problem is solved.}
}
\]

## Repository layout

```text
README.md
Core_signature.md
core/
  NEO/
  metric_lie_hodge/
  spectral_signature/
  curved_formation_signature/
history/
  worktrees/
```

`core/metric_lie_hodge/` và `core/spectral_signature/` là hai parent cores: một bên equation formation, một bên whole-state coordinate/completeness. `core/curved_formation_signature/` là canonical synthesis core hiện mô tả **curl-spectral differential observability** của formation geometry: state completeness, spectral soldering, Gauss/Codazzi/Ricci split, Codazzi reconstruction of hidden connection, singular spectral strata, Bianchi/higher-degree completion và signature-side dynamics. `core/NEO/` vẫn là methodology/workbench.
