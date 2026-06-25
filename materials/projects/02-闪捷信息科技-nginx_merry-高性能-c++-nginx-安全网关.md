nginx_merry — 高性能 C++ Nginx 安全网关模块

公司: 闪捷信息科技有限公司 | 时间: 2022.04-至今 | 角色: 高级研发工程师 / 技术负责人
技术栈: C++ · C · Nginx C Module · dlopen · ZooKeeper · Kafka · Redis · WAF

【项目简介】
自研企业级安全网关模块，基于 Nginx C 模块 + C++ 动态库分离架构，提供 WAF、数据脱敏、水印、访问控制、AI 内容安全检测等企业级安全能力。作为 Nexis（Rust/Pingora）的前身，其 Handler 插件链 + 三阶段分派 + 统一处置结果的架构模式在后续 Rust 网关中完整延续复用。

【核心职责】
- 设计 C + C++ 分离架构，通过 dlopen/dlsym 实现业务逻辑热更新，无需重启 nginx
- 设计 Handler 链式调用架构与三阶段处理模型（请求 / 响应头 / 响应体）
- 实现 11 个可插拔安全策略模块（黑白名单、访问控制、风险防护、脱敏、水印、账号发现、AI 检测等）
- 编写核心架构文档与开发规范

【技术亮点】
- C + C++ 分离架构：Nginx 模块层用 C 保持原生性能，C++ 业务库通过 dlopen 动态加载，支持单独更新 libmerry.so 不重启 nginx
- Handler 插件链：所有安全策略继承 MerryHandler 统一接口，通过单例模式管理，支持链式调用和中断
- 三阶段分派：请求阶段（NGX_HTTP_ACCESS_PHASE）→ 响应头阶段（header filter）→ 响应体阶段（body filter），覆盖完整请求生命周期
- 跨阶段数据传递：通过 ngx_str_t + JSON 在 nginx pool 中存储，解决 C/C++ 跨阶段数据共享问题
- 响应体完整缓冲：必须缓冲完整响应体后才能进行敏感信息检测、脱敏/水印处理、gzip 解压，通过 last_buf 触发机制确保处理完整性

【性能成果】
- 作为 Nexis 的性能对比基线，后续 Rust/Pingora 版本较此项目 QPS +138%，RT -63%
- 集成 ZooKeeper 动态配置、Kafka 审计日志、Redis 缓存，支撑完整安全运营闭环
- Fail-open 设计：业务库加载失败时请求直通，不影响 nginx 转发
- AI 快速路径：AI 聊天消息无策略时直接放行，减少性能损耗

【业务成果】
- 架构模式（Handler 插件链 / 三阶段分派 / 统一处置结果）在后续 Rust/Pingora 网关中完整延续复用
- 支撑企业级安全网关产品从 0 到 1 建设，验证核心架构可行性
- 为后续技术栈迁移（C++ → Rust）提供明确的性能基准与架构参照

---
基于 nginx_merry 项目文档整理。运行 make materials 重新生成。
