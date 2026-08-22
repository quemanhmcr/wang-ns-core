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

## Late Theory-2 frontier note

Một note mới tại [core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md](core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md) ghi lại late endpoint reconstruction với theorem-status tách rõ:

- complete moving flag cung cấp đúng half heat derivative mà historical heat-fiber estimate còn thiếu;
- reciprocal Lemma A có exact rational certificate cho \(Q\chi_{\rm geom}^2/|p-p'|\ge\sqrt6/8\);
- reciprocal Lemma B cho finite multiplicity \(\le2\) trên mỗi canonical companion role;
- equal-heat collision geometry để lại đúng heat invariant \(|k|^2\) bên cạnh amplitude/translation modes;
- final target được sharpen thành một **hypocoercive Polar--Korn coupling** giữa A+B reciprocal conductance/finite-incidence geometry và \(-\nu C^2\) heat-normal direction.

Các update này **không** tuyên bố global 3D regularity.  Modified-energy/hypocoercive inequality cần để biến exact visibility square thành finite action vẫn là open theorem target.


## Clay application handoff

Application-level Navier--Stokes endgame notes now live at
[application/clay_problem/theory2_realtime_endgame/](application/clay_problem/theory2_realtime_endgame/).

Hướng blow-up theorem-first mới được đặt tại [application/clay_problem/theory2_interaction_frame/](application/clay_problem/theory2_interaction_frame/): Mother/full flag vẫn là complete state; frontier finite-density hiện được retype thành three-scale UV locality, complete-core compactness và bài toán loại trừ persistent self-generated critical drift.
The handoff records the Theory-2 realtime anti-loop doctrine, exact reduction
chain, formula compendium, and the single remaining **open** Dynamic
Rich-Packet Polar--Korn theorem.  It is deliberately explicit that structural
finality of the reduction is not a claim of solved global regularity.

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

## Core 3 — Curl-Spectral Differential Observability and Presentation Bootstrap

Core thứ ba tại [core/curved_formation_signature/README.md](core/curved_formation_signature/README.md) hiện có bốn tầng rõ ràng.

\[
\boxed{
\text{state completeness}
\to
\text{differential spectral geometry}
\to
\text{formation-geometry observability}
\to
\text{presentation bootstrap}.
}
\]

Ba tầng đầu giữ nguyên architecture của Campaign III.  Trong curl spectral frame,

\[
\nabla=V+B,
\qquad
[V,C]=0,
\qquad
E=[B,C],
\]

và curvature mother cho Codazzi measurement

\[
K=K_B+\mathcal A_{C,E}(V).
\]

Ở generic tested finite strata, polarized data \((g,C,E,K)\) reconstruct formation connection; high-degeneracy strata giữ nguyên các singular/higher-order caveats đã canonical hóa.

Campaign IV hỏi một câu khác: **một generic state snapshot tự nó biết gì về law-space mà nó thuộc vào?**

Fix một generic state \(u_*\) và chỉ lấy hai operator letters

\[
\boxed{C,\qquad E_{u_*}=[\nabla_{u_*},C].}
\]

Trong canonical 28D physical spectral lab,

\[
\dim\operatorname{Alg}(C)=6,
\qquad
\boxed{\dim\operatorname{Alg}(C,E_{u_*})=784=28^2}.
\]

Word-span growth là

\[
\boxed{1,3,7,15,31,63,125,246,483,784},
\]

và full matrix-algebra saturation xảy ra đúng ở depth \(9\), là information-theoretic lower bound cho hai generators.

Nhưng phần mới quan trọng hơn full algebra là **relations**.  Trong base spectral window, ba state-independent laws

\[
\boxed{
p(C)=0,
\qquad
Dp_C(E)=0,
\qquad
Q(C,E)=0
}
\]

với

\[
p(x)=(x^2-1)(x^2-2)(x^2-3),
\]

và

\[
Q(C,E)
=(C^2-I)(C^2E+EC^2-5E)(C^2-I)
\]

sinh **toàn bộ numerical word-relation space** tới degree \(8\):

\[
2=2,
\qquad
9=9,
\qquad
28=28.
\]

Relation space học từ một generic mother transfer sang 80 unseen physical states với minimum principal cosine

\[
\boxed{0.9999999999999991}.
\]

Same-spectrum rival-law controls không share physical quotient relation.  Relation-only classifier phân biệt đúng cả ba physical same-count rivals và một eight-law stress family.

Điều này cũng sống trong exact helical action, không chỉ projected finite bracket.  Một generic state chỉ support trên ba Fourier directions

\[
(0,0,1),
\qquad
(0,1,-1),
\qquad
(1,-1,-1)
\]

recover toàn root-level interaction category trong mười exact helical windows từ \(52\) tới \(512\) nodes.  Ở window lớn nhất, cùng ba directions reveal

\[
432\text{ active channels}
\quad\text{và}\quad
324\text{ forbidden channels}.
\]

Các finite-window interaction laws còn projectively consistent khi scale tăng: restriction về old curl roots không thêm hay mất một old transition nào trong các refinement tests.

Nhưng Campaign IV cũng falsify câu quá mạnh:

\[
(C,E_u)
\not\Longrightarrow
\text{full polarized formation geometry}.
\]

Hai metric-compatible connection one-forms khác nhau có thể share cùng training

\[
(C,E_{u_*},\nabla_{u_*})
\]

tới machine precision và cùng presentation category, nhưng khác mạnh trên unseen directions.

Một generic scalar curvature polarization lại recover được hidden geometry parameter trong 80/80 trials, với noise slope \(0.995\).

Vì vậy architecture canonical mới là

\[
\boxed{
\text{snapshot}\Rightarrow\text{syntax / interaction category},
}
\]

\[
\boxed{
\text{polarized }E,K\Rightarrow\text{formation geometry},
}
\]

\[
\boxed{
\nu\Rightarrow\text{dissipative calibration}.
}
\]

Strongest current candidate name cho Campaign IV là

\[
\boxed{
\textbf{Curl--Mother Presentation Bootstrap}.
}
\]

Đọc [PRESENTATION_BOOTSTRAP.md](core/curved_formation_signature/PRESENTATION_BOOTSTRAP.md) cho campaign mới nhất, [GEOMETRIC_COMPLETENESS.md](core/curved_formation_signature/GEOMETRIC_COMPLETENESS.md) cho Campaign III, và [HISTORY_AND_FALSIFICATION.md](core/curved_formation_signature/HISTORY_AND_FALSIFICATION.md) cho toàn bộ các formulation đã bị experiments giết.

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
