#!/usr/bin/env node
/**
 * YAML → HTML 转换脚本
 * 读取 resume/data/resume.yaml，生成 HTML 文件
 *
 * 用法:
 *   node js/yaml-to-html.js
 *
 * 输出:
 *   html/output/resume.html
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const Mustache = require('mustache');

// 路径配置
const PROJECT_ROOT = path.resolve(__dirname, '..', '..');
const DATA_FILE = path.join(PROJECT_ROOT, 'data', 'resume.yaml');
const TEMPLATE_FILE = path.join(PROJECT_ROOT, 'html', 'template', 'resume.html');
const COPYABLE_TEMPLATE_FILE = path.join(PROJECT_ROOT, 'html', 'template', 'resume-copyable.html');
const CSS_FILE = path.join(PROJECT_ROOT, 'html', 'css', 'resume.css');
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'html', 'output');

// 确保输出目录存在
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

// 读取模板
const template = fs.readFileSync(TEMPLATE_FILE, 'utf-8');
const copyableTemplate = fs.readFileSync(COPYABLE_TEMPLATE_FILE, 'utf-8');

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
 * 生成 HTML
 */
function generateHTML() {
  const profile = data.profile;
  const summary = data.summary;
  const skills = data.core_skills;
  const experiences = data.experience;

  // 处理摘要
  const summaryBody = summary.trim();

  // 处理核心能力：details 数组 → 去尾部标点后用 ；连接
  const processedSkills = skills.map(skill => ({
    title: skill.title,
    details: Array.isArray(skill.details)
      ? skill.details.map(d => d.replace(/[。；，、\s]+$/, '')).join('；')
      : skill.details
  }));

  // 处理工作经历
  const processedExperiences = experiences.map(exp => {
    const role = exp.role;

    const processedProjects = exp.projects.map(proj => ({
      name: proj.name,
      highlights: proj.highlights.map(h => processHighlight(h))
    }));

    return {
      company: exp.company,
      role: role,
      period: exp.period,
      summary: exp.summary || '',
      projects: processedProjects
    };
  }).filter(exp => exp.projects.length > 0);

  // 构建 Mustache 数据
  const view = {
    // 个人资料
    name: profile.name,
    location: profile.location,
    email: profile.email,
    phone: profile.phone,
    tech: profile.tech || '',
    education: profile.education,
    birth_year: profile.birth_year || '',

    // 摘要
    summary_title: '个人简介',
    summary_has_title: false,
    summary_title_line: '',
    summary_body: summaryBody.replace(/\n/g, '<br>'),

    // 核心能力
    core_skills: processedSkills,

    // 工作经历
    experiences: processedExperiences,

    // 技术栈（YAML 中已移除，保留兼容）
    professional_certs: data.tech_stack?.professional_certs || '',
    languages: data.tech_stack?.languages || '',
    systems_gateways: data.tech_stack?.['systems_&_gateways'] || '',
    data_infrastructure: data.tech_stack?.['data_&_infrastructure'] || '',
    ai_llm_security: data.tech_stack?.ai_llm_security || '',
    honors: data.tech_stack?.honors || '',

    // 教育背景列表
    education_list: data.education
  };

  // 渲染 HTML
  let html = Mustache.render(template, view);

  // 内联 CSS
  html = html.replace(
    '<link rel="stylesheet" href="../css/resume.css">',
    `<style>\n${cssContent}\n</style>`
  );
  return html;
}

/**
 * 生成可复制的 HTML（简化版，方便粘贴到外部系统）
 */
function generateCopyableHTML() {
  const profile = data.profile;
  const summary = data.summary;
  const skills = data.core_skills;
  const experiences = data.experience;

  // 处理摘要
  const summaryBody = summary.trim();

  // 处理核心能力：details 数组 → 去尾部标点后用 ；连接
  const processedSkills = skills.map(skill => ({
    title: skill.title,
    details: Array.isArray(skill.details)
      ? skill.details.map(d => d.replace(/[。；，、\s]+$/, '')).join('；')
      : skill.details
  }));

  // 处理工作经历
  const processedExperiences = experiences.map(exp => {
    const role = exp.role;

    const processedProjects = exp.projects.map(proj => ({
      name: proj.name,
      highlights: proj.highlights.map(h => processHighlight(h))
    }));

    return {
      company: exp.company,
      role: role,
      period: exp.period,
      summary: exp.summary || '',
      projects: processedProjects
    };
  }).filter(exp => exp.projects.length > 0);

  // 构建 Mustache 数据
  const view = {
    // 个人资料
    name: profile.name,
    location: profile.location,
    email: profile.email,
    phone: profile.phone,
    education: profile.education,

    // 摘要
    summary_body: summaryBody.replace(/\n/g, '<br>'),

    // 核心能力
    core_skills: processedSkills,

    // 工作经历
    experiences: processedExperiences,

    // 教育背景列表
    education_list: data.education
  };

  // 渲染 HTML
  return Mustache.render(copyableTemplate, view);
}

// 生成打印版 HTML
const html = generateHTML();
const outputFile = path.join(OUTPUT_DIR, 'resume.html');
fs.writeFileSync(outputFile, html, 'utf-8');
console.log(`  ✓ ${outputFile}`);

// 生成可复制版 HTML
const copyableHtml = generateCopyableHTML();
const copyableOutputFile = path.join(OUTPUT_DIR, 'resume-copyable.html');
fs.writeFileSync(copyableOutputFile, copyableHtml, 'utf-8');
console.log(`  ✓ ${copyableOutputFile}`);

console.log('HTML generation complete!');
