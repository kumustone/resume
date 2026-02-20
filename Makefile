BUILD_DIR = build
DIST_DIR  = pdf
LATEX     = xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD_DIR)

VARIANT_SRCS = $(wildcard variants/*.tex)
VARIANT_PDFS = $(patsubst variants/%.tex,$(DIST_DIR)/%.pdf,$(VARIANT_SRCS))

ifeq ($(OS),Windows_NT)
  RM = cmd //C del
else
  RM = rm -f
endif

.PHONY: all pdf clean

all: pdf

pdf: $(BUILD_DIR) $(DIST_DIR) $(VARIANT_PDFS)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(DIST_DIR):
	mkdir -p $(DIST_DIR)

# Run xelatex from project root so all relative paths (fonts/, *.cls, *.sty) resolve correctly.
# TEXINPUTS includes variants/ so \input{content/...} and \documentclass{resume} both work.
# After compilation, copy the PDF from build/ to dist/.
$(DIST_DIR)/%.pdf: variants/%.tex | $(BUILD_DIR)
	TEXINPUTS=variants:$$TEXINPUTS $(LATEX) $<
	mkdir -p $(DIST_DIR)
	cp $(BUILD_DIR)/$*.pdf $(DIST_DIR)/

clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR)
