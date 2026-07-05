from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226962076.jpg"
img = Image.open(img_path)

# Crop the Overview metrics: X from 12 to 448, Y from 630 to 780
cropped = img.crop((12, 630, 448, 780))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_engagement.jpg")
print("Cropped obj_engagement.jpg successfully!")
