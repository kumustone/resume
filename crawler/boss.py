#!/usr/bin/env python3
"""
Boss直聘岗位爬虫
使用方式：
  1. 首次运行会打开浏览器，手动扫码登录
  2. 登录后 session 保存到 .auth/boss_state.json，后续无需重复登录
  3. 结果输出到 output/jobs_<timestamp>.csv 和终端表格

用法：
  python3 boss.py                    # 从 config.json 读取关键词搜索
  python3 boss.py --keywords "安全架构师" "API网关" --city 上海  # 临时覆盖关键词
  python3 boss.py --login            # 强制重新登录

关键词管理：
  python3 keyword_advisor.py         # 分析简历，自动生成关键词写入 config.json
  python3 keyword_advisor.py --feedback output/jobs_xxx.csv  # 基于结果优化关键词
"""

import argparse
import asyncio
import csv
import json
import random
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright
from rich.console import Console
from rich.table import Table

console = Console()

CRAWLER_DIR = Path(__file__).parent
CONFIG_FILE = CRAWLER_DIR / "config.json"

# ── 配置加载 ──────────────────────────────────────────────────────────────────
def load_config() -> dict:
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return {}


CITY_MAP = {
    "全国": "100010000",
    "北京": "101010100",
    "上海": "101020100",
    "深圳": "101280600",
    "杭州": "101210100",
    "广州": "101280100",
    "新加坡": "102600100",
}

AUTH_DIR = CRAWLER_DIR / ".auth"
OUTPUT_DIR = CRAWLER_DIR / "output"
STATE_FILE = AUTH_DIR / "boss_state.json"

BOSS_BASE = "https://www.zhipin.com"
# ──────────────────────────────────────────────────────────────────────────────


def build_search_url(keyword: str, city_code: str, page: int = 1) -> str:
    return (
        f"{BOSS_BASE}/web/geek/job"
        f"?query={keyword}&city={city_code}&page={page}"
    )


# Boss直聘风控/验证码的常见选择器
CAPTCHA_SELECTORS = [
    ".verify-wrap",          # 滑块验证
    ".tc-vcode",             # 图形验证码
    "#captcha_div",          # 通用验证
    ".boss-popup__content",  # 弹窗拦截
    "text=安全验证",
    "text=请完成安全验证",
    "text=访问频率过高",
]


async def wait_for_captcha_if_needed(page, url: str) -> bool:
    """
    检测页面是否触发风控/验证码。
    如果触发，打印提示并阻塞等待用户在浏览器中手动完成验证，
    然后重新加载目标页面，返回 True 表示发生了验证。
    """
    for selector in CAPTCHA_SELECTORS:
        try:
            if await page.locator(selector).count() > 0:
                console.print(
                    f"\n[bold red]⚠ 触发风控验证！[/bold red]\n"
                    f"请在弹出的浏览器窗口中完成验证，完成后回到终端按 [bold]Enter[/bold] 继续..."
                )
                input()
                console.print("[yellow]正在重新加载页面...[/yellow]")
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await page.wait_for_timeout(2000)
                return True
        except Exception:
            pass
    return False


def is_relevant(title: str, description: str, match_kws: list[str], exclude_kws: list[str]) -> bool:
    text = title + description
    if any(ex in title for ex in exclude_kws):
        return False
    return any(kw.lower() in text.lower() for kw in match_kws)


async def login(playwright):
    """打开浏览器让用户手动扫码登录，完成后保存 session。"""
    AUTH_DIR.mkdir(exist_ok=True)
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    console.print("[yellow]正在打开 Boss直聘，请扫码登录...[/yellow]")
    await page.goto(f"{BOSS_BASE}/web/user/?ka=header-login")

    console.print("[yellow]登录完成后请按 Enter 继续...[/yellow]")
    input()

    await context.storage_state(path=str(STATE_FILE))
    console.print(f"[green]✓ 登录状态已保存到 {STATE_FILE}[/green]")
    await browser.close()


