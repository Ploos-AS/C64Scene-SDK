; C64Scene SDK M1.2 - double IRQ raster stabilization reference
; PAL / 64tass. Technique reference, not an opaque SDK service.
;
; First IRQ schedules a second IRQ on the following raster line and burns
; cycles until it is taken. The second IRQ aligns execution to a known
; position using the classic raster compare correction.
;
; Qualification target: common PAL VIC-II, away from badlines.

* = $0801
.byte $0b,$08,$0a,$00,$9e
.text "2061"
.byte $00,$00,$00

* = $080d

VIC_CTRL1       = $d011
VIC_RASTER      = $d012
VIC_IRQ_FLAGS   = $d019
VIC_IRQ_ENABLE  = $d01a
VIC_BORDER      = $d020
CIA1_ICR        = $dc0d
CIA2_ICR        = $dd0d
IRQ_VECTOR      = $0314

TARGET_LINE     = 96

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

    lda #<irq1
    sta IRQ_VECTOR
    lda #>irq1
    sta IRQ_VECTOR+1

    lda #TARGET_LINE
    sta VIC_RASTER
    lda #$01
    sta VIC_IRQ_FLAGS
    sta VIC_IRQ_ENABLE
    cli

main:
    jmp main

; Phase 1: arrange the next-line IRQ.
irq1:
    pha
    txa
    pha
    tya
    pha

    lda #<irq2
    sta IRQ_VECTOR
    lda #>irq2
    sta IRQ_VECTOR+1
    inc VIC_RASTER
    lda #$01
    sta VIC_IRQ_FLAGS

    tsx
    cli

    ; Burn enough time that IRQ2 interrupts this phase.
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop

    ; IRQ2 should have happened before this path is reached.
irq1_wait:
    jmp irq1_wait

; Phase 2: stack pointer is restored to the phase-1 frame. The raster
; comparison compensates the remaining one-cycle entry ambiguity.
irq2:
    txs

    ldx #$08
irq2_delay:
    dex
    bne irq2_delay
    bit $00

    lda VIC_RASTER
    cmp VIC_RASTER
    beq *+2

    ; Stable work starts here. Border pulse is the qualification marker.
stable_start:
    inc VIC_BORDER
    nop
    nop
    nop
    nop
    dec VIC_BORDER

    lda #TARGET_LINE
    sta VIC_RASTER
    lda #<irq1
    sta IRQ_VECTOR
    lda #>irq1
    sta IRQ_VECTOR+1
    lda #$01
    sta VIC_IRQ_FLAGS

    pla
    tay
    pla
    tax
    pla
    rti
