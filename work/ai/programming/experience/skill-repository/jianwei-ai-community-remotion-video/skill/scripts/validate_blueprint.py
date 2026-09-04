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
    "referenceFidelity",
    "creativeDirection",
    "motionSystem",
    "timeline",
    "parameterization",
    "remotionPlan",
    "renderPipeline",
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


def validate_reference_fidelity(value: Any, input_mode: Any, errors: list[str]) -> None:
    location = "$.referenceFidelity"
    if input_mode == "text":
        if value is not None:
            errors.append(f"{location} must be null for text input")
        return
    if not isinstance(value, dict):
        errors.append(f"{location} must be an object for image or hybrid input")
        return
    require_keys(
        value,
        ("mode", "renderPolicy", "terminalOverlay", "targetLayoutLocked", "sourceWidth", "sourceHeight", "backgroundProfile", "exactCopy", "protectedElements", "allowedDifferences", "criticalRegions", "visualOwners", "finalHoldFrames", "finalFrameRule", "comparisonMethod"),
        location,
        errors,
    )
    if value.get("mode") not in {"layout-locked", "raster-motion", "approved-redesign"}:
        errors.append(f"{location}.mode is invalid")
    if value.get("renderPolicy") not in {"reconstructed-elements-only", "single-raster-plane", "approved-reconstruction-differences"}:
        errors.append(f"{location}.renderPolicy is invalid")
    if value.get("terminalOverlay") is not False:
        errors.append(f"{location}.terminalOverlay must be false; a full-frame terminal overlay is forbidden")
    if value.get("targetLayoutLocked") is not True:
        errors.append(f"{location}.targetLayoutLocked must be true")
    expected_policy = {
        "layout-locked": "reconstructed-elements-only",
        "raster-motion": "single-raster-plane",
        "approved-redesign": "approved-reconstruction-differences",
    }.get(value.get("mode"))
    if expected_policy and value.get("renderPolicy") != expected_policy:
        errors.append(f"{location}.renderPolicy must be {expected_policy} for mode {value.get('mode')}")
    for key in ("sourceWidth", "sourceHeight"):
        dimension = value.get(key)
        if not isinstance(dimension, int) or isinstance(dimension, bool) or dimension <= 0:
            errors.append(f"{location}.{key} must be a positive integer")
    background = value.get("backgroundProfile")
    background_location = f"{location}.backgroundProfile"
    require_keys(background, ("classification", "protected", "sampleRegions", "reconstructionMethod", "dynamicPolicy"), background_location, errors)
    if isinstance(background, dict):
        if background.get("classification") not in {"flat", "gradient", "texture", "image", "transparent", "mixed"}:
            errors.append(f"{background_location}.classification is invalid")
        if background.get("protected") is not True:
            errors.append(f"{background_location}.protected must be true")
        for key in ("reconstructionMethod", "dynamicPolicy"):
            if not isinstance(background.get(key), str) or not background.get(key, "").strip():
                errors.append(f"{background_location}.{key} must be a non-empty string")
        samples = background.get("sampleRegions")
        if not isinstance(samples, list) or len(samples) < 3:
            errors.append(f"{background_location}.sampleRegions must contain at least three safe regions")
        else:
            for index, sample in enumerate(samples):
                sample_location = f"{background_location}.sampleRegions[{index}]"
                require_keys(sample, ("name", "normalizedBounds", "meanRgb", "relativeLuminance"), sample_location, errors)
                if not isinstance(sample, dict):
                    continue
                if not isinstance(sample.get("name"), str) or not sample.get("name", "").strip():
                    errors.append(f"{sample_location}.name must be a non-empty string")
                bounds = sample.get("normalizedBounds")
                if not isinstance(bounds, list) or len(bounds) != 4 or any(not is_number(item) or item < 0 or item > 1 for item in bounds):
                    errors.append(f"{sample_location}.normalizedBounds must contain four numbers in the 0..1 range")
                elif bounds[2] <= 0 or bounds[3] <= 0 or bounds[0] + bounds[2] > 1 or bounds[1] + bounds[3] > 1:
                    errors.append(f"{sample_location}.normalizedBounds must have positive size and stay inside the canvas")
                mean_rgb = sample.get("meanRgb")
                if not isinstance(mean_rgb, list) or len(mean_rgb) != 3 or any(not is_number(item) or item < 0 or item > 255 for item in mean_rgb):
                    errors.append(f"{sample_location}.meanRgb must contain three numbers in the 0..255 range")
                luminance = sample.get("relativeLuminance")
                if not is_number(luminance) or luminance < 0 or luminance > 1:
                    errors.append(f"{sample_location}.relativeLuminance must be in the 0..1 range")
    require_string_list(value.get("exactCopy"), f"{location}.exactCopy", errors)
    require_string_list(value.get("protectedElements"), f"{location}.protectedElements", errors, 1)
    require_string_list(value.get("allowedDifferences"), f"{location}.allowedDifferences", errors)
    for key in ("finalFrameRule", "comparisonMethod"):
        if not isinstance(value.get(key), str) or not value.get(key, "").strip():
            errors.append(f"{location}.{key} must be a non-empty string")
    regions = value.get("criticalRegions")
    if not isinstance(regions, list) or not regions:
        errors.append(f"{location}.criticalRegions must be a non-empty array")
    else:
        for index, region in enumerate(regions):
            region_location = f"{location}.criticalRegions[{index}]"
            require_keys(region, ("name", "role", "normalizedBounds", "tolerancePercent"), region_location, errors)
            if not isinstance(region, dict):
                continue
            for key in ("name", "role"):
                if not isinstance(region.get(key), str) or not region.get(key, "").strip():
                    errors.append(f"{region_location}.{key} must be a non-empty string")
            bounds = region.get("normalizedBounds")
            if not isinstance(bounds, list) or len(bounds) != 4 or any(not is_number(item) or item < 0 or item > 1 for item in bounds):
                errors.append(f"{region_location}.normalizedBounds must contain four numbers in the 0..1 range")
            tolerance = region.get("tolerancePercent")
            if not is_number(tolerance) or tolerance < 0 or tolerance > 10:
                errors.append(f"{region_location}.tolerancePercent must be between 0 and 10")
    owners = value.get("visualOwners")
    if not isinstance(owners, list) or not owners:
        errors.append(f"{location}.visualOwners must be a non-empty array")
    else:
        owner_names: set[str] = set()
        for index, owner in enumerate(owners):
            owner_location = f"{location}.visualOwners[{index}]"
            require_keys(owner, ("name", "normalizedBounds", "ownerType", "editable", "finalState"), owner_location, errors)
            if not isinstance(owner, dict):
                continue
            name = owner.get("name")
            if not isinstance(name, str) or not name.strip():
                errors.append(f"{owner_location}.name must be a non-empty string")
            elif name in owner_names:
                errors.append(f"{owner_location}.name must be unique")
            else:
                owner_names.add(name)
            bounds = owner.get("normalizedBounds")
            if not isinstance(bounds, list) or len(bounds) != 4 or any(not is_number(item) or item < 0 or item > 1 for item in bounds):
                errors.append(f"{owner_location}.normalizedBounds must contain four numbers in the 0..1 range")
            if owner.get("ownerType") not in {"text", "number", "logo", "icon", "shape", "image-crop", "background-plate", "svg", "canvas", "three", "other"}:
                errors.append(f"{owner_location}.ownerType is invalid")
            if not isinstance(owner.get("editable"), bool):
                errors.append(f"{owner_location}.editable must be boolean")
            if not isinstance(owner.get("finalState"), str) or not owner.get("finalState", "").strip():
                errors.append(f"{owner_location}.finalState must be a non-empty string")
    hold_frames = value.get("finalHoldFrames")
    if not isinstance(hold_frames, list) or len(hold_frames) != 3 or any(not isinstance(frame, int) or isinstance(frame, bool) or frame < 0 for frame in hold_frames):
        errors.append(f"{location}.finalHoldFrames must contain exactly three non-negative integer frames")
    elif hold_frames != sorted(set(hold_frames)) or len(set(hold_frames)) != 3:
        errors.append(f"{location}.finalHoldFrames must be three distinct frames in ascending order")


