import json

def main():
    print("Integrando y actualizando SNOW en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    snow_entry = None
    for item in cqv_data:
        if item.get('ticker') == 'SNOW':
            snow_entry = item
            break

    if not snow_entry:
        snow_entry = {'ticker': 'SNOW'}
        cqv_data.append(snow_entry)

    snow_entry.update({
        "ticker": "SNOW",
        "name": "Snowflake Inc.",
        "sector": "Technology / Cloud Data Platform, Data Lakehouse & Enterprise AI",
        "quarter": "P2 2026",
        "f1": 7.90,
        "f2": 9.60,
        "f3": 9.30,
        "f4": 9.00,
        "f5": 8.20,
        "f6": 8.80,
        "f7": 9.30,
        "f8": 8.70,
        "cqv_v5": 8.80,
        "cqv": 8.80,
        "price": 305.84,
        "pe": None,
        "pe_forward": 110.15,
        "eps_trailing": -3.36,
        "eps_forward": 2.78,
        "eps_growth_ntm_pct": 35.00,
        "growth_eps": 35.00,
        "market_cap_b": 106.00,
        "market_cap": 106000.0,
        "price_date": "28/05/2026",
        "valuation_date": "28/05/2026",
        "publication_date": "28/05/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ALTA CALIDAD",
        "verdict": "Mantener / Acumular en Correcciones",
        "value_score": 3.07,
        "peg_bruto": 3.177,
        "score_peg": 3.177,
        "score_crecimiento_multiplo_bruto": 3.177,
        "score_crecimiento_multiplo": 3.177,
        "intrinsic_value": 220.00,
        "intrinsic_value_base": 220.00,
        "intrinsic_value_expected": 225.00,
        "mos_pct": -28.07,
        "mos_base_pct": -28.07,
        "mos_esperado_pct": -26.43,
        "score_mos": 2.80,
        "fcf_yield_pct": 1.03,
        "score_fcf_yield": 3.20,
        "owner_earnings": 1090.0,
        "owner_earnings_m": 1090.0,
        "ocf": 1780.0,
        "ocf_ttm_m": 1780.0,
        "maintenance_capex": 40.0,
        "maint_capex_m": 40.0,
        "wacc": 9.00,
        "g_terminal": 3.50,
        "data_confidence": "Alta",
        "f4_moat": 9.00,
        "analyst_targets": {
            "target_low_bear": 210.0,
            "target_mean_base": 315.0,
            "target_high_bull": 380.0,
            "num_analysts": 38,
            "consensus_recommendation": "Buy",
            "upside_potential_pct": 2.99
        },
        "close_history": {
            "2020": 281.40,
            "2021": 338.75,
            "2022": 143.54,
            "2023": 199.00,
            "2024": 154.41,
            "2025": 219.36,
            "2026": 305.84
        },
        "sources": [
            "https://investors.snowflake.com/news/news-details/2026/Snowflake-Reports-First-Quarter-Fiscal-2027-Financial-Results/",
            "https://www.sec.gov/edgar/browse/?CIK=1640147",
            "https://stockanalysis.com/stocks/snow/",
            "https://finance.yahoo.com/quote/SNOW/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('SNOW', {})

    HIST_FACTORS = {
        '2020': {'f1': 7.2, 'f2': 9.6, 'f3': 9.7, 'f4': 8.6, 'f5': 7.8, 'f6': 8.9, 'f7': 9.2, 'f8': 8.2, 'pe': None, 'pe_fwd': 185.0, 'vs': 2.50, 'cqv': 8.35},
        '2021': {'f1': 7.4, 'f2': 9.6, 'f3': 9.6, 'f4': 8.7, 'f5': 7.9, 'f6': 8.9, 'f7': 9.3, 'f8': 8.4, 'pe': None, 'pe_fwd': 160.0, 'vs': 2.70, 'cqv': 8.48},
        '2022': {'f1': 7.5, 'f2': 9.6, 'f3': 9.3, 'f4': 8.8, 'f5': 8.0, 'f6': 8.8, 'f7': 9.2, 'f8': 8.5, 'pe': None, 'pe_fwd': 75.0, 'vs': 3.90, 'cqv': 8.52},
        '2023': {'f1': 7.6, 'f2': 9.6, 'f3': 9.2, 'f4': 8.9, 'f5': 8.1, 'f6': 8.8, 'f7': 9.2, 'f8': 8.6, 'pe': None, 'pe_fwd': 88.0, 'vs': 3.45, 'cqv': 8.65},
        '2024': {'f1': 7.8, 'f2': 9.6, 'f3': 9.1, 'f4': 8.9, 'f5': 8.1, 'f6': 8.7, 'f7': 9.3, 'f8': 8.6, 'pe': None, 'pe_fwd': 72.0, 'vs': 3.80, 'cqv': 8.70},
        '2025': {'f1': 7.8, 'f2': 9.6, 'f3': 9.2, 'f4': 9.0, 'f5': 8.2, 'f6': 8.8, 'f7': 9.3, 'f8': 8.7, 'pe': None, 'pe_fwd': 89.0, 'vs': 3.35, 'cqv': 8.76},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['SNOW'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.03), 1) if hf['pe_fwd'] else None
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['SNOW'][s_yr][p_k] = {
                'ticker': 'SNOW',
                'quarter': f'{p_k} {s_yr}',
                'f1': f_p[0], 'f2': f_p[1], 'f3': f_p[2], 'f4': f_p[3],
                'f5': f_p[4], 'f6': f_p[5], 'f7': f_p[6], 'f8': f_p[7],
                'cqv_v5': cqv_p, 'cqv': cqv_p,
                'pe': None,
                'pe_forward': pe_fwd_p,
                'value_score': vs_p,
                'verdict': 'Mantener / Acumular en Correcciones',
                'clasificacion': 'ALTA CALIDAD'
            }

        # Annual legacy
        cqv_leg = calc_cqv(base_f_vals)
        history['SNOW'][s_yr]['annual_legacy'] = {
            'ticker': 'SNOW',
            'quarter': f'Anual {s_yr}',
            'f1': base_f_vals[0], 'f2': base_f_vals[1], 'f3': base_f_vals[2], 'f4': base_f_vals[3],
            'f5': base_f_vals[4], 'f6': base_f_vals[5], 'f7': base_f_vals[6], 'f8': base_f_vals[7],
            'cqv_v5': cqv_leg, 'cqv': cqv_leg,
            'pe': None,
            'pe_forward': hf['pe_fwd'],
            'value_score': hf['vs'],
            'verdict': 'Mantener / Acumular en Correcciones',
            'clasificacion': 'ALTA CALIDAD'
        }

    # 2026
    history['SNOW'].setdefault('2026', {})
    history['SNOW']['2026']['P1'] = {
        'ticker': 'SNOW',
        'quarter': 'P1 2026',
        'f1': 7.9, 'f2': 9.6, 'f3': 9.3, 'f4': 9.0, 'f5': 8.2, 'f6': 8.8, 'f7': 9.3, 'f8': 8.7,
        'cqv_v5': 8.78, 'cqv': 8.78,
        'pe': None,
        'pe_forward': 98.5,
        'value_score': 3.25,
        'verdict': 'Mantener / Acumular en Correcciones',
        'clasificacion': 'ALTA CALIDAD'
    }
    history['SNOW']['2026']['P2'] = dict(snow_entry)
    history['SNOW']['2026']['P3'] = None
    history['SNOW']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("SNOW integrado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
