import re
import sys
from pathlib import Path


def parse_front_matter(md: str) -> tuple[dict, str]:
    lines = md.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, md

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break

    if end is None:
        return {}, md

    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1 :])

    data: dict[str, str] = {}
    for line in fm_lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if ":" not in s:
            continue
        k, v = s.split(":", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        data[k] = v

    return data, body


def escape_latex(s: str) -> str:
    s = s.replace("\\", r"\textbackslash{}")
    s = s.replace("{", r"\{").replace("}", r"\}")
    s = s.replace("&", r"\&")
    s = s.replace("%", r"\%")
    s = s.replace("$", r"\$")
    s = s.replace("#", r"\#")
    s = s.replace("_", r"\_")
    s = s.replace("~", r"\textasciitilde{}")
    s = s.replace("^", r"\textasciicircum{}")
    s = s.replace("<", r"$<$")
    s = s.replace(">", r"$>$")
    return s


def inline_md_to_tex(s: str) -> str:
    """Render a limited subset of inline Markdown.

    Currently supported:
    - **bold** -> \\textbf{...} (automatically uses BoldFont=heiti from font config)

    All other content is LaTeX-escaped.
    """

    if not s:
        return ""

    out: list[str] = []
    last = 0
    for m in re.finditer(r"\*\*(.+?)\*\*", s):
        if m.start() > last:
            out.append(escape_latex(s[last : m.start()]))
        out.append(r"\textbf{" + escape_latex(m.group(1).strip()) + "}")
        last = m.end()
    if last < len(s):
        out.append(escape_latex(s[last:]))
    return "".join(out)


def extract_year(birth: str) -> str:
    m = re.search(r"(19\d{2}|20\d{2})", birth)
    return m.group(1) if m else birth


def extract_edu_parts(edu: str) -> tuple[str, str]:
    # e.g. "硕士（中国海洋大学 · 通信与信息系统）"
    degree = edu
    university = ""

    m = re.match(r"([^（(]+)[（(](.+?)[）)]", edu)
    if m:
        degree = m.group(1).strip()
        inside = m.group(2)
        university = inside.split("·", 1)[0].strip()

    return university, degree


def normalize_dates(s: str) -> str:
    s = s.strip()
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", "", s)
    s = s.replace("至今", "至今")
    return s


def parse_job_heading(line: str) -> tuple[str, str, str]:
    # "## 闪捷信息 ｜ 安全技术专家 | 2022.04 – 至今"
    s = line.lstrip("#").strip()
    parts = [p.strip() for p in s.split("|")]
    left = parts[0] if parts else s
    dates = normalize_dates(parts[1]) if len(parts) >= 2 else ""

    # left: "公司 ｜ 职位"
    left_parts = [p.strip() for p in left.split("｜")]
    company = left_parts[0] if left_parts else left
    title = left_parts[1] if len(left_parts) >= 2 else ""

    return company, title, dates


def parse_kv_bullet(line: str) -> tuple[str, str] | None:
    # "* **挑战**：xxx" or "- **挑战**：xxx"
    m = re.match(r"^\s*[*-]\s*\*\*(.+?)\*\*[:：]\s*(.+)$", line.strip())
    if not m:
        return None
    return m.group(1).strip(), m.group(2).strip()


def collect_list(lines: list[str], start: int) -> tuple[list[str], int]:
    items: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() in ("---", "***"):
            break
        if line.startswith("#"):
            break
        if re.match(r"^\s*[*-]\s+", line):
            # Ignore stray list markers like "-" with no content.
            if re.match(r"^\s*[*-]\s*$", line):
                i += 1
                continue
            items.append(line)
            i += 1
            continue
        # non-list line means end of list block
        break
    return items, i


def generate_tex(md_path: Path, out_path: Path) -> None:
    md = md_path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(md)

    is_security_resume = "security" in md_path.name.lower()
    vspace_block = r"\vspace{0.10cm}" if is_security_resume else r"\vspace{0.2cm}"
    list_setstretch = r"    \setstretch{1.05}" if is_security_resume else r"    \setstretch{1.1}"

    name = fm.get("name", "")
    location = fm.get("location", "")
    experience = fm.get("experience", "")
    tech_stack = fm.get("tech_stack", "")
    phone = fm.get("phone", "")
    email = fm.get("email", "")
    edu = fm.get("edu", "")
    birth = fm.get("birth", "")

    university, degree = extract_edu_parts(edu) if edu else ("", "")
    birth_year = extract_year(birth) if birth else ""

    lines = [l.rstrip("\n") for l in body.splitlines()]

    # Extract sections we care about by headings
    def find_heading(h: str) -> int:
        for idx, ln in enumerate(lines):
            if ln.strip() == h:
                return idx
        return -1

    def find_heading_any(headings: list[str]) -> int:
        for h in headings:
            idx = find_heading(h)
            if idx != -1:
                return idx
        return -1

    idx_position = find_heading("# 职业定位")
    idx_core = find_heading("# 核心能力")
    idx_exp = find_heading("# 工作经历")
    idx_stack = find_heading_any(["# 技术栈 & 证书", "# 技术栈 & 资质"])
    idx_achieve = find_heading("# 代表性安全体系成果")

    position_title = ""
    position_para = ""
    if idx_position != -1:
        # title is next non-empty line, usually bold
        i = idx_position + 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines):
            position_title = lines[i].strip()
            i += 1
        # paragraph until separator/heading
        paras: list[str] = []
        while i < len(lines):
            ln = lines[i].strip()
            if not ln:
                i += 1
                continue
            if ln == "---" or ln.startswith("#"):
                break
            paras.append(ln)
            i += 1
        position_para = "".join(paras)

    core_items: list[tuple[str, str]] = []
    if idx_core != -1:
        i = idx_core + 1
        while i < len(lines):
            ln = lines[i].strip()
            if not ln:
                i += 1
                continue
            if ln == "---" or ln.startswith("#"):
                break
            kv = parse_kv_bullet(ln)
            if kv:
                core_items.append(kv)
            i += 1

    achievements_blocks = []
    if idx_achieve != -1:
        i = idx_achieve + 1
        while i < len(lines):
            cur = lines[i].strip()
            if not cur:
                i += 1
                continue
            if cur in ("---", "***") or cur.startswith("# "):
                break
            if cur.startswith("### "):
                block_title = cur.lstrip("#").strip()
                i += 1
                while i < len(lines):
                    ln = lines[i].strip()
                    if not ln or ln in ("---", "***") or ln.startswith("#"):
                        break
                    if re.match(r"^\s*[*-]\s+", ln):
                        break
                    i += 1
                list_lines, i2 = collect_list(lines, i)
                i = i2
                bullets = []
                for bl in list_lines:
                    kv = parse_kv_bullet(bl)
                    if kv:
                        bullets.append(kv)
                    else:
                        bullets.append(bl)
                achievements_blocks.append({"title": block_title, "bullets": bullets})
                continue
            i += 1

    # Work experiences
    jobs: list[dict] = []
    if idx_exp != -1:
        i = idx_exp + 1
        while i < len(lines):
            ln = lines[i].strip()
            if not ln:
                i += 1
                continue
            if ln == "---":
                i += 1
                continue
            if ln.startswith("# "):
                # next main section
                break
            if ln.startswith("## "):
                company, title, dates = parse_job_heading(ln)
                job = {
                    "company": company,
                    "title": title,
                    "dates": dates,
                    "blocks": [],
                }
                i += 1
                # optional "职责" line
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines) and lines[i].strip().startswith("**职责**"):
                    duty = re.sub(r"^\*\*职责\*\*[:：]\s*", "", lines[i].strip())
                    job["duty"] = duty
                    i += 1
                else:
                    job["duty"] = ""

                # parse blocks until next job/section
                while i < len(lines):
                    cur = lines[i].strip()
                    if not cur:
                        i += 1
                        continue
                    if cur in ("---", "***"):
                        i += 1
                        continue
                    if cur.startswith("## ") or cur.startswith("# "):
                        break
                    if cur.startswith("### "):
                        block_title = cur.lstrip("#").strip()
                        i += 1
                        # Skip any non-list lines (paragraph text, bold headers, etc.) until we find a list
                        while i < len(lines):
                            ln = lines[i].strip()
                            if not ln or ln in ("---", "***"):
                                i += 1
                                continue
                            if ln.startswith("## ") or ln.startswith("# ") or ln.startswith("### "):
                                break
                            if re.match(r"^\s*[*-]\s+", lines[i]):
                                # Found the list
                                break
                            # Skip this non-list line
                            i += 1
                        
                        list_lines, i2 = collect_list(lines, i)
                        i = i2
                        bullets: list[tuple[str, str] | str] = []
                        for bl in list_lines:
                            kv = parse_kv_bullet(bl)
                            if kv:
                                bullets.append(kv)
                            else:
                                bullets.append(bl)
                        job["blocks"].append({"title": block_title, "bullets": bullets})
                        continue
                    # If not a ### block, try list items directly
                    if re.match(r"^\s*[*-]\s+", lines[i]):
                        list_lines, i2 = collect_list(lines, i)
                        i = i2
                        bullets: list[tuple[str, str] | str] = []
                        for bl in list_lines:
                            kv = parse_kv_bullet(bl)
                            if kv:
                                bullets.append(kv)
                            else:
                                bullets.append(bl)
                        job["blocks"].append({"title": "", "bullets": bullets})
                        continue

                    # otherwise ignore standalone lines for now
                    i += 1

                jobs.append(job)
                continue

            i += 1

    stack_items: list[tuple[str, str]] = []
    if idx_stack != -1:
        i = idx_stack + 1
        while i < len(lines):
            ln = lines[i].strip()
            if not ln:
                i += 1
                continue
            if ln == "---" or ln.startswith("#"):
                break
            kv = parse_kv_bullet(ln)
            if kv:
                stack_items.append(kv)
            i += 1

    # ---- Emit LaTeX ----
    out: list[str] = []
    out.append(r"\pagenumbering{gobble}")
    out.append("")
    if name:
        out.append(r"\name{" + escape_latex(name) + "}")
        out.append("")

    if (
        location
        or experience
        or tech_stack
        or phone
        or email
        or edu
        or birth
        or university
        or degree
        or birth_year
    ):
        out.append(
            r"\contactInfo{"
            + escape_latex(location)
            + "}{"
            + escape_latex(experience)
            + "}{"
            + escape_latex(tech_stack)
            + "}{"
            + escape_latex(email)
            + "}{"
            + escape_latex(phone)
            + "}{"
            + escape_latex(edu)
            + "}{"
            + escape_latex(birth)
            + "}"
        )
        out.append("")

    # 职业定位
    out.append(r"\section{职业定位}")
    out.append("")
    out.append(r"\sloppy")
    if position_title:
        # strip ** **
        t = position_title
        t = re.sub(r"^\*\*(.+)\*\*$", r"\1", t)
        out.append(r"\textbf{" + escape_latex(t) + "}")
        out.append("")
    if position_para:
        out.append(inline_md_to_tex(position_para))
        out.append("")

    out.append(vspace_block)
    out.append("")

    # 核心能力
    out.append(r"\section{核心能力}")
    if core_items:
        out.append(r"\begin{itemize}[parsep=0.2ex]")
        out.append(list_setstretch)
        for k, v in core_items:
            out.append(
                "  "
                + r"\item "
                + r"\textbf{" + escape_latex(k) + "}: "
                + inline_md_to_tex(v)
            )
        out.append(r"\end{itemize}")
    out.append("")
    out.append(vspace_block)
    out.append("")

    # 代表性安全体系成果
    if achievements_blocks:
        out.append(r"\section{代表性安全体系成果}")
        out.append(vspace_block)
        out.append("")
        for block in achievements_blocks:
            bt = block.get("title", "")
            if bt:
                out.append(r"\thirdheading{" + inline_md_to_tex(bt) + "}")
            out.append(r"\begin{itemize}")
            out.append(list_setstretch)
            for b in block.get("bullets", []):
                if isinstance(b, tuple):
                    k, v = b
                    out.append("    " + r"\item " + r"\textbf{" + escape_latex(k) + "}: " + inline_md_to_tex(v))
                else:
                    txt = re.sub(r"^\s*[*-]\s+", "", b.strip())
                    if not txt or txt == "-":
                        continue
                    out.append("    " + r"\item " + inline_md_to_tex(txt))
            out.append(r"\end{itemize}")
            out.append("")
        out.append(vspace_block)
        out.append("")

    # 工作经历
    out.append(r"\section{工作经验}")
    out.append(vspace_block)
    out.append("")

    for job in jobs:
        company = escape_latex(job["company"])
        title = escape_latex(job.get("title", ""))
        dates = escape_latex(job.get("dates", ""))
        # date in md like 2022.04-至今 -> keep as-is
        out.append(r"\datedsubsection{" + company + "}{" + title + "}{" + dates + "}")
        out.append("")
        duty = job.get("duty", "")
        if duty:
            out.append(inline_md_to_tex(duty))
            out.append("")

        for block in job["blocks"]:
            bt = block.get("title", "").strip()
            bullets_raw = block.get("bullets", [])
            if not bullets_raw:
                continue
            if bt:
                out.append(r"\thirdheading{" + inline_md_to_tex(bt) + "}")
            out.append(r"\begin{itemize}")
            out.append(list_setstretch)
            for b in bullets_raw:
                if isinstance(b, tuple):
                    k, v = b
                    out.append(
                        "    "
                        + r"\item "
                        + r"\textbf{" + escape_latex(k) + "}: "
                        + inline_md_to_tex(v)
                    )
                else:
                    txt = re.sub(r"^\s*[*-]\s+", "", b.strip())
                    if not txt or txt == "-":
                        continue
                    out.append("    " + r"\item " + inline_md_to_tex(txt))
            out.append(r"\end{itemize}")
            out.append("")

        out.append(vspace_block)
        out.append("")

    # 技术栈 & 证书
    out.append(r"\section{技术栈 \& 证书}")
    if stack_items:
        out.append(r"\begin{itemize}[parsep=0.2ex]")
        out.append(list_setstretch)
        for k, v in stack_items:
            out.append(
                "  "
                + r"\item "
                + r"\textbf{" + escape_latex(k) + "}: "
                + inline_md_to_tex(v)
            )
        out.append(r"\end{itemize}")
    out.append("")
    out.append(vspace_block)
    out.append("")

    # 教育背景：MD 目前没有结构化明细，沿用固定版式
    out.append(r"\section{教育背景}")
    out.append(r"\begin{tabularx}{\textwidth}{@{\extracolsep{\fill}}X X X X@{}}")
    out.append(r"  \textbf{中国海洋大学} & \textit{通信与信息系统} & \textit{硕士} & \textit{2007.9 - 2010.6} \\")
    out.append(r"  \textbf{怀化学院} & \textit{电子信息科学与技术} & \textit{本科} & \textit{2003.9 - 2007.6} \\")
    out.append(r"\end{tabularx}")
    out.append("")

    out_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python3 gen_resume_tex.py <resume_dev.md> <resume.tex>")

    md_path = Path(sys.argv[1]).resolve()
    out_path = Path(sys.argv[2]).resolve()

    generate_tex(md_path, out_path)


if __name__ == "__main__":
    main()
