# Timing and raster policy

C64Scene treats timing as production data, not an implementation detail.

## PAL baseline

The initial reference target is the common PAL VIC-II model with 312 raster lines and 63 CPU cycles per line. Code that depends on a particular VIC-II revision must say so explicitly.

## Badlines

A badline can remove a large part of the CPU budget from a raster line. C64Scene will therefore document effects in terms of raster line, cycle budget, badline interaction and VIC-II model rather than presenting a generic "frame time" abstraction.

## Stable raster IRQs

There is no single opaque `stable_irq()` API. We will keep multiple techniques as named reference implementations, with their assumptions and cycle costs documented. Likely variants include simple measured IRQ entry, double-IRQ stabilization and technique-specific synchronization where useful.

## Qualification

VICE is the initial reference emulator. M1.x qualification should capture labels/symbols and automate checks where practical, while still making manual monitor inspection straightforward for scene coders.
