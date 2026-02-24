BUILD_DIR = build
DIST_DIR  = pdf
LATEX     = xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD_DIR)

ENTRY_TEX = resume.tex
OUTPUT_PDF = $(DIST_DIR)/resume.pdf

MD_SOURCE = content/resume_dev.md
TEX_CONTENT = content/resume.tex

# Security specific paths
SEC_MD_SOURCE = content/resume_security_dev.md
SEC_TEX_CONTENT = content/resume_security.tex
SEC_ENTRY_TEX = resume_security.tex
SEC_OUTPUT_PDF = $(DIST_DIR)/resume_security.pdf
GEN_SCRIPT = gen_resume_tex.py

# Template/style dependencies: changing these should trigger a rebuild.
RESUME_CLASS = resume.cls
STYLE_FILES  = zh_CN-systemfonts.sty linespacing_fix.sty fontawesome.sty

ifeq ($(OS),Windows_NT)
  RM = cmd //C del
else
  RM = rm -f
endif


.PHONY: all pdfs security clean

all: pdfs

pdfs: $(OUTPUT_PDF)

security: $(SEC_OUTPUT_PDF)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(DIST_DIR):
	mkdir -p $(DIST_DIR)

# Generate TeX content from Markdown single source.
$(TEX_CONTENT): $(MD_SOURCE) $(GEN_SCRIPT)
	python3 $(GEN_SCRIPT) $(MD_SOURCE) $(TEX_CONTENT)

# Generate Security TeX content from Markdown single source.
$(SEC_TEX_CONTENT): $(SEC_MD_SOURCE) $(GEN_SCRIPT)
	python3 $(GEN_SCRIPT) $(SEC_MD_SOURCE) $(SEC_TEX_CONTENT)

# Build single resume from ENTRY_TEX, copy build output to dist.
$(OUTPUT_PDF): $(ENTRY_TEX) $(TEX_CONTENT) $(RESUME_CLASS) $(STYLE_FILES) | $(BUILD_DIR) $(DIST_DIR)
	$(LATEX) $(ENTRY_TEX)
	cp $(BUILD_DIR)/resume.pdf $(OUTPUT_PDF)

# Build security resume from SEC_ENTRY_TEX, copy build output to dist.
$(SEC_OUTPUT_PDF): $(SEC_ENTRY_TEX) $(SEC_TEX_CONTENT) $(RESUME_CLASS) $(STYLE_FILES) | $(BUILD_DIR) $(DIST_DIR)
	$(LATEX) $(SEC_ENTRY_TEX)
	cp $(BUILD_DIR)/resume_security.pdf $(SEC_OUTPUT_PDF)

clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR)
