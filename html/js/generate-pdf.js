#!/usr/bin/env node
/**
 * HTML → PDF 生成脚本（使用 Playwright）
 *
 * 用法:
 *   node js/generate-pdf.js
 *
 * 输入:
 *   html/output/resume_gateway.html
 *   html/output/resume_security.html
 *
 * 输出:
 *   output/resume_gateway.pdf
 *   output/resume_security.pdf
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// 路径配置
const PROJECT_ROOT = path.resolve(__dirname, '..', '..');
const HTML_DIR = path.join(PROJECT_ROOT, 'html', 'output');
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'output');

// 确保输出目录存在
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

const files = [
  { html: 'resume_gateway.html', pdf: 'resume_gateway.pdf' },
  { html: 'resume_security.html', pdf: 'resume_security.pdf' },
];

async function generatePDF() {
  // 使用系统已安装的 Chrome
  const browser = await chromium.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });

  for (const { html, pdf } of files) {
    const htmlPath = path.join(HTML_DIR, html);
    const pdfPath = path.join(OUTPUT_DIR, pdf);

    if (!fs.existsSync(htmlPath)) {
      console.warn(`Skipping: ${htmlPath} not found`);
      continue;
    }

    const page = await browser.newPage();

    // 加载本地 HTML 文件
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });

    // 等待字体加载
    await page.waitForTimeout(500);

    // 生成 PDF
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      margin: {
        top: '0.50in',
        right: '0.65in',
        bottom: '0.50in',
        left: '0.65in',
      },
    });

    await page.close();
    console.log(`Generated: ${pdfPath}`);
  }

  await browser.close();
  console.log('PDF generation complete!');
}

generatePDF().catch((err) => {
  console.error('Error generating PDF:', err);
  process.exit(1);
});
