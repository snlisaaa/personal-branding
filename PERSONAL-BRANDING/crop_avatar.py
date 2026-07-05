from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293470.jpg"
img = Image.open(img_path)

# Crop coordinates for the clean square profile picture of Lisa:
# X from 88 to 372, Y from 145 to 420
cropped = img.crop((88, 145, 372, 420))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\lisa_avatar.jpg")
print("Cropped lisa_avatar.jpg successfully!")
