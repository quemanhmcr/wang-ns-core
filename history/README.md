# History

This directory now records **two different histories** of the Wang–Navier–Stokes project. They should not be mixed with the current canonical theory in [`../core/spectral_signature/`](../core/spectral_signature/).

The first history is the older **physical-road / control-volume programme**. The second is the later sequence of **research worktrees** that moved from singular-endpoint normal forms through C0/C1/Type-I geometry to the material-curl mother and finally to the whole-state spectral-flag signature.

The current structural core is:

\[
\boxed{
E_u=[\nabla_u,C]
\quad\longleftrightarrow\quad
\{\mathscr O_a(u)\}_{a\in\mathbb R}.
}
\]

Nothing in `history/` should be read as overriding the current theorem/scope statements in the spectral-signature core.

## 1. Old physical-road history

The original physical-road distillation is preserved as:

- [`PHYSICAL_ROAD_HISTORY.md`](PHYSICAL_ROAD_HISTORY.md) — the former `history/README.md`, including the control-volume, helical-work, B/S/V/O and full-state frontier narrative as it stood before the terminal-worktree pivot.
- [`CONTROL_VOLUME_METHOD.md`](CONTROL_VOLUME_METHOD.md)
- [`PHYSICAL_CORE.md`](PHYSICAL_CORE.md)
- [`MIXED_FRONTIER.md`](MIXED_FRONTIER.md)
- [`SOLUTION_MAP.md`](SOLUTION_MAP.md)
- [`BSVO_FULL_STATE_FRONTIER.md`](BSVO_FULL_STATE_FRONTIER.md)
- [`NS_POLAR_COMPATIBILITY_ARCHITECTURE.md`](NS_POLAR_COMPATIBILITY_ARCHITECTURE.md)

These files are historically important because many later spectral-signature identities first appeared there as apparently separate pressure, torsion, stress, helicity-curvature or Codazzi faces.

## 2. Terminal-era problem contract and literature ledger

Two former root/research documents are now explicitly historical:

- [`TERMINAL_PROBLEM_CONTRACT.md`](TERMINAL_PROBLEM_CONTRACT.md) — formerly `DEFINE_PROBLEM.md`; the pivot from “control the whole trajectory” to “extract one admissible singular survivor and classify it by finite normal forms.”
- [`NS_HISTORY_FACT_LEDGER.md`](NS_HISTORY_FACT_LEDGER.md) — formerly `research/NS_HISTORY_FACTS_FOR_NEO.md`; literature and extraction facts used to type the terminal programme.

The contract is the best place to understand why global spectral readers were initially treated as a typed upgrade rather than default tools on bounded ancient profiles.

## 3. Worktree-era history

The old worktrees are summarized in [`worktrees/README.md`](worktrees/README.md).

Read them in this order:

1. [`worktrees/SINGULARITY_NORMAL_FORM.md`](worktrees/SINGULARITY_NORMAL_FORM.md) — the strategic reset: singular endpoint → terminal object → finite normal form.
2. [`worktrees/ENDPOINT_FIRST_RIGIDITY.md`](worktrees/ENDPOINT_FIRST_RIGIDITY.md) — record vorticity, C0/C1, circulation/energy microscopes, finite kill classes and the anti-jet-loop discipline.
3. [`worktrees/C0_TO_MATERIAL_CURL.md`](worktrees/C0_TO_MATERIAL_CURL.md) — C0 angular escape, C1/G3/Type-I geometry, failure of local/Hodge closure, and the emergence of the common material-curl parent `E=[D_u,C]`.
4. [`worktrees/PROVENANCE_TO_SPECTRAL_FLAG.md`](worktrees/PROVENANCE_TO_SPECTRAL_FLAG.md) — provenance/propagation attempts, the anti-history correction, shifted spectral cuts, spectral-flag tomography, completeness and theoremization.

These files are **narratives**, not theorem registries. Exact theorem status lives in the source commits named inside each narrative or in the current canonical core.

## 4. Why the worktree history matters

Without the worktree history, the final object can look artificially obvious. It was not.

The project first tried to close singularity by increasingly sharp terminal classifiers. C0 looked promising because a curl maximum with zero stretching forces strong scalar flatness. That route failed locally because angular vorticity motion survives. C1/G3 then looked promising because Riccati geometry compresses the first jet. That route also failed as a purely local closure because Hodge/heat and remote geometry remain independent. Type-I scale geometry forced companions and positive-volume escape, but did not provide the final sign.

Those failures were productive. They taught the project to ask a different question:

> Are pressure, Hodge, torsion, Riccati, stress, helicity curvature and spectral work really different mechanisms, or different readings of one deformation of curl geometry?

The first answer was the material-curl mother
\[
E_u=[D_u,C].
\]
The later answer was the shifted spectral-flag family
\[
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a],
\qquad H_a=\operatorname{sgn}(C-aI),
\]
which tomographically reconstructs the mother.

The final compression was therefore not “one more terminal defect.” It was the realization that the whole smooth NS state is encoded by the mother/spectral-flag geometry modulo the expected Killing/Galilean symmetry.

## 5. Current reading boundary

Use `history/` to understand **why** the current objects were discovered and which false shortcuts were eliminated.

Use [`../core/spectral_signature/`](../core/spectral_signature/) to understand **what is currently claimed**.

Use [`../core/NEO/`](../core/NEO/) to understand the compiler/workbench discipline that helped compress the ontology.
