# Wang–NS Physical Core

A distilled research kernel for the current Wang–Navier–Stokes no-escape programme.

This repository is **not** a smaller archive of [`wang-ns-triad-diamond`](https://github.com/quemanhmcr/wang-ns-triad-diamond). It is a backward slice from the current proof frontier: retain only the physical objects, structural theorems, anti-theorems, and recurrence laws still needed to stand at the mixed genuine-owner frontier.

Baseline distilled from the old repository at

`main@63178b0e7f9fabdfd8c344dab938a3d639639df5`

whose latest theorem state is the native material-service causal quotient

`d6ee03d5b9b7a82d11a2259c5dc0b8ae2ac945ab`.

There is **no claim here of a proof of 3D Navier–Stokes global regularity**. The current programme has closed many artificial or pure recurrence routes, but mixed genuine-native-owner recurrence, a local degenerate HH seam, and the initial/singular-time interfaces remain open.

## Method

The project follows the physical PDE rather than forcing the PDE into an analyst-chosen master currency.

1. Start from actual Navier–Stokes quantities and preserve their type.
2. Distinguish physical events from representation changes.
3. Quotient observer freedom before charging causality.
4. Never manufacture scale progress, event depth, source, or work from bookkeeping.
5. Let each genuine recurrence be controlled only by the native physical law it actually supplies.

The guiding question is not “what can we bound globally?” but:

> What did Navier–Stokes physically do, who owns that action, and what exact law can that owner not evade?

## Three living documents

- **`README.md`** — research contract, status, and map.
- **`PHYSICAL_CORE.md`** — the minimal physical theorem basis needed by the current architecture.
- **`MIXED_FRONTIER.md`** — what has been quotiented/closed, what is still genuinely recursive, and the exact next proof problem.

Historical proof scaffolding, CI ledgers, result archives, theorem-by-theorem chronology, and superseded representations are deliberately absent. Their irreversible lessons are retained as invariants or anti-theorems in the two core documents.

## Executable tripwires

`core_tripwires.py` and `test_core_tripwires.py` are intentionally tiny. They are **not proofs** and are not numerical substitutes for the PDE theorems. They encode a few semantics that future edits must not accidentally reverse: signed-before-Hahn routing, single recipient charge, stock/work separation, material-sidecar non-generation, antisymmetric relink flux, physical-first joint stops, and native-evidence admission.

Run them with no third-party dependency:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest -q test_core_tripwires.py
```

The test suite is meant to run continuously while doing research. A slow certification farm would defeat the purpose of this repository.

## Current proof picture

The live physical spine is

```text
actual signed NS nonlinear work
        ↓ Hahn once
a canonical positive physical cause
        ↓ physical ownership / donor provenance
hard tail: inherited stock OR true low→high supply
        ↓
pure UV  ───────────────→ first-shell natural-time route
resolved contact ───────→ K/S or contact-HH route
        ↓
physical first-stop / continuation laws
        ↓
quotient checkpoints, conservative relink, inherited stock,
material rereading and selected-family boundaries
        ↓
finite pure high-strain epochs
finite pure signed-good generated-HH epochs
        ↓
MIXED GENUINE NATIVE-OWNER RECURRENCE  ← current frontier
```

The current role/probe quotient removes analysis-role/probe changes as an independent causal currency.  The remaining master-facing native families are source/SGS, strain/dissipation, actual nonlinear work (including generic HH/high-tail work after its physical gates), and physical shell/service.  A role/probe observation must resolve into one of those mechanisms or fail closed.

The aim of this repository is to make that structure visible immediately, without requiring a reader to reconstruct it from thousands of historical files.
