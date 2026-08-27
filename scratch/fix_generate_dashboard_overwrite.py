import re

with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    code = f.read()

old_write_block = """        json_data = json.dumps(records, indent=2)
        
        # 1. Save raw JSON data to cqv_data.json
        with open('cqv_data.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
        print("Successfully saved cqv_data.json")"""

new_write_block = """        if os.path.exists('cqv_data.json'):
            with open('cqv_data.json', 'r', encoding='utf-8') as f:
                records = json.load(f)
        json_data = json.dumps(records, indent=2, ensure_ascii=False)"""

if old_write_block in code:
    code = code.replace(old_write_block, new_write_block)
    print("[OK] Prevented cqv_data.json overwrite in generate_dashboard.py")

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(code)
