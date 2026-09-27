# C64Scene SDK

**Assembly-first tools and routines for Commodore 64 scene productions.**

C64Scene SDK is built for demoscene-style development where scene credibility, direct hardware control, size, timing, and maximum use of the Commodore 64 matter more than abstraction.

## M0 principles

- **6510 assembly first.** Target-side code, examples, and reference routines are assembly-first.
- **Hardware first.** VIC-II, SID, CIA, memory banking, zero page, raster timing, and self-modifying code remain directly accessible.
- **No mandatory runtime.** Projects may use as much or as little of the SDK as they want.
- **Zero-cost helpers where practical.** Macros and routines must not hide unnecessary overhead.
- **Cycle-aware tooling.** The SDK should help measure and reason about cycles, badlines, raster positions, IRQ timing, and memory use.
- **Size coding matters.** 4K/16K/64K intros are first-class use cases.
- **PAL first, NTSC explicit.** PAL is the initial reference target; NTSC differences must be visible rather than silently abstracted.
- **Cross-development is encouraged.** Host-side tools may use modern languages; generated/target code stays scene-oriented and assembly-first.
- **Scene practice drives tool choices.** Assemblers, crunchers, music tools, and workflows are selected for C64 scene usefulness, not framework convenience.

## M0 scope

M0 establishes the project architecture and development contract. It does **not** attempt to ship a complete effect library or asset pipeline.

Initial structure:

```text
C64Scene-SDK/
├── docs/
│   ├── DESIGN.md
│   └── ROADMAP.md
├── examples/
│   └── hello-raster/
├── runtime/
│   └── asm/
├── tools/
├── Makefile
├── LICENSE
└── README.md
```

## Reference workflow

The first supported developer flow is intentionally simple:

```sh
make
make run
```

`make` assembles the reference example. `make run` starts it in VICE when `x64sc` is installed.

The M0 reference assembler is **64tass**. This is a reproducible baseline, not a declaration that other scene assemblers are second-class forever. ACME and KickAssembler compatibility/integration belong on the roadmap where useful.

## Direction

Future C64Scene tooling is expected to cover image/charset/sprite conversion, SID integration, raster profiling, disk images, crunching, timeline/sync support, labels/symbol integration, and automated emulator-based qualification.

> C64Scene SDK must not make the C64 less C64-like. It should make it easier to push the machine harder.
