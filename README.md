# Career Communication System

> 本仓库是刘波的 **Career Communication System**，而不只是简历项目。
>
> 它维护一套 **Career Knowledge Base**，并从中生成面向不同渠道的输出：Resume A / Resume B / LinkedIn / 自我介绍 / 面试故事 / 项目集 / 技术博客 / 个人网站。

## 目录结构

```
.
├── data/                    # 简历数据源（Source）
│   └── resume.yaml          # 当前简历主数据
├── materials/               # Career Knowledge Base
│   ├── raw/                 # 原材料：代码仓库、文档、PPT、截图、笔记
│   ├── facts/               # 确认的事实（Fact）
│   │   └── facts.yaml       # 已确认事实清单
│   ├── evidence/            # 佐证材料（Evidence）
│   ├── stories/             # 面试故事（Story）
│   ├── coarse/              # 粗料：按项目整理的事实草稿
│   ├── fine/                # 细料：可直接用于简历的 bullet
│   ├── projects/            # 项目详情素材
│   ├── annual-reviews/      # 述职材料
│   └── history-resume/      # 历史简历版本
├── outputs/                 # 输出产物（Output）
│   ├── resume-security.*    # Resume A — Application Security Engineer
│   ├── resume-backend.*     # Resume B — Senior Backend Engineer
│   ├── linkedin.md          # LinkedIn Profile
│   ├── self-intro.md        # 自我介绍
│   └── interview-stories.md # 面试故事集
├── prompts/                 # Claude Code 提示词与任务模板
├── review/                  # Review 记录与决策日志
├── scripts/                 # 构建/生成脚本
├── html/                    # HTML → PDF 构建管道
├── latex/                   # LaTeX 备用构建（非默认）
├── material/                # 历史版本与生成产物（待整理归档）
├── Makefile                 # 构建入口
├── PRD.md                   # Career Communication System 设计规范
├── CLAUDE.md                # 简历内容规则与排版规范
├── README.md
└── LICENSE
```

## 设计原则

- **Career Knowledge Base 是 Single Source of Truth**：所有输出都从 `materials/` 和 `data/` 生成。
- **简历只是 Output 之一**：本系统同时维护 Resume A（Security）和 Resume B（Backend）两个分支。
- **事实驱动**：所有内容必须可追溯至确认事实，不虚构、不夸大。
- **叙事一致性**：每个修改都必须强化候选人的专业身份。

## 构建

依赖：Node.js + Chrome（用于 PDF 生成）

```bash
# 安装依赖
cd html && npm install

# 构建当前默认简历（HTML + PDF）
cd ..
make

# 仅构建 HTML
make html

# 查看所有目标
make help
```

## 关键文档

- **`PRD.md`**：Career Communication System 设计规范（v3.0）
- **`CLAUDE.md`**：简历内容规则、求职定位与排版规范
- **`materials/facts/facts.yaml`**：已确认事实清单

## License

[The MIT License (MIT)](http://opensource.org/licenses/MIT)

Copyrighted fonts are not subjected to this License.
