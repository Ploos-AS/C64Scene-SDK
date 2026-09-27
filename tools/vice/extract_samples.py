#!/usr/bin/env python3
"""Extract explicit C64Scene timing markers from VICE-derived logs.

Accepted evidence line:
C64SCENE_TIMING frame=<n> line=<n> cycle=<n>

The marker must be emitted by a verified VICE adapter/monitor workflow.
Unknown monitor text is deliberately ignored rather than guessed.
"""
import argparse, csv, re, sys
from pathlib import Path

RX=re.compile(r"^C64SCENE_TIMING\s+frame=(\d+)\s+line=(\d+)\s+cycle=(\d+)\s*$")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--output", default="build/qualification/double-irq-samples.csv")
    ap.add_argument("--min-samples", type=int, default=1)
    args=ap.parse_args()

    rows=[]
    with open(args.log, encoding="utf-8", errors="replace") as f:
        for line in f:
            m=RX.match(line.strip())
            if m:
                rows.append(tuple(map(int,m.groups())))

    out=Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    if len(rows) < args.min_samples:
        print(f"no sufficient explicit timing evidence: {len(rows)} sample(s)", file=sys.stderr)
        return 2

    frames=[r[0] for r in rows]
    if len(frames) != len(set(frames)):
        print("duplicate frame identifiers in timing evidence", file=sys.stderr)
        return 3
    if frames != sorted(frames):
        print("non-monotonic frame identifiers in timing evidence", file=sys.stderr)
        return 4

    with out.open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["frame","line","cycle"])
        w.writerows(rows)
    print(f"wrote {len(rows)} samples to {out}")
    return 0

if __name__=="__main__":
    sys.exit(main())
