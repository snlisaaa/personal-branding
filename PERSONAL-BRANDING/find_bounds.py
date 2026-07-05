from PIL import Image

img_path = r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293470.jpg"
img = Image.open(img_path)
width, height = img.size

# Let's scan a vertical line down the center of the image (X = 230)
# and find where the background of the photo is.
# The background is light gray (e.g. R, G, B > 150).
# Let's print out the RGB values and find the exact coordinates.
center_x = 230
for y in range(100, 700):
    r, g, b = img.getpixel((center_x, y))[:3]
    if r > 150 and g > 150 and b > 150:
        print(f"Light area starts at Y = {y} with RGB = {(r, g, b)}")
        break

for y in range(700, 100, -1):
    r, g, b = img.getpixel((center_x, y))[:3]
    if r > 150 and g > 150 and b > 150:
        print(f"Light area ends at Y = {y} with RGB = {(r, g, b)}")
        break
