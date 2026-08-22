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

## III. Core 3 — Curl-Spectral Differential Observability của Formation Geometry

Core thứ ba bắt đầu như một câu hỏi nối hai theory đã trưởng thành, nhưng sau ba campaign nó đã biến thành một câu hỏi mạnh hơn hẳn.

Formation core trả lời:

\[
(g,T,C)
\Longrightarrow
\nabla,\mathcal J,\mathcal L_{\nu,u}.
\]

Spectral-signature core trả lời:

\[
E_u=[\nabla_u,C]
\Longleftrightarrow
u=u\ \text{modulo Killing/Galilean symmetry}.
\]

Core 3 lúc đầu chỉ hỏi hai construction đó có commute hay không.  Sau campaign curl-spectral reduction, câu hỏi đổi thành:

\[
\boxed{
(g_\Sigma,C,E,K)
\stackrel{?}{\Longrightarrow}
\nabla
\stackrel{?}{\Longrightarrow}
T,R,\mathcal J.
}
\]

Nói cách khác: Theory 2 có chỉ encode **state**, hay full differential signature của nó còn reverse-engineer được **formation geometry** đã sinh ra state dynamics?

Câu trả lời hiện tại rất mạnh nhưng phải type cẩn thận:

\[
\boxed{
\text{state completeness}
\to
\text{spectral differential geometry}
\to
\text{generic formation-geometry reconstruction}.
}
\]

Từ “generic” là thiết yếu.  Highly degenerate curl spectra tạo singular strata; ở đó higher covariant degrees và nonlinear information có thể cần thiết.

### III.1. Ba cấp completeness phải tách riêng

Core 3 hiện dùng ba khái niệm completeness khác nhau.

**Level A — state completeness.**  Trên canonical smooth mean-zero periodic physical core,

\[
\boxed{
E_u\Longrightarrow u
}
\]

modulo known Killing/Galilean sector.  Đây là theorem-level result kế thừa từ parent spectral-signature core.

**Level B — differential spectral geometry.**  Mother không chỉ là một observable của từng state; nó là một operator-valued one-form

\[
\boxed{
E=d_\nabla C.
}
\]

Differentiating covariantly,

\[
\boxed{
K:=d_\nabla E=d_\nabla^2C=[R,C].
}
\]

Tower đầu tiên là

\[
\boxed{
C
\xrightarrow{d_\nabla}
E
\xrightarrow{d_\nabla}
K=[R,C]
\xrightarrow{d_\nabla}
R\wedge E
\xrightarrow{d_\nabla}\cdots,
\qquad
d_\nabla R=0.
}
\]

**Level C — geometric completeness.**  Bây giờ hỏi full polarized data

\[
E(\cdot),
\qquad
K(\cdot,\cdot)
\]

có determine \(\nabla\) hay không.

Điểm này không được rút gọn thành “một snapshot \(E_u\) biết toàn background geometry”.  Vì \(K\) là two-form,

\[
K(u,u)=0.
\]

Một state snapshot và một differential geometry là hai loại data khác nhau.

### III.2. State-level bridge vẫn là nền móng

Trên fixed canonical formation core,

\[
\mathcal C_{NS}
=(\mathfrak g_\sigma,g,T,C),
\qquad
C=\operatorname{curl}.
\]

Koszul cho

\[
2g(\nabla_ab,c)
=g([a,b],c)-g([b,c],a)+g([c,a],b).
\]

Formation operator là

\[
\boxed{
\mathcal L_{\nu,u}
=\mathcal J_u-\nu C^2.
}
\]

Forward map tạo mother

\[
E_u=[\nabla_u,C].
\]

Principal symbol của mother đọc strain quadratic form

\[
q_u(x,n)=n^TS(u)(x)n,
\]

và spherical inversion reconstruct \(S(u)\), rồi

\[
\Delta u=2\operatorname{div}S(u)
\]

reconstruct \(u\) modulo Killing symmetry.

Do đó, khi background core đã fixed,

\[
\boxed{
E_u
\Longrightarrow
u
\Longrightarrow
\mathcal J_u
\Longrightarrow
\mathcal L_{\nu,u}.
}
\]

Đây là **transport/reconstruction of state over a known core**.  Campaign mới không thay thế kết quả này; nó hỏi liệu background core itself có recover từ differential signature hay không.

### III.3. Falsification nền tảng: signature coordinates không Euclideanize geometry

Ngay từ campaign đầu, một temptation rất tự nhiên là coi reduced signature coordinates như Euclidean coordinates.

Điều đó fail order one.

Metric đúng trên strain signature là

\[
\boxed{
\langle u,v\rangle_{L^2}
=
15\langle\Lambda^{-1}q_u,\Lambda^{-1}q_v\rangle,
}
\]

và

\[
\boxed{
\langle Cu,Cv\rangle_{L^2}
=
15\langle q_u,q_v\rangle.
}
\]

Nên

\[
\boxed{
 g^{\Sigma}_{\rm kinetic}=15\dot H^{-1},
\qquad
 g^{\Sigma}_{\rm Dirichlet}=15L^2,
\qquad
(g^{\Sigma}_{\rm kinetic})^{-1}g^{\Sigma}_{\rm Dirichlet}=\Lambda^2.
}
\]

Bài học này quay lại mạnh hơn trong geometric inverse: object đúng không phải raw matrices

\[
(C,E,K),
\]

mà là typed data

\[
\boxed{
(g_\Sigma,C,E,K).
}
\]

### III.4. Curl spectral reduction: connection tách thành phần thấy và phần mù

Take a typed spectral frame của self-adjoint signed curl \(C\).

Decompose metric connection

\[
\boxed{
\nabla=V+B,
\qquad
[V,C]=0.
}
\]

Ở đây:

- \(V\) chuyển động bên trong cùng curl eigensheet;
- \(B\) trộn giữa các eigensheets khác nhau.

Mother trở thành

\[
\boxed{
E=[B,C].
}
\]

Trên spectral blocks \(i,j\),

\[
E_{ij}
=(\lambda_j-\lambda_i)B_{ij}.
\]

Nếu \(\lambda_i\neq\lambda_j\),

\[
\boxed{
B_{ij}
=
\frac{E_{ij}}{\lambda_j-\lambda_i}.
}
\]

Nghĩa là degree one reconstruct **toàn cross-sheet connection**.

Phần còn thiếu chính xác là

\[
V\in\operatorname{comm}(C)\cap\mathfrak{so}.
\]

Đây là inverse problem thật sự của campaign III.

### III.5. Mother là orbit velocity, không phải eigenvalue drift

Với skew connection operator \(A=\nabla_u\), xét

\[
C(t)=e^{tA}Ce^{-tA}.
\]

Khi đó

\[
\dot C(0)=[A,C]=E_u.
\]

Eigenvalues của \(C(t)\) không đổi.

Do đó mother không đo “curl eigenvalues thay đổi bao nhiêu”.  Nó đo **spectral frame của curl bị formation connection xoay/mix như thế nào**.

Finite physical coordinate lab cho một scale picture rõ:

- skew connection dimension: \(378\);
- curl stabilizer dimension: \(62\);
- curl isospectral orbit tangent dimension: \(316\);
- physical state image rank: \(28\).

Vậy physical states chiếm một constrained distribution rất nhỏ bên trong full isospectral orbit tangent.

