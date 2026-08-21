# Core Signature

## I. Metric–Lie / Hodge formation core

Core canonical mới tại [core/metric_lie_hodge/README.md](core/metric_lie_hodge/README.md) xuất phát từ một câu hỏi khác với terminal/reader programmes: **cái gì sinh ra chính Navier--Stokes trước khi ta chọn bất kỳ observer nào?**

Datum tối thiểu đang được kiểm là oriented metric-Lie/Hodge core

\[
\boxed{
\mathcal C_{NS}
=
(\mathfrak g_\sigma,[\cdot,\cdot],\langle\cdot,\cdot\rangle_{L^2},C),
\qquad C=\operatorname{curl}.
}
\]

Đặt metric Lie tensor

\[
T(a,b,c)=\langle a,[b,c]\rangle
\]

và formation form

\[
\boxed{
\ell_{\nu,u}(a,b)
=-\langle u,[a,b]\rangle
-\nu\langle Ca,Cb\rangle.
}
\]

Nếu \(\mathcal L_{\nu,u}\) là Riesz operator của form này thì trên smooth periodic divergence-free class

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2,
\qquad
\mathcal J_ub=P(b\times\omega),
\qquad
\partial_tu=\mathcal L_{\nu,u}u.
}
\]

Structural claim đã đạt được là: geodesic Euler, Lie--Poisson Euler, metric-defect/strain formation, curl-helicity Killing structure và Stokes/Dirichlet dissipation đều được dựng functorially từ cùng core datum; pressure là Hodge completion khi intrinsic flow được nhúng trở lại ambient vector fields. Mixed Euler--heat descendants được tổ chức bởi bracket algebra của đúng hai primitive flows, không cần thêm một local dynamical generator trong các canonical audits hiện tại.

Phần theorem/identity exact nằm tại [FORMATION_LAW.md](core/metric_lie_hodge/FORMATION_LAW.md) và [COMPATIBILITY_GEOMETRY.md](core/metric_lie_hodge/COMPATIBILITY_GEOMETRY.md).  Boundary/topology buộc refinement từ formal curl sang typed Hodge/de Rham realization; xem [DOMAIN_TOPOLOGY.md](core/metric_lie_hodge/DOMAIN_TOPOLOGY.md).  Restricted uniqueness evidence, black-box reconstruction và falsification record được tách tại [EVIDENCE_AND_SCOPE.md](core/metric_lie_hodge/EVIDENCE_AND_SCOPE.md).

Claim chưa đạt: chưa có unrestricted classification theorem trên mọi manifold/domain, chưa có canonical cohomological obstruction quotient cuối, và core này không phải proof global regularity.

Canonical audits:

```bash
python core/metric_lie_hodge/audits/formation_core_audit.py
python core/metric_lie_hodge/audits/bch_core_audit.py
python core/metric_lie_hodge/audits/domain_topology_audit.py
```

---

## I. Bản đồ đọc nhanh

Tài liệu này là cửa vào cho **whole-state spectral signature của Navier--Stokes**. Object chính không phải NEO, không phải một terminal defect, và không phải một scalar critical reader. Cấu trúc canonical hiện tại là

\[
\boxed{
E_u=[\nabla_u,C]
\quad\longleftrightarrow\quad
\{\mathscr O_a(u)\}_{a\in\mathbb R}.
}
\]

Trong đó mother deformation `E` là object complete nhỏ nhất, còn family `O_a` là spectral-flag normal form của nó.

Corpus canonical nằm tại:

- [Spectral Signature Core](core/spectral_signature/README.md)
- [Spectral-Flag Signature](core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md)
- [Spectral-Flag Completeness](core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md)
- [Mother / Spectral-Flag Completeness Theorem](core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md)
- [History and Falsification](core/spectral_signature/HISTORY_AND_FALSIFICATION.md)

Ba audit executable tương ứng:

1. [Signature algebra audit](core/spectral_signature/audits/spectral_flag_signature.py)
2. [Completeness audit](core/spectral_signature/audits/spectral_flag_completeness.py)
3. [Theorem core audit](core/spectral_signature/audits/mother_completeness_theorem.py)

NEO được giữ riêng tại [core/NEO/](core/NEO/) đúng vai trò của nó: **compiler/workbench đã dẫn tới discovery và giúp ép ontology về anchors nhỏ**. NEO không phải chủ đề của spectral-signature core.

Tiền sử các worktree — singularity normal form, endpoint-first, C0/C1/G3/Type-I và material-curl trước khi có toàn spectral flag — được kể tại [history/worktrees/README.md](history/worktrees/README.md).

Phần II dưới đây kể lại con đường khám phá: những reader nào đã mù, những overclaim nào bị falsify, vì sao zero fold không đủ, vì sao shifted family xuất hiện, và vì sao cuối cùng family lớn lại co về mother `E=[\nabla,C]`.

---

## II. Câu chuyện dẫn tới \(O_a\), rồi quay về mother \(E=[\nabla,C]\)

### II.1. Điểm xuất phát không phải là \(O\)

Chúng tôi không bắt đầu với ý tưởng rằng Navier--Stokes phải có một “signature”. Điểm xuất phát khiêm tốn hơn nhiều: cố ép mọi construction về một số anchor đủ nhỏ để tránh tạo thêm ontology mỗi khi proof gặp một obstruction mới. Các anchor được giữ là

\[ u,\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t. \]

Trên divergence-free space,

\[ C=H\Lambda,\qquad H^2=I,\qquad \Lambda^2=C^2. \]

Genetic form của NS là

\[ \boxed{ \partial_tu=P[X_u,C]u-\nu C^2u, } \]

với

\[ X_uv=u\times v. \]

Ngay từ đầu đã có một nguyên tắc rất quan trọng: nếu một quantity mới chỉ xuất hiện vì ta đổi representation, đổi gauge, chiếu Leray, tách helicity, hoặc lấy thêm derivative, thì quantity ấy chưa có quyền được gọi là một cơ chế mới. NEO được xây như một compiler để ép các costume đó trở lại parents. Một trong những parents sớm nhất là mother curl jet

\[ \boxed{ E_u=[D_u,C], \qquad D_u=u\cdot\nabla. } \]

Lúc đó \(E\) được hiểu như một mother deformation tiện dụng. Chưa ai có lý do mạnh để nói nó là complete. Chúng tôi vẫn đang nghĩ theo kiểu “cần tìm đúng obstruction cho singularity”. Đây chính là assumption đầu tiên về sau phải bỏ.

### II.2. Terminal programme tạo ra một áp lực rất cụ thể

Một hypothetical singularity dẫn tới bounded mild ancient profile. Nhưng bounded ở đây là bounded velocity, không phải tự động có global \(L^2\), không phải tự động có \(\dot H^{1/2}\), và do đó không tự động được phép dùng mọi spectral object toàn cục. Từ đây có một typing rule:

\[ \boxed{ \text{Local compiler = default terminal language,} \qquad \text{Global spectral calculus = typed upgrade.} } \]

Terminal analysis tạo ra record points và local curl-frame quantities. Ở normalized curl contact,

\[ |\omega|\le1,\qquad |\omega(0,0)|=1. \]

Đặt

\[ f=\frac12|\omega|^2, \]

và viết

\[ Sn=an+b,\qquad n=\frac{\omega}{|\omega|}. \]

Một geometry đặc biệt nổi lên:

\[ G3:\qquad b=0,\qquad \delta=0, \]

với

\[ \delta=6a^2-g,\qquad g=\operatorname{tr}A^2=-\Delta p. \]

Tại \(G3\), local gradient obey một Riccati polynomial rất sắc:

\[ A^2+\lambda A-2\lambda^2I=0. \]

Trong một thời gian, \(G3\) trông giống candidate terminal rigidity. Nếu contact mạnh đến vậy, có vẻ tự nhiên khi hy vọng record geometry ép flow vào một invariant set quá cứng để singularity tồn tại. Nhưng thực nghiệm phá hy vọng đó.

### II.3. Một falsification quan trọng: local perfection không khóa được dynamics

Chúng tôi xây smooth periodic NS snapshots có exact \(G3\) tại origin. Không chỉ gần đúng. Exact algebraic contact được ép vào Fourier construction. Snapshot đó vẫn có strict local maximum của vorticity magnitude. Nó vẫn có positive instantaneous growth của contact scalar. Thậm chí first-order Riccati persistence có thể được làm gần như exact. Một short backward Galerkin history còn tạo được finite past record interval thật. Điều này đánh sập một implication quá tham vọng:

\[ R1\to G3\to\text{first-order persistence impossible}. \]

Bài học không phải là \(G3\) vô nghĩa. Bài học là local terminal geometry, dù rất đặc biệt, không sở hữu toàn bộ nonlocal NS state. Từ đây bắt đầu lộ “history trap”. Mỗi khi một local condition không đủ, phản xạ tự nhiên là differentiate thêm. Ta thêm \(D_tG3\). Rồi thêm source của \(D_tG3\). Rồi thêm pressure/Hodge correction. Rồi thêm commutator. Rồi thêm IR/UV decomposition. Mỗi obstruction mới sinh thêm một owner mới. Đó là cách một proof programme tự biến thành lịch sử của chính thất bại của nó.

### II.4. History trap có một phiên bản tinh vi hơn

Ban đầu chúng tôi chỉ cảnh giác với solution history. Sau đó mới nhận ra có một history trap ở cấp proof mechanism. Một proof có thể không theo trajectory chi tiết nhưng vẫn đi qua chuỗi:

