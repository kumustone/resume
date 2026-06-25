r_data_service — 多形态数据安全引擎 (Rust)

公司: 闪捷信息科技有限公司 | 时间: 2022.04-至今 | 角色: 高级研发工程师 / 技术负责人
技术栈: Rust · JNI · Regex · Trie · Watermark · Data Masking · Java SDK · Axum

【项目简介】
自研多形态数据安全服务引擎，基于 Rust 纯实现（零 JVM/Python 依赖），提供数据脱敏、数字水印、敏感数据识别、数据泄露检测等核心能力。同一套引擎代码支撑 Rust 库、Java SDK、HTTP Server、Web 管理端四种服务形态，覆盖不同技术栈的业务方接入场景。

【核心职责】
- 主导 Workspace 多 crate 架构设计（rds-infra 无状态引擎层 + rds-runtime 有状态编排层 + rds-jni JNI 绑定层）
- 设计 Segment → Recognize → Mask 三阶段流水线，承担识别与脱敏核心模块编码
- 推动 Java SDK 强类型 API 替代旧版 TLV 字符串协议，实现多平台动态库自动加载

【技术亮点】
- 多形态服务架构：同一套引擎代码，四种接入形态——Rust 库（零拷贝）、Java SDK（JNI 直接内存传递）、HTTP Server（REST API）、Web 管理端（Next.js 规则配置）
- 统一三阶段流水线：分词（JSON/HTML/XML/文本/中英混合）→ 识别（80+ 类型，正则/字典/Trie + Luhn 校验）→ 处理（脱敏/水印/重组输出）
- 80+ 敏感数据类型：覆盖基础身份、金融、交通、出入境、设备等全场景
- 20+ 脱敏算法：姓名/手机号/身份证/邮箱/银行卡/地址/护照等掩码规则
- 三模式水印：零宽字符水印（肉眼不可见）、SIM 水印（XOR 盐值 + Luhn 校验）、掩码水印（支持还原）
- 纯 Rust 实现：零外部依赖，自研 Office 文档解析（zip + quick-xml），性能优于 Presidio/python-docx 等开源方案

【性能成果】
- 核心引擎性能较旧版提升 10x（SIMD 加速正则 + Trie 优化字典查找 + Luhn 预计算）
- 整体链路吞吐 1 倍以上提升
- 单次脱敏延迟 < 10ms（简单 JSON）
- QPS > 1000（4核8G，HTTP Server 模式）
- 内存占用 < 500MB，规则支持 10万+

【业务成果】
- 支撑多业务线规模化落地，降低接入成本与交付周期
- Java SDK 强类型 API 替代 TLV 字符串协议，消除运行时类型错误
- 兼容多平台动态库自动加载（macOS ARM64 / Linux x86_64 / ARM64）
- 被 nexis 网关原生集成，实现 80+ 类敏感数据实时防护

---
基于 r_data_service 项目文档整理。运行 make materials 重新生成。