### III.6. Curvature split: Gauss/Ricci bên trong sheet, Codazzi giữa sheets

Formation curvature cũng tách

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0.
\]

Trong constant spectral-frame model,

\[
\boxed{
R_\parallel
=[V,V]+\Pi_\parallel[B,B].
}
\]

Ta có hai vertical curvature species:

1. \(\Pi_\parallel[B,B]\): within-sheet Gauss curvature induced bởi cross-sheet mixing, algebraically determined once \(B\) is known;
2. \([V,V]\): intrinsic stabilizer curvature từ within-sheet connection.

Cross-sheet sector \(R_\perp\) là Codazzi-like.

Curvature mother chỉ thấy

\[
\boxed{
K=[R,C]=[R_\perp,C].
}
\]

Vì vậy \(K\) không phải “toàn curvature”.  Nó là gap-weighted sensor của cross-sheet curvature.

Full physical helical Gauss/Codazzi tribunal kiểm decomposition này ở \(10^{-15}\)–\(10^{-13}\) scale.

### III.7. Cú mở mới: curvature có thể đo phần connection mà mother mù

Một khi \(E\) đã cho \(B\), câu hỏi còn lại là có recover được \(V\) hay không.

Trong exact finite metric-Lie / left-invariant torsion-free model, connection matrices viết

\[
\Gamma_i=B_i+V_i,
\qquad [V_i,C]=0.
\]

Curvature là

\[
R_{ij}
=[\Gamma_i,\Gamma_j]-\Gamma_{[e_i,e_j]}.
\]

Torsion-free bracket itself được sinh từ connection:

\[
[e_i,e_j]
=\Gamma_i e_j-\Gamma_j e_i.
\]

Bây giờ apply \([\cdot,C]\).

Pure quadratic vertical term

\[
[V_i,V_j]
\]

vẫn nằm trong curl stabilizer, nên bị commutator với \(C\) giết.

Các quadratic term mà vertical-generated bracket coefficient nhân một \(V\) khác cũng stabilizer-valued và bị giết.

Surviving terms chứa nhiều nhất một factor \(V\).

Do đó exact finite algebra cho

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V),
}
\]

với \(\mathcal A_{C,E}\) linear in hidden within-sheet connection.

Đây là **Codazzi observability map**.

Một reverse-engineering problem tưởng nonlinear bỗng thành một linear measurement system sau degree-one spectral reduction.

### III.8. Conditional reconstruction principle

Nếu

\[
\mathcal A_{C,E}
\]

injective modulo genuine stabilizer, thì

\[
E\Longrightarrow B,
\]

\[
K-K_B
=\mathcal A_{C,E}(V)
\Longrightarrow V,
\]

nên

\[
\boxed{
(g,C,E,K)\Longrightarrow\nabla.
}
\]

Sau đó torsion-free identity cho bracket:

\[
[u,v]=\nabla_uv-\nabla_vu.
\]

Từ bracket và metric có

\[
T(a,b,c)=\langle a,[b,c]\rangle,
\]

rồi reconstruct

\[
R,\qquad\mathcal J.
\]

Nếu \(\nu\) đã biết, formation operator là

\[
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2.
\]

Đây là exact **conditional** statement trong typed finite model.  Chưa có theorem rằng continuum NS Codazzi operator luôn/generically injective trên optimal function space.

### III.9. Exact Lie reconstruction tribunal: không chỉ fit tensor, mà rebuild cả dynamics

Tribunal đầu che hoàn toàn:

- bracket;
- \(T\);
- \(\nabla\);
- full curvature;
- Poisson operator.

Nó chỉ cho inverse biết

\[
g,C,E,K.
\]

Bốn exact Lie-algebra families được dùng:

\[
\mathfrak{so}(3)\oplus\mathfrak{so}(3),
\]

\[
\mathfrak{so}(3)\oplus\mathfrak h_3,
\]

\[
\mathfrak{so}(3)\oplus\mathfrak{se}(2),
\]

\[
\mathfrak h_3\oplus\mathfrak{se}(2),
\]

mỗi family randomize bằng non-bi-invariant metrics trên bốn seeds.

Kết quả:

\[
\boxed{16/16\text{ generic cases full rank}.}
\]

Affine-linearity residual:

\[
1.5\times10^{-16}	ext{--}2.5\times10^{-16}.
\]

Worst connection reconstruction error:

\[
\boxed{3.97\times10^{-15}}.
\]

Reconstructed connection sinh lại bracket, full curvature, \(\mathcal J\), \(\mathcal L\) ở roundoff scale.

Hai dynamics được integrate độc lập 80 RK4 steps; worst trajectory mismatch:

\[
\boxed{5.02\times10^{-16}}.
\]

Noise ladder \(10^{-10}\to10^{-4}\) cho slope

\[
\boxed{1.008}.
\]

Nghĩa là generic finite inverse vừa exact vừa linearly stable trong tested range.

### III.10. Physical helical tribunal: cố tình giấu một coefficient khỏi mother rồi lấy curvature tìm lại

Finite Lie result vẫn chưa đủ, vì arbitrary projection từng nói dối.

Nên campaign tạo một full physical Fourier/helical test.

Chọn transition

\[
q\longrightarrow q+p
\]

sao cho

\[
|q+p|=|q|
\]

và cùng helicity.

Input/output có cùng signed curl eigenvalue.  Do đó coefficient đó thuộc within-sheet connection và mother thấy chính xác zero trong channel này.

Sau đó thêm một Fourier direction khác để tạo cross-sheet curvature loop.

\(K\) recover hidden connection amplitude.

Trên 80 independent resonant triads:

\[
\boxed{
\text{median error}=9.56\times10^{-16},
}
\]

\[
\boxed{
\text{worst error}=3.51\times10^{-14}.
}
\]

Noise slope:

\[
\boxed{1.0004}.
\]

Đây là direct physical evidence mạnh nhất cho mechanism:

\[
\boxed{
E\text{ mù same-sheet coefficient, nhưng }K\text{ thấy nó qua cross-sheet holonomy.}
}
\]

### III.11. Falsification mới: \(E+K\) không universally complete

Nếu dừng sau successful generic tests, ta rất dễ overclaim

\[
(C,E,K)\Longrightarrow\nabla\quad\text{always}.
\]

Campaign cố tình phá statement này bằng phase diagram:

- 9 exact Lie-algebra families;
- 9 curl multiplicity patterns;
- 6 randomized metrics cho mỗi family/pattern.

Patterns chạy từ

\[
2+1+1+1+1
\]

qua

\[
2+2+2,\quad3+2+1,\quad3+3,\quad4+2,\quad5+1,
\]

và scalar control \(6\).

Trong 72 non-scalar family/pattern combinations,

\[
\boxed{68/72}
\]

full rank ở mọi tested seed.

Tất cả persistent failures tập trung tại

\[
\boxed{5+1}.
\]

Ví dụ degree-two nullities:

\[
2,\quad2,\quad11,\quad1.
\]

Do đó universal degree-two completeness bị falsify.

Correct picture phải là **stratified geometric observability**.

### III.12. Scalar curl là exact fully-dark negative control

Nếu

\[
C=\lambda I,
\]

thì

\[
E=[\nabla,C]=0,
\qquad
K=[R,C]=0.
\]

Toàn commutator spectral geometry collapse.

