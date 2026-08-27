import json

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_history = json.load(f)

# Define exact historical progression for APP
# Weights: F1:0.20, F2:0.15, F3:0.15, F4:0.15, F5:0.10, F6:0.10, F7:0.05, F8:0.10

history_params = {
    '2020': {'f': [8.20, 8.00, 8.50, 7.50, 7.80, 8.80, 8.00, 7.80], 'pe': 44.0, 'vs': 5.25, 'v': 'Acumular / Compra Escalonada'},
    '2021': {'f': [8.40, 8.20, 8.70, 7.80, 8.00, 9.00, 8.20, 8.00], 'pe': 49.0, 'vs': 5.35, 'v': 'Acumular / Compra Escalonada'},
    '2022': {'f': [8.00, 7.80, 7.20, 7.80, 7.80, 9.00, 8.20, 7.80], 'pe': 34.0, 'vs': 6.05, 'v': 'Acumular / Compra Escalonada'},
    '2023': {'f': [8.80, 8.50, 9.00, 8.50, 8.50, 9.30, 8.80, 8.50], 'pe': 37.0, 'vs': 6.25, 'v': 'Acumular / Compra Escalonada'},
    '2024': {'f': [9.20, 8.80, 9.30, 8.90, 9.00, 9.50, 9.10, 8.80], 'pe': 41.0, 'vs': 6.45, 'v': 'Comprar / Acumular'},
    '2025': {'f': [9.50, 9.00, 9.50, 9.10, 9.20, 9.60, 9.30, 9.00], 'pe': 43.0, 'vs': 6.70, 'v': 'Comprar / Acumular'},
    '2026_Q1': {'f': [9.60, 9.00, 9.40, 9.20, 9.20, 9.60, 9.30, 9.00], 'pe': 45.0, 'vs': 6.60, 'v': 'Comprar / Acumular'},
    '2026_Q2': {'f': [9.70, 9.10, 9.60, 9.30, 9.35, 9.65, 9.40, 9.10], 'pe': 36.80, 'pe_fwd': 27.50, 'vs': 6.85, 'v': 'Comprar / Acumular'}
}

def calc_cqv(f_list):
    w = [0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10]
    return round(sum(f_list[i] * w[i] for i in range(8)), 2)

if 'APP' not in cqv_history:
    cqv_history['APP'] = {}

for yr in ['2020', '2021', '2022', '2023', '2024', '2025']:
    params = history_params[yr]
    f_list = params['f']
    cqv_val = calc_cqv(f_list)
    
    if yr not in cqv_history['APP']:
        cqv_history['APP'][yr] = {}
        
    for q_key in ['Q1', 'Q2', 'Q3', 'Q4']:
        cqv_history['APP'][yr][q_key] = {
            'ticker': 'APP',
            'quarter': f"{q_key} {yr}",
            'f1': f_list[0], 'f2': f_list[1], 'f3': f_list[2], 'f4': f_list[3],
            'f5': f_list[4], 'f6': f_list[5], 'f7': f_list[6], 'f8': f_list[7],
            'cqv_v4': cqv_val, 'cqv': cqv_val,
            'pe': params['pe'],
            'value_score': params['vs'],
            'verdict': params['v']
        }

# Year 2026
if '2026' not in cqv_history['APP']:
    cqv_history['APP']['2026'] = {}

q1_params = history_params['2026_Q1']
q1_f = q1_params['f']
q1_cqv = calc_cqv(q1_f)
cqv_history['APP']['2026']['Q1'] = {
    'ticker': 'APP',
    'quarter': 'Q1 2026',
    'f1': q1_f[0], 'f2': q1_f[1], 'f3': q1_f[2], 'f4': q1_f[3],
    'f5': q1_f[4], 'f6': q1_f[5], 'f7': q1_f[6], 'f8': q1_f[7],
    'cqv_v4': q1_cqv, 'cqv': q1_cqv,
    'pe': q1_params['pe'],
    'value_score': q1_params['vs'],
    'verdict': q1_params['v']
}

q2_params = history_params['2026_Q2']
q2_f = q2_params['f']
q2_cqv = calc_cqv(q2_f)
cqv_history['APP']['2026']['Q2'] = {
    'ticker': 'APP',
    'quarter': 'Q2 2026',
    'f1': q2_f[0], 'f2': q2_f[1], 'f3': q2_f[2], 'f4': q2_f[3],
    'f5': q2_f[4], 'f6': q2_f[5], 'f7': q2_f[6], 'f8': q2_f[7],
    'cqv_v4': q2_cqv, 'cqv': q2_cqv,
    'pe': q2_params['pe'],
    'pe_forward': q2_params['pe_fwd'],
    'value_score': q2_params['vs'],
    'verdict': q2_params['v']
}

cqv_history['APP']['2026']['Q3'] = None
cqv_history['APP']['2026']['Q4'] = None

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_history, f, indent=2, ensure_ascii=False)

print("Successfully calibrated AppLovin (APP) historical CQV progression in cqv_history.json (2020-2026)!")
