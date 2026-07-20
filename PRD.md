# Resume Architecture Specification

> 版本：v1.0  
> 日期：2026-07-20  
> 适用范围：`/Users/liubo/workspace/github/kumustone/resume`

---

## 一、Mission（最高目标）

本项目不是“修改一份简历文档”，而是**设计两款 Resume Product**，分别服务两个不同的招聘市场：

- **Resume A — Application Security Engineer**
  - SDL
  - Security Platform
  - AI Security
  - API Security
  - Security Development
- **Resume B — Senior Backend Engineer**
  - Rust
  - Go
  - Gateway
  - IM
  - Distributed System
  - Network

**核心约束**：两份简历不是完全不同的人，而是**同一个人的两个 Narrative（职业叙事）**。工作经历、时间线、项目事实完全一致；变化的是信息架构、强调角度与 ATS 关键词。

---

## 二、设计原则

**Resume ≠ Biography**

简历不是人生流水账，也不是项目列表。简历是一份 **Information Architecture（信息架构）**。

目标：帮助招聘方在最短时间内建立对候选人的正确认知。

---

## 三、职业主线

候选人的职业经历本质上不是按公司排列，而是按技术能力演进：

```
Linux
  → Network
    → High Performance
      → Gateway
        → Distributed System
          → Security
            → AI Security
```

所有简历修改必须围绕这条主线展开，确保阅读者感受到一条清晰、连续、可解释的职业演进路径。

---

## 四、为什么需要两个版本

候选人的经历是一条连续演进路线，但不同岗位的招聘经理关注点不同：

| 阅读者 | 看到的关键词 | 产生的认知 |
|--------|-------------|-----------|
| Backend 招聘经理 | Gateway / Rust / IM / Network / Distributed System | 我是 Backend |
| Security 招聘经理 | WAF / Risk / Data Security / API Security / AI Security | 我是 Security |

因此需要维护两个 Resume Branch，而不是一份大杂烩。这本质上是 **Git Branch 的思想**：同一棵树，两个分支，不同叙事。

---

## 五、两个 Resume 的区别

| 维度 | Resume A（Security） | Resume B（Backend） |
|------|---------------------|---------------------|
| Summary | 强调安全平台、SDL、AI Security、企业安全建设 | 强调高性能基础设施、Gateway、IM、Rust、分布式 |
| Core Skills | 安全能力域优先 | 系统研发能力域优先 |
| 项目排序 | 安全相关项目前置 | 基础设施相关项目前置 |
| Bullet 强调点 | 风险、合规、检测、防护、安全架构 | 性能、并发、架构、可靠性、工程化 |
| 技术关键词 | WAF、Risk、Data Masking、Prompt Injection、Zero Trust | Pingora、Tokio、epoll、长连接、微服务、QPS/RT |
| ATS 关键词 | Application Security、SDL、API Security、AI Security | Senior Backend、Rust、Gateway、Distributed Systems |

**必须保持一致**：公司、职位、时间、项目、客观事实。

---

## 六、必须保持一致的内容

以下信息在两个 Resume 中必须完全一致，不得虚构、夸大或修改：

- 公司名
- 职位
- 在职时间
- 项目名
- 技术栈（可出现，但不得捏造未使用的技术）
- 可验证的业务结果（QPS、RT、成本、稳定性年限等）

允许改变的是：

- 信息组织方式
- 强调顺序
- Bullet 措辞角度
- 关键词密度与分布

---

## 七、每家公司如何组织

每家公司条目采用以下结构：

```
公司名 + 职位 + 时间
└── 一句话定位
    （在这家公司，我负责什么方向 / 处于什么角色）
    ├── 项目 A
    │   ├── 一句话目标：这个项目是做什么的
    │   ├── 贡献：我做了什么（What / How much）
    │   └── 结果：产生了什么影响（Impact / 量化）
    ├── 项目 B
    │   ├── 一句话目标
    │   ├── 贡献
    │   └── 结果
    └── ...
```

禁止简单罗列项目。每家公司必须先给定位，再给项目。

---

## 八、每个项目如何组织

每个项目 Bullet 只回答三类问题：

