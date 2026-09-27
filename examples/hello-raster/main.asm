; C64Scene SDK M0 reference example
; 64tass syntax
;
; Minimal direct-hardware raster color effect.
; No SDK runtime is required.

* = $0801

; BASIC stub: 10 SYS 2061
.byte $0c,$08,$0a,$00,$9e,$20,$32,$30,$36,$31,$00,$00,$00

start:
    sei

    lda #$00
    sta $d020       ; border
    sta $d021       ; background

main:
    lda $d012       ; current raster line
wait:
    cmp $d012
    beq wait

    lda $d012
    lsr
    lsr
    and #$0f
    sta $d020       ; direct VIC-II register write

    jmp main
