"""Tab icons (favicon.svg, favicon.ico, apple-touch-icon.png in the site root).

A "T" in DM Serif Text (the site's font), white on a rounded square in the
text colour (--gray-800). The letter is drawn as outlines, so the icon
doesn't depend on the font loading. The .ico (16/32/48 px) is for browsers
without SVG icons; the touch icon (180 px) is square, since iOS rounds it.

    pip install fonttools pillow
    python _tools/favicon.py path/to/DMSerifText-Regular.ttf .

The font: github.com/google/fonts/raw/main/ofl/dmseriftext/DMSerifText-Regular.ttf
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image, ImageDraw
from fontTools.pens.basePen import BasePen

font_path, out = sys.argv[1], sys.argv[2]
BG, FG = '#1f2937', '#ffffff'   # --gray-800 (text colour), white
SIZE, RADIUS, CAP = 32, 7, 0.62  # viewBox, corner radius, letter height / size

f = TTFont(font_path)
gs = f.getGlyphSet()
name = f.getBestCmap()[ord('T')]
bp = BoundsPen(gs); gs[name].draw(bp)
x0, y0, x1, y1 = bp.bounds
s = CAP * SIZE / (y1 - y0)
w, h = (x1 - x0) * s, (y1 - y0) * s
tx = (SIZE - w) / 2 - x0 * s
ty = (SIZE + h) / 2 + y0 * s     # y flipped: font y up, SVG y down
pen = SVGPathPen(gs, ntos=lambda v: f'{v:.2f}'.rstrip('0').rstrip('.'))
gs[name].draw(TransformPen(pen, (s, 0, 0, -s, tx, ty)))
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">'
       f'<rect width="{SIZE}" height="{SIZE}" rx="{RADIUS}" fill="{BG}"/>'
       f'<path fill="{FG}" d="{pen.getCommands()}"/></svg>\n')
open(f'{out}/favicon.svg', 'w').write(svg)

# Raster versions drawn from the same outline at high resolution.
def raster(px, rounded):
    k = 8; big = px * k; scale = big / SIZE
    im = Image.new('RGBA', (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if rounded: d.rounded_rectangle([0, 0, big - 1, big - 1], radius=RADIUS * scale, fill=BG)
    else: d.rectangle([0, 0, big, big], fill=BG)
    class Poly(BasePen):
        def __init__(self, gs): super().__init__(gs); self.polys=[]; self.cur=[]
        def _moveTo(self, p): self.cur=[p]
        def _lineTo(self, p): self.cur.append(p)
        def _curveToOne(self, a, b, c):
            p0 = self.cur[-1]
            for i in range(1, 17):
                t = i / 16; u = 1 - t
                self.cur.append((u**3*p0[0]+3*u*u*t*a[0]+3*u*t*t*b[0]+t**3*c[0], u**3*p0[1]+3*u*u*t*a[1]+3*u*t*t*b[1]+t**3*c[1]))
        def _qCurveToOne(self, a, b):
            p0 = self.cur[-1]
            for i in range(1, 17):
                t = i / 16; u = 1 - t
                self.cur.append((u*u*p0[0]+2*u*t*a[0]+t*t*b[0], u*u*p0[1]+2*u*t*a[1]+t*t*b[1]))
        def _closePath(self): self.polys.append(self.cur); self.cur=[]
    pp = Poly(gs); gs[name].draw(TransformPen(pp, (s*scale, 0, 0, -s*scale, tx*scale, ty*scale)))
    mask = Image.new('L', (big, big), 0); md = ImageDraw.Draw(mask)
    for poly in pp.polys: md.polygon(poly, fill=255)   # T is one contour, no holes
    im.paste(Image.new('RGBA', (big, big), FG), (0, 0), mask)
    return im.resize((px, px), Image.LANCZOS)

raster(180, rounded=False).convert('RGB').save(f'{out}/apple-touch-icon.png', optimize=True)
raster(48, rounded=True).save(f'{out}/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
