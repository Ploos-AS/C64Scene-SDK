; C64Scene SDK - IRQ primitives
; Deliberately tiny. Production code owns vectors, register policy and timing.

irq_disable_cia .macro
    lda #$7f
    sta CIA1_ICR
    sta CIA2_ICR
    lda CIA1_ICR
    lda CIA2_ICR
.endm

irq_enable_raster .macro
    lda #$01
    sta VIC_IRQ_ENABLE
.endm

irq_ack_raster .macro
    lda #$01
    sta VIC_IRQ_FLAGS
.endm
