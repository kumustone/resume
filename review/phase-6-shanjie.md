# Phase 6 — 闪捷（Shanjie）YAML 草稿

## 说明

- 本文件为 Phase 6 第一家公司（闪捷）的 YAML 草稿。
- 包含 Resume A（Security）与 Resume B（Backend）的闪捷经历。
- 同一段经历，两种叙事角度。
- 待用户确认后，写入 `data/resume-security.yaml` 与 `data/resume-backend.yaml`。

---

## Resume A — Application Security Engineer

```yaml
experience:
  - company: 闪捷信息科技有限公司
    role: 资深开发工程师 / 技术负责人
    period: 2022.04-至今
    summary: 负责 AI 安全网关、API 安全网关与数据安全引擎的核心设计与开发，服务金融、政务、互联网等行业客户。
    projects:
      - name: 企业级 AI 安全网关
        tech: [Rust, Pingora, Tokio, ZooKeeper, SSE, NDJSON, AI Gateway]
        highlights:
          - 基于 Cloudflare Pingora 自研企业级 AI 安全网关，较原 C++ Nginx 模块方案 QPS +138%，RT -63%。
          - 设计 AI 请求统一代理层，实现 Prompt Injection 检测、SSE/NDJSON 流式逐 chunk 内容审核与敏感数据脱敏代答。
          - 构建六层插件化架构与 ZooKeeper 热更新机制，支撑金融、政务等客户的多模型体系代理安全。
          - 完成 AI 网关市场竞品分析、PRD 与架构设计，支撑产品化方向决策。

      - name: 企业级 API 安全网关
        tech: [C++, Nginx C Module, dlopen, ZooKeeper, Kafka, Redis, WAF, Data Masking, Watermark]
        highlights:
          - 设计并实现基于 Nginx C Module + C++ 动态库的企业级 API 安全网关，实现 WAF、数据脱敏、7 种水印、访问控制与审计追溯。
          - 采用 dlopen/dlsym 实现业务逻辑热更新，Fail-open 设计保障客户现场业务连续性，产品已在金融、政务等行业客户稳定运行超 2 年。
          - 通过 Kafka → ClickHouse 构建请求全生命周期审计链路，支撑账号发现、日志采集与风险分析。
          - 设计 secagent 分布式节点管理器，为 nginx_merry 集群提供配置同步、状态上报与服务升级能力。

      - name: 多形态数据安全引擎
        tech: [Rust, JNI, Regex, Trie, Watermark, Data Masking, OCR, Java SDK]
        highlights:
          - 设计 Segment→Recognize→Mask 三阶段流水线，支撑 Rust 库、Java SDK、HTTP Server、Web 管理端四种服务形态。
          - 完成核心引擎 Rust 化代际升级，核心识别与脱敏能力性能提升 5x+，覆盖 80+ 敏感数据类型与 20+ 脱敏算法。
          - 集成 OCR 与文件敏感检测能力，支持图片、PDF、Office 文档等多格式文件的内容识别与涉密信息检测。
```

---

## Resume B — Senior Backend Engineer

```yaml
experience:
  - company: 闪捷信息科技有限公司
    role: 资深开发工程师 / 技术负责人
    period: 2022.04-至今
    summary: 负责高性能 AI 网关、API 网关与数据服务引擎的核心设计与开发，支撑金融、政务、互联网等行业客户。
    projects:
      - name: 企业级 AI 网关
        tech: [Rust, Pingora, Tokio, ZooKeeper, SSE, NDJSON, AI Gateway]
        highlights:
          - 基于 Rust/Pingora 自研企业级 AI 网关，较原 C++ Nginx 模块方案 QPS +138%，RT -63%。
          - 纯代理模式 QPS 15w/s，开启全量安全规则 QPS 10w+，支撑千万级项目 POC 与交付。
          - 设计六层插件化架构与全链路 async trait 异步化改造，实现 ZooKeeper 热更新与多模型体系代理。

      - name: 高性能 API 网关
        tech: [C++, Nginx C Module, dlopen, ZooKeeper, Kafka, Redis]
        highlights:
          - 设计基于 Nginx C Module + C++ 动态库分离架构的高性能网关，通过 dlopen/dlsym 实现业务逻辑热更新。
          - Fail-open 设计保障客户现场业务连续性，产品已在金融、政务等行业客户稳定运行超 2 年。
          - 实现请求全生命周期处理链，涵盖网络层、应用层与审计层，支撑高并发无感代理。

      - name: 多形态数据服务引擎
        tech: [Rust, JNI, Regex, Trie, Java SDK, HTTP Server]
        highlights:
          - 设计多 crate 架构（无状态引擎层 + 有状态编排层），支撑 Rust 库、Java SDK、HTTP Server、Web 管理端四种形态。
          - 完成核心引擎 Rust 化代际升级，核心识别与脱敏能力性能提升 5x+，Java SDK 替代 TLV 字符串协议。
          - 集成 OCR/文件解析能力，支持图片、PDF、Office 文档等多格式文件的内容识别与服务化检测。
```

---

## 关键差异对照

| 维度 | Resume A | Resume B |
|------|---------|---------|
| 公司定位 | AI 安全网关、API 安全网关、数据安全引擎 | 高性能 AI 网关、API 网关、数据服务引擎 |
| Nexis 强调 | Prompt Injection、SSE/NDJSON 审核、脱敏代答、AI 预研 | QPS +138%、RT -63%、15w/s QPS、async trait |
| nginx_merry 强调 | WAF、数据脱敏、7 种水印、审计追溯、secagent 节点管理 | 高性能网关、热更新、Fail-open、无感代理 |
| r_data_service 强调 | 敏感数据识别、脱敏、水印、OCR/文件检测 | 多 crate 架构、Java SDK、性能提升 5x+ |
| 独立项目 | 无 | 无 |

---

## 已确认

1. ✅ secagent 放在 nginx_merry 下合适。
2. ✅ Resume B 不需要提及 secagent。
3. ✅ Resume B 中 r_data_service 的「OCR/文件解析」保留。
4. ⏸️ 暂停进入下一阶段，等待用户下一步指令。

## 待写入正式 YAML

确认后，将闪捷部分写入 `data/resume-security.yaml` 与 `data/resume-backend.yaml`。
