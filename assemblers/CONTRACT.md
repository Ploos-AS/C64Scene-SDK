# Assembler adapter contract — v0

C64Scene invokes an adapter with:

    build.py <source> -o <program.prg> --labels <symbols>

The adapter owns assembler-specific CLI syntax.

Environment selection:

- `C64SCENE_ASSEMBLER=64tass|sceneasm`
- `ASM` may override the 64tass executable.
- `SCENEASM` may override the SceneASM executable.

## Required behavior

An enabled adapter must:

1. return non-zero on assembler failure;
2. produce the requested PRG;
3. produce symbol/debug metadata at the requested path or document a lossless conversion;
4. print useful diagnostics without rewriting source semantics;
5. add no target-side runtime code implicitly.

SceneASM remains disabled at the actual invocation boundary until its CLI contract is confirmed and qualified.
