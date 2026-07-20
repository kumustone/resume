# nginx_merry — 高性能 C++ Nginx 安全网关模块

## 基础事实
- 公司：闪捷信息科技有限公司
- 在职时间：2022.04-至今
- 职位：资深开发工程师 / 技术负责人
- 技术栈（从项目详情中提取，去重并规范）：C++ · C · Nginx C Module · dlopen · ZooKeeper · Kafka · Redis · WAF
- 代码仓库佐证（如适用）：`/Users/liubo/workspace/secsmart/aisg/nginx_merry`（C/C++，README: Nginx Merry 安全网关模块）

## 项目目标（一句话）
自研企业级安全网关模块，基于 Nginx C 模块 + C++ 动态库分离架构，提供 WAF、数据脱敏、水印、访问控制、AI 内容安全检测等企业级安全能力。

## 候选人贡献
- 设计 C + C++ 分离架构，通过 dlopen/dlsym 实现业务逻辑热更新，无需重启 nginx。
- 设计 Handler 链式调用架构与三阶段处理模型（请求 / 响应头 / 响应体）。
- 实现 11 个可插拔安全策略模块（黑白名单、访问控制、风险防护、脱敏、水印、账号发现、AI 检测等）。
- 集成 ZooKeeper 动态配置、Kafka 审计日志、Redis 缓存，支撑完整安全运营闭环。
- 编写核心架构文档与开发规范，其 Handler 插件链 / 三阶段分派 / 统一处置结果模式在后续 Rust/Pingora 网关中完整延续复用。

## 可量化结果/Impact
- 作为 Nexis 的性能对比基线，后续 Rust/Pingora 版本较此项目 QPS +138%，RT -63%——来源：项目详情「性能成果」。
- 11 个可插拔安全策略模块——来源：项目详情「核心职责」。
- 已持续稳定运行超 2 年（在闪捷各客户项目中）——来源：已确认事实。

## 两个 Resume Branch 的叙事角度
- Security Resume 强调点：企业级 WAF/数据安全网关、11 个安全策略模块、Handler 链式架构、三阶段分派、Kafka 审计日志。
- Backend Resume 强调点：Nginx C 模块高性能开发、C + C++ 分离架构与 dlopen 热更新、Fail-open 设计、架构模式被后续 Rust 网关复用。

## 待确认/缺失
- 具体服务客户数量/规模。
- 各安全策略模块的详细性能数据。
- nginx_merry 与 Nexis 的替代关系时间线。

## 加工备注
- 是否可直接用于简历：是（性能对比数据由 Nexis 承载，本项目作为基线/前身）。
- 敏感信息提醒：闪捷为乙方产品公司，避免将客户项目描述为公司内部系统。
