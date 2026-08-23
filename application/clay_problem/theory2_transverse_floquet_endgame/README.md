# Theory-2 Transverse Floquet Endgame

## Purpose

Folder này ghi lại **toàn bộ proof chain mới nhất của Theory-2 / NEO Navier–Stokes**, từ các exact equivalence đầu tiên cho tới frontier hiện tại: finite-viscosity normalized recurrence được reduce thành một **transverse Floquet fixed-point problem**, và stationary finite-`κ` branch tiếp tục được reduce thành một **common-ray Poisson-depth rigidity problem driven by `T`**.

Mục tiêu của dossier là giữ một record có thể audit được, theorem-first, không trộn lẫn:

- structural completeness của Theory-2;
- actual-state observability;
- incidence / triad / companion identities;
- finite-viscosity coercive results;
- terminal scaling và normalized recurrence;
- transverse Floquet reduction;
- all-positive-Poisson-depth stationary ray laws;
- những no-go theorem đã loại các shortcut;
- và đúng analytic arrow vẫn còn **OPEN**.

> **Không có claim Navier–Stokes regularity / Clay problem đã được giải.**
>
> Exact reductions dưới đây thu hẹp obstruction xuống nonlinear self-consistency của transverse Formation source `T`, nhưng theorem cuối chưa đóng.

---

## Governing doctrine

> Keep the complete Theory-2 state all the way through.  
> Contract only at the exact estimate that genuinely needs a scalar reader.

Không quay lại historical scalar traffic/source/Fisher/Codazzi architectures như independent ontologies. Chúng chỉ được dùng nếu cần để chỉ ra một shortcut là tautological hoặc false.

---

## Ledger convention

Mỗi kết quả quan trọng được gắn một trong bốn nhãn:

- **EXACT** — chứng minh đại số / spectral / Fourier trực tiếp từ stated Theory-2 identities.
- **DEDUCTION** — suy ra từ exact identities + compactness / continuity / profile hypotheses được ghi rõ.
- **AUDIT** — finite-dimensional, scaling, hoặc hostile model evidence; không được dùng như PDE theorem.
- **OPEN** — analytic arrow chưa proved.

---

## File map

1. `00_STATUS_SCOPE_AND_LEDGER.md` — status hiện tại, nonclaims, final frontier.
2. `01_CORE_THEORY2_STATE.md` — curl flag, commutator state, Poisson Formation mother, exact equivalences.
3. `02_CRITICAL_GEOMETRY_AND_CONSTRAINED_GRADIENT.md` — `M`, `W_Λ`, `G`, `γ`, `T`, helicity sheets, neutral-cell identities.
4. `03_FLAGS_COCYCLES_AND_ACTUAL_STATE_VISIBILITY.md` — Poisson/heat cocycles, parity, actual-state zero set, subordination.
5. `04_COMPANIONS_TRIADS_AND_MIXED_CURVATURE.md` — polarized Curl–Killing, real companions, mixed Poisson–heat positivity, triad sign preservation.
6. `05_ANGULAR_CANCELLATION_RANK_ONE_AND_MODULE_COERCIVITY.md` — angular kernel, rank-one completion, outward grading, radial SVD, bounded-module contraction.
7. `06_TERMINAL_SCALING_AND_RENORMALIZED_BRANCHES.md` — critical Reynolds scaling, Euler branch, finite-viscosity doubly normalized flow.
8. `07_TRANSVERSE_FLOQUET_NORMAL_FORM.md` — complete nontransverse integration, weighted log-frequency monodromy, `T`-only forcing equation.
9. `08_NO_GO_COUNTERMECHANISMS_AND_OPEN_THEOREMS.md` — exact false shortcuts, hostile constructions, terminal alternatives, theorem targets.
10. `09_CHRONOLOGICAL_THEOREM_CHAIN.md` — chronological proof chain từ Theory-2 deployment đầu tiên tới transverse Floquet reduction.
11. `10_COMMON_RAY_POISSON_DEPTH_AND_T_COERCIVITY.md` — stationary regression rigidity, all-depth Gaussian-Poisson ray law, common ray-stress eigenrelation, first-order depth equation for `T`, exact signed transverse passivity, `H^{-1/2}` `T`-coercivity, raywise radial-spread debt, and current common-ray rigidity frontier.

