# Career Communication System Specification

> 版本：v3.0  
> 日期：2026-07-20  
> 适用范围：`/Users/liubo/workspace/github/kumustone/resume`

---

## 最高原则

> **The purpose of a resume is not to tell everything you have done, but to make the hiring manager want to interview you.**
>
> 简历的目的不是告诉招聘方你做过的一切，而是让他想面试你。

> **Every modification must strengthen the candidate's professional identity.**
>
> 每一次修改都必须让招聘经理更确信：这就是他要找的人。

任何新增内容都可以用这两条检验：

1. 它是否增强了招聘方对候选人的**认知、兴趣或信任**？
2. 它是否强化了候选人的**专业身份**（Security Resume → Enterprise Security Engineer；Backend Resume → Infrastructure Engineer）？

如果任一答案为否，就应该删掉或重写。

---

## 一、Mission（最高目标）

**Design a Career Communication System.**

设计一套职业沟通系统，而不是几份简历文档。

本 Repository 维护的是 **Career Knowledge Base** —— 职业资料的 Single Source of Truth。所有面向不同渠道的输出都从这里生成：

```
Career Knowledge Base
        │
        ├── Resume A
        ├── Resume B
        ├── LinkedIn
        ├── Self Introduction
        ├── Interview Story
        ├── Project Portfolio
        ├── Tech Blog
        └── Personal Website
```

简历只是这个系统中最重要、但绝不是唯一的 Output。

---

## 二、Core Principle（核心决策原则）

### 2.1 简历不是展示能力，而是降低招聘风险

招聘经理不是在购买技术，而是在降低团队风险。

每一句话都应该帮助招聘经理减少一种顾虑：

| 招聘经理的顾虑 | 简历应该给出的信号 |
|---------------|-------------------|
| 担心不会落地 | 多个 0→1 项目、从设计到上线的完整闭环 |
| 担心不会维护 | 长期负责核心系统、已稳定运行多年 |
| 担心不会合作 | 团队 Leader、跨团队推进、客户现场支持 |
| 担心只是写 Demo | 金融、政企、双11等真实生产环境 |
| 担心只会一种语言 | Go / Rust / C++ 多语言工程实践 |
| 担心年龄大、学习慢 | 持续学习 AI / Pingora / Rust 等新技术 |
| 担心安全背景不够深 | CISSP、WAF、风控、数据安全、AI Security |
| 担心工程能力退化 | 高性能网关、QPS/RT 量化指标 |

### 2.2 修改方向检验

每次修改后，问自己：

> 这次修改，是否让招聘经理更确信这是他要找的人？

- Security Resume：是否更像 **Enterprise Security Engineer**？
- Backend Resume：是否更像 **Infrastructure Engineer**？

如果答案是否定的，即使这句话是真实的、有技术含量的，也应该删掉或换个角度表达。

---

## 三、Design Philosophy（设计哲学）

### 3.1 Resume is designed for scanning, not reading

| 阅读者 | 平均停留时间 | 简历的任务 |
|--------|-------------|-----------|
| HR / 简历筛选系统 | 20–30 秒 | 快速匹配关键词，决定是否通过 |
| Hiring Manager | 2–5 分钟 | 判断候选人与岗位的匹配度 |
| Technical Interviewer | 60–90 分钟（面试中） | 基于简历深入技术细节 |

简历的任务是**帮助候选人进入面试**，而不是在面试前回答所有问题。

### 3.2 Maximize curiosity, not explanation

简历应该最大化招聘方的好奇心，而不是最大化解释。

- ✅ 写：基于 Pingora 重构网关，QPS +138%，RT -63%。
- ❌ 不写：为什么选 Pingora、Pingora 的线程模型、模块如何拆分、异步 trait 如何处理阻塞。

技术深度留给面试。简历只负责制造「值得面试」的信号。

### 3.3 Every sentence should create a question

每一句话都应该引发招聘方的一个好问题，而不是把问题全部回答完。

- ✅ 「设计并落地企业级 AI 安全网关，服务金融、政企客户。」
  - 引发问题：AI 安全网关做了哪些检测？性能如何？客户规模多大？
