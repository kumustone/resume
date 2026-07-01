# ============================================================
# 简历构建入口 Makefile
# ============================================================

# ---- 目录定义 ----
BUILD_DIR    = build
DIST_DIR     = output
CONTENT_DIR  = content
HTML_DIR     = html
DATA_DIR     = data
SCRIPTS_DIR  = scripts

# ---- LaTeX 配置 ----
XELATEX      = TEXINPUTS=latex: xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD_DIR)

# ---- 数据源 ----
YAML_DATA = $(DATA_DIR)/resume.yaml

# ---- 脚本 ----
YAML_TO_LATEX_SCRIPT = $(SCRIPTS_DIR)/yaml-to-latex.py
YAML_TO_HTML_SCRIPT  = $(HTML_DIR)/js/yaml-to-html.js
HTML_TO_PDF_SCRIPT   = $(HTML_DIR)/js/generate-pdf.js

# ---- LaTeX 入口文件 ----
ENTRY_LATEX = latex/resume.tex

# ---- LaTeX 内容文件（由 YAML 生成）----
LATEX_CONTENT = $(CONTENT_DIR)/resume.tex

# ---- 输出文件 ----
PDF       = $(DIST_DIR)/resume.pdf
LATEX_PDF = $(DIST_DIR)/resume_latex.pdf

# ---- HTML 输出 ----
HTML = $(HTML_DIR)/output/resume.html

# ---- 样式文件依赖 ----
RESUME_CLASS = latex/resume.cls
STYLE_FILES  = latex/zh_CN-systemfonts.sty latex/linespacing_fix.sty latex/fontawesome.sty

# ---- PDF 查看器 ----
PDF_VIEWER = open -a wpsoffice

# ---- 跨平台命令 ----
ifeq ($(OS),Windows_NT)
  RM = cmd //C del //Q
  RMDIR = cmd //C rmdir //S //Q
else
  RM = rm -f
  RMDIR = rm -rf
endif

# ============================================================
# 默认目标
# ============================================================
.PHONY: all help clean view

all: html pdf
	@pkill -x wpsoffice 2>/dev/null || true
	@sleep 0.5
	@$(PDF_VIEWER) $(PDF)

# ============================================================
# 强制刷新 PDF（杀 WPS 进程后重新打开）
# ============================================================
view:
	@pkill -x wpsoffice 2>/dev/null || true
	@sleep 1
	@$(PDF_VIEWER) $(PDF)

# ============================================================
# 帮助信息
# ============================================================
help:
	@echo "简历构建系统"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all          - 构建全部 (HTML + PDF) 并用 WPS 打开"
	@echo "  view         - 强制刷新：杀 WPS 进程后重新打开 PDF"
	@echo "  latex        - 构建 LaTeX PDF (需要 XeLaTeX)"
	@echo "  html         - 生成 HTML"
	@echo "  pdf          - 生成 PDF (从 HTML, 依赖 html)"
	@echo "  yaml-latex   - 从 YAML 生成 LaTeX 内容文件"
	@echo "  yaml-html    - 从 YAML 生成 HTML 文件"
	@echo "  clean        - 清理所有构建产物"
	@echo "  clean-latex  - 清理 LaTeX 构建产物"
	@echo "  clean-html   - 清理 HTML/PDF 构建产物"
	@echo ""
	@echo "Outputs:"
	@echo "  $(DIST_DIR)/resume.pdf       - PDF (Playwright)"
	@echo "  $(DIST_DIR)/resume_latex.pdf - PDF (XeLaTeX)"
	@echo "  $(HTML_DIR)/output/resume.html - HTML 版本"
	@echo "  $(CONTENT_DIR)/resume.tex    - LaTeX 内容文件"

# ============================================================
# 目录创建
# ============================================================
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(DIST_DIR):
	mkdir -p $(DIST_DIR)

$(CONTENT_DIR):
	mkdir -p $(CONTENT_DIR)

$(HTML_DIR)/output:
	mkdir -p $(HTML_DIR)/output

# ============================================================
# YAML → LaTeX 内容生成
# ============================================================
.PHONY: yaml-latex

yaml-latex: $(YAML_DATA) $(YAML_TO_LATEX_SCRIPT) | $(CONTENT_DIR)
	@python3 $(YAML_TO_LATEX_SCRIPT)

$(LATEX_CONTENT): $(YAML_DATA) $(YAML_TO_LATEX_SCRIPT) | $(CONTENT_DIR)
	@python3 $(YAML_TO_LATEX_SCRIPT)

# ============================================================
# LaTeX PDF 构建 (XeLaTeX)
# ============================================================
.PHONY: latex

latex: $(LATEX_PDF)

$(LATEX_PDF): $(ENTRY_LATEX) $(LATEX_CONTENT) $(RESUME_CLASS) $(STYLE_FILES) | $(BUILD_DIR) $(DIST_DIR)
	@$(XELATEX) $(ENTRY_LATEX) > /dev/null 2>&1 || ($(XELATEX) $(ENTRY_LATEX); exit 1)
	cp $(BUILD_DIR)/resume.pdf $(LATEX_PDF)
	@echo "  ✓ $(LATEX_PDF)"

# ============================================================
# YAML → HTML 生成
# ============================================================
.PHONY: yaml-html html

html: yaml-html

yaml-html: $(YAML_DATA) $(YAML_TO_HTML_SCRIPT) | $(HTML_DIR)/output
	cd $(HTML_DIR) && node js/yaml-to-html.js

$(HTML): $(YAML_DATA) $(YAML_TO_HTML_SCRIPT) | $(HTML_DIR)/output
	cd $(HTML_DIR) && node js/yaml-to-html.js

# ============================================================
# HTML → PDF 生成 (Playwright)
# ============================================================
.PHONY: pdf

pdf: $(PDF)

$(PDF): $(HTML) $(HTML_TO_PDF_SCRIPT) | $(DIST_DIR)
	cd $(HTML_DIR) && node js/generate-pdf.js

# ============================================================
# 清理
# ============================================================
.PHONY: clean clean-latex clean-html clean-all

clean-latex:
	$(RMDIR) $(BUILD_DIR)
	$(RMDIR) $(CONTENT_DIR)
	@echo "  ✓ LaTeX artifacts cleaned."

clean-html:
	$(RMDIR) $(HTML_DIR)/output
	$(RMDIR) $(DIST_DIR)
	@echo "  ✓ HTML + PDF artifacts cleaned."

clean: clean-html
	@echo "Done. Use 'make clean-all' to also clean LaTeX artifacts."

clean-all: clean-latex clean-html
	@echo "All build artifacts cleaned."
