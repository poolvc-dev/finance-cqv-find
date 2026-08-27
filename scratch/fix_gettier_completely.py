import re

def clean_gettier_completely(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    clean_func = """function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }"""

    # Match any messed up getTier block
    code = re.sub(
        r'(// Data Helpers\s*)?function getTier\(score\) \{[\s\S]*?return \{ name: \'ESPECULATIVA\', class: \'tier-speculative\' \};\s*\}[\s\S]*?\}',
        r'// Data Helpers\n        ' + clean_func,
        code
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"[OK] Cleaned getTier completely in {filepath}")

clean_gettier_completely("generate_dashboard.py")
clean_gettier_completely("dashboard.html")
