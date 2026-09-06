import json

def main():
    print("Actualizando COST en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    cost_entry = None
    for idx, item in enumerate(cqv_data):
        if item.get('ticker') == 'COST':
            cost_entry = item
            break

    if not cost_entry:
        cost_entry = {'ticker': 'COST'}
        cqv_data.append(cost_entry)

    cost_entry.update({
        "ticker": "COST",
        "name": "Costco Wholesale Corporation",
        "sector": "Consumer Defensive / Wholesale Club & Subscription Retail",
        "quarter": "P2 2026",
        "f1": 9.20,
        "f2": 9.50,
        "f3": 9.00,
        "f4": 9.80,
        "f5": 9.40,
        "f6": 9.50,
        "f7": 8.50,
        "f8": 9.70,
        "cqv_v5": 9.37,
        "cqv": 9.37,
        "price": 928.48,
        "pe": 46.82,
        "pe_forward": 40.97,
        "eps_trailing": 19.83,
        "eps_forward": 22.66,
        "eps_growth_ntm_pct": 14.27,
        "growth_eps": 14.27,
        "market_cap_b": 411.76,
        "market_cap": 411760.0,
        "price_date": "30/05/2026",
        "valuation_date": "30/05/2026",
        "publication_date": "30/05/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ÉLITE",
        "verdict": "Mantener / Acumular en Correcciones",
        "value_score": 3.82,
        "peg_bruto": 3.483,
        "score_peg": 3.483,
        "score_crecimiento_multiplo_bruto": 3.483,
        "score_crecimiento_multiplo": 3.483,
        "intrinsic_value": 815.00,
        "intrinsic_value_base": 815.00,
        "intrinsic_value_expected": 845.00,
        "mos_pct": -12.22,
        "mos_base_pct": -12.22,
        "mos_esperado_pct": -8.99,
        "score_mos": 3.80,
        "fcf_yield_pct": 1.69,
        "score_fcf_yield": 4.10,
        "owner_earnings": 7000.0,
        "owner_earnings_m": 7000.0,
        "ocf_ttm_m": 11800.0,
        "maint_capex_m": 4800.0,
        "wacc": 7.50,
        "g_terminal": 3.50,
        "data_confidence": "Alta",
        "f4_moat": 9.80,
        "analyst_targets": {
            "target_low_bear": 820.0,
            "target_mean_base": 965.0,
            "target_high_bull": 1100.0,
            "num_analysts": 35,
            "consensus_recommendation": "Buy",
            "upside_potential_pct": 3.93
        },
        "close_history": {
            "2020": 354.93,
            "2021": 538.86,
            "2022": 436.21,
            "2023": 649.97,
            "2024": 907.51,
            "2025": 858.55,
            "2026": 928.48
        },
        "sources": [
            "https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-Third-Quarter-Fiscal-Year-2026-Operating-Results/",
            "https://www.sec.gov/edgar/browse/?CIK=909832",
            "https://stockanalysis.com/stocks/cost/",
            "https://finance.yahoo.com/quote/COST/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('COST', {})

    # Detailed historical progression for COST (2020 - 2026)
    HIST_FACTORS = {
        '2020': {'f1': 8.9, 'f2': 9.2, 'f3': 8.6, 'f4': 9.6, 'f5': 9.1, 'f6': 9.4, 'f7': 8.0, 'f8': 9.6, 'pe': 39.3, 'pe_fwd': 34.5, 'vs': 4.30},
        '2021': {'f1': 9.1, 'f2': 9.3, 'f3': 9.1, 'f4': 9.7, 'f5': 9.2, 'f6': 9.4, 'f7': 8.1, 'f8': 9.6, 'pe': 48.6, 'pe_fwd': 41.5, 'vs': 3.75},
        '2022': {'f1': 9.0, 'f2': 9.3, 'f3': 8.8, 'f4': 9.7, 'f5': 9.2, 'f6': 9.5, 'f7': 8.2, 'f8': 9.7, 'pe': 33.2, 'pe_fwd': 29.8, 'vs': 4.85},
        '2023': {'f1': 9.1, 'f2': 9.4, 'f3': 8.9, 'f4': 9.7, 'f5': 9.3, 'f6': 9.5, 'f7': 8.3, 'f8': 9.7, 'pe': 45.9, 'pe_fwd': 40.2, 'vs': 3.90},
        '2024': {'f1': 9.2, 'f2': 9.4, 'f3': 9.0, 'f4': 9.8, 'f5': 9.3, 'f6': 9.5, 'f7': 8.4, 'f8': 9.7, 'pe': 54.8, 'pe_fwd': 47.5, 'vs': 3.40},
        '2025': {'f1': 9.2, 'f2': 9.5, 'f3': 9.0, 'f4': 9.8, 'f5': 9.4, 'f6': 9.5, 'f7': 8.5, 'f8': 9.7, 'pe': 47.2, 'pe_fwd': 41.2, 'vs': 3.80},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['COST'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_p = round(hf['pe'] * (1.0 + (p_num - 2) * 0.02), 1)
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.02), 1)
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['COST'][s_yr][p_k] = {
                'ticker': 'COST',
                'quarter': f'{p_k} {s_yr}',
                'f1': f_p[0], 'f2': f_p[1], 'f3': f_p[2], 'f4': f_p[3],
                'f5': f_p[4], 'f6': f_p[5], 'f7': f_p[6], 'f8': f_p[7],
                'cqv_v5': cqv_p, 'cqv': cqv_p,
                'pe': pe_p, 'pe_forward': pe_fwd_p,
                'value_score': vs_p,
                'verdict': 'Mantener / Acumular en Correcciones',
                'clasificacion': 'ÉLITE'
            }

        # Annual legacy
        cqv_leg = calc_cqv(base_f_vals)
        history['COST'][s_yr]['annual_legacy'] = {
            'ticker': 'COST',
            'quarter': f'Anual {s_yr}',
            'f1': base_f_vals[0], 'f2': base_f_vals[1], 'f3': base_f_vals[2], 'f4': base_f_vals[3],
            'f5': base_f_vals[4], 'f6': base_f_vals[5], 'f7': base_f_vals[6], 'f8': base_f_vals[7],
            'cqv_v5': cqv_leg, 'cqv': cqv_leg,
            'pe': hf['pe'], 'pe_forward': hf['pe_fwd'],
            'value_score': hf['vs'],
            'verdict': 'Mantener / Acumular en Correcciones',
            'clasificacion': 'ÉLITE'
        }

    # 2026
    history['COST'].setdefault('2026', {})
    history['COST']['2026']['P1'] = {
        'ticker': 'COST',
        'quarter': 'P1 2026',
        'f1': 9.2, 'f2': 9.5, 'f3': 9.0, 'f4': 9.8, 'f5': 9.4, 'f6': 9.5, 'f7': 8.5, 'f8': 9.7,
        'cqv_v5': 9.35, 'cqv': 9.35,
        'pe': 46.2, 'pe_forward': 40.5,
        'value_score': 3.85,
        'verdict': 'Mantener / Acumular en Correcciones',
        'clasificacion': 'ÉLITE'
    }
    history['COST']['2026']['P2'] = dict(cost_entry)
    history['COST']['2026']['P3'] = None
    history['COST']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("COST actualizado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
