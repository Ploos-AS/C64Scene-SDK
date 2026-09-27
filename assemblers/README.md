# Assembler adapters

Assembler-specific integration belongs here.

The adapter boundary exists so C64Scene can qualify SceneASM without coupling the SDK to SceneASM internals.

Initial backends:

- `64tass` — reference assembler / current baseline.
- `sceneasm` — M2 integration target.

Adapters may define command-line invocation, output paths, symbol conversion and diagnostic normalization. They must not introduce hidden target-side runtime code.
