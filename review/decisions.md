# Repository Restructure Decision

## 决策

按 PRD.md v3.0 第 10 章「Repository 设计原则」，将 Repository 从单一简历项目升级为 Career Communication System。

## 变更内容

- 新增 `outputs/`：存放 Resume A / Resume B / LinkedIn / 自我介绍 / 面试故事等输出产物。
- 新增 `prompts/`：存放 Claude Code 系统提示与任务模板。
- 新增 `review/`：存放 Review 记录与决策日志。
- 在 `materials/` 下新增：
  - `facts/`：确认的事实（Fact），`facts.yaml` 从 `materials/fine/` 迁移至此。
  - `evidence/`：佐证材料（Evidence）。
  - `stories/`：面试故事（Story）。
- 更新 `README.md` 以反映新结构。
- 更新 `PRD.md` 中 Knowledge Base 的物料分层说明。

## 原因

- 简历只是 Career Communication System 的输出之一。
- 需要明确 Source（`data/`、`materials/`）与 Output（`outputs/`）的边界。
- 为长期维护、多输出渲染、Review 追溯提供清晰的目录结构。

## 时间

2026-07-20

## 涉及文件

- `outputs/README.md`
- `prompts/README.md`
- `review/README.md`
- `materials/facts/README.md`
- `materials/facts/facts.yaml`（从 `materials/fine/` 迁移）
- `materials/evidence/README.md`
- `materials/stories/README.md`
- `materials/fine/README.md`
- `README.md`
- `PRD.md`

---

# Resume A/B Branch Strategy Decision

## 决策

Resume A（Security）与 Resume B（Backend）采用**一个 Git 分支、两个简历文件**的策略。

## 文件规划

- `data/resume-security.yaml` — Resume A 数据源
- `data/resume-backend.yaml` — Resume B 数据源
- `outputs/resume-security.*` — Resume A 输出产物
- `outputs/resume-backend.*` — Resume B 输出产物
- 共享 `materials/` Career Knowledge Base
- 共享 `scripts/`、`html/` 构建管道

## 原因

- Resume A/B 是同一职业经历的两种**渲染（Render）**，不是两个独立项目。
- 事实层（`materials/facts/facts.yaml`、`materials/coarse/`、`materials/evidence/`）完全共享。
- 避免跨分支同步事实的维护成本。
- 便于对比两个简历，确保事实一致。
- 符合 Career Communication System 的 Single Source of Truth 原则。

## 未决事项

- `Makefile` 与 `html/js/yaml-to-html.js`、`html/js/generate-pdf.js` 需要支持双简历输入/输出，将在 Phase 6 实际生成两个简历时实现。
- 当前默认 `data/resume.yaml` 将在 Phase 1-6 完成后被 `data/resume-security.yaml` 和 `data/resume-backend.yaml` 替代。

## 时间

2026-07-20

## 涉及文件

- `data/resume-security.yaml`（待创建）
- `data/resume-backend.yaml`（待创建）
- `Makefile`（待更新）
- `PRD.md`（已更新）
