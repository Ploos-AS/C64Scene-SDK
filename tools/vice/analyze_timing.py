#!/usr/bin/env python3
"""Analyze C64Scene raster timing samples.

Input CSV (header required):
frame,line,cycle

PASS criterion defaults to identical line/cycle for every sample.
"""
import argparse, csv, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("samples")
    ap.add_argument("--min-frames", type=int, default=120)
    ap.add_argument("--result", default="build/qualification/double-irq-timing.result")
    args=ap.parse_args()

    rows=[]
    with open(args.samples, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append((int(r["frame"]), int(r["line"]), int(r["cycle"])))

    out=Path(args.result)
    out.parent.mkdir(parents=True, exist_ok=True)

    if len(rows) < args.min_frames:
        result=["status=UNQUALIFIED", "reason=INSUFFICIENT_SAMPLES",
                f"samples={len(rows)}", f"required={args.min_frames}"]
        out.write_text("\n".join(result)+"\n")
        return 2

    positions={(line,cycle) for _,line,cycle in rows}
    lines=[x[1] for x in rows]
    cycles=[x[2] for x in rows]
    stable=len(positions)==1
    result=[
        "status=" + ("QUALIFIED_PASS" if stable else "QUALIFIED_FAIL"),
        f"samples={len(rows)}",
        f"unique_positions={len(positions)}",
        f"line_min={min(lines)}",
        f"line_max={max(lines)}",
        f"cycle_min={min(cycles)}",
        f"cycle_max={max(cycles)}",
        f"cycle_jitter={max(cycles)-min(cycles)}",
    ]
    if stable:
        line,cycle=next(iter(positions))
        result += [f"stable_line={line}", f"stable_cycle={cycle}"]
    out.write_text("\n".join(result)+"\n")
    print("\n".join(result))
    return 0 if stable else 1

if __name__=="__main__":
    sys.exit(main())
