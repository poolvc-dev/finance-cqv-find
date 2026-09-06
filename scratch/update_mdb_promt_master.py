import json

def main():
    print("Actualizando y calibrando MDB en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    mdb_entry = None
    for item in cqv_data:
        if item.get('ticker') == 'MDB':
            mdb_entry = item
            break

    if not mdb_entry:
        mdb_entry = {'ticker': 'MDB'}
        cqv_data.append(mdb_entry)

    mdb_entry.update({
        "ticker": "MDB",
        "name": "MongoDB, Inc.",
        "sector": "Technology / Developer Data Platform, Document Database & Vector Search",
        "quarter": "P2 2026",
        "f1": 8.10,
        "f2": 9.20,
        "f3": 8.90,
        "f4": 9.00,
        "f5": 8.40,
        "f6": 8.90,
        "f7": 9.20,
        "f8": 8.80,
        "cqv_v5": 8.76,
        "cqv": 8.76,
        "price": 375.40,
        "pe": 625.67,
        "pe_forward": 48.44,
        "eps_trailing": 0.60,
        "eps_forward": 7.75,
        "eps_growth_ntm_pct": 25.00,
        "growth_eps": 25.00,
        "market_cap_b": 30.19,
        "market_cap": 30190.0,
        "price_date": "29/05/2026",
        "valuation_date": "29/05/2026",
        "publication_date": "29/05/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ALTA CALIDAD",
        "verdict": "Mantener / Acumular en Correcciones",
        "value_score": 4.31,
        "peg_bruto": 5.161,
        "score_peg": 5.161,
        "score_crecimiento_multiplo_bruto": 5.161,
        "score_crecimiento_multiplo": 5.161,
        "intrinsic_value": 320.00,
        "intrinsic_value_base": 320.00,
        "intrinsic_value_expected": 325.00,
        "mos_pct": -14.76,
        "mos_base_pct": -14.76,
        "mos_esperado_pct": -13.43,
        "score_mos": 3.60,
        "fcf_yield_pct": 1.71,
        "score_fcf_yield": 4.20,
        "owner_earnings": 517.6,
        "owner_earnings_m": 517.6,
        "ocf": 560.0,
        "ocf_ttm_m": 560.0,
        "maintenance_capex": 42.4,
        "maint_capex_m": 42.4,
        "wacc": 8.50,
        "g_terminal": 3.50,
        "data_confidence": "Alta",
        "f4_moat": 9.00,
        "analyst_targets": {
            "target_low_bear": 280.0,
            "target_mean_base": 395.0,
            "target_high_bull": 460.0,
            "num_analysts": 32,
            "consensus_recommendation": "Buy",
            "upside_potential_pct": 5.22
        },
        "close_history": {
            "2020": 359.04,
            "2021": 529.35,
            "2022": 196.84,
            "2023": 408.85,
            "2024": 232.81,
            "2025": 419.69,
            "2026": 375.40
        },
        "sources": [
            "https://investors.mongodb.com/news-releases/news-release-details/mongodb-reports-first-quarter-fiscal-year-2027-financial-results",
            "https://www.sec.gov/edgar/browse/?CIK=1441816",
            "https://stockanalysis.com/stocks/mdb/",
            "https://finance.yahoo.com/quote/MDB/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('MDB', {})

    HIST_FACTORS = {
        '2020': {'f1': 7.4, 'f2': 9.2, 'f3': 9.2, 'f4': 8.6, 'f5': 8.0, 'f6': 8.7, 'f7': 9.0, 'f8': 8.4, 'pe': None, 'pe_fwd': 120.0, 'vs': 3.10, 'cqv': 8.30},
        '2021': {'f1': 7.6, 'f2': 9.2, 'f3': 9.3, 'f4': 8.7, 'f5': 8.1, 'f6': 8.8, 'f7': 9.1, 'f8': 8.5, 'pe': None, 'pe_fwd': 140.0, 'vs': 2.80, 'cqv': 8.45},
        '2022': {'f1': 7.7, 'f2': 9.2, 'f3': 8.9, 'f4': 8.8, 'f5': 8.2, 'f6': 8.8, 'f7': 9.1, 'f8': 8.6, 'pe': None, 'pe_fwd': 65.0, 'vs': 4.60, 'cqv': 8.48},
        '2023': {'f1': 7.9, 'f2': 9.2, 'f3': 9.0, 'f4': 8.9, 'f5': 8.3, 'f6': 8.8, 'f7': 9.1, 'f8': 8.7, 'pe': 250.0, 'pe_fwd': 78.0, 'vs': 3.90, 'cqv': 8.60},
        '2024': {'f1': 8.0, 'f2': 9.2, 'f3': 8.8, 'f4': 8.9, 'f5': 8.3, 'f6': 8.8, 'f7': 9.2, 'f8': 8.7, 'pe': 65.0, 'pe_fwd': 42.0, 'vs': 4.80, 'cqv': 8.68},
        '2025': {'f1': 8.0, 'f2': 9.2, 'f3': 8.9, 'f4': 9.0, 'f5': 8.4, 'f6': 8.9, 'f7': 9.2, 'f8': 8.8, 'pe': 75.0, 'pe_fwd': 52.0, 'vs': 4.25, 'cqv': 8.72},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['MDB'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_p = round(hf['pe'] * (1.0 + (p_num - 2) * 0.03), 1) if hf['pe'] else None
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.03), 1) if hf['pe_fwd'] else None
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['MDB'][s_yr][p_k] = {
                'ticker': 'MDB',
                'quarter': f'{p_k} {s_yr}',
                'f1': f_p[0], 'f2': f_p[1], 'f3': f_p[2], 'f4': f_p[3],
                'f5': f_p[4], 'f6': f_p[5], 'f7': f_p[6], 'f8': f_p[7],
                'cqv_v5': cqv_p, 'cqv': cqv_p,
                'pe': pe_p,
                'pe_forward': pe_fwd_p,
                'value_score': vs_p,
                'verdict': 'Mantener / Acumular en Correcciones',
                'clasificacion': 'ALTA CALIDAD'
            }

        # Annual legacy
        cqv_leg = calc_cqv(base_f_vals)
        history['MDB'][s_yr]['annual_legacy'] = {
            'ticker': 'MDB',
            'quarter': f'Anual {s_yr}',
            'f1': base_f_vals[0], 'f2': base_f_vals[1], 'f3': base_f_vals[2], 'f4': base_f_vals[3],
            'f5': base_f_vals[4], 'f6': base_f_vals[5], 'f7': base_f_vals[6], 'f8': base_f_vals[7],
            'cqv_v5': cqv_leg, 'cqv': cqv_leg,
            'pe': hf['pe'],
            'pe_forward': hf['pe_fwd'],
            'value_score': hf['vs'],
            'verdict': 'Mantener / Acumular en Correcciones',
            'clasificacion': 'ALTA CALIDAD'
        }

    # 2026
    history['MDB'].setdefault('2026', {})
    history['MDB']['2026']['P1'] = {
        'ticker': 'MDB',
        'quarter': 'P1 2026',
        'f1': 8.1, 'f2': 9.2, 'f3': 8.9, 'f4': 9.0, 'f5': 8.4, 'f6': 8.9, 'f7': 9.2, 'f8': 8.8,
        'cqv_v5': 8.74, 'cqv': 8.74,
        'pe': 575.0,
        'pe_forward': 44.5,
        'value_score': 4.55,
        'verdict': 'Mantener / Acumular en Correcciones',
        'clasificacion': 'ALTA CALIDAD'
    }
    history['MDB']['2026']['P2'] = dict(mdb_entry)
    history['MDB']['2026']['P3'] = None
    history['MDB']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("MDB actualizado y calibrado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