- ❌ 「采用 Rust 是因为其内存安全特性，使用 Pingora 是因为 Cloudflare 开源的高性能代理框架……」
  - 没有引发问题，只是在解释。

### 3.4 Resume ≠ Biography

简历不是人生流水账，也不是项目列表。简历是一份 **Information Architecture（信息架构）**。

目标：帮助招聘方在最短时间内建立对候选人的正确认知。

### 3.5 Resume Deletion Principle

> **Perfection is achieved not when there is nothing more to add, but when there is nothing left to remove.**

如果一句话满足下面任何一项，删：

- 不影响 Offer
- 不影响 ATS
- 不影响 Narrative
- 不影响招聘经理决策
- 不降低招聘风险
- 不强化专业身份

简历的信息预算是有限的。每一句话都必须有存在的理由。

---

## 四、Career Arc（职业价值演进主线）

候选人的职业经历本质上不是按公司排列，而是按**职业价值**演进：

```
Reliable Software Engineering
        ↓
High Performance Infrastructure
        ↓
    Large Scale Backend
        ↓
    Enterprise Platform
        ↓
    Enterprise Security
        ↓
     AI Infrastructure
```

这是招聘经理能读懂的语言：

| 阶段 | 含义 | 对应经历 |
|------|------|---------|
| Reliable Software Engineering | 电信级工程纪律、高可靠软件交付 | 华为 VFM 模块 |
| High Performance Infrastructure | 高性能网络服务、长连接、协议解析 | 千方/中交兴路 CADN、蘑菇街 IM |
| Large Scale Backend | 大规模后端系统、网关、分布式 | 蘑菇街 WAF、玩物得志风控 |
| Enterprise Platform | 企业级平台建设、0→1 产品化 | 玩物得志安全治理、闪捷 nginx_merry |
| Enterprise Security | 企业安全平台、风控、数据安全、合规 | 玩物得志风控/反垃圾、闪捷 r_data_service |
| AI Infrastructure | AI 网关、AI 安全、新一代基础设施 | 闪捷 Nexis、AI 研究 |

所有简历修改必须围绕这条主线展开，确保阅读者感受到一条清晰、连续、可解释的职业演进路径。

---

## 五、Resume Product 定义

本系统最终输出两款 Resume Product，分别服务两个招聘市场：

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

## 六、为什么需要两个版本

候选人的经历是一条连续演进路线，但不同岗位的招聘经理关注点不同：

| 阅读者 | 看到的关键词 | 产生的认知 |
|--------|-------------|-----------|
| Backend 招聘经理 | Gateway / Rust / IM / Network / Distributed System | 我是 Backend |
| Security 招聘经理 | WAF / Risk / Data Security / API Security / AI Security | 我是 Security |

因此需要维护两个 Resume Branch，而不是一份大杂烩。这本质上是 **Git Branch 的思想**：同一棵树，两个分支，不同叙事。

---

## 七、两个 Resume 的区别

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

## 八、必须保持一致的内容

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

## 九、Knowledge Base（知识库）

### 9.1 知识流

Career Knowledge Base 不是资料堆，而是有层次的知识流：

```
        Fact
          ↓
       Evidence
          ↓
        Story
          ↓
     Resume Bullet
```

- **Fact**：客观事实，如「QPS +138%」。
- **Evidence**：事实的佐证，如 Benchmark 数据、客户反馈、专利证书。
- **Story**：可复用的面试故事，如 STAR 结构的项目经历。
- **Resume Bullet**：最终写入简历的一句话。

Resume 只是最后一层，不是第二层。

### 9.2 目录结构

```
resume/
├── data/                  # 当前简历主数据（Source）
├── materials/             # Career Knowledge Base
│   ├── raw/               # 原材料
│   │   ├── repos/         # 代码仓库
│   │   ├── docs/          # 文档/PDF
│   │   ├── slides/        # PPT/Keynote
│   │   ├── screenshots/   # 截图/架构图
│   │   └── notes/         # 零散笔记
│   ├── facts/             # 确认的事实（Fact）
│   ├── evidence/          # 佐证材料（Evidence）
│   ├── stories/           # 面试故事（Story）
│   ├── coarse/            # 粗料（按项目整理）
│   └── fine/              # 细料（可直接用于简历）
├── outputs/               # 输出产物
│   ├── resume-security.*
│   ├── resume-backend.*
│   ├── linkedin.md
│   └── self-intro.md
├── prompts/               # Claude Code 提示词与系统指令
├── scripts/               # 构建/生成脚本
├── review/                # Review 记录与决策日志
└── PRD.md                 # 本规范
```

