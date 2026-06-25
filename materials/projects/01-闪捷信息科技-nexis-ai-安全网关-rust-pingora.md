Nexis — 企业级 AI 安全网关 (Rust/Pingora)

公司: 闪捷信息科技有限公司 | 时间: 2022.04-至今 | 角色: 高级研发工程师 / 技术负责人
技术栈: Rust · Pingora · Tokio · ZooKeeper · SSE · NDJSON · AI Gateway

【项目简介】
基于 Cloudflare Pingora 框架自研的企业级 AI 安全网关，替代原有 C++ Nginx 模块方案。定位为 AI Gateway + 安全网关一体化平台，支持多模型体系（Dify / OpenAI / Anthropic / Ollama）代理及全面安全防护能力，服务金融、政企客户，已持续稳定运行超 2 年。

【核心职责】
- 主导从 C++ Nginx 模块到 Rust Pingora 异步网关的完整架构迁移
- 设计六层插件化架构（Core→Gateway→Platform→Proxy→Service→Support），实现安全策略动态编排与 ZK 热更新
- 完成全链路 async trait 异步化改造，承担异步 proxy 层与安全策略引擎核心模块编码
- 设计 AI 网关统一代理层，实现 Prompt 注入检测、SSE/NDJSON 流式逐 chunk 内容审核与脱敏代答

【技术亮点】
- 六层插件化架构：每层职责清晰、接口稳定，新增产品形态只需实现 Gateway trait，安全策略在 Service 层统一复用
- 三阶段处理链：请求阶段 → 响应头阶段 → 响应体阶段，覆盖账号发现、黑白名单、访问控制、数据脱敏、水印、AI 检查等完整策略
- AI Gateway 路由分层：L0 协议入口 → L1 静态路由 → L2 动态路由 → L3 协议决策 → L4 协议转换（OpenAI ↔ Anthropic）→ L5 上游转发
- 零拷贝 JSON 解析器：利用 bytes::Bytes 零拷贝特性，直接在 HTTP body 字节切片上做字段提取和正则匹配，避免完整解析的内存分配开销

【性能成果】
- QPS 较 C++ 版本提升 138%（24,270 vs 10,189），平均延迟降低 63%（32.70ms vs 88.31ms）
- 纯代理模式 QPS 15w/s，开启全量安全规则（80+ 敏感数据检测 + WAF 规则链）QPS 10w+

【业务成果】
- 支撑千万级项目 POC 与交付，服务金融、政企客户
- 搭建 macOS → Linux 交叉编译与多环境自动部署流水线
- 网关平台已持续稳定运行超 2 年

---
基于 nexis 项目文档整理。运行 make materials 重新生成。
