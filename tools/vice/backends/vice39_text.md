# VICE 3.9 textual-monitor backend

Initial target: VICE/x64sc 3.9, PAL.

The VICE manual documents that breakpoint hits print the current raster line and raster cycle. The backend uses that checkpoint-hit record as its timing source and converts it to C64Scene's canonical marker format.

It also uses the documented `-moncommands` startup facility.

## Qualification status

Backend implementation: PRESENT

Real 120-frame evidence: NOT YET RECORDED

Therefore this backend does not by itself make the double-IRQ routine qualified.

## Constraints

- `stable_start` is resolved from the 64tass label output.
- PAL is forced for the initial qualification path.
- Unknown/non-matching monitor output is rejected.
- Raw VICE output is retained by the outer probe.
- A future binary-monitor backend may provide a more robust machine interface.
