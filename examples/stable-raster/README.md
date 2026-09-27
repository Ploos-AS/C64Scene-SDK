# stable-raster baseline

This M1.1 example establishes a controlled raster IRQ baseline for PAL qualification.

It deliberately does **not** hide IRQ setup or claim cycle stability that has not been measured. The border pulse makes IRQ execution easy to inspect in VICE. The next step is to qualify entry jitter and add explicitly named stabilization variants.

Build with 64tass and inspect raster line 100 in the VICE monitor/debugger.
