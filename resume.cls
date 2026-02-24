% ==============================
%  resume.cls 简历模板（类文件）
% ==============================
% 这个文件用于定义整份简历的“全局排版风格”：
% - 纸张与页边距（geometry）
% - 字体加载（fontspec / xeCJK 在 resume.tex/zh_CN-systemfonts.sty 中）
% - 标题样式（titlesec）
% - 列表间距（enumitem）
% - 常用宏：\name / \contactInfo / \datedsubsection ...
%
% 调参建议：
% - 想“更紧凑/更松”：优先调 enumitem 的 itemsep/topsep
% - 想“左右留白更多/更少”：调 geometry 的 left/right
% - 想“标题更醒目”：调 \titleformat 与 \titlespacing
%
% ------------------------------
% 基础概念速查（单位/优先级）
% ------------------------------
% 1) 常用长度单位：
% - pt：point，排版绝对单位（LaTeX 的基本长度单位之一）
% - pc：pica，1pc = 12pt（传统印刷单位）；例如 1.5pc = 18pt
% - in：英寸，1in ≈ 72.27pt
% - em：相对单位，1em ≈ 当前字体大小（字号变了，em 也跟着变）
%   用 em 的好处是“自适应”：字号变大，间距/缩进也按比例变大。
%
% 2) 配置覆盖/优先级（经验法则）：
% - 就近原则：越“具体”的设置越优先，例如
%   \setlist[itemize]{...} 会覆盖 \setlist{...} 的同名参数。
% - 显式设置优先：例如你同时写了
%   \setlist{noitemsep} 与 \setlist{itemsep=0.25em}
%   最终以 itemsep=0.25em 为准（因为它显式指定了 itemsep）。
%
% 3) itemize vs enumerate：
% - itemize：无序列表（圆点/符号）—— 简历里最常用
% - enumerate：有序列表（1/2/3 编号）—— 用于步骤、编号说明
%   所以这里分别写两行 \setlist[itemize] 与 \setlist[enumerate] 便于分别调参。

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}[2015/05/25 An elegant Résumé class]

% 继承 article 类：这里的 10pt 是全局基准字号
% - 如果想整体字号更大：可以改为 11pt / 12pt（会影响整篇密度）
\LoadClass[10pt]{article}

% ------------------------------
% 段落：全局禁用首行缩进
% - 简历常见做法：避免段首缩进导致视觉跳动
% ------------------------------
\setlength{\parindent}{0pt}
% ------------------------------
% 基础依赖：
% - xltxtra：XeLaTeX 的一些辅助宏
% - xifthen：提供 if-then 判断（下面 contactInfo 用到了 \ifthenelse）
% - fontawesome：图标（如 GitHub）
% - xcolor：颜色支持
% - fontspec：加载系统字体（仅 XeLaTeX/LuaLaTeX）
% ------------------------------
\RequirePackage{xltxtra}
\RequirePackage{xifthen}
\RequirePackage{fontawesome}
\RequirePackage[usenames,dvipsnames]{xcolor}
\RequirePackage{fontspec}
% ------------------------------
% 英文字体（主字体）
% - 这里只影响拉丁字母/数字等（中文字体在 zh_CN-systemfonts.sty 里由 xeCJK 控制）
% - Path/Extension/UprightFont 等配置，允许你放自定义字体文件到 fonts/Main/
% - 如果你不使用 fonts/Main/ 的自带字体，也可以改成系统字体名，例如：\setmainfont{Times New Roman}
% ------------------------------
\setmainfont[
  Path = fonts/Main/ ,
  Extension = .otf ,
  UprightFont = *-regular ,
  BoldFont = *-bold ,
  ItalicFont = *-italic ,
  BoldItalicFont = *-bolditalic ,
  SmallCapsFont = Fontin-SmallCaps
]{texgyretermes}

