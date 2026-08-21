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

## Curved Formation–Signature core

Core hợp nhất tại [core/curved_formation_signature/README.md](core/curved_formation_signature/README.md) trả lời câu hỏi xuất hiện sau khi hai theory trên đã trưởng thành: **formation core sinh ra phương trình, còn spectral signature chỉ là tọa độ hoàn chỉnh hay thật sự mang geometry của formation core?**

Kết quả canonical đã được sharpen sau campaign thứ hai.  Không chỉ có

\[
\boxed{
E=d_\nabla C,
\qquad
E_u=[\nabla_u,C],
}
\]

và

\[
\boxed{
d_\nabla E=d_\nabla^2C=[R,C].
}
\]

Curl còn tạo một **spectral reduction** của formation connection.  Trong curl spectral frame,

\[
\boxed{
\nabla=V+B,
\qquad
[V,C]=0,
\qquad
E=[B,C].
}
\]

Nói cách khác, \(V\) quay bên trong cùng curl eigensheet, còn \(B\) trộn giữa các eigensheets; mother \(E\) đo chính sheet-mixing part này, weighted bởi spectral gaps.

Formation curvature cũng tách

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0,
\]

với within-sheet Gauss/Ricci sector

\[
R_\parallel=[V,V]+\Pi_\parallel[B,B]
\]

và cross-sheet Codazzi sector \(R_\perp\).  Curvature mother chỉ thấy cross-sheet part:

\[
\boxed{
K=[R,C]=[R_\perp,C].
}
\]

Higher Bianchi levels couple hidden within-sheet curvature trở lại các sensor đã thấy:

\[
\boxed{
d_\nabla K=R\wedge E,
\qquad
d_\nabla R=0.
}
\]

Shifted spectral cuts vẫn tomograph curvature action:

\[
\boxed{
\frac12\int [R,H_a]\,da=[R,C].
}
\]

Metric bridge giữ nguyên exact trên strain signature \(q_u(x,n)=n^TS(u)(x)n\):

\[
\boxed{
L^2_u\longleftrightarrow15\,\dot H^{-1}_q,
\qquad
\|Cu\|_2^2\longleftrightarrow15\,L^2_q.
}
\]

Strongest current wording là:

\[
\boxed{
\textbf{Navier–Stokes formation geometry admits a canonical curl-spectral reduction.}
}
\]

“Curved representation” ở đây nghĩa là signature coordinates mang transported formation connection/curvature; **signature image tự nó vẫn là một linear flat state image**.  \([R,C]\) cũng không phải blow-up amplitude: 2D, Beltrami và shear controls đều có thể có nonzero ambient curvature.  `comm(C)` chỉ là first-order stabilizer, không phải final gauge; và \(\ker C\) không được đồng nhất với gauge trên topology không tầm thường.

Hai notes quan trọng nhất của update này:

- [CURL_SPECTRAL_REDUCTION.md](core/curved_formation_signature/CURL_SPECTRAL_REDUCTION.md) — isospectral orbit, stabilizer splitting, spectral sheets, Gauss–Codazzi–Ricci và Cartan/Bianchi structure.
- [DEEP_GEOMETRY_LESSONS.md](core/curved_formation_signature/DEEP_GEOMETRY_LESSONS.md) — falsifications, topology/boundary lessons, BCH distinction, harmless classes và các scope corrections.

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
```

Ba audit suites phục vụ ba tầng claim khác nhau: formation/core geometry ở `metric_lie_hodge`, whole-state signature/completeness ở `spectral_signature`, và curl-spectral reduction / transported formation geometry ở `curved_formation_signature`.  Deep suite cố ý giữ cả negative controls: harmless curvature, topology zero-mode, boundary typing, BCH-vs-curvature và flat-image-vs-curved-connection.

## Scope

Repository hiện có hai theorem-level parent structures và một canonical synthesis core. Spectral-signature completeness được theoremize sạch trên smooth mean-zero periodic state space; formation identities là exact trên typed periodic setting; core thứ ba hiện được sharpen thành **curl-spectral reduction of formation geometry**, tổ chức exact connection/curvature identities cùng full-physical adversarial tribunals mà không overclaim thành regularity theorem.

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

`core/metric_lie_hodge/` và `core/spectral_signature/` là hai parent cores: một bên equation formation, một bên whole-state coordinate/completeness. `core/curved_formation_signature/` là canonical synthesis core mô tả **curl-spectral reduction** của formation geometry: spectral soldering, Gauss/Codazzi/Ricci curvature split, Bianchi coupling và signature-side dynamics. `core/NEO/` vẫn là methodology/workbench.
