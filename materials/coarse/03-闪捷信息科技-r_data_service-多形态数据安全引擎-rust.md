# r_data_service — 多形态数据安全引擎 (Rust)

## 基础事实
- 公司：闪捷信息科技有限公司
- 在职时间：2022.04-至今
- 职位：资深开发工程师 / 技术负责人
- 技术栈（从项目详情中提取，去重并规范）：Rust · JNI · Regex · Trie · Watermark · Data Masking · Java SDK · Axum
- 代码仓库佐证（如适用）：`/Users/liubo/workspace/secsmart/aisg/r_data_service`（Rust，README: 数据脱敏、水印服务，支持 Rust 库和 Java JNI 绑定）

## 项目目标（一句话）
自研多形态数据安全服务引擎，提供数据脱敏、数字水印、敏感数据识别、数据泄露检测等核心能力，同一套引擎代码支撑 Rust 库、Java SDK、HTTP Server、Web 管理端四种服务形态。

## 候选人贡献
- 主导 Workspace 多 crate 架构设计（rds-infra 无状态引擎层 + rds-runtime 有状态编排层 + rds-jni JNI 绑定层）。
- 设计 Segment → Recognize → Mask 三阶段流水线，承担识别与脱敏核心模块编码。
- 推动 Java SDK 强类型 API 替代旧版 TLV 字符串协议，实现多平台动态库自动加载。
- 实现 80+ 敏感数据类型识别与 20+ 脱敏算法。
- 实现三模式水印：零宽字符水印、SIM 水印（XOR 盐值 + Luhn 校验）、掩码水印（支持还原）。

## 可量化结果/Impact
- 核心引擎性能较旧版提升 5x+——来源：已确认事实（项目详情写 10x，以已确认事实 5x+ 为准）。
- 整体链路吞吐 1 倍以上提升——来源：项目详情「性能成果」。
- 单次脱敏延迟 < 10ms（简单 JSON）——来源：项目详情「性能成果」。
- QPS > 1000（4核8G，HTTP Server 模式）——来源：项目详情「性能成果」。
- 内存占用 < 500MB，规则支持 10万+——来源：项目详情「性能成果」。
- 80+ 敏感数据类型、20+ 脱敏算法——来源：项目详情「技术亮点」。
- 被 Nexis 网关原生集成——来源：项目详情「业务成果」。

## 两个 Resume Branch 的叙事角度
- Security Resume 强调点：数据安全引擎、80+ 敏感数据类型识别、20+ 脱敏算法、三模式水印、数据泄露检测。
- Backend Resume 强调点：Rust 多形态服务架构、Workspace 多 crate 设计、JNI 直接内存传递、被 Nexis 网关集成。

## 待确认/缺失
- 5x+ 性能提升的测试基准与旧版具体版本。
- 客户落地规模与业务线数量。
- Web 管理端是否基于 Next.js 及其具体职责。

## 加工备注
- 是否可直接用于简历：是（注意性能提升数字用 5x+，而非项目详情中的 10x）。
- 敏感信息提醒：无。
