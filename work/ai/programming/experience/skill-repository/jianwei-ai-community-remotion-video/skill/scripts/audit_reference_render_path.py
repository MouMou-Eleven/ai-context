#!/usr/bin/env python3
"""Reject full-frame reference-image cheats in a Remotion production source tree.

The approved reference still belongs in an analysis/comparison path.  In the
default ``layout-locked`` mode it must not be imported by the production
composition or used as a last-second opacity/crossfade layer.  This small,
deterministic audit catches the failure mode that a final-frame pixel check
alone cannot see.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path


SOURCE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}
SIGNAL_PATTERNS = (
    re.compile(r"\bFinalFrame(?:Lock|Reference|Overlay)\b", re.IGNORECASE),
    re.compile(r"\b(?:terminal|reference|final)[-_ ]?(?:reference|frame)[-_ ]?(?:lock|overlay|layer)\b", re.IGNORECASE),
    re.compile(r"\b(?:reference|final)(?:Frame)?(?:Overlay|Lock)\b", re.IGNORECASE),
    re.compile(r"\blockFinalFrame\b", re.IGNORECASE),
)


def _strip_line_comment(line: str) -> str:
    """Remove the common single-line comments without hiding string literals."""

    if "//" in line:
        return line.split("//", 1)[0]
    return line


def audit(project_root: Path, reference_asset: str, source_dir: str) -> list[dict[str, object]]:
    source_root = project_root / source_dir
    if not source_root.is_dir():
        raise FileNotFoundError(f"source directory does not exist: {source_root}")
    asset_token = Path(reference_asset).name.lower()
    findings: list[dict[str, object]] = []
    for path in sorted(source_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SOURCE_EXTENSIONS:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            findings.append({"file": str(path), "line": 0, "reason": "source is not UTF-8; audit it manually"})
            continue
        for line_number, line in enumerate(lines, start=1):
            code = _strip_line_comment(line)
            if asset_token and asset_token in code.lower():
                findings.append({"file": str(path), "line": line_number, "reason": f"reference asset token '{asset_token}' is used by production source", "text": line.strip()})
            for pattern in SIGNAL_PATTERNS:
                if pattern.search(code):
                    findings.append({"file": str(path), "line": line_number, "reason": f"terminal reference-overlay signal '{pattern.pattern}'", "text": line.strip()})
                    break
    return findings


def run_self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="reference-path-audit-") as directory:
        root = Path(directory)
        (root / "src").mkdir()
        (root / "src" / "good.tsx").write_text("export const Scene = () => <div />;\n", encoding="utf-8")
        if audit(root, "reference.png", "src"):
            print("Self-test failed: clean source was rejected", file=sys.stderr)
            return 1
        (root / "src" / "bad.tsx").write_text("const src = staticFile('reference.png');\nconst FinalFrameLock = () => null;\n", encoding="utf-8")
        findings = audit(root, "reference.png", "src")
        if len(findings) < 2:
            print("Self-test failed: reference overlay was not detected", file=sys.stderr)
            return 1
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", type=Path, help="Remotion project root")
    parser.add_argument("--reference-asset", default="reference.png", help="Reference asset basename or path used only for comparison")
    parser.add_argument("--source-dir", default="src", help="Production source directory relative to project root")
    parser.add_argument("--json", action="store_true", help="Print machine-readable findings")
    parser.add_argument("--self-test", action="store_true", help="Run built-in clean/bad fixtures")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if args.project_root is None:
        parser.error("project_root is required unless --self-test is used")
    try:
        findings = audit(args.project_root, args.reference_asset, args.source_dir)
    except OSError as error:
        print(f"Could not audit source: {error}", file=sys.stderr)
        return 1
    result = {"projectRoot": str(args.project_root), "referenceAsset": args.reference_asset, "findings": findings, "passed": not findings}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif findings:
        print("Reference render-path audit: FAIL")
        for finding in findings:
            print(f"- {finding['file']}:{finding['line']} — {finding['reason']}")
    else:
        print("Reference render-path audit: PASS (no production reference overlay detected)")
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