### 9.3 当前物料分层

| 层级 | 路径 | 说明 |
|------|------|------|
| 原材料（raw） | `materials/raw/` | 代码仓库、文档、PPT、截图、笔记等原始物料 |
| 事实（facts） | `materials/facts/facts.yaml` | 已确认的客观事实清单 |
| 粗料（coarse） | `materials/coarse/` | 按项目/公司整理的事实草稿，回答 What / Contribution / Impact |
| 细料（fine） | `materials/fine/` | 可直接用于简历的 bullet 单元 |
| 主数据 | `data/resume.yaml` | 当前简历统一数据源 |
| 项目详情 | `materials/projects/*.md` | 各项目详细素材 |
| 述职材料 | `materials/annual-reviews/*.md` | 年度/半年度述职 |
| 历史简历 | `materials/history-resume/*` | 历史版本 PDF/MD/DOCX |
| 构建产物 | `material/history-resume/*` | 近期 HTML/PDF 历史版本 |

### 9.4 主项目与子项目/配套能力的呈现原则

同一公司下，若存在多个相关仓库或子系统，简历中可采用两种组织方式：

- **独立项目**：适合强调产品线广度或 Security Resume 中突出安全能力矩阵。
- **并入主项目**：适合强调核心系统深度或 Backend Resume 中突出工程聚焦。

例如闪捷：
- 核心项目：Nexis、nginx_merry、r_data_service
- 配套能力：secagent（节点管理）、AI-dataset（数据管理）、AI 研究（技术预研）、flint-ocr（OCR 识别）、file-inspector（文件检测）

具体是否独立或并入，由 Resume Branch 的叙事需求决定，并在 Phase 3「整体目录」中明确。

### 9.5 物料不足时的处理

当发现以下情况时，必须暂停修改，向候选人确认：

- 某个项目缺少可量化的 Impact。
- 某段经历的技术栈或职责边界不清。
- 某个数据（如 QPS、RT、成本降低比例）无法核对。
- 不确定某个经历是否适合放入当前 Resume Branch。

**不要猜测、不要脑补、不要虚构。**

---

## 十、Repository 设计原则

本 Repository 采用类似软件工程的 Source / Build / Output 结构：

| 目录 | 角色 | 说明 |
|------|------|------|
| `data/` | Source | 简历唯一数据源，人工维护 |
| `materials/` | Knowledge Base | 职业知识库，持续积累 |
| `outputs/` | Output | 面向不同渠道的最终产物 |
| `prompts/` | Prompts | Claude Code 系统提示与任务模板 |
| `scripts/` | Scripts | 构建、生成、检查脚本 |
| `review/` | Review Log | Review 记录、决策日志、版本说明 |
| `PRD.md` | Spec | 本规范 |

**原则**：

- `data/` 和 `materials/` 是 Source，不可由脚本自动生成后覆盖。
- `outputs/` 是 Generated，可以从 Source 和 Knowledge Base 重新生成。
- 所有修改必须有记录：要么更新 `data/`，要么更新 `materials/`，要么在 `review/` 留下决策说明。

---

## 十一、每家公司如何组织

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

## 十二、每个项目如何组织

每个项目 Bullet 只回答三类问题：

1. **What** — 这是什么系统/能力？
2. **Contribution** — 我做了什么？
3. **Impact** — 产生了什么结果？

不回答：

- Why（为什么采用 Rust / Pingora / 这种设计）
- How（具体实现细节、模块拆分、Trade-off）
- 技术深度说明（留给技术面试）

---

## 十三、Information Density

高级工程师简历不是信息越多越好。原则是：

