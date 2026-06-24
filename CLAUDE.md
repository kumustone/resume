# Resume — CLAUDE.md

本文件记录简历项目的求职定位、内容规则和排版规范。后续 Agent 修改简历前先读此文件。

---

## 目标岗位与市场定位

| 维度 | 定位 |
|------|------|
| **目标岗位** | 高级研发工程师 / 技术负责人（IC+TL 混合型） |
| **目标企业** | 外企 R&D 中心、研究院、国企技术部门、成熟中小企业 |
| **对标级别** | Senior Software Engineer / Tech Lead |
| **不要** | Principal Engineer、技术总监、AI 专家、纯架构师 |
| **英文 title** | Senior Software Engineer / Tech Lead（非 Principal） |

### 核心画像

```
电信级工程纪律（华为起源）
+ 15年系统研发深度（C++/Rust/Linux）
+ 安全领域纵深（CISSP + WAF/数据安全/风控）
+ 近期技术演进证明（AI Gateway）
+ 独立闭环能力（0→1 系统建设）
+ 稳定可靠的工作预期（不是跳板型候选人）
```

---

## 简历语言规则

### 角色定位词

| ✅ 用 | ❌ 不用 |
|------|--------|
| 高级研发工程师 / 技术负责人 | 架构负责人、系统架构师 |
| 核心开发 / 架构设计 | 技术总监 |
| 设计并实现 | 自研（过度使用） |
| 主导设计、主导建设 | 负责（太弱） |

### 去互联网安全黑话

| ❌ 互联网黑话 | ✅ 通用工程表达 |
|-------------|---------------|
| 对抗体系建设 | 风险控制体系建设 |
| 反爬虫、反作弊 | 异常行为检测 |
| 私域导流 | 业务违规行为治理 |
| 资损风险 | 业务风险与损失 |
| 攻防演练 | 安全测试与风险验证 |
| 强对抗场景 | 高并发、高风险业务场景 |
| 头部客户 | 金融、政企客户 |
| 安全运营闭环 | 持续运营机制 |
| 甲方企业安全体系建设负责人 | 企业安全平台建设 / 安全架构方向 |

### 项目描述规则

- 保留"设计并实现"用于真正从0到1的系统（WAF引擎、反垃圾引擎）
- 保留技术稀缺性关键词：Pingora、Tokio、async trait、block_in_place、SSE/NDJSON、Prompt Injection、零拷贝
- 每个核心项目收尾要有业务价值陈述（成本降低%、稳定性年限、客户规模）
- 安全产品列表不要堆砌——先说能力域（网络/应用/终端安全），再举例（含 WAF、EDR、SIEM 等）
- 30% Leader / 70% Engineer 感觉——体现技术决策和项目推进能力，不要强调团队规模

### 数据亮点（简历中已前置）

| 数据 | 位置 |
|------|------|
| QPS +138%, RT -63% | 闪捷网关 |
| WAF 超时率 10%→0.01% | 蘑菇街（仅此处，核心能力禁止重复） |
| 年度安全成本降低 60% | 玩物得志反垃圾 |
| 核心引擎性能 10x 提升 | r_data_service |
| 华为高可靠理念"贯穿后续15年工程实践" | 华为条目收尾 |
| 千方 period "（毕业前入职）" | 避免 HR 系统标记时间线冲突 |

---

## 内容结构（YAML）

数据源文件：`data/resume.yaml`

### Profile
- 无出生年份
- `experience_summary: 15 年系统研发经验 · 高性能网络服务 / 企业安全平台`
- `tech_stack: Rust / C++ / Go`（Rust 放首位）

### Summary（gateway 方向）
- 定位：资深系统研发，不是 AI 专家
- 提及电信级软件研发背景
- AI 作为近年实践方向，不是核心标签
- 提及独立闭环能力
- 持有 CISSP

### Core Skills（gateway 方向，5 项）
1. 高性能网络与系统研发（C++ / Rust / Linux） — 关键词：TCP/IP 网络编程（非 Linux 网络栈），Pingora 必须加括号解释
2. 企业安全平台建设（WAF / 风控 / 数据安全） — **禁止出现 WAF 具体数字**（20K+、10%→0.01%），这些数据只在蘑菇街经历里出现
3. AI 网关与 LLM 安全实践
4. 工程可靠性与系统演进 — 含 CISSP
5. AI 工具链与团队效能

