# Phase 2 — Resume A/B Branch 定位与 ATS 策略

## 用户确认摘要

- 拆分为 `data/resume-security.yaml` 与 `data/resume-backend.yaml`。
- 保留 `profile.birth_year` 和现有 YAML 基本格式。
- flint-ocr / file-inspector 用一个 Item 简要提及。
- Resume A 补充蘑菇街企业级信息安全治理项目。
- 不写具体客户名，只写行业领域（金融、汽车、政务、互联网等）。

---

## 一、Resume A — Application Security Engineer

### 1.1 目标岗位

- Primary：Application Security Engineer / Security Platform Engineer
- Secondary：AI Security Engineer / API Security Engineer / Security Development Engineer
- 目标公司：金融、政企、互联网大厂安全部门、安全厂商、甲方安全团队

### 1.2 招聘经理画像

- 安全团队负责人 / Security Hiring Manager
- 关注点：是否能建设企业级安全平台、是否懂安全又懂开发、是否有 0→1 产品经验、是否能落地合规与风控
- 阅读时间：2–5 分钟

### 1.3 简历必须证明的核心命题

> **「我是一个长期建设企业安全平台的人，懂网络、懂网关、懂开发，安全做得比普通安全工程师更深。」**

### 1.4 关键能力信号

- **AI 安全网关**：Prompt Injection、SSE/NDJSON 流式审核、大模型内容安全
- **API 安全网关**：WAF、访问控制、数据脱敏、水印、审计追溯
- **数据安全引擎**：敏感数据识别、脱敏、水印、多形态服务化
- **业务风控与反垃圾**：实时风控、异常行为检测、规则引擎
- **企业安全治理**：等保合规、HIDS、漏洞扫描、安全运营

### 1.5 项目权重与排序

1. **闪捷 Nexis** — AI 安全网关（P0，最详细）
2. **闪捷 nginx_merry** — API 安全网关（P0，详细）
3. **闪捷 r_data_service** — 数据安全引擎（P0，详细）
4. **玩物得志 业务风控引擎** — 实时风控（P1，详细）
5. **玩物得志 高性能文本反垃圾系统** — 内容安全（P1，中等）
6. **玩物得志 企业级安全治理与等保合规** — 安全治理（P1，中等）
7. **蘑菇街 WAF 网关** — Web 应用安全（P2，中等）
8. **蘑菇街 企业级信息安全治理** — HIDS / 漏洞扫描 / 防火墙（P2，补充）
9. **蘑菇街 自研 IM** — 长连接安全基础（P2，简要）
10. **千方/中交兴路 CADN** — 车联网安全接入（P3，简要）
11. **华为 VFM** — 电信级安全工程纪律（P3，一句）
12. **flint-ocr / file-inspector** — 文件/图片敏感检测（用一个 Item 在 r_data_service 或 Nexis 中提及）

---

## 二、Resume B — Senior Backend Engineer

### 2.1 目标岗位

- Primary：Senior Backend Engineer / Staff Software Engineer
- Secondary：Infrastructure Engineer / Gateway Engineer / Distributed Systems Engineer
- 目标公司：外企 R&D、云厂商、基础设施团队、高性能网关团队、IM/实时通信团队

### 2.2 招聘经理画像

- Backend Hiring Manager / Infrastructure TL
- 关注点：高性能、高并发、分布式、Rust/Go、网关、长连接、工程化能力
- 阅读时间：2–5 分钟

### 2.3 简历必须证明的核心命题

> **「我是一个长期做高性能基础设施的人，懂 Gateway、懂 IM、懂 Rust、懂分布式。安全只是我的工程背景。」**

### 2.4 关键能力信号

- **高性能异步网关**：Rust / Pingora、QPS/RT 优化、插件化架构
- **C++ 网关 / Nginx 模块**：高并发代理、热更新、进程间通信
- **长连接基础设施**：IM 系统、自研 SDK、epoll/kqueue、跨平台
- **分布式系统**：服务发现、一致性哈希、消息总线、集群化
- **数据引擎服务化**：多 crate 架构、JNI、HTTP Server、SDK
- **多语言工程能力**：Go / Rust / C++

