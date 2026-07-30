"""
Algoritmo Standalone: CQV v1.1 (5 Macro-Factores Pro con ROIC Real y Filtro de Degradación)
Metodología: metodo_v1.1.md
Fórmula: CQV v1.1 = (F1_v1.1 * 0.25) + (F2_v1.1 * 0.15) + (F3_v1.1 * 0.15) + (F4 * 0.25) + (F5 * 0.20)
Filtro: Si F4 < 6.0 o F2_v1.1 < 5.0 => CQV v1.1 = min(CQV v1.1, 7.00)
"""

import sys
import json
import os

def compute_real_roic(nopat, invested_capital):
    if not invested_capital or invested_capital <= 0:
        return 0.0
    return nopat / invested_capital

def calculate_cqv_v1_1(f1_v1_1, f2_v1_1, f3_v1_1, f4, f5):
    """
    Calcula el score CQV v1.1 aplicando el filtro de degradación fundamental.
    """
    score = (f1_v1_1 * 0.25) + (f2_v1_1 * 0.15) + (f3_v1_1 * 0.15) + (f4 * 0.25) + (f5 * 0.20)
    
    # Filtro de Degradación Fundamental
    if f4 < 6.0 or f2_v1_1 < 5.0:
        score = min(score, 7.00)
        
    return round(score, 2)

if __name__ == '__main__':
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'FICO'
    print(f"=== CALCULADORA STANDALONE CQV v1.1: {ticker} ===")
    
    f1_v1_1, f2_v1_1, f3_v1_1, f4, f5 = 10.00, 9.36, 9.82, 9.91, 9.69
    if os.path.exists('cqv_qualitative_config.json'):
        with open('cqv_qualitative_config.json', 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        if ticker in cfg:
            t_cfg = cfg[ticker]
            f1_v1_1 = t_cfg.get('f1', f1_v1_1)
            f2_v1_1 = t_cfg.get('f2', f2_v1_1)
            f3_v1_1 = t_cfg.get('f3', f3_v1_1)
            f4 = t_cfg.get('f4', f4)
            f5 = t_cfg.get('f5', f5)

    cqv_v1_1 = calculate_cqv_v1_1(f1_v1_1, f2_v1_1, f3_v1_1, f4, f5)
    print(f"Factores v1.1: F1={f1_v1_1}, F2={f2_v1_1}, F3={f3_v1_1}, F4={f4}, F5={f5}")
    print(f"CQV v1.1 Score: {cqv_v1_1} / 10.00")