规则：
- 标题带关键词标签 `（xxx）`
- details 精简到 1-3 行，删虚词
- 能力集描述"能做什么"，不描述"怎么做"的实现细节
- 禁止与工作经历逐字重复数据
- Pingora 等小众技术必须加括号解释，如 `（Pingora，Cloudflare 开源的下一代高性能网络代理）`

### Experience — 闪捷（2022.04-至今）
- `role_gateway: 高级研发工程师 / 技术负责人`
- 项目名：`核心开发 / 架构设计` 而非 `架构负责人`
- 2 个 gateway 项目：企业级AI安全网关平台 + r_data_service
- 必须有 hands-on 信号（"承担核心模块编码"）
- 网关平台条目加"已持续稳定运行超 2 年"
- 客户描述：`金融、政企客户`

### Experience — 其他公司
- 华为条目作为"原点故事"，末尾加"贯穿后续 15 年工程实践"
- 玩物得志、蘑菇街保持 Engineer 角色描述，不过度包装

### Tech Stack
- 无 CET-6
- `ai_llm` 字段表达为工程实践，非营销语言
- 无 `tags` 字段（已删除）

---

## 排版规范（CSS）

文件：`html/css/resume.css`

| 属性 | 值 | 说明 |
|------|-----|------|
| **字体-正文/标题** | PingFang SC | 全文统一，靠字重区分层级 |
| **字体-个人简介** | Adobe Kaiti Std（楷体）| 唯一例外，视觉区分 |
| **正文字号** | 10.5pt | 五号 |
| **正文字重** | 400（Regular） | |
| **正文行高** | 1.4 | 中文密集档 |
| **正文颜色** | #1a1a1a | 深灰，不是纯黑 |
| **字号层级** | 20 → 13 → 12 → 11 → 10.5 → 9.5 | 姓名→section→公司→项目→正文→页眉 |
| **标题字重** | 600（Semibold） | |
| **section 分隔线** | 1pt solid #000 | |
| **list item 间距** | 0.3em | |
| **experience-item 间距** | 0.6em | |
| **section 间距** | 0.6em | |
| **页面边距** | Playwright 控制（top:0.50in, right:0.65in, bottom:0.50in, left:0.65in） | ~12.7mm/16.5mm |
| **页眉字号** | 9.5pt | |
| **对齐方式** | text-align: justify + text-justify: inter-ideograph | 中文两端对齐 |
| **禁止** | small-caps、中文斜体、font-synthesis | |
| **页数** | ≤ 3 页 | |

---

## 构建

```bash
cd resume
make          # 构建 HTML + PDF（默认）
make html     # 仅 HTML
make pdf      # 仅 PDF（依赖 html）
make latex    # LaTeX PDF（需 XeLaTeX，非默认）
make clean    # 清理 HTML + PDF 产物
make clean-all # 清理全部含 LaTeX
```

依赖：Node.js（js-yaml, mustache, playwright）+ Chrome（headless PDF）

---

## 字体资源

已安装到 `~/Library/Fonts/`：
- PingFang SC（macOS 系统自带）
- Adobe Song Std L / Adobe Heiti Std R / Adobe Kaiti Std R（来自 iCloud 备份）
- Source Han Serif VF / Source Han Sans SC VF（Homebrew 安装）

当前使用：全文 PingFang SC + 简介 Adobe Kaiti Std。

---

## 工作进展（截至 2026-06-22）

### ✅ 已完成
- 简历内容：YAML 数据源完成，gateway/security 双方向
- 排版：PingFang SC + Adobe Kaiti Std，字号层级稳定，3页不超限
- 语言：去互联网安全黑话，定位为"资深系统研发+安全+AI实践"
- 构建：`make all` → HTML + PDF 一键生成
- 目录：LaTeX 文件归入 `latex/`，career/ 拆分重组
- Git tag: `v2.0.0`

### 🔲 待办
- [ ] LaTeX 构建验证（fontawesome 字体路径需修复，低优先级）
- [ ] `interview/data/` 面试题内容补充
- [ ] `interview/data/market/` 职位数据更新

---

## 版本

| Tag | 说明 |
|-----|------|
| `v2.0.0` | YAML数据驱动 + HTML/PDF现代排版，完成所有内容和排版优化 |