- 每一句都有价值。
- 没有废话。
- 没有功能说明书。
- 没有产品手册。
- 没有 API 文档。

**一句话只回答一个问题。** 不要一句话回答三个问题。

---

## 十四、经历权重与核心开发者定位

### 14.1 核心开发者定位

在所有项目物料中，候选人均为**绝对的核心开发角色**。简历描述必须体现这一点：

- 使用「独立设计并开发」「主导」「核心开发 / 架构设计」「从 0 到 1 搭建」等表述。
- 避免弱化表达，如「参与」「协助」「负责部分模块」等，除非事实确实如此。
- 若某项目中候选人并非核心角色，则该项目不应作为重点出现。

### 14.2 经历权重分配

简历篇幅和细节密度应按工作经历的新近程度递减：

| 优先级 | 时间段 | 公司 | 简历中的处理方式 |
|--------|--------|------|-----------------|
| P0 | 2022.04-至今 | 闪捷信息科技 | 最详细；3 个核心项目（Nexis、nginx_merry、r_data_service）重点展开，5 个配套能力（secagent、AI-dataset、AI 研究、flint-ocr、file-inspector）按 Resume Branch 选择独立或并入 |
| P1 | 2019.08-2022.03 | 玩物得志 | 详细，2-3 个项目 |
| P2 | 2015.05-2019.08 | 蘑菇街 | 中等，2-3 个项目 |
| P3 | 2009-2015 | 千方/中交兴路 / 华为 | 简要，作为能力起点和长期工程纪律背书 |

**原则**：

- 最近 5-10 年的经历占简历主体篇幅（约 70%）。
- 早期经历用于建立「电信级工程纪律」「底层系统能力」「长期技术演进」的叙事，不展开技术细节。
- 同一家公司内部，也按项目重要性和候选人贡献度分配 bullet 数量。

---

## 十五、每份简历应该给人的第一印象

### Resume A（Security）

> 这是一个长期做企业安全平台的人。懂网络、懂网关、懂开发，所以安全做得比普通安全工程师更深。

### Resume B（Backend）

> 这是一个长期做高性能基础设施的人。懂 Gateway、懂 IM、懂 Rust、懂分布式。安全只是他的工程背景。

---

## 十六、Resume Reading Order

不同角色的阅读路径不同。Claude 在设计简历时应确保关键信息在每个路径上都快速可见。

### HR / 简历筛选系统（20–30 秒）

```
Summary
  ↓
Core Skills
  ↓
Recent Company / Role
  ↓
ATS Keywords
```

### Hiring Manager（2–5 分钟）

```
Summary
  ↓
最近 1-2 个核心项目
  ↓
每家公司的一句话定位
  ↓
量化结果
  ↓
Core Skills（验证匹配度）
```

### CEO / 高级管理者

```
Summary
  ↓
最近项目影响力
  ↓
0→1 建设能力
  ↓
行业/客户影响力
```

### Technical Interviewer（面试中）

```
项目标题
  ↓
What / Contribution / Impact
  ↓
引发深入技术问题的钩子
```

**设计原则**：

- 前 1/3 页面必须回答「他是谁」「他做什么」「他是否匹配这个岗位」。
- 量化结果必须在快速扫描时可见。
- 技术深度细节均匀分布，为面试预留提问点。

---

## 十七、ATS Strategy

ATS 是必要但不充分条件。简历首先要通过 ATS，但最终征服的是 Hiring Manager。

### 17.1 目标岗位关键词矩阵

#### Resume A（Application Security Engineer）

| 关键词类别 | 关键词 |
|-----------|--------|
| 岗位 | Application Security Engineer、Security Engineer、Security Platform Engineer、AI Security Engineer |
| 领域 | SDL、DevSecOps、API Security、AI Security、Data Security、Cloud Security |
| 产品/能力 | WAF、Web Application Firewall、Threat Detection、Risk Control、Data Masking、Watermark、Prompt Injection、DLP |
| 合规/治理 | Security Compliance、MLPS、等保、Vulnerability Management、Incident Response、Security Audit |
| 技术 | Rust、Go、C++、Nginx、Gateway、Microservices、Kafka、Redis |

