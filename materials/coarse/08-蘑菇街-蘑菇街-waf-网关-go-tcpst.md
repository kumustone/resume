# 蘑菇街 WAF 网关（Go/tcpstream）— 核心开发 / 架构设计

## 基础事实
- 公司：蘑菇街
- 在职时间：2015.05-2019.08
- 职位：资深开发工程师
- 技术栈（从项目详情中提取，去重并规范）：Go · tcpstream · Reverse Proxy · WAF · easyjson · Regex Engine · TCP Long Connection
- 代码仓库佐证（如适用）：`/Users/liubo/workspace/mogu`（含 im-cloud-server、im-server-new、network-sdk-cpp、wolverine-hids）

## 项目目标（一句话）
设计并实现 waf-gate + waf-server 进程分离架构的全站 WAF 网关，自研 tcpstream 长连接库作为进程间通信层，支撑全站 HTTP/HTTPS 流量接入。

## 候选人贡献
- 设计 waf-gate（极简 HTTP 反向代理）+ waf-server（检测引擎）进程分离架构。
- 自研 tcpstream 长连接库作为 Gate 与 Server 间通信层。
- 基于 Go 标准库 `httputil.ReverseProxy` 最小化修改构建代理层。
- 使用 easyjson 零分配序列化协议 + 正则预编译 + 多 Server 轮询负载均衡。
- 设计 JSON 配置驱动的多字段组合规则引擎，支持 Host/Referer/URL/User-Agent/Content-Type 正则匹配 + IP 黑白名单。
- 实现规则文件叠加热加载。
- 解决正则 ReDoS 攻击（正则复杂度分析 + 执行超时熔断 100μs）。
- 解决大 Body 内存控制（超过 100KB 不发送 waf-server 检测）。
- 实现 TLS 证书热加载。

## 可量化结果/Impact
- 单机峰值 QPS 20K+——来源：项目详情「性能数据」。
- 爬虫高峰期超时率从 10% 压至 0.01%（三个数量级改善）——来源：项目详情「性能数据」。
- 检测链路开销毫秒级——来源：项目详情「性能数据」。
- tcpstream 进程间通信延迟 <1ms——来源：项目详情「性能数据」。
- 20ms 超时自动放行——来源：项目详情「架构设计」。

## 两个 Resume Branch 的叙事角度
- Security Resume 强调点：全站 WAF 网关、多字段组合规则引擎、IP 黑白名单、ReDoS 防护、20ms 超时 bypass 机制。
- Backend Resume 强调点：Go 高性能反向代理、自研 tcpstream 长连接库、进程分离架构、easyjson 零分配、QPS 20K+。

## 待确认/缺失
- 全站流量规模与 waf-server 集群规模。
- tcpstream 是否开源或仅在内部使用。
- WAF 规则数量与命中率的量化数据。
- 100μs 熔断阈值的生产效果。

## 加工备注
- 是否可直接用于简历：是（WAF 超时率 10%→0.01% 仅此处可用，其他项目禁止复用）。
- 敏感信息提醒：该项目的 20K+ QPS / 10%→0.01% 数据为简历核心亮点，不要分散到其他项目中重复。
