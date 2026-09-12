#!/usr/bin/env python3
"""Compare a Remotion final still with its approved reference frame.

The script intentionally compares same-size stills, not player screenshots.  In
``locked`` mode it is a hard gate; ``overlay`` mode is an inspection report for
editable reconstructions where changed pixels are expected.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageChops, ImageEnhance
except ImportError as error:  # pragma: no cover - exercised only without Pillow
    print("Pillow is required: install it in the active Python environment before comparing frames.", file=sys.stderr)
    raise SystemExit(2) from error


def _values(image: Image.Image) -> Iterable[tuple[int, int, int]]:
    return image.convert("RGB").getdata()


def compare(reference_path: Path, final_path: Path, pixel_threshold: int) -> dict[str, object]:
    with Image.open(reference_path) as reference_source, Image.open(final_path) as final_source:
        reference = reference_source.convert("RGB")
        final = final_source.convert("RGB")
        if reference.size != final.size:
            raise ValueError(f"dimension mismatch: reference={reference.size[0]}x{reference.size[1]}, final={final.size[0]}x{final.size[1]}")

        difference = ImageChops.difference(reference, final)
        pixel_count = reference.width * reference.height
        abs_sum = 0
        square_sum = 0
        changed = 0
        max_channel_delta = 0
        for ref_pixel, final_pixel in zip(_values(reference), _values(final)):
            deltas = tuple(abs(a - b) for a, b in zip(ref_pixel, final_pixel))
            abs_sum += sum(deltas)
            square_sum += sum(delta * delta for delta in deltas)
            max_channel_delta = max(max_channel_delta, *deltas)
            if max(deltas) > pixel_threshold:
                changed += 1

        channel_count = pixel_count * 3
        return {
            "width": reference.width,
            "height": reference.height,
            "mae": abs_sum / channel_count / 255,
            "rmse": math.sqrt(square_sum / channel_count) / 255,
            "changedPixelPercent": changed / pixel_count * 100,
            "pixelThreshold": pixel_threshold,
            "maxChannelDelta": max_channel_delta,
            "differenceBoundingBox": list(difference.getbbox()) if difference.getbbox() else None,
            "reference": str(reference_path),
            "final": str(final_path),
        }


def write_inspection_images(reference_path: Path, final_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with Image.open(reference_path) as reference_source, Image.open(final_path) as final_source:
        reference = reference_source.convert("RGB")
        final = final_source.convert("RGB")
        Image.blend(reference, final, 0.5).save(output_dir / "reference-overlay-50.png")
        difference = ImageChops.difference(reference, final)
        amplified = difference.point(lambda channel: min(255, channel * 8))
        ImageEnhance.Contrast(amplified).enhance(1.5).save(output_dir / "reference-diff-amplified.png")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path, help="Approved reference still")
    parser.add_argument("final_still", type=Path, help="Rendered final still")
    parser.add_argument("--mode", choices=("locked", "overlay", "rebuild"), default="locked")
    parser.add_argument("--pixel-threshold", type=int, default=12, help="Per-channel delta counted as changed (default: 12/255)")
    parser.add_argument("--max-mae", type=float, default=0.005, help="Locked-mode maximum normalized MAE (default: 0.005)")
    parser.add_argument("--max-changed-percent", type=float, default=1.0, help="Locked-mode maximum changed-pixel percentage (default: 1.0)")
    parser.add_argument("--output-dir", type=Path, help="Write 50%% overlay and amplified difference images here")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    try:
        metrics = compare(args.reference, args.final_still, args.pixel_threshold)
    except (OSError, ValueError) as error:
        print(f"Could not compare frames: {error}", file=sys.stderr)
        return 1

    if args.output_dir:
        try:
            write_inspection_images(args.reference, args.final_still, args.output_dir)
            metrics["inspectionDir"] = str(args.output_dir)
        except OSError as error:
            print(f"Could not write inspection images: {error}", file=sys.stderr)
            return 1

    passed = True
    if args.mode == "locked":
        passed = metrics["mae"] <= args.max_mae and metrics["changedPixelPercent"] <= args.max_changed_percent
        metrics["gate"] = {"mode": "locked", "maxMae": args.max_mae, "maxChangedPixelPercent": args.max_changed_percent, "passed": passed}
    else:
        metrics["gate"] = {"mode": args.mode, "passed": True, "note": "Use the overlay, protected-region bounds, and approved difference list for human acceptance."}

    if args.json:
        print(json.dumps(metrics, ensure_ascii=False, indent=2))
    else:
        print(f"{args.mode} comparison: {'PASS' if passed else 'FAIL'}")
        print(f"- dimensions: {metrics['width']}x{metrics['height']}")
        print(f"- normalized MAE: {metrics['mae']:.6f}")
        print(f"- normalized RMSE: {metrics['rmse']:.6f}")
        print(f"- changed pixels (> {args.pixel_threshold}/255): {metrics['changedPixelPercent']:.3f}%")
        print(f"- max channel delta: {metrics['maxChannelDelta']}")
        if metrics.get("inspectionDir"):
            print(f"- inspection images: {metrics['inspectionDir']}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
