from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783225732429.png"
img = Image.open(img_path)

# Crop the Views section: X from 242 to 425, Y from 195 to 395
cropped = img.crop((242, 195, 425, 395)).convert("RGB")
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_awareness.jpg")
print("Cropped obj_awareness.jpg successfully!")
