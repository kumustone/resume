# Phase 1 → Phase 2 用户确认

## 用户回答

| # | 问题 | 回答 |
|---|------|------|
| 1 | 是否将 `resume.yaml` 拆分为 `resume-security.yaml` 和 `resume-backend.yaml`？ | **拆分**。 |
| 2 | 是否删除 `profile.birth_year`？ | **不删除**，原先的基本格式不变。 |
| 3 | 闪捷 5 个配套项目如何呈现？ | **flint-ocr 和 file-inspector 用一个 Item 简要提及即可**，不独立展开。secagent、AI-dataset、AI 研究的具体呈现方式待 Phase 3 确定。 |
| 4 | 蘑菇街「企业级信息安全治理」是否需要在 Resume A 中补充？ | **可以提醒/补充**。 |
| 5 | 已确认数据是否可以公开写入？ | **不写具体客户名**，可大概写项目涉及行业，如金融、汽车、政务、互联网等。 |

## 决策影响

1. **YAML 格式保持**：`profile`、`summary`、`core_skills`、`experience`、`education` 等字段结构不变。
2. **双文件并行**：创建 `data/resume-security.yaml` 和 `data/resume-backend.yaml`。
3. **客户信息脱敏**：简历中只写行业领域，不写具体客户名称。
4. **闪捷项目精简**：flint-ocr / file-inspector 合并或简要提及，不单独成项目。
5. **Resume A 补充安全治理**：蘑菇街信息安全治理项目需要出现。

## 时间

2026-07-20
