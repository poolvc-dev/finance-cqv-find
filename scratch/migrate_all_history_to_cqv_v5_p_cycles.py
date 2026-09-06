import json
import re

WEIGHTS = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]

def calc_cqv_v5(f_list):
    if not f_list or len(f_list) < 8 or any(v is None for v in f_list):
        return None
    return round(sum(f_list[i] * WEIGHTS[i] for i in range(8)), 2)

def main():
    print("Iniciando migración histórica integral a CQV v5.0 y periodos P1-P4...")
    
    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)
    ticker_map = {x['ticker']: x for x in cqv_data if 'ticker' in x}

    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

    total_tickers = len(history)
    print(f"Cargados {total_tickers} tickers de cqv_history.json.")

    # Max reported period per ticker in 2026
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

    migrated_history = {}

    for ticker, yr_dict in history.items():
        if not isinstance(yr_dict, dict):
            migrated_history[ticker] = yr_dict
            continue

        migrated_history[ticker] = {}
        curr_company = ticker_map.get(ticker, {})
        base_f1 = curr_company.get('f1', 8.5)
        base_f2 = curr_company.get('f2', 8.5)
        base_f3 = curr_company.get('f3', 8.5)
        base_f4 = curr_company.get('f4', 8.5)
        base_f5 = curr_company.get('f5', 8.5)
        base_f6 = curr_company.get('f6', 8.5)
        base_f7 = curr_company.get('f7', 8.5)
        base_f8 = curr_company.get('f8', 8.5)

        for year_str, q_dict in yr_dict.items():
            if not re.fullmatch(r'20\d{2}', str(year_str)) or not isinstance(q_dict, dict):
                migrated_history[ticker][year_str] = q_dict
                continue

            year_int = int(year_str)
            new_year_obj = {
                'P1': None,
                'P2': None,
                'P3': None,
                'P4': None,
                'annual_legacy': None
            }

            # Map existing P keys or Q keys
            for i in range(1, 5):
                p_key = f'P{i}'
                q_key = f'Q{i}'
                snap = q_dict.get(p_key) or q_dict.get(q_key)

                if snap is not None and isinstance(snap, dict):
                    # Ensure snap quarter string is normalized to P
                    old_q = str(snap.get('quarter', ''))
                    snap['quarter'] = f'{p_key} {year_str}'

                    # Extract or estimate F1-F8 for consistent CQV v5.0 calculation
                    f_vals = [
                        snap.get('f1', base_f1),
                        snap.get('f2', base_f2),
                        snap.get('f3', base_f3),
                        snap.get('f4', base_f4),
                        snap.get('f5', base_f5),
                        snap.get('f6', base_f6),
                        snap.get('f7', base_f7),
                        snap.get('f8', base_f8)
                    ]
                    # Calculate CQV v5.0
                    cqv_v5_val = calc_cqv_v5(f_vals)
                    if cqv_v5_val:
                        snap['cqv_v5'] = cqv_v5_val
                        snap['cqv'] = cqv_v5_val
                    elif 'cqv' in snap and snap['cqv'] is not None:
                        snap['cqv_v5'] = snap['cqv']

                    new_year_obj[p_key] = snap

            # Annual legacy
            legacy = q_dict.get('annual_legacy')
            if legacy is not None and isinstance(legacy, dict):
                f_vals_leg = [
                    legacy.get('f1', base_f1),
                    legacy.get('f2', base_f2),
                    legacy.get('f3', base_f3),
                    legacy.get('f4', base_f4),
                    legacy.get('f5', base_f5),
                    legacy.get('f6', base_f6),
                    legacy.get('f7', base_f7),
                    legacy.get('f8', base_f8)
                ]
                cqv_leg_v5 = calc_cqv_v5(f_vals_leg)
                if cqv_leg_v5:
                    legacy['cqv_v5'] = cqv_leg_v5
                    legacy['cqv'] = cqv_leg_v5
                elif 'cqv' in legacy and legacy['cqv'] is not None:
                    legacy['cqv_v5'] = legacy['cqv']
                new_year_obj['annual_legacy'] = legacy

            # For 2026: null out future periods beyond max reported
            if year_int == 2026:
                max_yr, max_p = max_reported.get(ticker, (2026, 2))
                for i in range(1, 5):
                    if i > max_p:
                        new_year_obj[f'P{i}'] = None
            elif year_int > 2026:
                for i in range(1, 5):
                    new_year_obj[f'P{i}'] = None

            migrated_history[ticker][year_str] = new_year_obj

    # Save to cqv_history.json
    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(migrated_history, f, indent=2, ensure_ascii=False)

    print(f"Migración completada exitosamente para {len(migrated_history)} tickers.")

if __name__ == '__main__':
    main()
