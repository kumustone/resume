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
