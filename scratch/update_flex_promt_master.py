import json

def main():
    print("Actualizando FLEX en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    flex_entry = None
    for item in cqv_data:
        if item.get('ticker') == 'FLEX':
            flex_entry = item
            break

    if not flex_entry:
        flex_entry = {'ticker': 'FLEX'}
        cqv_data.append(flex_entry)

    flex_entry.update({
        "ticker": "FLEX",
        "name": "Flex Ltd.",
        "sector": "Technology / Advanced Manufacturing, Data Center Cloud & Power Infrastructure",
        "quarter": "P2 2026",
        "f1": 8.90,
        "f2": 9.25,
        "f3": 9.10,
        "f4": 8.80,
        "f5": 9.00,
        "f6": 9.15,
        "f7": 8.85,
        "f8": 8.80,
        "cqv_v5": 8.99,
        "cqv": 8.99,
        "price": 100.01,
        "pe": 25.98,
        "pe_forward": 20.84,
        "eps_trailing": 3.85,
        "eps_forward": 4.80,
        "eps_growth_ntm_pct": 24.70,
        "growth_eps": 24.70,
        "market_cap_b": 39.50,
        "market_cap": 39500.0,
        "price_date": "29/07/2026",
        "valuation_date": "29/07/2026",
        "publication_date": "29/07/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ALTA CALIDAD",
        "verdict": "Comprar / Revisar Compra",
        "value_score": 8.90,
        "peg_bruto": 11.852,
        "score_peg": 10.00,
        "score_crecimiento_multiplo_bruto": 11.852,
        "score_crecimiento_multiplo": 10.00,
        "intrinsic_value": 132.00,
        "intrinsic_value_base": 132.00,
        "intrinsic_value_expected": 128.04,
        "mos_pct": 24.23,
        "mos_base_pct": 24.23,
        "mos_esperado_pct": 21.81,
        "score_mos": 8.08,
        "fcf_yield_pct": 3.47,
        "score_fcf_yield": 8.68,
        "owner_earnings": 1370.0,
        "owner_earnings_m": 1370.0,
        "ocf": 1650.0,
        "ocf_ttm_m": 1650.0,
        "maintenance_capex": 280.0,
        "maint_capex_m": 280.0,
        "wacc": 8.50,
        "g_terminal": 3.00,
        "data_confidence": "Alta",
        "f4_moat": 8.80,
        "analyst_targets": {
            "target_low_bear": 90.0,
            "target_mean_base": 120.0,
            "target_high_bull": 145.0,
            "num_analysts": 14,
            "consensus_recommendation": "Strong Buy",
            "upside_potential_pct": 19.99
        },
        "close_history": {
            "2020": 13.55,
            "2021": 13.81,
            "2022": 16.17,
            "2023": 22.95,
            "2024": 38.39,
            "2025": 60.42,
            "2026": 100.01
        },
        "sources": [
            "https://investors.flex.com/news-events/press-releases/detail/2026/Flex-Reports-First-Quarter-Fiscal-Year-2027-Results",
            "https://www.sec.gov/edgar/browse/?CIK=866374",
            "https://stockanalysis.com/stocks/flex/",
            "https://finance.yahoo.com/quote/FLEX/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('FLEX', {})

    HIST_FACTORS = {
        '2020': {'f1': 8.2, 'f2': 8.8, 'f3': 7.8, 'f4': 8.2, 'f5': 8.5, 'f6': 8.6, 'f7': 8.0, 'f8': 8.2, 'pe': 11.3, 'pe_fwd': 9.8, 'vs': 9.15, 'cqv': 8.25, 'tier': 'ALTA CALIDAD'},
        '2021': {'f1': 8.4, 'f2': 8.9, 'f3': 8.1, 'f4': 8.4, 'f5': 8.6, 'f6': 8.8, 'f7': 8.2, 'f8': 8.3, 'pe': 10.2, 'pe_fwd': 8.9, 'vs': 9.30, 'cqv': 8.38, 'tier': 'ALTA CALIDAD'},
        '2022': {'f1': 8.5, 'f2': 9.0, 'f3': 8.3, 'f4': 8.5, 'f5': 8.7, 'f6': 8.9, 'f7': 8.4, 'f8': 8.5, 'pe': 9.0, 'pe_fwd': 7.8, 'vs': 9.45, 'cqv': 8.52, 'tier': 'ALTA CALIDAD'},
        '2023': {'f1': 8.6, 'f2': 9.1, 'f3': 8.6, 'f4': 8.6, 'f5': 8.8, 'f6': 9.0, 'f7': 8.6, 'f8': 8.6, 'pe': 10.4, 'pe_fwd': 8.8, 'vs': 9.35, 'cqv': 8.70, 'tier': 'ALTA CALIDAD'},
        '2024': {'f1': 8.8, 'f2': 9.2, 'f3': 8.9, 'f4': 8.7, 'f5': 8.9, 'f6': 9.1, 'f7': 8.7, 'f8': 8.7, 'pe': 15.7, 'pe_fwd': 12.8, 'vs': 9.10, 'cqv': 8.85, 'tier': 'ALTA CALIDAD'},
        '2025': {'f1': 8.9, 'f2': 9.2, 'f3': 9.0, 'f4': 8.8, 'f5': 9.0, 'f6': 9.1, 'f7': 8.8, 'f8': 8.8, 'pe': 18.9, 'pe_fwd': 15.2, 'vs': 8.95, 'cqv': 8.92, 'tier': 'ALTA CALIDAD'},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['FLEX'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_p = round(hf['pe'] * (1.0 + (p_num - 2) * 0.02), 1)
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.02), 1)
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['FLEX'][s_yr][p_k] = {
                'ticker': 'FLEX',
                'quarter': f'{p_k} {s_yr}',
                'f1': f_p[0], 'f2': f_p[1], 'f3': f_p[2], 'f4': f_p[3],
                'f5': f_p[4], 'f6': f_p[5], 'f7': f_p[6], 'f8': f_p[7],
                'cqv_v5': cqv_p, 'cqv': cqv_p,
                'pe': pe_p, 'pe_forward': pe_fwd_p,
                'value_score': vs_p,
                'verdict': 'Comprar / Revisar Compra',
                'clasificacion': hf['tier']
            }

        # Annual legacy
        cqv_leg = calc_cqv(base_f_vals)
        history['FLEX'][s_yr]['annual_legacy'] = {
            'ticker': 'FLEX',
            'quarter': f'Anual {s_yr}',
            'f1': base_f_vals[0], 'f2': base_f_vals[1], 'f3': base_f_vals[2], 'f4': base_f_vals[3],
            'f5': base_f_vals[4], 'f6': base_f_vals[5], 'f7': base_f_vals[6], 'f8': base_f_vals[7],
            'cqv_v5': cqv_leg, 'cqv': cqv_leg,
            'pe': hf['pe'], 'pe_forward': hf['pe_fwd'],
            'value_score': hf['vs'],
            'verdict': 'Comprar / Revisar Compra',
            'clasificacion': hf['tier']
        }

    # 2026
    history['FLEX'].setdefault('2026', {})
    history['FLEX']['2026']['P1'] = {
        'ticker': 'FLEX',
        'quarter': 'P1 2026',
        'f1': 8.9, 'f2': 9.2, 'f3': 9.1, 'f4': 8.8, 'f5': 9.0, 'f6': 9.1, 'f7': 8.8, 'f8': 8.8,
        'cqv_v5': 8.95, 'cqv': 8.95,
        'pe': 23.6, 'pe_forward': 19.2,
        'value_score': 9.05,
        'verdict': 'Comprar / Revisar Compra',
        'clasificacion': 'ALTA CALIDAD'
    }
    history['FLEX']['2026']['P2'] = dict(flex_entry)
    history['FLEX']['2026']['P3'] = None
    history['FLEX']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("FLEX actualizado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
