#!/usr/bin/env python3
"""Validate measured element bounds and clipping state across rendered frames."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Any


PHASES = {"motion-peak", "hold-start", "hold-mid", "hold-end", "parameter-stress"}
KINDS = {"text", "number", "logo", "icon", "image", "shape", "other"}


def _number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _rect(value: Any, location: str, errors: list[str]) -> tuple[float, float, float, float] | None:
    if not isinstance(value, dict):
        errors.append(f"{location} must be an object")
        return None
    required = ("left", "top", "width", "height")
    for key in required:
        if key not in value:
            errors.append(f"{location}.{key} is required")
    if any(key not in value for key in required):
        return None
    if any(not _number(value[key]) for key in required):
        errors.append(f"{location} values must be numbers")
        return None
    left, top, width, height = (float(value[key]) for key in required)
    if width <= 0 or height <= 0:
        errors.append(f"{location} width and height must be positive")
        return None
    return left, top, left + width, top + height


def _contained(inner: tuple[float, float, float, float], outer: tuple[float, float, float, float], tolerance: float) -> bool:
    return inner[0] >= outer[0] - tolerance and inner[1] >= outer[1] - tolerance and inner[2] <= outer[2] + tolerance and inner[3] <= outer[3] + tolerance


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["$ must be an object"]
    if data.get("schemaVersion") != 1:
        errors.append("$.schemaVersion must be 1")
    canvas = data.get("canvas")
    if not isinstance(canvas, dict):
        errors.append("$.canvas must be an object")
        canvas_rect = None
    else:
        width, height = canvas.get("width"), canvas.get("height")
        if not _number(width) or not _number(height) or width <= 0 or height <= 0:
            errors.append("$.canvas width and height must be positive numbers")
            canvas_rect = None
        else:
            canvas_rect = (0.0, 0.0, float(width), float(height))
    tolerance = data.get("tolerancePx", 1)
    if not _number(tolerance) or tolerance < 0 or tolerance > 4:
        errors.append("$.tolerancePx must be a number from 0 to 4")
        tolerance = 1.0
    else:
        tolerance = float(tolerance)
    protected = data.get("protectedElements")
    if not isinstance(protected, list) or not protected or any(not _nonempty(item) for item in protected):
        errors.append("$.protectedElements must contain at least one non-empty name")
        protected_names: set[str] = set()
    else:
        protected_names = set(protected)
        if len(protected_names) != len(protected):
            errors.append("$.protectedElements names must be unique")
    if not _nonempty(data.get("measurementMethod")):
        errors.append("$.measurementMethod must describe actual browser/text measurement")

    frames = data.get("frames")
    if not isinstance(frames, list) or len(frames) < 3:
        errors.append("$.frames must contain at least three measured frames")
        return errors
    seen_phases: set[str] = set()
    seen_frames: set[int] = set()
    hold_presence: dict[str, set[str]] = {"hold-start": set(), "hold-end": set()}
    for frame_index, frame in enumerate(frames):
        frame_location = f"$.frames[{frame_index}]"
        if not isinstance(frame, dict):
            errors.append(f"{frame_location} must be an object")
            continue
        frame_number = frame.get("frame")
        if not isinstance(frame_number, int) or isinstance(frame_number, bool) or frame_number < 0:
            errors.append(f"{frame_location}.frame must be a non-negative integer")
        elif frame_number in seen_frames:
            errors.append(f"{frame_location}.frame must be unique")
        else:
            seen_frames.add(frame_number)
        phase = frame.get("phase")
        if phase not in PHASES:
            errors.append(f"{frame_location}.phase is invalid")
        else:
            seen_phases.add(phase)
        elements = frame.get("elements")
        if not isinstance(elements, list) or not elements:
            errors.append(f"{frame_location}.elements must be a non-empty array")
            continue
        names_in_frame: set[str] = set()
        for element_index, element in enumerate(elements):
            location = f"{frame_location}.elements[{element_index}]"
            if not isinstance(element, dict):
                errors.append(f"{location} must be an object")
                continue
            name = element.get("name")
            if not _nonempty(name):
                errors.append(f"{location}.name must be a non-empty string")
                continue
            if name in names_in_frame:
                errors.append(f"{location}.name must be unique within the frame")
            names_in_frame.add(name)
            if phase in hold_presence:
                hold_presence[phase].add(name)
            if element.get("kind") not in KINDS:
                errors.append(f"{location}.kind is invalid")
            if not _nonempty(element.get("measurement")):
                errors.append(f"{location}.measurement must describe the measured visible/ink bounds")
            bounds = _rect(element.get("bounds"), f"{location}.bounds", errors)
            approved_crop = element.get("approvedCrop")
            if not isinstance(approved_crop, bool):
                errors.append(f"{location}.approvedCrop must be boolean")
                approved_crop = False
            crop_reason = element.get("cropReason")
            if approved_crop and not _nonempty(crop_reason):
                errors.append(f"{location}.cropReason is required when approvedCrop=true")
            if not approved_crop and crop_reason not in (None, ""):
                errors.append(f"{location}.cropReason must be null/empty when approvedCrop=false")
            if bounds is not None and canvas_rect is not None and not approved_crop and not _contained(bounds, canvas_rect, tolerance):
                errors.append(f"{location}.bounds are cropped by the canvas")
            ancestors = element.get("clipAncestors")
            if not isinstance(ancestors, list):
                errors.append(f"{location}.clipAncestors must be an array")
                ancestors = []
            for ancestor_index, ancestor in enumerate(ancestors):
                ancestor_location = f"{location}.clipAncestors[{ancestor_index}]"
                if not isinstance(ancestor, dict) or not _nonempty(ancestor.get("name")):
                    errors.append(f"{ancestor_location}.name must be a non-empty string")
                    continue
                ancestor_bounds = _rect(ancestor.get("bounds"), f"{ancestor_location}.bounds", errors)
                if bounds is not None and ancestor_bounds is not None and not approved_crop and not _contained(bounds, ancestor_bounds, tolerance):
                    errors.append(f"{location}.bounds are cropped by ancestor {ancestor.get('name')}")
            for key in ("activeClipPath", "activeMask"):
                if not isinstance(element.get(key), bool):
                    errors.append(f"{location}.{key} must be boolean")
                elif phase in {"hold-start", "hold-mid", "hold-end", "parameter-stress"} and element[key] and not approved_crop:
                    errors.append(f"{location}.{key} must be false in stable/readable frames")
    for required_phase in ("motion-peak", "hold-start", "hold-end"):
        if required_phase not in seen_phases:
            errors.append(f"$.frames must include phase={required_phase}")
    for phase, present in hold_presence.items():
        missing = sorted(protected_names - present)
        if missing:
            errors.append(f"$.frames phase={phase} is missing protected elements: {', '.join(missing)}")
    return errors


def _fixture() -> dict[str, Any]:
    elements = [
        {
            "name": "main-title",
            "kind": "text",
            "measurement": "DOM Range plus Canvas actualBoundingBox metrics after document.fonts.ready",
            "bounds": {"left": 126, "top": 276, "width": 900, "height": 165},
            "clipAncestors": [],
            "activeClipPath": False,
            "activeMask": False,
            "approvedCrop": False,
            "cropReason": None,
        }
    ]
    return {
        "schemaVersion": 1,
        "canvas": {"width": 1280, "height": 720},
        "tolerancePx": 1,
        "protectedElements": ["main-title"],
        "measurementMethod": "Browser DOM measurement after fonts loaded; text ink metrics included",
        "frames": [
            {"frame": 70, "phase": "motion-peak", "elements": elements},
            {"frame": 128, "phase": "hold-start", "elements": elements},
            {"frame": 149, "phase": "hold-end", "elements": elements},
        ],
    }


def run_self_test() -> int:
    valid = _fixture()
    if errors := validate(valid):
        print("Self-test failed: valid visibility report was rejected", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    invalid = json.loads(json.dumps(valid))
    title = invalid["frames"][1]["elements"][0]
    title["clipAncestors"] = [{"name": "title-mask", "bounds": {"left": 126, "top": 281, "width": 900, "height": 148}}]
    title["activeClipPath"] = True
    errors = validate(invalid)
    expected = ("cropped by ancestor", "activeClipPath must be false")
    if any(not any(fragment in error for error in errors) for fragment in expected):
        print("Self-test failed: cropped title was accepted", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory(prefix="visibility-report-") as directory:
        Path(directory, "fixture.json").write_text(json.dumps(valid), encoding="utf-8")
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if args.report is None:
        parser.error("report is required unless --self-test is used")
    try:
        data = json.loads(args.report.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read visibility report: {error}", file=sys.stderr)
        return 1
    errors = validate(data)
    if errors:
        print("Visibility report is invalid:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Visibility report passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