async def scrape_jobs(
    keywords: list[str],
    city: str,
    max_pages: int,
    headless: bool,
    match_kws: list[str],
    exclude_kws: list[str],
    delay: dict,
) -> tuple[list[dict], dict[str, int]]:
    city_code = CITY_MAP.get(city, CITY_MAP["全国"])
    jobs = []
    seen_ids = set()
    keyword_hits: dict[str, int] = defaultdict(int)

    async with async_playwright() as playwright:
        if not STATE_FILE.exists():
            console.print("[red]未找到登录状态，正在启动登录流程...[/red]")
            await login(playwright)

        # headless 模式会被 Boss直聘识别，强制使用有头模式
        browser = await playwright.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        context = await browser.new_context(
            storage_state=str(STATE_FILE),
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
        )
        page = await context.new_page()
        # 清除 webdriver 标志，避免被 JS 检测
        await page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        for keyword in keywords:
            console.print(f"\n[cyan]搜索关键词：{keyword} | 城市：{city}[/cyan]")

            for page_num in range(1, max_pages + 1):
                url = build_search_url(keyword, city_code, page_num)
                console.print(f"  第 {page_num} 页: {url}")

                try:
                    await page.goto(url, wait_until="networkidle", timeout=30000)
                    await page.wait_for_timeout(2000)

                    # 检测风控/验证码，阻塞直到用户完成验证
                    await wait_for_captcha_if_needed(page, url)

                    # 检测是否登录失效
                    if await page.locator(".login-btn").count() > 0:
                        console.print("[red]  ⚠ 登录已失效，请重新运行 --login[/red]")
                        break

                    job_cards = await page.locator(".job-card-wrapper").all()
                    if not job_cards:
                        # 可能是静默风控（不弹验证码，直接返回空页面）
                        console.print(
                            "  [yellow]未找到岗位卡片。\n"
                            "  请检查浏览器窗口：\n"
                            "  - 若有验证码/风控提示，完成后按 Enter 重试\n"
                            "  - 若页面确实无结果，直接按 Enter 跳过[/yellow]"
                        )
                        user_input = input("  [Enter继续 / r+Enter重试] > ").strip().lower()
                        if user_input == "r":
                            await wait_for_captcha_if_needed(page, url)
                            job_cards = await page.locator(".job-card-wrapper").all()
                        if not job_cards:
                            console.print("  确认无结果，停止翻页")
                            break

                    for card in job_cards:
                        try:
                            job = await parse_card(card)
                            if job and job["id"] not in seen_ids:
                                if is_relevant(job["title"], job.get("tags", ""), match_kws, exclude_kws):
                                    seen_ids.add(job["id"])
                                    job["search_keyword"] = keyword
                                    jobs.append(job)
                                    keyword_hits[keyword] += 1
                                    console.print(
                                        f"  [green]✓[/green] {job['title']} | "
                                        f"{job['company']} | {job['salary']}"
                                    )
                        except Exception as e:
                            console.print(f"  [dim]解析卡片失败: {e}[/dim]")

                    # 翻页间延迟
                    page_wait = random.randint(
                        delay.get("page_min", 4) * 1000,
                        delay.get("page_max", 8) * 1000,
                    )
                    console.print(f"  [dim]等待 {page_wait // 1000}s...[/dim]")
                    await page.wait_for_timeout(page_wait)

                except Exception as e:
                    console.print(f"  [red]页面加载失败: {e}[/red]")
                    break

            # 关键词间延迟（比翻页延迟更长）
            if keyword != keywords[-1]:
                kw_wait = random.randint(
                    delay.get("keyword_min", 8) * 1000,
                    delay.get("keyword_max", 15) * 1000,
                )
                console.print(f"\n[dim]切换关键词，等待 {kw_wait // 1000}s...[/dim]")
                await page.wait_for_timeout(kw_wait)

        await browser.close()

    return jobs, dict(keyword_hits)


