ASM ?= 64tass
VICE ?= x64sc
BUILD_DIR := build

HELLO_SRC := examples/hello-raster/main.asm
HELLO_PRG := $(BUILD_DIR)/hello-raster.prg
HELLO_LABELS := $(BUILD_DIR)/hello-raster.labels

STABLE_SRC := examples/stable-raster/main.asm
STABLE_PRG := $(BUILD_DIR)/stable-raster.prg
STABLE_LABELS := $(BUILD_DIR)/stable-raster.labels

DOUBLE_SRC := examples/double-irq/main.asm
DOUBLE_PRG := $(BUILD_DIR)/double-irq.prg
DOUBLE_LABELS := $(BUILD_DIR)/double-irq.labels

.PHONY: all run run-stable run-double-irq qualify-double-irq qualify-headless probe-double-irq timing-adapter-selftest timing-analyzer-selftest sanity clean

all: $(HELLO_PRG) $(STABLE_PRG) $(DOUBLE_PRG)

$(HELLO_PRG): $(HELLO_SRC)
	mkdir -p $(BUILD_DIR)
	$(ASM) --cbm-prg -Wall -a -B -L $(HELLO_LABELS) -o $(HELLO_PRG) $(HELLO_SRC)

$(STABLE_PRG): $(STABLE_SRC)
	mkdir -p $(BUILD_DIR)
	$(ASM) --cbm-prg -Wall -a -B -L $(STABLE_LABELS) -o $(STABLE_PRG) $(STABLE_SRC)

$(DOUBLE_PRG): $(DOUBLE_SRC)
	mkdir -p $(BUILD_DIR)
	$(ASM) --cbm-prg -Wall -a -B -L $(DOUBLE_LABELS) -o $(DOUBLE_PRG) $(DOUBLE_SRC)

run: $(HELLO_PRG)
	$(VICE) -autostart $(HELLO_PRG)

run-stable: $(STABLE_PRG)
	$(VICE) -autostart $(STABLE_PRG)

run-double-irq: $(DOUBLE_PRG)
	$(VICE) -autostart $(DOUBLE_PRG)

qualify-double-irq: $(DOUBLE_PRG)
	$(VICE) -moncommands tools/vice/double-irq.mon -autostart $(DOUBLE_PRG)

qualify-headless: $(DOUBLE_PRG)
	sh tools/vice/qualify-double-irq.sh $(DOUBLE_PRG)

probe-double-irq: $(DOUBLE_PRG)
	python3 tools/vice/probe_double_irq.py --vice "$(VICE)" --prg $(DOUBLE_PRG)

timing-adapter-selftest:
	python3 tools/vice/extract_samples.py tools/vice/adapter.example.log --min-samples 4 --output build/qualification/adapter-selftest.csv
	test "$(wc -l < build/qualification/adapter-selftest.csv)" -eq 5

timing-analyzer-selftest:
	python3 tools/vice/analyze_timing.py tools/vice/samples.example.csv --min-frames 4 --result build/qualification/analyzer-selftest.result
	grep -q '^status=QUALIFIED_PASS$' build/qualification/analyzer-selftest.result

sanity: all
	test -s $(HELLO_PRG)
	test -s $(STABLE_PRG)
	test -s $(DOUBLE_PRG)
	grep -q "stable_start" $(DOUBLE_LABELS)

clean:
	rm -rf $(BUILD_DIR)