---

## Current strongest stationary frontier

For a nondegenerate stationary normalized finite-`κ` profile,

\[
\beta=2\kappa D_2,
\qquad
H_3=0,
\qquad
|b|<1.
\]

At canonical heat depth

\[
\tau_*=\frac1{4D_2},
\]

define

\[
\mathcal V_\sigma(y,\omega)
=\int_0^\infty
\rho^2e^{-\tau_*\rho^2-y\rho}
f_\sigma(\rho,\omega)\,d\rho.
\]

Then for every positive Poisson depth,

\[
\boxed{
\mathcal N_\sigma(y,\omega)
=-2\kappa D_2y\,\mathcal V_\sigma(y,\omega).
}
\]

Equivalently, for physical stress `\mathsf R=v\otimes v`,

\[
\boxed{
P_\omega\mathsf S_y(\omega)\omega
=-2i\kappa D_2y\,\mathcal V(y,\omega).
}
\]

Using `N=γG+T`, the transverse ray reader satisfies

\[
\boxed{
\gamma(1-\sigma b)\partial_y\mathcal V_\sigma
+(\gamma a-2\kappa D_2y)\mathcal V_\sigma
=\mathcal T_\sigma.
}
\]

Because `|b|<1`, the derivative coefficient is positive on both helicity sheets.  With the explicit integrating factor `I_σ`,

\[
\boxed{
\int_{y_0}^\infty
I_\sigma^2
\operatorname{Re}
\langle\mathcal V_\sigma,\mathcal T_\sigma\rangle\,dy
=-\frac{\gamma(1-\sigma b)}2
I_\sigma(y_0)^2
\|\mathcal V_\sigma(y_0)\|_2^2.
}
\]

Hence on compact stationary finite-Reynolds strata,

\[
\boxed{
\|T\|_{H^{-1/2}}\ge c_{\mathcal K}\kappa.
}
\]

At the same canonical heat depth, smoothed Formation is raywise

\[
\boxed{\text{energy-inward}}
\qquad\text{and}\qquad
\boxed{\text{critical-neutral}},
\]

forcing a positive conditional radial-variance debt on every active ray.

---

## Current final frontier

The stationary finite-Reynolds problem is now reduced to **common-ray Formation rigidity**:

\[
\boxed{
P_\omega
\left[
\int_0^\infty
\rho^2e^{-\rho^2/(4D_2)-y\rho}
\widehat{v\otimes v}(\rho\omega)\,d\rho
\right]\omega
=-2i\kappa D_2y
\int_0^\infty
\rho^2e^{-\rho^2/(4D_2)-y\rho}
\widehat v(\rho\omega)\,d\rho
}
\]

for every `y>0` and `ω∈S²`, subject simultaneously to

\[
E=M=1,
\qquad H_3=0,
\qquad d>0,
\qquad |b|<1,
\]

reality, polarized Curl–Killing, and physical rank-one companion completion.

The all-depth Laplace family is injective, but injectivity alone is not a global coercive gap.  The decisive remaining step must exploit that the stress is the **same-state rank-one object**

\[
\mathsf R=v\otimes v,
\]

not an arbitrary tensor field.

For periodic finite-`κ` recurrence, the corresponding open theorem remains the time-ordered transverse Floquet version.

---

## Nonclaim

Dossier này **không** chứng minh global regularity của 3D Navier–Stokes. Nó chứng minh nhiều exact subtheorem và loại nhiều obstruction giả, đồng thời cô lập stationary obstruction thành a common-state/rank-one common-ray rigidity problem và periodic obstruction thành a transverse Floquet self-consistency problem.
