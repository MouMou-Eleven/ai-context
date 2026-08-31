#!/usr/bin/env python3
"""Validate the stable fields and timeline semantics of a Motion Blueprint JSON."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


TOP_LEVEL = (
    "request",
    "approval",
    "creativeDirection",
    "motionSystem",
    "timeline",
    "remotionPlan",
    "quality",
)


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def require_keys(value: Any, keys: tuple[str, ...], location: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{location} must be an object")
        return
    for key in keys:
        if key not in value:
            errors.append(f"{location}.{key} is required")


def require_string_list(value: Any, location: str, errors: list[str], minimum: int = 0) -> None:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        errors.append(f"{location} must be an array of strings")
    elif len(value) < minimum:
        errors.append(f"{location} must contain at least {minimum} item(s)")


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    require_keys(data, TOP_LEVEL, "$", errors)
    if not isinstance(data, dict):
        return errors

    request = data.get("request")
    request_keys = (
        "inputMode",
        "goal",
        "deliverable",
        "width",
        "height",
        "fps",
        "durationSeconds",
        "confirmedFacts",
        "assumptions",
    )
    require_keys(request, request_keys, "$.request", errors)
    if isinstance(request, dict):
        input_mode = request.get("inputMode")
        if input_mode not in {"text", "image", "hybrid"}:
            errors.append("$.request.inputMode must be text, image, or hybrid")
        if request.get("deliverable") not in {"blueprint", "code", "preview", "render"}:
            errors.append("$.request.deliverable is invalid")
        for key in ("width", "height", "fps"):
            value = request.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                errors.append(f"$.request.{key} must be a positive integer")
        duration = request.get("durationSeconds")
        if not is_number(duration) or duration <= 0:
            errors.append("$.request.durationSeconds must be a positive number")
        require_string_list(request.get("confirmedFacts"), "$.request.confirmedFacts", errors)
        require_string_list(request.get("assumptions"), "$.request.assumptions", errors)
        if input_mode in {"image", "hybrid"} and not isinstance(data.get("visualAnalysis"), dict):
            errors.append("$.visualAnalysis is required for image and hybrid input")

    approval = data.get("approval")
    require_keys(approval, ("mode", "status", "approvedScope", "evidence"), "$.approval", errors)
    if isinstance(approval, dict):
        mode = approval.get("mode")
        status = approval.get("status")
        evidence = approval.get("evidence")
        if mode not in {"required", "explicitly-waived"}:
            errors.append("$.approval.mode must be required or explicitly-waived")
        if status not in {"pending", "approved"}:
            errors.append("$.approval.status must be pending or approved")
        require_string_list(approval.get("approvedScope"), "$.approval.approvedScope", errors)
        if status == "approved":
            if not isinstance(evidence, str) or not evidence.strip():
                errors.append("$.approval.evidence must quote explicit user approval when status is approved")
            if not isinstance(approval.get("approvedScope"), list) or not approval.get("approvedScope"):
                errors.append("$.approval.approvedScope must not be empty when status is approved")
        elif evidence is not None:
            errors.append("$.approval.evidence must be null while status is pending")
        if mode == "explicitly-waived" and status != "approved":
            errors.append("$.approval.status must be approved when confirmation is explicitly waived")

    visual = data.get("visualAnalysis")
    if isinstance(visual, dict):
        require_keys(
            visual,
            ("observed", "hierarchy", "coreVisual", "preserve", "mayChange", "layerCandidates", "risks"),
            "$.visualAnalysis",
            errors,
        )
        for key in ("observed", "hierarchy", "preserve", "mayChange", "risks"):
            require_string_list(visual.get(key), f"$.visualAnalysis.{key}", errors, 1 if key == "hierarchy" else 0)
        if not isinstance(visual.get("coreVisual"), str) or not visual.get("coreVisual", "").strip():
            errors.append("$.visualAnalysis.coreVisual must be a non-empty string")
        layers = visual.get("layerCandidates")
        if not isinstance(layers, list):
            errors.append("$.visualAnalysis.layerCandidates must be an array")
        else:
            for index, layer in enumerate(layers):
                require_keys(layer, ("name", "role", "depth", "source", "editable"), f"$.visualAnalysis.layerCandidates[{index}]", errors)

    creative = data.get("creativeDirection")
    require_keys(creative, ("concept", "memoryHook", "styleWords", "intensity", "spatialModel"), "$.creativeDirection", errors)
    if isinstance(creative, dict):
        require_string_list(creative.get("styleWords"), "$.creativeDirection.styleWords", errors, 3)
        if isinstance(creative.get("styleWords"), list) and len(creative["styleWords"]) > 6:
            errors.append("$.creativeDirection.styleWords must contain no more than 6 items")
        if creative.get("intensity") not in {1, 2, 3}:
            errors.append("$.creativeDirection.intensity must be 1, 2, or 3")
        if creative.get("spatialModel") not in {"2d", "2.5d", "3d", "hybrid"}:
            errors.append("$.creativeDirection.spatialModel is invalid")

    motion = data.get("motionSystem")
    motion_keys = (
        "heroAction",
        "cameraPath",
        "elementActions",
        "secondaryActions",
        "microMotion",
        "continuityAnchor",
        "focusStrategy",
        "transitionLanguage",
        "audioStrategy",
        "negativeConstraints",
    )
    require_keys(motion, motion_keys, "$.motionSystem", errors)
    if isinstance(motion, dict):
        element_actions = motion.get("elementActions")
        if not isinstance(element_actions, list) or not element_actions:
            errors.append("$.motionSystem.elementActions must be a non-empty array")
        else:
            action_keys = ("element", "trigger", "startState", "motion", "durationSeconds", "easing", "causes", "endState", "implementation")
            for index, action in enumerate(element_actions):
                location = f"$.motionSystem.elementActions[{index}]"
                require_keys(action, action_keys, location, errors)
                if not isinstance(action, dict):
                    continue
                for key in ("element", "trigger", "startState", "motion", "easing", "causes", "endState", "implementation"):
                    if not isinstance(action.get(key), str) or not action.get(key, "").strip():
                        errors.append(f"{location}.{key} must be a non-empty string")
                if not is_number(action.get("durationSeconds")) or action.get("durationSeconds", 0) <= 0:
                    errors.append(f"{location}.durationSeconds must be a positive number")
        for key in ("secondaryActions", "microMotion", "transitionLanguage", "audioStrategy"):
            require_string_list(motion.get(key), f"$.motionSystem.{key}", errors)
        require_string_list(motion.get("negativeConstraints"), "$.motionSystem.negativeConstraints", errors, 1)

    timeline = data.get("timeline")
    duration = request.get("durationSeconds") if isinstance(request, dict) else None
    if not isinstance(timeline, list) or not timeline:
        errors.append("$.timeline must be a non-empty array")
    else:
        previous_end = 0.0
        for index, item in enumerate(timeline):
            location = f"$.timeline[{index}]"
            require_keys(
                item,
                ("startSeconds", "endSeconds", "beat", "pictureAction", "camera", "focusAndLayers", "audioCue", "implementation"),
                location,
                errors,
            )
            if not isinstance(item, dict):
                continue
            start = item.get("startSeconds")
            end = item.get("endSeconds")
            if not is_number(start) or not is_number(end) or end <= start:
                errors.append(f"{location} must have numeric endSeconds greater than startSeconds")
                continue
            if abs(start - previous_end) > 0.001:
                errors.append(f"{location}.startSeconds must equal the previous endSeconds ({previous_end:g})")
            previous_end = float(end)
        if is_number(duration) and abs(previous_end - float(duration)) > 0.001:
            errors.append("$.timeline must end at $.request.durationSeconds")

    plan = data.get("remotionPlan")
    require_keys(plan, ("compositionId", "components", "packages", "editableProps", "documentationToLoad", "checkFrames"), "$.remotionPlan", errors)
    if isinstance(plan, dict):
        require_string_list(plan.get("components"), "$.remotionPlan.components", errors, 1)
        require_string_list(plan.get("packages"), "$.remotionPlan.packages", errors)
        require_string_list(plan.get("editableProps"), "$.remotionPlan.editableProps", errors)
        require_string_list(plan.get("documentationToLoad"), "$.remotionPlan.documentationToLoad", errors, 1)
        check_frames = plan.get("checkFrames")
        if not isinstance(check_frames, list) or len(check_frames) < 3 or any(not isinstance(frame, int) or isinstance(frame, bool) or frame < 0 for frame in check_frames):
            errors.append("$.remotionPlan.checkFrames must contain at least 3 non-negative integers")

    quality = data.get("quality")
    require_keys(quality, ("acceptanceCriteria", "evidenceRequired"), "$.quality", errors)
    if isinstance(quality, dict):
        require_string_list(quality.get("acceptanceCriteria"), "$.quality.acceptanceCriteria", errors, 1)
        require_string_list(quality.get("evidenceRequired"), "$.quality.evidenceRequired", errors, 1)

    return errors


def run_self_test() -> int:
    valid = {
        "request": {
            "inputMode": "text",
            "goal": "Animate a card bounce",
            "deliverable": "blueprint",
            "width": 1920,
            "height": 1080,
            "fps": 30,
            "durationSeconds": 2,
            "confirmedFacts": ["The subject is one card"],
            "assumptions": ["Clean UI style"],
        },
        "approval": {
            "mode": "required",
            "status": "pending",
            "approvedScope": [],
            "evidence": None,
        },
        "creativeDirection": {
            "concept": "One controlled bounce",
            "memoryHook": "The landing compression",
            "styleWords": ["clean", "light", "tactile"],
            "intensity": 2,
            "spatialModel": "2.5d",
        },
        "motionSystem": {
            "heroAction": "Compress, release, settle",
            "cameraPath": "Subtle push-in",
            "elementActions": [
                {
                    "element": "Card",
                    "trigger": "Timeline starts",
                    "startState": "Six percent compressed below the landing point",
                    "motion": "Release upward, overshoot, and settle on the landing point",
                    "durationSeconds": 1.2,
                    "easing": "Spring with one controlled overshoot",
                    "causes": "The landing compresses the shadow",
                    "endState": "Front-facing card at rest with subtle edge flex",
                    "implementation": "Frame-driven scale and translate interpolation",
                }
            ],
            "secondaryActions": ["Shadow compression"],
            "microMotion": ["Edge flex"],
            "continuityAnchor": "Card center",
            "focusStrategy": "Hold the card center",
            "transitionLanguage": [],
            "audioStrategy": ["Soft landing click"],
            "negativeConstraints": ["No repeated random bounce"],
        },
        "timeline": [
            {"startSeconds": 0, "endSeconds": 0.4, "beat": "Anticipate", "pictureAction": "Card compresses", "camera": "Static", "focusAndLayers": "Card and shadow", "audioCue": None, "implementation": "CSS and interpolate"},
            {"startSeconds": 0.4, "endSeconds": 1.2, "beat": "Release", "pictureAction": "Card overshoots and returns", "camera": "Push in", "focusAndLayers": "Card center", "audioCue": "Landing", "implementation": "Easing.spring"},
            {"startSeconds": 1.2, "endSeconds": 2, "beat": "Hold", "pictureAction": "Card settles", "camera": "Locked", "focusAndLayers": "Final card", "audioCue": None, "implementation": "Clamped interpolate"},
        ],
        "remotionPlan": {
            "compositionId": "CardBounce",
            "components": ["CardBounce"],
            "packages": ["remotion"],
            "editableProps": ["title", "color"],
            "documentationToLoad": ["remotion-markup"],
            "checkFrames": [0, 24, 48],
        },
        "quality": {
            "acceptanceCriteria": ["Card is readable at the landing"],
            "evidenceRequired": ["Three representative frames"],
        },
    }
    valid_errors = validate(valid)
    invalid = json.loads(json.dumps(valid))
    invalid["request"]["inputMode"] = "image"
    invalid["timeline"][1]["startSeconds"] = 0.7
    invalid["approval"]["evidence"] = "Not approved"
    invalid_errors = validate(invalid)
    if valid_errors:
        print("Self-test failed: valid fixture was rejected", file=sys.stderr)
        for error in valid_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if len(invalid_errors) < 3:
        print("Self-test failed: invalid fixture was not rejected", file=sys.stderr)
        return 1
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", nargs="?", type=Path, help="Path to a Motion Blueprint JSON file")
    parser.add_argument("--self-test", action="store_true", help="Run built-in valid and invalid fixtures")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if args.blueprint is None:
        parser.error("blueprint is required unless --self-test is used")

    try:
        data = json.loads(args.blueprint.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read blueprint: {error}", file=sys.stderr)
        return 1

    errors = validate(data)
    if errors:
        print("Motion Blueprint is invalid:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Motion Blueprint is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