#### Resume B（Senior Backend Engineer）

| 关键词类别 | 关键词 |
|-----------|--------|
| 岗位 | Senior Backend Engineer、Staff Software Engineer、Senior Software Engineer、Infrastructure Engineer |
| 领域 | Distributed Systems、High Performance、Network Programming、Gateway、IM、Concurrency |
| 技术/框架 | Rust、Go、C++、Tokio、Pingora、Nginx、gRPC、Microservices、Event-Driven |
| 基础设施 | Kafka、Redis、ZooKeeper、Docker、Kubernetes、ClickHouse、LVS |
| 协议/网络 | TCP/IP、HTTP/HTTPS、WebSocket、SSE、NDJSON、epoll、Long Connection |

### 17.2 关键词密度策略

关键词不应随机出现，应在关键位置均匀分布：

| 位置 | 目标 |
|------|------|
| Summary | 每个核心关键词出现 1 次 |
| Core Skills | 每个核心关键词明确列出 1 次 |
| 最近 1-2 家公司 | 每个核心关键词在项目描述中出现 1-2 次 |
| 早期经历 | 不强制铺关键词，自然出现即可 |

**原则**：关键词服务于 ATS 和人类阅读，不堆砌、不重复、不牺牲可读性。

---

## 十八、Resume Budget（信息预算）

### 18.1 总体篇幅

- **Resume 长度**：2 页
- **字数预算**：900–1200 词（中文约 1500–2000 字）

### 18.2 篇幅分配

| 模块 | 占比 | 说明 |
|------|------|------|
| 最近 5-10 年经历 | ~70% | 闪捷 + 玩物得志 |
| 早期经历 | ~20% | 蘑菇街 + 千方/中交兴路 + 华为 |
| 教育 / 其他 | ~10% | 学历、证书、专利等 |

### 18.3 每家公司 Bullet 预算

| 优先级 | 每家公司 Bullet 数量建议 |
|--------|------------------------|
| P0（闪捷） | 每项目 2–4 个 bullet，全公司 8–12 个 bullet |
| P1（玩物得志） | 每项目 2–3 个 bullet，全公司 6–9 个 bullet |
| P2（蘑菇街） | 每项目 1–3 个 bullet，全公司 4–7 个 bullet |
| P3（早期） | 每段经历 1–2 个 bullet |

---

## 十九、Narrative Consistency（叙事一致性）

每一份简历中的每一家公司、每一个项目，最终都必须服务于同一个 Narrative：

- **Resume A**：所有内容共同证明候选人是 **Enterprise Security Engineer**。
- **Resume B**：所有内容共同证明候选人是 **Infrastructure Engineer**。

### 19.1 每家公司如何推进 Narrative

| 公司 | Resume A 叙事 | Resume B 叙事 |
|------|---------------|---------------|
| 华为 | 电信级高可靠系统安全意识奠基 | C / Linux Kernel / 文件系统底层研发奠基 |
| 千方/中交兴路 | 国家级平台高可靠接入、长连接安全治理能力奠基 | C++ 分布式车联网平台、epoll 长连接、十万级并发设计能力奠基 |
| 蘑菇街 | IM 长连接安全、WAF 网关、企业安全治理 | 高性能 IM 基础设施、自研长连接 SDK、WAF 网关工程化 |
| 玩物得志 | 业务风控、反垃圾、企业安全治理与合规 | 高并发风控引擎、高性能文本处理、从 0 到 1 平台建设 |
| 闪捷 | AI 安全网关、API 安全、数据安全引擎 | Rust/Pingora 高性能网关、分布式安全基础设施、数据安全引擎 |

### 19.2 检查方法

每写完一个项目后，问自己：

> 这个项目是否让招聘方更相信「他是 Enterprise Security Engineer」或「他是 Infrastructure Engineer」？

如果不能，要么调整叙述角度，要么考虑删除或简化。

---

## 二十、输出与迭代流程

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

## 二十一、When to Ask Instead of Writing

以下情况出现时，**必须立即停止生成**，先向候选人提问，确认后再继续：