### 2.5 项目权重与排序

1. **闪捷 Nexis** — Rust/Pingora 高性能 AI 网关（P0，最详细）
2. **闪捷 nginx_merry** — C++ Nginx 高性能安全网关（P0，详细）
3. **闪捷 r_data_service** — Rust 多形态数据服务引擎（P0，详细）
4. **蘑菇街 自研 IM** — C++ 长连接基础设施（P2，详细）
5. **蘑菇街 WAF 网关** — Go 高性能网关 + 自研 tcpstream（P2，中等）
6. **玩物得志 业务风控引擎** — 高并发实时决策系统（P1，中等）
7. **玩物得志 高性能文本反垃圾系统** — 高性能检测引擎（P1，简要）
8. **千方/中交兴路 CADN** — 分布式车联网接入平台（P3，简要）
9. **华为 VFM** — 电信级工程纪律奠基（P3，一句）
10. **玩物得志 企业级安全治理** — 基础设施运维与合规（P1，可选/简要）
11. **蘑菇街 企业级信息安全治理** — 可选/简要或删除
12. **flint-ocr / file-inspector** — 用一个 Item 在 r_data_service 中提及 OCR/文件解析能力

---

## 三、Resume A/B 差异矩阵

| 维度 | Resume A（Security） | Resume B（Backend） |
|------|---------------------|---------------------|
| **目标岗位** | Application Security Engineer / Security Platform Engineer | Senior Backend Engineer / Infrastructure Engineer |
| **第一印象** | 企业安全平台建设者 | 高性能基础设施工程师 |
| **Summary 核心** | 15 年系统研发 + 企业安全平台 + AI 安全实践 | 15 年系统研发 + 高性能网关/IM/分布式 + Rust/Go |
| **Core Skills 第一优先级** | 安全能力域（WAF、风控、数据安全、AI 安全） | 系统研发能力域（网关、IM、分布式、Rust/Go） |
| **项目排序** | 安全相关项目前置 | 基础设施相关项目前置 |
| **Nexis 强调点** | AI 安全网关、Prompt Injection、SSE/NDJSON 流式审核 | Rust/Pingora 高性能异步网关、QPS +138% / RT -63% |
| **nginx_merry 强调点** | API 安全网关、WAF、数据脱敏、审计 | C++ Nginx 高性能模块、进程间通信、热更新 |
| **r_data_service 强调点** | 数据安全引擎、敏感数据识别、脱敏水印 | Rust 多形态服务引擎、性能优化、JNI/SDK |
| **玩物得志风控强调点** | 业务风控、反欺诈、异常行为检测 | 高并发实时决策系统、10w+ QPS、<50ms |
| **蘑菇街 IM 强调点** | 长连接安全、IM 系统稳定性 | C++ 高性能长连接 SDK、亿级消息峰值 |
| **蘑菇街 WAF 强调点** | Web 应用安全、规则引擎 | Go 高性能网关、自研 tcpstream、20K+ QPS |
| **早期经历强调点** | 电信级安全接入、国家级平台高可靠 | 高性能长连接、分布式车联网、十万级并发 |

---

## 四、ATS 关键词策略

### 4.1 Resume A 关键词矩阵

| 位置 | 关键词 |
|------|--------|
| **Summary** | Application Security Engineer、Enterprise Security、AI Security、API Security、Security Platform、SDL、Risk Control |
| **Core Skills** | WAF、Data Masking、Watermark、Prompt Injection、Threat Detection、Anomaly Detection、Security Compliance、MLPS |
| **最近公司项目** | AI Gateway、SSE/NDJSON、Content Moderation、Data Security Engine、Sensitive Data Recognition、Risk Engine、Anti-fraud、Anti-spam、HIDS、Vulnerability Scanning |
| **技术栈** | Rust、Go、C++、Nginx、Pingora、Tokio、Kafka、Redis、ZooKeeper |

### 4.2 Resume B 关键词矩阵

