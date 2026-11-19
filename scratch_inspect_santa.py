import os
from PIL import Image

src_path = r'C:\Users\ivank\.gemini\antigravity\brain\ddb134be-b8e6-4bde-8ca6-7fb3afc9d6b2\.user_uploaded\media_1794816065642_1376fe10.png'
im = Image.open(src_path)
print("Santa image size:", im.size, "mode:", im.mode)
bbox = im.getbbox()
print("bbox:", bbox)

# Crop tight to content and save to assets/bonus_santa.webp
if bbox:
    cropped = im.crop(bbox)
else:
    cropped = im

dst_path = r'C:\Users\ivank\Desktop\игра_ловля\assets\bonus_santa.webp'
cropped.save(dst_path, 'WEBP', quality=95)
print(f"Saved {dst_path}, size={cropped.size}, aspect ratio={cropped.size[0]/cropped.size[1]:.2f}")
