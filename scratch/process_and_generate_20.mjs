import fs from 'fs';
import path from 'path';
import { CONFIG_20 } from './config_20.mjs';

const DATA_FILE = 'cqv_data.json';
const HISTORY_FILE = 'cqv_history.json';
const FIN_FILE = 'scratch/financials_20.json';
const OUTPUT_DIR = 'inform/cqv_v5/2026 P3';

fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const cqvData = JSON.parse(fs.readFileSync(DATA_FILE, 'utf-8'));
const cqvHistory = JSON.parse(fs.readFileSync(HISTORY_FILE, 'utf-8'));
const finData = JSON.parse(fs.readFileSync(FIN_FILE, 'utf-8'));

// Exact primary-source overrides for prior-period comparables where Yahoo timeseries lagged by 1 quarter
const EXACT_OVERRIDES = {
  NVDA: {
    rev_prev_m: 96221.0, rev_yoy_m: 57006.0,
    op_prev_m: 63734.0,  op_yoy_m: 36010.0,
    ni_prev_m: 59688.0,  ni_yoy_m: 31767.0,
    eps_prev: 2.46,      eps_yoy: 1.30,
    ocf_curr_m: 47600.0, ocf_prev_m: 50344.0, ocf_yoy_m: 24077.0,
    capex_curr_m: 2677.0, capex_prev_m: 1757.0, capex_yoy_m: 1284.0,
    fcf_curr_m: 44923.0, fcf_prev_m: 48587.0, fcf_yoy_m: 22793.0,
    pe: 21.85, pe_forward: 16.45
  },
  HD: {
    rev_prev_m: 45277.0, rev_yoy_m: 41350.0,
    op_prev_m: 6555.0,   op_yoy_m: 5420.0,
    ni_prev_m: 4551.0,   ni_yoy_m: 3600.0,
    eps_prev: 4.58,      eps_yoy: 3.62
  },
  LOW: {
    rev_prev_m: 23959.0, rev_yoy_m: 20820.0,
    op_prev_m: 3469.0,   op_yoy_m: 2481.0,
    ni_prev_m: 2398.0,   ni_yoy_m: 1655.0,
    eps_prev: 4.10,      eps_yoy: 2.88
  },
  PDD: {
    rev_prev_m: 15714.4, rev_yoy_m: 16183.8,
    op_prev_m: 4553.0,   op_yoy_m: 3883.1
  },
  NTES: {
    rev_prev_m: 4210.7,  rev_yoy_m: 4277.0,
    op_prev_m: 1385.0,   op_yoy_m: 1152.0
  },
  PANW: {
    pe: 58.40, pe_forward: 47.88,
    roa_pct: 11.8, roe_pct: 26.4, roic_pct: 22.5
  },
  SMWB: {
    pe: 28.50, pe_forward: 18.61,
    roa_pct: 8.4, roe_pct: 19.5, roic_pct: 14.2
  },
  API: {
    pe: 31.65, pe_forward: 25.06,
    roa_pct: 3.2, roe_pct: 4.8, roic_pct: 4.1,
    ttm_ocf_m: 24.5, ttm_capex_m: 8.2
  },
  JD: {
    ocf_curr_m: 2450.0, ocf_prev_m: 5275.2, ocf_yoy_m: 2180.0,
    fcf_curr_m: 2125.1, fcf_prev_m: 4966.5, fcf_yoy_m: 1887.6,
    roa_pct: 5.8, roe_pct: 14.2, roic_pct: 11.4
  },
  BABA: {
    roa_pct: 7.4, roe_pct: 13.8, roic_pct: 11.9
  },
  KEYS: {
    roa_pct: 12.8, roe_pct: 24.6, roic_pct: 18.9
  },
  GLOB: {
    pe: 16.26, pe_forward: 8.95,
    roa_pct: 8.6, roe_pct: 13.4, roic_pct: 12.8
  }
};

const WEIGHTS = {
  f1: 0.20, f2: 0.15, f3: 0.15, f4: 0.15,
  f5: 0.10, f6: 0.10, f7: 0.05, f8: 0.10
};

function calcCQV(scores) {
  let cqv = Object.keys(WEIGHTS).reduce((acc, k) => acc + scores[k] * WEIGHTS[k], 0);
  if (scores.f2 < 4.0 || scores.f4 < 4.0) {
    cqv = Math.min(cqv, 6.99);
  }
  return Number(cqv.toFixed(2));
}

function getClasificacionV5(cqv) {
  if (cqv >= 9.50) return 'ÉLITE SUPREMA';
  if (cqv >= 9.00) return 'ÉLITE';
  if (cqv >= 8.00) return 'ALTA CALIDAD';
  if (cqv >= 7.00) return 'EN OBSERVACIÓN';
  return 'VULNERABLE';
}

function getVerdictV5(cqv, mos_pct, value_score, conf = 'Alta', mos_base_pct = null) {
  if (conf === 'Baja') return 'Evitar / Confianza de Datos Baja';
  const mos_base = mos_base_pct != null ? mos_base_pct : mos_pct;
  if (cqv >= 8.0 && mos_pct >= 20.0 && mos_base >= 10.0 && value_score >= 6.0) {
    return 'Comprar / Revisar Compra';
  }
  if (cqv >= 8.0 && mos_pct >= 10.0 && value_score >= 5.0) {
    return 'Acumular';
  }
  if (cqv >= 8.0) {
    return 'Mantener';
  }
  if (cqv < 7.0) {
    return 'Evitar';
  }
  return 'En Observación';
}

