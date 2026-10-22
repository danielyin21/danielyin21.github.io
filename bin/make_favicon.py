#!/usr/bin/env python
"""Draw the 皓 seal favicon set.

Writes favicon.ico, assets/img/favicon.svg and assets/img/apple-touch-icon.png.
The glyph comes from Ma Shan Zheng (SIL OFL), fetched from Google Fonts as a
one-character subset unless --font is given. Don't swap in a macOS system font:
their licence doesn't allow publishing glyph outlines.

usage:
  pip install fonttools pillow
  python bin/make_favicon.py [--font FONT.ttf] [--preview preview.png]
"""

import argparse
import os
import re
import tempfile
import urllib.parse
import urllib.request

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHAR = "皓"
FAMILY = "Ma Shan Zheng"
RED = "#A32D2D"
INK = "#FCEBEB"
GLYPH = 40  # glyph's longest side, in 64-unit seal space
GLYPH_SMALL = 46  # larger glyph for the 16 px icon, which drops the inner frame


def fetch_font():
    """Download a subset of FAMILY containing only CHAR; returns its path."""
    query = urllib.parse.urlencode({"family": FAMILY, "text": CHAR})
    with urllib.request.urlopen(f"https://fonts.googleapis.com/css2?{query}") as r:
        css = r.read().decode()
    url = re.search(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", css).group(1)
    path = os.path.join(tempfile.mkdtemp(), "font.ttf")
    urllib.request.urlretrieve(url, path)
    return path


def svg_icon(font_path, glyph_size, frame=True):
    f = TTFont(font_path)
    gs = f.getGlyphSet()
    name = f.getBestCmap()[ord(CHAR)]
    bp = BoundsPen(gs)
    gs[name].draw(bp)
    x0, y0, x1, y1 = bp.bounds
    k = glyph_size / max(x1 - x0, y1 - y0)
    tx = 32 - k * (x0 + x1) / 2
    ty = 32 + k * (y0 + y1) / 2
    pp = SVGPathPen(gs)
    gs[name].draw(pp)
    frame_el = (
        f'<rect x="5" y="5" width="54" height="54" rx="4" fill="none" stroke="{INK}" stroke-width="2.5"/>'
        if frame
        else ""
    )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<rect width="64" height="64" rx="8" fill="{RED}"/>'
        f"{frame_el}"
        f'<path fill="{INK}" transform="translate({tx:.3f} {ty:.3f}) scale({k:.5f} {-k:.5f})" d="{pp.getCommands()}"/>'
        "</svg>\n"
    )


def raster(font_path, size, glyph_size, frame=True, rounded=True, R=1024):
    """Render at R px, then downsample to size."""
    u = R / 64
    img = Image.new("RGBA", (R, R), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, R - 1, R - 1], radius=8 * u, fill=RED)
    else:
        d.rectangle([0, 0, R - 1, R - 1], fill=RED)
    if frame:
        w = 2.5 * u
        d.rounded_rectangle(
            [5 * u - w / 2, 5 * u - w / 2, 59 * u + w / 2, 59 * u + w / 2],
            radius=4 * u + w / 2,
            outline=INK,
            width=round(w),
        )
    probe = ImageFont.truetype(font_path, 1000)
    bx0, by0, bx1, by1 = probe.getbbox(CHAR)
    fs = 1000 * glyph_size * u / max(bx1 - bx0, by1 - by0)
    font = ImageFont.truetype(font_path, round(fs))
    bx0, by0, bx1, by1 = font.getbbox(CHAR)
    d.text((R / 2 - (bx0 + bx1) / 2, R / 2 - (by0 + by1) / 2), CHAR, font=font, fill=INK)
    return img.resize((size, size), Image.LANCZOS)


def preview(font_path, out):
    """Framed vs. frameless at tab sizes, on light and dark strips, zoomed 4x."""
    cells = [
        lambda s: raster(font_path, s, GLYPH),
        lambda s: raster(font_path, s, GLYPH_SMALL, frame=False),
    ]
    sheet = Image.new("RGB", (2 * 360, 2 * 200), "white")
    for row, bg in enumerate(["#F1EFE8", "#3a3a38"]):
        for col, fn in enumerate(cells):
            ox, oy = col * 360, row * 200
            ImageDraw.Draw(sheet).rectangle([ox, oy, ox + 359, oy + 199], fill=bg)
            x = ox + 16
            for s in (16, 32):
                im = fn(s)
                sheet.paste(im, (x, oy + 16), im)
                z = im.resize((s * 4, s * 4), Image.NEAREST)
                sheet.paste(z, (x, oy + 56), z)
                x += s * 4 + 24
            big = fn(128).resize((96, 96))
            sheet.paste(big, (x, oy + 56), big)
    sheet.save(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--font", help=f"font file with {CHAR} (default: fetch {FAMILY} from Google Fonts)")
    ap.add_argument("--preview", help="also write a tab-size preview sheet to this path")
    args = ap.parse_args()
    font_path = args.font or fetch_font()

    with open(os.path.join(ROOT, "assets/img/favicon.svg"), "w") as fh:
        fh.write(svg_icon(font_path, GLYPH))

    ico = [
        raster(font_path, 16, GLYPH_SMALL, frame=False),
        raster(font_path, 32, GLYPH),
        raster(font_path, 48, GLYPH),
    ]
    ico[-1].save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)], append_images=ico[:-1])

    # iOS masks its own rounded corners, so the touch icon is a full-bleed square
    raster(font_path, 180, GLYPH, rounded=False).convert("RGB").save(os.path.join(ROOT, "assets/img/apple-touch-icon.png"))

    if args.preview:
        preview(font_path, args.preview)


if __name__ == "__main__":
    main()
