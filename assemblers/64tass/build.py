#!/usr/bin/env python3
import argparse, os, shutil, subprocess
ap=argparse.ArgumentParser()
ap.add_argument("source"); ap.add_argument("-o","--output",required=True)
ap.add_argument("--labels",required=True)
a=ap.parse_args()
exe=os.environ.get("ASM","64tass")
if not shutil.which(exe):
    raise SystemExit(f"64tass not found: {exe}")
cmd=[exe,"--cbm-prg","-Wall","-a","-B","-L",a.labels,"-o",a.output,a.source]
raise SystemExit(subprocess.run(cmd).returncode)
