import sys, glob, os
from PIL import Image, ImageDraw
src = sys.argv[1]
out = sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 4
files = sorted(glob.glob(os.path.join(src, 'slide-*.png')))
os.makedirs(out, exist_ok=True)
for k in range(0, len(files), per):
    chunk = files[k:k+per]
    cols = 2
    rows = (len(chunk) + 1) // 2
    tw, th = 960, 540
    sheet = Image.new('RGB', (cols * tw + 10 * (cols + 1), rows * th + 10 * (rows + 1)), (60, 60, 60))
    for i, f in enumerate(chunk):
        im = Image.open(f).convert('RGB').resize((tw, th), Image.LANCZOS)
        x = 10 + (i % cols) * (tw + 10)
        y = 10 + (i // cols) * (th + 10)
        sheet.paste(im, (x, y))
        d = ImageDraw.Draw(sheet)
        d.rectangle([x, y, x + 70, y + 22], fill=(0, 0, 0))
        d.text((x + 6, y + 5), os.path.basename(f)[6:8], fill=(255, 255, 255))
    p = os.path.join(out, f'sheet-{k//per+1:02d}.png')
    sheet.save(p)
    print(p)
