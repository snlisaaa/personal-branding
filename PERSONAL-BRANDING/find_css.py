with open(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "obj-card" in line or "objectives-grid" in line:
        print(f"Line {i+1}: {line.strip()}")
