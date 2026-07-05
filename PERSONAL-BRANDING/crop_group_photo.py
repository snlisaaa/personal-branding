from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226962076.jpg"
img = Image.open(img_path)

# Let's crop the actual Group Photo image box:
# X from 88 to 372, Y from 189 to 375
cropped = img.crop((88, 189, 372, 375))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_group_crop.jpg")
print("Cropped obj_group_crop.jpg successfully!")