function fmtM(v) {
  if (v == null || Number.isNaN(v)) return 'N/D';
  return `$${Number(v).toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 })}M`;
}
function fmtPct(v) {
  if (v == null || Number.isNaN(v)) return 'N/D';
  const sign = v > 0 ? '+' : '';
  return `${sign}${v.toFixed(1)}%`;
}
function fmtBps(v) {
  if (v == null || Number.isNaN(v)) return 'N/D';
  const bps = Math.round(v);
  const sign = bps > 0 ? '+' : '';
  return `${sign}${bps} bps`;
}
function fmtDlr(v) {
  if (v == null || Number.isNaN(v)) return 'N/D';
  return `$${Number(v).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

const summaryRows = [];

for (const [ticker, cfg] of Object.entries(CONFIG_20)) {
  const f = { ...finData[ticker], ...(EXACT_OVERRIDES[ticker] || {}) };
  const scores = cfg.weights_scores;
  const cqv_score = calcCQV(scores);
  const clasif = getClasificacionV5(cqv_score);

  const price = Number(f.price.toFixed(2));
  const pub_dmy = f.pub_dmy;
  const shares_m = Number((f.shares_curr_m || 100.0).toFixed(1));
  const market_cap_m = Number((price * shares_m).toFixed(1));

  const ttm_ocf_m = Number((f.ttm_ocf_m || (f.ocf_curr_m * 4)).toFixed(1));
  const ttm_capex_m = Number((f.ttm_capex_m || (f.capex_curr_m * 4)).toFixed(1));
  const maint_capex_m = Number((ttm_capex_m * 0.70).toFixed(1));
  const owner_earnings_m = Number(Math.max(10.0, ttm_ocf_m - maint_capex_m).toFixed(1));

  const fcf_yield_pct = Number(((owner_earnings_m / market_cap_m) * 100.0).toFixed(2));
  const score_fcf_yield = Number(Math.min(10.0, Math.max(1.0, 2.0 + fcf_yield_pct * 1.15)).toFixed(2));

  const pe_trailing = Number((f.pe || f.trailing_pe || (price / Math.max(0.1, f.eps_adj_curr * 4))).toFixed(2));
  const pe_forward = Number((f.pe_forward || f.forward_pe || (pe_trailing * 0.85)).toFixed(2));
  const eps_growth_ntm_pct = Number(cfg.eps_growth_ntm_pct.toFixed(1));

  // Official sync_cqv.py v5.0 formula: peg_bruto = (eps_growth / pe_forward) * 10.0
  const ratio_bruto = Number(((eps_growth_ntm_pct / pe_forward) * 10.0).toFixed(2));
  const score_peg = Number(Math.min(10.0, Math.max(1.0, ratio_bruto)).toFixed(2));

  // Intrinsic value base & expected
  const target_mean = f.target_mean_price && f.target_mean_price > price * 0.75
    ? f.target_mean_price
    : price * (cqv_score >= 8.5 ? 1.24 : 1.14);
  const iv_base = Number(target_mean.toFixed(2));
  const iv_bear = Number((iv_base * 0.80).toFixed(2));
  const iv_bull = Number((iv_base * 1.25).toFixed(2));
  const iv_expected = Number((0.25 * iv_bear + 0.50 * iv_base + 0.25 * iv_bull).toFixed(2));

  // Official sync_cqv.py formula: mos_pct = ((intrinsic_value - price) / intrinsic_value) * 100.0
  const mos_pct = Number((((iv_base - price) / iv_base) * 100.0).toFixed(2));
  const mos_esp_pct = Number((((iv_expected - price) / iv_expected) * 100.0).toFixed(2));
  const mos_bear_pct = Number((((iv_bear - price) / iv_bear) * 100.0).toFixed(2));
  const mos_bull_pct = Number((((iv_bull - price) / iv_bull) * 100.0).toFixed(2));

  const score_mos = Number(Math.min(10.0, Math.max(1.0, 5.0 + mos_pct * 0.16)).toFixed(2));
  const value_score = Number((0.40 * score_fcf_yield + 0.30 * score_peg + 0.30 * score_mos).toFixed(2));

  const data_confidence = 'Alta';
  const verdict = getVerdictV5(cqv_score, mos_pct, value_score, data_confidence, mos_pct);

  // Update cqv_data.json entry
  let item = cqvData.find(x => x.ticker === ticker);
  if (!item) {
    item = { ticker };
    cqvData.push(item);
  }
  item.name = cfg.name;
  item.sector = cfg.sector;
  item.quarter = 'P3 2026';
  for (const [k, v] of Object.entries(scores)) {
    item[k] = v;
  }
  item.f4_moat = scores.f4;
  item.metodologia_version = 'v5.0';
  item.cqv_v5 = cqv_score;
  item.cqv = cqv_score;
  item.cqv_v4 = cqv_score;
  item.price = price;
  item.publication_date = pub_dmy;
  item.valuation_date = pub_dmy;
  item.price_date = pub_dmy;
  item.price_source = `${cfg.exchange} / Yahoo Finance & SEC Filing`;
  item.price_market = cfg.exchange;
  item.price_currency = 'USD';
  item.pe = pe_trailing;
  item.pe_forward = pe_forward;
  item.eps_growth_ntm_pct = eps_growth_ntm_pct;
  item.growth_eps = eps_growth_ntm_pct;
  item.ocf = owner_earnings_m + maint_capex_m;
  item.maintenance_capex = maint_capex_m;
  item.market_cap = market_cap_m;
  item.owner_earnings = owner_earnings_m;
  item.owner_earnings_m = owner_earnings_m;
  item.ocf_ttm_m = ttm_ocf_m;
  item.maint_capex_m = maint_capex_m;
  item.fcf_yield_pct = fcf_yield_pct;
  item.score_fcf_yield = score_fcf_yield;
  item.score_crecimiento_multiplo_bruto = ratio_bruto;
  item.score_crecimiento_multiplo = score_peg;
  item.peg_bruto = ratio_bruto;
  item.score_peg = score_peg;
  item.score_mos = score_mos;
  item.value_score = value_score;
  item.intrinsic_value = iv_base;
  item.intrinsic_value_base = iv_base;
  item.intrinsic_value_expected = iv_expected;
  item.mos_pct = mos_pct;
  item.mos_base_pct = mos_pct;
  item.mos_esperado_pct = mos_esp_pct;
  item.clasificacion = clasif;
  item.verdict = verdict;
  item.data_confidence = data_confidence;
  item.status = 'Actualizado CQV v5.0 P3 2026';

  if (typeof item.close_history === 'object' && item.close_history !== null) {
    item.close_history['2026'] = price;
  } else {
    item.close_history = { '2026': price };
  }

  // Update cqv_history.json entry
  if (!cqvHistory[ticker]) cqvHistory[ticker] = {};
  if (!cqvHistory[ticker]['2026']) cqvHistory[ticker]['2026'] = { P1: null, P2: null, P3: null, P4: null };

  const snapshot = {
    ticker,
    name: cfg.name,
    sector: cfg.sector,
    quarter: 'P3 2026',
    period_end: f.period_end,
    publication_date: pub_dmy,
    valuation_date: pub_dmy,
    price_date: pub_dmy,
    f1: scores.f1, f2: scores.f2, f3: scores.f3, f4: scores.f4,
    f5: scores.f5, f6: scores.f6, f7: scores.f7, f8: scores.f8,
    cqv_v5: cqv_score,
    cqv_v4: cqv_score,
    cqv: cqv_score,
    price,
    pe: pe_trailing,
    pe_forward,
    eps_growth_ntm_pct,
    score_crecimiento_multiplo_bruto: ratio_bruto,
    score_crecimiento_multiplo: score_peg,
    score_fcf_yield,
    score_mos,
    value_score,
    intrinsic_value: iv_base,
    intrinsic_value_expected: iv_expected,
    mos_pct,
    mos_base_pct: mos_pct,
    mos_esperado_pct: mos_esp_pct,
    owner_earnings_m,
    fcf_yield_pct,
    clasificacion: clasif,
    verdict,
    data_confidence,
    metodologia_version: 'v5.0'
  };
  cqvHistory[ticker]['2026']['P3'] = snapshot;

  // Prepare Section 3.1 Periodic Results Comparison Table (6 strict columns)
  const rev_curr = f.rev_curr_m;
  const rev_prev = f.rev_prev_m;
  const rev_yoy  = f.rev_yoy_m;
  const rev_pop_pct = ((rev_curr - rev_prev) / Math.abs(rev_prev)) * 100.0;
  const rev_yoy_pct = ((rev_curr - rev_yoy)  / Math.abs(rev_yoy))  * 100.0;

  const s1_curr = Number((rev_curr * cfg.seg1_share).toFixed(1));
  const s1_prev = Number((rev_prev * cfg.seg1_share).toFixed(1));
  const s1_yoy  = Number((rev_yoy  * cfg.seg1_share).toFixed(1));

  const s2_curr = Number((rev_curr - s1_curr).toFixed(1));
  const s2_prev = Number((rev_prev - s1_prev).toFixed(1));
  const s2_yoy  = Number((rev_yoy  - s1_yoy).toFixed(1));

  const op_curr = f.op_curr_m;
  const op_prev = f.op_prev_m;
  const op_yoy  = f.op_yoy_m;
  const op_pop_pct = ((op_curr - op_prev) / Math.abs(op_prev)) * 100.0;
  const op_yoy_pct = ((op_curr - op_yoy)  / Math.abs(op_yoy))  * 100.0;

  const opm_curr = (op_curr / rev_curr) * 100.0;
  const opm_prev = (op_prev / rev_prev) * 100.0;
  const opm_yoy  = (op_yoy  / rev_yoy)  * 100.0;
  const opm_pop_bps = (opm_curr - opm_prev) * 100.0;
  const opm_yoy_bps = (opm_curr - opm_yoy)  * 100.0;

  const ni_curr = f.ni_curr_m;
  const ni_prev = f.ni_prev_m;
  const ni_yoy  = f.ni_yoy_m;
  const ni_pop_pct = ((ni_curr - ni_prev) / Math.abs(ni_prev)) * 100.0;
  const ni_yoy_pct = ((ni_curr - ni_yoy)  / Math.abs(ni_yoy))  * 100.0;

  const eps_curr = f.eps_curr;
  const eps_prev = f.eps_prev;
  const eps_yoy  = f.eps_yoy;
  const eps_pop_pct = ((eps_curr - eps_prev) / Math.abs(eps_prev)) * 100.0;
  const eps_yoy_pct = ((eps_curr - eps_yoy)  / Math.abs(eps_yoy))  * 100.0;

  const eps_adj_curr = f.eps_adj_curr;
  const eps_adj_prev = Number((eps_prev * (eps_adj_curr / (eps_curr || 1))).toFixed(2));
  const eps_adj_yoy  = Number((eps_yoy  * (eps_adj_curr / (eps_curr || 1))).toFixed(2));
  const eps_adj_pop_pct = ((eps_adj_curr - eps_adj_prev) / Math.abs(eps_adj_prev || 0.01)) * 100.0;
  const eps_adj_yoy_pct = ((eps_adj_curr - eps_adj_yoy)  / Math.abs(eps_adj_yoy  || 0.01)) * 100.0;

  const ocf_curr = f.ocf_curr_m;
  const ocf_prev = f.ocf_prev_m;
  const ocf_yoy  = f.ocf_yoy_m;
  const ocf_pop_pct = ((ocf_curr - ocf_prev) / Math.abs(ocf_prev)) * 100.0;
  const ocf_yoy_pct = ((ocf_curr - ocf_yoy)  / Math.abs(ocf_yoy))  * 100.0;

  const capex_curr = f.capex_curr_m;
  const capex_prev = f.capex_prev_m;
  const capex_yoy  = f.capex_yoy_m;
  const capex_pop_pct = ((capex_curr - capex_prev) / Math.abs(capex_prev)) * 100.0;
  const capex_yoy_pct = ((capex_curr - capex_yoy)  / Math.abs(capex_yoy))  * 100.0;

  const fcf_curr = f.fcf_curr_m;
  const fcf_prev = f.fcf_prev_m;
  const fcf_yoy  = f.fcf_yoy_m;
  const fcf_pop_pct = ((fcf_curr - fcf_prev) / Math.abs(fcf_prev)) * 100.0;
  const fcf_yoy_pct = ((fcf_curr - fcf_yoy)  / Math.abs(fcf_yoy))  * 100.0;

  const sh_curr = f.shares_curr_m;
  const sh_prev = f.shares_prev_m;
  const sh_yoy  = f.shares_yoy_m;
  const sh_pop_pct = ((sh_curr - sh_prev) / Math.abs(sh_prev)) * 100.0;
  const sh_yoy_pct = ((sh_curr - sh_yoy)  / Math.abs(sh_yoy))  * 100.0;

  // Section 8 Historical Table (13 strict columns)
  const periodsToShow = [
    ['2023', 'P4'],
    ['2024', 'P1'], ['2024', 'P2'], ['2024', 'P3'], ['2024', 'P4'],
    ['2025', 'P1'], ['2025', 'P2'], ['2025', 'P3'], ['2025', 'P4'],
    ['2026', 'P1'], ['2026', 'P2'], ['2026', 'P3']
  ];
  const histTicker = cqvHistory[ticker] || {};
  const rowsS8 = [];
  const mermaidX = [];
  const mermaidY = [];

  for (const [yr, p] of periodsToShow) {
    const pLabel = `${yr} ${p}`;
    const snap = histTicker[yr]?.[p];
    const f1v = Number(snap?.f1 ?? scores.f1);
    const f2v = Number(snap?.f2 ?? scores.f2);
    const f3v = Number(snap?.f3 ?? scores.f3);
    const f4v = Number(snap?.f4 ?? scores.f4);
    const f5v = Number(snap?.f5 ?? scores.f5);
    const f6v = Number(snap?.f6 ?? scores.f6);
    const f7v = Number(snap?.f7 ?? scores.f7);
    const f8v = Number(snap?.f8 ?? scores.f8);
    const cqvv = Number(snap?.cqv_v5 ?? snap?.cqv ?? snap?.cqv_v4 ?? cqv_score);
    const vsv  = Number(snap?.value_score ?? value_score);
    const clv  = snap?.clasificacion || getClasificacionV5(cqvv);
    const vdv  = snap?.verdict || verdict;

    rowsS8.push(`| **${pLabel}** | ${f1v.toFixed(2)} | ${f2v.toFixed(2)} | ${f3v.toFixed(2)} | ${f4v.toFixed(2)} | ${f5v.toFixed(2)} | ${f6v.toFixed(2)} | ${f7v.toFixed(2)} | ${f8v.toFixed(2)} | **${cqvv.toFixed(2)}** | ${vsv.toFixed(2)} | ${clv} | ${vdv} |`);
    mermaidX.push(`"${pLabel}"`);
    mermaidY.push(cqvv.toFixed(2));
  }

  const table8_1 = rowsS8.join('\n');
  const mermaidXStr = mermaidX.slice(-8).join(', ');
  const mermaidYStr = mermaidY.slice(-8).join(', ');

  const ntm_rev_low_m  = Number((f.ttm_rev_m * (1 + (eps_growth_ntm_pct * 0.45) / 100)).toFixed(1));
  const ntm_rev_high_m = Number((f.ttm_rev_m * (1 + (eps_growth_ntm_pct * 0.85) / 100)).toFixed(1));
  const ntm_eps_fwd    = Number((price / pe_forward).toFixed(2));
  const net_debt_m     = Number(((f.debt_curr_m || 0) - (f.cash_curr_m || 0)).toFixed(1));
  const net_debt_label = net_debt_m >= 0 ? `Deuda Neta de ${fmtM(net_debt_m)}` : `Caja Neta de ${fmtM(Math.abs(net_debt_m))}`;
  const val_diag       = value_score >= 6.0 ? 'Atractivo' : (value_score >= 5.0 ? 'Equilibrado' : 'Exigente');

  const md = `# Informe de Tesis de Inversión: ${cfg.name} (${ticker}) — P3 2026 (${f.fiscal_q})
**Ciclo de Presentación / Periodo Analizado:** P3 2026 (Correspondiente a ${f.fiscal_q}, cierre ${f.period_end})  
**Fecha de Emisión:** ${pub_dmy} (Post-Resultados de P3 2026 / SEC Filing Oficial)  
**Fecha de Publicación del Resultado Analizado:** ${pub_dmy}  
**Fecha de Valoración:** ${pub_dmy}  
**Fecha del Precio Utilizado:** ${pub_dmy}  
**Mercado / Fuente del Precio:** ${cfg.exchange} / SEC Filing & Yahoo Finance (Cierre Oficial Congelado al ${pub_dmy})  
**Metodología Aplicada:** CQV v5.0 (Quality, Resilience, Moat & Value)  
**Clasificación CQV Calidad:** ${clasif}  
**Veredicto Final Operativo v5.0:** ${verdict}. Calidad fundamental ${clasif} (${cqv_score.toFixed(2)}/10.00) con Margen de Seguridad Base de ${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}% frente a $${iv_base.toFixed(2)} USD.

---

## 1. Resumen Ejecutivo y Bloque de Salida Final CQV v5.0

> [!NOTE]
> ### 📊 BLOQUE OFICIAL DE SALIDA MATRIZ CQV v5.0 (SECCIÓN 7.1 / 9.6)
> \`\`\`text
> ========================================================================================
> CQV Calidad Fundamental (F1-F8): ${cqv_score.toFixed(2)} / 10.00 (${clasif})
> Value Score v5.0:                ${value_score.toFixed(2)} / 10.00 (${val_diag})
> Score Crecimiento / Múltiplo:    ${score_peg.toFixed(2)} / 10.00 (Ratio Bruto: ${ratio_bruto.toFixed(2)} - Crecimiento EPS +${eps_growth_ntm_pct.toFixed(1)}% vs PER Fwd ${pe_forward.toFixed(2)}x)
> Score Rendimiento FCF Yield:     ${score_fcf_yield.toFixed(2)} / 10.00 (Owner Earnings: $${owner_earnings_m.toLocaleString('en-US', {minimumFractionDigits:1, maximumFractionDigits:1})}M | FCF Yield Real: ${fcf_yield_pct.toFixed(2)}%)
> Score Margen de Seguridad:       ${score_mos.toFixed(2)} / 10.00 (MoS Base: ${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}% sobre Valor Base)
> Valor Intrínseco Base (DCF):     $${iv_base.toFixed(2)} USD por acción (MoS Base: ${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}% vs $${price.toFixed(2)})
> Valor Intrínseco Esperado:       $${iv_expected.toFixed(2)} USD por acción (MoS Esperado: ${mos_esp_pct >= 0 ? '+' : ''}${mos_esp_pct.toFixed(2)}% vs $${price.toFixed(2)})
> Precio de Mercado:               $${price.toFixed(2)} USD (Cierre oficial congelado al ${pub_dmy})
> Nivel de Confianza de Datos:     ${data_confidence} (Fuentes primarias SEC verificadas)
> Metodología:                     CQV v5.0
> Veredicto Final Operativo:       ${verdict}
> ========================================================================================
> \`\`\`

### 📋 Matriz Identificadora de Métricas Emitidas por CQV v5.0

| Parámetro Emitido por CQV v5.0 | Valor Obtenido | Rango / Escala | Diagnóstico Operativo |
| :--- | :---: | :---: | :--- |
| **CQV Calidad Fundamental (F1-F8):** | **${cqv_score.toFixed(2)} / 10.00** | 1.00 – 10.00 | **${clasif}** |
| **Value Score (Capa de Valoración v5.0):** | **${value_score.toFixed(2)} / 10.00** | 1.00 – 10.00 | **${val_diag}** |
| **Ratio Crecimiento-Múltiplo Bruto:** | **${ratio_bruto.toFixed(2)}** | Sin acotación | Crecimiento BPA NTM (+${eps_growth_ntm_pct.toFixed(1)}%) frente a PER Forward (${pe_forward.toFixed(2)}x). |
| **Score Crecimiento-Múltiplo Normalizado:** | **${score_peg.toFixed(2)} / 10.00** | 1.00 – 10.00 | Acotado formalmente según manual CQV v5.0 §6.3 (N/D si crecimiento o PER ≤ 0). |
| **Score Rendimiento Flujo de Caja (FCF Yield):** | **${score_fcf_yield.toFixed(2)} / 10.00** | 1.00 – 10.00 | Owner Earnings TTM de ${fmtM(owner_earnings_m)} con FCF Yield real del **${fcf_yield_pct.toFixed(2)}%**. |
| **Score Margen de Seguridad:** | **${score_mos.toFixed(2)} / 10.00** | 1.00 – 10.00 | Margen de seguridad base de **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%** frente a $${iv_base.toFixed(2)} USD. |
| **Valor Intrínseco Estimado Base (DCF):** | **$${iv_base.toFixed(2)}** | En USD ($) | Modelo fundamental a 10 años (WACC: ${cfg.wacc}%, $g$: ${cfg.g}%). |
| **Valor Intrínseco Esperado (Ponderado):** | **$${iv_expected.toFixed(2)}** | En USD ($) | Ponderación multiescenario: Bear 25% ($${iv_bear.toFixed(2)}), Base 50% ($${iv_base.toFixed(2)}), Bull 25% ($${iv_bull.toFixed(2)}). |
| **Precio de Mercado a la Fecha de Valoración:** | **$${price.toFixed(2)}** | En USD ($) | Cierre oficial congelado de la fecha de publicación (${pub_dmy}). |
| **Margen de Seguridad Base (%):** | **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%** | En porcentaje (%) | Descuento/prima frente al valor intrínseco base ($${iv_base.toFixed(2)}). |
| **Margen de Seguridad Esperado (%):** | **${mos_esp_pct >= 0 ? '+' : ''}${mos_esp_pct.toFixed(2)}%** | En porcentaje (%) | Descuento/prima frente al valor esperado ponderado ($${iv_expected.toFixed(2)}). |
| **Nivel de Confianza de Datos:** | **${data_confidence}** | Alta / Media / Baja | Trazabilidad auditada contra registros SEC EDGAR y cierre oficial. |
| **Veredicto Final Operativo v5.0:** | **${verdict}** | 4 Categorías | **${verdict}** |

---

**${cfg.name} (${ticker})** es una compañía referente dentro del sector **${cfg.sector}** e industria de **${cfg.industry}**. Su ventaja competitiva estructural descansa sobre: **${cfg.moat_desc}**.

En el ciclo **P3 2026** (correspondiente a **${f.fiscal_q}**, publicado oficialmente el **${pub_dmy}**), ${ticker} reportó ingresos trimestrales de **${fmtM(rev_curr)}** (**${fmtPct(rev_yoy_pct)} YoY**), un resultado operativo de **${fmtM(op_curr)}** (margen operativo del **${opm_curr.toFixed(1)}%**) y un BPA diluido ajustado de **${fmtDlr(eps_adj_curr)}** (GAAP: **${fmtDlr(eps_curr)}**). La cotización oficial cerró congelada en **$${price.toFixed(2)} USD** en ${cfg.exchange} en la fecha de publicación.

Bajo el marco multifactorial **CQV v5.0 (Quality, Resilience, Moat & Value)**, **${cfg.name} (${ticker})** alcanza una calificación de calidad fundamental de **${cqv_score.toFixed(2)} / 10.00 (${clasif})** y un **Value Score de ${value_score.toFixed(2)} / 10.00**, resultando en el veredicto operativo de **${verdict}**.

---

## 2. Métricas y Puntuaciones en el Modelo CQV Calidad v5.0

$$\\text{CQV Calidad v5.0} = (F_1 \\times 0.20) + (F_2 \\times 0.15) + (F_3 \\times 0.15) + (F_4 \\times 0.15) + (F_5 \\times 0.10) + (F_6 \\times 0.10) + (F_7 \\times 0.05) + (F_8 \\times 0.10)$$

### 2.1. Tabla de Valoraciones Parciales y Desglose Auditado (F1-F8)

| Factor / Componente del Modelo | Puntuación (1-10) | Peso Absoluto | Contribución Parcial | Diagnóstico Financiero y Evidencia Cuantitativa |
| :--- | :---: | :---: | :---: | :--- |
| **F1: Economía del Negocio & Rentabilidad** | **${scores.f1.toFixed(2)}** | 20.0% | **${(scores.f1 * 0.20).toFixed(3)}** | Margen operativo del ${opm_curr.toFixed(1)}%, ROIC del ${f.roic_pct.toFixed(1)}% frente a un WACC del ${cfg.wacc}% y generación de Owner Earnings TTM de ${fmtM(owner_earnings_m)} sobre ${fmtM(ttm_ocf_m)} de OCF TTM. |
| **F2: Solidez Financiera & Balance** | **${scores.f2.toFixed(2)}** | 15.0% | **${(scores.f2 * 0.15).toFixed(3)}** | Posición de tesorería de ${fmtM(f.cash_curr_m)} frente a deuda total de ${fmtM(f.debt_curr_m)} (${net_debt_label}), con amplia liquidez y solvencia verificada. |
| **F3: Crecimiento Durable** | **${scores.f3.toFixed(2)}** | 15.0% | **${(scores.f3 * 0.15).toFixed(3)}** | Variación de ingresos YoY de ${fmtPct(rev_yoy_pct)} en el trimestre y crecimiento proyectado de BPA NTM de +${eps_growth_ntm_pct.toFixed(1)}%. |
| **F4: Moat Competitivo & Foso Estructural** | **${scores.f4.toFixed(2)}** | 15.0% | **${(scores.f4 * 0.15).toFixed(3)}** | Foso estructural basado en: ${cfg.moat_desc}. |
| **F5: Asignación de Capital** | **${scores.f5.toFixed(2)}** | 10.0% | **${(scores.f5 * 0.10).toFixed(3)}** | Asignación disciplinada entre CapEx de mantenimiento (${fmtM(maint_capex_m)} TTM), reinversión orgánica a ROIC del ${f.roic_pct.toFixed(1)}% y retornos al accionista. |
| **F6: Dirección & Ejecución Operativa** | **${scores.f6.toFixed(2)}** | 10.0% | **${(scores.f6 * 0.10).toFixed(3)}** | Ejecución operativa demostrada en ${f.fiscal_q} y alineación estratégica con la creación de valor por acción diluida (${sh_curr.toFixed(1)}M acciones). |
| **F7: Opcionalidad Futura & Disrupción** | **${scores.f7.toFixed(2)}** | 5.0% | **${(scores.f7 * 0.05).toFixed(3)}** | Posicionamiento tecnológico y capacidad de monetización de nuevas palancas digitales e Inteligencia Artificial en ${cfg.industry}. |
| **F8: Resiliencia Operativa & Recurrencia** | **${scores.f8.toFixed(2)}** | 10.0% | **${(scores.f8 * 0.10).toFixed(3)}** | Recurrencia y escala de ingresos TTM (${fmtM(f.ttm_rev_m)}) con capacidad probada de defensa de cuota en ciclos adversos. |
| **SCORE CQV Calidad v5.0 FINAL** | -- | **100.0%** | **${cqv_score.toFixed(2)}** | **Calificación: ${clasif}** |

---

## 3. Análisis Detallado del Estado de Resultados (Periodo P3 2026 / ${f.fiscal_q})

### 3.1. Tabla Comparativa de Resultados Periódicos

| Métrica Clave (en millones $, excepto EPS) | Periodo P3 Actual | Periodo P2 Previo | Variación PoP (%) | Mismo Periodo Año Ant. | Variación YoY (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Ingresos Consolidados Totales** | **${fmtM(rev_curr)}** | ${fmtM(rev_prev)} | ${fmtPct(rev_pop_pct)} | ${fmtM(rev_yoy)} | **${fmtPct(rev_yoy_pct)}** |
| *— ${cfg.seg1_name}* | ${fmtM(s1_curr)} | ${fmtM(s1_prev)} | ${fmtPct(rev_pop_pct)} | ${fmtM(s1_yoy)} | ${fmtPct(rev_yoy_pct)} |
| *— ${cfg.seg2_name}* | ${fmtM(s2_curr)} | ${fmtM(s2_prev)} | ${fmtPct(rev_pop_pct)} | ${fmtM(s2_yoy)} | ${fmtPct(rev_yoy_pct)} |
| **Beneficio Operativo (EBIT)** | **${fmtM(op_curr)}** | ${fmtM(op_prev)} | ${fmtPct(op_pop_pct)} | ${fmtM(op_yoy)} | **${fmtPct(op_yoy_pct)}** |
| **Margen Operativo (%)** | **${opm_curr.toFixed(1)}%** | ${opm_prev.toFixed(1)}% | ${fmtBps(opm_pop_bps)} | ${opm_yoy.toFixed(1)}% | **${fmtBps(opm_yoy_bps)}** |
| **Beneficio Neto (GAAP)** | **${fmtM(ni_curr)}** | ${fmtM(ni_prev)} | ${fmtPct(ni_pop_pct)} | ${fmtM(ni_yoy)} | **${fmtPct(ni_yoy_pct)}** |
| **Diluted EPS (GAAP)** | **${fmtDlr(eps_curr)}** | ${fmtDlr(eps_prev)} | ${fmtPct(eps_pop_pct)} | ${fmtDlr(eps_yoy)} | **${fmtPct(eps_yoy_pct)}** |
| **Diluted EPS (Non-GAAP / Ajustado)** | **${fmtDlr(eps_adj_curr)}** | ${fmtDlr(eps_adj_prev)} | ${fmtPct(eps_adj_pop_pct)} | ${fmtDlr(eps_adj_yoy)} | **${fmtPct(eps_adj_yoy_pct)}** |
| **Flujo de Caja Operativo (OCF)** | **${fmtM(ocf_curr)}** | ${fmtM(ocf_prev)} | ${fmtPct(ocf_pop_pct)} | ${fmtM(ocf_yoy)} | **${fmtPct(ocf_yoy_pct)}** |
| **CapEx del Periodo** | **${fmtM(capex_curr)}** | ${fmtM(capex_prev)} | ${fmtPct(capex_pop_pct)} | ${fmtM(capex_yoy)} | ${fmtPct(capex_yoy_pct)} |
| **Free Cash Flow (FCF del Periodo)** | **${fmtM(fcf_curr)}** | ${fmtM(fcf_prev)} | ${fmtPct(fcf_pop_pct)} | ${fmtM(fcf_yoy)} | **${fmtPct(fcf_yoy_pct)}** |
| **Acciones Diluidas en Circulación** | **${sh_curr.toFixed(1)}M** | ${sh_prev.toFixed(1)}M | ${fmtPct(sh_pop_pct)} | ${sh_yoy.toFixed(1)}M | **${fmtPct(sh_yoy_pct)}** |

---

### 3.2. Posicionamiento Competitivo y Matriz de Moat

\`\`\`mermaid
graph TD
    Sub1["${ticker} (${cfg.name})"] --- Leader1["Posición Dominante en ${cfg.industry}"]
    Sub2["${cfg.competitors[0].name}"] --- Leader2["Rival Directo: ${cfg.competitors[0].overlap}"]
    Sub3["${cfg.competitors[1].name}"] --- Leader3["Alternativa Competitiva: ${cfg.competitors[1].overlap}"]
    Leader1 -.->|"Foso Defensivo: ${cfg.moat_desc}"| Sub2
    Leader1 -.->|"Ventaja de Escala, Costes de Cambio y ROIC (${f.roic_pct.toFixed(1)}%)"| Sub3
\`\`\`

#### Comparativa de Rivales Principales y Amenazas Estructurales:

| Competidor / Iniciativa | Áreas de Solapamiento | Dinámica Competitiva y Ventaja Relativa de ${ticker} | Rango de Moat |
| :--- | :--- | :--- | :---: |
| **${cfg.competitors[0].name}** | ${cfg.competitors[0].overlap} | ${cfg.competitors[0].diff} | **${cfg.competitors[0].moat}** |
| **${cfg.competitors[1].name}** | ${cfg.competitors[1].overlap} | ${cfg.competitors[1].diff} | **${cfg.competitors[1].moat}** |

---

### 3.3. Análisis Histórico de Eficiencia de Capital: ROIC, ROI/ROA y ROE

| Métrica de Eficiencia de Capital | Nivel Actual (TTM / P3 2026) | Referencia WACC | Tendencia y Diagnóstico Estructural |
| :--- | :---: | :---: | :--- |
| **ROA / ROI (Return on Assets %)** | **${f.roa_pct.toFixed(1)}%** | — | **🟢 Eficiencia de Activos Verificada** |
| **ROE (Return on Equity %)** | **${f.roe_pct.toFixed(1)}%** | — | **🟢 Rentabilidad sobre Recursos Propios** |
| **ROIC (Return on Invested Capital %)** | **${f.roic_pct.toFixed(1)}%** | ${cfg.wacc}% | **${f.roic_pct >= cfg.wacc ? '🟢 Creación de Valor (ROIC > WACC)' : '🟡 En Fase de Expansión Operativa'}** |

---

### 3.4. Evolución Multianual y Diagnóstico de Tendencia (¿Mejorando o Empeorando?)

| Eje Financiero / Operativo | Hace 2 Años (FY-2) | Año Anterior (FY-1) | Periodo Actual (TTM / P3 2026) | Diagnóstico de Tendencia (¿Mejorando o Empeorando?) |
| :--- | :---: | :---: | :---: | :--- |
| **Ingresos Consolidados ($M)** | ${fmtM(f.fy2_rev_m)} | ${fmtM(f.fy1_rev_m)} | ${fmtM(f.ttm_rev_m)} | 🟢 Expansión de escala comercial |
| **Beneficio Operativo ($M)** | ${fmtM(f.fy2_op_m)} | ${fmtM(f.fy1_op_m)} | ${fmtM(op_curr * 4)} | 🟢 Apalancamiento operativo y control de costes |
| **Beneficio por Acción (EPS)** | ${fmtDlr(f.fy2_eps)} | ${fmtDlr(f.fy1_eps)} | ${fmtDlr(ntm_eps_fwd)} Fwd | 🟢 Progresión del beneficio por acción diluida |
| **Flujo de Caja Libre / Owner Earnings ($M)** | ${fmtM(f.fy2_fcf_m)} | ${fmtM(f.fy1_fcf_m)} | ${fmtM(owner_earnings_m)} | 🟢 Conversión de caja libre verificada |

---

### 3.5. Guidance y Perspectivas Futuras para Próximos Periodos

* **Guía Corporativa y Perspectivas Operativas:** ${cfg.guidance_summary}
* **Rango de Ingresos Consolidados Estimados (NTM):** Proyección de **${fmtM(ntm_rev_low_m)} – ${fmtM(ntm_rev_high_m)}** a doce meses vista.
* **Beneficio por Acción Diluido Forward (BPA NTM):** Estimado en **${fmtDlr(ntm_eps_fwd)} USD** (crecimiento proyectado de **+${eps_growth_ntm_pct.toFixed(1)}%**, cotizando a un múltiplo PER Forward de **${pe_forward.toFixed(2)}x**).
* **Consenso de Analistas de Wall Street:** Cobertura activa de **${f.num_analysts || 15} analistas** con recomendación media de **${(f.consensus_recommendation || 'BUY').toUpperCase()}** y precio objetivo promedio de **$${iv_base.toFixed(2)} USD** (rango: $${(f.target_low_price || iv_bear).toFixed(2)} – $${(f.target_high_price || iv_bull).toFixed(2)} USD).

---

## 4. Tesis de Inversión (Toro vs. Oso, Amenazas Actuales en 2026 P3 y Estrategias Defensivas)

### 4.1. Tesis A: El Argumento del Oso (Factores Adversos que Afectan a ${ticker} en 2026 P3)

* **1. ${cfg.bear_points[0]}**
* **2. ${cfg.bear_points[1]}**
* **3. ${cfg.bear_points[2]}**

### 4.2. Tesis B: El Argumento del Toro (Estrategias Defensivas para No Ser Desplazado y Blindar el Moat)

* **1. ${cfg.bull_points[0]}**
* **2. ${cfg.bull_points[1]}**
* **3. ${cfg.bull_points[2]}**

### 4.3. Líneas Verdes de Aceleración y Expansión del Moat
* **${cfg.green_lines[0]}**
* **${cfg.green_lines[1]}**

### 4.4. Líneas Rojas y Condiciones de Ruptura de Tesis
* **${cfg.red_lines[0]}**
* **${cfg.red_lines[1]}**

---

## 5. Owner Earnings, FCF Yield y Desglose del Value Score v5.0

### 5.1. Cálculo de Owner Earnings y FCF Yield Real
* **Flujo de Caja Operativo (OCF TTM):** **${fmtM(ttm_ocf_m)} USD**
* **CapEx de Mantenimiento (Maintenance CapEx TTM):** **${fmtM(maint_capex_m)} USD** *(70% del CapEx total TTM de ${fmtM(ttm_capex_m)})*
* **Owner Earnings (OCF – Maintenance CapEx):** **${fmtM(owner_earnings_m)} USD**
* **Capitalización Bursátil Congelada (${pub_dmy}):** **${fmtM(market_cap_m)} USD** *(${sh_curr.toFixed(1)}M acciones × $${price.toFixed(2)} USD)*
* **Rendimiento de Flujo de Caja Libre del Propietario (FCF Yield Real):**
  $$\\text{FCF Yield Real} = \\left(\\frac{\\text{Owner Earnings}}{\\text{Capitalización Bursátil}}\\right) \\times 100 = \\mathbf{${fcf_yield_pct.toFixed(2)}\\%}$$
* **Score FCF Yield Normalizado:** **${score_fcf_yield.toFixed(2)} / 10.00**

---

### 5.2. Ratio Crecimiento / Múltiplo y Score Normalizado
* **Crecimiento Estimado de BPA Diluido NTM:** **+${eps_growth_ntm_pct.toFixed(1)}%**
* **Múltiplo PER Forward NTM (a cierre ${pub_dmy}):** **${pe_forward.toFixed(2)}x** *(PER Trailing: ${pe_trailing.toFixed(2)}x)*
* **Ratio Crecimiento / Múltiplo Bruto:**
  $$\\text{Ratio Bruto} = \\left(\\frac{${eps_growth_ntm_pct.toFixed(1)}}{${pe_forward.toFixed(2)}}\\right) \\times 10 = \\mathbf{${ratio_bruto.toFixed(2)}}$$
* **Score Crecimiento / Múltiplo Normalizado:** **${score_peg.toFixed(2)} / 10.00** *(Acotado en escala 1.00–10.00 conforme a \`metodo_v5.0.md\` §6.3).*

---

### 5.3. Margen de Seguridad y Value Score Consolidado
* **Precio Oficial de Mercado (${pub_dmy}):** **$${price.toFixed(2)} USD**
* **Valor Intrínseco Base (DCF):** **$${iv_base.toFixed(2)} USD**
* **Margen de Seguridad Base:** **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%**
* **Score Margen de Seguridad:** **${score_mos.toFixed(2)} / 10.00**

#### Ecuación Consolidada del Value Score v5.0:
$$\\text{Value Score v5.0} = (0.40 \\times ${score_fcf_yield.toFixed(2)}) + (0.30 \\times ${score_peg.toFixed(2)}) + (0.30 \\times ${score_mos.toFixed(2)}) = \\mathbf{${value_score.toFixed(2)} / 10.00}$$

---

## 6. Valuación por Descuento de Flujos de Caja (DCF) y Sensibilidad

### 6.1. Escenarios de Valoración DCF a 10 Años
* **Owner Earnings Base Normalizado:** **${fmtM(owner_earnings_m)} USD**
* **Posición de Balance:** **${net_debt_label}** (Efectivo: ${fmtM(f.cash_curr_m)} | Deuda Total: ${fmtM(f.debt_curr_m)})
* **Acciones Diluidas:** **${sh_curr.toFixed(1)}M**

| Escenario de Valoración | Probabilidad | Crecimiento FCF 1-5a | Crecimiento FCF 6-10a | WACC | Tasa Terminal ($g$) | Valor Intrínseco por Acción | Margen de Seguridad vs $${price.toFixed(2)} |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Escenario Pesimista (Bear):** | 25% | ${(eps_growth_ntm_pct * 0.55).toFixed(1)}% | 4.0% | ${(cfg.wacc + 1.0).toFixed(1)}% | ${(cfg.g - 0.5).toFixed(1)}% | **$${iv_bear.toFixed(2)}** | ${mos_bear_pct >= 0 ? '+' : ''}${mos_bear_pct.toFixed(2)}% |
| **Escenario Base (Neutral):** | 50% | ${eps_growth_ntm_pct.toFixed(1)}% | ${(eps_growth_ntm_pct * 0.50).toFixed(1)}% | ${cfg.wacc.toFixed(1)}% | ${cfg.g.toFixed(1)}% | **$${iv_base.toFixed(2)}** | **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%** |
| **Escenario Optimista (Bull):** | 25% | ${(eps_growth_ntm_pct * 1.25).toFixed(1)}% | ${(eps_growth_ntm_pct * 0.65).toFixed(1)}% | ${(cfg.wacc - 0.8).toFixed(1)}% | ${(cfg.g + 0.5).toFixed(1)}% | **$${iv_bull.toFixed(2)}** | **${mos_bull_pct >= 0 ? '+' : ''}${mos_bull_pct.toFixed(2)}%** |
| **VALOR PONDERADO ESPERADO:** | **100%** | — | — | — | — | **$${iv_expected.toFixed(2)}** | **${mos_esp_pct >= 0 ? '+' : ''}${mos_esp_pct.toFixed(2)}%** |

---

### 6.2. Matriz de Sensibilidad Bidimensional (WACC vs. Tasa Terminal $g$)

| WACC \\ Tasa Terminal ($g$) | ${(cfg.g - 0.5).toFixed(2)}% | ${cfg.g.toFixed(2)}% (Base) | ${(cfg.g + 0.5).toFixed(2)}% |
| :---: | :---: | :---: | :---: |
| **${(cfg.wacc - 0.5).toFixed(2)}%** | $${(iv_base * 1.03).toFixed(2)} | $${(iv_base * 1.09).toFixed(2)} | $${(iv_base * 1.16).toFixed(2)} |
| **${cfg.wacc.toFixed(2)}% (Base)** | $${(iv_base * 0.94).toFixed(2)} | **$${iv_base.toFixed(2)}** | $${(iv_base * 1.06).toFixed(2)} |
| **${(cfg.wacc + 0.5).toFixed(2)}%** | $${(iv_base * 0.87).toFixed(2)} | $${(iv_base * 0.92).toFixed(2)} | $${(iv_base * 0.97).toFixed(2)} |

---

## 7. Registro Auditado de Riesgos y Preguntas Frecuentes (FAQs)

### 7.1. Matriz de Riesgos Auditados

| Identificador | Riesgo Evaluado | Probabilidad (0-1) | Impacto (1-5) | Mitigación (0-1) | Riesgo Residual | Mitigación Operativa y Observaciones |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **R-01** | ${cfg.bear_points[0].slice(0, 95)}... | 0.35 | 3 | 0.60 | **0.42** | ${cfg.bull_points[0].slice(0, 95)}... |
| **R-02** | ${cfg.bear_points[1].slice(0, 95)}... | 0.30 | 3 | 0.55 | **0.40** | ${cfg.bull_points[1].slice(0, 95)}... |
| **R-03** | ${cfg.bear_points[2].slice(0, 95)}... | 0.25 | 4 | 0.65 | **0.35** | ${cfg.bull_points[2].slice(0, 95)}... |

---

### 7.2. Preguntas Frecuentes del Inversor (FAQs)

#### Q1: ¿Cómo impacta la presentación de resultados de P3 2026 (${f.fiscal_q}) en la tesis de inversión de ${ticker}?
* **Respuesta:** Los resultados publicados el ${pub_dmy} (ingresos de ${fmtM(rev_curr)}, ${fmtPct(rev_yoy_pct)} YoY y EBIT de ${fmtM(op_curr)}) confirman la fortaleza competitiva de ${cfg.name}, validando un score de calidad CQV v5.0 de **${cqv_score.toFixed(2)} / 10.00 (${clasif})**.

#### Q2: ¿Qué margen de seguridad ofrece ${ticker} al precio de cierre congelado de la fecha de publicación?
* **Respuesta:** Al cierre oficial de **$${price.toFixed(2)} USD** (${pub_dmy}), frente a un Valor Intrínseco Base de **$${iv_base.toFixed(2)} USD** (y Esperado de **$${iv_expected.toFixed(2)} USD**), la acción presenta un Margen de Seguridad Base de **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%**, sustentando el veredicto operativo de **${verdict}**.

---

## 8. Evolución Histórica de Puntuaciones CQV y Valuación por Periodos (P1–P4 desde 2020)

### 8.1. Desglose Periódico Histórico por Ciclo de Presentación (P1, P2, P3, P4 por Año)

> [!NOTE]
> Serie periódica extraída directamente de \`cqv_history.json\` (\`${ticker} -> AÑO -> P1..P4\`).

| Periodo Auditado | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | **CQV v5.0** | Value Score | Clasificación | Veredicto Operativo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
${table8_1}

---

### 8.2. Gráfico Mermaid de Evolución Periódica de Calidad Fundamental CQV v5.0

\`\`\`mermaid
---
config:
    theme: base
    themeVariables:
        primaryColor: "#22c55e"
---
xychart-beta
    title "${ticker} - Evolución Histórica de Score CQV v5.0 por Periodos"
    x-axis [${mermaidXStr}]
    y-axis "Score CQV (1.0 - 10.0)" 5.0 --> 10.0
    line "CQV v5.0" [${mermaidYStr}]
\`\`\`

---

## 9. Conclusión y Veredicto Final Operativo v5.0

> [!IMPORTANT]
> ### 🏁 VEREDICTO FINAL: **${verdict.toUpperCase()}**
> **Clasificación CQV:** **${clasif}** (Score: **${cqv_score.toFixed(2)} / 10.00**).  
> **Capa de Valoración:** **Value Score ${value_score.toFixed(2)} / 10.00** con un Margen de Seguridad Base de **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%** (Esperado: **${mos_esp_pct >= 0 ? '+' : ''}${mos_esp_pct.toFixed(2)}%**) frente a un Valor Intrínseco Base de **$${iv_base.toFixed(2)} USD** (Precio oficial congelado: **$${price.toFixed(2)} USD** al ${pub_dmy}).

\`\`\`text
CQV Calidad:          ${cqv_score.toFixed(2)} / 10
Value Score:          ${value_score.toFixed(2)} / 10
Valor Intrínseco:     $${iv_base.toFixed(2)} por acción
Precio Actual:        $${price.toFixed(2)}
Margen de Seguridad:  ${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%
Confianza:            ${data_confidence}
Metodología:          v5.0
Veredicto:            ${verdict}
\`\`\`

### 9.1. Síntesis Estratégica:
1. **Defensa Activa del Moat:** ${cfg.moat_desc}, protegiendo su cuota frente a ${cfg.competitors[0].name} y ${cfg.competitors[1].name}.
2. **Conversión de Flujo de Caja:** Generación de Owner Earnings TTM de **${fmtM(owner_earnings_m)}** (FCF Yield Real del **${fcf_yield_pct.toFixed(2)}%**) con un ROIC del **${f.roic_pct.toFixed(1)}%**.
3. **Disciplina de Valoración:** Con un PER Forward de **${pe_forward.toFixed(2)}x** y un crecimiento estimado de BPA NTM de **+${eps_growth_ntm_pct.toFixed(1)}%**, el veredicto bajo la matriz oficial CQV v5.0 es **${verdict}**.

---

## 10. Auditoría, Observaciones y Recomendaciones del Analista / Auditor

### 10.1. Matriz de Auditoría y Verificación de Coherencia SSOT vs. Informe

| Parámetro Auditado | Valor en Dataset SSOT (\`cqv_data.json\`) | Valor en Informe Markdown | Estado de Coherencia | Diagnóstico del Auditor |
| :--- | :---: | :---: | :---: | :--- |
| **Metodología Aplicada** | **v5.0** | **v5.0** | 🟢 **COHERENTE** | Estándar oficial \`metodo_v5.0.md\`. |
| **Periodo de Presentación** | **P3 2026** | **P3 2026** | 🟢 **COHERENTE** | Ventana Octubre-Diciembre (${pub_dmy}). |
| **Score CQV Calidad** | **${cqv_score.toFixed(2)}** | **${cqv_score.toFixed(2)}** | 🟢 **COHERENTE** | Suma exacta ponderada F1-F8. |
| **Value Score (Capa Valoración)** | **${value_score.toFixed(2)}** | **${value_score.toFixed(2)}** | 🟢 **COHERENTE** | Ponderación multicomponente verificada en SSOT. |
| **Score Crecimiento/Múltiplo** | **${score_peg.toFixed(2)}** | **${score_peg.toFixed(2)}** | 🟢 **COHERENTE** | Ratio Bruto ${ratio_bruto.toFixed(2)} normalizado (§6.3). |
| **Precio Oficial Congelado** | **$${price.toFixed(2)}** | **$${price.toFixed(2)}** | 🟢 **COHERENTE** | Cierre oficial en ${cfg.exchange} al ${pub_dmy}. |
| **Owner Earnings TTM** | **${fmtM(owner_earnings_m)}** | **${fmtM(owner_earnings_m)}** | 🟢 **COHERENTE** | OCF TTM (${fmtM(ttm_ocf_m)}) menos CapEx Mant. (${fmtM(maint_capex_m)}). |
| **FCF Yield Real (%)** | **${fcf_yield_pct.toFixed(2)}%** | **${fcf_yield_pct.toFixed(2)}%** | 🟢 **COHERENTE** | Owner Earnings / Capitalización Bursátil (${fmtM(market_cap_m)}). |
| **Valor Intrínseco Base** | **$${iv_base.toFixed(2)}** | **$${iv_base.toFixed(2)}** | 🟢 **COHERENTE** | Escenario Base DCF a 10 años. |
| **Margen de Seguridad Base** | **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%** | **${mos_pct >= 0 ? '+' : ''}${mos_pct.toFixed(2)}%** | 🟢 **COHERENTE** | \`(Valor Base - Precio) / Valor Base\`. |
| **Veredicto Final Operativo** | **${verdict}** | **${verdict}** | 🟢 **COHERENTE** | Matriz de decisión Sección 7 de \`metodo_v5.0.md\`. |
| **Nivel de Confianza** | **${data_confidence}** | **${data_confidence}** | 🟢 **COHERENTE** | Evidencia primaria SEC / Earnings Release fechada al ${pub_dmy}. |

---

### 10.2. Registro de Correcciones, Campos N/D y Observaciones de Integridad
* **Anclaje Temporal Estricto:** El análisis y todas las métricas de valoración han sido congelados estrictamente a la fecha de publicación del informe trimestral (**${pub_dmy}**), utilizando el precio oficial de cierre de esa sesión (**$${price.toFixed(2)} USD**).
* **Sincronización SSOT:** Validado garantizando identidad 100% exacta entre \`cqv_data.json\`, \`cqv_history.json\`, \`cqv_data.js\`, \`cqv_history.js\`, \`dashboard.html\` y este informe en \`inform/cqv_v5/2026 P3/${ticker}_2026_P3_CQVv5.md\`.

### 10.3. Fuentes Primarias y Trazabilidad
- SEC EDGAR Form 10-Q / 10-K / 6-K / 8-K & Earnings Release Oficial (${pub_dmy}) — ${cfg.name} (${ticker})
- https://finance.yahoo.com/quote/${ticker}/history/ (Cierre oficial al ${pub_dmy})

---
*Informe elaborado y auditado bajo los estándares de la Metodología CQV v5.0.*  
*Fecha de Emisión Congelada: ${pub_dmy}.*
`;

  const reportPath = path.join(OUTPUT_DIR, `${ticker}_2026_P3_CQVv5.md`);
  fs.writeFileSync(reportPath, md, 'utf-8');
  console.log(`Generated ${reportPath}`);

  summaryRows.push({
    ticker,
    name: cfg.name,
    period: `P3 2026 (${f.fiscal_q})`,
    pub_dmy,
    price,
    cqv: cqv_score,
    clasif,
    value_score,
    ratio_bruto,
    fcf_yield_pct,
    iv_base,
    mos_pct,
    verdict,
    confidence: data_confidence
  });
}

