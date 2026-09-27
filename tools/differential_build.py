#!/usr/bin/env python3
"""Build one C64Scene source with 64tass and SceneASM and compare PRGs."""
import argparse, os, pathlib, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]

def run(assembler, source, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    prg=outdir/(source.stem+".prg")
    labels=outdir/(source.stem+".labels")
    cmd=[sys.executable,str(ROOT/"tools/build.py"),"--assembler",assembler,
         str(source),"-o",str(prg),"--labels",str(labels)]
    p=subprocess.run(cmd,cwd=ROOT)
    return p.returncode,prg,labels

def first_difference(a,b):
    for i,(x,y) in enumerate(zip(a,b)):
        if x!=y: return i,x,y
    if len(a)!=len(b): return min(len(a),len(b)),None,None
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--build-dir",default="build/differential")
    a=ap.parse_args()
    source=(ROOT/a.source).resolve()
    base=ROOT/a.build_dir

    r64,p64,_=run("64tass",source,base/"64tass")
    rsa,psa,_=run("sceneasm",source,base/"sceneasm")
    if r64 or rsa:
        print(f"status=UNQUALIFIED 64tass_rc={r64} sceneasm_rc={rsa}")
        return 2

    left,right=p64.read_bytes(),psa.read_bytes()
    diff=first_difference(left,right)
    if diff is None:
        print(f"status=MATCH bytes={len(left)}")
        return 0
    off,x,y=diff
    print(f"status=MISMATCH offset={off} 64tass={x!r} sceneasm={y!r} 64tass_size={len(left)} sceneasm_size={len(right)}")
    return 1

if __name__=="__main__":
    raise SystemExit(main())
