from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293470.jpg"
img = Image.open(img_path)

# Let's crop only the actual photo box, which is a square roughly 
# centered from X=15 to X=445 (width 430) and Y=144 to Y=574.
cropped = img.crop((12, 144, 448, 580))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\lisa_portrait_clean.jpg")
print("Cropped clean portrait successfully!")
