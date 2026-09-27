; C64Scene SDK M1.1 reference: raster IRQ baseline
; 64tass syntax. PAL qualification target.
;
; This is intentionally a baseline, not a claim that every entry path is
; cycle-stable. The next qualification step measures entry jitter in VICE
; and evolves this into documented stable variants.

* = $0801
.byte $0b,$08,$0a,$00,$9e
.text "2061"
.byte $00,$00,$00

* = $080d

VIC_CTRL1      = $d011
VIC_RASTER     = $d012
VIC_IRQ_FLAGS  = $d019
VIC_IRQ_ENABLE = $d01a
VIC_BORDER     = $d020
CIA1_ICR       = $dc0d
CIA2_ICR       = $dd0d
IRQ_VECTOR     = $0314

start:
    sei
    lda #$7f
    sta CIA1_ICR
    sta CIA2_ICR
    lda CIA1_ICR
    lda CIA2_ICR

    lda VIC_CTRL1
    and #$7f
    sta VIC_CTRL1

    lda #100
    sta VIC_RASTER

    lda #<raster_irq
    sta IRQ_VECTOR
    lda #>raster_irq
    sta IRQ_VECTOR+1

    lda #$01
    sta VIC_IRQ_FLAGS
    sta VIC_IRQ_ENABLE
    cli

main:
    jmp main

raster_irq:
    pha
    txa
    pha
    tya
    pha

    lda #$01
    sta VIC_IRQ_FLAGS

    inc VIC_BORDER
    ; Effect work goes here. Keep cycle cost explicit.
    dec VIC_BORDER

    pla
    tay
    pla
    tax
    pla
    rti
