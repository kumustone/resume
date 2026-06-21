#!/usr/bin/env python3
"""
YAML → LaTeX 转换脚本
读取 resume/data/resume.yaml，生成 LaTeX content/*.tex 文件

用法:
    python scripts/yaml-to-latex.py

输出:
    resume/latex/content/resume.tex
    resume/latex/content/resume_security.tex
"""

import yaml
import sys
from pathlib import Path

# 路径配置
PROJECT_ROOT = Path(__file__).parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "resume.yaml"
LATEX_CONTENT_DIR = PROJECT_ROOT / "content"


def escape_latex(text: str) -> str:
    """转义 LaTeX 特殊字符"""
    replacements = [
        ("\\", "\\textbackslash{}"),
        ("&", "\\&"),
        ("%", "\\%"),
        ("$", "\\$"),
        ("#", "\\#"),
        ("_", "\\_"),
        ("{", "\\{"),
        ("}", "\\}"),
        ("~", "\\textasciitilde{}"),
        ("^", "\\textasciicircum{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def render_profile(data: dict) -> str:
    """渲染页眉个人信息"""
    p = data["profile"]
    return (
        f"\\name{{{p['name']}}}\n\n"
        f"\\contactInfo{{{p['location']}}}"
        f"{{{p['experience_summary']}}}"
        f"{{{p['tech_stack']}}}"
        f"{{{p['email']}}}"
        f"{{{p['phone']}}}"
        f"{{{p['education']}}}"
        f"{{{p['birth_year']}}}"
    )


def render_summary(summary_text: str, direction: str) -> str:
    """渲染个人简介/职业定位"""
    if direction == "security":
        title = "职业定位"
        # 安全方向有标题行和段落
        lines = summary_text.strip().split("\n")
        title_line = lines[0].strip()
        body = "\\n".join(lines[2:]).strip() if len(lines) > 2 else ""
        return (
            f"\\section{{{title}}}\n\n"
            f"\\sloppy\n"
            f"\\textbf{{{escape_latex(title_line)}}}\n\n"
            f"{escape_latex(body)}"
        )
    else:
        title = "个人简介"
        return (
            f"\\section{{{title}}}\n\n"
            f"\\sloppy\n"
            f"{escape_latex(summary_text.strip())}"
        )


def render_core_skills(skills: list, direction: str) -> str:
    """渲染核心能力"""
    lines = ["\\section{核心能力}", "\\begin{itemize}[parsep=0.2ex]"]

    if direction == "gateway":
        lines.append("    \\setstretch{1.1}")
    else:
        lines.append("    \\setstretch{1.05}")

    for skill in skills:
        title = escape_latex(skill["title"])
        details = escape_latex(skill["details"])
        lines.append(f"  \\item \\textbf{{{title}}}: {details}")

    lines.append("\\end{itemize}")
    return "\n".join(lines)


def render_experience(experiences: list, direction: str) -> str:
    """渲染工作经历"""
    lines = ["\\section{工作经验}"]

    if direction == "gateway":
        lines.append("\\vspace{0.2cm}")
    else:
        lines.append("\\vspace{0.10cm}")

    for exp in experiences:
        role_key = f"role_{direction}"
        role = exp.get(role_key, exp["role_gateway"])

        lines.append("")
        lines.append(f"\\datedsubsection{{{escape_latex(exp['company'])}}}{{{escape_latex(role)}}}{{{exp['period']}}}")

        # 过滤出该方向的项目
        direction_projects = [
            p for p in exp["projects"]
            if direction in p.get("direction", ["gateway"])
        ]

        for proj in direction_projects:
            lines.append("")
            lines.append(f"\\thirdheading{{{escape_latex(proj['name'])}}}")
            lines.append("\\begin{itemize}")

            if direction == "gateway":
                lines.append("    \\setstretch{1.1}")
            else:
                lines.append("    \\setstretch{1.05}")

            for highlight in proj["highlights"]:
                # 处理 "标题：内容" 格式
                if "：" in highlight:
                    parts = highlight.split("：", 1)
                    title = escape_latex(parts[0])
                    content = escape_latex(parts[1])
                    lines.append(f"    \\item \\textbf{{{title}}}: {content}")
                else:
                    lines.append(f"    \\item {escape_latex(highlight)}")

            lines.append("\\end{itemize}")

        if direction == "gateway":
            lines.append("\\vspace{0.2cm}")
        else:
            lines.append("\\vspace{0.10cm}")

    return "\n".join(lines)


def render_tech_stack(data: dict, direction: str) -> str:
    """渲染技术栈与证书"""
    ts = data["tech_stack"]

    lines = ["\\section{技术栈 \\& 证书}"]

    if direction == "security":
        lines.append("")
        lines.append("\\vspace{0.10cm}")

    lines.append("\\begin{itemize}[parsep=0.2ex]")

    if direction == "gateway":
        lines.append("    \\setstretch{1.1}")
    else:
        lines.append("    \\setstretch{1.05}")

    lines.append(f"  \\item \\textbf{{核心语言}}: \\textbf{{{escape_latex(ts['languages'])}}}")
    lines.append(f"  \\item \\textbf{{系统底座}}: {escape_latex(ts['systems'])}")
    lines.append(f"  \\item \\textbf{{数据组件}}: {escape_latex(ts['data'])}")
    lines.append(f"  \\item \\textbf{{专业资质}}: \\textbf{{{escape_latex(ts['certifications'])}}}")
    lines.append(f"  \\item \\textbf{{荣誉奖励}}: {escape_latex(ts['honors'])}")
    lines.append(f"  \\item \\textbf{{核心标签}}: {escape_latex(ts['tags'])}")

    lines.append("\\end{itemize}")

    if direction == "gateway":
        lines.append("\\vspace{0.2cm}")

    return "\n".join(lines)


def render_education(education: list) -> str:
    """渲染教育背景"""
    lines = ["\\section{教育背景}"]
    lines.append("\\begin{tabularx}{\\textwidth}{@{\\extracolsep{\\fill}}X X X X@{}}")

    for edu in education:
        school = escape_latex(edu["school"])
        major = escape_latex(edu["major"])
        degree = escape_latex(edu["degree"])
        period = escape_latex(edu["period"])
        lines.append(
            f"  \\textbf{{{school}}} & \\textit{{{major}}} & \\textit{{{degree}}} & \\textit{{{period}}} \\\\"
        )

    lines.append("\\end{tabularx}")
    return "\n".join(lines)


def generate_latex(data: dict, direction: str) -> str:
    """生成完整 LaTeX 内容文件"""
    parts = [
        "\\pagenumbering{gobble}",
        "",
        render_profile(data),
        "",
        render_summary(data["summary"][direction], direction),
        "",
        "\\vspace{0.2cm}" if direction == "gateway" else "\\vspace{0.10cm}",
        "",
        render_core_skills(data["core_skills"][direction], direction),
        "",
        "\\vspace{0.2cm}" if direction == "gateway" else "\\vspace{0.10cm}",
        "",
        render_experience(data["experience"], direction),
        "",
        render_tech_stack(data, direction),
        "",
        "\\vspace{0.2cm}" if direction == "gateway" else "",
        "",
        render_education(data["education"]),
    ]

    return "\n".join(parts)


def main():
    # 确保输出目录存在
    LATEX_CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # 读取 YAML
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # 生成两个方向的 LaTeX 内容
    for direction in ["gateway", "security"]:
        output_file = LATEX_CONTENT_DIR / f"resume_{direction}.tex"
        content = generate_latex(data, direction)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Generated: {output_file}")

    # 同时生成兼容旧命名的文件
    # resume.tex → gateway, resume_security.tex → security
    (LATEX_CONTENT_DIR / "resume.tex").write_text(
        generate_latex(data, "gateway"), encoding="utf-8"
    )
    (LATEX_CONTENT_DIR / "resume_security.tex").write_text(
        generate_latex(data, "security"), encoding="utf-8"
    )
    print(f"Generated: {LATEX_CONTENT_DIR / 'resume.tex'}")
    print(f"Generated: {LATEX_CONTENT_DIR / 'resume_security.tex'}")


if __name__ == "__main__":
    main()
