ASM ?= 64tass
ASSEMBLER ?= 64tass
VICE ?= x64sc
BUILD = python3 tools/build.py --assembler $(ASSEMBLER)
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

.PHONY: all run run-stable run-double-irq qualify-double-irq qualify-headless probe-double-irq probe-double-irq-vice39 analyze-vice-log binary-monitor-selftest timing-adapter-selftest timing-analyzer-selftest sanity clean

all: $(HELLO_PRG) $(STABLE_PRG) $(DOUBLE_PRG)

$(HELLO_PRG): $(HELLO_SRC)
	mkdir -p $(BUILD_DIR)
	$(BUILD) $(HELLO_SRC) -o $(HELLO_PRG) --labels $(HELLO_LABELS)

$(STABLE_PRG): $(STABLE_SRC)
	mkdir -p $(BUILD_DIR)
	$(BUILD) $(STABLE_SRC) -o $(STABLE_PRG) --labels $(STABLE_LABELS)

$(DOUBLE_PRG): $(DOUBLE_SRC)
	mkdir -p $(BUILD_DIR)
	$(BUILD) $(DOUBLE_SRC) -o $(DOUBLE_PRG) --labels $(DOUBLE_LABELS)

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

probe-double-irq-vice39: $(DOUBLE_PRG)
	C64SCENE_VICE_TIMING_BACKEND=tools/vice/backends/vice39_text.py python3 tools/vice/probe_double_irq.py --vice "$(VICE)" --prg $(DOUBLE_PRG)

analyze-vice-log:
	test -n "$(LOG)"
	python3 tools/vice/run_qualification.py "$(LOG)" --frames 120

binary-monitor-selftest:
	cd tools/vice && python3 test_binary_protocol.py

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