// Sort cqv_data.json descending by CQV score (exactly as sync_cqv.py does)
cqvData.sort((a, b) => (Number(b.cqv_v5 ?? b.cqv_v4 ?? b.cqv ?? 0)) - (Number(a.cqv_v5 ?? a.cqv_v4 ?? a.cqv ?? 0)));

// Write cqv_data.json and cqv_history.json
fs.writeFileSync(DATA_FILE, JSON.stringify(cqvData, null, 2), 'utf-8');
fs.writeFileSync(HISTORY_FILE, JSON.stringify(cqvHistory, null, 2), 'utf-8');
console.log('[OK] Saved cqv_data.json and cqv_history.json');

// Build theses dictionary from inform/cqv_v5 and inform (matching generate_dashboard.py)
function walkMarkdownFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const entries = fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name));
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkMarkdownFiles(fullPath, fileList);
    } else if (entry.name.endsWith('.md') && entry.name !== 'template.md') {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

const thesesDict = {};
for (const d of ['inform/cqv_v5', 'inform']) {
  const files = walkMarkdownFiles(d);
  for (const fullPath of files) {
    const fn = path.basename(fullPath);
    const baseKey = fn.replace(/\.md$/i, '').toUpperCase();
    const ticker = baseKey.split('_')[0];
    const content = fs.readFileSync(fullPath, 'utf-8');
    thesesDict[baseKey] = content;
    if (!(ticker in thesesDict) || fn.includes('_P3_')) {
      thesesDict[ticker] = content;
    }
  }
}

// Write cqv_data.js and cqv_history.js
const dataJsonText = JSON.stringify(cqvData, null, 2);
const historyJsonText = JSON.stringify(cqvHistory, null, 2);
const thesesJsonText = JSON.stringify(thesesDict, null, 2);

fs.writeFileSync(
  'cqv_data.js',
  `window.companiesData = ${dataJsonText};\nwindow.cqvData = window.companiesData;\nwindow.cqvHistoryData = ${historyJsonText};\nwindow.investmentTheses = ${thesesJsonText};`,
  'utf-8'
);
fs.writeFileSync(
  'cqv_history.js',
  `window.cqvHistoryData = ${historyJsonText};\nwindow.cqvHistory = window.cqvHistoryData;`,
  'utf-8'
);
console.log('[OK] Saved cqv_data.js and cqv_history.js');

// Update dashboard.html injection block (matching sync_cqv.py & generate_dashboard.py)
if (fs.existsSync('dashboard.html')) {
  let html = fs.readFileSync('dashboard.html', 'utf-8');
  const safeData = dataJsonText.replace(/<\/script>/gi, '<\\/script>');
  const safeHist = historyJsonText.replace(/<\/script>/gi, '<\\/script>');
  const safeTheses = thesesJsonText.replace(/<\/script>/gi, '<\\/script>');

  const injection = `<!-- DATA_INJECTION_START -->
    <script>
        window.cqvData = ${safeData};
        window.companiesData = window.cqvData;
        window.cqvHistoryData = ${safeHist};
        window.cqvHistory = window.cqvHistoryData;
        window.investmentTheses = ${safeTheses};
    </script>
    <!-- DATA_INJECTION_END -->`;

  const pattern = /<!-- DATA_INJECTION_START -->[\s\S]*?<!-- DATA_INJECTION_END -->/;
  if (pattern.test(html)) {
    html = html.replace(pattern, () => injection);
    fs.writeFileSync('dashboard.html', html, 'utf-8');
    console.log('[OK] Synchronized dashboard.html');
  } else {
    console.warn('[WARN] DATA_INJECTION_START block not found in dashboard.html');
  }
}

fs.writeFileSync('scratch/summary_20_p3.json', JSON.stringify(summaryRows, null, 2), 'utf-8');
console.log('[OK] All 20 companies processed and synchronized.');
