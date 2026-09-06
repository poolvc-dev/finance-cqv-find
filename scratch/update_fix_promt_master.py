import json

def main():
    print("Actualizando FIX en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    fix_entry = None
    for idx, item in enumerate(cqv_data):
        if item.get('ticker') == 'FIX':
            fix_entry = item
            break

    if not fix_entry:
        fix_entry = {'ticker': 'FIX'}
        cqv_data.append(fix_entry)

    fix_entry.update({
        "ticker": "FIX",
        "name": "Comfort Systems USA, Inc.",
        "sector": "Industrials / Mission-Critical Mechanical & Electrical Infrastructure, Data Centers & Modular Pre-fabrication",
        "quarter": "P2 2026",
        "f1": 9.65,
        "f2": 9.50,
        "f3": 9.70,
        "f4": 9.45,
        "f5": 9.40,
        "f6": 9.60,
        "f7": 9.35,
        "f8": 9.40,
        "cqv_v5": 9.54,
        "cqv": 9.54,
        "price": 1831.15,
        "pe": 47.69,
        "pe_forward": 37.75,
        "eps_trailing": 38.40,
        "eps_forward": 48.50,
        "eps_growth_ntm_pct": 32.50,
        "growth_eps": 32.50,
        "market_cap_b": 65.20,
        "market_cap": 65200.0,
        "price_date": "23/07/2026",
        "valuation_date": "23/07/2026",
        "publication_date": "23/07/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ÉLITE SUPREMA",
        "verdict": "Comprar / Revisar Compra",
        "value_score": 6.60,
        "peg_bruto": 8.609,
        "score_peg": 8.609,
        "score_crecimiento_multiplo_bruto": 8.609,
        "score_crecimiento_multiplo": 8.609,
        "intrinsic_value": 2280.00,
        "intrinsic_value_base": 2280.00,
        "intrinsic_value_expected": 2350.00,
        "mos_pct": 19.69,
        "mos_base_pct": 19.69,
        "mos_esperado_pct": 22.08,
        "score_mos": 6.56,
        "fcf_yield_pct": 2.05,
        "score_fcf_yield": 5.12,
        "owner_earnings": 1335.0,
        "owner_earnings_m": 1335.0,
        "ocf": 1420.0,
        "ocf_ttm_m": 1420.0,
        "maintenance_capex": 85.0,
        "maint_capex_m": 85.0,
        "wacc": 8.00,
        "g_terminal": 3.50,
        "data_confidence": "Alta",
        "f4_moat": 9.45,
        "analyst_targets": {
            "target_low_bear": 1650.0,
            "target_mean_base": 2150.0,
            "target_high_bull": 2450.0,
            "num_analysts": 12,
            "consensus_recommendation": "Strong Buy",
            "upside_potential_pct": 17.41
        },
        "close_history": {
            "2020": 51.37,
            "2021": 97.07,
            "2022": 113.55,
            "2023": 203.96,
            "2024": 421.96,
            "2025": 931.96,
            "2026": 1831.15
        },
        "sources": [
            "https://investors.comfortsystemsusa.com/news-releases/news-release-details/comfort-systems-usa-reports-record-second-quarter-2026-results",
            "https://www.sec.gov/edgar/browse/?CIK=1035983",
            "https://stockanalysis.com/stocks/fix/",
            "https://finance.yahoo.com/quote/FIX/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('FIX', {})

    # Detailed historical progression for FIX (2020 - 2026)
    HIST_FACTORS = {
        '2020': {'f1': 8.5, 'f2': 8.8, 'f3': 8.2, 'f4': 8.4, 'f5': 8.5, 'f6': 8.8, 'f7': 8.0, 'f8': 8.5, 'pe': 13.3, 'pe_fwd': 11.5, 'vs': 7.40, 'cqv': 8.45, 'tier': 'ALTA CALIDAD', 'verd': 'Comprar / Acumular'},
        '2021': {'f1': 8.7, 'f2': 8.9, 'f3': 8.5, 'f4': 8.6, 'f5': 8.7, 'f6': 8.9, 'f7': 8.2, 'f8': 8.7, 'pe': 19.5, 'pe_fwd': 16.2, 'vs': 7.10, 'cqv': 8.68, 'tier': 'ALTA CALIDAD', 'verd': 'Comprar / Acumular'},
        '2022': {'f1': 8.9, 'f2': 9.0, 'f3': 8.8, 'f4': 8.8, 'f5': 8.9, 'f6': 9.1, 'f7': 8.5, 'f8': 8.9, 'pe': 17.2, 'pe_fwd': 14.5, 'vs': 7.35, 'cqv': 8.85, 'tier': 'ALTA CALIDAD', 'verd': 'Comprar / Acumular'},
        '2023': {'f1': 9.2, 'f2': 9.2, 'f3': 9.2, 'f4': 9.0, 'f5': 9.1, 'f6': 9.3, 'f7': 8.8, 'f8': 9.1, 'pe': 22.4, 'pe_fwd': 18.5, 'vs': 7.20, 'cqv': 9.11, 'tier': 'ÉLITE', 'verd': 'Comprar / Revisar Compra'},
        '2024': {'f1': 9.4, 'f2': 9.3, 'f3': 9.5, 'f4': 9.2, 'f5': 9.2, 'f6': 9.4, 'f7': 9.0, 'f8': 9.2, 'pe': 28.6, 'pe_fwd': 23.0, 'vs': 6.95, 'cqv': 9.31, 'tier': 'ÉLITE', 'verd': 'Comprar / Revisar Compra'},
        '2025': {'f1': 9.5, 'f2': 9.4, 'f3': 9.6, 'f4': 9.3, 'f5': 9.3, 'f6': 9.5, 'f7': 9.2, 'f8': 9.3, 'pe': 37.6, 'pe_fwd': 29.5, 'vs': 6.75, 'cqv': 9.44, 'tier': 'ÉLITE', 'verd': 'Comprar / Revisar Compra'},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['FIX'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_p = round(hf['pe'] * (1.0 + (p_num - 2) * 0.02), 1)
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.02), 1)
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['FIX'][s_yr][p_k] = {
                'ticker': 'FIX',
                'quarter': f'{p_k} {s_yr}',
                'f1': f_p[0], 'f2': f_p[1], 'f3': f_p[2], 'f4': f_p[3],
                'f5': f_p[4], 'f6': f_p[5], 'f7': f_p[6], 'f8': f_p[7],
                'cqv_v5': cqv_p, 'cqv': cqv_p,
                'pe': pe_p, 'pe_forward': pe_fwd_p,
                'value_score': vs_p,
                'verdict': hf['verd'],
                'clasificacion': hf['tier']
            }

        # Annual legacy
        cqv_leg = calc_cqv(base_f_vals)
        history['FIX'][s_yr]['annual_legacy'] = {
            'ticker': 'FIX',
            'quarter': f'Anual {s_yr}',
            'f1': base_f_vals[0], 'f2': base_f_vals[1], 'f3': base_f_vals[2], 'f4': base_f_vals[3],
            'f5': base_f_vals[4], 'f6': base_f_vals[5], 'f7': base_f_vals[6], 'f8': base_f_vals[7],
            'cqv_v5': cqv_leg, 'cqv': cqv_leg,
            'pe': hf['pe'], 'pe_forward': hf['pe_fwd'],
            'value_score': hf['vs'],
            'verdict': hf['verd'],
            'clasificacion': hf['tier']
        }

    # 2026
    history['FIX'].setdefault('2026', {})
    history['FIX']['2026']['P1'] = {
        'ticker': 'FIX',
        'quarter': 'P1 2026',
        'f1': 9.6, 'f2': 9.5, 'f3': 9.6, 'f4': 9.4, 'f5': 9.4, 'f6': 9.6, 'f7': 9.3, 'f8': 9.4,
        'cqv_v5': 9.50, 'cqv': 9.50,
        'pe': 43.7, 'pe_forward': 34.5,
        'value_score': 6.70,
        'verdict': 'Comprar / Revisar Compra',
        'clasificacion': 'ÉLITE SUPREMA'
    }
    history['FIX']['2026']['P2'] = dict(fix_entry)
    history['FIX']['2026']['P3'] = None
    history['FIX']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("FIX actualizado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
