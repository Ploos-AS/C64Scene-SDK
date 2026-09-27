# VICE qualification support

This directory contains monitor/debugger inputs used to inspect C64Scene reference routines.

M1.3 intentionally separates **build success** from **timing qualification**. An assembled PRG is not evidence that a raster routine is cycle-stable.

## Double IRQ

Build:

    make build/double-irq.prg

Interactive qualification:

    make qualify-double-irq

The generated 64tass label file is kept in `build/double-irq.labels`. Monitor command compatibility varies between VICE releases, so the initial monitor script uses explicit addresses for the bootstrap and VIC-II border register.

## Qualification output

Recorded qualification results belong under `qualification/` and must state emulator/version, video standard/model, raster target, badline relationship, observed stable entry and jitter. Do not mark a result PASS without an actual run.