Trong six-dimensional controls,

\[
\boxed{90/90}
\]

hidden connection coefficients remain dark.

Điều này chứng minh geometric-completeness mechanism không phải một formal commutator trick.  Nó phụ thuộc essential vào nontrivial curl spectral separation.

### III.13. Higher covariant degrees là completion channels ở singular strata

Ở \(5+1\) failures, campaign không bỏ case xấu mà thêm đúng các degrees tiếp theo:

\[
K,\qquad dK,\qquad d^2K,\ldots
\]

Ba families có kernel

\[
2,\quad2,\quad1
\]

được degree three giết sạch:

\[
2\to0,\qquad2\to0,\qquad1\to0.
\]

Hardest family

\[
\mathfrak h_3\oplus\mathbb R^3
\]

cho

\[
\boxed{11\to9\to6}
\]

qua degrees two, three, four.

Đẩy tới maximal exterior tower trong base dimension six vẫn còn nullity six.

Bài học:

\[
\boxed{
\text{higher degree = additional observability on singular strata, not automatically a new physical mechanism.}
}
\]

### III.14. Falsification tiếp: Bianchi/Jacobi không tự động cứu uniqueness

Một hypothesis quá đẹp khác là:

> nếu \(K\) không đủ, cứ impose second Bianchi hoặc Jacobi thì uniqueness phải đóng.

Experiments không cho phép nói vậy.

Trong several \(5+1\) families, đúng là Bianchi hoặc Jacobi đóng kernel.

Nhưng hardest case cho:

\[
K:\ 11,
\]

\[
K+D R:\ 11,
\]

\[
K+\text{Jacobi}:\ 7.
\]

Stack maximal tower + Jacobi + Bianchi vẫn còn

\[
\boxed{5}
\]

linearized blind directions.

Vậy “Cartan integrability automatically gives full-rank inverse” cũng bị falsify.

### III.15. Cú tinh nhất: Jacobian kernel không phải finite darkness

Năm linearized blind directions còn lại có thể được gọi vội là “true gauge”.

Campaign không làm vậy.

Nó perturb finite theo direction \(w\) trong chính 5D kernel:

\[
V(t)=V_0+t w.
\]

Đo full maximal-tower + Jacobi sensor residual.

Across 2 seeds × 3 random directions, fitted log-log slopes đều bằng

\[
\boxed{2.0000000000}
\]

đến numerical precision.

Tức

\[
\boxed{
\|\mathcal S(V_0+tw)-\mathcal S(V_0)\|
\sim c(w)t^2.
}
\]

First derivative bằng zero, nhưng second-order data nhìn thấy direction.

Random finite sphere scans ở radii

\[
0.02,\ 0.05,\ 0.1,\ 0.2
\]

không tìm thấy machine-zero collision.

Đây không phải proof of nonlinear injectivity.  Nhưng nó giết một ngộ nhận quan trọng:

\[
\boxed{
\text{Jacobian kernel}\neq\text{proved gauge or finite non-uniqueness}.
}
\]

Một future theorem có thể cần stratified nonlinear inverse geometry, không chỉ inverse-function theorem uniform.

### III.16. 28D sparse stress test: information threshold gần dimension counting

Canonical 28D coordinate lab có curl multiplicities

\[
2,6,6,6,6,2.
\]

Sau degree one, số hidden within-sheet connection coefficients là

\[
\boxed{1736}.
\]

Không đưa full tensor \(K\) cho inverse.  Chỉ lấy random scalar curvature projections.

Với 12 projections per state pair:

- measurements: \(4536\);
- hidden coefficients: \(1736\);
- LSQR recovery error: \(2.75\times10^{-12}\);
- reconstructed \(\nabla,T,\mathcal J,\mathcal L\): khoảng \(4\times10^{-13}\);
- noise slope: \(1.0002\).

Measurement-density sweep cho:

\[
\begin{array}{c|c|c}
\text{projections/pair}&\text{equations}&\text{error}\\\hline
2&756&0.672\\
3&1134&0.508\\
4&1512&0.245\\
5&1890&4.4\times10^{-10}\\
6&2268&1.3\times10^{-10}
\end{array}
\]

Accuracy collapse đúng lúc equation count vừa vượt hidden dimension.

Đây là evidence rất mạnh rằng \(K\) đang cung cấp một genuine measurement system cho hidden connection.

Scope warning vẫn giữ: 28D projected object là coordinate stress lab, không phải faithful finite Lie category.

### III.17. Metric covariance: inverse geometry sống trên \(g_\Sigma\), không trên raw coordinates

Geometric inverse được randomize bằng non-orthogonal charts condition numbers

\[
1,\ 10,\ 100,\ 1000.
\]

Nếu decoder dùng transported metric \(G_\Sigma\), recovery errors là khoảng

\[
10^{-15},\quad10^{-15},\quad10^{-12},\quad10^{-8},
\]

theo numerical conditioning.

Nếu giả vờ signature coordinates có identity metric, errors jump lên

\[
0.20\text{--}0.53.
\]

Vậy campaign mới tái xác nhận bài học cổ nhất của Core 3:

\[
\boxed{
\text{complete coordinates do not erase the metric.}
}
\]

### III.18. Held-out spectral readers: inverse recover generator, không chỉ fit \(E,K\)

Một inverse có thể reproduce training tensors nhưng vẫn không recover đúng geometry.

Nên campaign fit **chỉ** \(E\) và \(K\), rồi bắt reconstructed connection predict unseen readers:

\[
[\nabla,C^2],
\qquad
[\nabla,C^3],
\qquad
[\nabla,e^{0.17C}],
\]

\[
[\nabla,\sin(0.4C)],
\qquad
[\nabla,|C|],
\]

hinge readers, shifted cuts,

\[
[R,f(C)],
\]

và held-out \(dK\).

Tất cả prediction errors ở khoảng

\[
\boxed{10^{-15}}.
\]

Negative control fit \(E\) alone miss một curvature reader tới

\[
\boxed{0.931}.
\]

Interpretation mạnh nhất:

> full-rank \(E+K\) inverse đang recover connection generator của tested curl functional calculus, không chỉ interpolate hai observed tensors.

### III.19. Shifted flag vẫn là tomography của cùng differential geometry

Với

\[
H_a=\operatorname{sgn}(C-aI),
\]

spectral layer cake cho

\[
\boxed{
\frac12\int_{\mathbb R}[R,H_a]\,da=[R,C].
}
\]

Do đó shifted cuts không tạo một species curvature khác.  Chúng tomograph cùng cross-sheet curvature mother.

Functional calculus cũng collapse về một mother:

\[
[R,f(C)]_{xy}
=f^{[1]}(x,y)[R,C]_{xy}.
\]

Campaign held-out reader confirm chính điều này sau reconstruction.

### III.20. Viscosity là boundary rõ của geometric completeness

Reversible differential geometry không biết \(\nu\).

Hai systems có cùng

\[
(g,C,E,K)
\]

nhưng khác viscosity có different formation operators.

Representative operator gap trong tribunal:

\[
\boxed{0.684}.
\]

Nhưng sau khi reconstruct reversible geometry, một generic observed time tangent đủ calibrate \(\nu\).

Noise slopes:

\[
1.02\text{--}1.04.
\]

Architecture rõ nhất hiện tại là

