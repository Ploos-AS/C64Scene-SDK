ASM ?= 64tass
VICE ?= x64sc
BUILD_DIR := build
EXAMPLE := examples/hello-raster/main.asm
PRG := $(BUILD_DIR)/hello-raster.prg
LABELS := $(BUILD_DIR)/hello-raster.labels

.PHONY: all run clean

all: $(PRG)

$(PRG): $(EXAMPLE)
	mkdir -p $(BUILD_DIR)
	$(ASM) --cbm-prg -Wall -a -B -L $(LABELS) -o $(PRG) $(EXAMPLE)

run: $(PRG)
	$(VICE) -autostart $(PRG)

clean:
	rm -rf $(BUILD_DIR)
