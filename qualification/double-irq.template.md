# Double IRQ qualification

Status: NOT RUN

- C64Scene commit:
- Routine: `examples/double-irq/main.asm`
- Assembler:
- VICE:
- VIC-II model:
- Video standard:
- Target line: 96
- IRQ1 badline:
- IRQ2 badline:
- `stable_start` line/cycle:
- Observed jitter:
- Frames observed:
- Result: NOT RUN

## Criterion

PASS requires `stable_start` to reach the documented cycle position without observed cycle-to-cycle jitter across the qualification sample. Any model-specific assumptions must be recorded.

## Notes

Do not replace NOT RUN with PASS based only on successful assembly.