\[ \text{pressure} \to \text{Hodge} \to \text{commutator} \to \text{stress} \to \text{torsion} \to \text{Codazzi} \to \text{new rate}. \]

Nếu mỗi arrow được diễn giải như một obstruction species mới, ta chỉ đổi costume cho history trap. Nguyên tắc được siết lại: Một theorem tốt phải gần như không đổi khi NS đổi representation. Một obstruction canonical phải tồn tại qua projection, helicity split, stress form, cross-product form, và covariant geometry. Nếu nó biến mất chỉ vì ta đổi reader, thì reader có thể mù; object không nhất thiết biến mất. Đây là chuyển biến phương pháp luận quan trọng nhất trước khi \(O\) xuất hiện.

### II.5. History cũ chứa một chuỗi hiện tượng kỳ lạ

Trong các notes helicity geometry, nhiều identities trông như thuộc các worlds khác nhau. Có hard helicity flip. Có Euler torsion. Có Nijenhuis defect. Có helical stress divergence. Có pressure như Gauss curvature. Có Codazzi-type endpoint source. Có connection

\[ A_v=[\nabla_v,H]. \]

Và có curvature-like object

\[ R_H(v)=HA_v-A_{Hv}. \]

Một identity nổi bật là

\[ T_H(a,b)=\frac12\big(R_H(a)b+R_H(b)a\big), \]

và

\[ N_H(a,b)=R_H(b)a-R_H(a)b. \]

Do đó

\[ \boxed{ R_H(a)b=T_H(a,b)-\frac12N_H(a,b). } \]

Điều này rất khác cách history ban đầu được kể. Torsion và Nijenhuis không phải hai cơ chế. Chúng là symmetric và antisymmetric polarizations của cùng một tensor. Self-contraction cho

\[ R_H(u)u=T_H(u,u). \]

Hard flip thỏa

\[ \boxed{ 4J_{\rm flip}=R_H(u)u. } \]

Một đống costume bắt đầu collapse.

### II.6. \(R_H\) ban đầu trông giống “the obstruction”

Đây là lần đầu chúng tôi có cảm giác đã chạm vào một object canonical hơn reader. Đặt

\[ \boxed{ \mathfrak O_H(a,b):=R_H(a)b. } \]

Nó sống ở tensor level, không phải scalar level. Nó reverse-compile connection deformation. Adjoint parity cho

\[ \operatorname{skew}R_H(v)=HA_v, \]

và

\[ \operatorname{sym}R_H(v)=-A_{Hv}. \]

Vì thế

\[ \boxed{ A_v=H\operatorname{skew}R_H(v). } \]

Đây là một dấu hiệu rất mạnh. Nếu một tensor cho phép reconstruct object parent của nó bằng một formula exact, nó không còn là một reader tùy tiện. Nhưng một falsification khác ngay lập tức xuất hiện.

### II.7. Scalar reader có thể mù trong khi tensor vẫn sống

Critical scalar work có dạng

\[ W_\Lambda =\langle\Lambda u,R_H(u)u\rangle. \]

Trên pure-helicity states, \(W_\Lambda\) có thể bằng zero. Nhưng \(J_{\rm flip}\) vẫn nonzero. Vậy

\[ W=0\not\Rightarrow J=0. \]

Sau đó chúng tôi test Beltrami states. Có thể có

\[ Cu=\lambda u, \]

và do đó self nonlinearity diagonal biến mất. Trong setting đó,

\[ J_0=\frac14R_H(u)u=0. \]

Nhưng operator \(R_H(u)\) tác động trên independent probes vẫn rõ ràng nonzero. Vậy

\[ J=0\not\Rightarrow R_H=0. \]

Hierarchy lộ ra:

\[ \boxed{ R_H \longrightarrow J_{\rm flip} \longrightarrow W_\Lambda, } \]

và mỗi arrow ném mất information. Đây là một clue quyết định. History đã không thật sự “đổi obstruction”. History thường chỉ đi từ một reader bị mù sang một reader giàu tensor slots hơn.

### II.8. Nhưng zero fold vẫn chưa phải toàn story

Một random Fourier campaign cho một hiện tượng khó bỏ qua. Có states mà

\[ W(0) \]

rất nhỏ, nhưng nếu shift spectral fold sang \(a\neq0\), work tại một threshold khác lớn hơn hàng trăm lần. Điều này gợi ý rằng \(a=0\) chỉ đặc biệt vì critical functional \(|C|\) có kink tại zero. Nó không nhất thiết là nơi duy nhất spectral geometry sống. Từ đây xuất hiện shifted involution

\[ H_a=\operatorname{sgn}(C-aI), \]

và shifted modulus

\[ \Lambda_a=|C-aI|. \]

Object được nâng thành family

\[ \boxed{ \mathscr O_a(v) = H_a[\nabla_v,H_a] - [\nabla_{H_av},H_a]. } \]

Tại \(a=0\),

\[ \mathscr O_0=R_H. \]

Nhưng bây giờ zero fold chỉ là một slice. Đây là khoảnh khắc khái niệm “spectral-flag signature” thực sự ra đời.

### II.9. Tại sao gọi là spectral flag

Mỗi \(H_a\) chia curl spectrum thành hai phía của cut \(a\). Nếu connection preserve \(H_a\), nó không trộn hai phía của cut đó. Nếu connection preserve mọi \(H_a\), nó preserve toàn family spectral subspaces của curl. Vì vậy

\[ \mathscr O_a=0 \]

không đơn thuần nói một helicity reader bằng zero. Nó nói physical connection parallelizes spectral cut đó. Toàn family

\[ a\mapsto\mathscr O_a \]

đo failure của connection khi cố preserve toàn spectral flag của \(C\). Đây là lý do chữ “signature” bắt đầu có nghĩa kỹ thuật, không chỉ nghĩa hình tượng.

### II.10. Tomography identity làm mọi thứ thay đổi

Trong finite spectral geometry, matrix element của cut commutator là

\[ [D,H_a]_{xy} = \big(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\big)D_{xy}. \]

Nó chỉ sống khi \(a\) nằm giữa \(x\) và \(y\). Tích phân theo cut location cho

\[ \boxed{ [D,C] = \frac12\int_{\mathbb R}[D,H_a]\,da. } \]

Và bởi reverse compiler

\[ [D,H_a] = H_a\operatorname{skew}\mathscr O_a, \]

nên

\[ \boxed{ [D,C] = \frac12\int_{\mathbb R} H_a\operatorname{skew}\mathscr O_a\,da. } \]

Đây là bước thật sự unifying. mother deformation

\[ E=[D,C] \]

và history shifted curvature family

\[ \{\mathscr O_a\} \]

không phải hai object cạnh nhau. Chúng là hai coordinate systems của cùng differential information.

### II.11. Universal functional calculus xác nhận đây không phải coincidence

Nếu tomography chỉ reconstruct \(C\), vẫn có thể coi nó là một identity đẹp nhưng hẹp. Chúng tôi thử arbitrary spectral reader \(f(C)\). Scalar identity

