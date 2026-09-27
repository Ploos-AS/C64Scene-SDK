# C64Scene SDK Design Contract

## Purpose

C64Scene SDK is a scene-oriented Commodore 64 SDK for coders who want direct control over the machine. The SDK exists to accelerate low-level work without hiding the hardware.

## Target philosophy

1. 6510 assembly is the primary target language.
2. Hardware control wins over abstraction.
3. Exact timing and exact bytes are observable and controllable.
4. The SDK must be usable piecemeal; no mandatory framework runtime.
5. Generated data must be friendly to assembly projects: raw binaries, includes, labels, offsets, alignment information, and maps.
6. PAL is the first qualification target; NTSC behavior must be explicit.
7. Host tools may be implemented in modern languages when that improves reproducibility or usability.

## Hardware domains

The SDK should expose rather than hide:

- MOS 6510 CPU behavior
- VIC-II registers, raster timing, badlines and memory layout
- SID registers and playback integration
- CIA timers, IRQ/NMI sources and input
- zero page allocation
- memory banking and ROM/I/O visibility
- self-modifying code and code/data placement

## Toolchain baseline

M0 uses 64tass as the reference assembler because it gives us a straightforward open cross-assembly baseline and suitable output for automation. The architecture must not prevent ACME or KickAssembler integration later.

VICE `x64sc` is the initial reference emulator. Emulator integration should evolve toward labels, monitor scripts, breakpoints, memory dumps, raster/cycle diagnostics and automated qualification.

## Runtime policy

`runtime/asm` is a routine library, not a required runtime. A production may import one routine, many routines, or none.

Routines should document where practical:

- clobbered registers
- zero-page requirements
- memory requirements
- expected entry/exit state
- PAL/NTSC assumptions
- cycle cost or timing constraints
- self-modifying locations

## Scene credibility

Design decisions should be judged against real scene workflows. Convenience features are welcome when they do not impose hidden cost, constrain hardware tricks, or turn low-level effects into opaque framework calls.

## Non-goals for M0

M0 does not promise a full effect library, complete graphics conversion suite, integrated music editor, universal assembler syntax, or transparent PAL/NTSC portability. Those require later milestones and qualification.
