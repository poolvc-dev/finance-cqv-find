import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Search for .toFixed calls without null check
matches = re.findall(r'([a-zA-Z0-9_\.\[\]]+)\.toFixed\(', html)
print("Found .toFixed targets:", set(matches))
