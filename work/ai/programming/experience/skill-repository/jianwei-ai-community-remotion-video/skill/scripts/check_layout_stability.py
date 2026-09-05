"""Check sampled layout boxes for deterministic geometry and settle stability."""
from __future__ import annotations
import argparse, json, sys

def main():
    p=argparse.ArgumentParser()
    p.add_argument("samples")
    p.add_argument("--max-drift",type=float,default=0.25)
    p.add_argument("--settle-from",type=int,default=0)
    a=p.parse_args()
    data=json.load(open(a.samples,encoding="utf-8"))
    frames=data.get("frames",[])
    if len(frames)<2: print("need at least two frames",file=sys.stderr); return 2
    names=set().union(*(f.get("elements",{}).keys() for f in frames))
    errors=[]
    for name in sorted(names):
        vals=[]
        for f in frames:
            box=f.get("elements",{}).get(name)
            if not isinstance(box,list) or len(box)<4: errors.append(f"{name}: missing box"); continue
            vals.append(box[:5])
        for i in range(1,len(vals)):
            if any(abs(vals[i][j]-vals[i-1][j])>a.max_drift for j in range(4)) and i>=a.settle_from:
                errors.append(f"{name}: drift between samples {i-1}->{i}: {vals[i-1]} -> {vals[i]}")
        widths={round(v[2],3) for v in vals}
        if len(widths)>1 and a.settle_from < len(vals): errors.append(f"{name}: width changes across samples: {sorted(widths)}")
    if errors:
        print("layout stability failed",file=sys.stderr)
        print("\n".join(errors),file=sys.stderr); return 1
    print(f"layout stability passed: {len(names)} elements, {len(frames)} samples")
    return 0
if __name__=="__main__": raise SystemExit(main())
