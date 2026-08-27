def fix_trailing(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    bad = """        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }"""

    good = """        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }"""

    if bad in code:
        code = code.replace(bad, good)
        print(f"[OK] Fixed trailing getTier lines in {filepath}")
    else:
        code = code.replace("return { name: 'ESPECULATIVA', class: 'tier-speculative' };\n        };\n            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };\n            return { name: 'ESPECULATIVA', class: 'tier-speculative' };\n        }", "return { name: 'ESPECULATIVA', class: 'tier-speculative' };\n        }")
        print(f"[OK] Applied fallback fix in {filepath}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

fix_trailing("generate_dashboard.py")
fix_trailing("dashboard.html")
