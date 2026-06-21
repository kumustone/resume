#!/usr/bin/env node
/**
 * YAML → HTML 转换脚本
 * 读取 resume/data/resume.yaml，生成 HTML 文件
 *
 * 用法:
 *   node js/yaml-to-html.js
 *
 * 输出:
 *   html/output/resume_gateway.html
 *   html/output/resume_security.html
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const Mustache = require('mustache');

// 路径配置
const PROJECT_ROOT = path.resolve(__dirname, '..', '..');
const DATA_FILE = path.join(PROJECT_ROOT, 'data', 'resume.yaml');
const TEMPLATE_FILE = path.join(PROJECT_ROOT, 'html', 'template', 'resume.html');
const CSS_FILE = path.join(PROJECT_ROOT, 'html', 'css', 'resume.css');
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'html', 'output');

// 确保输出目录存在
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

// 读取模板
const template = fs.readFileSync(TEMPLATE_FILE, 'utf-8');

// 读取 CSS（内联到 HTML 中，避免外部文件依赖）
const cssContent = fs.readFileSync(CSS_FILE, 'utf-8');

// 读取 YAML 数据
const yamlContent = fs.readFileSync(DATA_FILE, 'utf-8');
const data = yaml.load(yamlContent);

/**
 * 处理高亮文本，将 "标题：内容" 转为加粗格式
 */
function processHighlight(text) {
  // 匹配 "标题：内容" 格式，将标题加粗
  return text.replace(/^(.+?)：(.+)$/, '<strong>$1</strong>：$2');
}

/**
 * 为指定方向生成 HTML
 */
function generateHTML(direction) {
  const profile = data.profile;
  const summary = data.summary[direction];
  const skills = data.core_skills[direction];
  const experiences = data.experience;

  // 处理摘要
  const summaryLines = summary.trim().split('\n').filter(l => l.trim());
  let summaryTitle = direction === 'security' ? '职业定位' : '个人简介';
  let summaryHasTitle = false;
  let summaryTitleLine = '';
  let summaryBody = '';

  if (direction === 'security' && summaryLines.length > 0) {
    summaryHasTitle = true;
    summaryTitleLine = summaryLines[0].trim();
    summaryBody = summaryLines.slice(2).join('\n').trim();
  } else {
    summaryBody = summary.trim();
  }

  // 处理工作经历：过滤该方向的项目
  const processedExperiences = experiences.map(exp => {
    const role = exp[`role_${direction}`] || exp.role_gateway;

    // 过滤项目
    const directionProjects = exp.projects.filter(
      p => p.direction && p.direction.includes(direction)
    );

    const processedProjects = directionProjects.map(proj => ({
      name: proj.name,
      highlights: proj.highlights.map(h => processHighlight(h))
    }));

    return {
      company: exp.company,
      role: role,
      period: exp.period,
      projects: processedProjects
    };
  }).filter(exp => exp.projects.length > 0);

  // 构建 Mustache 数据
  const view = {
    // 个人资料
    name: profile.name,
    location: profile.location,
    experience_summary: profile.experience_summary,
    tech_stack: profile.tech_stack,
    email: profile.email,
    phone: profile.phone,
    education: profile.education,
    birth_year: '',

    // 摘要
    summary_title: summaryTitle,
    summary_has_title: summaryHasTitle,
    summary_title_line: summaryTitleLine,
    summary_body: summaryBody.replace(/\n/g, '<br>'),

    // 核心能力
    core_skills: skills,

    // 工作经历
    experiences: processedExperiences,

    // 技术栈
    tech_languages: data.tech_stack.languages,
    tech_systems: data.tech_stack.systems,
    tech_ai_llm: data.tech_stack.ai_llm || '',
    tech_data: data.tech_stack.data,
    tech_certifications: data.tech_stack.certifications,
    tech_honors: data.tech_stack.honors,

    // 教育背景列表
    education_list: data.education
  };

  // 渲染 HTML
  let html = Mustache.render(template, view);

  // 内联 CSS
  const bodyClass = direction === 'security' ? 'security' : 'gateway';
  html = html.replace(
    '<link rel="stylesheet" href="../css/resume.css">',
    `<style>\n${cssContent}\n</style>`
  );
  html = html.replace('<body>', `<body class="${bodyClass}">`);

  return html;
}

// 生成两个方向
for (const direction of ['gateway', 'security']) {
  const html = generateHTML(direction);
  const outputFile = path.join(OUTPUT_DIR, `resume_${direction}.html`);
  fs.writeFileSync(outputFile, html, 'utf-8');
  console.log(`Generated: ${outputFile}`);
}

console.log('HTML generation complete!');
