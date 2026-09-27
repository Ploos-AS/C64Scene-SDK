#!/usr/bin/env python3
"""C64Scene assembler-neutral build entry point."""
import argparse, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BACKENDS=ROOT/"assemblers"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("-o","--output",required=True)
    ap.add_argument("--labels",required=True)
    ap.add_argument("--assembler",default=os.environ.get("C64SCENE_ASSEMBLER","64tass"),
                    choices=["64tass","sceneasm"])
    args=ap.parse_args()
    adapter=BACKENDS/args.assembler/"build.py"
    cmd=[sys.executable,str(adapter),args.source,"-o",args.output,"--labels",args.labels]
    return subprocess.run(cmd,cwd=ROOT).returncode

if __name__=="__main__":
    raise SystemExit(main())
