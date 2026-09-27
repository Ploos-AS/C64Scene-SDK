#!/usr/bin/env python3
"""Collect repeated VICE textual-monitor checkpoint timing hits.

Input is raw VICE monitor output on stdin. Output is canonical timing markers.
This collector is deliberately independent of process control.
"""
import argparse,re,sys
ap=argparse.ArgumentParser()
ap.add_argument("--frames",type=int,default=120)
a=ap.parse_args()
rx=re.compile(r"^#\d+\s+\(Stop on\s+exec\s+[0-9a-fA-F]+\)\s+(\d+)/\$[0-9a-fA-F]+,\s+(\d+)/\$[0-9a-fA-F]+")
n=0
for raw in sys.stdin:
    m=rx.match(raw.strip())
    if not m: continue
    n+=1
    line,cycle=m.groups()
    print(f"C64SCENE_TIMING frame={n} line={line} cycle={cycle}")
    if n>=a.frames: break
if n<a.frames:
    print(f"insufficient checkpoint hits: {n}/{a.frames}",file=sys.stderr)
    raise SystemExit(2)
