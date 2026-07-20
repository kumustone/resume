# Phase 5 — Resume A/B Core Skills 设计

## 版本演进

- v1：完整叙述句，项目细节过多 → **已废弃**
- v2：关键词化，但分类标题偏欧美 → **已废弃**
- **v3**：中文分类标题 + 行业习惯术语，国内技术总监阅读优先

---

## 设计原则

1. **分类标题全部中文**：国内简历的阅读节奏。
2. **技术术语遵循行业习惯**：中文概念 + 英文专业术语（如 TCP/IP、Nginx、Kafka 保留英文，领域词如 后端开发、并发编程 使用中文）。
3. **纯关键词，无动词**：不写「熟悉」「具备」「掌握」「主导」「负责」。
4. **每域 4–6 个关键词**：5 秒内扫完。
5. **Snmary / Core Skills / Project Experience 严格分离**：不重复。
6. **优先国内技术总监阅读习惯**，不刻意迎合 ATS。

---

## Resume A — Application Security Engineer

### Core Skills v3

```yaml
core_skills:
  - title: 应用安全
    details:
      - AI安全
      - API安全
      - WAF
      - 内容安全
      - 业务风控
      - 数据安全

  - title: 安全工程
    details:
      - SDL
      - 代码审计
      - 漏洞治理
      - 安全治理
      - 等保合规
      - HIDS

  - title: 安全产品
    details:
      - AI网关
      - 数据安全引擎
      - 反欺诈
      - 反垃圾
      - 访问控制

  - title: 编程语言
    details:
      - Rust
      - Go
      - C++

  - title: 基础组件
    details:
      - Nginx
      - Pingora
      - Linux
      - TCP/IP
      - Kafka
      - Redis
```

### 设计说明

| 分类 | 为什么这样分类 | 为什么保留这些关键词 | 是否还能精简 |
|------|---------------|---------------------|-------------|
| **应用安全** | 覆盖安全能力域广度，技术总监一眼看到能力覆盖范围。 | AI安全、API安全、WAF、内容安全、业务风控、数据安全是简历中实际覆盖的方向，有项目支撑。 | 6 个已是最小集合。DLP 与数据安全语义重叠，去掉。 |
| **安全工程** | 区分安全开发与安全工程/治理能力，这是 Resume A 的核心差异化。 | SDL、代码审计、漏洞治理体现安全研发能力；安全治理、等保合规、HIDS 体现体系建设能力。 | 6 个已精选。去掉了 Compliance（用等保合规代替）、Security Governance（用安全治理代替）。 |
| **安全产品** | 建立安全产品研发人设，与「应用安全」（能力域）区分：前者回答会什么，后者回答做过什么类型的产品。 | AI网关、数据安全引擎、反欺诈、反垃圾、访问控制对应闪捷和玩物得志的实际产品。 | 5 个，略少，但 AIDataset、OCR 等太细，不放。 |
| **编程语言** | Core Skills 中唯一保持 3 个关键词的项，多反而不精。 | Rust、Go、C++ 是实际工程语言，不需要列出 Python。 | 已最精简。 |
| **基础组件** | 支撑安全产品的技术底座，让技术总监感知到不是只会写脚本。 | Nginx、Pingora、Linux、TCP/IP、Kafka、Redis 覆盖网络、代理、操作系统、消息、缓存，足够。 | 可以考虑去掉 Redis 或 Kafka，但两者都体现分布式能力，暂保留。 |

### 删除说明

- 英文分类标题（Application Security → 应用安全）。
- CISSP → 放在 Certification/Education 区域。
- DLP → 与数据安全语义重叠。
- 身份与访问（Identity & Access）→ 改为更具体的「访问控制」。
- 所有动词前缀（熟悉、具备、掌握等）。

---

## Resume B — Senior Backend Engineer

### Core Skills v3

```yaml
core_skills:
  - title: 后端开发
    details:
      - 高性能
      - 网关
      - 长连接
      - IM系统
      - 分布式系统
      - 低延迟

  - title: 编程语言
    details:
      - Rust
      - Go
      - C++
      - Linux

  - title: 网关与网络
    details:
      - Nginx
      - Pingora
      - 反向代理
      - TCP/IP
      - HTTP/HTTPS
      - WebSocket

  - title: 并发编程
    details:
      - epoll
      - kqueue
      - 异步
      - 无锁
      - 高并发

  - title: 中间件
    details:
      - Redis
      - Kafka
      - ZooKeeper
      - MySQL
      - ClickHouse
```

