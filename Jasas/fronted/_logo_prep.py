from PIL import Image
from collections import Counter

src = r"C:\Users\Вадим\.cursor\projects\d-Agents-mini-app\assets\____________226_20261113140806-3bac1b71-046f-4acd-9750-134068eb1cca.png"
im = Image.open(src).convert("RGB")
px = im.load()
cols = Counter()
for y in range(240, 764):
    for x in range(321, 812):
        r, g, b = px[x, y]
        if r + g + b < 25:
            continue
        cols[(r // 16 * 16, g // 16 * 16, b // 16 * 16)] += 1
print("top colors")
for c, n in cols.most_common(24):
    print(c, n)