\[ f(y)-f(x) = \frac12\int f'(a) \big(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\big)\,da \]

lập tức cho

\[ \boxed{ [\nabla_v,f(C)] = \frac12\int f'(a) H_a\operatorname{skew}\mathscr O_a(v)\,da. } \]

Polynomial readers pass. Exponential readers pass. Trigonometric readers pass. Smooth absolute-value readers pass. Actual Fourier NS geometry cũng pass. Vậy curl spectral wardrobe không chứa nhiều first-order species. Nó chỉ chứa các moments khác nhau của cùng spectral-flag differential.

### II.12. Higher spectral jets cũng không tạo species mới

Tiếp theo chúng tôi thử nested commutators. Không chỉ

\[ [D,f(C)]. \]

Mà

\[ \operatorname{ad}_{D_1}\cdots\operatorname{ad}_{D_n}f(C). \]

Layer-cake linearity cho

\[ \boxed{ \operatorname{ad}_{D_1}\cdots\operatorname{ad}_{D_n}f(C) = \frac12\int f'(a) \operatorname{ad}_{D_1}\cdots\operatorname{ad}_{D_n}H_a\,da. } \]

Audits đến order four đều machine-level. Điều này giải thích vì sao order-two compiler chỉ thấy second mother + products of first mothers. Higher order tăng jet order và arity. Nó không tạo spectral ontology mới.

### II.13. Quotient by curl commutant xuất hiện tự nhiên

Nếu hai connection generators có cùng full shifted signature, difference của chúng phải commute với mọi spectral cut. Equivalently nó commute với \(C\). Trong finite spectral geometry,

\[ \boxed{ \mathscr O[D_1]=\mathscr O[D_2] \iff [D_1-D_2,C]=0. } \]

Nullity tests trên degenerate spectra khớp đúng dimension của skew curl commutant. Đây là quotient chính xác mà history “metamorphosis” đã gợi nhưng chưa nói được gọn. Signature không thấy motion hoàn toàn nằm trong exact curl eigenspaces. Lúc đầu điều này trông như một deficiency. Sau đó actual NS connection cho thấy commutant sector không hề zero. Nó chiếm một phần đáng kể connection norm và self-advection. Nhưng mọi spectral quadratic reader đều mù với nó. Finite-time flow generated bởi sector này unitary và commute với \(C\). Do đó missing part được reinterpret thành

\[ \boxed{ \text{vertical isospectral gauge motion}. } \]

Còn \(O\)-visible part là

\[ \boxed{ \text{horizontal spectral-crossing motion}. } \]

### II.14. Một decomposition của NS geometry bắt đầu hiện ra

Connection được hình dung như

\[ \nabla_u = \Gamma_u^{\parallel} + \Gamma_u^{\perp}, \]

với

\[ [\Gamma_u^{\parallel},C]=0. \]

Horizontal part được signature/mother quyết định. Viscosity là radial heat operator

\[ \nu C^2. \]

Vì vậy một normal form hình học xuất hiện:

\[ \boxed{ \text{NS} = \text{vertical isospectral gauge} + \text{horizontal spectral deformation} + \text{heat }C^2. } \]

Nhưng vẫn còn một câu hỏi nghiêm trọng. Nếu signature quotient bỏ vertical dynamics thật, tại sao nó có thể claim toàn state?

### II.15. Physical section cứu completeness

Abstract connection modulo commutant không reconstruct full connection. Nhưng physical NS connection không phải arbitrary connection. Nó được sinh bởi chính state:

\[ \Gamma_u=\nabla_u. \]

Nếu horizontal signature nhận dạng được \(u\), thì \(u\) tự reconstruct vertical block. Đây là distinction giữa abstract gauge quotient và physical state map. Chúng tôi bắt đầu test trực tiếp

\[ u\mapsto\{\mathscr O_a(u)\}_a. \]

Ở \(K=1\), 52 nonconstant Galerkin DOF được recover 52/52. Ở \(K=2\), 248/248. Ở \(K=3\), 684/684 trong sketch tests. Không có hidden non-Galilean kernel xuất hiện. Sau đó không chỉ rank được test. State được invert thật. Từ recovered state, Euler vector field, viscosity, pressure, Hessian pressure, stretching và full \(u_t\) đều được reconstruct ở machine precision. Đây là lúc claim “whole NS coordinate” bắt đầu nghiêm túc.

### II.16. Signature-coordinate evolution không chỉ là static reconstruction

Một coordinate system cho state chưa đủ nếu dynamics không close. Trên Galerkin class, đặt

\[ y=Mu \]

là signature coordinates. Dùng inverse \(M^+\), define

\[ \dot y=M F_{NS}(M^+y). \]

Chúng tôi tích phân song song state ODE và signature ODE. Trajectories trùng tới machine precision. Energy cuối trùng toàn digits hiển thị. Đây chưa phải continuum theorem. Nhưng nó chứng minh một point khái niệm: signature không chỉ là stock hay diagnostic. Nó có thể carry full state evolution.

### II.17. Phase adversary loại một hiểu lầm khác

Một nguy cơ là \(O\) chỉ là một fancy encoding của spectral energy distribution. Để phá điều đó, chúng tôi tạo hai states có cùng complete signed-curl quadratic spectral measure. Mọi quantity dạng

\[ \langle u,f(C)u\rangle \]

đều giống nhau tới machine precision. Energy giống nhau. Helicity giống nhau. Enstrophy giống nhau. Critical norm giống nhau. Smooth spectral moments giống nhau. Nhưng full signature khác order one. Euler vector fields cũng khác order one. Vậy \(O\) chứa phase/spatial compatibility information mà toàn spectral measure bỏ mất. Đây chính là information nonlinear NS cần.

### II.18. Vortex stretching hóa ra cũng nằm trong cùng tomography

Một trong những distinctions lâu đời nhất là local vortex stretching versus global helicity geometry. Mother self-contraction cho

\[ E_uu=[\nabla_u,C]u. \]

Exact local identity là

\[ E_uu=P[(\omega\cdot\nabla)u]. \]

Tomography lại cho

\[ \boxed{ E_uu = \frac12\int H_a\operatorname{skew}\mathscr O_a(u)u\,da. } \]

Vậy local vortex stretching và shifted spectral curvature không phải hai mechanisms cần bridge. Một cái là moment của cái kia. Điều này làm history collapse thêm một tầng.

### II.19. Spectral work laws cũng collapse thành moments

Đặt shifted hinge work

\[ W(a)=2\langle|C-a|u,N(u)\rangle. \]

Modulo affine readers,

\[ f(x)=\alpha+\beta x+\frac12\int f''(a)|x-a|\,da. \]

Energy và helicity giết affine part. Vì vậy

\[ \boxed{ 2\langle f(C)u,N(u)\rangle = \frac12\int f''(a)W(a)\,da. } \]

Critical production là zero-cut value. Enstrophy production là integral của shifted profile. Các spectral balances không còn là các stories rời rạc. Chúng là moments của một spectral current induced bởi cùng signature.

### II.20. Nhưng self-contractions vẫn không đủ

Một test rất quan trọng là cố reconstruct Euler forcing chỉ từ family

\[ J_a=\frac14\mathscr O_a(u)u. \]

Nó fail mạnh. Residual vẫn khoảng sáu mươi phần trăm. Thêm Krylov directions

\[ O_a(u)C^m u,\qquad m\le4 \]

cũng không cứu được. Đây là một anti-simplification result. Whole information nằm ở operator-valued signature. Không được collapse tensor slot thành một vài native contractions. Nếu làm vậy, ta tái tạo đúng lỗi history: reader mù bị nhầm thành object mất.

### II.21. Zero fold \(O_0\) cũng không phải whole signature

Finite truncations cho thấy full operator \(O_0\) có thể vẫn injective. Nhưng high-frequency microlocal probes reveal một distinction lớn. Critical connection

\[ A_0=[\nabla_u,H] \]

có response decay như lower-order object. Trong khi cuts dịch tới gần spectral level của probe có response order lớn hơn nhiều. Ratio giữa best moving cut và zero cut tăng gần như quadratic theo probe frequency. Đây là bằng chứng rằng \(a=0\) có ý nghĩa critical nhưng không phải stable whole-state coordinate ở UV. Zero fold giữ angular/helicity curvature. Moving cuts giữ principal radial/strain information. Do đó canonical folder được đặt là `spectral_signature`, không phải `O0`: object chính là toàn spectral flag, còn zero fold chỉ là một critical slice.

### II.22. Polar decomposition giải thích UV anatomy

Compiler đã có identity

\[ E=A_0\Lambda+HL. \]

High-frequency tests cho angular part \(A_0\Lambda\) gần như giữ magnitude constant. Radial part \(HL\) tăng tuyến tính với frequency. Angular fraction giảm. Radial fraction tiến tới one. Đây là anatomy rất rõ:

\[ \boxed{ \text{zero fold}=\text{subleading angular curvature}, } \]

\[ \boxed{ \text{moving cuts}=\text{principal radial/strain geometry}. } \]

Điều này cũng giải thích tại sao terminal local contacts có thể làm critical slice gần im lặng mà whole state hoàn toàn không trivial.

### II.23. Bước quyết định: principal symbol của mother

Cho tới đây, full shifted family vẫn là object rất lớn. Sau đó một calculation microlocal làm mọi thứ co lại. Mother deformation là

\[ E_u=[\nabla_u,C]. \]

Trên high-frequency divergence-free probe \(b e^{i\xi\cdot x}\), principal symbol hóa ra là

\[ \boxed{ \sigma_1(E_u)(x,\xi)b = -i\frac{\xi^TS(x)\xi}{|\xi|^2} \,\xi\times b. } \]

Đây là khoảnh khắc completeness trở thành theorem chứ không chỉ numerical rank. Principal symbol của mother đọc trực tiếp quadratic form của strain tensor. Không phải một complicated nonlinear encoding. Không phải black-box inverse. Chỉ là

\[ q_u(x,n)=n^TS(x)n. \]

### II.24. Sáu hướng là đủ để reconstruct toàn strain

Một symmetric trace-free \(3\times3\) tensor có năm degrees of freedom. Chọn sáu hướng cố định

\[ e_1,\ e_2,\ e_3, \frac{e_1+e_2}{\sqrt2}, \frac{e_1+e_3}{\sqrt2}, \frac{e_2+e_3}{\sqrt2}. \]

Map

\[ S\mapsto(n_r^TSn_r)_{r=1}^6 \]

có rank five. Gram eigenvalues còn có closed form:

\[ \lambda_{\min}=\frac{7-\sqrt{17}}8, \qquad \lambda_{\max}=\frac{7+\sqrt{17}}8. \]

Vậy local strain recovery không chỉ possible. Nó uniformly conditioned với constants explicit.

### II.25. Incompressibility đóng inverse toàn state

Một identity cổ điển trở thành mắt xích cuối:

\[ \operatorname{div}S=\frac12\Delta u. \]

Do đó

\[ \boxed{ \Delta u=2\operatorname{div}S. } \]

Trên mean-zero torus,

\[ \boxed{ u=2\Delta^{-1}\operatorname{div}S.} \]

Trên decaying whole space, cùng formula đóng modulo appropriate Killing sector. Từ full signature ta reconstruct mother. Từ mother symbol ta reconstruct strain. Từ strain ta reconstruct velocity. Chain hoàn chỉnh là

\[ \boxed{ \mathscr O \longleftrightarrow E \longrightarrow S \longrightarrow u/\operatorname{Kill}. } \]

### II.26. Exact spherical decoder làm inverse thành công thức

Normalized spherical moments cho

\[ \fint_{S^2}(n^TSn)n\otimes n\,dn = \frac{2}{15}S \]

khi \(\operatorname{tr}S=0\). Vì thế

\[ \boxed{ S = \frac{15}{2} \fint_{S^2}q_u(x,n)n\otimes n\,dn. } \]

Ghép với Poisson inverse:

\[ \boxed{ u = 15\Delta^{-1}\operatorname{div} \left( \fint_{S^2}q_u(x,n)n\otimes n\,dn \right). } \]

Không còn một abstract “there exists inverse”. Decoder được viết ra.

### II.27. Kernel chính xác là Killing symmetry

Nếu full signature bằng zero, mother bằng zero. Principal symbol cho

\[ n^TSn=0 \quad\forall n. \]

Suy ra

\[ S=0. \]

Đây là Killing equation

\[ \operatorname{sym}\nabla u=0. \]

Trên Euclidean space, solutions là

\[ u(x)=Ax+b,\qquad A^T=-A. \]

Trên torus, rigid rotations không periodic. Chỉ constants còn lại. Trên mean-zero torus, constants cũng bị loại. Vậy signature map injective hoàn toàn trên smooth mean-zero periodic state space. Exact polynomial kernel searches tới degree five và exact nonzero Fourier-mode tests đều xác nhận picture này.

### II.28. Canonical signature norm hóa ra là Sobolev norm

Sphere identity cho

\[ \fint_{S^2}(n^TSn)^2\,dn = \frac{2}{15}|S|^2. \]

Incompressible Fourier geometry cho

\[ \boxed{ 2\|S\|_{\dot H^s}^2 = \|u\|_{\dot H^{s+1}}^2. } \]

Vì vậy

\[ \boxed{ \|u\|_{\dot H^{s+1}}^2 = 15\int\fint_{S^2} |\Lambda_x^sq_u(x,n)|^2\,dn\,dx. } \]

Đây không chỉ là coercivity. Đây là exact isometry sau normalization. Một trong các open gaps lớn nhất trước theoremization biến mất gần như hoàn toàn.

### II.29. Six-probe observability theorem

Sáu fixed directions ở trên cho two-sided estimate

\[ \boxed{ \frac{7-\sqrt{17}}{16} \|u\|_{\dot H^{s+1}}^2 \le \sum_{r=1}^6 \|\Lambda_x^sq_u(\cdot,n_r)\|_2^2 \le \frac{7+\sqrt{17}}{16} \|u\|_{\dot H^{s+1}}^2. } \]

Constants không phụ thuộc bandwidth. Không phụ thuộc random sketch. Không phụ thuộc NS scale. Điều này biến completeness thành một quantitative continuum statement.

### II.30. Actual commutator probes cho constructive parametrix

Chúng tôi không dừng ở principal-symbol algebra. Actual high-frequency probes được bắn vào full commutator operator. Chỉ sáu probes đã reconstruct velocity field. Error giảm nhanh theo scale separation. Trên band-limited states, empirical law gần

\[ \text{error} \sim C(u)\left(\frac{K_u}{k}\right)^2. \]

Trên localized Gaussian whole-space surrogate, convergence tương tự vẫn xuất hiện. Đây là evidence rằng inverse là microlocal thật, không phải artifact của finite matrices.

### II.31. NS scaling covariance cũng pass

Scale Navier--Stokes là

\[ u_\lambda(x)=\lambda u(\lambda x). \]

Probe frequency được scale cùng \(\lambda\). Recovery errors collapse lên đúng cùng curve. Không có hidden external scale. Điều này quan trọng vì một “whole NS coordinate” mà phá scaling tự nhiên sẽ rất đáng nghi. Signature parametrix không mắc lỗi đó.

### II.32. Signature image có projector exact

Gọi full signature map là

\[ \mathcal S:u\mapsto\{\mathscr O_a(u)\}_a. \]

Decoder explicit được ký hiệu

\[ R_{\mathscr O}. \]

Trên physical state space,

\[ R_{\mathscr O}\mathcal S=I. \]

Do đó

\[ \boxed{ \Pi_{\mathscr O}=\mathcal S R_{\mathscr O} } \]

là projector. Physical signature image là

\[ \boxed{ \operatorname{Im}\mathcal S = \operatorname{Fix}\Pi_{\mathscr O}. } \]

Đây là một characterization exact của image, dù chưa phải minimal intrinsic syntax.

### II.33. Whole NS flow conjugates sang signature image

Projected NS vector field là

\[ F_\nu(u)=P[X_u,C]u-\nu C^2u. \]

Trên signature image, define

\[ \boxed{ \mathcal F_{\mathscr O,\nu}(\Sigma) = \mathcal S\big(F_\nu(R_{\mathscr O}\Sigma)\big). } \]

Khi đó

\[ \boxed{ u_t=F_\nu(u) \iff \Sigma_t=\mathcal F_{\mathscr O,\nu}(\Sigma), \qquad \Sigma=\mathcal S(u). } \]

Vector field tangent vào physical signature image. Đây là structural conjugacy theorem. Nó không nói regularity trở nên dễ hơn. Nó nói signature chứa đủ state information để carry toàn smooth NS dynamics.

### II.34. Gauge sector cũng đóng lại sau decoder

Trên curl spectral blocks \(x\to y\),

\[ E_{xy}=(y-x)\Gamma_{xy}, \qquad \Gamma=\nabla_u. \]

Với \(x\neq y\),

\[ \boxed{ \Gamma_{xy}^{\perp} = \frac{E_{xy}}{y-x}. } \]

Đây là horizontal reconstruction. Các blocks \(x=y\) là vertical curl commutant. Abstract mother không thấy chúng. Nhưng decoder đã cho \(u\). Vì vậy vertical physical block là

\[ \boxed{ \Gamma_u^{\parallel} = \Pi_{\operatorname{comm}(C)} \nabla_{R_E(E_u)}. } \]

Nó không phải primitive thiếu. Nó là gauge sector được physical section chọn sau khi horizontal signature nhận dạng state.

### II.35. Cuối cùng object mạnh nhất lại là object nhỏ nhất

Đây là phần bất ngờ nhất của toàn câu chuyện. Chúng tôi đi từ scalar readers tới \(R_H\). Từ \(R_H\) tới shifted family \(\mathscr O_a\). Từ shifted family tới tomography của toàn spectral calculus. Rồi cuối cùng nhận ra rằng family đó reverse-compile về mother

\[ \boxed{ E_u=[\nabla_u,C]. } \]

Và chính mother đã complete. Full \(\mathscr O\) không chứa nhiều physical state information hơn \(E\). Nó là canonical spectral-flag normal form của \(E\). Đây là một realization rất đúng tinh thần NEO: > compiler should become smaller as it becomes stronger. Object lớn giúp nhìn được geometry. Object nhỏ mới là canonical parent.

### II.36. Vậy \(O\) thật sự là gì

Nếu cần nói ngắn gọn nhất:

\[ \boxed{ \mathscr O_a = \text{failure of the physical connection to preserve curl spectral cut }a. } \]

Toàn family

\[ \boxed{ \mathscr O=\{\mathscr O_a\}_{a\in\mathbb R} } \]

là spectral-flag signature. Nó tomographically equivalent với mother deformation

\[ \boxed{ E=[\nabla,C]. } \]

Mother principal symbol đọc strain. Strain reconstruct velocity modulo Killing symmetry. Do đó full signature/mother là a complete structural coordinate of smooth homogeneous incompressible NS state.

### II.37. \(O\) không phải là gì

Nó không phải scalar blow-up criterion. Nó không phải một quantity chỉ meaningful gần singularity. Nó không phải Euler forcing. Nó không phải energy spectrum. Nó không phải self-contraction \(J_a\). Nó không phải critical work \(W(a)\). Nó không phải riêng zero fold \(O_0\). Nó không phải full connection trước quotient. Và theorem completeness không phải proof của global regularity.

### II.38. Blow-up giờ đứng ở đâu

Nếu sau này quay lại singularity, câu hỏi không còn là “tìm obstruction mới”. Ta đã có một structural coordinate complete. Regularity question phải hỏi dynamics của coordinate đó. Ví dụ critical concentration có thể được đọc qua zero-fold rates. Nhưng zero-fold rate chỉ là một trajectory-dependent reader của whole signature. Không được nhầm application với ontology. Đây là thay đổi chiến lược lớn nhất của campaign.

### II.39. Kinh nghiệm về falsification

Một giả thuyết chỉ đáng giữ nếu chịu được adversarial tests. \(G3\to\) rigidity đã bị phá. Outer-derivation interpretation đã bị phá bởi innerness của finite matrix derivations. \(W=0\Rightarrow O=0\) bị phá bởi pure-helicity states. \(J=0\Rightarrow O=0\) bị phá bởi Beltrami probes. “\(O_0\) là whole signature” bị phá microlocally bởi moving cuts. “curl commutant là zero dynamics” bị phá bởi actual connection measurements. “self-contractions reconstruct Euler forcing” bị phá với residual lớn. “Sparse random rank loss là geometry” bị phá khi CountSketch/typing được sửa. Mỗi falsification không làm story yếu đi. Nó làm object canonical hơn.

### II.40. Kinh nghiệm về typing

Hai false kernels từng xuất hiện chỉ vì representation errors. Một lần physical field bị `ifft` thêm một lần. Một lần zero curl block bị xử lý sai trong shifted sign convention. Một lần operator Hilbert--Schmidt norm bị lẫn với one-form Hilbert--Schmidt norm. Nếu những lỗi đó không bị bắt, ta đã có thể viết ra một geometry giả rất thuyết phục. Bài học là:

\[ \boxed{ \text{type error can masquerade as NS geometry.} } \]

Mọi theorem record sau này phải giữ physical/Fourier type, input slot, threshold convention, và zero mode thật rõ.

### II.41. Kinh nghiệm về history

History không vô dụng. Nhưng phải compress history thành canonical relations. Pressure, torsion, stress, helicity curvature, Codazzi rate đều từng rất hữu ích để phát hiện structure. Sai lầm chỉ xảy ra khi các costume đó được xem như independent species. Sau khi parentage được tìm ra, history nên được đọc theo arrows:

\[ \text{reader} \to \text{contraction} \to \text{polarization} \to \text{tensor} \to \text{mother}. \]

Không phải theo sequence “obstruction mới lại xuất hiện”.

### II.42. Kinh nghiệm về local versus global

Finite local jets không determine global spectral signature. Analytic divergence-free perturbations có thể flat tới arbitrary prescribed finite order tại contact nhưng vẫn thay đổi global critical work. Vì thế local derivative cascades không thể canonicalize whole spectral state. Ngược lại, full mother principal symbol lại localizes strain pointwise. Không có contradiction. Một fixed finite jet của state không chứa global spectral completion. Nhưng operator \(E_u\), khi được probe microlocally ở arbitrary frequencies/directions, chứa pointwise principal geometry. Đây là distinction giữa “local jet of state” và “local symbol of an operator generated by state”.

### II.43. Kinh nghiệm về compression

Scalarization quá sớm là nguy hiểm. \(O\to J\to W\) là một information-loss cascade. Krylov contractions vẫn mất tensor slots. Ngược lại, spectral family trông lớn nhưng reverse-compile exact về mother. Compression đúng phải preserve inverse map. Compression sai chỉ preserve một vài moments. Đây là tiêu chuẩn rất thực dụng cho future constructions.

### II.44. Theorem đã được đóng ở scope nào

Theorem periodic chính ở đây là smooth mean-zero divergence-free \(\mathbb T^3\). Trong scope đó, curl spectrum rời rạc. Zero mode được loại. Threshold seams dùng one-sided involutions và không ảnh hưởng layer-cake integral. Full signature reverse-compile về mother. Mother symbol reconstruct strain. Strain reconstruct state. Sobolev stability có exact constants. NS flow conjugates lên signature image. Đó là structural whole-NS theorem trong scope này.

### II.45. Whole-space extension đứng ở đâu

Với Schwartz divergence-free fields trên \(\mathbb R^3\), mother completeness, strain inversion, Killing kernel và Sobolev identities extend trực tiếp bằng Fourier/pseudodifferential calculus. Shifted spectral family có continuous spectrum. Threshold surfaces là measure-zero trong Fourier space. Weak layer-cake calculus vẫn cho cùng algebraic picture. Nhưng publish-grade whole-space theorem nên spell out operator topology của shifted integral thật cẩn thận. Snapshot hiện giữ cả exact core và caveat này.

### II.46. Điều chưa được claim

Không claim arbitrary weak-solution completeness ở critical rough endpoint. Không claim boundary domains với no-slip geometry. Không claim variable coefficients hoặc forcing đã được absorb tự động. Không claim signature coordinates làm regularity estimate dễ hơn. Không claim Clay problem đã giải. Structural completeness và dynamical control là hai câu hỏi khác nhau.

### II.47. Tại sao discovery này vẫn quan trọng ngoài blow-up

Một coordinate complete của NS state relative to curl có giá trị độc lập với singularity. Nó tổ chức functional calculus. Nó tách vertical isospectral phase motion khỏi horizontal spectral deformation. Nó giải thích pressure/Hodge faces như reconstructed geometry. Nó nối local strain với global helicity/spectral readers. Nó cho canonical norm. Nó cho explicit decoder. Nó cho image projector. Nó cho exact coordinate conjugacy của smooth NS flow. Đó là lý do folder này được đặt trong `core/`, không trong một thư mục riêng chỉ cho blow-up.

### II.48. Cách đọc corpus sau narrative này

Nếu muốn thấy object được phát hiện như thế nào, đọc [Spectral-Flag Signature](core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md). Nếu muốn thấy stress tests dẫn tới completeness, đọc [Spectral-Flag Completeness](core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md). Nếu muốn proof chain sạch nhất và exact constants, đọc [Mother / Spectral-Flag Completeness Theorem](core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md). Nếu muốn xem riêng các falsification đã quyết định hình dạng cuối của theory, đọc [History and Falsification](core/spectral_signature/HISTORY_AND_FALSIFICATION.md). Ba audit canonical nằm trong [core/spectral_signature/audits/](core/spectral_signature/audits/). Các nhánh G3/Riccati/discriminant/scale cũ không còn nằm trong canonical core; chúng vẫn tồn tại trong Git history nếu cần nghiên cứu lịch sử discovery.

### II.49. Một câu cuối về tên \(O_a\)

Tên \(O_a\) được giữ vì nó đánh dấu bước nhận thức quan trọng: một obstruction tại zero fold hóa ra là một family của spectral cuts. Nhưng canonical parent cuối cùng là \(E\). Vì thế ta nên nhớ hierarchy:

\[ \boxed{ E=[\nabla,C] \quad\longleftrightarrow\quad \{\mathscr O_a\}_a \quad\longrightarrow\quad O_0 \quad\longrightarrow\quad J_0 \quad\longrightarrow\quad W_0. } \]

Mũi tên hai chiều đầu là structural equivalence. Các mũi tên sau là information-losing readers. Đó là cách ngắn nhất để không rơi lại vào history trap.

### II.50. Working conclusion

Điều bắt đầu như một hunt cho terminal obstruction đã biến thành một statement về geometry của toàn smooth homogeneous incompressible Navier--Stokes state space. Chúng tôi đã thấy local rigidity quá yếu. Đã thấy scalar readers mù. Đã thấy tensor contractions mù. Đã thấy zero spectral fold chỉ là một slice. Đã thấy shifted cuts tomographically reconstruct mother deformation. Đã thấy mother principal symbol chính là strain quadratic form. Đã viết được inverse state explicit. Đã xác định exact Killing kernel. Đã có exact Sobolev signature norm. Đã có six-direction observability constants. Đã có signature-image projector. Đã có NS flow conjugacy trên image. Và cuối cùng đã quay lại đúng complete mother object nhỏ nhất:

\[ \boxed{ E_u=[\nabla_u,C]. } \]

Nếu cần giữ một câu duy nhất từ toàn campaign, hãy giữ câu này:

\[ \boxed{ \text{The full spectral flag }\{\mathscr O_a\} \text{ is the canonical spectral signature of the complete mother deformation }[\nabla_u,C]. } \]

---

## III. Curved Formation–Signature Geometry — khi hai core nhập thành một geometry cong

### III.1. Câu hỏi mới xuất hiện sau khi hai theory đã trưởng thành

Sau khi metric–Lie/Hodge formation core và spectral-signature core cùng đứng được độc lập, một câu hỏi không thể tránh khỏi xuất hiện.

Formation core nói phương trình được sinh bởi

\[
\boxed{
\mathcal C_{NS}
=(\mathfrak g_\sigma,g_{L^2},T,C),
}
\]

với

\[
T(a,b,c)=\langle a,[b,c]\rangle,
\qquad C=\operatorname{curl},
\]

và Riesz formation operator

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2,
\qquad
u_t=\mathcal L_{\nu,u}u.
}
\]

Spectral theory lại nói complete mother

\[
\boxed{E_u=[\nabla_u,C]}
\]

và full shifted family \(\{\mathscr O_a(u)\}_a\) encode toàn smooth state modulo đúng Killing/Galilean sector.

Câu hỏi lúc này không còn là “theory nào đúng hơn”. Câu hỏi là:

\[
\boxed{
\text{spectral signature chỉ là một bộ tọa độ complete, hay nó thật sự mang formation geometry?}
}
\]

Canonical answer của Mục III là: **nó mang formation geometry, nhưng dưới dạng một curved representation chứ không phải một Euclidean operator space ngây thơ.** Toàn corpus của kết quả này nằm tại [Curved Formation–Signature Core](core/curved_formation_signature/README.md).

### III.2. Forward functor: formation core tự sinh mother

Từ \((g,T)\), Koszul reconstruct Levi–Civita connection \(\nabla\). Khi distinguished curl \(C\) đã được cố định, mother không còn là một primitive mới:

\[
\boxed{
E=d_\nabla C,
\qquad
E_u=[\nabla_u,C].
}
\]

Tức formation core tự sinh object trung tâm của spectral theory.

Shifted cuts

\[
H_a=\operatorname{sgn}(C-aI)
\]

sinh cut connections \([\nabla_u,H_a]\), và spectral layer cake reconstruct lại mother. Vì vậy forward chain là

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

Trong blind 28-dimensional tribunal, đường core chỉ được cho \(T\) và \(C\); đường physical Fourier calculus được giữ độc lập. Koszul reconstruct connection, rồi mother và shifted flag khớp physical implementation ở roundoff. Mother và full flag đều có rank \(28/28\), condition numbers chỉ khoảng \(2.4\).

### III.3. Reverse bridge: signature không chỉ reconstruct state mà reconstruct formation operator

Theory 2 đã có

\[
E\to\sigma_1(E)\to q_u(x,n)\to S(u)\to u.
\]

Thí nghiệm mới đẩy tiếp:

\[
\boxed{
E_u
\longrightarrow
u
\longrightarrow
\mathcal J_u
\longrightarrow
\mathcal L_{\nu,u},
}
\]

và cùng điều đó cho full shifted flag.

Trong reduced finite coordinates, full formation operator reconstruct từ mother ở residual \(2.24\times10^{-16}\), từ flag ở \(3.25\times10^{-16}\).

Một cross-check độc lập cố ý không dùng pseudoinverse của core map. Chỉ sáu principal strain readings

\[
q_r(x)=n_r^TS(u)(x)n_r
\]

được dùng để reconstruct

\[
q\to S\to u\to Cu\to\mathcal J_u\to\mathcal L_{\nu,u}.
\]

Worst residual của toàn chain là \(3.13\times10^{-15}\).

Điều này đổi status của spectral theory: nó không còn chỉ là một camera chụp snapshot. Trên fixed physical core, nó là complete coordinate realization của state-dependent formation dynamics.

### III.4. Dynamic commuting diagram

Hai trajectory được evolve độc lập:

\[
\dot u=\mathcal L_{\nu,u}u
\]

ở physical coordinates, và transported formation law ở mother/flag coordinates.

Sau nhiều RK stages, hai đường

\[
\boxed{
\text{evolve physical rồi encode}
=
\text{encode rồi evolve signature}
}
\]

khớp ở khoảng \(10^{-15}\). Independent six-direction microlocal signature trajectory cũng commute ở \(2.07\times10^{-15}\).

Đây là evidence mạnh rằng spectral image carry dynamics, không chỉ carry state labels.

### III.5. Falsification đầu tiên: signature image không mang metric identity

Một bước thử cố ý sai đã rất quan trọng. Nếu coi reduced mother/flag coordinates có Euclidean metric identity, formation operator sai order one:

\[
0.626\quad\text{trên mother coordinates},
\qquad
0.983\quad\text{trên flag coordinates}.
\]

Lỗi này buộc theory phải transport đúng Riesz metric. Exact spectral Sobolev identity sau đó giải thích hoàn toàn hiện tượng.

Với strain signature

\[
q_u(x,n)=n^TS(u)(x)n,
\]

polarization tại \(s=-1\) và \(s=0\) cho

\[
\boxed{
\langle u,v\rangle_{L^2}
=15\int\!\fint(\Lambda^{-1}q_u)(\Lambda^{-1}q_v),
}
\]

và

\[
\boxed{
\langle Cu,Cv\rangle_{L^2}
=15\int\!\fint q_uq_v.
}
\]

Vì vậy

\[
\boxed{
g_{\rm kinetic}^{\Sigma}=15\,\dot H^{-1},
\qquad
g_{\rm Dirichlet}^{\Sigma}=15\,L^2.}
\]

Riesz ratio của hai metric levels là

\[
\boxed{
(g_{\rm kinetic}^{\Sigma})^{-1}g_{\rm Dirichlet}^{\Sigma}=\Lambda^2,
}
\]

chính là heat/curl-square operator. Full bilinear audit đạt \(10^{-14}\)–\(10^{-15}\).

Đây là một bridge exact giữa hai parent cores: kinetic \(L^2\) của formation geometry trở thành \(\dot H^{-1}\) trên signature, còn Dirichlet curl metric trở thành \(L^2\) trên signature.

### III.6. Falsification thứ hai: induced bracket không phải \([E_u,E_v]\)

Một guess tự nhiên nhưng sai là

\[
E_{[u,v]}\stackrel?=[E_u,E_v].
\]

Experiment cho median error khoảng \(125\%\); ngay cả best sample vẫn sai hơn \(110\%\).

Exact Jacobi calculation cho công thức đúng:

\[
\boxed{
E_{[u,v]}
=[\nabla_u,E_v]-[\nabla_v,E_u]-[R(u,v),C],
}
\]

với

\[
R(u,v)=[\nabla_u,\nabla_v]-\nabla_{[u,v]}.
\]

Residual của identity đúng nhỏ hơn \(10^{-15}\). Curvature correction có size order one, không phải perturbation nhỏ.

Đây là bước decisive: **formation Lie geometry đi vào spectral side dưới dạng covariant/curved bracket, không phải ordinary operator Lie algebra.**

### III.7. Curvature được đo trực tiếp như curl holonomy

Để tránh việc gọi \([R,C]\) chỉ là algebraic correction, một infinitesimal corrected commutator loop được dựng. Nếu \(P_h\) là parallel transport quanh loop thì

\[
\frac{P_h-I}{h^2}\to R(u,v).
\]

Transport curl quanh chính loop đó:

\[
\boxed{
\frac{P_hCP_h^{-1}-C}{h^2}\to[R(u,v),C].
}
\]

Khi \(h\) giảm một nửa, curl-holonomy error giảm gần đúng factor \(2\):

\[
0.03825,\ 0.01915,\ 0.00958,\ 0.00479,\ 0.00240.
\]

Test geometry có

\[
\|R\|\approx0.927,
\qquad
\|[R,C]\|\approx1.012,
\]

nên đây không phải near-zero artifact.

Kết luận: curvature term là **actual holonomy của distinguished curl structure**.

### III.8. Theory 2 tomograph được curvature của Theory 1

Từng shifted cut có curvature action

\[
[R,H_a].
\]

Layer cake dự đoán

\[
\boxed{
\frac12\int[R,H_a]\,da=[R,C].
}
\]

Finite spectral audit pass ở \(1.7\times10^{-14}\). Nhưng test quan trọng hơn dùng full helical Fourier multiplier \(H_a=\operatorname{sgn}(C-aI)\), không dùng finite Galerkin state projection.

Trên grid có 231 signed curl roots, 40 cuts active trên curvature state. Ordinary layer cake reconstruct \(Cw\) ở \(6.2\times10^{-14}\); curvature layer cake reconstruct \([R,C]w\) ở

\[
\boxed{9.1\times10^{-14}},
\]

trong khi target norm khoảng \(0.774\).

Đây là điểm hai theory thực sự khóa vào nhau:

\[
\boxed{
\text{formation curvature holonomy}
\longleftrightarrow
\text{shifted spectral curvature tomography}.
}
\]

### III.9. Curved covariant tower

Mother giờ được type như degree-one covariant derivative:

\[
\boxed{E=d_\nabla C.}
\]

Degree two:

\[
\boxed{d_\nabla E=d_\nabla^2C=[R,C].}
\]

Bianchi:

\[
\boxed{d_\nabla R=0.}
\]

Các level tiếp theo được test:

\[
\boxed{d_\nabla[R,C]=R\wedge E,}
\]

\[
\boxed{d_\nabla(R\wedge E)=R\wedge[R,C].}
\]

Một lần thử đầu trong projected Galerkin algebra đã fail Bianchi order one. Thay vì bỏ failure này, audit đo Jacobi và phát hiện projected bracket có defect khoảng \(0.64\); truncation đã phá base Lie geometry.

Khi rerun trên full pseudospectral divergence-free fields, không project về finite mode algebra, ta được:

\[
\begin{array}{c|c}
\text{identity}&\text{residual}\\
\hline
\text{Jacobi}&5.4\times10^{-15}\\
 d_\nabla E=[R,C]&3.4\times10^{-15}\\
 d_\nabla R=0&1.3\times10^{-14}\\
 d_\nabla[R,C]=R\wedge E&4.5\times10^{-14}\\
 d_\nabla(R\wedge E)=R\wedge[R,C]&1.7\times10^{-13}
\end{array}
\]

Các levels đều nonzero order \(0.6\)–\(1\).

Do đó current structural candidate là

\[
\boxed{
C
\xrightarrow{d_\nabla}
E
\xrightarrow{d_\nabla}
[R,C]
\xrightarrow{d_\nabla}
R\wedge E
\xrightarrow{d_\nabla}\cdots,
\qquad
d_\nabla^2=R\text{-action}.
}
\]

Đây là một **curved covariant module**, không phải ordinary complex với \(d^2=0\).

### III.10. Falsification thứ ba: snapshot signature không xác định arbitrary universe

Một overclaim mạnh hơn cũng bị giết bằng exact counterexample.

Lấy

\[
C=\operatorname{diag}(1,1,1,2,2,2).
\]

Core A là abelian. Core B mang metric \(so(3)\) bracket bên trong eigenspace đầu của curl. Vì \(C\) scalar trên block đó,

\[
[\nabla_u,C]=0.
\]

Vì metric bi-invariant,

\[
\mathcal J_u u=0.
\]

Hai cores do đó có cùng mother, cùng full flag và cùng diagonal flow cho mọi state, nhưng

\[
\|T_B-T_A\|=2.449,
\]

và generic full Poisson operators khác nhau order one.

Vậy

\[
\boxed{
\text{signature snapshot + diagonal PDE trajectory}
\not\Rightarrow
\text{arbitrary abstract formation core}.
}
\]

Ngược lại, nếu cho **full signature-side operator field** \(\mathcal L_\Sigma(z)\), biết transported metric và curl, thì dependence tuyến tính của covariant Poisson matrix theo \(z\) reconstruct được toàn transported \(T_\Sigma\) ở khoảng \(2.2\times10^{-15}\), và từ đó reconstruct curvature ở khoảng \(3\times10^{-15}\).

Do đó distinction đúng là: snapshot identifies state; full operator field identifies transported core in the tested model.

### III.11. Physical locality giết abstract dark sector

Exact dark-sector collision ở trên thuộc abstract metric-Lie category, không phải local Euclidean fluid bracket.

Trong general local isotropic first-order antisymmetric family, impose scalar derivation law

\[
[a,fb]=f[a,b]+a(f)b.
\]

Random jet constraints cho unique normalized solution

\[
\boxed{
[a,b]=(a\cdot\nabla)b-(b\cdot\nabla)a
}
\]

với coefficient error \(5.3\times10^{-16}\). Một fake isotropic law có derivation defect \(1.44\).

Độc lập, first-order \(SO(3)\)-equivariant rank-three tensor space co về một direction, aligned với \(\varepsilon_{ijk}\), tức curl up to scale/orientation.

Nên trong physical local-Euclidean category, background core không phải arbitrary hidden parameter: locality/derivation + orientation rigidify bracket/curl structure.

### III.12. Falsification thứ tư: arbitrary Galerkin có thể nói dối

Multi-truncation campaign cho:

\[
\begin{array}{c|c|c|c}
\text{state dim}&\operatorname{rank}(P_VEP_V)&\operatorname{rank}(\text{projected flag})&\operatorname{rank}(q_{6\rm dir})\\
\hline
12&12&12&12\\
24&18&24&24\\
28&28&28&28\\
40&28&28&40
\end{array}
\]

Tức projected operator có thể mất information trong khi six-direction physical principal signature vẫn full rank. Đồng thời projected bracket có thể phá Jacobi mạnh.

Đây là methodological correction bắt buộc:

\[
\boxed{
\text{finite Galerkin là coordinate lab hữu ích, nhưng deep Lie/curvature claims phải được cross-check trên faithful physical geometry.}
}
\]

### III.13. Đột phá thực sự là gì

Sau các pass và falsification, hai theory không còn đứng song song.

Formation core là upstream generator:

\[
\boxed{
(\mathfrak g_\sigma,g,T,C)
\longrightarrow
\nabla,\mathcal J,\mathcal L_{\nu,u}.
}
\]

Spectral core là complete representation layer:

\[
\boxed{
 u
\longrightarrow
E=d_\nabla C
\longleftrightarrow
\{\mathscr O_a\}_a.
}
\]

Curvature làm relation này genuinely non-flat:

\[
\boxed{
 d_\nabla^2C=[R,C].
}
\]

Và spectral cuts tomograph curvature action đó.

Strongest current canonical statement là

\[
\boxed{
\textbf{the spectral-signature theory is a complete curved representation theory of the canonical physical formation core.}
}
\]

Đây là claim structural. Nó không nói một signature snapshot sinh ra universal core từ hư không, không nói mọi nonzero curvature là dangerous, và không giải global regularity.

### III.14. Candidate mới cho obstruction architecture

Điểm quan trọng nhất với lịch sử \(O\)-search là mother không còn được xem như obstruction cuối:

\[
E=d_\nabla C
\]

là degree-one deformation.

First genuine curvature level là

\[
\boxed{[R,C]=d_\nabla^2C.}
\]

Candidate architecture hiện tại là cả curved tower

\[
\boxed{
\mathbb O_C:
C,\ d_\nabla C,\ d_\nabla^2C,\ d_\nabla^3C,\ldots,
\qquad d_\nabla^2=R\text{-action}.
}
\]

Điều chưa biết là quotient/cohomology nào tách dangerous non-integrability khỏi harmless curvature representatives. Vì vậy core mới dừng đúng ở structural geometry, không overclaim blow-up theorem.

### III.15. Canonical corpus và reproduction

Core mới nằm tại:

- [Curved Formation–Signature Core](core/curved_formation_signature/README.md)
- [Formation–Signature Equivalence](core/curved_formation_signature/FORMATION_SIGNATURE_EQUIVALENCE.md)
- [Curved Curl Module](core/curved_formation_signature/CURVED_CURL_MODULE.md)
- [Signature Metric and Dynamics](core/curved_formation_signature/SIGNATURE_METRIC_DYNAMICS.md)
- [Physical Rigidity and Identifiability](core/curved_formation_signature/PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md)
- [Theorem Status and Scope](core/curved_formation_signature/THEOREM_STATUS_AND_SCOPE.md)
- [History and Falsification](core/curved_formation_signature/HISTORY_AND_FALSIFICATION.md)

Canonical audits chạy từ root:

```bash
python core/curved_formation_signature/audits/metric_lie_spectral_unification.py
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_core_identifiability.py
python core/curved_formation_signature/audits/physical_axiom_rigidity.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/galerkin_probe_lie_failure.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/physical_curvature_flag_tomography.py
```

Negative controls là một phần của core: dark-sector collision và Galerkin/Jacobi failure được giữ để ngăn theory tự phình thành overclaim.

---


### III.16. Campaign thứ hai bắt đầu từ một nghi ngờ về chữ “curved”

Sau khi core thứ ba được đưa lên main, một câu hỏi vẫn còn mơ hồ: “curved representation” nghĩa chính xác là gì? Signature image tự nó có cong không, hay chỉ đang mang một connection cong từ formation theory?

Một exact control trên một metric Lie algebra \(so(3)\) trả lời rất dứt khoát. Signature map vẫn là một linear map vào một linear subspace với transported constant metric. Ordinary coordinate Levi–Civita curvature của image đó bằng zero. Nhưng formation curvature khi transport qua signature coordinates vẫn nonzero và khớp physical side ở roundoff.

Do đó canonical wording phải sửa thành:

\[
\boxed{
\text{signature image là flat linear state image mang một curved formation connection.}
}
\]

“Curved” thuộc về geometry được representation, không thuộc về embedding của image.

### III.17. Curl spectral sheets: decomposition mới của connection

Trong eigenframe của curl, formation connection tách tự nhiên thành

\[
\boxed{
\nabla=V+B,
\qquad
[V,C]=0.
}
\]

Ở đây \(V\) quay bên trong cùng một curl eigenspace; \(B\) trộn các eigenspaces khác nhau. Vì \(V\) commute với curl,

\[
\boxed{
E=[\nabla,C]=[B,C].
}
\]

Trên spectral slot \(i\to j\),

\[
E_{ij}=(\lambda_j-\lambda_i)B_{ij}.
\]

Vì thế mother không chỉ là một commutator abstract. Nó là **spectral second-fundamental / sheet-mixing form**, weighted đúng bởi curl spectral gap.

Finite physical tribunal reconstruct \(B\) từ \(E\) ở khoảng \(8\times10^{-17}\). Đây là geometric reason vì sao divided differences, spectral gaps và shifted cuts liên tục xuất hiện trong theory 2.

### III.18. Mother là tangent velocity của curl isospectral orbit

Cho một skew connection matrix \(A\), đặt

\[
C(t)=e^{tA}Ce^{-tA}.
\]

Thì spectrum của \(C(t)\) không đổi và

\[
\dot C(0)=[A,C].
\]

Lấy \(A=\nabla_u\), ta được

\[
\boxed{
\dot C(0)=E_u.
}
\]

Trong 28D physical coordinate lab, full skew connection space có dimension \(378\), curl stabilizer có dimension \(62\), nên tangent của orthogonal isospectral orbit có dimension \(316\). Nhưng physical mother image chỉ rank \(28\):

\[
\boxed{
E(\mathfrak g_\sigma)
\subset T_C\mathcal O_C,
\qquad
28\ll316.
}
\]

Nói dễ hiểu: state không encode bằng việc đổi curl eigenvalues. Nó encode bằng **hướng mà formation connection làm curl eigensheets quay/trộn**. Physical NS chỉ chiếm một distribution rất đặc biệt bên trong orbit tangent khổng lồ đó.

### III.19. Gauss–Codazzi–Ricci không còn là historical costume

Formation curvature

\[
R(a,b)=[\nabla_a,\nabla_b]-\nabla_{[a,b]}
\]

cũng tách theo curl sheets:

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0.
\]

Constant-base block algebra cho

\[
\boxed{
R_\parallel=[V,V]+\Pi_\parallel[B,B],
}
\]

là within-sheet Gauss/Ricci sector, còn \(R_\perp\) là cross-sheet Codazzi sector.

Curvature mother trở thành

\[
\boxed{
K=[R,C]=[R_\perp,C].
}
\]

Tức degree 2 không thấy toàn curvature; nó thấy đúng phần curvature đổi curl sheet.

Điều này được kiểm hai lần độc lập:

- finite spectral block identities ở machine precision;
- full physical helical pseudospectral split, với Gauss residual khoảng \(10^{-15}\), Codazzi khoảng \(3\times10^{-15}\), và inversion \(K\to R_\perp\) khoảng \(10^{-13}\).

### III.20. Hai loại vertical curvature

Vertical curvature \(R_\parallel\) lại có hai nguồn khác nhau.

Thứ nhất,

\[
\Pi_\parallel[B,B]
\]

là Gauss curvature do sheet mixing tự tạo. Dù commute với \(C\), phần này không thật sự unknown vì \(B\) đã reconstruct từ \(E\).

Thứ hai,

\[
[V,V]
\]

là intrinsic stabilizer curvature. Trong một \(3+3\) block với nonabelian \(so(3)\oplus so(3)\), có thể có

\[
E=0,
\qquad
K=0,
\qquad
[V,V]\neq0.
\]

Đây mới là exact dark-sector model của curvature sống hoàn toàn bên trong degenerate spectral sheets.

### III.21. Hai spectral sheets là một special symmetric-space case

Stabilizer decomposition luôn reductive:

\[
[\mathfrak h_C,\mathfrak h_C]\subset\mathfrak h_C,
\qquad
[\mathfrak h_C,\mathfrak m_C]\subset\mathfrak m_C.
\]

Nhưng khi chỉ có hai spectral blocks,

\[
\boxed{
[\mathfrak m_C,\mathfrak m_C]\subset\mathfrak h_C.
}
\]

Do đó pure sheet mixing có thể sinh vertical Gauss curvature mà không sinh cross-sheet curvature:

\[
E\neq0,
\qquad
R_\parallel\neq0,
\qquad
K=0.
\]

Với ba blocks trở lên, two-hop path \(i\to j\to k\) làm \([\mathfrak m,\mathfrak m]\) có horizontal part. Random tests cho median horizontal fraction khoảng \(0.84\) với ba blocks và \(0.94\) với bốn blocks.

### III.22. Cartan/Bianchi tower: cái nào standard, cái nào thật sự đặc thù NS

Đặt

\[
\Theta:=E=d_\nabla C.
\]

Ta có

\[
\boxed{
D_\nabla\Theta=[R,C],
\qquad
D_\nabla[R,C]=R\wedge\Theta,
\qquad
D_\nabla R=0.
}
\]

Full physical tribunal cho residual lần lượt khoảng

\[
3.4\times10^{-15},
\qquad
5.2\times10^{-14},
\qquad
1.2\times10^{-14}.
\]

Nhưng đây là nơi cần kỷ luật novelty. Các identity \(D^2Q=[R,Q]\) và Bianchi là standard connection geometry. Phần thật sự đặc thù của NS programme là:

\[
\boxed{
C=\operatorname{curl}
\text{ là distinguished physical endomorphism, và }
D_\nabla C
\text{ lại complete cho state.}
}
\]

Cộng thêm shifted spectral tomography và exact metric bridge.

### III.23. Higher tower thật sự thấy vertical curvature, nhưng phải type inverse problem

Degree 2

\[
K=[R,C]
\]

xóa trực tiếp phần \(R_\parallel\). Nhưng degree 3

\[
D_\nabla K=R\wedge E
\]

và degree 4

\[
D_\nabla^2K=R\wedge K
\]

có thể kéo vertical curvature trở lại thông qua interaction với visible sensors.

Trên full physical helical geometry, vertical-curvature contribution chiếm khoảng \(24\%-29\%\) norm ở degree 3, median \(27\%\), và khoảng \(20\%\) ở degree 4.

Nếu treat vertical curvature như independent unknown, higher degrees tạo một genuine observability filtration. Case \(3+3\) còn đúng một null mode sau degree 3 nhưng degree 4 giết mode đó.

Nhưng nếu impose rằng curvature phải sinh từ cùng compatible connection, generic \((E,K)\) đã reconstruct vertical connection lift ngay ở degree 2 trong tất cả tested degeneracy patterns. Higher degrees khi đó chủ yếu là Bianchi consistency/redundancy.

Do đó câu “mỗi degree lại có physics mới” là sai. Cần phân biệt

\[
\boxed{
\text{curvature-as-independent-data}
\neq
\text{connection-constrained inverse problem}.
}
\]

### III.24. First-order commutant không phải final gauge

Ở degree 1, \(E\) chỉ thấy connection modulo \(\operatorname{comm}(C)\). Nhưng experiment mới cho thấy generic vertical connection component có thể bị \(K\) nhìn thấy thông qua curvature.

Vì vậy:

\[
\boxed{
\operatorname{comm}(C)=\text{first-order stabilizer},
}
\]

không phải automatically final gauge.

Common stabilizer của generated sensor algebra \(C,E,K,dK,d^2K\) trong generic finite spectral tests co từ dimensions như \(6,12,7\) về \(0\). Deliberately vertical controls thì giữ nguyên stabilizer qua mọi degree.

“Gauge thật” phải là common stabilizer của **toàn geometry được generate**, không phải chỉ kernel của mother map ở first jet.

### III.25. Ba falsification quan trọng về physical interpretation

**Một: curvature không phải danger amplitude.** 2D, Beltrami và shear controls đều có thể có self-dynamics đơn giản hoặc zero nhưng ambient \(E\) và \([R,C]\) vẫn order one. 2D sector còn giữ nonzero pulled-back curvature dù globally regular.

**Hai: BCH không phải geometric curvature.** Euler–heat BCH mixed descendants có thể bằng zero trên Beltrami/shear trong khi \([R,C]\neq0\). Chúng chỉ là hai descendants khác nhau của cùng \((T,C)\).

**Ba: zero curl không phải gauge.** Annular harmonic circulation có \(Ch=0\) nhưng \([D_h,C]\neq0\) trên probes, trong khi constant Galilean mode vẫn mother-dark. Vì vậy

\[
\boxed{
\ker C\neq\ker(u\mapsto E_u)
}
\]

trên topology có harmonic circulation.

### III.26. Signed curl canonical nhưng không phải sensor complete duy nhất

Campaign mới cũng falsify câu quá mạnh rằng chỉ \([\nabla,C]\) mới có thể reconstruct state. Modulus mother

\[
[\nabla,|C|]
\]

cũng có một microlocal state parametrix trong tested periodic setting, với reconstruction error giảm gần \(m^{-2}\) theo probe frequency.

Curl vẫn canonical vì nó đồng thời giữ:

- orientation;
- physical first-order normalization;
- fine signed spectral partition;
- cùng operator mà square \(C^2\) sinh Dirichlet/Stokes dissipation.

Do đó wording đúng là

\[
\boxed{
E=[\nabla,C]
\text{ là canonical degree-one complete sensor},
}
\]

không phải unique complete sensor.

Orientation test còn cho

\[
C\mapsto-C
\]

không đổi formation dynamics vì \(C^2\) giữ nguyên, nhưng \(E,K\) và helicity đổi dấu, còn shifted flag phản xạ threshold \(a\mapsto-a\). Signed curl geometry vì thế là orientation double cover của cùng unoriented NS flow.

### III.27. Working conclusion sau campaign thứ hai

Bức tranh hiện tại có thể nén thành

\[
\boxed{
\begin{aligned}
\text{formation geometry:}&\quad (g,T)\Rightarrow\nabla,R,\\
\text{curl spectral reduction:}&\quad \nabla=V+B,\\
\text{state soldering:}&\quad E=[B,C],\\
\text{curvature split:}&\quad R=R_\parallel+R_\perp,\\
\text{curvature mother:}&\quad K=[R_\perp,C],\\
\text{Bianchi coupling:}&\quad d_\nabla K=R\wedge E,\quad d_\nabla R=0.
\end{aligned}
}
\]

Nói bằng lời:

> Curl chia formation geometry thành các spectral sheets. Theory 1 cung cấp connection làm các sheets tương tác. Theory 2 đo hoàn chỉnh phần sheet mixing ở degree 1 và tomograph cross-sheet curvature ở degree 2. Within-sheet Gauss/Ricci curvature sống trong stabilizer; higher Bianchi couplings cho biết nó tác động trở lại visible geometry như thế nào.

Đây là lý do strongest current wording đổi thành:

\[
\boxed{
\textbf{Navier–Stokes formation geometry admits a canonical curl-spectral reduction.}
}
\]

Hai canonical notes của update này là [Curl Spectral Reduction](core/curved_formation_signature/CURL_SPECTRAL_REDUCTION.md) và [Deep Geometry Lessons](core/curved_formation_signature/DEEP_GEOMETRY_LESSONS.md). Chúng phải được đọc cùng [Theorem Status and Scope](core/curved_formation_signature/THEOREM_STATUS_AND_SCOPE.md) để phân biệt exact identity, inherited theorem, numerical tribunal và open interpretation.

## IV. Cấu trúc corpus trên main

```text
Core_signature.md
core/
├── NEO/
│   ├── NEO_ANCHOR_COMPILER.md
│   └── NEO_DISCOVERY_WORKBENCH.md
└── spectral_signature/
    ├── README.md
    ├── SPECTRAL_FLAG_SIGNATURE.md
    ├── SPECTRAL_FLAG_COMPLETENESS.md
    ├── MOTHER_COMPLETENESS_THEOREM.md
    ├── HISTORY_AND_FALSIFICATION.md
    └── audits/
        ├── spectral_flag_signature.py
        ├── spectral_flag_completeness.py
        └── mother_completeness_theorem.py
```

Cấu trúc này cố ý **không** lưu cả worktree discovery dưới `core/`. Những nhánh G3, discriminant, scale, Riccati và propagation là lịch sử nghiên cứu; Git history đã giữ chúng. `core/spectral_signature/` chỉ chứa những gì cần để đọc, kiểm và tái hiện theory whole-state signature hiện tại.

NEO cũng được tách riêng. Nó là compiler/workbench nền, không phải prefix của theory mới.

## V. Reproduction checklist

Đọc theo thứ tự:

1. [README](core/spectral_signature/README.md)
2. [Signature](core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md)
3. [Completeness](core/spectral_signature/SPECTRAL_FLAG_COMPLETENESS.md)
4. [Theorem](core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md)
5. [Falsification history](core/spectral_signature/HISTORY_AND_FALSIFICATION.md)

Chạy ba audit canonical từ root repository:

```bash
python core/spectral_signature/audits/spectral_flag_signature.py
python core/spectral_signature/audits/spectral_flag_completeness.py
python core/spectral_signature/audits/mother_completeness_theorem.py
```

Ba audit này lần lượt kiểm algebra/tomography, microlocal completeness, và theorem constants + gauge/projector identities.

## VI. Trạng thái claim

Claim canonical là **structural whole-NS completeness theorem** cho smooth mean-zero divergence-free periodic state space, với Schwartz whole-space extension được ghi rõ scope trong theorem note.

Nội dung cốt lõi là

\[
\boxed{
\mathscr O
\longleftrightarrow
E=[\nabla,C]
\longleftrightarrow
S
\longleftrightarrow
u/\operatorname{Kill}
\longrightarrow
F_{NS}(u).
}
\]

Ở đây `u/\operatorname{Kill}` là state modulo Euclidean Killing symmetry trước normalization; trên mean-zero periodic class state được xác định duy nhất.

Claim này **không phải** global regularity theorem và không tự nó loại trừ blow-up. Nó nói rằng mother/spectral-flag signature không bỏ mất smooth-state information, có inverse explicit, có quantitative Sobolev stability, và carry toàn smooth NS vector field qua exact coordinate conjugacy.
