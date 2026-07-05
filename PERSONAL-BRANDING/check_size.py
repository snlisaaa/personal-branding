from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293470.jpg"
img = Image.open(img_path)
print(f"Size: {img.size}")
