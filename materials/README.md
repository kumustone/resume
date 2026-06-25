# 项目素材库

> 方便在招聘网站填写表单时直接复制粘贴。
> 每张卡片 = 简历精简版（直接贴）+ 架构设计/技术决策/性能数据/踩坑记录（面试用）。
>
> 详细信息来自 `data/project-details.yaml`，与简历 YAML 独立维护。

**基本信息**

刘波 · 杭州 · 15 年系统研发经验 · 高性能网络服务 / 企业安全平台 · Rust / C++ / Go

---

## 标签索引

`AI Gateway` `Anti-fraud` `Anti-spam` `C` `C++` `Client Hardening` `Cluster` `Consistent Hash` `Cross-platform SDK` `DFA` `Data Masking` `Debugging` `Device Fingerprint` `Filesystem` `GPS Protocol` `Go` `HIDS` `IM` `JNI` `Java SDK` `Kafka` `LVS` `Linux Kernel` `Load Balance` `Long Connection` `Luhn` `MLPS 2.0` `Memory Management` `NDJSON` `Nginx` `Nginx C Module` `OCR` `Patent` `Penetration Testing` `Performance Optimization` `Pingora` `Redis` `Regex` `Regex Engine` `Reverse Proxy` `Risk Engine` `Rust` `SIM Watermark` `SSE` `Security Compliance` `Socket` `TCP` `TCP Long Connection` `Thread Pool` `Tokio` `Trie` `VRP` `Vulnerability Scanner` `WAF` `Watermark` `ZooKeeper` `async trait` `dlopen` `easyjson` `epoll` `iptables` `kqueue` `tcpstream`

---

## 按公司排列


### 闪捷信息科技有限公司

- [企业级 AI 安全网关平台 (Rust/Pingora) — 核心开发 / 架构设计](projects/01-闪捷信息科技-企业级-ai-安全网关平台-rust-.md)
  Rust, Pingora, Tokio, ZooKeeper, SSE, NDJSON, async trait, AI Gateway, Nginx, C++
- [nginx_merry 高性能 C++ Nginx 安全网关模块 — 核心开发 / 架构设计](projects/02-闪捷信息科技-nginx_merry-高性能-c++-.md)
  C++, Nginx C Module, dlopen, ZooKeeper, Kafka, Redis, WAF, Data Masking, Watermark
- [r_data_service 多形态数据安全引擎 (Rust) — 核心开发 / 架构设计](projects/03-闪捷信息科技-r_data_service-多形态数据.md)
  Rust, JNI, Regex, Trie, Luhn, OCR, Watermark, Data Masking, SIM Watermark, Java SDK

### 玩物得志

- [业务风险控制平台从 0-1 建设](projects/04-玩物得志-业务风险控制平台从-0-1-建设.md)
  Go, Risk Engine, Kafka, Redis, Device Fingerprint, Anti-fraud
- [高性能文本反垃圾系统 (自研)](projects/05-玩物得志-高性能文本反垃圾系统-自研.md)
  Go, DFA, Regex, Anti-spam, Performance Optimization
- [企业级安全治理与等保合规](projects/06-玩物得志-企业级安全治理与等保合规.md)
  Security Compliance, MLPS 2.0, Device Fingerprint, Client Hardening

### 蘑菇街

- [蘑菇街 自研 IM (C++) — 核心开发](projects/07-蘑菇街-蘑菇街-自研-im-c++-—-核心.md)
  C++, epoll, kqueue, TCP, IM, Cross-platform SDK, Long Connection
- [蘑菇街 WAF 网关 (Go/tcpstream) — 核心开发 / 架构设计](projects/08-蘑菇街-蘑菇街-waf-网关-go-tcpst.md)
  Go, tcpstream, Reverse Proxy, WAF, easyjson, Regex Engine, TCP Long Connection
- [企业级信息安全治理](projects/09-蘑菇街-企业级信息安全治理.md)
  Go, HIDS, iptables, Vulnerability Scanner, Penetration Testing

### 北京中交兴路车联网

- [核心服务研发](projects/10-北京中交兴路-核心服务研发.md)
  C++, epoll, Redis, Cluster, Load Balance, Consistent Hash, Patent

### 华为技术有限公司

- [虚拟文件管理模块（VRPV8 电信级路由器）](projects/11-华为技术有限-虚拟文件管理模块（vrpv8-电信级路由.md)
  C, Linux Kernel, Filesystem, VRP, Memory Management, Debugging

### 北京千方集团科技有限公司

- [高并发接入模块](projects/12-北京千方集团-高并发接入模块.md)
  C++, Socket, epoll, TCP, GPS Protocol, LVS, Thread Pool


---

## 使用方式

| 场景 | 操作 |
|------|------|
| 填网站表单 | 打开目标卡片 → 全选 → 复制 → 粘贴到项目经历栏 |
| 准备面试 | 看「架构设计」+「技术决策」+「踩坑与解决」 |
| 技术面 self-intro | 用「角色与职责」+「简历版」组织 2 分钟项目介绍 |

> 数据源: `resume/data/resume.yaml` + `resume/data/project-details.yaml`。运行 `make materials` 重新生成。