### 设计说明

| 分类 | 为什么这样分类 | 为什么保留这些关键词 | 是否还能精简 |
|------|---------------|---------------------|-------------|
| **后端开发** | 核心能力域标题，覆盖六个后端技术画像关键词。 | 高性能、网关、长连接、IM系统、分布式系统、低延迟 — 每个词对应一个实际项目方向。 | 6 个，如果要去一个，考虑去掉 低延迟（在并发编程中隐含）。 |
| **编程语言** | 多语言系统编程是 Backend 简历的核心信号。 | Rust、Go、C++ 三种工程语言，Linux 作为系统编程底座。 | 不精简。 |
| **网关与网络** | Resume B 最核心的差异化能力域。 | Nginx、Pingora 是实际代理框架，反向代理、TCP/IP、HTTP/HTTPS、WebSocket 覆盖 L4–L7。 | 6 个已精简，去掉了 TLS（不是核心卖点）。 |
| **并发编程** | 高性能后端的能力底座。 | epoll、kqueue 是具体 I/O 模型，异步、无锁、高并发是并发编程关键词。 | 5 个，略少，但可以了。 |
| **中间件** | 常用基础设施，技术总监默认会看这一行。 | Redis、Kafka、ZooKeeper、MySQL、ClickHouse 是实际使用的组件，有项目支撑。 | 5 个，可以考虑去掉 ClickHouse（如果不足以成为亮点）。 |

### 删除说明

- 英文分类标题（Backend Development → 后端开发等）。
- 所有项目成果数字（QPS、RT、亿级、10w+）。
- 所有经验描述词（0→1、生产环境、电信级高可靠、团队管理）。
- 具体技术实现词（Java SDK、JNI、OCR）。

---

## v3 与 v2 对比

| 维度 | v2 | v3 |
|------|----|----|
| 分类标题 | Application Security、Programming Languages | 应用安全、编程语言 |
| 阅读节奏 | 中英混合，偏欧美简历 | 纯中文标题，国内阅读自然 |
| 领域词 | Backend Development、Concurrency | 后端开发、并发编程 |
| 关键词形式 | 英文为主 | 中文概念 + 英文专业术语 |
| 每域数量 | 4–8 个 | 4–6 个 |
| 动词/前缀 | 无 | 无（保持） |
| Resume A 域数 | 5 | 5（保持） |
| Resume B 域数 | 5 | 5（保持） |

---

## A/B 区分度

| 维度 | Resume A | Resume B |
|------|---------|---------|
| 第一项 | 应用安全 | 后端开发 |
| 第二项 | 安全工程 | 编程语言 |
| 第三项 | 安全产品 | 网关与网络 |
| 第四项 | 编程语言 | 并发编程 |
| 第五项 | 基础组件 | 中间件 |
| 技术总监第一眼 | 安全人 | 后端人 |

---

## 与 Summary / Project Experience 的职责分离

| 模块 | 职责 | 是否越界 |
|------|------|---------|
| Summary | 我是谁（技术人设） | ✅ 否 |
| Core Skills | 我掌握哪些技术领域（技术画像） | ✅ 否 |
| Project Experience | 我具体做过什么（能力证明） | ✅ Core Skills 不承载 |

---

## 确认结论（v3）

- Resume A 采用 **Core Skills v3**。
- Resume B 采用 **Core Skills v3**。
- 后续所有引用 Core Skills 的位置统一用 v3。
- 分类标题统一中文，技术术语遵循行业习惯。

---

## Core Skills v4（根据国内技术总监反馈优化）

### 调整要点

| 反馈 | 修改 |
|------|------|
| Resume A「业务风控」不属于应用安全域 | 从「应用安全」移至「安全产品」 |
| Resume A「HIDS」在安全工程中层次不匹配（方法论 vs 产品） | 删除 |
| Resume A「基础组件」命名不准确 | 改名为「技术栈」 |
| Resume B「高性能」与「低延迟」表达相似 | 替换为「网络编程」，覆盖更广 |
| Resume B「高并发」是结果不是技术 | 替换为「IO多路复用」 |
| Resume B「Linux」放在编程语言不合适 | 移至「网关与网络」 |
| 排序应体现最大竞争力 | 重新排序能力域 |