\[
\boxed{
\text{differential spectral geometry}
+
\nu
=
\text{full formation law}.
}
\]

Nếu \(\nu\) unknown, một generic dynamical calibration suffices trong finite tribunal.

### III.21. “Curved representation” phải hiểu đúng

Signature image là linear state image.  Nó có thể flat như một ordinary constant-metric vector subspace.

Curvature là curvature của **transported formation connection**.

Exact control từng cho:

- formation curvature norm \(\approx0.304\);
- transported match \(\sim7.8\times10^{-17}\);
- naive linear image curvature \(=0\).

Vậy câu đúng là

\[
\boxed{
\text{linear signature representation carrying curved formation geometry}.
}
\]

Không phải “signature embedding tự nó cong”.

### III.22. First-order commutant không phải final gauge; Jacobian kernel cũng chưa phải gauge

Degree one cho

\[
[V,C]=0
\]

nên \(V\) mother-dark.

Nhưng generic \(K\) reconstruct \(V\).

Do đó

\[
\operatorname{comm}(C)
\]

chỉ là first-order stabilizer.

Campaign III thêm một correction nữa: ngay cả nullspace của maximal **linearized** sensor map cũng chưa được gọi là gauge, vì finite perturbations có thể visible ở order two.

True gauge phải là exact finite stabilizer của full differential-spectral geometry trong đúng physical category.

Đây là một open classification problem liên quan đến holonomy/centralizer structure.

### III.23. Topology: \(\ker C\) vẫn không phải gauge

Một harmonic circulation có thể satisfy

\[
Cu=0
\]

nhưng

\[
E_u\neq0.
\]

Constant Galilean mode có thể both curl-zero và mother-dark.

Do đó

\[
\boxed{
\ker C\neq\ker(u\mapsto E_u)
}
\]

in general.

Future geometric-completeness theorem trên nontrivial topology phải giữ harmonic sector typed, không quotient \(\ker C\) mù quáng.

### III.24. Structural geometry không phải blow-up alarm

2D, Beltrami, shear controls đã falsify interpretation

\[
\|E\|\text{ lớn}
\quad\text{or}\quad
\|K\|\text{ lớn}
\Rightarrow
\text{danger}.
\]

Các harmless classes có thể ambiently curved.

Core 3 do đó không biến geometric completeness thành regularity theorem bằng ngôn ngữ.

Nếu sau này geometry này giúp regularity, cần một separate coercive/a-priori theorem.

### III.25. BCH Euler–heat descendants vẫn là object khác

Euler–heat BCH descendants và formation curl curvature cùng sinh từ parent core \((T,C)\), nhưng không đồng nhất.

Beltrami/shear controls cho BCH descendant zero trong khi \([R,C]\) nonzero.

Do đó

\[
\boxed{
\text{Euler–heat BCH defect}\neq[R,C].
}
\]

Unification phải qua common parent data, không qua rename descendants.

### III.26. Boundary extension vẫn là category change

Periodic theory dùng self-adjoint signed curl trong đúng \(L^2\) geometry.

Trên bounded domain, raw nonnormal curl analog làm reverse formulas fail order one, trong khi positive Stokes form vẫn survive.

Geometric-completeness theorem ở boundary vì vậy cần:

- operator/form domains;
- boundary trace pairing;
- Hodge harmonic sector;
- a correctly typed self-adjoint curl realization hoặc Hodge/Stokes replacement.

Không copy periodic syntax nguyên xi.

### III.27. Điều thực sự mới của Theory 2 sau campaign III

Theory 2 không còn được mô tả tốt nhất như một “signature of velocity”.

Hierarchy bây giờ là:

\[
\boxed{
\textbf{Level A: state completeness}
}
\]

\[
E_u\Longleftrightarrow u,
\]

rồi

\[
\boxed{
\textbf{Level B: differential curl geometry}
}
\]

\[
C\to E\to K\to dK\to\cdots,
\]

rồi generic tested finite geometry cho

\[
\boxed{
\textbf{Level C: formation-geometry reconstruction}
}
\]

\[
(g,C,E,K)
\Longrightarrow
\nabla,T,R,\mathcal J.
\]

Đây là lý do strongest current name được sharpen thành

\[
\boxed{
\textbf{Curl-Spectral Differential Observability of Formation Geometry.}
}
\]

Một phrase mạnh hơn, “Curl-Spectral Formation-Geometry Completeness”, nên dành cho theorem sau khi continuum injectivity/singular-strata analysis thật sự được đóng.

### III.27A. Regularity-frontier post-mortem: Theory 2 chỉ ra hai chìa khóa bị mất dấu

Campaign III làm một việc quan trọng hơn việc thêm một observer mới: nó cho phép đọc lại toàn bộ late regularity frontier bằng **complete spectral flag** thay vì bằng từng historical costume riêng lẻ.

Câu chuyện có ba pha.

#### Pha 1 — historical heat analysis thấy thiếu đúng một nửa đạo hàm

Forced hard-edge heat law có dạng

\[
(\partial_t+\nu\kappa_e)f_e=g_e,
\qquad
\kappa_e=P^2+M^2.
\]

Heat-fiber/Cauchy analysis của history cho thấy direct resultant endpoint cần

\[
G_{-1/2}
=\sum_e\kappa_e^{-1/2}|g_e|^2,
\]

trong khi generic edge estimate mới dừng ở

\[
G_{-1}.
\]

Endpoint \(\alpha=-1/2\) log-diverges.  Lúc đó cách đọc tự nhiên là: *còn thiếu nửa heat derivative*.

Theory 2 đổi cách đọc.  Với hard edge signed roots

\[
x=hP,
\qquad y=hM,
\qquad z=-hQ,
\]

moving selector

\[
\chi_a(e)
=\frac14(1-H_a(z)H_a(x))(1-H_a(z)H_a(y))
\]

có support length

\[
\boxed{
d_e=Q+\min(P,M).
}
\]

Và triangle closure cho

\[
\boxed{
\frac1{\sqrt2}\sqrt\kappa_e
\le d_e
\le\frac3{\sqrt2}\sqrt\kappa_e.
}
\]

Do đó

\[
\boxed{
\int_{\mathbb R}G_{-1}^{\rm flag}(a)\,da
\asymp
G_{-1/2}.
}
\]

Tức nửa đạo hàm không phải một supplier mới. Nó là **độ dài coarea của complete moving curl flag**. Trong deep high--high \(\to\) low, child-side \(Q/\sqrt\kappa\to0\), còn parent-side sweep tiến tới \(1/\sqrt2\). Zero cut đã bỏ mất đúng phần đó.

Ở operator level cùng statement là

\[
\boxed{
\frac14\int_{\mathbb R}\|[T,H_a]\|_{\rm edge}^2da
=\bigl\||\operatorname{ad}_C|^{1/2}T\bigr\|_{\rm edge}^2.
}
\]

Đây là chìa khóa thứ nhất: **missing half derivative = half derivative của spectral deformation trong operator space**.

#### Pha 2 — Theory 2/NEO giải mã static coherence thành A và B

Khi endpoint đã có đúng half-derivative geometry, câu hỏi chuyển sang: contraction có thể dùng coherence để trốn payment hay không?

Exact projective classification ép aligned equal-heat fibers về hai nontrivial geometries:

1. reflection/equal-\(\beta\), tiến về Beltrami equal-radius null và được radial variance khóa;
2. reciprocal-\(\beta\)/orthogonal-plane, phát actual companion sources.