def validate_render_pipeline(value: Any, errors: list[str]) -> None:
    location = "$.renderPipeline"
    require_keys(
        value,
        ("previewFirst", "previewScale", "previewMaxLongEdge", "previewCodec", "finalRenderRequiresApproval", "finalApprovalStatus", "finalApprovalEvidence", "rendererPolicy", "performanceNotes"),
        location,
        errors,
    )
    if not isinstance(value, dict):
        return
    if value.get("previewFirst") is not True:
        errors.append(f"{location}.previewFirst must be true")
    scale = value.get("previewScale")
    if not is_number(scale) or scale <= 0 or scale > 1:
        errors.append(f"{location}.previewScale must be greater than 0 and at most 1")
    max_edge = value.get("previewMaxLongEdge")
    if not isinstance(max_edge, int) or isinstance(max_edge, bool) or max_edge < 320:
        errors.append(f"{location}.previewMaxLongEdge must be an integer of at least 320")
    if not isinstance(value.get("previewCodec"), str) or not value.get("previewCodec", "").strip():
        errors.append(f"{location}.previewCodec must be a non-empty string")
    if value.get("finalRenderRequiresApproval") is not True:
        errors.append(f"{location}.finalRenderRequiresApproval must be true")
    status = value.get("finalApprovalStatus")
    if status not in {"pending", "approved", "waived"}:
        errors.append(f"{location}.finalApprovalStatus is invalid")
    evidence = value.get("finalApprovalEvidence")
    if status in {"approved", "waived"} and (not isinstance(evidence, str) or not evidence.strip()):
        errors.append(f"{location}.finalApprovalEvidence must quote explicit final-render approval")
    if status == "pending" and evidence is not None:
        errors.append(f"{location}.finalApprovalEvidence must be null while finalApprovalStatus is pending")
    if value.get("rendererPolicy") not in {"default-first", "software-fallback", "software-only"}:
        errors.append(f"{location}.rendererPolicy is invalid")
    if not isinstance(value.get("performanceNotes"), str) or not value.get("performanceNotes", "").strip():
        errors.append(f"{location}.performanceNotes must be a non-empty string")


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
        validate_reference_fidelity(data.get("referenceFidelity"), input_mode, errors)
        reference = data.get("referenceFidelity")
        if isinstance(reference, dict) and isinstance(request.get("durationSeconds"), (int, float)) and isinstance(request.get("fps"), int):
            max_frame = math.ceil(request["durationSeconds"] * request["fps"]) - 1
            for index, frame in enumerate(reference.get("finalHoldFrames", [])):
                if isinstance(frame, int) and not isinstance(frame, bool) and frame > max_frame:
                    errors.append(f"$.referenceFidelity.finalHoldFrames[{index}] must be within the composition ({max_frame} max)")
    elif "referenceFidelity" in data:
        validate_reference_fidelity(data.get("referenceFidelity"), None, errors)

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
    require_keys(
        creative,
        (
            "concept",
            "targetFrame",
            "stateContrast",
            "memoryHook",
            "memoryHookTime",
            "payoff",
            "timingOverlap",
            "styleWords",
            "intensity",
            "spatialModel",
        ),
        "$.creativeDirection",
        errors,
    )
    if isinstance(creative, dict):
        for key in ("concept", "targetFrame", "stateContrast", "memoryHook", "payoff", "timingOverlap"):
            if not isinstance(creative.get(key), str) or not creative.get(key, "").strip():
                errors.append(f"$.creativeDirection.{key} must be a non-empty string")
        hook_time = creative.get("memoryHookTime")
        require_keys(hook_time, ("startSeconds", "endSeconds"), "$.creativeDirection.memoryHookTime", errors)
        if isinstance(hook_time, dict):
            hook_start = hook_time.get("startSeconds")
            hook_end = hook_time.get("endSeconds")
            if not is_number(hook_start) or not is_number(hook_end) or hook_start < 0 or hook_end <= hook_start:
                errors.append("$.creativeDirection.memoryHookTime must have endSeconds greater than startSeconds")
            elif isinstance(request, dict) and is_number(request.get("durationSeconds")) and hook_end > request["durationSeconds"]:
                errors.append("$.creativeDirection.memoryHookTime must fit inside the composition duration")
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
        coverage_end = 0.0
        previous_start = -1.0
        for index, item in enumerate(timeline):
            location = f"$.timeline[{index}]"
            require_keys(
                item,
                ("startSeconds", "endSeconds", "beat", "pictureAction", "camera", "focusAndLayers", "causalOverlap", "audioCue", "implementation"),
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
            if index == 0 and abs(start) > 0.001:
                errors.append("$.timeline[0].startSeconds must be 0")
            if start + 0.001 < previous_start:
                errors.append(f"{location}.startSeconds must be in non-decreasing order")
            if start - coverage_end > 0.001:
                errors.append(f"{location}.startSeconds leaves an uncovered gap after {coverage_end:g}s")
            if not isinstance(item.get("causalOverlap"), str) or not item.get("causalOverlap", "").strip():
                errors.append(f"{location}.causalOverlap must be a non-empty string")
            previous_start = float(start)
            coverage_end = max(coverage_end, float(end))
        if is_number(duration) and abs(coverage_end - float(duration)) > 0.001:
            errors.append("$.timeline coverage must end at $.request.durationSeconds")

    parameterization = data.get("parameterization")
    require_keys(
        parameterization,
        ("mode", "editableInStudio", "fields", "testValues", "artifactNote"),
        "$.parameterization",
        errors,
    )
    if isinstance(parameterization, dict):
        mode = parameterization.get("mode")
        editable = parameterization.get("editableInStudio")
        fields = parameterization.get("fields")
        test_values = parameterization.get("testValues")
        if mode not in {"parameterized", "fixed"}:
            errors.append("$.parameterization.mode must be parameterized or fixed")
        if not isinstance(editable, bool):
            errors.append("$.parameterization.editableInStudio must be a boolean")
        if mode == "parameterized" and editable is not True:
            errors.append("$.parameterization.editableInStudio must be true in parameterized mode")
        if mode == "fixed" and editable is not False:
            errors.append("$.parameterization.editableInStudio must be false in fixed mode")
        if not isinstance(fields, list):
            errors.append("$.parameterization.fields must be an array")
            fields = []
        elif mode == "parameterized" and len(fields) < 2:
            errors.append("$.parameterization.fields must contain at least 2 fields in parameterized mode")
        field_names: set[str] = set()
        field_types: set[str] = set()
        for index, field in enumerate(fields):
            location = f"$.parameterization.fields[{index}]"
            require_keys(field, ("name", "type", "defaultValue", "purpose", "validation", "boundElements"), location, errors)
            if not isinstance(field, dict):
                continue
            name = field.get("name")
            field_type = field.get("type")
            if not isinstance(name, str) or not name.strip():
                errors.append(f"{location}.name must be a non-empty string")
            elif name in field_names:
                errors.append(f"{location}.name must be unique")
            else:
                field_names.add(name)
            if field_type not in {"string", "number", "color", "boolean", "select"}:
                errors.append(f"{location}.type is invalid")
            else:
                field_types.add(field_type)
            for key in ("purpose", "validation"):
                if not isinstance(field.get(key), str) or not field.get(key, "").strip():
                    errors.append(f"{location}.{key} must be a non-empty string")
            require_string_list(field.get("boundElements"), f"{location}.boundElements", errors, 1)
        if mode == "parameterized":
            if "string" not in field_types:
                errors.append("$.parameterization.fields must include a string field in parameterized mode")
            if "color" not in field_types:
                errors.append("$.parameterization.fields must include a color field in parameterized mode")
            if not isinstance(test_values, dict) or not test_values:
                errors.append("$.parameterization.testValues must contain a non-default parameter set")
            elif not set(test_values).issubset(field_names):
                errors.append("$.parameterization.testValues contains names not declared in fields")
        elif not isinstance(test_values, dict):
            errors.append("$.parameterization.testValues must be an object")
        if not isinstance(parameterization.get("artifactNote"), str) or not parameterization.get("artifactNote", "").strip():
            errors.append("$.parameterization.artifactNote must be a non-empty string")

    plan = data.get("remotionPlan")
    require_keys(plan, ("compositionId", "components", "packages", "editableProps", "documentationToLoad", "checkFrames"), "$.remotionPlan", errors)
    if isinstance(plan, dict):
        require_string_list(plan.get("components"), "$.remotionPlan.components", errors, 1)
        require_string_list(plan.get("packages"), "$.remotionPlan.packages", errors)
        require_string_list(plan.get("editableProps"), "$.remotionPlan.editableProps", errors)
        require_string_list(plan.get("documentationToLoad"), "$.remotionPlan.documentationToLoad", errors, 1)
        if isinstance(parameterization, dict) and parameterization.get("mode") == "parameterized":
            docs = plan.get("documentationToLoad")
            packages = plan.get("packages")
            editable_props = plan.get("editableProps")
            if isinstance(docs, list):
                if not any("remotion-interactivity" in item for item in docs):
                    errors.append("$.remotionPlan.documentationToLoad must include remotion-interactivity in parameterized mode")
                if not any("parameters" in item for item in docs):
                    errors.append("$.remotionPlan.documentationToLoad must include the Remotion parameters guidance")
            if isinstance(packages, list):
                if "zod" not in packages:
                    errors.append("$.remotionPlan.packages must include zod in parameterized mode")
                if "@remotion/zod-types" not in packages:
                    errors.append("$.remotionPlan.packages must include @remotion/zod-types in parameterized mode")
            if isinstance(editable_props, list) and not field_names.issubset(set(editable_props)):
                errors.append("$.remotionPlan.editableProps must include every declared parameter field")
        check_frames = plan.get("checkFrames")
        if not isinstance(check_frames, list) or len(check_frames) < 3 or any(not isinstance(frame, int) or isinstance(frame, bool) or frame < 0 for frame in check_frames):
            errors.append("$.remotionPlan.checkFrames must contain at least 3 non-negative integers")

    validate_render_pipeline(data.get("renderPipeline"), errors)

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
        "referenceFidelity": None,
        "creativeDirection": {
            "concept": "One controlled bounce",
            "targetFrame": "A front-facing card resting at the center",
            "stateContrast": "Compressed and tense to released and stable",
            "memoryHook": "The landing compression",
            "memoryHookTime": {"startSeconds": 0.72, "endSeconds": 1.02},
            "payoff": "The shadow catches up one beat after the card settles",
            "timingOverlap": "The shadow reaction begins when the card passes 80 percent of its landing path",
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
            {"startSeconds": 0, "endSeconds": 0.5, "beat": "Anticipate", "pictureAction": "Card compresses", "camera": "Static", "focusAndLayers": "Card and shadow", "causalOverlap": "Opening beat; no prior overlap", "audioCue": None, "implementation": "CSS and interpolate"},
            {"startSeconds": 0.35, "endSeconds": 1.25, "beat": "Release", "pictureAction": "Card overshoots and returns", "camera": "Push in", "focusAndLayers": "Card center", "causalOverlap": "Starts when compression reaches 70 percent", "audioCue": "Landing", "implementation": "Easing.spring"},
            {"startSeconds": 1.05, "endSeconds": 2, "beat": "Hold", "pictureAction": "Card settles", "camera": "Locked", "focusAndLayers": "Final card", "causalOverlap": "Starts during the final deceleration", "audioCue": None, "implementation": "Clamped interpolate"},
        ],
        "parameterization": {
            "mode": "parameterized",
            "editableInStudio": True,
            "fields": [
                {"name": "title", "type": "string", "defaultValue": "Launch", "purpose": "Main card copy", "validation": "Maximum 24 characters", "boundElements": ["Card title"]},
                {"name": "accentColor", "type": "color", "defaultValue": "#0B84FF", "purpose": "Card accent and shadow response", "validation": "Must retain readable contrast", "boundElements": ["Card", "Shadow"]},
            ],
            "testValues": {"title": "New title", "accentColor": "#FF3B30"},
            "artifactNote": "The MP4 is a rendered parameter snapshot; the Remotion project is editable in Studio",
        },
        "remotionPlan": {
            "compositionId": "CardBounce",
            "components": ["CardBounce"],
            "packages": ["remotion", "zod", "@remotion/zod-types"],
            "editableProps": ["title", "accentColor"],
            "documentationToLoad": ["remotion-markup", "remotion-interactivity", "remotion-markup/parameters"],
            "checkFrames": [0, 24, 48],
        },
        "renderPipeline": {
            "previewFirst": True,
            "previewScale": 0.5,
            "previewMaxLongEdge": 960,
            "previewCodec": "H.264 MP4 CRF 28",
            "finalRenderRequiresApproval": True,
            "finalApprovalStatus": "pending",
            "finalApprovalEvidence": None,
            "rendererPolicy": "default-first",
            "performanceNotes": "Reuse the same Composition and timing; report actual renderer and elapsed time",
        },
        "quality": {
            "acceptanceCriteria": ["Card is readable at the landing"],
            "evidenceRequired": ["Three representative frames"],
        },
    }
    valid_errors = validate(valid)
    fixed = json.loads(json.dumps(valid))
    fixed["parameterization"] = {
        "mode": "fixed",
        "editableInStudio": False,
        "fields": [],
        "testValues": {},
        "artifactNote": "This delivery is a fixed render and is not parameter-editable in Studio",
    }
    fixed["remotionPlan"]["editableProps"] = []
    fixed_errors = validate(fixed)
    invalid = json.loads(json.dumps(valid))
    invalid["request"]["inputMode"] = "image"
    invalid["timeline"][1]["startSeconds"] = 0.8
    invalid["approval"]["evidence"] = "Not approved"
    invalid["parameterization"]["editableInStudio"] = False
    invalid["parameterization"]["fields"] = invalid["parameterization"]["fields"][:1]
    invalid_errors = validate(invalid)
    image_valid = json.loads(json.dumps(valid))
    image_valid["request"]["inputMode"] = "image"
    image_valid["visualAnalysis"] = {
        "observed": ["A single centered card"],
        "hierarchy": ["Card", "Shadow"],
        "coreVisual": "A card lands with a tactile bounce",
        "preserve": ["Card silhouette"],
        "mayChange": ["Card position during entry"],
        "layerCandidates": [{"name": "Card", "role": "hero", "depth": 0, "source": "reconstructed DOM", "editable": True}],
        "risks": ["Font metrics"],
    }
    image_valid["referenceFidelity"] = {
        "mode": "layout-locked",
        "renderPolicy": "reconstructed-elements-only",
        "terminalOverlay": False,
        "targetLayoutLocked": True,
        "sourceWidth": 1920,
        "sourceHeight": 1080,
        "backgroundProfile": {
            "classification": "flat",
            "protected": True,
            "sampleRegions": [
                {"name": "top-left", "normalizedBounds": [0.0, 0.0, 0.1, 0.1], "meanRgb": [1, 8, 42], "relativeLuminance": 0.03},
                {"name": "top-center", "normalizedBounds": [0.45, 0.0, 0.1, 0.1], "meanRgb": [1, 8, 42], "relativeLuminance": 0.03},
                {"name": "bottom-left", "normalizedBounds": [0.0, 0.8, 0.1, 0.1], "meanRgb": [1, 8, 42], "relativeLuminance": 0.03},
            ],
            "reconstructionMethod": "Sampled solid background",
            "dynamicPolicy": "Temporary local light only; return to samples before hold",
        },
        "exactCopy": ["Card title"],
        "protectedElements": ["Card silhouette"],
        "allowedDifferences": [],
        "criticalRegions": [{"name": "Card", "role": "hero", "normalizedBounds": [0.2, 0.2, 0.6, 0.4], "tolerancePercent": 1}],
        "visualOwners": [{"name": "Card", "normalizedBounds": [0.2, 0.2, 0.6, 0.4], "ownerType": "shape", "editable": True, "finalState": "Front-facing card at rest"}],
        "finalHoldFrames": [48, 54, 59],
        "finalFrameRule": "The same Card component reaches the target bounds; no full-frame reference layer",
        "comparisonMethod": "Compare same-size PNG and three final-hold frames",
    }
    image_errors = validate(image_valid)
    image_overlay = json.loads(json.dumps(image_valid))
    image_overlay["referenceFidelity"]["terminalOverlay"] = True
    image_overlay_errors = validate(image_overlay)
    image_background = json.loads(json.dumps(image_valid))
    image_background["referenceFidelity"]["backgroundProfile"]["protected"] = False
    image_background["referenceFidelity"]["backgroundProfile"]["sampleRegions"] = image_background["referenceFidelity"]["backgroundProfile"]["sampleRegions"][:2]
    image_background_errors = validate(image_background)
    if valid_errors:
        print("Self-test failed: valid fixture was rejected", file=sys.stderr)
        for error in valid_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if fixed_errors:
        print("Self-test failed: fixed-mode fixture was rejected", file=sys.stderr)
        for error in fixed_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if image_errors:
        print("Self-test failed: valid image fixture was rejected", file=sys.stderr)
        for error in image_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if not any("terminalOverlay must be false" in error for error in image_overlay_errors):
        print("Self-test failed: terminal overlay was not rejected", file=sys.stderr)
        for error in image_overlay_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    expected_background_fragments = ("protected must be true", "at least three safe regions")
    if any(not any(fragment in error for error in image_background_errors) for fragment in expected_background_fragments):
        print("Self-test failed: invalid background profile was not rejected", file=sys.stderr)
        for error in image_background_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    expected_invalid_fragments = (
        "visualAnalysis is required",
        "evidence must be null",
        "uncovered gap",
        "editableInStudio must be true",
        "at least 2 fields",
    )
    if any(not any(fragment in error for error in invalid_errors) for fragment in expected_invalid_fragments):
        print("Self-test failed: invalid fixture was not rejected", file=sys.stderr)
        for error in invalid_errors:
            print(f"- {error}", file=sys.stderr)
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
