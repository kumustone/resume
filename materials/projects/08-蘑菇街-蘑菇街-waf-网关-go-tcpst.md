# 蘑菇街 WAF 网关 (Go/tcpstream) — 核心开发 / 架构设计

**公司**: 蘑菇街 | **时间**: 2015.05-2019.08 | **角色**: 资深开发工程师

**技术栈**: Go · tcpstream · Reverse Proxy · WAF · easyjson · Regex Engine · TCP Long Connection

---

## 简历版（简洁 · 适合 1 页简历）

- 架构设计：设计 waf-gate（极简 HTTP 反向代理）+ waf-server（检测引擎）进程分离架构，通过自研 tcpstream 长连接库通信。稳定性优先：waf-server 崩溃/超时（20ms）自动放行 bypass，服务不可用时全流量透传，实现网关稳定性与检测能力的完全解耦。
- 性能优化：基于 Go 标准库 `httputil.ReverseProxy` 最小化修改构建代理层，使用 easyjson 零分配序列化协议 + 正则预编译 + 多 Server 轮询负载均衡，将检测链路开销压至毫秒级。单机峰值 QPS 20K+，爬虫高峰期超时率从 10% 压至 0.01%（三个数量级改善）。
- 规则引擎：设计 JSON 配置驱动的多字段组合规则引擎，支持 Host/Referer/URL/User-Agent/Content-Type 正则匹配 + IP 黑白名单，规则文件叠加热加载，兼顾攻防响应速度与运营灵活性。

## 角色与职责

设计并实现 waf-gate + waf-server 进程分离架构的全站 WAF 网关，自研 tcpstream 长连接库
作为进程间通信层，支撑全站 HTTP/HTTPS 流量接入。

## 架构设计

waf-gate：基于 Go 标准库 `httputil.ReverseProxy` 最小化修改的极简 HTTP/HTTPS 反向代理，
负责流量接入、TLS 终结、upstream 路由、waf-server 健康检查。对业务链路完全透明。
waf-server：WAF 检测引擎，包括 IP 黑白名单、多字段正则规则引擎（Host/Referer/URL/
User-Agent/Content-Type）、JSON 配置驱动规则管理。
通信层（tcpstream）：自研 TCP 长连接库，Gate 与 Server 之间多对多连接 + 轮询负载均衡。
20ms 超时自动放行，Server 崩溃或不可用时全流量 bypass——网关稳定性与检测能力完全解耦。

## 技术决策

- 为什么 Gate/Server 进程分离：①稳定性隔离——waf-server 崩溃不影响用户请求；②资源隔离——检测计算密集（正则匹配）不争抢代理层的 CPU；③独立扩缩——Server 可以独立横向扩展。
- 为什么 20ms 超时：HTTP 请求的整体延迟预算通常在 100-200ms，WAF 检测占 20ms 是可接受上限。超过即判定 Server 异常，放行保证业务可用。
- 为什么用 easyjson：Go 标准 `encoding/json` 使用反射，每次序列化都有分配开销。easyjson 在编译期生成序列化代码，零分配，对高 QPS 场景的 GC 压力降低显著。
- 为什么正则预编译：每个请求都要做规则匹配，如果每次 `regexp.MatchString` 都重新编译正则，CPU 开销不可接受。启动时一次性编译，运行时直接 `FindString`。

## 性能数据

单机峰值 QPS 20K+，检测链路开销毫秒级。
爬虫高峰期超时率从 10% 压至 0.01%（三个数量级改善），通过 easyjson 零分配 + 正则预编译 + 多 Server 轮询实现。
tcpstream 自研库：支持多对多长连接、自动重连、连接池、超时控制，在 waf-gate 和 waf-server 之间实现 <1ms 的进程间通信延迟。

## 踩坑与解决

- 正则 ReDoS 攻击：恶意请求构造特殊的字符串触发正则回溯爆炸。通过正则复杂度分析 + 执行超时熔断（100μs）解决。
- 大 Body 内存控制：请求体超过 100KB 不发送 waf-server 检测（避免内存攻击），但需要在 gate 层做协议完整性校验。
- TLS 证书热加载：HTTPS 多个二级域名使用不同证书，证书变更不能重启服务。通过文件监听 + 证书缓存实现热加载。

---
*生成自 `data/resume.yaml` + `data/project-details.yaml`。运行 `make materials` 重新生成。*
