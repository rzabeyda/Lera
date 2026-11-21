from PIL import Image, ImageDraw, ImageFont
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#12466a"/><text x="32" y="46" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="800" font-size="40" fill="#f2a93b">P</text></svg>'''
open(os.path.join(OUT, 'favicon.svg'), 'w', encoding='utf-8').write(svg)
def render(n):
    im = Image.new('RGBA', (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, n - 1, n - 1], radius=int(n * .22), fill='#12466a')
    f = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', int(n * .68))
    b = d.textbbox((0, 0), 'P', font=f); w, h = b[2] - b[0], b[3] - b[1]
    d.text(((n - w) / 2 - b[0], (n - h) / 2 - b[1]), 'P', font=f, fill='#f2a93b')
    return im
render(180).save(os.path.join(OUT, 'apple-touch-icon.png'))
render(512).save(os.path.join(OUT, 'icon-512.png'))
render(256).save(os.path.join(OUT, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
print('icons ok')
