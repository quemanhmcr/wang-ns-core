# 01 — Theory-2 realtime doctrine

## 1. Thế nào là bị lạc trong Navier--Stokes?

Historical loop có dạng

\[
X_0\to X_1\to X_2\to\cdots
\]

với mỗi `X_j` được đặt tên như một mechanism mới chỉ vì quantity trước chưa bound được.

Ví dụ template sai:

\[
\text{traffic khó}
\Rightarrow
\text{differentiate traffic}
\Rightarrow
\text{Codazzi}
\Rightarrow
\text{differentiate Codazzi}
\Rightarrow
\text{next mother}
\Rightarrow\cdots
\]

Điều nguy hiểm là mỗi identity có thể đúng, nhưng proof không giảm physical freedom.

## 2. Realtime compiler

Mỗi apparent obstruction mới phải qua sáu câu hỏi trước khi được phép tồn tại độc lập.

### (i) Parentage

Nó là primitive, mother, second mother, hay chỉ renderer/contraction?

Nếu renderer: compile ngược, không mở branch mới.

### (ii) Kernel

Nếu defect bằng zero, dangerous dynamics còn sống không?

Nếu có, defect chưa phải final coordinate.

### (iii) Owner

Quantity này có finite action từ một physical law đã chứng minh không?

Nếu không: không được gọi nó là budget.

### (iv) Scaling

Proposed estimate có đúng NS critical scaling không?

Sai scaling => sai theorem type.

### (v) Completeness

Apparent disappearance có thể chỉ là activity chuyển sang coordinate khác của complete signature không?

Nếu có: nâng về complete state.

### (vi) Stop test

Differentiate tiếp có tạo physics mới hay chỉ next mother của cùng obstruction?

Nếu chỉ next mother: **STOP**.

## 3. Realtime stop rule ở final door

Từ thời điểm current handoff:

\[
\boxed{\text{Không phát minh observer mới.}}
\]
\[
\boxed{\text{Không differentiate rate defect để tìm next owner.}}
\]
\[
\boxed{\text{Không gọi companion/source-square là dissipation mới.}}
\]

Chỉ hai loại bước được chấp nhận:

1. **coercivity:** dùng chính A+B/flag/heat/kinetic owners để bound current projective rate;
2. **rigidity:** nếu coercivity degenerates, prove state tiến vào exact terminal kernel.

Nếu một bước không thuộc hai loại này, nó phải được xem là khả năng quay lại loop.

## 4. Vì sao complete signature thay đổi cách chơi?

Một scalar reader

\[
u\mapsto X(u)
\]

mất phase/polarization/migration information.

Theory 2 giữ operator-valued family

\[
\Sigma(u)=\{\mathscr O_a(u)\}_{a\in\mathbb R},
\]

nên NS không còn có thể “escape” chỉ bằng cách chuyển activity giữa zero cut, shifted cut, helicity sheet hay radial location.  Escape thật phải là **noncompact motion của complete state**.

Đây là lý do proof programme cuối chuyển từ “find a better criterion” sang “classify/kill the only admissible complete-state noncompact rate defect”.
