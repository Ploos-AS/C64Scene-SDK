; C64Scene SDK - reference timing constants
; Values are intentionally visible to scene code.
PAL_LINES               = 312
PAL_CYCLES_PER_LINE     = 63
NTSC_OLD_LINES          = 262
NTSC_OLD_CYCLES_PER_LINE = 64
NTSC_NEW_LINES          = 263
NTSC_NEW_CYCLES_PER_LINE = 65

; VIC-II character fetch badline cadence is every 8 raster lines when the
; display conditions match. Exact applicability remains the coder's concern.
BADLINE_PERIOD          = 8
