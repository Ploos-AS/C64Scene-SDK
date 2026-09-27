#!/bin/sh
set -eu

VICE="${VICE:-x64sc}"
PRG="${1:-build/double-irq.prg}"
OUTDIR="${QUALIFY_OUT:-build/qualification}"
LOG="$OUTDIR/double-irq-vice.log"
RESULT="$OUTDIR/double-irq.result"

mkdir -p "$OUTDIR"
rm -f "$LOG" "$RESULT"

if ! command -v "$VICE" >/dev/null 2>&1; then
    printf '%s\n' "status=UNQUALIFIED" "reason=VICE_NOT_FOUND" > "$RESULT"
    echo "VICE executable not found: $VICE" >&2
    exit 2
fi

# VICE CLI options differ somewhat between releases. Keep invocation small
# and capture everything needed to diagnose runner compatibility.
set +e
"$VICE" -console -moncommands tools/vice/headless-double-irq.mon -autostart "$PRG" >"$LOG" 2>&1
rc=$?
set -e

{
    echo "vice_exit=$rc"
    echo "log=$LOG"
} >> "$RESULT"

if [ "$rc" -ne 0 ]; then
    echo "status=UNQUALIFIED" >> "$RESULT"
    echo "reason=VICE_RUN_FAILED" >> "$RESULT"
    exit "$rc"
fi

# Reaching here proves only that the scripted emulator path ran successfully.
# It does NOT prove cycle stability.
echo "status=RUN" >> "$RESULT"
echo "timing=NOT_MEASURED" >> "$RESULT"
