#!/usr/bin/env python3
"""VICE 3.9 textual-monitor timing backend for C64Scene.

Parses documented checkpoint-hit output:
  #N (Stop on exec ADDR) LINE/$HEXLINE, CYCLE/$HEXCYCLE

stdout: canonical C64SCENE_TIMING markers only.
stderr: diagnostics/raw VICE output.
"""
import re, subprocess, sys, tempfile
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: vice39_text.py <x64sc> <prg>", file=sys.stderr)
    raise SystemExit(2)

vice, prg = sys.argv[1:]
# stable_start address is resolved from the 64tass label file.
labels=Path("build/double-irq.labels")
if not labels.exists():
    print("missing build/double-irq.labels", file=sys.stderr); raise SystemExit(2)

addr=None
# 64tass label listings contain the symbol and its hex address; accept either order.
hexrx=re.compile(r"(?:\$|0x)?([0-9a-fA-F]{4})")
for line in labels.read_text(errors="replace").splitlines():
    if "stable_start" in line:
        m=hexrx.search(line)
        if m:
            addr=m.group(1); break
if not addr:
    print("could not resolve stable_start from labels", file=sys.stderr); raise SystemExit(2)

with tempfile.NamedTemporaryFile("w", suffix=".mon", delete=False) as f:
    mon=Path(f.name)
    # Stop repeatedly at stable_start. Monitor hit text carries raster line/cycle.
    f.write(f"break ${addr}\n")
    f.write("x\n")

cmd=[vice,"-console","-pal","-moncommands",str(mon),"-autostart",prg]
try:
    p=subprocess.run(cmd,text=True,capture_output=True,timeout=20)
finally:
    mon.unlink(missing_ok=True)

raw=p.stdout+p.stderr
print(raw, file=sys.stderr, end="")

# Documented form example:
# #1 (Stop on exec ea31)   41/$029,  35/$23
rx=re.compile(r"^#\d+\s+\(Stop on\s+exec\s+[0-9a-fA-F]+\)\s+(\d+)/\$[0-9a-fA-F]+,\s+(\d+)/\$[0-9a-fA-F]+", re.M)
hits=rx.findall(raw)
for frame,(line,cycle) in enumerate(hits,1):
    print(f"C64SCENE_TIMING frame={frame} line={line} cycle={cycle}")

if p.returncode:
    raise SystemExit(p.returncode)
if not hits:
    print("no documented checkpoint-hit timing lines found", file=sys.stderr)
    raise SystemExit(3)
