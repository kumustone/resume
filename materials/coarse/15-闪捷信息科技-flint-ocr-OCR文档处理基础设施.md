# flint-ocr — OCR 文档处理基础设施

## 基础事实
- 公司：闪捷信息科技有限公司
- 时间：2022.04-至今（与闪捷同期）
- 职位：资深开发工程师 / 技术负责人
- 技术栈：Rust · PaddleOCR · LLM Vision · OpenAI Vision 协议 · Docker
- 代码仓库佐证：`/Users/liubo/workspace/secsmart/aisg/flint-ocr`（Rust，165 文件）

## 项目目标（一句话）
面向 AI 时代的文档处理基础设施，提供本地 PaddleOCR + 云端 LLM Vision 双引擎 OCR 服务，兼顾成本、速度与准确率。

## 候选人贡献
- 设计并实现基于 Rust 的 OCR 文档处理服务。
- 实现本地 PaddleOCR（零成本、120ms）与云端 LLM Vision（92% 准确率）双引擎架构。
- 兼容 OpenAI Vision 协议，支持一行代码替换 GPT-4V 调用。
- 支持 Docker 部署与私有化落地。

## 可量化结果/Impact
- 本地推理 120ms，较云端 GPT-4V 快 6 倍。
- 云端模式准确率 92%。
- 本地模式零成本起步。
- （待补充：实际部署客户数、日均处理量等）

## 两个 Resume Branch 的叙事角度
- Security Resume：AI 时代数据安全识别能力、文档敏感信息检测、OCR 与水印/脱敏联动。
- Backend Resume：Rust 高性能 OCR 服务、双引擎架构、成本与性能平衡设计。

## 待确认/缺失
- 与 r_data_service / file-inspector 的集成关系。
- 实际生产环境部署规模。
- 是否作为独立项目呈现，还是并入数据安全产品线。

## 加工备注
- **简历权重**：P1-P2（可作为数据安全/AI 安全能力的重要组成）。
- 是否可直接用于简历：是，但需确认与其他项目的边界。
- 敏感信息提醒：避免披露具体客户使用场景。