Reciprocal branch sinh hai partition ratios

\[
A=\frac{G_{pp'}G_{mm'}}{G_{pm}G_{p'm'}},
\qquad
B=\frac{G_{pm'}G_{mp'}}{G_{pm}G_{p'm'}}.
\]

Exact rational certificate mới cho

\[
\boxed{
A^2+B^2\ge\frac3{32}\frac{R^2}{Q^2},
}
\]

và do

\[
|p-p'|\le\frac R{\sqrt2},
\]

suy ra sharp uniform lower bound

\[
\boxed{
\frac{Q\chi_{\rm geom}^2}{|p-p'|}
\ge\frac{\sqrt6}{8}.
}
\]

Đây là **Lemma A**: local reciprocal conductance không suy giảm ở deep fiber.

Sau đó exact symbolic elimination cho fixed companion role:

\[
\operatorname{Res}_w(F,G)
=4S^6L(S)\bigl[D(S-a)^2-E^2\bigr].
\]

Nonphysical \(L\)-branch bị loại; physical branch có đúng một radial root và nhiều nhất hai mirror children. Jacobian angular chỉ suy biến trên source-null faces.

Đây là **Lemma B**:

\[
\boxed{
\#\text{ reciprocal preimages per canonical companion role}\le2.
}
\]

A + B + diamond coarea

\[
 d\Xi=\frac{dp\,dp'\,d\mathcal H^2(y)}{16|p-p'|}
\]

để lại đúng

\[
\boxed{Q^{-1}}.
\]

Tức static reciprocal seam trước đây ghi là open đã được đóng ở aligned level.

#### Pha 3 — vì sao sau A+B vẫn bị kéo vào Codazzi/time-packing

Sau A+B, ta vô tình tiếp tục hỏi theo historical habit:

\[
\text{``làm sao bound }\Lambda^{-1}C_H\text{ hoặc làm Codazzi spike persist?''}
\]

Theory 2 cho thấy đây là cách đặt câu hỏi chưa đúng. Codazzi là covariant jet của cùng complete signature; square riêng nó làm mất tangent/normal coupling và dẫn lại đúng temporal-integrability deficit cũ.

Để thấy ổ khóa thật, xét equal-heat diamond defect

\[
\delta_\Diamond\eta
=\eta_p+\eta_m-\eta_{p'}-\eta_{m'},
\qquad
\eta_k=\frac{N_k}{a_k}.
\]

Momentum + equal heat giữ không chỉ affine invariants mà cả quadratic heat invariant:

\[
\boxed{
\eta_k=\alpha+\beta\cdot k+\gamma|k|^2
\quad\Longrightarrow\quad
\delta_\Diamond\eta=0.
}
\]

Vì vậy equal-heat collision kernel tự nhiên có năm directions

\[
\boxed{
1,\ k_x,\ k_y,\ k_z,\ |k|^2.
}
\]

Finite-lattice complete relation audits tại \(K=1,2,3\) cho nullity đúng \(5\), không thấy extra UV soft mode. Chìa khóa bị thiếu không phải một graph eigenvector bí ẩn: **mode thứ năm chính là heat**.

Physical logarithmic rate là

\[
\boxed{
r_k=\frac{\dot a_k}{a_k}=\eta_k-\nu|k|^2.
}
\]

Với arbitrary same-output pair, parabolic defect

\[
\boxed{
\Delta_\Diamond^\nu\eta
=\eta_p+\eta_m-\eta_{p'}-\eta_{m'}
-\nu(\kappa-\kappa')
}
\]

thỏa identically

\[
\boxed{
\Delta_\Diamond^\nu\eta
=r_p+r_m-r_{p'}-r_{m'}.
}
\]

Do đó late problem có đúng split mà complete Theory 2 đòi hỏi:

\[
\boxed{
\text{A+B / projective geometry = tangent coercivity trên equal-heat fibers},
}
\]

\[
\boxed{
-\nu C^2 = normal heat calibration.
}
\]

Hai phần này phải được ghép như một hypocoercive system; không phần nào là một wallet mới.

#### Chìa khóa cuối thực sự: Polar--Korn cross term

Mother completeness đã cho exact Korn observability cho mọi tangent vector \(v\):

\[
\boxed{
2\|S(v)\|_{\dot H^s}^2
=\|v\|_{\dot H^{s+1}}^2.
}
\]

Vậy observability không còn thiếu. A+B cũng đã cho static tangent geometry; \(\nu C^2\) cho distinguished normal direction.

Exact radial--Jordan--Codazzi acceleration law lại có sẵn square đúng dấu:

\[
\boxed{
EQ'-\frac E2\ddot{\mathcal R}_0-W_\Lambda^2
=\mathcal U\bigl(\langle\Lambda u,Z_{\rm Cod}\rangle+\mathcal C_{compat}\bigr).
}
\]

Và finite singular endpoint bắt

\[
\boxed{
\int^{T_*}\mathfrak v\,dt=\infty,
\qquad
\mathfrak v=\frac{W_\Lambda^2}{\mathcal U}.
}
\]

Điều còn thiếu vì vậy không nên là

\[
\int\|\Lambda^{-1}Z_{\rm Cod}\|_2^2dt<\infty.
\]

Target đúng là tìm một **modified hypocoercive energy** \(\mathscr E_{\rm T2}\), có cross term giữa angular/equal-heat coordinate và radial/heat coordinate, sao cho

\[
\boxed{
\frac d{dt}\mathscr E_{\rm T2}
+c\frac{W_\Lambda^2}{\mathcal U}
\le
\text{genuine viscous / already-owned terms}.
}
\]

Nếu có inequality này, visibility speed trở thành time-integrable và mâu thuẫn endpoint xảy ra trực tiếp. Codazzi lúc đó là coupling term được absorb/cancel trong modified energy, không phải một source norm cần square độc lập.

Đây là **chìa khóa thứ hai**:

\[
\boxed{
\textbf{A+B reciprocal conductance/finite-incidence control}
+\textbf{ heat fifth-mode calibration}
+\textbf{ hypocoercive Polar--Korn cross term}.
}
\]

Status phải giữ chính xác:

- moving-flag half derivative: **EXACT**;
- reciprocal Lemma A: **CERTIFIED**;
- reciprocal Lemma B: **EXACT SYMBOLIC**;
- equal-heat five-dimensional kernel: four+heat invariants **EXACT**, no-extra-kernel for tested boxes **AUDIT**;
- mother Korn observability: **EXACT**;
- hypocoercive Polar--Korn modified-energy inequality: **OPEN**;
- global 3D regularity: **OPEN**.

Canonical late-frontier note và executable certificates nằm tại [From the Missing Half Derivative to the Polar--Korn Target](core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md).

### III.28. Candidate theorem bây giờ đã đủ precise để tấn công

Open theorem target là định nghĩa continuum Codazzi observability operator

\[
\boxed{
\mathcal A_{C,E}:
\Omega^1(\mathfrak h_C)
\to
\Omega^2(\mathfrak m_C)
}
\]

trên đúng periodic Sobolev/Fréchet scale, rồi prove một statement dạng

\[
\boxed{
(g_\Sigma,C,E,K,\text{finite higher jets if needed})
\Longrightarrow
\nabla
\quad\text{modulo true differential-spectral stabilizer}.
}
\]

Các hard pieces đã hiện rất rõ:

1. unbounded operator domains của \(C\), \(\nabla\), commutators;
2. rigorous \(\operatorname{ad}_C^{-1}\) off the commutant;
3. Fredholm/injectivity analysis của \(\mathcal A_{C,E}\);
4. high shell multiplicity và singular spectral strata;
5. nonlinear injectivity khi Jacobian singular;
6. exact true stabilizer/holonomy centralizer;
7. topology/harmonic modes;
8. boundary Hodge/Stokes typing;
9. viscosity as a separate scalar calibration.

Đây là một theorem programme cụ thể, không còn là “tìm thêm mechanism”.

### III.29. Canonical falsification rules từ ba campaign

Core 3 bây giờ giữ các rules sau như một phần của methodology:

1. Complete coordinates không được Euclideanize nếu transported metric không cho phép.
2. Naive operator commutator không được dùng thay induced curved bracket.
3. Snapshot completeness không được promoted thành arbitrary-core identifiability.
4. Galerkin projection không được dùng làm proof của higher Lie geometry nếu Jacobi fail.
5. `comm(C)` không được gọi final gauge từ degree one.
6. \(\ker C\) không được quotient thành gauge trên topology tổng quát.
7. Higher tower không được gọi “new physics” chỉ vì nó có degree cao hơn.
8. Bianchi/Jacobi không được assumed to imply uniqueness without rank test.
9. Jacobian kernel không được gọi true darkness nếu chưa có finite nonlinear collision test.
10. Nonzero curvature không được gọi danger/blow-up amplitude nếu chưa có regularity theorem.
11. Reconstruction phải predict held-out readers/trajectories, không chỉ fitted tensors.
12. Generic reconstruction claim phải bị stress bằng high spectral degeneracy trước khi canonicalize.

### III.30. Reproduction map cho Core 3 mới

New central reconstruction tribunals:

```bash
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

Chúng phải được đọc cùng original state/metric/curvature tribunals, đặc biệt:

```bash
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/full_physical_gauss_codazzi.py
python core/curved_formation_signature/audits/representation_curvature_not_embedding_curvature.py
python core/curved_formation_signature/audits/harmless_class_curvature.py
python core/curved_formation_signature/audits/boundary_metric_typing.py
```

Strongest current conclusion của Mục III là:

\[
\boxed{
\begin{aligned}
&\text{Theory 2 theoremically identifies state on the canonical periodic core;}\\
&\text{its full differential signature carries curl-spectral formation geometry;}\\
&\text{curvature generically resolves first-order spectral blindness;}\\
&\text{and the tested finite/physical evidence supports formation-geometry reconstruction}\\
&\text{away from, and with stratified treatment of, high-symmetry spectral singularities.}
\end{aligned}
}
\]

Đây vẫn chưa phải global regularity theorem, và chưa phải completed infinite-dimensional geometric-completeness theorem.  Nhưng Core 3 không còn chỉ là một bridge giữa hai representations: nó đã trở thành một explicit inverse geometry programme.

### III.31. Campaign IV: câu hỏi mới không còn là “reconstruct connection”

Campaign III dùng polarized differential data để hỏi

\[
(g,C,E,K)\rightsquigarrow\nabla?
\]

Campaign IV cố tình lấy ít data hơn.

Fix một generic state \(u_*\) và chỉ giữ

\[
\boxed{
C,
\qquad
E_{u_*}=[\nabla_{u_*},C].
}
\]

Câu hỏi là:

> một generic state mother có mang theo state-independent **syntax của interaction law** mà state đó thuộc vào hay không?

Đây là inverse problem khác geometric completeness.  Nó hỏi về **presentation/category**, không hỏi toàn coefficients của connection.

### III.32. Hai operator letters nổ thành full observable algebra

Trong canonical 28D physical spectral lab,

\[
\dim\operatorname{Alg}(C)=6.
\]

Nhưng với một generic mother,

\[
\boxed{
\dim\operatorname{Alg}(C,E_u)=784=28^2.
}
\]

Noncommutative word span tăng theo

\[
\boxed{
1,3,7,15,31,63,125,246,483,784.
}
\]

Hai generators không thể span \(784\) directions trước depth \(9\), vì

\[
2^9-1=511<784<1023=2^{10}-1.
\]

Observed saturation xảy ra đúng tại

\[
\boxed{L=9},
\]

là information-theoretic minimum depth.

Independent SVD trên toàn \(1023\) words xác nhận rank \(784/784\) trên nhiều generic states.

Đồng thời common commutant collapse

\[
\boxed{
152\to1.
}
\]

Tức một generic mother phá toàn nontrivial linear symmetry commuting with curl trong tested 28D representation.

### III.33. Falsification: graph connected chưa đủ

Một explanation quá đơn giản là:

\[
\text{connected curl-sheet graph}
\Rightarrow
\text{full operator algebra}.
\]

Sai.

Với curl multiplicities

\[
(2,6,6,6,6,2),
\]

all \(1296\) connected labeled trees vẫn giữ nontrivial commutant.

Complete graph với rank-one block maps vẫn còn commutant dimension

\[
45.
\]

Generic rich block maps mới nhanh chóng collapse về scalar identity.

Vì vậy theorem target đúng hơn là

\[
\boxed{
\text{spectral connectivity}
+
\text{inter-sheet channel richness}
\Rightarrow
\text{irreducibility}.
}
\]

### III.34. First relations: curl law và derivative của curl law

Base window có signed roots

\[
\{\pm1,\pm\sqrt2,\pm\sqrt3\}.
\]

Do đó exact finite spectral relation là

\[
\boxed{
p(C)=0,
\qquad
p(x)=(x^2-1)(x^2-2)(x^2-3).
}
\]

Hay

\[
C^6-6C^4+11C^2-6I=0.
\]

Vì

\[
E=[A,C],
\]

commute relation trên với \(A\) cho

\[
\boxed{Dp_C(E)=0.}
\]

At word degree \(6\), có \(127\) formal words nhưng rank \(125\).  Numerical nullspace đúng 2D, và two theoretical relations \(p(C),Dp_C(E)\) span toàn nullspace với principal cosines

\[
\boxed{1,1}.
\]

### III.35. Relation thứ ba là physical interaction law

At degree \(7\), ngoài spectral ideal xuất hiện đúng một state-independent relation mới.

Blind extraction và root-incidence analysis cho closed form

\[
\boxed{
Q(C,E)
=(C^2-I)(C^2E+EC^2-5E)(C^2-I)=0.
}
\]

Nó encode base-window interaction selection:

\[
-\sqrt3\leftrightarrow+\sqrt3,
\qquad
-\sqrt2\leftrightarrow+\sqrt2
\]

là forbidden, còn \(-1\leftrightarrow+1\) vẫn allowed.

Pure root/multiplicity calculation không suy ra relation này.  Same-spectrum generic off-block control cũng không có nó.

Vì vậy

\[
\boxed{
Q\text{ records physical interaction incidence, not spectrum alone.}
}
\]

### III.36. Ba laws sinh toàn pre-saturation presentation

Ba state-independent laws

\[
\boxed{
p(C)=0,\qquad Dp_C(E)=0,\qquad Q(C,E)=0}
\]

không chỉ giải thích vài identity riêng lẻ.

Across four generic physical states, two-sided ideal của chúng match **toàn numerical relation space**:

\[
\begin{array}{c|c|c}
\text{degree}&\text{numerical nullity}&\text{three-law ideal rank}\\
\hline
6&2&2\\
7&9&9\\
8&28&28
\end{array}
\]

Không còn hidden relation trước degree \(9\).

At degree \(9\), word algebra hit finite ceiling

\[
\dim M_{28}=784,
\]

nên finite-representation capacity bắt đầu sinh nhiều relations mới.

Do đó finite-window evidence support một presentation dạng

\[
\boxed{
\mathcal A_{\rm window}
\approx
\langle C,E\mid p(C),Dp_C(E),Q(C,E)\rangle
}
\]

trước saturation.

### III.37. One-snapshot law archaeology và rival-theory identification

Cho algorithm chỉ

\[
C,E_{u_*}
\]

của một generic state.

Không cho full mother one-form, connection, bracket, Fourier graph hay forbidden-edge list.

Relation learned từ một state transfer sang \(200\) unseen physical mother states ở machine precision.

Toàn degree-8 relation subspace learned từ one state transfer sang \(80\) unseen physical states với minimum principal cosine

\[
\boxed{0.9999999999999991}.
\]

Sau quotient common spectral relations, physical-specific subspace reject same-spectrum generic off-block law với separation

\[
\boxed{5.98\times10^8}.
\]

Relation-only classifier còn distinguish đúng:

- all three same-spectrum same-forbidden-count physical rivals;
- an independent eight-law same-spectrum stress family.

Tức snapshot fingerprint có thể identify **which interaction law**, không chỉ number of missing channels.

### III.38. Exact-helical law holography

Các effects trên không chỉ sống trong projected finite bracket.

Exact complex helical mother restricted to base window satisfies

\[
p(C)=0,
\qquad
Dp_C(E)=0,
\qquad
Q(C,E)=0
\]

với normalized residuals khoảng

\[
10^{-19}\text{--}10^{-21}.
\]

Ở exact \(|k|^2\le6\) window:

\[
160\text{ helical nodes},
\qquad
12\text{ signed curl roots},
\]

whole support category dùng \(13\) independent support representatives.

Nhưng generic state chỉ support trên

\[
\boxed{
(0,0,1),
\quad
(0,1,-1),
\quad
(1,-1,-1)
}
\]

đã recover complete root-level interaction category và degree-16 physical quotient relation.

Relation cosine bằng essentially \(1\), và all \(12\) forbidden root channels được recover với minimum separation \(1.53\times10^9\).

### III.39. Scale tăng, law phức tạp hơn nhưng three-direction illumination vẫn sống

Cùng fixed three support directions được tested trên exact helical windows:

\[
52,64,112,160,184,244,292,356,500,512
\]

nodes.

At largest tested window:

\[
28\text{ signed curl roots},
\qquad
432\text{ active channels},
\qquad
324\text{ forbidden channels}.
\]

Vẫn có

\[
\boxed{
\text{missing}=0,
\qquad
\text{extra}=0.
}
\]

trong root-level category recovered by the same three-direction generic state.

Presentation degree tăng với scale, nên law không trivialize.  Nhưng tested support complexity để illuminate law vẫn bounded by three.

Đây là current **law-holography** phenomenon.

### III.40. Projective consistency của spectral windows

Interaction categories được compare dưới refinements

\[
3\to4\to5\to6\to8\to9\to10\to12\to14\to16.
\]

Ở every step, restrict larger-window law xuống old signed curl roots cho

\[
\boxed{
\text{old edges added}=0,
\qquad
\text{old edges lost}=0.
}
\]

Chỉ new roots mang new channels/relations vào.

Điều này chưa prove continuum inverse limit, nhưng nó là evidence đầu tiên rằng finite-window presentations có thể organize thành một coherent projective family.

### III.41. Falsification quyết định: one snapshot không reconstruct full polarized geometry

Version quá mạnh

\[
(C,E_u)
\Longrightarrow
\text{full formation geometry}
\]

bị giết trực tiếp.

Hai distinct metric-compatible connection one-forms được construct sao cho training

\[
(C,E_{u_*},\nabla_{u_*})
\]

match tới machine precision và share same tested presentation category.

Nhưng unseen directions có

\[
\text{mother median difference}=17.2\%,
\qquad
\text{max}=53.7\%,
\]

và

\[
\text{connection median difference}=22.4\%,
\qquad
\text{max}=75.7\%.
\]

Vậy canonical boundary là

\[
\boxed{
\text{snapshot}\rightsquigarrow\text{syntax/category},
\qquad
\text{not full polarized coefficients}.
}
\]

### III.42. Curvature là geometry calibration beyond snapshot

Snapshot collision được refine thành continuous one-parameter family \(\nabla^{(\delta)}\) có same training snapshot.

Một generic scalar curvature polarization

\[
\langle z,K^{(\delta)}(u_*,v)w\rangle
\]

recover hidden parameter trong

\[
\boxed{80/80}
\]

trials.

Median error

\[
9.1\times10^{-15},
\]

worst error

\[
4.1\times10^{-13},
\]

noise slope

\[
\boxed{0.995}.
\]

Đây nối Campaign IV trở lại Campaign III cực sạch:

\[
\boxed{
\text{mother snapshot}\Rightarrow\text{law syntax},
\qquad
\text{curvature polarization}\Rightarrow\text{geometry calibration}.
}
\]

### III.43. Core-3 hierarchy sau Campaign IV

Core 3 hiện có bốn levels:

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

Strongest candidate wording cho level mới là

\[
\boxed{
\textbf{Curl--Mother Presentation Bootstrap}.
}
\]

Nhưng câu “one snapshot knows the whole theory” là false.

Câu sống sót mạnh hơn về cấu trúc là:

> một generic mother snapshot có thể mang state-independent syntax của physical interaction category, trong khi polarized \(E,K\) determine geometric realization cụ thể của syntax đó.

### III.44. Reproduction map cho Campaign IV

Complete presentation-bootstrap suite:

```bash
python core/curved_formation_signature/run_presentation_bootstrap_audits.py
```

Runner này execute \(39\) tribunals canonicalized dưới

```text
research/theory2_universal_compiler/audits/
```

bao gồm full-algebra generation, SVD robustness, relation extraction, three-law presentation closure, same-spectrum rival theories, exact-helical law holography, projective window consistency, noise breakdown, nonorthogonal covariance, snapshot impossibility và one-curvature-scalar calibration.

## IV. Cấu trúc corpus trên main

Corpus canonical hiện tại có ba tầng mathematical core và một methodology/workbench:

```text
Core_signature.md
README.md
core/
├── NEO/
│   ├── NEO_ANCHOR_COMPILER.md
│   └── NEO_DISCOVERY_WORKBENCH.md
├── metric_lie_hodge/
│   ├── README.md
│   ├── FORMATION_LAW.md
│   ├── COMPATIBILITY_GEOMETRY.md
│   └── audits/
├── spectral_signature/
│   ├── README.md
│   ├── SPECTRAL_FLAG_SIGNATURE.md
│   ├── SPECTRAL_FLAG_COMPLETENESS.md
│   ├── MOTHER_COMPLETENESS_THEOREM.md
│   ├── HISTORY_AND_FALSIFICATION.md
│   └── audits/
└── curved_formation_signature/
    ├── README.md
    ├── GEOMETRIC_COMPLETENESS.md
    ├── PRESENTATION_BOOTSTRAP.md
    ├── run_presentation_bootstrap_audits.py
    ├── CURL_SPECTRAL_REDUCTION.md
    ├── FORMATION_SIGNATURE_EQUIVALENCE.md
    ├── CURVED_CURL_MODULE.md
    ├── SIGNATURE_METRIC_DYNAMICS.md
    ├── PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md
    ├── DEEP_GEOMETRY_LESSONS.md
    ├── THEOREM_STATUS_AND_SCOPE.md
    ├── HISTORY_AND_FALSIFICATION.md
    └── audits/
research/
└── theory2_universal_compiler/
    ├── THEORY2_SELF_DESCRIBING_ALGEBRA_LAB.md
    └── audits/
```

Vai trò từng core:

1. `metric_lie_hodge/`: **formation core** — metric, Lie tensor, signed curl/Hodge data và formation operator.
2. `spectral_signature/`: **state completeness core** — mother/shifted flag, reverse compiler và quantitative state reconstruction.
3. `curved_formation_signature/`: **differential observability + presentation core** — transport giữa hai parent cores, curl-spectral reduction, curvature/holonomy, Codazzi reconstruction candidate, singular spectral strata, higher/nonlinear completion và Campaign-IV generator--relations bootstrap.
4. `research/theory2_universal_compiler/`: executable Campaign-IV tribunal corpus referenced canonically by Core 3.
5. `NEO/`: methodology/workbench — giữ riêng khỏi theorem subject.

Discovery worktrees, failed mechanisms và proof programmes cũ không được copy wholesale vào `core/`; Git history và `history/` giữ archaeology.  Canonical core chỉ giữ theory, scope corrections và executable tribunals cần để reproduce current claims.

## V. Reproduction checklist

### V.1. Formation parent core

```bash
python core/metric_lie_hodge/audits/formation_core_audit.py
python core/metric_lie_hodge/audits/bch_core_audit.py
python core/metric_lie_hodge/audits/domain_topology_audit.py
```

### V.2. Spectral-signature parent core

```bash
python core/spectral_signature/audits/spectral_flag_signature.py
python core/spectral_signature/audits/spectral_flag_completeness.py
python core/spectral_signature/audits/mother_completeness_theorem.py
```

### V.3. Core 3 — state bridge / physical geometry

```bash
python core/curved_formation_signature/audits/metric_lie_spectral_unification.py
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_core_identifiability.py
python core/curved_formation_signature/audits/physical_axiom_rigidity.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/physical_curvature_flag_tomography.py
python core/curved_formation_signature/audits/full_physical_gauss_codazzi.py
```

### V.4. Core 3 — geometric-completeness campaign

```bash
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

### V.5. Core 3 — presentation-bootstrap campaign

```bash
python core/curved_formation_signature/run_presentation_bootstrap_audits.py
```

Runner này execute toàn \(39\) Campaign-IV audits trong `research/theory2_universal_compiler/audits/`.

Negative controls are part of the suite, not failures to be removed.  In particular:

- scalar curl must remain fully dark;
- high-degeneracy \(5+1\) cases must expose rank loss;
- Bianchi/Jacobi must **not** be reported as universal uniqueness mechanisms;
- the five-dimensional linearized hardest-case kernel must remain quadratically visible rather than being mislabeled as exact gauge;
- Euclideanizing a non-orthogonal signature chart must fail;
- \(E\)-only held-out curvature prediction must fail by order one;
- one snapshot must **not** determine the full polarized mother/connection one-form;
- the base-window selection polynomial must fail on larger windows;
- connected low-rank block graphs must retain nontrivial symmetry;
- high enough noise must eventually break law classification rather than being hidden.

## VI. Trạng thái claim

Repository hiện có hai theorem-level parent achievements và một stronger synthesis layer với hai distinct candidate inverse levels: formation-geometry observability và presentation bootstrap.

### VI.1. Theorem-level state statement

Trên smooth mean-zero divergence-free periodic state space,

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

Đây là whole-state completeness/conjugacy statement của parent spectral-signature theory.

### VI.2. Exact Core-3 differential identities

Core 3 exact layer gồm

\[
E=d_\nabla C,
\qquad
K=d_\nabla E=[R,C],
\qquad
d_\nabla K=R\wedge E,
\qquad
d_\nabla R=0,
\]

cùng curl spectral splitting

\[
\nabla=V+B,
\qquad
[V,C]=0,
\qquad
E=[B,C].
\]

Trong exact finite metric-Lie setting, after \(B\) is recovered from \(E\), curvature mother satisfies

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V)
}
\]

