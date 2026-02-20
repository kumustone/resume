#!/usr/bin/env python3
"""
简历关键词分析器
- 解析 content/ 下的 .tex 文件，提取技术栈和职位信息
- 基于规则映射生成 Boss直聘 搜索关键词
- 写入 config.json，供 boss.py 使用

用法：
  python3 keyword_advisor.py                  # 分析简历并更新 config.json
  python3 keyword_advisor.py --dry-run        # 只打印推荐，不写入
  python3 keyword_advisor.py --feedback output/jobs_xxx.csv  # 基于爬取结果优化关键词
"""

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

CRAWLER_DIR = Path(__file__).parent
RESUME_CONTENT_DIR = CRAWLER_DIR.parent / "content"
CONFIG_FILE = CRAWLER_DIR / "config.json"

# ── 技术词 → Boss直聘 搜索关键词 映射 ──────────────────────────────────────────
# 格式：(正则匹配简历中的技术词, [对应的搜索关键词列表], 权重)
TECH_TO_KEYWORD_RULES = [
    # 安全方向
    (r"WAF|Web应用防火墙",          ["WAF开发工程师", "Web安全开发"],          3),
    (r"API.{0,4}安全|API.{0,4}网关", ["API安全工程师", "API网关开发"],          3),
    (r"HIDS|主机入侵检测",           ["HIDS开发", "主机安全开发"],              2),
    (r"CISSP",                       ["安全架构师", "信息安全专家"],             3),
    (r"风控|黑灰产|反爬|人机对抗",   ["安全风控工程师", "风控系统开发"],         2),
    (r"等保|渗透测试",               ["安全开发工程师", "网络安全工程师"],        2),
    (r"安全.{0,6}体系|安全.{0,6}建设", ["安全架构师", "安全负责人"],             2),

    # 网关/高性能
    (r"Nginx.{0,8}开发|Nginx.{0,8}模块", ["Nginx开发", "高性能网关开发"],       3),
    (r"网关|Gateway",                ["API网关开发", "流量网关工程师"],           2),
    (r"高并发|高性能|epoll|事件驱动", ["高性能后端工程师", "C++服务端开发"],      2),
    (r"分布式",                      ["分布式系统工程师", "后端架构师"],          1),

    # 语言
    (r"C\+\+",                       ["C++后端开发", "C++高级工程师"],           2),
    (r"Golang|Go语言",               ["Golang后端开发", "Go工程师"],             2),
    (r"Python",                      ["Python后端开发"],                         1),

    # IM/长连接
    (r"IM|即时通讯|长连接|长链",     ["IM后端开发", "消息系统开发"],             1),

    # 管理
    (r"团队.{0,4}leader|技术负责人|研发经理|项目管理",
                                     ["技术负责人", "研发经理", "技术总监"],      1),
]

# 岗位级别推断（根据工作年限/职位）
SENIORITY_PREFIXES = ["高级", "资深", "专家级", "架构师"]


def strip_latex(text: str) -> str:
    """去除 LaTeX 命令，保留纯文本。"""
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[{}%]", " ", text)
    return text


def load_resume_text() -> str:
    """读取 content/ 下所有 .tex 文件（优先 release 版，跳过 dev/）。"""
    texts = []
    for tex_file in sorted(RESUME_CONTENT_DIR.glob("*.tex")):
        texts.append(tex_file.read_text(encoding="utf-8"))
    return "\n".join(texts)


def analyze_resume(resume_text: str) -> list[str]:
    """基于规则分析简历文本，返回推荐关键词列表（去重，按权重排序）。"""
    plain = strip_latex(resume_text)
    keyword_scores: dict[str, int] = {}

    for pattern, keywords, weight in TECH_TO_KEYWORD_RULES:
        if re.search(pattern, plain, re.IGNORECASE):
            for kw in keywords:
                keyword_scores[kw] = keyword_scores.get(kw, 0) + weight

    # 按权重降序，取 top 12
    sorted_kws = sorted(keyword_scores.items(), key=lambda x: -x[1])
    return [kw for kw, _ in sorted_kws[:12]]


