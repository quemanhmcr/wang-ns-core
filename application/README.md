# Application layer

`application/` là lớp **dùng core để tấn công một bài toán cụ thể**.  Khác với `core/`, thư mục này được phép chọn một endpoint, một normalization và một contradiction architecture; nhưng mọi object mới phải compile ngược về các primitive đã có trong core trước khi được dùng.

Nguyên tắc bắt buộc:

1. `core/` định nghĩa ontology và exact identities;
2. `application/` chỉ tổ chức chúng thành proof programme;
3. một quantity trong application không được tự phong thành source/budget mới;
4. mọi claim phải gắn nhãn `EXACT`, `DEDUCTION`, `OPEN`, hoặc `AUDIT`;
5. nếu một bước sinh ra một uncontrolled descendant mới thay vì xử lý obstruction hiện tại, proof programme đã quay lại historical loop.

Hiện tại:

- [clay_problem/](clay_problem/) chứa các application hướng tới Clay Millennium problems;
- [clay_problem/theory2_realtime_endgame/](clay_problem/theory2_realtime_endgame/) là handoff đầy đủ cho Theory-2 realtime Navier--Stokes endgame.
- [clay_problem/theory2_interaction_frame/](clay_problem/theory2_interaction_frame/) là spine blow-up theorem-first: complete Theory-2 state + anchored interaction frame + moving heat geometry + critical monodromy frontier.
