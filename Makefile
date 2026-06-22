# ============================================================
# 简历统一构建入口 Makefile
# 支持: LaTeX (XeLaTeX) + HTML + PDF 三种输出
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
YAML_DATA    = $(DATA_DIR)/resume.yaml

# ---- 脚本 ----
YAML_TO_LATEX_SCRIPT = $(SCRIPTS_DIR)/yaml-to-latex.py
YAML_TO_HTML_SCRIPT  = $(HTML_DIR)/js/yaml-to-html.js
HTML_TO_PDF_SCRIPT   = $(HTML_DIR)/js/generate-pdf.js

# ---- LaTeX 入口文件 ----
ENTRY_GATEWAY  = latex/resume.tex
ENTRY_SECURITY = latex/resume_security.tex

# ---- LaTeX 内容文件（由 YAML 生成）----
LATEX_CONTENT_GATEWAY  = $(CONTENT_DIR)/resume.tex
LATEX_CONTENT_SECURITY = $(CONTENT_DIR)/resume_security.tex

# ---- 输出文件 ----
PDF_GATEWAY       = $(DIST_DIR)/resume_gateway.pdf
PDF_SECURITY      = $(DIST_DIR)/resume_security.pdf
LATEX_PDF_GATEWAY = $(DIST_DIR)/resume_latex.pdf
LATEX_PDF_SECURITY= $(DIST_DIR)/resume_security_latex.pdf

# ---- HTML 输出 ----
HTML_GATEWAY  = $(HTML_DIR)/output/resume_gateway.html
HTML_SECURITY = $(HTML_DIR)/output/resume_security.html

# ---- 样式文件依赖 ----
RESUME_CLASS = latex/resume.cls
STYLE_FILES  = latex/zh_CN-systemfonts.sty latex/linespacing_fix.sty latex/fontawesome.sty

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
.PHONY: all help clean

all: html pdf

# ============================================================
# 帮助信息
# ============================================================
help:
	@echo "简历统一构建系统"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all          - 构建全部 (HTML + PDF)"
	@echo "  latex        - 仅构建 LaTeX PDF (需要 XeLaTeX)"
	@echo "  html         - 仅生成 HTML"
	@echo "  pdf          - 仅生成 PDF (从 HTML, 依赖 html)"
	@echo "  gateway      - 构建网关方向全部输出"
	@echo "  security     - 构建安全方向全部输出"
	@echo "  yaml-latex   - 从 YAML 生成 LaTeX 内容文件"
	@echo "  yaml-html    - 从 YAML 生成 HTML 文件"
	@echo "  clean        - 清理所有构建产物"
	@echo "  clean-latex  - 仅清理 LaTeX 构建产物"
	@echo "  clean-html   - 仅清理 HTML/PDF 构建产物"
	@echo ""
	@echo "Outputs:"
	@echo "  $(DIST_DIR)/resume_gateway.pdf       - 网关方向 PDF (Playwright)"
	@echo "  $(DIST_DIR)/resume_security.pdf      - 安全方向 PDF (Playwright)"
	@echo "  $(DIST_DIR)/resume_latex.pdf         - 网关方向 PDF (XeLaTeX)"
	@echo "  $(DIST_DIR)/resume_security_latex.pdf- 安全方向 PDF (XeLaTeX)"
	@echo "  $(HTML_DIR)/output/*.html            - HTML 版本"
	@echo "  $(CONTENT_DIR)/*.tex           - LaTeX 内容文件"

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

$(LATEX_CONTENT_GATEWAY): $(YAML_DATA) $(YAML_TO_LATEX_SCRIPT) | $(CONTENT_DIR)
	@python3 $(YAML_TO_LATEX_SCRIPT)

$(LATEX_CONTENT_SECURITY): $(YAML_DATA) $(YAML_TO_LATEX_SCRIPT) | $(CONTENT_DIR)
	@python3 $(YAML_TO_LATEX_SCRIPT)

# ============================================================
# LaTeX PDF 构建 (XeLaTeX)
# ============================================================
.PHONY: latex latex-gateway latex-security

latex: latex-gateway latex-security

latex-gateway: $(LATEX_PDF_GATEWAY)
latex-security: $(LATEX_PDF_SECURITY)

$(LATEX_PDF_GATEWAY): $(ENTRY_GATEWAY) $(LATEX_CONTENT_GATEWAY) $(RESUME_CLASS) $(STYLE_FILES) | $(BUILD_DIR) $(DIST_DIR)
	@$(XELATEX) $(ENTRY_GATEWAY) > /dev/null 2>&1 || ($(XELATEX) $(ENTRY_GATEWAY); exit 1)
	cp $(BUILD_DIR)/resume.pdf $(LATEX_PDF_GATEWAY)
	@echo "  ✓ $(LATEX_PDF_GATEWAY)"

$(LATEX_PDF_SECURITY): $(ENTRY_SECURITY) $(LATEX_CONTENT_SECURITY) $(RESUME_CLASS) $(STYLE_FILES) | $(BUILD_DIR) $(DIST_DIR)
	@$(XELATEX) $(ENTRY_SECURITY) > /dev/null 2>&1 || ($(XELATEX) $(ENTRY_SECURITY); exit 1)
	cp $(BUILD_DIR)/resume_security.pdf $(LATEX_PDF_SECURITY)
	@echo "  ✓ $(LATEX_PDF_SECURITY)"

# ============================================================
# YAML → HTML 生成
# ============================================================
.PHONY: yaml-html html

html: yaml-html

yaml-html: $(YAML_DATA) $(YAML_TO_HTML_SCRIPT) | $(HTML_DIR)/output
	cd $(HTML_DIR) && node js/yaml-to-html.js

$(HTML_GATEWAY): $(YAML_DATA) $(YAML_TO_HTML_SCRIPT) | $(HTML_DIR)/output
	cd $(HTML_DIR) && node js/yaml-to-html.js

$(HTML_SECURITY): $(YAML_DATA) $(YAML_TO_HTML_SCRIPT) | $(HTML_DIR)/output
	cd $(HTML_DIR) && node js/yaml-to-html.js

# ============================================================
# HTML → PDF 生成 (Playwright)
# ============================================================
.PHONY: pdf pdf-gateway pdf-security

pdf: pdf-gateway pdf-security

pdf-gateway: $(PDF_GATEWAY)
pdf-security: $(PDF_SECURITY)

$(PDF_GATEWAY): $(HTML_GATEWAY) $(HTML_TO_PDF_SCRIPT) | $(DIST_DIR)
	cd $(HTML_DIR) && node js/generate-pdf.js

$(PDF_SECURITY): $(HTML_SECURITY) $(HTML_TO_PDF_SCRIPT) | $(DIST_DIR)
	cd $(HTML_DIR) && node js/generate-pdf.js

# ============================================================
# 方向聚合构建
# ============================================================
.PHONY: gateway security

gateway: $(PDF_GATEWAY) $(HTML_GATEWAY)
	@echo "Gateway direction build complete."

security: $(PDF_SECURITY) $(HTML_SECURITY)
	@echo "Security direction build complete."

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
