#!/usr/bin/env python3
"""C64Scene adapter for the qualified SceneASM M2.0 CLI contract."""
import argparse, os, shutil, subprocess, sys

ap=argparse.ArgumentParser()
ap.add_argument("source")
ap.add_argument("-o","--output",required=True)
ap.add_argument("--labels",required=True)
a=ap.parse_args()

exe=os.environ.get("SCENEASM","sceneasm")
path=shutil.which(exe)
if not path:
    print(f"SceneASM not found: {exe}",file=sys.stderr)
    raise SystemExit(2)

v=subprocess.run([path,"--version"],text=True,capture_output=True)
print((v.stdout or v.stderr).strip(),file=sys.stderr)

cmd=[path,"build",a.source,"--target","c64","--output",a.output,"--symbols",a.labels]
raise SystemExit(subprocess.run(cmd).returncode)
