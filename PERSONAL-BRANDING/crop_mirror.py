from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226928309.jpg"
img = Image.open(img_path)

# Let's crop a square photo of the mirror selfie: X from 88 to 372, Y from 138 to 350
cropped = img.crop((88, 138, 372, 350))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_mirror_crop.jpg")
print("Cropped obj_mirror_crop.jpg successfully!")
