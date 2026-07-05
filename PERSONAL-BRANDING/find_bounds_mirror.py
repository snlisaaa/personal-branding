from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226928309.jpg"
img = Image.open(img_path)
width, height = img.size

# Let's find the vertical bounds of the photo in this mirror selfie screenshot.
# The background is black (R,G,B < 15)
center_x = 230
for y in range(120, 800):
    r, g, b = img.getpixel((center_x, y))[:3]
    if r > 15 or g > 15 or b > 15:
        print(f"Photo starts at Y = {y}")
        break

for y in range(800, 120, -1):
    r, g, b = img.getpixel((center_x, y))[:3]
    if r > 15 or g > 15 or b > 15:
        print(f"Photo ends at Y = {y}")
        break