def feedback_optimize(csv_path: Path, current_keywords: list[str]) -> list[str]:
    """
    基于爬取结果 CSV 优化关键词：
    - 统计每个搜索关键词的命中数
    - 命中数为 0 的关键词建议移除
    - 从命中岗位的标题中提取高频词，建议新增
    """
    if not csv_path.exists():
        console.print(f"[red]文件不存在: {csv_path}[/red]")
        return current_keywords

    rows = []
    with open(csv_path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        console.print("[yellow]CSV 为空，无法优化[/yellow]")
        return current_keywords

    # 从岗位标题提取高频词（2字以上中文词组）
    all_titles = " ".join(r.get("title", "") for r in rows)
    title_words = re.findall(r"[\u4e00-\u9fff]{2,6}|[A-Za-z+]{2,}", all_titles)
    freq = Counter(title_words)

    # 过滤掉太通用的词
    stop_words = {"工程师", "开发", "研发", "负责人", "专家", "高级", "资深", "架构师", "经理"}
    candidates = [
        w for w, c in freq.most_common(30)
        if c >= 2 and w not in stop_words and len(w) >= 2
    ]

    # 生成新关键词建议（已有的不重复添加）
    existing_set = set(current_keywords)
    new_suggestions = []
    for word in candidates:
        candidate_kw = f"{word}开发" if re.match(r"[\u4e00-\u9fff]", word) else word
        if candidate_kw not in existing_set:
            new_suggestions.append(candidate_kw)
        if len(new_suggestions) >= 5:
            break

    # 打印分析结果
    table = Table(title="岗位标题高频词（来自爬取结果）")
    table.add_column("词", style="cyan")
    table.add_column("出现次数", style="green")
    for w, c in freq.most_common(15):
        if w not in stop_words:
            table.add_row(w, str(c))
    console.print(table)

    if new_suggestions:
        console.print(f"\n[green]建议新增关键词：[/green] {new_suggestions}")
        updated = current_keywords + new_suggestions
        return updated[:15]  # 最多保留 15 个

    return current_keywords


def load_config() -> dict:
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return {}


def save_config(config: dict):
    CONFIG_FILE.write_text(
        json.dumps(config, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def print_keywords(keywords: list[str], title: str = "推荐关键词"):
    table = Table(title=title)
    table.add_column("#", style="dim")
    table.add_column("关键词", style="bold cyan")
    for i, kw in enumerate(keywords, 1):
        table.add_row(str(i), kw)
    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="简历关键词分析器")
    parser.add_argument("--dry-run", action="store_true", help="只打印推荐，不写入 config.json")
    parser.add_argument("--feedback", type=Path, metavar="CSV", help="基于爬取结果 CSV 优化关键词")
    args = parser.parse_args()

    config = load_config()

    if args.feedback:
        current = config.get("keywords", [])
        if not current:
            console.print("[yellow]config.json 中暂无关键词，先运行分析...[/yellow]")
            resume_text = load_resume_text()
            current = analyze_resume(resume_text)
        updated = feedback_optimize(args.feedback, current)
        print_keywords(updated, "优化后关键词")
        if not args.dry_run:
            config["keywords"] = updated
            save_config(config)
            console.print(f"[green]✓ 已更新 {CONFIG_FILE}[/green]")
        return

    # 分析简历
    console.print(f"[cyan]正在分析简历：{RESUME_CONTENT_DIR}[/cyan]")
    resume_text = load_resume_text()
    if not resume_text.strip():
        console.print("[red]未找到简历内容，请确认 content/*.tex 存在[/red]")
        return

    keywords = analyze_resume(resume_text)
    print_keywords(keywords, "基于简历分析的推荐关键词")

    if not args.dry_run:
        config["keywords"] = keywords
        save_config(config)
        console.print(f"\n[green]✓ 已写入 {CONFIG_FILE}[/green]")
        console.print("[dim]运行 python3 boss.py 开始搜索[/dim]")
    else:
        console.print("\n[yellow]--dry-run 模式，未写入 config.json[/yellow]")


if __name__ == "__main__":
    main()
