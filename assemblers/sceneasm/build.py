#!/usr/bin/env python3
"""SceneASM M2.0 adapter contract.

The CLI flags below are the C64Scene-side desired contract. Until SceneASM
implements/confirms this interface, fail explicitly rather than guessing.
"""
import argparse, os, shutil, subprocess, sys
ap=argparse.ArgumentParser()
ap.add_argument("source"); ap.add_argument("-o","--output",required=True)
ap.add_argument("--labels",required=True)
a=ap.parse_args()
exe=os.environ.get("SCENEASM","sceneasm")
path=shutil.which(exe)
if not path:
    print(f"SceneASM not found: {exe}",file=sys.stderr); raise SystemExit(2)

v=subprocess.run([path,"--version"],text=True,capture_output=True)
print((v.stdout or v.stderr).strip(),file=sys.stderr)

print("SceneASM adapter present, but CLI build contract is not yet qualified.",file=sys.stderr)
print("Required next: confirm SceneASM C64 target/output/symbol flags, then enable invocation.",file=sys.stderr)
raise SystemExit(3)
