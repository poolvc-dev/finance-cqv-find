def fix_gettier(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    bad = """;
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }"""

    good = """function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }"""

    if bad in code:
        code = code.replace(bad, good)
        print(f"[OK] Replaced malformed getTier in {filepath}")
    else:
        # Fallback replacing `;` followed by if (score >= 9.0)
        code = code.replace(";\n            if (score >= 9.0) return", "function getTier(score) {\n            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };\n            if (score >= 9.0) return")
        print(f"[OK] Applied fallback fix in {filepath}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

fix_gettier("generate_dashboard.py")
fix_gettier("dashboard.html")
