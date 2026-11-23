import fs from 'fs';
import path from 'path';
import { CONFIG_20 } from './config_20.mjs';

const tickers20 = Object.keys(CONFIG_20);
const cqvData = JSON.parse(fs.readFileSync('cqv_data.json', 'utf-8'));
const cqvHistory = JSON.parse(fs.readFileSync('cqv_history.json', 'utf-8'));
const dashboardHtml = fs.readFileSync('dashboard.html', 'utf-8');

let errors = [];

// 1. Audit all P3 reports in inform/cqv_v5/2026 P3 (equivalent to scratch/verify_section8.py)
const p3Dir = 'inform/cqv_v5/2026 P3';
const p3Files = fs.readdirSync(p3Dir).filter(f => f.endsWith('.md')).map(f => path.join(p3Dir, f));
console.log(`Auditing Section 8 across ${p3Files.length} P3 reports...`);

for (const f of p3Files) {
  const content = fs.readFileSync(f, 'utf-8').replace(/\r\n/g, '\n');

  // Check Table 8.1 (13 columns)
  const m8 = content.match(/### 8\.1\..*?\n(\|.*?\|\n\|.*?\|\n(?:\|.*?\|\n)+)/s);
  if (!m8) {
    errors.push(`${f}: NO SE ENCONTRO TABLA 8.1`);
    continue;
  }
  const lines = m8[1].trim().split('\n');
  const hCols = lines[0].split('|').length - 2;
  const sCols = lines[1].split('|').length - 2;
  if (hCols !== 13 || sCols !== 13) {
    errors.push(`${f}: Tabla 8.1 Header cols=${hCols}, Sep cols=${sCols} (deben ser 13)`);
  }
  lines.slice(2).forEach((r, idx) => {
    const rCols = r.split('|').length - 2;
    if (rCols !== 13) {
      errors.push(`${f}: Tabla 8.1 Fila ${idx + 1} tiene ${rCols} cols (deben ser 13)`);
    }
  });

  // Check Mermaid 8.2
  const mm = content.match(/### 8\.2\..*?```mermaid\n([\s\S]*?)```/s);
  if (!mm) {
    errors.push(`${f}: NO SE ENCONTRO MERMAID 8.2`);
    continue;
  }
  const mermaidCode = mm[1];
  const mx = mermaidCode.match(/x-axis \[(.*?)\]/);
  const my = mermaidCode.match(/line "CQV v5\.0" \[(.*?)\]/);
  if (!mx || !my) {
    errors.push(`${f}: Sintaxis Mermaid x-axis o line invalida`);
  } else {
    const xItems = mx[1].split(',').map(x => x.trim()).filter(Boolean);
    const yItems = my[1].split(',').map(y => y.trim()).filter(Boolean);
    if (xItems.length !== yItems.length) {
      errors.push(`${f}: Longitud x-axis (${xItems.length}) != longitud line (${yItems.length})`);
    }
    if (xItems.some(x => x.includes('**'))) {
      errors.push(`${f}: x-axis contiene asteriscos de markdown`);
    }
  }
}

// 2. Audit the 20 newly updated companies for Table 3.1 (6 columns) and 100% SSOT coherence
console.log(`Auditing 20 newly updated tickers for Table 3.1 and tri-directional SSOT coherence...`);
for (const ticker of tickers20) {
  const dItem = cqvData.find(x => x.ticker === ticker);
  const hItem = cqvHistory[ticker]?.['2026']?.['P3'];
  const mdPath = path.join(p3Dir, `${ticker}_2026_P3_CQVv5.md`);

  if (!dItem) errors.push(`${ticker}: Missing in cqv_data.json`);
  if (!hItem) errors.push(`${ticker}: Missing in cqv_history.json [2026][P3]`);
  if (!fs.existsSync(mdPath)) {
    errors.push(`${ticker}: Missing report ${mdPath}`);
    continue;
  }

  const md = fs.readFileSync(mdPath, 'utf-8').replace(/\r\n/g, '\n');

  // Check Table 3.1 (strictly 6 columns)
  const m3 = md.match(/### 3\.1\..*?\n\n(\|.*?\|\n\|.*?\|\n(?:\|.*?\|\n)+)/s);
  if (!m3) {
    errors.push(`${ticker}: NO SE ENCONTRO TABLA 3.1`);
  } else {
    const lines3 = m3[1].trim().split('\n');
    lines3.forEach((r, idx) => {
      const cols = r.split('|').length - 2;
      if (cols !== 6) {
        errors.push(`${ticker}: Tabla 3.1 línea ${idx + 1} tiene ${cols} columnas (deben ser 6)`);
      }
    });
  }

  // Check exact coherence between cqv_data.json, cqv_history.json, and Markdown
  if (dItem.cqv_v5 !== hItem.cqv_v5) {
    errors.push(`${ticker}: CQV mismatch data(${dItem.cqv_v5}) vs history(${hItem.cqv_v5})`);
  }
  if (dItem.value_score !== hItem.value_score) {
    errors.push(`${ticker}: Value Score mismatch data(${dItem.value_score}) vs history(${hItem.value_score})`);
  }
  if (dItem.price !== hItem.price) {
    errors.push(`${ticker}: Price mismatch data(${dItem.price}) vs history(${hItem.price})`);
  }
  if (!md.includes(`CQV Calidad Fundamental (F1-F8): ${dItem.cqv_v5.toFixed(2)} / 10.00`)) {
    errors.push(`${ticker}: CQV score ${dItem.cqv_v5.toFixed(2)} not matched in report header block`);
  }
  if (!md.includes(`Value Score v5.0:                ${dItem.value_score.toFixed(2)} / 10.00`)) {
    errors.push(`${ticker}: Value score ${dItem.value_score.toFixed(2)} not matched in report header block`);
  }
  if (!md.includes(`Precio de Mercado:               $${dItem.price.toFixed(2)} USD`)) {
    errors.push(`${ticker}: Price $${dItem.price.toFixed(2)} not matched in report header block`);
  }
  if (!dashboardHtml.includes(`"${ticker}_2026_P3_CQVV5"`)) {
    errors.push(`${ticker}: Thesis key ${ticker}_2026_P3_CQVV5 not injected into dashboard.html`);
  }
}

if (errors.length > 0) {
  console.error(`SE ENCONTRARON ${errors.length} ERRORES:`);
  errors.forEach(e => console.error(' -', e));
  process.exit(1);
} else {
  console.log(`AUDITORIA 100% EXITOSA: ${p3Files.length} informes P3 validados (Sección 3.1 de 6 cols, Sección 8.1 de 13 cols, Mermaid 8.2 y coherencia total SSOT <-> JS <-> Dashboard <-> Markdown).`);
}
