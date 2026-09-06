import json
import os
from pathlib import Path

def main():
    print("Iniciando purga completa de SMH (VanEck Semiconductor ETF)...")

    # 1. cqv_data.json
    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    before_len = len(data)
    data = [x for x in data if x.get('ticker') != 'SMH']
    after_len = len(data)
    print(f"cqv_data.json: {before_len} -> {after_len} registros (eliminado SMH: {before_len - after_len})")

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # 2. cqv_history.json
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        hist = json.load(f)

    if 'SMH' in hist:
        del hist['SMH']
        print("cqv_history.json: Ticker SMH eliminado con éxito.")
    else:
        print("cqv_history.json: SMH no estaba presente.")

    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(hist, f, indent=2, ensure_ascii=False)

    # 3. Informes en inform/
    smh_reports = list(Path('inform').glob('**/*SMH*'))
    for rep in smh_reports:
        try:
            os.remove(rep)
            print(f"Eliminado informe: {rep}")
        except Exception as e:
            print(f"Error eliminando {rep}: {e}")

    print("Purga de SMH completada.")

if __name__ == '__main__':
    main()
