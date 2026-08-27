with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    gd_code = f.read()

gd_code = gd_code.replace("const historySelect =", "var historySelect =")
gd_code = gd_code.replace("const simSelect =", "var simSelect =")
gd_code = gd_code.replace("const themeIcon =", "var themeIcon =")

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(gd_code)

print("[OK] Replaced const with var for element selectors in generate_dashboard.py")

with open("dashboard.html", "r", encoding="utf-8") as f:
    dh_code = f.read()

dh_code = dh_code.replace("const historySelect =", "var historySelect =")
dh_code = dh_code.replace("const simSelect =", "var simSelect =")
dh_code = dh_code.replace("const themeIcon =", "var themeIcon =")

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(dh_code)

print("[OK] Replaced const with var for element selectors in dashboard.html")
