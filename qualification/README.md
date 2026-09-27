# Qualification results

C64Scene distinguishes three states:

- **BUILD** — source assembles successfully.
- **RUN** — artifact starts and reaches the intended emulator/runtime path.
- **QUALIFIED** — the stated timing/behaviour has been measured under a documented configuration.

A timing-sensitive routine must not be promoted from BUILD/RUN to QUALIFIED from source inspection alone.

## Required metadata

Each timing qualification record should contain:

- C64Scene commit;
- example/routine;
- assembler and version;
- emulator and version;
- VIC-II family/model;
- PAL/NTSC standard;
- target raster line;
- badline relationship;
- measured stable-start raster/cycle;
- observed jitter/range;
- PASS/FAIL with a precise criterion.

Real hardware qualification may be added separately and must identify the machine/chip revision where known.