- [ ] 缺少量化指标
- [ ] Impact 无法验证
- [ ] 技术栈冲突或描述不一致
- [ ] 公司 / 项目 / 时间存在冲突
- [ ] Narrative 出现断层（某段经历无法支撑当前 Resume Branch 的专业身份）
- [ ] ATS 关键词与目标岗位冲突
- [ ] Resume 超过信息预算
- [ ] 两个 Resume Branch 出现事实不一致
- [ ] 不确定某个项目是否独立呈现或并入主项目
- [ ] 发现原材料与已有事实矛盾

**原则**：不确定就停，不猜测、不脑补、不为了写而写。

---

## 二十二、Resume Review Checklist（输出前检查清单）

每阶段输出前，必须逐项检查：

### 内容质量

- [ ] 有没有流水账？
- [ ] 有没有产品说明书？
- [ ] 有没有 API 文档？
- [ ] 有没有一句话回答三个问题？
- [ ] 有没有 Why？
- [ ] 有没有 Implementation Detail？
- [ ] 有没有一句废话？
- [ ] 有没有重复表达？
- [ ] 有没有项目之间重复的内容？

### 事实与一致性

- [ ] 是否改变了事实？
- [ ] 是否夸大了经历？
- [ ] 是否增加了不存在的内容？
- [ ] 公司、职位、时间是否一致？
- [ ] 工作经历是否保持时间倒序？

### ATS 与关键词

- [ ] 是否包含目标岗位 ATS 关键词？
- [ ] 关键词密度是否合理（不堆砌、不遗漏）？
- [ ] 技术术语是否准确？

### Narrative

- [ ] 是否符合当前 Resume Branch 定位？
- [ ] 每家公司是否推进了 Narrative？
- [ ] 是否服务于「Enterprise Security Engineer」或「Infrastructure Engineer」形象？

### 预算

- [ ] 是否在 2 页 / 900–1200 词预算内？
- [ ] 最近 5-10 年经历是否占约 70%？
- [ ] 每家公司 bullet 数量是否符合优先级预算？

### 沟通效率与风险降低

- [ ] 每一句话是否提升了沟通效率？
- [ ] 是否帮助招聘经理更快建立正确认知？
- [ ] 是否降低了至少一种招聘风险？
- [ ] 是否强化了候选人的专业身份？
- [ ] 是否让招聘经理想面试这个候选人？

---

## 二十三、首席职业叙事架构师职责

> 请把自己当成这位候选人的 **Chief Career Narrative Architect**，而不是编辑器。>
> 你的职责不是修改句子，而是设计一套能够帮助候选人获得目标岗位 Offer 的职业沟通系统。
>
> 如果发现原有信息组织方式不能体现候选人的真实能力，请大胆重构信息架构。
>
> 但必须遵守：
> 1. 不改变事实；
> 2. 不夸大经历；
> 3. 不增加不存在的内容；
> 4. 工作经历保持时间倒序；
> 5. 技术细节留给面试，简历重职责、贡献与结果；
> 6. 同时维护 Security Resume 与 Backend Resume 两个分支，它们共享同一职业经历，但拥有不同的 Narrative、Summary、Core Skills、项目强调点与 ATS 关键词；
> 7. 不确定时先提问，不为了写而写。

---

## 二十四、版本记录

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.0 | 2026-07-20 | 初始版本，从“修改建议”升级为 Resume Architecture Specification |
| v1.1 | 2026-07-20 | 增加经历权重与核心开发者定位；明确早期工作经历简写原则 |
| v1.2 | 2026-07-20 | 补充物料分层体系（raw/coarse/fine）；增加主项目与子项目/配套能力的呈现原则；更新闪捷项目清单 |
| v2.0 | 2026-07-20 | 全面升级：最高原则、Mission 升维、Design Philosophy、Knowledge Base、ATS Strategy、Resume Budget、Narrative Consistency、Resume Review Checklist、优化职业主线 |
| v3.0 | 2026-07-20 | 升维为 Career Communication System：新增 Hiring Risk Reduction、Resume Reading Order、Resume Deletion Principle、Repository 设计原则、When to Ask Instead of Writing、Fact→Evidence→Story→Resume 知识流、职业价值演进主线 |