với \(\mathcal A_{C,E}\) linear in hidden stabilizer connection.

Nếu \(\mathcal A_{C,E}\) injective modulo true stabilizer, reconstruction

\[
(g,C,E,K)\Longrightarrow\nabla,T,R,\mathcal J
\]

là exact conditional implication.

### VI.3. Candidate continuum statement

Executable campaign supports mạnh rằng generic tested spectral strata are degree-two observable, while highly degenerate strata form singular inverse geometry where higher/nonlinear data matter.

Nhưng repository **chưa** theoremize:

\[
(g_\Sigma,C,E,K,\ldots)
\Longrightarrow
\nabla
\]

trên full infinite-dimensional NS Sobolev/Fréchet category.

Open pieces include continuum Codazzi injectivity/Fredholm theory, shell multiplicity strata, nonlinear singular observability, true stabilizer/holonomy centralizer, operator domains, topology and boundary Hodge typing.

### VI.4. Campaign-IV presentation statement

Finite/exact-helical tribunals support một level inverse khác:

\[
\boxed{
(C,E_{u_*})
\rightsquigarrow
\text{operator syntax / relation ideal / interaction category}.
}
\]

Base-window evidence cho two-generator algebra saturation

\[
\operatorname{Alg}(C,E_u)=M_{28}
\]

