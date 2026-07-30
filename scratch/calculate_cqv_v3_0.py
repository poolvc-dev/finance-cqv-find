"""
Algoritmo Standalone: CQV v3.0 (8 Macro-Factores Pro)
Metodología: metodo_v3.0.md
Fórmula: CQV v3.0 = (F1*0.20) + (F2*0.10) + (F3*0.10) + (F4*0.20) + (F5*0.10) + (F6*0.10) + (F7*0.10) + (F8*0.10)
Filtro: Si F4 < 6.0 o F2 < 5.0 => CQV v3.0 = min(CQV v3.0, 7.00)
"""

import sys
import json
import os

def calculate_cqv_v3_0(f1, f2, f3, f4, f5, f6, f7, f8):
    """
    Calcula el score CQV v3.0 con los 8 factores cuantitativa y cualitativamente desglosados.
    """
    score = (f1 * 0.20) + (f2 * 0.10) + (f3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.10) + (f8 * 0.10)
    
    # Filtro de Degradación Fundamental
    if f4 < 6.0 or f2 < 5.0:
        score = min(score, 7.00)
        
    return round(score, 2)

if __name__ == '__main__':
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'FICO'
    print(f"=== CALCULADORA STANDALONE CQV v3.0: {ticker} ===")
    
    f1, f2, f3, f4, f5, f6, f7, f8 = 10.00, 9.36, 9.82, 9.91, 9.69, 9.51, 9.45, 8.66
    if os.path.exists('cqv_qualitative_config.json'):
        with open('cqv_qualitative_config.json', 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        if ticker in cfg:
            t_cfg = cfg[ticker]
            f1 = t_cfg.get('f1', f1)
            f2 = t_cfg.get('f2', f2)
            f3 = t_cfg.get('f3', f3)
            f4 = t_cfg.get('f4', f4)
            f5 = t_cfg.get('f5', f5)
            f6 = t_cfg.get('f6', f6)
            f7 = t_cfg.get('f7', f7)
            f8 = t_cfg.get('f8', f8)

    cqv_v3 = calculate_cqv_v3_0(f1, f2, f3, f4, f5, f6, f7, f8)
    print(f"Factores v3.0: F1={f1}, F2={f2}, F3={f3}, F4={f4}, F5={f5}, F6={f6}, F7={f7}, F8={f8}")
    print(f"CQV v3.0 Score: {cqv_v3} / 10.00")
