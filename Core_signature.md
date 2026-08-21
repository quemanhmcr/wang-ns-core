# Core Signature

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

## III. Cấu trúc corpus trên main

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

## IV. Reproduction checklist

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

## V. Trạng thái claim

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