trong generic tested states, và three-law pre-saturation presentation

\[
\langle C,E\mid p(C),Dp_C(E),Q(C,E)\rangle.
\]

Exact-helical multi-window tribunals support sparse law holography và projective consistency của root-level interaction categories.

Nhưng repository cũng có exact experimental counterexample to

\[
(C,E_u)\Rightarrow\text{full polarized geometry}.
\]

Do đó canonical split là

\[
\boxed{
\text{snapshot}\Rightarrow\text{syntax/category},
\qquad
\text{polarized }E,K\Rightarrow\text{geometry coefficients}.
}
\]

No continuum presentation theorem or inverse-limit theorem is claimed.

### VI.5. Viscosity and regularity nonclaims

Reversible differential geometry does not determine \(\nu\); one extra scalar dynamical calibration is required when viscosity is not already given.

None of the above is a global regularity theorem.  Core 3 does not claim that nonzero \(E\), \(K\), \(R\), or any finite tower norm characterizes blow-up.  2D, shear and Beltrami controls explicitly forbid that shortcut.

Strongest current sentence is therefore:

\[
\boxed{
\textbf{Theory 2 is state-complete; its polarized differential signature is a strongly supported stratified observability geometry, while a generic mother snapshot is experimentally supported as a finite spectral presentation bootstrap for the physical interaction category.}
}
\]
