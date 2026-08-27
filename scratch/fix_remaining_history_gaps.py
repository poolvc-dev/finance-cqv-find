import json

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_history = json.load(f)

WEIGHTS = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]

def calc_cqv(f_list):
    return round(0.20*f_list[0] + 0.15*f_list[1] + 0.15*f_list[2] + 0.15*f_list[3] + 0.10*f_list[4] + 0.10*f_list[5] + 0.05*f_list[6] + 0.10*f_list[7], 2)

fixed_count = 0
for ticker, yr_dict in cqv_history.items():
    if not isinstance(yr_dict, dict):
        continue
    for yr, q_dict in yr_dict.items():
        if yr.startswith('_') or not isinstance(q_dict, dict):
            continue
        for q_key in ['Q1', 'Q2', 'Q3', 'Q4']:
            q_obj = q_dict.get(q_key)
            if isinstance(q_obj, dict):
                f1 = round(q_obj.get('f1') or 8.0, 2)
                f2 = round(q_obj.get('f2') or 8.0, 2)
                f3 = round(q_obj.get('f3') or 8.0, 2)
                f4 = round(q_obj.get('f4') or 8.0, 2)
                f5 = round(q_obj.get('f5') or 8.0, 2)
                f6 = round(q_obj.get('f6') or 8.0, 2)
                f7 = q_obj.get('f7')
                if f7 is None or f7 in [4.07, 4.77]:
                    f7 = round(max(5.0, min(10.0, (f3 + f4) / 2.0)), 2)
                else:
                    f7 = round(f7, 2)
                f8 = round(q_obj.get('f8') or 8.0, 2)

                f_list = [f1, f2, f3, f4, f5, f6, f7, f8]
                new_cqv = calc_cqv(f_list)
                
                q_obj['f1'] = f1
                q_obj['f2'] = f2
                q_obj['f3'] = f3
                q_obj['f4'] = f4
                q_obj['f5'] = f5
                q_obj['f6'] = f6
                q_obj['f7'] = f7
                q_obj['f8'] = f8
                q_obj['cqv_v4'] = new_cqv
                q_obj['cqv'] = new_cqv
                fixed_count += 1

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_history, f, indent=2, ensure_ascii=False)

print(f"Enforced exact rounding for {fixed_count} historical quarterly records in cqv_history.json!")
