from PIL import Image

im = Image.open(r'C:\Users\ivank\Desktop\игра_ловля\scratch_user_score_crop.png').convert('RGB')
w, h = im.size

# Find the bounding boxes of the digits (+350) and the coin
text_ymin, text_ymax, text_xmin, text_xmax = 9999, -1, 9999, -1
coin_ymin, coin_ymax, coin_xmin, coin_xmax = 9999, -1, 9999, -1

for y in range(h):
    for x in range(w):
        r, g, b = im.getpixel((x, y))
        # Blue text (+350): r < 30, g between 40 and 100, b > 120
        if r < 30 and g > 40 and g < 110 and b > 120:
            text_ymin = min(text_ymin, y)
            text_ymax = max(text_ymax, y)
            text_xmin = min(text_xmin, x)
            text_xmax = max(text_xmax, x)
        # Orange coin: r > 200, g between 80 and 180, b < 60
        if r > 200 and g > 80 and g < 180 and b < 60:
            coin_ymin = min(coin_ymin, y)
            coin_ymax = max(coin_ymax, y)
            coin_xmin = min(coin_xmin, x)
            coin_xmax = max(coin_xmax, x)

print(f"Text in crop: x={text_xmin}..{text_xmax} (w={text_xmax-text_xmin}), y={text_ymin}..{text_ymax} (h={text_ymax-text_ymin})")
print(f"Coin in crop: x={coin_xmin}..{coin_xmax} (w={coin_xmax-coin_xmin}), y={coin_ymin}..{coin_ymax} (h={coin_ymax-coin_ymin})")
print(f"Coin height / text height: {(coin_ymax-coin_ymin)/(text_ymax-text_ymin):.2f}")
