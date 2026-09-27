# SceneASM integration

C64Scene and SceneASM are complementary projects.

> C64Scene owns scene knowledge. SceneASM owns assembly knowledge.

C64Scene remains usable with an independent reference assembler. SceneASM integration must earn preferred status through compatibility and qualification rather than becoming a mandatory dependency.

## Responsibilities

### C64Scene owns

- C64/VIC-II/SID/CIA definitions and scene-oriented helpers;
- raster, badline and video-standard knowledge;
- asset conversion and demo packaging;
- emulator/runtime qualification;
- C64-specific examples and reference techniques;
- machine-specific profiling semantics.

### SceneASM owns

- 6502/6510 assembly language and instruction encoding;
- expressions, symbols, diagnostics and source locations;
- sections/linking where applicable;
- static instruction-cycle analysis;
- debug/symbol output;
- editor/LSP integration.

## M2 integration stages

1. **M2.0 adapter** — selectable assembler backend; 64tass remains default.
2. **M2.1 syntax subset** — C64Scene examples use a documented common subset where practical.
3. **M2.2 differential build** — compare generated PRG payloads and symbols.
4. **M2.3 timing metadata** — SceneASM exports predicted instruction/raster timing in a machine-readable form.
5. **M2.4 qualification join** — compare SceneASM predictions with VICE measurements.
6. **M2.5 editor integration** — C64Scene hardware metadata feeds SceneASM diagnostics/LSP.
7. **M2.6 preferred evaluation** — only after qualification may SceneASM be considered for preferred-toolchain status.

## Differential qualification

For deterministic examples C64Scene should be able to build with both:

    c64scene/build-64tass
    c64scene/build-sceneasm

The comparison should distinguish:

- exact binary match;
- semantically equivalent binary with layout differences;
- symbol-map differences;
- assembler diagnostics;
- predicted timing differences.

An exact match is useful evidence, but not required where SceneASM deliberately provides different linking/layout features.

## Machine-readable boundary

The projects should exchange data through versioned formats rather than importing each other's internals. Initial candidates:

- symbol map;
- source map;
- section/layout map;
- instruction timing map;
- C64 hardware metadata;
- qualification result.

This keeps SceneASM reusable for future AmiScene/K16 integrations without making C64Scene generic or weakening its C64 focus.
