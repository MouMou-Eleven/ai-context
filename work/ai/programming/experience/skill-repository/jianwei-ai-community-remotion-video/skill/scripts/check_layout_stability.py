"""Check sampled layout boxes, baselines, fonts, and settle stability."""
from __future__ import annotations
import argparse, json, sys

def _box(value):
    if isinstance(value, dict):
        value = value.get("bounds", value.get("box"))
    if not isinstance(value, list) or len(value) < 4:
        return None
    try:
        return [float(v) for v in value[:5]]
    except (TypeError, ValueError):
        return None

def main():
    p=argparse.ArgumentParser()
    p.add_argument("samples", nargs="?")
    p.add_argument("--max-drift",type=float,default=0.25)
    p.add_argument("--settle-from",type=int,default=0)
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test:
        import tempfile
        fixtures = [
            {"settleFrom": 2, "frames": [{"elements": {"title": [10, 20, 100, 30, 24]}}, {"elements": {"title": [11, 20, 100, 30, 24]}}, {"elements": {"title": {"bounds": [11, 20, 100, 30, 24], "fontSignature": "Inter-700-32"}}}, {"elements": {"title": {"bounds": [11, 20, 100, 30, 24], "fontSignature": "Inter-700-32"}}}]},
            {"frames": [{"elements": {"title": [10, 20, 100, 30]}}, {"elements": {"title": [10, 23, 100, 30]}}]},
        ]
        with tempfile.TemporaryDirectory(prefix="layout-stability-") as d:
            path = f"{d}/valid.json"
            with open(path, "w", encoding="utf-8") as h: json.dump(fixtures[0], h)
            if _run(path, 0.25, 2) != 0: return 1
            path = f"{d}/invalid.json"
            with open(path, "w", encoding="utf-8") as h: json.dump(fixtures[1], h)
            if _run(path, 0.25, 0) == 0: return 1
        print("layout stability self-test passed")
        return 0
    if not a.samples:
        p.error("samples is required unless --self-test is used")
    return _run(a.samples, a.max_drift, a.settle_from)

def _run(path, max_drift, settle_from):
    data=json.load(open(path,encoding="utf-8"))
    frames=data.get("frames",[])
    if len(frames)<2: print("need at least two frames",file=sys.stderr); return 2
    names=set().union(*(f.get("elements",{}).keys() for f in frames))
    errors=[]
    for name in sorted(names):
        vals=[]
        for f in frames:
            raw=f.get("elements",{}).get(name)
            box=_box(raw)
            if box is None: errors.append(f"{name}: missing box"); continue
            vals.append((box, raw))
        for i in range(1,len(vals)):
            if i>=settle_from and any(abs(vals[i][0][j]-vals[i-1][0][j])>max_drift for j in range(min(5, len(vals[i][0]), len(vals[i-1][0])))):
                errors.append(f"{name}: drift between samples {i-1}->{i}: {vals[i-1][0]} -> {vals[i][0]}")
        stable=vals[max(0, settle_from):]
        widths={round(v[0][2],3) for v in stable}
        if len(widths)>1: errors.append(f"{name}: width changes in settle: {sorted(widths)}")
        signatures={v[1].get("fontSignature") for v in stable if isinstance(v[1], dict) and v[1].get("fontSignature")}
        if len(signatures)>1: errors.append(f"{name}: font signature changes in settle: {sorted(signatures)}")
    if errors:
        print("layout stability failed",file=sys.stderr)
        print("\n".join(errors),file=sys.stderr); return 1
    print(f"layout stability passed: {len(names)} elements, {len(frames)} samples")
    return 0
if __name__=="__main__": raise SystemExit(main())
