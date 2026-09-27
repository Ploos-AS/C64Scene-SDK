#!/usr/bin/env python3
"""Run a version-aware VICE timing probe.

This runner never fabricates raster/cycle observations. A backend must emit
canonical C64SCENE_TIMING markers. Until a verified backend is selected for
the detected VICE version, the result remains UNQUALIFIED.
"""
import argparse, os, shutil, subprocess, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--vice", default=os.environ.get("VICE","x64sc"))
    ap.add_argument("--prg", default="build/double-irq.prg")
    ap.add_argument("--outdir", default="build/qualification")
    args=ap.parse_args()

    out=Path(args.outdir); out.mkdir(parents=True, exist_ok=True)
    raw=out/"double-irq-probe.raw.log"
    result=out/"double-irq-probe.result"

    exe=shutil.which(args.vice)
    if not exe:
        result.write_text("status=UNQUALIFIED\nreason=VICE_NOT_FOUND\n")
        return 2

    ver=subprocess.run([exe,"-version"],text=True,capture_output=True)
    version=(ver.stdout+ver.stderr).strip().replace("\n"," ")
    (out/"vice.version.txt").write_text(version+"\n")

    # A backend is intentionally required rather than guessing monitor syntax.
    backend=os.environ.get("C64SCENE_VICE_TIMING_BACKEND")
    if not backend:
        raw.write_text("")
        result.write_text(
            "status=UNQUALIFIED\n"
            "reason=NO_VERIFIED_TIMING_BACKEND\n"
            f"vice={version}\n"
        )
        return 3

    p=subprocess.run([backend,exe,args.prg],text=True,capture_output=True)
    raw.write_text(p.stdout+p.stderr)
    if p.returncode:
        result.write_text(
            "status=UNQUALIFIED\n"
            "reason=TIMING_BACKEND_FAILED\n"
            f"backend_exit={p.returncode}\n"
            f"vice={version}\n"
        )
        return p.returncode

    result.write_text("status=RUN\nraw="+str(raw)+"\nvice="+version+"\n")
    return 0

if __name__=="__main__":
    sys.exit(main())