| 位置 | 关键词 |
|------|--------|
| **Summary** | Senior Backend Engineer、Infrastructure Engineer、High Performance、Distributed Systems、Gateway、IM、Rust、Go |
| **Core Skills** | Gateway、Long Connection、epoll、TCP/IP、Microservices、Concurrency、Distributed Systems、Performance Optimization |
| **最近公司项目** | Pingora、Async Gateway、QPS、Latency、Nginx C Module、Cross-platform SDK、Message Bus、Consistent Hashing、Service Discovery |
| **技术栈** | Rust、Go、C++、Tokio、Nginx、Kafka、Redis、ZooKeeper、Docker |

### 4.3 关键词密度

- Summary：每个核心关键词出现 1 次。
- Core Skills：每个核心关键词明确列出 1 次。
- 最近 1-2 家公司：每个核心关键词在自然语境中出现 1–2 次。
- 早期经历：不强制铺关键词。

---

## 五、每家公司叙事角度对照

| 公司 | Resume A 叙事 | Resume B 叙事 |
|------|---------------|---------------|
| **闪捷** | 企业级安全平台产品化：AI 安全网关 + API 安全网关 + 数据安全引擎 | 高性能基础设施产品化：Rust/Pingora 网关 + C++ Nginx 模块 + Rust 多形态服务引擎 |
| **玩物得志** | 业务安全平台建设：风控 + 反垃圾 + 安全治理与合规 | 高并发后端平台建设：实时决策系统 + 高性能文本处理 + 0→1 平台建设 |
| **蘑菇街** | 企业安全与 IM 安全：WAF + 安全治理 + 长连接安全 | 高性能基础设施：IM 长连接 SDK + WAF 网关工程化 |
| **千方/中交兴路** | 车联网安全接入与高可靠平台 | 分布式车联网接入与高性能长连接 |
| **华为** | 电信级安全工程纪律奠基 | 电信级高可靠系统开发奠基 |

---

## 六、项目包含/排除/合并决策

### Resume A

| 项目 | 决策 | 说明 |
|------|------|------|
| Nexis | ✅ 保留，重点 | AI 安全网关 |
| nginx_merry | ✅ 保留，重点 | API 安全网关 |
| r_data_service | ✅ 保留，重点 | 数据安全引擎 |
| 业务风控引擎 | ✅ 保留，重点 | 业务安全 |
| 文本反垃圾系统 | ✅ 保留，中等 | 内容安全 |
| 企业安全治理 | ✅ 保留，中等 | 安全治理与合规 |
| 蘑菇街 IM | ✅ 保留，简要 | 长连接安全基础 |
| 蘑菇街 WAF | ✅ 保留，中等 | Web 应用安全 |
| 蘑菇街信息安全治理 | ✅ 补充/保留，简要 | HIDS / 漏洞扫描 |
| CADN | ✅ 保留，简要 | 车联网安全接入 |
| 华为 VFM | ✅ 保留，一句 | 工程纪律奠基 |
| flint-ocr / file-inspector | ⚠️ 合并提及 | 在 r_data_service 或 Nexis 中用一个 bullet 提及 |
| secagent | ⚠️ 可选 | 可并入 nginx_merry/Nexis 作为集群部署能力 |
| AI-dataset / AI 研究 | ⚠️ 可选 | 可并入 Nexis 作为 AI 安全能力建设 |

### Resume B

| 项目 | 决策 | 说明 |
|------|------|------|
| Nexis | ✅ 保留，重点 | Rust/Pingora 高性能网关 |
| nginx_merry | ✅ 保留，重点 | C++ Nginx 高性能模块 |
| r_data_service | ✅ 保留，重点 | Rust 多形态服务引擎 |
| 业务风控引擎 | ✅ 保留，中等 | 高并发实时决策系统 |
| 文本反垃圾系统 | ⚠️ 可选/简要 | 高性能文本处理 |
| 企业安全治理 | ⚠️ 可选/删除 | 安全治理对 Backend 叙事贡献低 |
| 蘑菇街 IM | ✅ 保留，详细 | C++ 长连接基础设施 |
| 蘑菇街 WAF | ✅ 保留，中等 | Go 高性能网关 |
| 蘑菇街信息安全治理 | ❌ 删除或一句 | Backend Resume 不需要 |
| CADN | ✅ 保留，简要 | 分布式车联网平台 |
| 华为 VFM | ✅ 保留，一句 | 工程纪律奠基 |
| flint-ocr / file-inspector | ⚠️ 合并提及 | 在 r_data_service 中提及 OCR/文件解析能力 |
| secagent | ⚠️ 可选 | 可并入 nginx_merry/Nexis |
| AI-dataset / AI 研究 | ⚠️ 可选 | 可并入 Nexis |

