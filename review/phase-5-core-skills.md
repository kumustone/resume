# Phase 5 — Resume A/B Core Skills 设计

## 设计原则

- 4–5 个能力域，每个能力域 2–3 行。
- 每行包含 1–2 个 ATS 关键词。
- 不写低价值工具（VIM / Git / CET-6 / Claude Code）。
- Resume A 安全能力域前置，Resume B 系统研发能力域前置。
- 避免与 Summary 逐字重复，但关键词可呼应。

---

## Resume A — Application Security Engineer

### Core Skills v1

```yaml
core_skills:
  - title: AI / API 安全网关
    details:
      - 企业级 AI 安全网关设计，覆盖 Prompt Injection 检测、SSE/NDJSON 流式内容审核、AI 应答脱敏代答。
      - API 安全网关开发，具备 WAF、访问控制、数据脱敏、数字水印、请求审计与风险追溯能力。

  - title: 数据安全与合规
    details:
      - 数据安全引擎设计，支持敏感数据识别、数据脱敏、零宽字符/SIM 水印、OCR/文件敏感检测。
      - 企业安全治理与等保合规建设，覆盖 SDL、DevSecOps、漏洞管理、HIDS、安全审计。

  - title: 业务风控与内容安全
    details:
      - 实时业务风控引擎，覆盖反欺诈、反洗钱、异常行为检测、设备指纹与规则策略编排。
      - 高性能文本反垃圾系统，基于 DFA/正则/自定义规则，覆盖 IM、评论、社区等多业务场景。

  - title: 安全工程化基础
    details:
      - 熟悉 Rust / Go / C++ 安全产品开发，具备 Nginx/Pingora 网关、Kafka、Redis、ZooKeeper 工程经验。
      - 主导多个 0→1 安全产品建设，具备金融、政务、互联网行业客户现场落地与规模化交付能力。
```

### 设计说明

| 能力域 | ATS 关键词 |
|--------|-----------|
| AI / API 安全网关 | AI Security、API Security、WAF、Prompt Injection、Content Moderation、Data Masking |
| 数据安全与合规 | Data Security、Data Masking、Watermark、DLP、SDL、DevSecOps、MLPS、HIDS |
| 业务风控与内容安全 | Risk Control、Anti-fraud、Anti-spam、Anomaly Detection、Device Fingerprint |
| 安全工程化基础 | Rust、Go、C++、Nginx、Pingora、0→1、Enterprise Security |

---

## Resume B — Senior Backend Engineer

### Core Skills v1

```yaml
core_skills:
  - title: 高性能网关
    details:
      - 基于 Rust/Pingora 的异步高性能网关开发，具备插件化架构、热更新与全链路 async 改造经验。
      - 基于 Nginx C Module + C++ 动态库的高性能代理开发，熟悉请求生命周期处理与进程间通信优化。

  - title: 长连接与 IM 基础设施
    details:
      - C++ 跨平台长连接 SDK 开发，基于 epoll/kqueue 实现异步非阻塞 I/O，支撑亿级消息峰值。
      - IM 系统全流程设计，覆盖接入服务器、登录鉴权、会话管理、长链推送与 AppServer 模块。

  - title: 分布式系统
    details:
      - 分布式接入平台设计，覆盖服务发现、一致性哈希、消息总线、负载均衡与无共享状态集群。
      - 高并发实时决策系统开发，支撑 10w+ QPS，平均决策延迟 <50ms。

  - title: 系统编程与工程化
    details:
      - 熟悉 Rust / Go / C++ 系统编程，具备 JNI、多平台 SDK、交叉编译与多环境部署经验。
      - 主导多个 0→1 系统建设，具备电信级高可靠系统开发背景与大规模生产环境运维能力。
```

### 设计说明

| 能力域 | ATS 关键词 |
|--------|-----------|
| 高性能网关 | High Performance Gateway、Rust、Pingora、Nginx、C++、Async、Hot Reload |
| 长连接与 IM 基础设施 | Long Connection、IM、epoll、kqueue、Cross-platform SDK、Message Peak |
| 分布式系统 | Distributed Systems、Service Discovery、Consistent Hashing、Message Bus、High Concurrency |
| 系统编程与工程化 | Rust、Go、C++、JNI、SDK、System Programming、0→1、Telecom-grade |

---

## Resume A/B Core Skills 对比

| 维度 | Resume A | Resume B |
|------|---------|---------|
| 第一项 | AI / API 安全网关 | 高性能网关 |
| 第二项 | 数据安全与合规 | 长连接与 IM 基础设施 |
| 第三项 | 业务风控与内容安全 | 分布式系统 |
| 第四项 | 安全工程化基础 | 系统编程与工程化 |
| 共同技术栈 | Rust / Go / C++、Nginx/Pingora | Rust / Go / C++、Nginx/Pingora |
| 差异关键词 | WAF、DLP、SDL、HIDS、Risk、Compliance | epoll、kqueue、IM、Distributed、Performance |

---

## 与 Summary 的呼应

### Resume A

- Summary 提到「企业安全平台建设与 AI 安全基础设施」→ Core Skills 展开为 AI/API 安全网关、数据安全、风控内容安全。
- Summary 提到「金融、政务、互联网」→ Core Skills 第四项补充行业落地能力。
- Summary 提到「持有 CISSP」→ Core Skills 数据安全与合规项呼应。

### Resume B

- Summary 提到「高性能网络服务与分布式基础设施」→ Core Skills 展开为高性能网关、长连接 IM、分布式系统。
- Summary 提到「QPS +138%、RT -63%」→ Core Skills 高性能网关项呼应。
- Summary 提到「C++ / Go / Rust 多语言」→ Core Skills 系统编程项呼应。

---

## 待确认问题

1. Core Skills 是否需要加入「团队管理 / Team Lead」项？
2. Resume A 是否需要单独的「安全合规」项（当前并入数据安全与合规）？
3. Resume B 是否需要加入「性能优化 / Performance Tuning」独立项？
4. 是否需要为每个能力域增加「年限」信号（如 5 年网关经验）？
5. 两个 Branch 的 Core Skills 数量是否一致（当前都是 4 项）？

确认后进入 Phase 6：逐家公司/项目修改。
