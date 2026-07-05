import os
import shutil

src_dir = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453"
dest_dir = r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Find all media files
files = [f for f in os.listdir(src_dir) if f.startswith("media__") and (f.endswith(".png") or f.endswith(".jpg"))]

html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Image Catalog</title>
    <style>
        body { font-family: sans-serif; background: #111; color: #eee; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
        .card { background: #222; border: 1px solid #333; padding: 10px; border-radius: 8px; text-align: center; }
        img { max-width: 100%; max-height: 250px; border-radius: 4px; display: block; margin: 0 auto 10px; }
        .name { font-size: 12px; word-break: break-all; font-family: monospace; }
    </style>
</head>
<body>
    <h1>Image Catalog</h1>
    <div class="grid">
"""

for f in files:
    src_path = os.path.join(src_dir, f)
    dest_path = os.path.join(dest_dir, f)
    shutil.copy2(src_path, dest_path)
    
    html_content += f"""
        <div class="card">
            <img src="{f}" alt="{f}">
            <div class="name">{f}</div>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

with open(os.path.join(dest_dir, "catalog.html"), "w", encoding="utf-8") as f_out:
    f_out.write(html_content)

print(f"Successfully copied {len(files)} files and created catalog.html")