% ------------------------------
% 页面尺寸与页边距（A4）
% - left/right/top/bottom 控制四边留白
% - 想增加可写内容宽度：减小 left/right
% - 想更“呼吸感”：增大 left/right 或 top/bottom
% ------------------------------
\RequirePackage[
	a4paper,
	left=0.7in,
	right=0.7in,
	top=0.50in,
	bottom=0.5in,
	nohead
]{geometry}

% ------------------------------
% 标题样式（titlesec）
% 列表样式与间距（enumitem）
% ------------------------------
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage{tabularx}

% ------------------------------
% enumitem 常用参数说明（最常调的就是这些）
% ------------------------------
% - itemsep：item 与 item 之间的垂直间距（最常用）
% - topsep：整个列表与上下正文之间的垂直间距
% - parsep：item 内部“段落之间”的间距（通常简历用不到）
% - leftmargin：列表整体左缩进（影响圆点/编号位置与对齐感）
% - labelsep：圆点/编号 与正文之间的水平间距
% - labelwidth：label（圆点/编号）占用宽度
%
% 小技巧：
% - 想“更松”：增大 itemsep/topsep，例如 itemsep=0.3em
% - 想“更紧”：减小 itemsep/topsep，或使用 noitemsep/nosep
% - 想让列表更靠左、更整齐：减小 leftmargin（例如 1.2pc 或 1.2em）
% - 想控制某一个列表：也可以在具体环境上写
%   \begin{itemize}[itemsep=0.2em, topsep=0.1em]
%   这种写法的优先级最高（只影响这一处）。

% 列表“全局默认”选项：
% - noitemsep：压缩 item 与 item 之间的间距（itemsep=0）
% - nosep：压缩所有间距（itemsep/topsep/parsep 等都变小）
% 注意：下面你又显式设置了 itemsep=0.25em，会覆盖 noitemsep 的效果。
% 你可以二选一：
% - 紧凑：保留 noitemsep，并去掉 itemsep=...
% - 松一点：去掉 noitemsep，仅保留 itemsep/topsep
\setlist{noitemsep}
%\setlist{nosep}

% itemsep：每个 \item 之间的垂直间距（你要“item 之间稍微宽一点”主要就调它）
% 常用范围：0.15em ~ 0.4em
\setlist{itemsep=0.1em}

% topsep：列表整体与上下正文之间的间距
% leftmargin：列表缩进（调小会更“齐”，调大会更传统）
\setlist[itemize]{topsep=0.20em, leftmargin=1.5pc}
\setlist[enumerate]{topsep=0.20em, leftmargin=1.5pc}
\RequirePackage[super]{nth}

% ------------------------------
% 一级标题（\section）样式：如“工作经验 / 核心能力”
% - \Large：标题字号
% - \scshape：小型大写（对英文更明显；中文基本无影响）
% - \titlerule：标题下方横线
% - \titlespacing：控制标题前/后的垂直间距
%   格式：\titlespacing*{命令}{左缩进}{前间距}{后间距}
%   想让标题更紧凑：减小 {前间距}/{后间距}
% ------------------------------
\titleformat{\section}
  {\Large\heiti\raggedright}
  {}{0em}
  {}
  [\titlerule]
\titlespacing*{\section}{0cm}{*1}{*1}

% 二级标题（\subsection）样式：在本模板里主要给 datedsubsection 使用
% - 想让公司/职位行更紧凑：减小后间距 {*0.5}
\titleformat{\subsection}
  {\large\heiti\raggedright}
  {}{0em}
  {}
\titlespacing*{\subsection}{0cm}{*1}{*0.5}