---

## Resume A — Application Security Engineer

### Core Skills v4

```yaml
core_skills:
  - title: 应用安全
    details:
      - AI安全
      - API安全
      - WAF
      - 内容安全
      - 数据安全

  - title: 安全产品
    details:
      - AI网关
      - 数据安全引擎
      - 业务风控
      - 反欺诈
      - 反垃圾
      - 访问控制

  - title: 安全工程
    details:
      - SDL
      - 代码审计
      - 漏洞治理
      - 安全治理
      - 等保合规

  - title: 编程语言
    details:
      - Rust
      - Go
      - C++

  - title: 技术栈
    details:
      - Nginx
      - Pingora
      - Linux
      - TCP/IP
      - Kafka
      - Redis
```

### 修改说明

| 修改 | 说明 |
|------|------|
| 业务风控 移至安全产品 | 业务风控是产品形态，不是应用安全领域。安全产品回答「你做过什么类型的产品」。 |
| 删除 HIDS | HIDS 是具体产品，与 SDL、代码审计、漏洞治理等安全方法论不在同一层次。如必须保留，可改为「主机安全」。 |
| 基础组件 → 技术栈 | Linux、TCP/IP、Pingora 不是「组件」，改为「技术栈」更自然。 |
| 重新排序 | 应用安全（能力域）→ 安全产品（产品形态）→ 安全工程（工程方法）→ 编程语言 → 技术栈。从业务到技术，阅读更流畅。 |

---

## Resume B — Senior Backend Engineer

### Core Skills v4

```yaml
core_skills:
  - title: 后端开发
    details:
      - 网关
      - 长连接
      - IM系统
      - 分布式系统
      - 网络编程
      - 低延迟

  - title: 网关与网络
    details:
      - Nginx
      - Pingora
      - 反向代理
      - TCP/IP
      - HTTP/HTTPS
      - Linux

  - title: 并发编程
    details:
      - epoll
      - kqueue
      - 异步
      - 无锁
      - IO多路复用

  - title: 编程语言
    details:
      - Rust
      - Go
      - C++

  - title: 中间件
    details:
      - Redis
      - Kafka
      - ZooKeeper
      - MySQL
      - ClickHouse
```

### 修改说明

| 修改 | 说明 |
|------|------|
| 高性能 → 网络编程 | 「高性能」与「低延迟」语义重叠。改为「网络编程」扩大覆盖面，体现从 TCP 到应用层的完整能力。 |
| 高并发 → IO多路复用 | 「高并发」是结果不是技术。改为「IO多路复用」更加具体、技术化，国内工程师更接受。 |
| Linux 移至「网关与网络」 | Linux 不是编程语言，放在「网关与网络」作为基础平台更自然。 |
| 重新排序 | 后端开发（能力域）→ 网关与网络（核心竞争力）→ 并发编程（技术底座）→ 编程语言 → 中间件。突出网关是最大竞争力。 |

---

## v4 与 v3 对比

| 维度 | v3 | v4 |
|------|----|----|
| Resume A 业务风控 | 在应用安全 | 移至安全产品 |
| Resume A HIDS | 在安全工程 | 删除 |
| Resume A 基础组件/技术栈 | 基础组件 | 技术栈 |
| Resume B 高性能 | 在后端开发 | 替换为 网络编程 |
| Resume B 高并发 | 在并发编程 | 替换为 IO多路复用 |
| Resume B Linux | 在编程语言 | 移至网关与网络 |
| 排序逻辑 | 按类型 | 按竞争力权重 |

---

## 确认结论（v4）

- Resume A 采用 **Core Skills v4**。
- Resume B 采用 **Core Skills v4**。
- Core Skills 优化到此为止，后续精力转向 Project Experience。


---

## 待确认问题

1. Resume A 的「安全产品」和「应用安全」是否分类清晰？是否需要合并？
2. Resume B 的「并发编程」域是否需要增加关键词？
3. Resume A 的「基础组件」是否改为「基础设施」更自然？
4. 是否需要为关键开源技术（Pingora）加括号解释？
5. 是否有遗漏的重要关键词？

确认后，用 v5 Summary + v3 Core Skills 进入项目经历阶段。
