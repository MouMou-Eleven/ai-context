#!/usr/bin/env python3
"""Validate the internal second-pass director brief before Remotion implementation."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Any


TOP_LEVEL = (
    "visibility",
    "requestDigest",
    "immutableConstraints",
    "visualFacts",
    "directorTranslation",
    "energyChain",
    "cameraKeyPoses",
    "elementDirections",
    "timingStrategy",
    "parameterization",
    "negativeConstraints",
    "selfCritique",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: Any, minimum: int = 0) -> bool:
    return isinstance(value, list) and len(value) >= minimum and all(_nonempty(item) for item in value)


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["$ must be an object"]
    missing = [key for key in TOP_LEVEL if key not in data]
    errors.extend(f"$.{key} is required" for key in missing)
    extras = sorted(set(data) - set(TOP_LEVEL))
    errors.extend(f"$.{key} is not allowed" for key in extras)
    if data.get("visibility") != "internal":
        errors.append("$.visibility must be internal")
    if not _nonempty(data.get("requestDigest")):
        errors.append("$.requestDigest must be a non-empty string")
    if not _strings(data.get("immutableConstraints"), 1):
        errors.append("$.immutableConstraints must contain at least one string")

    visual = data.get("visualFacts")
    if not isinstance(visual, dict):
        errors.append("$.visualFacts must be an object")
    else:
        if visual.get("sourceMode") not in {"text", "image", "hybrid"}:
            errors.append("$.visualFacts.sourceMode is invalid")
        if not _strings(visual.get("hierarchy"), 1):
            errors.append("$.visualFacts.hierarchy must contain at least one string")
        for key in ("targetFrame", "backgroundStrategy"):
            if not _nonempty(visual.get(key)):
                errors.append(f"$.visualFacts.{key} must be a non-empty string")

    translation = data.get("directorTranslation")
    if not isinstance(translation, dict):
        errors.append("$.directorTranslation must be an object")
    else:
        for key in ("userIntent", "motionLogic", "memoryHook"):
            if not _nonempty(translation.get(key)):
                errors.append(f"$.directorTranslation.{key} must be a non-empty string")
        if not _strings(translation.get("tone"), 2):
            errors.append("$.directorTranslation.tone must contain at least two strings")

    energy = data.get("energyChain")
    if not isinstance(energy, dict):
        errors.append("$.energyChain must be an object")
    else:
        for key in ("driver", "anticipation", "primaryAction", "impactOrTurn", "settle"):
            if not _nonempty(energy.get(key)):
                errors.append(f"$.energyChain.{key} must be a non-empty string")
        if not _strings(energy.get("responses"), 1):
            errors.append("$.energyChain.responses must contain at least one causal response")

    poses = data.get("cameraKeyPoses")
    if not isinstance(poses, list) or len(poses) < 3:
        errors.append("$.cameraKeyPoses must contain at least three key poses")
    else:
        times: list[float] = []
        for index, pose in enumerate(poses):
            location = f"$.cameraKeyPoses[{index}]"
            if not isinstance(pose, dict):
                errors.append(f"{location} must be an object")
                continue
            time = pose.get("timeSeconds")
            if not isinstance(time, (int, float)) or isinstance(time, bool) or time < 0:
                errors.append(f"{location}.timeSeconds must be non-negative")
            else:
                times.append(float(time))
            for key in ("target", "pose", "purpose"):
                if not _nonempty(pose.get(key)):
                    errors.append(f"{location}.{key} must be a non-empty string")
            if not isinstance(pose.get("identity"), bool):
                errors.append(f"{location}.identity must be boolean")
        if len(times) == len(poses) and (times != sorted(times) or len(set(times)) != len(times)):
            errors.append("$.cameraKeyPoses times must be distinct and ascending")
        if isinstance(poses[-1], dict) and poses[-1].get("identity") is not True:
            errors.append("$.cameraKeyPoses final pose must have identity=true")

    directions = data.get("elementDirections")
    hero_count = 0
    if not isinstance(directions, list) or not directions:
        errors.append("$.elementDirections must be a non-empty array")
    else:
        names: set[str] = set()
        for index, direction in enumerate(directions):
            location = f"$.elementDirections[{index}]"
            if not isinstance(direction, dict):
                errors.append(f"{location} must be an object")
                continue
            name = direction.get("name")
            if not _nonempty(name):
                errors.append(f"{location}.name must be a non-empty string")
            elif name in names:
                errors.append(f"{location}.name must be unique")
            else:
                names.add(name)
            role = direction.get("motionRole")
            if role not in {"hero", "support", "reaction", "ambient"}:
                errors.append(f"{location}.motionRole is invalid")
            if role == "hero":
                hero_count += 1
                if not _strings(direction.get("phases"), 4):
                    errors.append(f"{location}.phases must contain at least four stages for the hero motion")
            elif not _strings(direction.get("phases"), 2):
                errors.append(f"{location}.phases must contain at least two stages")
            for key in ("trigger", "endState", "implementation"):
                if not _nonempty(direction.get(key)):
                    errors.append(f"{location}.{key} must be a non-empty string")
            bounds = direction.get("targetBounds")
            if bounds is not None and (not isinstance(bounds, list) or len(bounds) != 4 or any(not isinstance(item, (int, float)) or isinstance(item, bool) or item < 0 or item > 1 for item in bounds)):
                errors.append(f"{location}.targetBounds must be null or four numbers in 0..1")
        if hero_count != 1:
            errors.append("$.elementDirections must contain exactly one hero motion")

    if not _nonempty(data.get("timingStrategy")):
        errors.append("$.timingStrategy must be a non-empty string")
    if not _strings(data.get("parameterization")):
        errors.append("$.parameterization must be an array of strings")
    if not _strings(data.get("negativeConstraints"), 1):
        errors.append("$.negativeConstraints must contain at least one string")
    critique = data.get("selfCritique")
    if not isinstance(critique, dict):
        errors.append("$.selfCritique must be an object")
    else:
        for key in ("flatnessRisk", "fidelityRisk", "backgroundRisk"):
            if not _nonempty(critique.get(key)):
                errors.append(f"$.selfCritique.{key} must be a non-empty string")
        if not _strings(critique.get("corrections"), 1):
            errors.append("$.selfCritique.corrections must contain at least one string")
    return errors


def _fixture() -> dict[str, Any]:
    return {
        "visibility": "internal",
        "requestDigest": "Build a lively title intro from the approved reference.",
        "immutableConstraints": ["Preserve target geometry and dark background"],
        "visualFacts": {"sourceMode": "image", "hierarchy": ["Title", "Badge", "Icon"], "targetFrame": "Approved reference geometry", "backgroundStrategy": "Match sampled navy regions"},
        "directorTranslation": {"userIntent": "More natural and dynamic", "motionLogic": "The icon ignition transfers energy into the title build", "memoryHook": "One controlled ignition impact", "tone": ["dynamic", "precise"]},
        "energyChain": {"driver": "Play icon", "anticipation": "Outline gathers", "primaryAction": "Icon ignites", "impactOrTurn": "A short impact pulse", "responses": ["Camera recoils then settles"], "settle": "All owners reach target bounds"},
        "cameraKeyPoses": [
            {"timeSeconds": 0, "target": "Play icon", "pose": "Off-axis near", "purpose": "Establish depth", "identity": False},
            {"timeSeconds": 1.2, "target": "Title", "pose": "Impact recoil", "purpose": "Respond to ignition", "identity": False},
            {"timeSeconds": 3.9, "target": "Full frame", "pose": "Front-facing", "purpose": "Restore reference layout", "identity": True},
        ],
        "elementDirections": [{"name": "Play icon", "targetBounds": [0.78, 0.4, 0.18, 0.3], "motionRole": "hero", "trigger": "Timeline start", "phases": ["gather", "ignite", "impact", "settle"], "endState": "Reference bounds", "implementation": "SVG plus frame-driven transform"}],
        "timingStrategy": "Overlap responses at the primary action threshold and hold the result.",
        "parameterization": ["title", "accentColor"],
        "negativeConstraints": ["No full-frame reference overlay"],
        "selfCritique": {"flatnessRisk": "Avoid monotonic camera easing", "fidelityRisk": "Lock all target bounds", "backgroundRisk": "Do not lighten navy toward white", "corrections": ["Use event-linked recoil and sampled background colors"]},
    }


def run_self_test() -> int:
    valid = _fixture()
    if errors := validate(valid):
        print("Self-test failed: valid fixture was rejected", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    invalid = json.loads(json.dumps(valid))
    invalid["cameraKeyPoses"][-1]["identity"] = False
    invalid["elementDirections"][0]["phases"] = ["enter", "settle"]
    invalid["selfCritique"]["corrections"] = []
    errors = validate(invalid)
    expected = ("final pose", "at least four stages", "corrections")
    if any(not any(fragment in error for error in errors) for fragment in expected):
        print("Self-test failed: invalid fixture was accepted", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory(prefix="production-brief-") as directory:
        Path(directory, "fixture.json").write_text(json.dumps(valid, ensure_ascii=False), encoding="utf-8")
    print("Self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if args.brief is None:
        parser.error("brief is required unless --self-test is used")
    try:
        data = json.loads(args.brief.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read production brief: {error}", file=sys.stderr)
        return 1
    errors = validate(data)
    if errors:
        print("Internal production brief is invalid:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Internal production brief is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