% ------------------------------
% 常用宏：带日期的 section（很少用到；保留备用）
% 用法：\datedsection{标题}{右侧日期}
% ------------------------------
\newcommand{\datedsection}[2]{%
  \section[#1]{#1 \hfill #2}%
}

% \newcommand{\datedsubsection}[3]{%
%   \subsection[#1]{#1 \textit{#2} \hfill \textit{#3}}%
% }

\newcommand{\datedsubsection}[3]{%
  \subsection*{%
    \begin{tabularx}{\textwidth}{@{}lXr@{}}
    {\textbf{#1}} & {\textbf{#2}} & {\textbf{#3}} \\
    \end{tabularx}%
  }%
}

\newcommand{\thirdheading}[1]{%
  \vspace{0.2ex}%
  {\par\noindent{\heiti\bfseries\normalsize #1}\par}%
  \vspace{0.2ex}%
}


% 一行左右对齐：左边 #1，右边 #2
% 适合做“学校/学位/年份”等单行信息
\newcommand{\datedline}[2]{%
  {\par #1 \hfill #2 \par}%
}

% 简历姓名（页首大标题）
% - 想让名字更大：把 \Huge 改为 \huge 或更大（但注意可能换行）
% - 想让名字更紧凑：调 vspace 的数值
\newcommand{\resumename}{}
\newcommand{\name}[1]{
  \def\resumename{#1}
}

\newcommand{\headersep}{\hspace{0.6em}\textbar\hspace{0.6em}}

% 联系方式行（页首第二行）
% 说明：该宏负责渲染整段“页眉”信息（左侧三行信息 + 右侧姓名）。
%
% 参数（由 gen_resume_tex.py 从 resume_dev.md 的 YAML 头生成）：
% - #1 location（地点）
% - #2 experience（经验年限/一句话简介）
% - #3 tech_stack（技术栈）
% - #4 email（邮箱）
% - #5 phone（手机号）
% - #6 edu（学历信息，建议已包含学校/专业）
% - #7 birth（出生年份/年龄信息，如“1985 年生”）
%
% 版式结构：
% - 外层使用 tabularx 两列：左侧信息块（X 自动伸缩），右侧姓名块（固定宽度 p{...}）。
% - 左侧信息块内部再嵌一层 tabular：图标独立一列（固定宽度），文本一列；这样三行对齐更规整。
% - 分隔符使用 \headersep，统一“|”两侧的间距，避免肉眼不齐。
%
% 可调参数（排版微调入口）：
% - 右侧姓名列宽：tabularx 的 p{0.24\textwidth}（信息拥挤时可调小，如 0.22）。
% - 信息字号：\small（想更紧凑可改 \footnotesize，想更醒目可改 \normalsize）。
% - 左侧整体上移：\vspace{...} 负值（用于修正不同字体 ascent 导致的视觉顶边不齐）。
%
% 注意：这里使用 \parbox[t] + \vspace{0pt} 让左右两块“顶对齐”；
% 但字体自身的 ascent 不一致仍可能造成视觉偏差，因此保留上移微调量。
\newcommand{\contactInfo}[7]{
  \noindent
  \begin{tabularx}{\textwidth}{@{}X p{0.24\textwidth}@{}} % 左：信息块（自适应） 右：姓名（固定宽度）
    \parbox[t]{\hsize}{\raggedright\sffamily\small
      \vspace{0pt}% 顶对齐：避免按基线对齐导致左右上下错位
      \vspace{-0.8ex}% 视觉微调：把信息块整体上移一点，使其与右侧姓名块更齐
      \begin{tabular}[t]{@{}p{1.4em}l@{}} % 图标列宽：1.4em（可按需微调）
        {\faMapMarker} & {#1\headersep #2\headersep #3}\\[0.25ex]
        {\faEnvelopeO} & {#4\headersep \faPhone\ {#5}}\\[0.25ex]
        {\faGraduationCap} & {#6\headersep #7}\\
      \end{tabular}
    }
    &
    \parbox[t]{0.24\textwidth}{\raggedleft\fontsize{22}{24}\selectfont\scshape\vspace{0ex}\resumename\vspace{0pt}}
  \end{tabularx}
  % 联系方式行与正文之间的距离
  \vspace{0.7ex}
}

% role：用于“标题下的一行说明”（目前未必用到）
% - #1 通常为斜体前缀，#2 为正文
% - vspace 控制其与后文间距
\newcommand{\role}[2]{
  {\par \textit{#1} ~ #2 \par}
  \vspace{0.5ex}
}
