#!/usr/bin/env python3
"""Compare protected background regions between a reference and rendered still."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageStat
except ImportError as error:  # pragma: no cover
    print("Pillow is required before comparing background regions.", file=sys.stderr)
    raise SystemExit(2) from error


def parse_region(raw: str) -> tuple[float, float, float, float]:
    try:
        x, y, width, height = (float(part.strip()) for part in raw.split(","))
    except (TypeError, ValueError) as error:
        raise argparse.ArgumentTypeError("region must be x,y,width,height in normalized 0..1 coordinates") from error
    if min(x, y) < 0 or min(width, height) <= 0 or x + width > 1 or y + height > 1:
        raise argparse.ArgumentTypeError("region must stay inside normalized 0..1 bounds")
    return x, y, width, height


def _box(region: tuple[float, float, float, float], size: tuple[int, int]) -> tuple[int, int, int, int]:
    x, y, width, height = region
    left = round(x * size[0])
    top = round(y * size[1])
    right = max(left + 1, round((x + width) * size[0]))
    bottom = max(top + 1, round((y + height) * size[1]))
    return left, top, right, bottom


def _luminance(rgb: tuple[float, float, float]) -> float:
    return (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) / 255


def compare(reference_path: Path, final_path: Path, regions: list[tuple[float, float, float, float]], max_rgb_mae: float, max_luminance_delta: float) -> dict[str, object]:
    with Image.open(reference_path) as reference_source, Image.open(final_path) as final_source:
        reference = reference_source.convert("RGB")
        final = final_source.convert("RGB")
        if reference.size != final.size:
            raise ValueError(f"dimension mismatch: reference={reference.size[0]}x{reference.size[1]}, final={final.size[0]}x{final.size[1]}")
        reports: list[dict[str, object]] = []
        for index, region in enumerate(regions):
            box = _box(region, reference.size)
            ref_crop = reference.crop(box)
            final_crop = final.crop(box)
            ref_mean = tuple(ImageStat.Stat(ref_crop).mean)
            final_mean = tuple(ImageStat.Stat(final_crop).mean)
            difference = ImageChops.difference(ref_crop, final_crop)
            rgb_mae = sum(ImageStat.Stat(difference).mean) / 3 / 255
            luminance_delta = abs(_luminance(ref_mean) - _luminance(final_mean))
            passed = rgb_mae <= max_rgb_mae and luminance_delta <= max_luminance_delta
            reports.append({
                "index": index,
                "normalizedBounds": list(region),
                "pixelBounds": list(box),
                "referenceMeanRgb": [round(value, 3) for value in ref_mean],
                "finalMeanRgb": [round(value, 3) for value in final_mean],
                "rgbMae": rgb_mae,
                "luminanceDelta": luminance_delta,
                "passed": passed,
            })
    return {
        "reference": str(reference_path),
        "final": str(final_path),
        "thresholds": {"maxRgbMae": max_rgb_mae, "maxLuminanceDelta": max_luminance_delta},
        "regions": reports,
        "passed": all(report["passed"] for report in reports),
    }


def run_self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="background-fidelity-") as directory:
        root = Path(directory)
        reference = root / "reference.png"
        same = root / "same.png"
        wrong = root / "wrong.png"
        Image.new("RGB", (32, 18), (1, 8, 42)).save(reference)
        Image.new("RGB", (32, 18), (2, 9, 43)).save(same)
        Image.new("RGB", (32, 18), (80, 86, 101)).save(wrong)
        regions = [(0.0, 0.0, 0.4, 0.4), (0.6, 0.0, 0.4, 0.4), (0.0, 0.6, 0.4, 0.4)]
        if not compare(reference, same, regions, 0.06, 0.05)["passed"]:
            print("Self-test failed: matching dark background was rejected", file=sys.stderr)
            return 1
        if compare(reference, wrong, regions, 0.06, 0.05)["passed"]:
            print("Self-test failed: washed-out background was accepted", file=sys.stderr)
            return 1
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", nargs="?", type=Path, help="Approved reference still")
    parser.add_argument("final_still", nargs="?", type=Path, help="Rendered final still")
    parser.add_argument("--region", action="append", type=parse_region, help="Protected x,y,width,height region; repeat at least three times")
    parser.add_argument("--max-rgb-mae", type=float, default=0.06)
    parser.add_argument("--max-luminance-delta", type=float, default=0.05)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if args.reference is None or args.final_still is None:
        parser.error("reference and final_still are required unless --self-test is used")
    if not args.region or len(args.region) < 3:
        parser.error("repeat --region at least three times using safe background areas")
    try:
        result = compare(args.reference, args.final_still, args.region, args.max_rgb_mae, args.max_luminance_delta)
    except (OSError, ValueError) as error:
        print(f"Could not compare background regions: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Background fidelity: {'PASS' if result['passed'] else 'FAIL'}")
        for region in result["regions"]:
            print(f"- region {region['index']}: RGB MAE={region['rgbMae']:.6f}, luminance delta={region['luminanceDelta']:.6f}, {'PASS' if region['passed'] else 'FAIL'}")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
