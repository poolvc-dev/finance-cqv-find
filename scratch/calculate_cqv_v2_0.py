"""
Algoritmo Standalone: CQV v2.0 (8 Macro-Factores Legacy)
Metodología: metodo_v2.0.md
Fórmula: CQV v2.0 = (F1*0.20) + (F2*0.10) + (F3*0.10) + (F4*0.20) + (F5*0.10) + (F6*0.10) + (F7*0.10) + (F8*0.10)
Heurísticas Legacy:
  F6 = (F1 + F3) / 2
  F7 = max(1.0, min(10.0, 10.0 - (F1 - 5.0) * 0.8))
  F8 = 8.0 (predeterminado)
"""

import sys
import json
import os

def calculate_cqv_v2_0(f1, f2, f3, f4, f5, f6=None, f7=None, f8=None):
    """
    Calcula el score CQV v2.0 aplicando las heurísticas históricas de v2.0 si no se pasan f6, f7 o f8.
    """
    if f6 is None:
        f6 = round((f1 + f3) / 2.0, 2)
    if f7 is None:
        f7 = round(max(1.0, min(10.0, (10.0 - (f1 - 5.0)) * 0.8)), 2)
    if f8 is None:
        f8 = 8.00

    score = (f1 * 0.20) + (f2 * 0.10) + (f3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.10) + (f8 * 0.10)
    return round(score, 2), f6, f7, f8

if __name__ == '__main__':
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'FICO'
    print(f"=== CALCULADORA STANDALONE CQV v2.0 (LEGACY): {ticker} ===")
    
    f1, f2, f3, f4, f5 = 10.00, 8.75, 9.50, 9.90, 9.50
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

    cqv_v2, f6, f7, f8 = calculate_cqv_v2_0(f1, f2, f3, f4, f5)
    print(f"Factores v2.0: F1={f1}, F2={f2}, F3={f3}, F4={f4}, F5={f5}, F6={f6}, F7={f7}, F8={f8}")
    print(f"CQV v2.0 Score: {cqv_v2} / 10.00")