---

## 七、需要删除或弱化的内容

### 两份简历都要删除/弱化

- 「热爱技术、积极乐观、自我驱动力强、乐于挑战新事物」等软技能描述。
- Core Skills 中的「Claude Code / windsurf / VIM / Git / CET-6」。
- 项目中的 Why / How / Trade-off / 实现细节。
- 产品说明书式功能列表。
- 过度详细的早期经历（千方、华为）。

### Resume A 要弱化

- IM 项目中的纯性能描述，改为长连接安全/稳定性角度。
- Backend 通用技术栈的罗列，改为安全场景下的应用。

### Resume B 要弱化

- 安全合规、等保、风控规则等偏安全运营的描述。
- WAF 规则引擎细节，改为网关性能与架构。
- 数据安全业务语义，改为服务化引擎与性能。

---

## 八、信息预算分配建议

### Resume A

| 模块 | 预算 |
|------|------|
| Summary | 4–6 句 |
| Core Skills | 4–5 项，每项 2–3 行 |
| 闪捷 | 8–12 个 bullet |
| 玩物得志 | 6–9 个 bullet |
| 蘑菇街 | 4–7 个 bullet |
| 千方/中交兴路 | 2–3 个 bullet |
| 华为 | 1–2 个 bullet |
| 教育/其他 | 2–4 行 |

### Resume B

| 模块 | 预算 |
|------|------|
| Summary | 4–6 句 |
| Core Skills | 4–5 项，每项 2–3 行 |
| 闪捷 | 8–12 个 bullet |
| 蘑菇街 | 6–9 个 bullet（IM 项目更详细） |
| 玩物得志 | 4–7 个 bullet |
| 千方/中交兴路 | 2–3 个 bullet |
| 华为 | 1–2 个 bullet |
| 教育/其他 | 2–4 行 |

---

## 九、Phase 3 预告

Phase 3 将输出两份简历的完整目录结构：

```yaml
data/resume-security.yaml:
  profile
  summary
  core_skills
  experience:
    - 闪捷:
        - Nexis
        - nginx_merry
        - r_data_service
        - flint-ocr/file-inspector (合并提及)
    - 玩物得志:
        - 业务风控引擎
        - 文本反垃圾系统
        - 企业级安全治理
    - 蘑菇街:
        - WAF 网关
        - 企业级信息安全治理
        - 自研 IM
    - 千方/中交兴路:
        - CADN 车联网平台
    - 华为:
        - VFM 模块
  education

data/resume-backend.yaml:
  profile
  summary
  core_skills
  experience:
    - 闪捷:
        - Nexis
        - nginx_merry
        - r_data_service
        - flint-ocr/file-inspector (合并提及)
    - 蘑菇街:
        - 自研 IM
        - WAF 网关
    - 玩物得志:
        - 业务风控引擎
        - 文本反垃圾系统
    - 千方/中交兴路:
        - CADN 车联网平台
    - 华为:
        - VFM 模块
  education
```

---

## 十、待 Phase 3 确认的问题

1. **闪捷 secagent / AI-dataset / AI 研究**：
   - Resume A 是否完全不提，还是作为 Nexis / r_data_service 的配套能力一句话带过？
   - Resume B 是否完全不提？
2. **玩物得志企业级安全治理** 在 Resume B 中是否保留一句话，还是完全删除？
3. **蘑菇街信息安全治理** 在 Resume A 中的详细程度：是 1 个 bullet 还是 2 个 bullet？
4. **flint-ocr / file-inspector 合并位置**：放在 r_data_service 下更合适，还是放在 Nexis 下更合适？
   - r_data_service：数据安全引擎的 OCR/文件识别能力延伸。
   - Nexis：AI 安全网关的文件/图片内容检测能力。

确认后进入 Phase 3。
