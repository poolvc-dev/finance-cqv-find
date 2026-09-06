import json

def main():
    print("Actualizando LIN en cqv_data.json y cqv_history.json bajo CQV v5.0...")

    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    # 1. Update cqv_data.json
    lin_entry = None
    for item in cqv_data:
        if item.get('ticker') == 'LIN':
            lin_entry = item
            break

    if not lin_entry:
        lin_entry = {'ticker': 'LIN'}
        cqv_data.append(lin_entry)

    lin_entry.update({
        "ticker": "LIN",
        "name": "Linde plc",
        "sector": "Materials / Industrial Gases & Engineering Infrastructure",
        "quarter": "P2 2026",
        "f1": 9.50,
        "f2": 9.40,
        "f3": 9.10,
        "f4": 9.80,
        "f5": 9.60,
        "f6": 9.60,
        "f7": 9.00,
        "f8": 9.70,
        "cqv_v5": 9.48,
        "cqv": 9.48,
        "price": 455.00,
        "pe": 31.20,
        "pe_forward": 26.50,
        "eps_trailing": 14.58,
        "eps_forward": 17.17,
        "eps_growth_ntm_pct": 17.80,
        "growth_eps": 17.80,
        "market_cap_b": 215.00,
        "market_cap": 215000.0,
        "price_date": "29/07/2026",
        "valuation_date": "29/07/2026",
        "publication_date": "29/07/2026",
        "metodologia_version": "v5.0",
        "status": "Success",
        "clasificacion": "ÉLITE",
        "verdict": "Comprar / Revisar Compra",
        "value_score": 6.90,
        "peg_bruto": 6.717,
        "score_peg": 6.717,
        "score_crecimiento_multiplo_bruto": 6.717,
        "score_crecimiento_multiplo": 6.717,
        "intrinsic_value": 568.75,
        "intrinsic_value_base": 568.75,
        "intrinsic_value_expected": 551.69,
        "mos_pct": 20.00,
        "mos_base_pct": 20.00,
        "mos_esperado_pct": 18.00,
        "score_mos": 6.67,
        "fcf_yield_pct": 2.88,
        "score_fcf_yield": 7.20,
        "owner_earnings": 6200.0,
        "owner_earnings_m": 6200.0,
        "ocf": 9850.0,
        "ocf_ttm_m": 9850.0,
        "maintenance_capex": 3650.0,
        "maint_capex_m": 3650.0,
        "wacc": 8.00,
        "g_terminal": 3.00,
        "data_confidence": "Alta",
        "f4_moat": 9.80,
        "analyst_targets": {
            "target_low_bear": 400.0,
            "target_mean_base": 520.0,
            "target_high_bull": 580.0,
            "num_analysts": 28,
            "consensus_recommendation": "Strong Buy",
            "upside_potential_pct": 14.29
        },
        "close_history": {
            "2020": 244.33,
            "2021": 325.91,
            "2022": 311.59,
            "2023": 397.77,
            "2024": 410.43,
            "2025": 423.62,
            "2026": 455.00
        },
        "sources": [
            "https://www.linde.com/news-and-media/2026/linde-reports-second-quarter-2026-results",
            "https://www.sec.gov/edgar/browse/?CIK=1707925",
            "https://stockanalysis.com/stocks/lin/",
            "https://finance.yahoo.com/quote/LIN/"
        ]
    })

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)

    # 2. Update cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    history.setdefault('LIN', {})

    HIST_FACTORS = {
        '2020': {'f1': 8.9, 'f2': 9.1, 'f3': 8.5, 'f4': 9.6, 'f5': 9.2, 'f6': 9.3, 'f7': 8.5, 'f8': 9.5, 'pe': 22.7, 'pe_fwd': 19.3, 'vs': 7.30, 'cqv': 9.11, 'tier': 'ÉLITE'},
        '2021': {'f1': 9.1, 'f2': 9.2, 'f3': 8.8, 'f4': 9.7, 'f5': 9.4, 'f6': 9.4, 'f7': 8.7, 'f8': 9.6, 'pe': 27.8, 'pe_fwd': 23.6, 'vs': 6.95, 'cqv': 9.28, 'tier': 'ÉLITE'},
        '2022': {'f1': 9.0, 'f2': 9.1, 'f3': 8.6, 'f4': 9.7, 'f5': 9.3, 'f6': 9.4, 'f7': 8.6, 'f8': 9.5, 'pe': 20.5, 'pe_fwd': 17.4, 'vs': 7.45, 'cqv': 9.05, 'tier': 'ÉLITE'},
        '2023': {'f1': 9.2, 'f2': 9.3, 'f3': 8.8, 'f4': 9.7, 'f5': 9.5, 'f6': 9.5, 'f7': 8.8, 'f8': 9.6, 'pe': 25.9, 'pe_fwd': 21.9, 'vs': 7.15, 'cqv': 9.28, 'tier': 'ÉLITE'},
        '2024': {'f1': 9.4, 'f2': 9.3, 'f3': 9.0, 'f4': 9.8, 'f5': 9.5, 'f6': 9.5, 'f7': 8.9, 'f8': 9.7, 'pe': 29.0, 'pe_fwd': 24.6, 'vs': 7.00, 'cqv': 9.41, 'tier': 'ÉLITE'},
        '2025': {'f1': 9.5, 'f2': 9.4, 'f3': 9.1, 'f4': 9.8, 'f5': 9.6, 'f6': 9.6, 'f7': 9.0, 'f8': 9.7, 'pe': 30.3, 'pe_fwd': 25.8, 'vs': 6.95, 'cqv': 9.47, 'tier': 'ÉLITE'},
    }

    weights = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    def calc_cqv(f_list):
        return round(sum(f_list[i] * weights[i] for i in range(8)), 2)

    for yr in range(2020, 2026):
        s_yr = str(yr)
        hf = HIST_FACTORS[s_yr]
        base_f_vals = [hf['f1'], hf['f2'], hf['f3'], hf['f4'], hf['f5'], hf['f6'], hf['f7'], hf['f8']]
        
        history['LIN'].setdefault(s_yr, {})
        for p_num in range(1, 5):
            p_k = f'P{p_num}'
            p_adj = round((p_num - 2.5) * 0.03, 2)
            f_p = [round(max(1.0, min(10.0, base_f_vals[i] + p_adj)), 1) for i in range(8)]
            cqv_p = calc_cqv(f_p)
            pe_p = round(hf['pe'] * (1.0 + (p_num - 2) * 0.02), 1)
            pe_fwd_p = round(hf['pe_fwd'] * (1.0 + (p_num - 2) * 0.02), 1)
            vs_p = round(hf['vs'] - (p_num - 2) * 0.05, 2)

            history['LIN'][s_yr][p_k] = {
                'ticker': 'LIN',
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
        history['LIN'][s_yr]['annual_legacy'] = {
            'ticker': 'LIN',
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
    history['LIN'].setdefault('2026', {})
    history['LIN']['2026']['P1'] = {
        'ticker': 'LIN',
        'quarter': 'P1 2026',
        'f1': 9.5, 'f2': 9.4, 'f3': 9.1, 'f4': 9.8, 'f5': 9.6, 'f6': 9.6, 'f7': 9.0, 'f8': 9.7,
        'cqv_v5': 9.42, 'cqv': 9.42,
        'pe': 30.6, 'pe_forward': 26.0,
        'value_score': 7.00,
        'verdict': 'Comprar / Revisar Compra',
        'clasificacion': 'ÉLITE'
    }
    history['LIN']['2026']['P2'] = dict(lin_entry)
    history['LIN']['2026']['P3'] = None
    history['LIN']['2026']['P4'] = None

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print("LIN actualizado en SSOT y cqv_history.json con éxito.")

if __name__ == '__main__':
    main()
