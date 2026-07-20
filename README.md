# 个人简历

本仓库为刘波的个人简历项目，采用 YAML 数据驱动 + HTML/PDF 现代排版。

## 目录结构

```
.
├── data/
│   └── resume.yaml          # 简历唯一数据源
├── html/
│   ├── css/resume.css       # 排版样式
│   ├── js/
│   │   ├── yaml-to-html.js  # YAML → HTML
│   │   └── generate-pdf.js  # HTML → PDF（Playwright + Chrome）
│   └── template/
│       └── resume.html      # Mustache 模板
├── latex/                   # LaTeX 备用构建（非默认）
├── scripts/
│   └── yaml-to-latex.py     # YAML → LaTeX
├── material/                # 历史版本与生成产物
├── materials/               # 原始素材与历史简历
├── Makefile                 # 构建入口
├── README.md
└── LICENSE
```

## 构建

依赖：Node.js + Chrome（用于 PDF 生成）

```bash
# 安装依赖
cd html && npm install

# 构建 HTML + PDF
cd ..
make

# 仅构建 HTML
make html

# 查看所有目标
make help
```

## 设计原则

- **单一数据源**：`data/resume.yaml` 是简历内容的唯一来源。
- **现代排版**：基于 CSS + Playwright 生成 PDF，替代传统 LaTeX 复杂字体依赖。
- **版本化**：关键版本使用 Git tag 管理（`v2.0.0`、`v2.1.0`）。

## License

[The MIT License (MIT)](http://opensource.org/licenses/MIT)

Copyrighted fonts are not subjected to this License.
