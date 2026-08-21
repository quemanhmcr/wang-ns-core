# Wang–Navier–Stokes Core

Repository này tập trung vào một structural description của smooth homogeneous incompressible Navier–Stokes thông qua **mother curl deformation** và **curl spectral-flag signature**.

Object trung tâm là

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

- [Core_signature.md](Core_signature.md) — narrative dài: từ terminal/C0 failures tới \(O_a\), rồi quay về complete mother \(E=[\nabla,C]\).
- [core/spectral_signature/README.md](core/spectral_signature/README.md) — cửa vào canonical theory.
- [core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md](core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md) — definition, reverse compiler, tomography, functional calculus, quotient và readers.
- [core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md](core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md) — adversarial completeness campaign và falsification record.
- [core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md](core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md) — structural completeness theorem và explicit decoder.
- [core/spectral_signature/HISTORY_AND_FALSIFICATION.md](core/spectral_signature/HISTORY_AND_FALSIFICATION.md) — các failure trực tiếp quyết định hình dạng cuối của theory.

NEO compiler/workbench được giữ riêng tại [core/NEO/](core/NEO/). Nó là phương pháp dẫn tới discovery, không phải subject chính của spectral-signature theory.

Lịch sử các proof programmes/worktrees trước whole-state signature nằm tại [history/README.md](history/README.md), đặc biệt [history/worktrees/README.md](history/worktrees/README.md).

## Reproduce canonical audits

```bash
python core/spectral_signature/audits/spectral_flag_signature.py
python core/spectral_signature/audits/spectral_flag_completeness.py
python core/spectral_signature/audits/mother_completeness_theorem.py
```

Ba audits này kiểm các identity và experiments canonical: reverse signature algebra, shifted tomography, quotient kernel, microlocal state recovery, Killing kernel, Sobolev/frame constants, gauge reconstruction và signature-image conjugacy.

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
  spectral_signature/
history/
  worktrees/
```

`core/spectral_signature/` là phần canonical quan trọng nhất của repository hiện tại.
