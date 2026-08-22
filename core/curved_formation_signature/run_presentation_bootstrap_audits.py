#!/usr/bin/env python3
"""Run the complete Core-3 Campaign-IV presentation-bootstrap tribunal suite."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDITS = ROOT / "research" / "theory2_universal_compiler" / "audits"


def main() -> None:
    files = sorted(AUDITS.glob("*.py"))
    if not files:
        raise SystemExit(f"no presentation-bootstrap audits found in {AUDITS}")
    for idx, path in enumerate(files, 1):
        print(f"=== [{idx}/{len(files)}] {path.name} ===", flush=True)
        subprocess.run([sys.executable, str(path)], cwd=ROOT, check=True)
    print(f"ALL_PRESENTATION_BOOTSTRAP_AUDITS_PASS count={len(files)}")


if __name__ == "__main__":
    main()
