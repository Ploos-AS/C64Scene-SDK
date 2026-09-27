# ASM routine library

This directory will contain optional, composable 6510 assembly routines for C64Scene SDK.

It is deliberately **not** a mandatory runtime. Scene code may include selected routines or bypass this directory entirely.

Planned domains include VIC-II, IRQ/raster, CIA, SID, memory/banking, loaders, math, synchronization, sprites, charset/bitmap and scrolling.

Each routine should document clobbered registers, zero-page use, memory requirements, entry/exit assumptions, PAL/NTSC assumptions and timing/cycle constraints where relevant.
