# Singularity-Normal-Form Worktree
## From trajectory surveillance to one terminal object

**Historical branch:** `research/neo-singularity-normal-form`
**Recorded HEAD:** `dc31898`
**Important scratch artifact:** `research/NEO_SINGULARITY_NORMAL_FORM_01.md` existed as an untracked worktree notebook.

This was a short branch, but strategically it changed the unit of research.

Before this pivot, much of the programme still carried the implicit burden of following what a possible singular solution was doing across its whole pre-singular history. The singularity-normal-form branch imposed a harder rule:

\[
\boxed{
T_*<\infty
\longrightarrow
\text{one admissible terminal object}
\longrightarrow
\text{finite normal forms}
\longrightarrow
\text{rigidity or a named analytic gap}.
}
\]

The branch did not solve the extraction problem. Its importance was to **type the problem correctly**.

## 1. The former active contract

The root `DEFINE_PROBLEM.md`, now archived as [`../TERMINAL_PROBLEM_CONTRACT.md`](../TERMINAL_PROBLEM_CONTRACT.md), became the reference contract.

The external target was a finite-time singular endpoint in the classical unforced whole-space Navier--Stokes problem. The intended external doorway was a bounded mild ancient profile
\[
U:\mathbb R^3\times(-\infty,0]\to\mathbb R^3.
\]

The crucial typing warning was already explicit:

- bounded means bounded velocity;
- it does **not** automatically imply global `L^2`;
- it does **not** automatically imply `\dot H^{1/2}`;
- it does **not** automatically license global helicity or Fourier tightness.

This later became one of the most important safeguards in the spectral-signature programme.

## 2. Frozen anchors

The worktree froze the ontology at
\[
\boxed{
u(t),\ P,\ C=\operatorname{curl},\ C^2=(-\Delta)P,\ t.}
\]

The projected genetic law remained
\[
\boxed{
u_t=P[X_u,C]u-\nu C^2u.}
\]

The point was not that these symbols were new. The point was that **everything else had to compile back to them** before being admitted as a new mechanism.

Pressure, strain, transport, Riccati geometry, helicity readers and local differential tensors were therefore treated as compiled faces.

## 3. Separation of three tasks

The scratch notebook forced a clean dependency graph:

1. **Extraction** supplies an analytic terminal class.
2. **Nondegeneracy** prevents the terminal object from disappearing into Galilean constants.
3. **Rigidity** must eliminate the surviving normal forms.

This sounds obvious in hindsight, but it prevented a recurring error: using a local NEO identity as though it could repair a missing external compactness theorem.

## 4. Local first, spectral only when licensed

The branch explicitly distinguished
\[
\boxed{
\text{local differential geometry}
\quad\text{from}\quad
\text{global spectral geometry}.
}
\]

For a bounded ancient object, local quantities such as
\[
\nabla U,\ CU,\ C^2U,\ S,\ \omega
\]
are legitimate after local parabolic smoothing.

By contrast, `H=sgn C`, `|C|`, global helical decompositions and global spectral inner products were only a typed upgrade when the extraction class justified them.

This restriction later mattered when the full spectral flag was discovered. The spectral signature is a structural theorem on classes where the spectral calculus is licensed; it is not silently imported into every ancient blow-up profile.

## 5. The anti-loop rule

The most durable rule of the branch was:

> If a computation merely moves unresolved freedom into the next jet, stop.

A new derivative did not count as progress merely because it was exact.

A finite terminal classifier had to end in one of four ways:

- killed by rigidity;
- reduced to a lower-dimensional exact class;
- upgraded to a function space where a stronger reader becomes legal;
- or left open with one named analytic obstruction.

This rule shaped every later worktree.

## 6. Why the branch was superseded

The singularity-normal-form notebook still expected that a finite family of terminal geometries might be enough to close the problem directly.

The next worktrees showed why that was too optimistic. C0 retained angular freedom. C1/G3 retained Hodge/heat freedom. Type-I companion geometry forced nonlocal structure without supplying a final sign. Eventually the project learned that even tracking the terminal obstruction through more refined normal forms could become another history trap.

But without this branch, the later failures would have been much harder to interpret. It supplied the discipline that allowed the project to recognize a failed normal-form strategy as a **failed strategy**, rather than an invitation to generate another descendant.

## 7. Historical source map

Useful historical coordinates from this era:

- former root `DEFINE_PROBLEM.md` → now [`../TERMINAL_PROBLEM_CONTRACT.md`](../TERMINAL_PROBLEM_CONTRACT.md);
- branch scratch notebook `research/NEO_SINGULARITY_NORMAL_FORM_01.md`;
- literature ledger → now [`../NS_HISTORY_FACT_LEDGER.md`](../NS_HISTORY_FACT_LEDGER.md);
- compiler/workbench → current [`../../core/NEO/`](../../core/NEO/).

The branch itself contains little final mathematics. Its legacy is the **proof-search grammar** that made the later worktree history intelligible.
