with open(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\style.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "avatar-placeholder" in line or "about-avatar" in line or "avatar-ring" in line:
        print(f"Line {i+1}: {line.strip()}")
