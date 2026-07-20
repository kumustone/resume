# Phase 4 — Resume A/B Summary 设计

## 设计原则

- 第一句直接建立专业身份。
- 不出现软技能或性格描述。
- 每句包含 ATS 关键词或能力信号。
- 体现 Career Arc：电信级工程纪律 → 高性能基础设施 → 企业安全 / AI 基础设施。
- 不写具体客户名，只写行业领域。

---

## Resume A — Application Security Engineer

### Summary v1（已废弃）

```text
15 年系统研发经验，专注企业安全平台建设与 AI 安全基础设施，兼具高性能网关与数据安全引擎的实战背景。主导设计并落地企业级 AI 安全网关（Nexis）、API 安全网关（nginx_merry）与多形态数据安全引擎（r_data_service），服务金融、政务、互联网等行业客户。覆盖 AI 内容安全、WAF、数据脱敏、敏感数据识别、业务风控、反垃圾、等保合规等企业安全核心领域。从 0 到 1 搭建过业务风控平台、文本反垃圾系统与企业安全治理体系，具备安全产品化与规模化落地能力。持有 CISSP，职业主线从电信级高可靠系统演进至 AI 安全基础设施。
```

### Summary v2（根据反馈修订）

```text
专注企业安全平台建设与 AI 安全基础设施，兼具高性能网关与数据安全引擎的实战背景。主导设计并落地企业级 AI 安全网关、API 安全网关与多形态数据安全引擎，服务金融、政务、互联网等行业客户。覆盖 AI 内容安全、WAF、数据脱敏、敏感数据识别、业务风控、反垃圾、等保合规等企业安全核心领域。从 0 到 1 搭建过业务风控平台、文本反垃圾系统与企业安全治理体系，具备安全产品化与规模化落地能力。持有 CISSP。
```

### 设计说明

| 句子 | 功能 | ATS 关键词 / 能力信号 |
|------|------|----------------------|
| 第一句 | 建立身份：15 年 + 企业安全平台 + AI 安全基础设施 | Application Security、AI Security、Enterprise Security |
| 第二句 | 核心产品矩阵与行业覆盖 | WAF、Data Security、Gateway、金融、政务 |
| 第三句 | 安全能力域广度 | AI Content Safety、Data Masking、Sensitive Data Recognition、Risk Control、Anti-spam、Compliance |
| 第四句 | 0→1 建设与产品化能力 | 0→1、Security Platform、规模化落地 |
| 第五句 | 资质与职业主线 | CISSP、Telecom-grade、AI Security Infrastructure |

### 替代版本（更简洁）

```text
15 年系统研发经验，专注企业安全平台建设，覆盖 AI 安全网关、API 安全网关与数据安全引擎。主导 Nexis、nginx_merry、r_data_service 等核心产品，服务金融、政务、互联网行业，实现 AI 内容审核、WAF、数据脱敏、敏感数据识别与业务风控能力。具备从 0 到 1 搭建安全平台、推动等保合规与规模化落地的完整经验。持有 CISSP，职业主线从电信级高可靠系统演进至 AI 安全基础设施。
```

---

## Resume B — Senior Backend Engineer

### Summary v1（已废弃）

```text
15 年系统研发经验，专注高性能网络服务与分布式基础设施，覆盖高性能网关、长连接 IM 系统与数据服务引擎。主导基于 Rust/Pingora 的 AI 网关、基于 Nginx C Module 的高性能 API 网关与 Rust 多形态数据服务引擎，实现 QPS +138%、RT -63% 等关键性能提升。具备 C++ / Go / Rust 多语言工程化能力，主导过 0→1 系统建设、大规模生产环境落地与团队技术管理。职业主线从电信级高可靠系统演进至高并发网关、分布式后端与 AI 基础设施。
```

### Summary v2（根据反馈修订）

```text
专注高性能网络服务与分布式基础设施，覆盖高性能网关、长连接 IM 系统与数据服务引擎。主导基于 Rust/Pingora 的 AI 网关、基于 Nginx C Module 的高性能 API 网关与 Rust 多形态数据服务引擎，实现 QPS +138%、RT -63% 等关键性能提升。具备 C++ / Go / Rust 多语言工程化能力，主导过 0→1 系统建设、大规模生产环境落地与团队技术管理。
```

### 设计说明

| 句子 | 功能 | ATS 关键词 / 能力信号 |
|------|------|----------------------|
| 第一句 | 建立身份：15 年 + 高性能网络服务 + 分布式基础设施 | Senior Backend、Infrastructure、High Performance、Distributed Systems |
| 第二句 | 核心产品矩阵与性能成果 | Rust、Pingora、Nginx、Gateway、QPS、Latency、Data Service Engine |
| 第三句 | 多语言能力与工程领导力 | C++、Go、Rust、0→1、Production、Team Lead |
| 第四句 | 职业主线 | Telecom-grade、Gateway、Distributed Backend、AI Infrastructure |

### 替代版本（更突出 Gateway）

```text
15 年系统研发经验，专注高性能网关、长连接基础设施与分布式系统。主导基于 Rust/Pingora 的企业级 AI 网关与基于 Nginx C Module 的高性能 API 网关，实现 QPS +138%、RT -63%；设计 C++ 跨平台长连接 SDK 支撑亿级消息峰值。具备 C++ / Go / Rust 多语言工程化与 0→1 系统建设能力，服务金融、政务、互联网行业。职业主线从电信级高可靠系统演进至高并发网关与 AI 基础设施。
```

---

## 对比分析（基于 v2）

| 维度 | Resume A Summary | Resume B Summary |
|------|------------------|------------------|
| 第一句话核心 | 企业安全平台 + AI 安全基础设施 | 高性能网络服务 + 分布式基础设施 |
| 核心产品 | AI 安全网关、API 安全网关、数据安全引擎 | Rust/Pingora AI 网关、Nginx C Module API 网关、Rust 数据服务引擎 |
| 强调能力 | 安全能力域广度、合规、风控 | 性能、并发、架构、多语言 |
| 行业覆盖 | 金融、政务、互联网 | 金融、政务、互联网 |
| 资质 | CISSP | 无（Backend 不需要强调安全资质） |
| 内部项目名 | 不出现 Nexis / nginx_merry | 不出现具体产品名 |
| 职业主线表述 | 不出现 | 不出现 |

---

## 用户反馈与修订记录

1. **去掉「15 年系统研发经验」**：v2 已删除该开头。
2. **去掉内部项目名 Nexis / nginx_merry**：v2 不再在 Summary 中写括号内代码名。
3. **去掉「职业主线从……演进至……」**：v2 已删除该 AI 味过重的表达。
4. **开源项目不提**：Core Skills 与 Summary 均不提 go-fast-waf / tcpstream。

---

## 确认结论

- Resume A 采用 **Summary v2**。
- Resume B 采用 **Summary v2**。
- 进入 Phase 5：Core Skills 设计。
