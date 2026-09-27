# M1.2 double-IRQ stabilization

This is the first C64Scene reference routine intended to demonstrate a classic scene-oriented raster stabilization technique.

## Purpose

The first raster IRQ schedules another IRQ on the next line. The second entry uses the known relationship between the two interrupts to reduce IRQ-entry jitter and establish a predictable point for cycle-sensitive work.

## Rules

- PAL is the first qualification target.
- The chosen reference raster region must avoid a badline while qualifying the routine.
- The routine is deliberately visible and editable.
- C64Scene does not promise that this exact prologue is optimal for every production.
- Effect code should treat `stable_start` as the point to measure.
- VIC-II revision and emulator settings belong in qualification results.

## VICE inspection

Build with:

    make

Run with:

    make run-double-irq

Use the VICE monitor/debug facilities and the generated labels to inspect `stable_start`, raster position and border transitions.

The next step is automated/recorded qualification rather than adding more abstraction.
