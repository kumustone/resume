# Raw Materials（原材料）

本目录存放简历重构所需的全部原始物料。所有内容仅作归档和来源标注，不直接用于简历写作。粗料和细料从原材料中加工而来。

## 目录结构

```
materials/raw/
├── repos/          # 代码仓库
├── docs/           # Word / PDF / Markdown 文档
├── slides/         # PPT / Keynote
├── screenshots/    # 系统截图、架构图
└── notes/          # 零散笔记、聊天记录
```

## 代码仓库（repos）

### 中交兴路 / 千方集团

| 仓库路径 | 对应简历项目 | 访问状态 | 备注 |
|---------|-------------|---------|------|
| `/Users/liubo/workspace/zhongjiao/cadn_v6.4` | CADN 车联网接入平台 | 本地 | 千方/中交兴路合并呈现 |

### 蘑菇街

| 仓库路径 | 对应简历项目 | 访问状态 | 备注 |
|---------|-------------|---------|------|
| `/Users/liubo/workspace/mogu/im-cloud-server` | 自研 IM（C++） | 本地 | IM 云端服务 |
| `/Users/liubo/workspace/mogu/im-server-new` | 自研 IM（C++） | 本地 | IM 新服务端 |
| `/Users/liubo/workspace/mogu/network-sdk-cpp` | 自研 IM（C++）/ 长连接 SDK | 本地 | C++ 跨平台长连接 SDK |
| `/Users/liubo/workspace/mogu/wolverine-hids` | 企业级信息安全治理 | 本地 | HIDS Agent/服务端 |

### 玩物得志

| 仓库路径 | 对应简历项目 | 访问状态 | 备注 |
|---------|-------------|---------|------|
| `/Users/liubo/workspace/wanwu` | 业务风控平台、文本反垃圾、安全治理 | 本地 | 代码不多，大量为运营相关工作；风控核心代码缺失 |

### 闪捷信息科技

| 仓库路径 | 对应简历项目 | 访问状态 | 备注 |
|---------|-------------|---------|------|
| `/Users/liubo/workspace/secsmart/aisg/ai-dataset` | AI 安全网关 / Nexis | 本地 | — |
| `/Users/liubo/workspace/secsmart/aisg/nexis` | Nexis AI 安全网关 | 本地 | — |
| `/Users/liubo/workspace/secsmart/aisg/nginx_merry` | nginx_merry C++ 安全网关 | 本地 | 客户现场多项目运行，稳定运行超 2 年 |
| `/Users/liubo/workspace/secsmart/aisg/r_data_service` | r_data_service 数据安全引擎 | 本地 | — |
| `/Users/liubo/workspace/secsmart/aisg/secagent` | 终端/主机安全相关 | 本地 | — |
| `/Users/liubo/workspace/secsmart/aisg/ai_research` | AI 安全研究 | 本地 | — |
| `/Users/liubo/workspace/secsmart/aisg/flint-ocr` | OCR 相关数据识别 | 本地 | — |
| `/Users/liubo/workspace/secsmart/aisg/file-inspector` | 文件检查/数据安全 | 本地 | — |

## 非代码物料（docs / slides / screenshots / notes）

| 类型 | 路径/来源 | 状态 | 备注 |
|------|----------|------|------|
| 项目详情 Markdown | `materials/projects/*.md` | 已归档 | 11 个项目 |
| 述职材料 | `materials/annual-reviews/*.md` | 已归档 | 2023 / 2025-H1 / 2026 |
| 历史简历 | `materials/history-resume/*` | 已归档 | PDF/DOCX/MD |
| 近期构建产物 | `material/history-resume/*` | 已归档 | HTML/PDF |

## 加工原则

1. **代码仓库不是全部**：工作经历不能仅由代码体现。代码仅用于佐证技术栈、架构选择和工程规模。
2. **敏感信息脱敏**：任何含客户名、内部架构细节、未公开数据的原材料，加工为粗料/细料时必须脱敏。
3. **来源标注**：每个粗料/细料事实单元必须标注来源（来自哪个 raw 文件或仓库的哪个部分）。