async def parse_card(card) -> dict | None:
    """从岗位卡片中提取结构化数据。"""
    try:
        # 岗位链接和 ID
        link_el = card.locator("a.job-card-left").first
        href = await link_el.get_attribute("href") or ""
        job_id = re.search(r"/job_detail/([^.]+)\.html", href)
        job_id = job_id.group(1) if job_id else href

        title = await card.locator(".job-name").first.inner_text()
        salary = await card.locator(".salary").first.inner_text()
        company = await card.locator(".company-name").first.inner_text()

        # 城市/经验/学历
        job_info = await card.locator(".job-info .tag-list").first.inner_text()

        # 公司标签（融资阶段、规模等）
        company_tags = ""
        company_tag_els = await card.locator(".company-tag-list").all()
        if company_tag_els:
            company_tags = await company_tag_els[0].inner_text()

        return {
            "id": job_id,
            "title": title.strip(),
            "salary": salary.strip(),
            "company": company.strip(),
            "info": job_info.strip().replace("\n", " / "),
            "tags": company_tags.strip().replace("\n", " / "),
            "url": BOSS_BASE + href if href.startswith("/") else href,
            "crawled_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    except Exception:
        return None


def save_csv(jobs: list[dict], output_dir: Path) -> Path:
    output_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = output_dir / f"jobs_{ts}.csv"
    if not jobs:
        return path
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
        writer.writeheader()
        writer.writerows(jobs)
    return path


def print_table(jobs: list[dict]):
    table = Table(title=f"匹配岗位（共 {len(jobs)} 条）", show_lines=True)
    table.add_column("岗位", style="bold cyan", max_width=26)
    table.add_column("薪资", style="green", max_width=14)
    table.add_column("公司", max_width=18)
    table.add_column("信息", max_width=22)
    table.add_column("搜索词", style="dim", max_width=16)
    for j in jobs:
        table.add_row(j["title"], j["salary"], j["company"], j["info"], j.get("search_keyword", ""))
    console.print(table)


def print_keyword_stats(keyword_hits: dict[str, int], all_keywords: list[str]):
    table = Table(title="关键词命中统计")
    table.add_column("关键词", style="cyan")
    table.add_column("命中数", style="green", justify="right")
    table.add_column("建议", style="yellow")
    for kw in all_keywords:
        hits = keyword_hits.get(kw, 0)
        suggestion = "[red]考虑移除或替换[/red]" if hits == 0 else ""
        table.add_row(kw, str(hits), suggestion)
    console.print(table)
    zero_hit = [kw for kw in all_keywords if keyword_hits.get(kw, 0) == 0]
    if zero_hit:
        console.print(f"[dim]提示：运行 python3 keyword_advisor.py --feedback <csv> 可自动优化关键词[/dim]")


def parse_args():
    parser = argparse.ArgumentParser(description="Boss直聘岗位爬虫")
    parser.add_argument(
        "--keywords", nargs="+", default=None,
        help="临时覆盖搜索关键词（默认从 config.json 读取）"
    )
    parser.add_argument(
        "--city", default=None,
        choices=list(CITY_MAP.keys()),
        help="目标城市（默认从 config.json 读取）"
    )
    parser.add_argument(
        "--pages", type=int, default=None,
        help="每个关键词最多爬取页数（默认从 config.json 读取，fallback 3）"
    )
    parser.add_argument(
        "--login", action="store_true",
        help="强制重新登录"
    )
    parser.add_argument(
        "--show-browser", action="store_true",
        help="显示浏览器窗口（调试用）"
    )
    return parser.parse_args()


async def main():
    args = parse_args()
    config = load_config()

    # 关键词优先级：命令行 > config.json > 提示用户先运行 advisor
    keywords = args.keywords or config.get("keywords") or []
    if not keywords:
        console.print(
            "[red]未找到关键词！请先运行：[/red]\n"
            "  python3 keyword_advisor.py\n"
            "或使用 --keywords 临时指定"
        )
        return

    city = args.city or config.get("city", "全国")
    max_pages = args.pages or config.get("max_pages", 3)
    match_kws = config.get("match_keywords", ["安全", "网关", "WAF", "API", "C++", "Golang"])
    exclude_kws = config.get("exclude_keywords", ["实习", "外包", "派遣"])

    console.print(f"[cyan]关键词来源：{'命令行' if args.keywords else 'config.json'}[/cyan]")
    console.print(f"[cyan]关键词列表：{keywords}[/cyan]")
    console.print(f"[cyan]城市：{city} | 每词最多 {max_pages} 页[/cyan]\n")

    if args.login and STATE_FILE.exists():
        STATE_FILE.unlink()
        console.print("[yellow]已清除旧登录状态[/yellow]")

    if not STATE_FILE.exists() or args.login:
        async with async_playwright() as p:
            await login(p)

    delay = config.get("delay", {})

    jobs, keyword_hits = await scrape_jobs(
        keywords=keywords,
        city=city,
        max_pages=max_pages,
        headless=not args.show_browser,
        match_kws=match_kws,
        exclude_kws=exclude_kws,
        delay=delay,
    )

    if not jobs:
        console.print("[red]未找到匹配岗位[/red]")
        print_keyword_stats(keyword_hits, keywords)
        return

    print_table(jobs)
    print_keyword_stats(keyword_hits, keywords)

    csv_path = save_csv(jobs, OUTPUT_DIR)
    console.print(f"\n[green]✓ 结果已保存到 {csv_path}[/green]")
    console.print(f"[dim]优化关键词：python3 keyword_advisor.py --feedback {csv_path}[/dim]")


if __name__ == "__main__":
    asyncio.run(main())
