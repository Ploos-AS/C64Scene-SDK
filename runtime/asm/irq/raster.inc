; C64Scene SDK - minimal raster IRQ helpers
; These macros expose the writes. They do not install hidden state.

raster_ack .macro
    asl VIC_IRQ_FLAGS
.endm

raster_set_line .macro line
    lda #line
    sta VIC_RASTER
.endm
