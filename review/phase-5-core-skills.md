# Phase 5 — Resume A/B Core Skills 设计

## 重要 redesign 说明

Core Skills v1 的问题：把 Core Skills 写成了「缩短版项目经历」，包含大量项目细节（Prompt Injection、SSE/NDJSON、亿级消息、10w+ QPS）和成果性描述（0→1、生产环境落地）。

**Core Skills 的真正作用**：让技术总监在 5 秒内扫一眼，建立技术画像。

因此 v2 完全推倒重做：

- 只保留**技术域关键词和技术名词**，不写完整叙述句。
- 每个能力域控制在 **4–8 个关键词**。
- 项目成果、业务背景、性能数字、0→1 等全部移到 Project Experience。
- Summary、Core Skills、Project Experience 三者职责严格分离，避免重复。
- 优先服务国内技术总监阅读习惯，而非 ATS 堆砌。

---

## Resume A — Application Security Engineer

### Core Skills v2

```yaml
core_skills:
  - title: Application Security
    details:
      - AI Security
      - API Security
      - WAF
      - Content Security
      - Risk Control
      - Data Security
      - DLP

  - title: Security Engineering
    details:
      - SDL
      - Code Audit
      - Vulnerability Management
      - Security Governance
      - Compliance
      - HIDS

  - title: Security Products
    details:
      - AI Gateway
      - Data Security Engine
      - Anti-fraud
      - Anti-spam
      - Identity & Access

  - title: Programming Languages
    details:
      - Rust
      - Go
      - C++

  - title: Infrastructure
    details:
      - Nginx
      - Pingora
      - Linux
      - TCP/IP
      - Kafka
      - Redis
```

### 设计说明

| 能力域 | 关键词 | 说明 |
|--------|--------|------|
| Application Security | AI Security, API Security, WAF, Content Security, Risk Control, Data Security, DLP | 安全能力域广度，覆盖 Resume A 的核心方向。 |
| Security Engineering | SDL, Code Audit, Vulnerability Management, Security Governance, Compliance, HIDS | 安全工程与体系建设能力，区分于纯安全开发。 |
| Security Products | AI Gateway, Data Security Engine, Anti-fraud, Anti-spam, Identity & Access | 产品形态，帮助建立"安全产品研发"人设。 |
| Programming Languages | Rust, Go, C++ | 核心语言栈，不写"熟悉""具备"等废话。 |
| Infrastructure | Nginx, Pingora, Linux, TCP/IP, Kafka, Redis | 技术基础设施，支撑安全产品的工程底座。 |

### 删除说明

- **删除 CISSP**：资质放到 Education / Certification 区域。
- **删除 Prompt Injection / SSE / NDJSON / 零宽字符 / SIM 水印 / OCR**：项目实现细节，下放项目。
- **删除 0→1 / 规模化落地 / 金融政务互联网**：项目成果与行业背景，下放项目。

---

## Resume B — Senior Backend Engineer

### Core Skills v2

```yaml
core_skills:
  - title: Backend Development
    details:
      - High Performance
      - Gateway
      - Long Connection
      - IM System
      - Distributed Systems
      - Low Latency

  - title: Programming Languages
    details:
      - Rust
      - Go
      - C++
      - Linux

  - title: Gateway & Networking
    details:
      - Nginx
      - Pingora
      - Reverse Proxy
      - TCP/IP
      - HTTP/HTTPS
      - WebSocket

  - title: Concurrency
    details:
      - epoll
      - kqueue
      - Async
      - Lock-free
      - High Concurrency

  - title: Middleware
    details:
      - Redis
      - Kafka
      - ZooKeeper
      - MySQL
      - ClickHouse
```

### 设计说明

| 能力域 | 关键词 | 说明 |
|--------|--------|------|
| Backend Development | High Performance, Gateway, Long Connection, IM System, Distributed Systems, Low Latency | 核心后端技术画像，区别于 Resume A 的安全方向。 |
| Programming Languages | Rust, Go, C++, Linux | 多语言系统编程能力。 |
| Gateway & Networking | Nginx, Pingora, Reverse Proxy, TCP/IP, HTTP/HTTPS, WebSocket | 网关与网络协议栈。 |
| Concurrency | epoll, kqueue, Async, Lock-free, High Concurrency | 并发与高性能编程。 |
| Middleware | Redis, Kafka, ZooKeeper, MySQL, ClickHouse | 常用基础设施组件。 |

### 删除说明

- **删除 亿级消息峰值 / 10w+ QPS / <50ms**：项目成果数字，下放项目。
- **删除 0→1 / 生产环境 / 电信级高可靠**：项目经验描述，下放项目。
- **删除 Java SDK / JNI**：具体技术实现，下放项目。

---

## Resume A/B Core Skills 对比

| 维度 | Resume A | Resume B |
|------|---------|---------|
| 第一项 | Application Security | Backend Development |
| 第二项 | Security Engineering | Programming Languages |
| 第三项 | Security Products | Gateway & Networking |
| 第四项 | Programming Languages | Concurrency |
| 第五项 | Infrastructure | Middleware |
| 共同语言栈 | Rust, Go, C++ | Rust, Go, C++ |
| 核心差异 | 安全域关键词 | 后端/网关/并发关键词 |

---

## 与 Summary / Project Experience 的职责分离

| 模块 | 职责 | 当前 Core Skills 是否越界 |
|------|------|--------------------------|
| Summary | 建立技术人设 | 否 |
| Core Skills | 建立技术画像（关键词扫描） | v1 越界，v2 已修正 |
| Project Experience | 证明能力（What / Contribution / Impact） | Core Skills 不应承载 |

---

## 设计原则总结

1. **名词 > 句子**：只写技术名词和领域词，不写"熟悉""具备""主导"等动词句。
2. **4–8 个关键词/域**：方便 5 秒内扫完。
3. **不重复项目内容**：项目细节、成果、数字全部下放 Project Experience。
4. **不重复 Summary**：Summary 说"我是谁"，Core Skills 说"我掌握哪些技术域"。
5. **国内阅读优先**：服务技术总监快速扫描，而非 ATS 关键词堆砌。

---

## 待确认问题

1. Resume A 的 5 个能力域分类是否清晰？是否需要合并 Application Security 与 Security Products？
2. Resume B 是否需要增加「Performance Optimization」或「System Design」独立域？
3. 是否需要为某些关键词加简短说明（如 Pingora），还是保持纯名词？
4. 两个 Branch 的能力域数量是否统一（当前都是 5 项）？
5. 是否有遗漏的关键技术域？

确认后，用 v2 替换之前所有 Core Skills 引用，并继续项目经历优化。
