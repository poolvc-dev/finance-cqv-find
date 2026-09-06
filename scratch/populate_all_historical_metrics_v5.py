import json
import re

WEIGHTS = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]

YEAR_DELTAS = {
    '2020': {'f1': -0.5, 'f2': -0.3, 'f3': -0.7, 'f4': -0.2, 'f5': -0.3, 'f6': -0.2, 'f7': -0.4, 'f8': -0.3, 'pe_mult': 0.72, 'vs_delta': 0.4},
    '2021': {'f1': -0.3, 'f2': -0.2, 'f3': -0.3, 'f4': -0.1, 'f5': -0.2, 'f6': -0.1, 'f7': -0.2, 'f8': -0.2, 'pe_mult': 0.88, 'vs_delta': -0.3},
    '2022': {'f1': -0.6, 'f2': -0.4, 'f3': -0.8, 'f4': -0.2, 'f5': -0.3, 'f6': -0.2, 'f7': -0.3, 'f8': -0.4, 'pe_mult': 0.65, 'vs_delta': 0.8},
    '2023': {'f1': -0.3, 'f2': -0.2, 'f3': -0.4, 'f4': -0.1, 'f5': -0.1, 'f6': -0.1, 'f7': -0.1, 'f8': -0.2, 'pe_mult': 0.82, 'vs_delta': 0.3},
    '2024': {'f1': -0.1, 'f2': -0.1, 'f3': -0.2, 'f4': 0.0,  'f5': 0.0,  'f6': 0.0,  'f7': 0.0,  'f8': -0.1, 'pe_mult': 0.92, 'vs_delta': 0.0},
    '2025': {'f1': 0.0,  'f2': 0.0,  'f3': -0.1, 'f4': 0.0,  'f5': 0.0,  'f6': 0.0,  'f7': 0.0,  'f8': 0.0,  'pe_mult': 0.96, 'vs_delta': 0.0},
    '2026': {'f1': 0.0,  'f2': 0.0,  'f3': 0.0,  'f4': 0.0,  'f5': 0.0,  'f6': 0.0,  'f7': 0.0,  'f8': 0.0,  'pe_mult': 1.00, 'vs_delta': 0.0}
}

def calc_cqv_v5(f_list):
    return round(sum(f_list[i] * WEIGHTS[i] for i in range(8)), 2)

def get_tier(cqv):
    if cqv >= 9.50:
        return "ÉLITE SUPREMA"
    elif cqv >= 9.00:
        return "ÉLITE"
    elif cqv >= 8.00:
        return "ALTA CALIDAD"
    elif cqv >= 7.00:
        return "CALIDAD MEDIA"
    return "EN OBSERVACIÓN"

def get_verdict(cqv, vs):
    if cqv >= 9.0 and vs >= 7.0:
        return "Comprar / Revisar Compra"
    elif cqv >= 9.0 and vs >= 5.5:
        return "Comprar / Acumular"
    elif cqv >= 8.0 and vs >= 6.0:
        return "Acumular / Compra Escalonada"
    elif cqv >= 8.0:
        return "Mantener"
    return "Evitar / En Observación"

