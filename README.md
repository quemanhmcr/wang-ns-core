# Wang–Navier–Stokes Core

Repository này chứa các structural cores bổ sung nhau cho smooth homogeneous incompressible Navier–Stokes.  `core/spectral_signature/` mô tả whole-state encoding qua mother curl deformation và shifted spectral flags; `core/metric_lie_hodge/` mô tả formation law của chính phương trình từ metric-Lie/Hodge data.  `core/NEO/` được giữ riêng như compiler/workbench discovery.

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

- [Core_signature.md](Core_signature.md) — entry narrative chung; Mục I mới tóm tắt metric–Lie/Hodge formation core, Mục II cũ giữ nguyên lịch sử spectral-signature.
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

Hai audit suites phục vụ hai claim khác nhau: formation/core geometry ở `metric_lie_hodge`, và whole-state signature/completeness ở `spectral_signature`.

## Scope

Current structural theorem là một **completeness / coordinate theorem** cho smooth homogeneous incompressible Navier–Stokes, đặc biệt được theoremize sạch trên smooth mean-zero periodic state space.

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
history/
  worktrees/
```

`core/spectral_signature/` và `core/metric_lie_hodge/` là hai canonical theory folders với nhiệm vụ khác nhau: một bên whole-state coordinate/completeness, một bên equation formation/core geometry.  `core/NEO/` vẫn là methodology/workbench.
