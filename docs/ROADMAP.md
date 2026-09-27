# C64Scene SDK Roadmap

## M0 — Architecture & Skeleton

Goal: establish the assembly-first contract and a reproducible minimal build/run path.

- project principles and scope
- 64tass reference assembler
- VICE x64sc reference emulator
- minimal raster example
- Makefile build/run interface
- initial runtime/asm and tools layout
- MIT software license

Exit criterion: a clean checkout with 64tass can build the reference PRG, and VICE can launch it with `make run`.

## M1 — Core ASM foundation

- register/include conventions
- memory-map helpers
- IRQ helpers
- VIC-II helpers
- CIA helpers
- SID playback integration interface
- zero-page allocation conventions
- PAL timing tables
- initial NTSC timing tables
- documented clobbers/cycle costs

## M2 — Asset pipeline

- image conversion
- charset conversion/deduplication
- sprite conversion
- screen/color RAM generation
- binary/include/label outputs
- deterministic builds and caching

## M3 — Raster & profiling

- raster/cycle profiler
- badline visualization/reporting
- IRQ timing analysis
- memory maps
- symbol/label ingestion
- VICE monitor automation

## M4 — Music, sync & timeline

- SID metadata/import workflow
- replay-routine integration points
- frame/pattern/event sync
- scene timeline/director format
- generated assembly tables rather than mandatory runtime control

## M5 — Packing & media

- cruncher integration
- PRG packaging
- D64 generation
- optional D81 workflows
- loader integration points
- release artifact generation

## M6 — Reference techniques

Hackable reference implementations and documentation for selected scene techniques, potentially including stable raster, sprite multiplexing, FLD, FLI-family techniques, DYCP/scrollers, sprite stretching, and other hardware-driven effects.

Reference effects are examples and reusable routines, never opaque mandatory framework calls.

## M7 — Qualification & compatibility

- automated VICE qualification
- PAL/NTSC matrices
- ACME integration
- KickAssembler integration where licensing/workflow permits
- artifact and regression reports
- reproducible release builds

## Long-term rule

Every milestone must preserve the ability for an experienced scene coder to bypass SDK helpers and address the machine directly.