1. **What** — 这是什么系统/能力？
2. **Contribution** — 我做了什么？
3. **Impact** — 产生了什么结果？

不回答：

- Why（为什么采用 Rust / Pingora / 这种设计）
- How（具体实现细节、模块拆分、Trade-off）
- 技术深度说明（留给技术面试）

---

## 九、Information Density

高级工程师简历不是信息越多越好。原则是：

- 每一句都有价值。
- 没有废话。
- 没有功能说明书。
- 没有产品手册。
- 没有 API 文档。

**一句话只回答一个问题。** 不要一句话回答三个问题。

---

## 十、每份简历应该给人的第一印象

### Resume A（Security）

> 这是一个长期做企业安全平台的人。懂网络、懂网关、懂开发，所以安全做得比普通安全工程师更深。

### Resume B（Backend）

> 这是一个长期做高性能基础设施的人。懂 Gateway、懂 IM、懂 Rust、懂分布式。安全只是他的工程背景。

---

## 十一、Source Material 机制（物料机制）

### 11.1 原则

简历内容 = 对客观事实物料的**选择性、有叙事角度的串联**。

- 所有客观事实必须先沉淀为 Source Material（物料）。
- 物料是可核对、可追问、可验证的原始素材。
- 简历修改时，只能使用物料库中已确认的事实；不得凭空增加经历或结果。

### 11.2 当前物料清单

| 类型 | 路径 | 说明 |
|------|------|------|
| 主数据 | `data/resume.yaml` | 当前简历统一数据源 |
| 项目详情 | `materials/projects/*.md` | 各项目详细素材 |
| 述职材料 | `materials/annual-reviews/*.md` | 年度/半年度述职 |
| 历史简历 | `materials/history-resume/*` | 历史版本 PDF/MD/DOCX |
| 构建产物 | `material/history-resume/*` | 近期 HTML/PDF 历史版本 |

### 11.3 物料不足时的处理

当发现以下情况时，必须暂停修改，向候选人确认：

- 某个项目缺少可量化的 Impact。
- 某段经历的技术栈或职责边界不清。
- 某个数据（如 QPS、RT、成本降低比例）无法核对。
- 不确定某个经历是否适合放入当前 Resume Branch。

**不要猜测、不要脑补、不要虚构。**

---

## 十二、输出与迭代流程

严禁一次性输出完整简历。按以下阶段推进，每阶段完成后等待确认：

1. **Phase 1 — 现状分析**：分析当前 `data/resume.yaml` 的 Information Architecture 问题。
2. **Phase 2 — Branch 设计**：明确 Resume A / Resume B 的分支定位、差异矩阵、ATS 关键词。
3. **Phase 3 — 整体目录**：输出两份简历的完整目录结构（公司/项目/Bullet 标题）。
4. **Phase 4 — Summary**：分别输出 Resume A 与 Resume B 的 Summary。
5. **Phase 5 — Core Skills**：分别输出两份简历的 Core Skills。
6. **Phase 6 — 逐家公司修改**：每家公司单独修改，改完一家等待 review。

最终目标：

- `data/resume-security.yaml` 或 `output/resume-security.pdf` — Resume A
- `data/resume-backend.yaml` 或 `output/resume-backend.pdf` — Resume B

（具体文件命名在 Phase 2 确定。）

---

## 十三、首席简历架构师职责

> 请把自己当成这份简历的 **Chief Resume Architect**，而不是编辑器。
>
> 你的职责不是修改句子，而是设计一款能够帮助候选人获得目标岗位 Offer 的产品。
>
> 如果发现原有信息组织方式不能体现候选人的真实能力，请大胆重构信息架构。
>
> 但必须遵守：
> 1. 不改变事实；
> 2. 不夸大经历；
> 3. 不增加不存在的内容；
> 4. 工作经历保持时间倒序；
> 5. 技术细节留给面试，简历重职责、贡献与结果；
> 6. 同时维护 Security Resume 与 Backend Resume 两个分支，它们共享同一职业经历，但拥有不同的 Narrative、Summary、Core Skills、项目强调点与 ATS 关键词。

---

## 十四、版本记录

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.0 | 2026-07-20 | 初始版本，从“修改建议”升级为 Resume Architecture Specification |
