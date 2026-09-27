; C64Scene SDK - CPU port and common memory map
CPU_DDR         = $0000
CPU_PORT        = $0001
IRQ_VECTOR      = $0314
NMI_VECTOR      = $0318
SCREEN_DEFAULT  = $0400
BASIC_START     = $0801
KERNAL_IRQ      = $ea31

; Common $01 values. These are deliberately constants, not hidden policy.
MEM_ALL_RAM     = %00110100
MEM_IO_RAM      = %00110101
MEM_BASIC_IO_KERNAL = %00110111
