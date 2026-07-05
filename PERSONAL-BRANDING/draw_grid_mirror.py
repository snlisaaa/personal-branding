from PIL import Image, ImageDraw

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226928309.jpg"
img = Image.open(img_path).convert("RGB")

draw = ImageDraw.Draw(img)
for y in range(0, img.height, 50):
    draw.line([(0, y), (img.width, y)], fill="red", width=1)
    draw.text((10, y + 2), str(y), fill="red")
for x in range(0, img.width, 50):
    draw.line([(x, 0), (x, img.height)], fill="blue", width=1)
    draw.text((x + 2, 10), str(x), fill="blue")

img.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\grid_mirror.jpg")
print("Grid check for mirror selfie saved!")
