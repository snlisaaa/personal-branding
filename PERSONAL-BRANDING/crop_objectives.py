from PIL import Image

# Coordinates for crops in 460x1024 mobile screenshots:
# - Summary card: X from 12 to 448, Y from 345 to 600 or Y=590 to Y=850 depending on post.
# - Action row: X from 12 to 448, Y from 370 to 445 (for Let Them post).

# 1. Awareness: already done (obj_awareness.jpg)

# 2. Engagement: let's use the action row from Let Them post (media__1783226928335.jpg)
# showing 55 likes, 7 comments, 14 shares, 10 saves, 2 bookmarks.
img_letthem = Image.open(r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226928335.jpg")
crop_eng = img_letthem.crop((12, 370, 448, 445))
crop_eng.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_engagement.jpg")

# 3. Lead Gen: summary card of Mirror Selfie post (media__1783226928309.jpg)
img_mirror = Image.open(r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783226928309.jpg")
crop_lead = img_mirror.crop((12, 380, 448, 590))
crop_lead.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_leadgen.jpg")

# 4. Lead Quality: summary card of Let Them post (media__1783226928335.jpg)
crop_quality = img_letthem.crop((12, 630, 448, 840))
crop_quality.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_leadquality.jpg")

# 5. Pain Points: let's use the summary card of the Book Page post (media__1783227293479.jpg)
# which shows 406 views, 8 interactions, and profile activity.
img_bookpage = Image.open(r"C:\Users\lenovo\.gemini\antigravity\brain\34a87eb0-2102-431d-bd12-9eb739dcb453\media__1783227293479.jpg")
crop_pain = img_bookpage.crop((12, 630, 448, 840))
crop_pain.save(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\assets\images\obj_painpoints.jpg")

print("Created all 5 cropped images for Slide 4 objectives!")
