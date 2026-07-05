from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293470.jpg"
img = Image.open(img_path)

# Let's crop using the coordinates found: X from 12 to 448, Y from 145 to 562
cropped = img.crop((12, 145, 448, 562))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\lisa_portrait_clean.jpg")
print("Clean portrait cropped at exact boundaries Y=145 to Y=562!")