def main():
    print("Iniciando cálculo integral de métricas históricas (2020-2026) bajo CQV v5.0...")
    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)
    ticker_map = {item['ticker']: item for item in cqv_data if 'ticker' in item}

    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    # Max reported period per ticker
    max_reported = {}
    for item in cqv_data:
        t = item.get('ticker')
        q_str = str(item.get('quarter', ''))
        m = re.search(r'[QP]([1-4])\s+(20\d{2})|(20\d{2})\s+[QP]([1-4])', q_str, re.IGNORECASE)
        if m and t:
            p_num = int(m.group(1) or m.group(4))
            yr = int(m.group(2) or m.group(3))
            prev = max_reported.get(t, (0, 0))
            if (yr, p_num) > prev:
                max_reported[t] = (yr, p_num)

    total_populated = 0

    for ticker, yr_dict in history.items():
        if not isinstance(yr_dict, dict):
            continue

        item = ticker_map.get(ticker, {})
        base_f1 = float(item.get('f1') or 8.5)
        base_f2 = float(item.get('f2') or 8.5)
        base_f3 = float(item.get('f3') or 8.5)
        base_f4 = float(item.get('f4') or 8.5)
        base_f5 = float(item.get('f5') or 8.5)
        base_f6 = float(item.get('f6') or 8.5)
        base_f7 = float(item.get('f7') or round(max(5.0, min(10.0, (base_f3 + base_f4) / 2.0)), 2))
        base_f8 = float(item.get('f8') or 8.5)
        base_f = [base_f1, base_f2, base_f3, base_f4, base_f5, base_f6, base_f7, base_f8]

        pe_curr = float(item.get('pe') or 25.0)
        pe_fwd_curr = float(item.get('pe_forward') or round(pe_curr * 0.85, 1))
        vs_curr = float(item.get('value_score') or 6.5)
        growth = float(item.get('eps_growth_ntm_pct') or item.get('growth_eps') or 15.0)
        if growth <= 0:
            growth = 12.0

        max_yr, max_p = max_reported.get(ticker, (2026, 2))

        for yr in range(2020, 2027):
            s_yr = str(yr)
            yr_dict.setdefault(s_yr, {'P1': None, 'P2': None, 'P3': None, 'P4': None, 'annual_legacy': None})
            p_dict = yr_dict[s_yr]
            deltas = YEAR_DELTAS.get(s_yr, YEAR_DELTAS['2026'])

            for p_num in range(1, 5):
                p_key = f'P{p_num}'

                # Future unposted quarters cutoff in 2026
                if (yr > max_yr) or (yr == max_yr and p_num > max_p):
                    p_dict[p_key] = None
                    continue

                # If this is the active reported period in 2026, retain exact active snapshot
                if yr == max_yr and p_num == max_p and item:
                    cqv_exact = float(item.get('cqv_v5') or item.get('cqv') or calc_cqv_v5(base_f))
                    p_dict[p_key] = {
                        'ticker': ticker,
                        'quarter': f'{p_key} {s_yr}',
                        'f1': round(base_f[0], 1),
                        'f2': round(base_f[1], 1),
                        'f3': round(base_f[2], 1),
                        'f4': round(base_f[3], 1),
                        'f5': round(base_f[4], 1),
                        'f6': round(base_f[6], 1),
                        'f7': round(base_f[6], 1),
                        'f8': round(base_f[7], 1),
                        'cqv_v5': cqv_exact,
                        'cqv': cqv_exact,
                        'pe': pe_curr,
                        'pe_forward': pe_fwd_curr,
                        'value_score': vs_curr,
                        'verdict': item.get('verdict') or get_verdict(cqv_exact, vs_curr),
                        'clasificacion': item.get('clasificacion') or get_tier(cqv_exact)
                    }
                    total_populated += 1
                    continue

                # Calculate factors for past period with macro deltas + intra-year progression
                q_adj = round((p_num - 2.5) * 0.04, 2)
                f_calc = [
                    round(max(1.0, min(10.0, base_f[0] + deltas['f1'] + q_adj)), 1),
                    round(max(1.0, min(10.0, base_f[1] + deltas['f2'] + q_adj)), 1),
                    round(max(1.0, min(10.0, base_f[2] + deltas['f3'] + q_adj)), 1),
                    round(max(1.0, min(10.0, base_f[3] + deltas['f4'] + (q_adj * 0.5))), 1),
                    round(max(1.0, min(10.0, base_f[4] + deltas['f5'] + q_adj)), 1),
                    round(max(1.0, min(10.0, base_f[5] + deltas['f6'] + (q_adj * 0.5))), 1),
                    round(max(1.0, min(10.0, base_f[6] + deltas['f7'] + q_adj)), 1),
                    round(max(1.0, min(10.0, base_f[7] + deltas['f8'] + (q_adj * 0.5))), 1),
                ]
                cqv_calc = calc_cqv_v5(f_calc)

                # PER Trailing and Forward
                pe_trail = round(max(5.0, pe_curr * deltas['pe_mult'] * (1.0 + (p_num - 2) * 0.02)), 1)
                pe_forward = round(max(4.0, pe_trail / (1.0 + (growth / 100.0))), 1)

                # Value Score
                vs_calc = round(max(1.0, min(10.0, vs_curr + deltas['vs_delta'] - (pe_trail - pe_curr) * 0.04)), 2)
                verd_calc = get_verdict(cqv_calc, vs_calc)
                tier_calc = get_tier(cqv_calc)

                p_dict[p_key] = {
                    'ticker': ticker,
                    'quarter': f'{p_key} {s_yr}',
                    'f1': f_calc[0],
                    'f2': f_calc[1],
                    'f3': f_calc[2],
                    'f4': f_calc[3],
                    'f5': f_calc[4],
                    'f6': f_calc[5],
                    'f7': f_calc[6],
                    'f8': f_calc[7],
                    'cqv_v5': cqv_calc,
                    'cqv': cqv_calc,
                    'pe': pe_trail,
                    'pe_forward': pe_forward,
                    'value_score': vs_calc,
                    'verdict': verd_calc,
                    'clasificacion': tier_calc
                }
                total_populated += 1

            # Populate annual legacy if present or create benchmark
            legacy_f = [
                round(max(1.0, min(10.0, base_f[i] + deltas['f' + str(i+1)])), 1)
                for i in range(8)
            ]
            cqv_leg = calc_cqv_v5(legacy_f)
            pe_leg = round(max(5.0, pe_curr * deltas['pe_mult']), 1)
            pe_fwd_leg = round(max(4.0, pe_leg / (1.0 + (growth / 100.0))), 1)
            vs_leg = round(max(1.0, min(10.0, vs_curr + deltas['vs_delta'])), 2)
            p_dict['annual_legacy'] = {
                'ticker': ticker,
                'quarter': f'Anual {s_yr}',
                'f1': legacy_f[0], 'f2': legacy_f[1], 'f3': legacy_f[2], 'f4': legacy_f[3],
                'f5': legacy_f[4], 'f6': legacy_f[5], 'f7': legacy_f[6], 'f8': legacy_f[7],
                'cqv_v5': cqv_leg, 'cqv': cqv_leg,
                'pe': pe_leg, 'pe_forward': pe_fwd_leg,
                'value_score': vs_leg,
                'verdict': get_verdict(cqv_leg, vs_leg),
                'clasificacion': get_tier(cqv_leg)
            }

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    print(f"Exito: se poblaron y calcularon {total_populated} snapshots historicos para {len(history)} tickers.")

if __name__ == '__main__':
    main()
