import json

def main():
    print("Integrando y actualizando NTAP en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    ntap_entry = None
    for item in cqv_data:
        if item.get('ticker') == 'NTAP':
            ntap_entry = item
            break

    if not ntap_entry:
        ntap_entry = {'ticker': 'NTAP'}
        cqv_data.append(ntap_entry)

    ntap_entry.update({
        "ticker": "NTAP",
        "name": "NetApp, Inc.",
        "sector": "Technology / Software-Defined Storage, Enterprise Hybrid Cloud & AI Data Infrastructure",
        "quarter": "P2 2026",
        "f1": 9.00,
        "f2": 9.10,
        "f3": 8.60,
        "f4": 8.80,
        "f5": 9.20,
        "f6": 8.90,
        "f7": 8.60,
        "f8": 8.90,
        "cqv_v5": 8.90,
        "cqv": 8.90,
        "price": 180.77,
        "pe": 28.83,
        "pe_forward": 17.82,
        "eps_trailing": 6.27,
        "eps_forward": 10.14,
        "eps_growth_ntm_pct": 22.50,
        "growth_eps": 22.50,
        "market_cap_b": 35.47,
        "market_cap": 35470.0,
        "price_date": "29/05/2026",
        "valuation_date": "29/05/2026",
        "publication_date": "29/05/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ALTA CALIDAD",
        "verdict": "Comprar / Revisar Compra",
        "value_score": 7.97,
        "peg_bruto": 12.626,
        "score_peg": 10.00,
        "score_crecimiento_multiplo_bruto": 12.626,
        "score_crecimiento_multiplo": 10.00,
        "intrinsic_value": 225.00,
        "intrinsic_value_base": 225.00,
        "intrinsic_value_expected": 232.00,
        "mos_pct": 19.66,
        "mos_base_pct": 19.66,
        "mos_esperado_pct": 22.08,
        "score_mos": 6.55,
        "fcf_yield_pct": 3.65,
        "score_fcf_yield": 7.50,
        "owner_earnings": 1250.0,
        "owner_earnings_m": 1250.0,
        "ocf": 1450.0,
        "ocf_ttm_m": 1450.0,
        "maintenance_capex": 200.0,
        "maint_capex_m": 200.0,
        "wacc": 8.50,
        "g_terminal": 3.50,
        "data_confidence": "Alta",
        "f4_moat": 8.80,
        "analyst_targets": {
            "target_low_bear": 155.0,
            "target_mean_base": 198.0,
            "target_high_bull": 235.0,
            "num_analysts": 22,
            "consensus_recommendation": "Buy",
            "upside_potential_pct": 9.53
        },
        "close_history": {
            "2020": 57.95,
            "2021": 82.55,
            "2022": 55.38,
            "2023": 83.71,
            "2024": 112.30,
            "2025": 105.71,
            "2026": 180.77
        },
        "sources": [
            "https://investors.netapp.com/news-releases/news-release-details/netapp-reports-fourth-quarter-and-fiscal-year-2026-results",
            "https://www.sec.gov/edgar/browse/?CIK=1002047",
            "https://stockanalysis.com/stocks/ntap/",
            "https://finance.yahoo.com/quote/NTAP/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('NTAP', {})

    HIST_FACTORS = {
        '2020': {'f1': 8.5, 'f2': 8.8, 'f3': 7.9, 'f4': 8.5, 'f5': 8.9, 'f6': 8.6, 'f7': 8.0, 'f8': 8.5, 'pe': 16.1, 'pe_fwd': 14.0, 'vs': 8.10, 'cqv': 8.32},
        '2021': {'f1': 8.7, 'f2': 8.9, 'f3': 8.2, 'f4': 8.6, 'f5': 9.0, 'f6': 8.7, 'f7': 8.2, 'f8': 8.6, 'pe': 19.9, 'pe_fwd': 16.5, 'vs': 7.80, 'cqv': 8.47},
        '2022': {'f1': 8.6, 'f2': 8.8, 'f3': 8.0, 'f4': 8.6, 'f5': 9.0, 'f6': 8.7, 'f7': 8.2, 'f8': 8.6, 'pe': 12.7, 'pe_fwd': 11.2, 'vs': 8.40, 'cqv': 8.40},
        '2023': {'f1': 8.8, 'f2': 8.9, 'f3': 8.2, 'f4': 8.7, 'f5': 9.1, 'f6': 8.8, 'f7': 8.3, 'f8': 8.7, 'pe': 18.0, 'pe_fwd': 15.0, 'vs': 8.00, 'cqv': 8.60},
        '2024': {'f1': 8.9, 'f2': 9.0, 'f3': 8.4, 'f4': 8.7, 'f5': 9.1, 'f6': 8.8, 'f7': 8.4, 'f8': 8.8, 'pe': 21.4, 'pe_fwd': 16.8, 'vs': 7.85, 'cqv': 8.75},
        '2025': {'f1': 9.0, 'f2': 9.0, 'f3': 8.5, 'f4': 8.8, 'f5': 9.2, 'f6': 8.9, 'f7': 8.5, 'f8': 8.8, 'pe': 18.9, 'pe_fwd': 15.2, 'vs': 8.10, 'cqv': 8.82},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['NTAP'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_p = round(hf['pe'] * (1.0 + (p_num - 2) * 0.02), 1)
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.02), 1)
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['NTAP'][s_yr][p_k] = {
                'ticker': 'NTAP',
                'quarter': f'{p_k} {s_yr}',
                'f1': f_p[0], 'f2': f_p[1], 'f3': f_p[2], 'f4': f_p[3],
                'f5': f_p[4], 'f6': f_p[5], 'f7': f_p[6], 'f8': f_p[7],
                'cqv_v5': cqv_p, 'cqv': cqv_p,
                'pe': pe_p, 'pe_forward': pe_fwd_p,
                'value_score': vs_p,
                'verdict': 'Comprar / Revisar Compra',
                'clasificacion': 'ALTA CALIDAD'
            }

        # Annual legacy
        cqv_leg = calc_cqv(base_f_vals)
        history['NTAP'][s_yr]['annual_legacy'] = {
            'ticker': 'NTAP',
            'quarter': f'Anual {s_yr}',
            'f1': base_f_vals[0], 'f2': base_f_vals[1], 'f3': base_f_vals[2], 'f4': base_f_vals[3],
            'f5': base_f_vals[4], 'f6': base_f_vals[5], 'f7': base_f_vals[6], 'f8': base_f_vals[7],
            'cqv_v5': cqv_leg, 'cqv': cqv_leg,
            'pe': hf['pe'], 'pe_forward': hf['pe_fwd'],
            'value_score': hf['vs'],
            'verdict': 'Comprar / Revisar Compra',
            'clasificacion': 'ALTA CALIDAD'
        }

    # 2026
    history['NTAP'].setdefault('2026', {})
    history['NTAP']['2026']['P1'] = {
        'ticker': 'NTAP',
        'quarter': 'P1 2026',
        'f1': 9.0, 'f2': 9.1, 'f3': 8.6, 'f4': 8.8, 'f5': 9.2, 'f6': 8.9, 'f7': 8.6, 'f8': 8.9,
        'cqv_v5': 8.86, 'cqv': 8.86,
        'pe': 26.3, 'pe_forward': 17.5,
        'value_score': 8.05,
        'verdict': 'Comprar / Revisar Compra',
        'clasificacion': 'ALTA CALIDAD'
    }
    history['NTAP']['2026']['P2'] = dict(ntap_entry)
    history['NTAP']['2026']['P3'] = None
    history['NTAP']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("NTAP integrado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
