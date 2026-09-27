ASM ?= 64tass
VICE ?= x64sc
BUILD_DIR := build

HELLO_SRC := examples/hello-raster/main.asm
HELLO_PRG := $(BUILD_DIR)/hello-raster.prg
HELLO_LABELS := $(BUILD_DIR)/hello-raster.labels

STABLE_SRC := examples/stable-raster/main.asm
STABLE_PRG := $(BUILD_DIR)/stable-raster.prg
STABLE_LABELS := $(BUILD_DIR)/stable-raster.labels

.PHONY: all run run-stable clean

all: $(HELLO_PRG) $(STABLE_PRG)

$(HELLO_PRG): $(HELLO_SRC)
	mkdir -p $(BUILD_DIR)
	$(ASM) --cbm-prg -Wall -a -B -L $(HELLO_LABELS) -o $(HELLO_PRG) $(HELLO_SRC)

$(STABLE_PRG): $(STABLE_SRC)
	mkdir -p $(BUILD_DIR)
	$(ASM) --cbm-prg -Wall -a -B -L $(STABLE_LABELS) -o $(STABLE_PRG) $(STABLE_SRC)

run: $(HELLO_PRG)
	$(VICE) -autostart $(HELLO_PRG)

run-stable: $(STABLE_PRG)
	$(VICE) -autostart $(STABLE_PRG)

clean:
	rm -rf $(BUILD_DIR)
