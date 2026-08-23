# Clay-problem applications

Thư mục này chứa các proof programmes dùng Wang--NS Core để nghiên cứu bài toán Clay.  Tài liệu ở đây **không tự động là proof của Clay problem**; chúng là application contracts với theorem-status tách rõ.

## Navier--Stokes

### Theory-2 transverse Floquet endgame

[theory2_transverse_floquet_endgame/](theory2_transverse_floquet_endgame/) là dossier theorem-first mới nhất, ghi lại toàn bộ chain từ complete Theory-2 state, Poisson/heat Formation cocycles, constrained-gradient geometry, physical companion/rank-one completion, mixed curvature, bounded-module coercivity, terminal critical-Reynolds scaling, tới normalized finite-viscosity **transverse Floquet fixed-point frontier**.

Frontier hiện tại được cô lập thành

\[
F=\mathbb M_0[F]F+\mathbb G_T[F],
\]

trong đó `\mathbb M_0` là explicit weighted critical log-frequency translation của toàn bộ nontransverse dynamics, còn `\mathbb G_T` là one-cycle propagated transverse Formation source. Folder giữ ledger `EXACT / DEDUCTION / AUDIT / OPEN` và **không claim Clay solved**.

### Theory-2 realtime endgame

[theory2_realtime_endgame/](theory2_realtime_endgame/) ghi lại toàn bộ late-stage reduction từ complete spectral signature tới cánh cửa analytic cuối cùng.

Mục tiêu của handoff này là để một phiên làm việc mới có thể tiếp tục ngay tại frontier thật, không phải tái phát minh traffic/Codazzi/companion/next-mother criteria đã được compile và falsify trong history.

### Theory-2 interaction frame / moving heat geometry

[theory2_interaction_frame/](theory2_interaction_frame/) là spine theorem-first mới cho blow-up application.  Nó bắt đầu trực tiếp từ Mother/Flag Completeness và dùng một anchored unitary material frame để viết NS như heat trên một curl geometry chuyển động,

\[
v_t=-\nu(C^\sharp)^2v,
\qquad
C^\sharp_t=U^*E_uU.
\]

Folder này giữ \(u\leftrightarrow E_u\leftrightarrow\Sigma(u)\) làm complete state, coi interaction frame là coordinate có gauge được giữ rõ ràng, và hiện retype finite-density frontier thành three-scale UV locality, complete-core compactness và no persistent self-generated critical drift; shell current vẫn chỉ là reader, không phải ontology mới.
