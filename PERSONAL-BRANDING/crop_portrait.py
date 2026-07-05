from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293470.jpg"
img = Image.open(img_path)

# Let's crop the image content. In a 460x1024 mobile screenshot, 
# the post image is usually centered horizontally and occupies 
# the full width of 460, starting below the header.
# Let's try crop coordinates: x0=0, y0=138, x1=460, y1=598 (which is 460px high)
cropped = img.crop((0, 138, 460, 598))
cropped.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\lisa_portrait.jpg")
print("Cropped lisa_portrait.jpg successfully!")
