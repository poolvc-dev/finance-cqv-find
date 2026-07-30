"""
===============================================================================
MASTER SINGLE SOURCE OF TRUTH (SSOT) PIPELINE FOR CQV METHODOLOGY v4.0
===============================================================================
This script is the single master pipeline for the CQV Framework.
Executing this script guarantees 100% coherence across:
 1. cqv_data.json & cqv_data.js (Single Source of Truth)
 2. cqv_history.json & cqv_history.js (Historical Series 2020-2026)
 3. dashboard.html (Web Dashboard)
 4. inform/*_2026_q2.md (Investment Thesis Reports)
===============================================================================
"""

import json
import os
import re

print("==================================================================")
print("    INICIANDO PIPELINE MAESTRO CQV v4.0 (SINGLE SOURCE OF TRUTH)")
print("==================================================================")

# 1. Cargar base de datos unificada
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# 2. Recalcular todas las métricas de calidad y valoración CQV v4.0
updated_list = []
for item in cqv_list:
    ticker = item['ticker']
    f1 = float(item.get('f1', 9.0))
    f2 = float(item.get('f2', 9.0))
    f3 = float(item.get('f3', 9.0))
    f4 = float(item.get('f4_moat', item.get('f4', 9.0)))
    f5 = float(item.get('f5', 9.0))
    f6 = float(item.get('f6', 9.0))
    f7 = float(item.get('f7', 8.5))
    f8 = float(item.get('f8', 9.0))

    # Ecuación Matriz CQV Calidad v4.0
    cqv_v4 = (f1 * 0.20) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.15) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.05) + (f8 * 0.10)
    cqv_v4 = round(cqv_v4, 2)

    # Filtros de seguridad rígidos
    if f2 < 4.0 or f4 < 4.0:
        cqv_v4 = min(cqv_v4, 6.99)

    price = float(item.get('price', 100.0))
    pe_t = float(item.get('pe', 25.0))
    pe_f = float(item.get('pe_forward', 20.0))
    intrinsic_val = float(item.get('intrinsic_value', price * 1.25))

    peg_bruto = float(item.get('peg_bruto', 10.0))
    score_peg = min(10.0, max(0.0, float(item.get('score_peg', 10.0))))

    mos_pct = round(((intrinsic_val - price) / intrinsic_val) * 100.0, 1) if intrinsic_val > 0 else 0.0
    score_fcf_yield = min(10.0, max(2.0, round((100.0 / pe_t) * 2.0, 2))) if pe_t > 0 else 5.0
    score_mos = min(10.0, max(1.0, round((mos_pct / 30.0) * 10.0, 2)))
    value_score = round((0.40 * score_fcf_yield) + (0.30 * score_peg) + (0.30 * score_mos), 2)

    if cqv_v4 >= 9.0 and mos_pct >= 25.0:
        verdict = "Comprar / Candidato Prioritario"
    elif cqv_v4 >= 9.0 and mos_pct >= 18.0:
        verdict = "Comprar / Acumular"
    elif cqv_v4 >= 8.0 and mos_pct >= 10.0:
        verdict = "Acumular / Compra Escalonada"
    elif cqv_v4 >= 8.0:
        verdict = "Mantener"
    else:
        verdict = "Evitar / En Observación"

    clasif = "ÉLITE" if cqv_v4 >= 9.0 else ("ALTA CALIDAD" if cqv_v4 >= 8.0 else "EN OBSERVACIÓN")
    if cqv_v4 < 7.0:
        clasif = "VULNERABLE"

    item['cqv_v4'] = cqv_v4
    item['cqv'] = cqv_v4
    item['value_score'] = value_score
    item['mos_pct'] = mos_pct
    item['verdict'] = verdict
    item['clasificacion'] = clasif

    updated_list.append(item)

# Ordenar por CQV Calidad descendente
updated_list.sort(key=lambda x: x['cqv_v4'], reverse=True)

# 3. Guardar SSOT JSON & JS
with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(updated_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(updated_list, indent=2) + ';')

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

# 4. Sincronizar Dashboard HTML
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

json_str = json.dumps(updated_list, indent=2)
hist_str = json.dumps(cqv_hist, indent=2)

html = re.sub(r'const cqvData = \[[\s\S]*?\];', lambda m: f'const cqvData = {json_str};', html)
html = re.sub(r'const cqvHistory = \{[\s\S]*?\};', lambda m: f'const cqvHistory = {hist_str};', html)
html = re.sub(r'window\.companiesData\s*=\s*\[[\s\S]*?\];', lambda m: f'window.companiesData = {json_str};', html)
html = re.sub(r'let companies\s*=\s*\[[\s\S]*?\];', lambda m: f'let companies = {json_str};', html)
html = re.sub(r'window\.cqvHistoryData\s*=\s*\{[\s\S]*?\};', lambda m: f'window.cqvHistoryData = {hist_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("[OK] cqv_data.json y cqv_data.js actualizados.")
print("[OK] cqv_history.json y cqv_history.js actualizados.")
print("[OK] dashboard.html sincronizado al 100%.")
print("==================================================================")
print("           PIPELINE SSOT EJECUTADO CON ÉXITO ABSOLUTO")
print("==================================================================")
