# Fine Materials（细料）

本目录存放可直接用于简历写作的精炼事实单元（fine material）。

## 加工标准

- 每一句话都符合 **What / Contribution / Impact**。
- 每一句话只回答一个问题。
- 每一句话都有来源，可追溯至 `materials/coarse/` 或 `materials/raw/`。
- 无解释性废话，无技术实现细节，无 Why/How/Trade-off。

## 生成流程

细料在 Phase 6「逐家公司修改」时生成。每家公司基于对应粗料文件，按 Resume Branch 的叙事角度输出可直接写入 YAML 的 bullet。

## 文件规划

| 文件 | 说明 |
|------|------|
| `facts.yaml` | 已确认的全局事实与每项目核心事实 |
| `resume-security-bullets.yaml` | Resume A（Security）可直接使用的 bullet |
| `resume-backend-bullets.yaml` | Resume B（Backend）可直接使用的 bullet |

---

## 当前状态

- `facts.yaml`：已生成，包含已确认事实。
- `resume-security-bullets.yaml` / `resume-backend-bullets.yaml`：待 Phase 6 生成。
