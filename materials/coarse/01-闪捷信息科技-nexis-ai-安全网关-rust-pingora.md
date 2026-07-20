# Nexis — 企业级 AI 安全网关 (Rust/Pingora)

## 基础事实
- 公司：闪捷信息科技有限公司
- 在职时间：2022.04-至今
- 职位：资深开发工程师 / 技术负责人
- 技术栈（从项目详情中提取，去重并规范）：Rust · Pingora · Tokio · ZooKeeper · SSE · NDJSON · AI Gateway
- 代码仓库佐证（如适用）：`/Users/liubo/workspace/secsmart/aisg/nexis`（Rust，README: A Nginx-like reverse proxy built on Pingora）

## 项目目标（一句话）
基于 Cloudflare Pingora 框架自研企业级 AI 安全网关，替代原有 C++ Nginx 模块方案，实现 AI Gateway 与安全网关一体化，服务金融、政企客户。

## 候选人贡献
- 主导从 C++ Nginx 模块到 Rust Pingora 异步网关的完整架构迁移。
- 设计六层插件化架构（Core→Gateway→Platform→Proxy→Service→Support），实现安全策略动态编排与 ZK 热更新。
- 完成全链路 async trait 异步化改造，承担异步 proxy 层与安全策略引擎核心模块编码。
- 设计 AI 网关统一代理层，实现 Prompt 注入检测、SSE/NDJSON 流式逐 chunk 内容审核与脱敏代答。
- 搭建 macOS → Linux 交叉编译与多环境自动部署流水线。

## 可量化结果/Impact
- QPS +138%（24,270 vs 10,189），RT -63%（32.70ms vs 88.31ms）——来源：项目详情「性能成果」。
- 纯代理模式 QPS 15w/s，开启全量安全规则（80+ 敏感数据检测 + WAF 规则链）QPS 10w+——来源：项目详情「性能成果」。
- 支撑千万级项目 POC 与交付——来源：项目详情「业务成果」。

## 两个 Resume Branch 的叙事角度
- Security Resume 强调点：AI 安全网关、Prompt 注入检测、SSE/NDJSON 流式审核、敏感数据脱敏代答、多模型体系代理安全。
- Backend Resume 强调点：Rust/Pingora 高性能异步网关、六层插件化架构、全链路 async trait、零拷贝 JSON 解析、QPS +138% / RT -63%。

## 待确认/缺失
- 千万级项目 POC 与交付的具体客户数量/规模。
- 80+ 敏感数据检测 / WAF 规则链的具体规则数量依据。
- 金融、政企客户具体名称（脱敏后是否可用）。

## 加工备注
- 是否可直接用于简历：是（需核实稳定运行年限归属）。
- 敏感信息提醒：避免暴露具体客户名称；Pingora 需在简历中加括号解释。
