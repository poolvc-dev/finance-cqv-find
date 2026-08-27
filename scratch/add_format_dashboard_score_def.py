with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

func_defs = """        function formatDashboardScore(value) {
            return (value !== undefined && value !== null && Number.isFinite(Number(value))) ? Number(value).toFixed(2) : 'N/D';
        }

        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }
"""

# Insert right after 'let companies = [];'
if "function formatDashboardScore" not in code:
    code = code.replace("let companies = [];", "let companies = [];\n" + func_defs)

with open('generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("[OK] Added formatDashboardScore and getTier definitions to generate_dashboard.py")
