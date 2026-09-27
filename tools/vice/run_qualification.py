#!/usr/bin/env python3
"""End-to-end C64Scene timing qualification from canonical evidence."""
import argparse,subprocess,sys
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument("raw_log")
ap.add_argument("--frames",type=int,default=120)
ap.add_argument("--outdir",default="build/qualification")
a=ap.parse_args()
out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True)
canonical=out/"double-irq-canonical.log"
samples=out/"double-irq-samples.csv"
result=out/"double-irq-timing.result"

with open(a.raw_log,encoding="utf-8",errors="replace") as src:
    p=subprocess.run([sys.executable,"tools/vice/collect_checkpoint_hits.py","--frames",str(a.frames)],
                     stdin=src,text=True,capture_output=True)
canonical.write_text(p.stdout)
if p.returncode:
    result.write_text(f"status=UNQUALIFIED\nreason=INSUFFICIENT_CHECKPOINT_HITS\nrequired={a.frames}\n")
    print(p.stderr,end="",file=sys.stderr); raise SystemExit(p.returncode)

subprocess.run([sys.executable,"tools/vice/extract_samples.py",str(canonical),
                "--min-samples",str(a.frames),"--output",str(samples)],check=True)
raise SystemExit(subprocess.run([sys.executable,"tools/vice/analyze_timing.py",str(samples),
                "--min-frames",str(a.frames),"--result",str(result)]).returncode)
