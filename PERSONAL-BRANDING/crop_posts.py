import os
from PIL import Image

src_dir = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453"
dest_dir = r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images"

posts = {
    "mirror": "media__1783226928309.jpg",
    "group": "media__1783226962076.jpg",
    "letthem": "media__1783226928335.jpg",
    "camera": "media__1783226928343.jpg",
    "bedah": "media__1783226962037.jpg",
    "bazar": "media__1783226928305.jpg",
    "portrait": "media__1783227293470.jpg",
    "bookpage": "media__1783227293479.jpg"
}

for name, filename in posts.items():
    img_path = os.path.join(src_dir, filename)
    if not os.path.exists(img_path):
        print(f"Skipping {name}: {filename} not found")
        continue
        
    img = Image.open(img_path)
    # Let's find the vertical bounds of the post image.
    # The Instagram background is very dark (R,G,B < 30).
    # We will scan from Y=100 to Y=700 down the center column.
    center_x = img.width // 2
    
    y_start = None
    y_end = None
    
    for y in range(120, 750):
        r, g, b = img.getpixel((center_x, y))[:3]
        # If color is not dark gray (R,G,B > 35)
        if r > 35 or g > 35 or b > 35:
            y_start = y
            break
            
    for y in range(750, 120, -1):
        r, g, b = img.getpixel((center_x, y))[:3]
        if r > 35 or g > 35 or b > 35:
            y_end = y
            break
            
    if y_start is not None and y_end is not None:
        # Give 5px padding
        y_start = max(120, y_start - 3)
        y_end = min(img.height, y_end + 3)
        
        # Crop full width
        cropped = img.crop((0, y_start, img.width, y_end))
        # Convert to RGB if RGBA
        if cropped.mode == "RGBA":
            cropped = cropped.convert("RGB")
            
        out_path = os.path.join(dest_dir, f"post_{name}.jpg")
        cropped.save(out_path)
        print(f"Cropped post_{name}.jpg: Y={y_start} to Y={y_end}")
    else:
        print(f"Could not find bounds for {name}")
