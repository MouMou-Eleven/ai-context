#!/usr/bin/env python3
"""Check that the final hold is a continuous settle, not a late scene swap."""

from __future__ import annotations

import argparse
import json
import math
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image
except ImportError as error:  # pragma: no cover
    print("Pillow is required: install it in the active Python environment before checking frames.", file=sys.stderr)
    raise SystemExit(2) from error


def _metrics(first: Image.Image, second: Image.Image, pixel_threshold: int) -> dict[str, float]:
    a = first.convert("RGB")
    b = second.convert("RGB")
    if a.size != b.size:
        raise ValueError(f"dimension mismatch: {a.size[0]}x{a.size[1]} vs {b.size[0]}x{b.size[1]}")
    abs_sum = 0
    square_sum = 0
    changed = 0
    pixels = a.width * a.height
    for pa, pb in zip(a.getdata(), b.getdata()):
        deltas = tuple(abs(x - y) for x, y in zip(pa, pb))
        abs_sum += sum(deltas)
        square_sum += sum(delta * delta for delta in deltas)
        if max(deltas) > pixel_threshold:
            changed += 1
    return {
        "mae": abs_sum / (pixels * 3) / 255,
        "rmse": math.sqrt(square_sum / (pixels * 3)) / 255,
        "changedPixelPercent": changed / pixels * 100,
    }


def check(paths: list[Path], pixel_threshold: int, max_mae: float, max_changed_percent: float) -> dict[str, object]:
    if len(paths) < 3:
        raise ValueError("provide at least three consecutive final-hold stills")
    pairs: list[dict[str, object]] = []
    with Image.open(paths[0]) as first_source:
        first = first_source.convert("RGB")
        for index, path in enumerate(paths[1:], start=1):
            with Image.open(path) as second_source:
                second = second_source.convert("RGB")
                metrics = _metrics(first, second, pixel_threshold)
            pairs.append({"from": str(paths[index - 1]), "to": str(path), **metrics})
            first = second
    passed = all(pair["mae"] <= max_mae and pair["changedPixelPercent"] <= max_changed_percent for pair in pairs)
    return {
        "frames": [str(path) for path in paths],
        "pairs": pairs,
        "thresholds": {"pixelThreshold": pixel_threshold, "maxMae": max_mae, "maxChangedPixelPercent": max_changed_percent},
        "passed": passed,
    }


def run_self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="settle-continuity-") as directory:
        root = Path(directory)
        clean = []
        for index in range(3):
            path = root / f"clean-{index}.png"
            Image.new("RGB", (16, 16), (4, 8, 30)).save(path)
            clean.append(path)
        if not check(clean, 12, 0.02, 6.0)["passed"]:
            print("Self-test failed: stable hold was rejected", file=sys.stderr)
            return 1
        bad = root / "bad.png"
        Image.new("RGB", (16, 16), (240, 240, 240)).save(bad)
        if check([clean[0], clean[1], bad], 12, 0.02, 6.0)["passed"]:
            print("Self-test failed: scene swap was accepted", file=sys.stderr)
            return 1
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("frames", nargs="*", type=Path, help="At least three stills sampled across the final hold")
    parser.add_argument("--pixel-threshold", type=int, default=12, help="Per-channel delta counted as changed")
    parser.add_argument("--max-mae", type=float, default=0.02, help="Maximum normalized MAE between hold frames")
    parser.add_argument("--max-changed-percent", type=float, default=6.0, help="Maximum changed-pixel percentage between hold frames")
    parser.add_argument("--json", action="store_true", help="Print machine-readable metrics")
    parser.add_argument("--self-test", action="store_true", help="Run built-in stable/swap fixtures")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if len(args.frames) < 3:
        parser.error("at least three frames are required unless --self-test is used")
    try:
        result = check(args.frames, args.pixel_threshold, args.max_mae, args.max_changed_percent)
    except (OSError, ValueError) as error:
        print(f"Could not check settle continuity: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Final-hold continuity: {'PASS' if result['passed'] else 'FAIL'}")
        for pair in result["pairs"]:
            print(f"- {pair['from']} → {pair['to']}: MAE={pair['mae']:.6f}, changed={pair['changedPixelPercent']:.3f}%")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
