"""build_cover.py -- final cover builder for the Minimalist Cat Coloring Book.

This is the script that produced cover.pdf / cover.png in this folder: palette
"D" (Ink navy & cream), art 04_cat_sleeping_crescent_moon.png, spine
deliberately text-free. It also renders the rejected "E" (slate) alternative
for reference; cover.pdf in this folder is D.
"""
#!/usr/bin/env python3
"""
make_variants.py -- "Minimalist Cat Coloring Book": THREE color-direction cover
variants (A/B/C) for owner review. Cover-only pass: interior.pdf, the approved
assemble_cover.py and its cover.pdf/cover.png outputs are NOT touched.

Wrap geometry -- identical to the verified assemble_cover.py:
    spine  = 84 x 0.002252                     = 0.189168"
    page   = (17 + spine + 0.25) x 11.25       = 17.439168" x 11.25"
    panels L->R: bleed | back 8.5 | spine | front 8.5 | bleed; 0.125" bleed.

Front-cover art: 04_cat_sleeping_crescent_moon.png ("crescent-moon sleeper"),
replacing 14_regal_sitting_cat everywhere. The art is cropped to its content
bounding box, white-point corrected, and placed as RGBA with a transparent
background so panels/discs show through. Line art stays pure black (A, C) or
reversed bone (B); color is used only in fields, panels and type.

Spine text: 84 pages >= KDP's 79-page minimum for spine text. KDP rule: spine
text must fit within the spine and leave >= 0.0625" (1.6 mm) clear of each
spine edge. All-caps text occupies only its cap height (0.718 em for
Helvetica-Bold), so the largest fully compliant size here is
    (0.189168 - 2 x 0.0625) x 72 / 0.718 = 6.43 pt;
6.2 pt is used, leaving 0.0637" clearance per side (a real margin, not a
rounding-edge pass). Rendered evidence: spine-zoom.png.
"""
import os
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
import pypdfium2 as pdfium

SRC = "/home/team/shared/assets/minimalist-cat-coloring-book"
ART = os.path.join(SRC, "04_cat_sleeping_crescent_moon.png")
OUT_DIR = ("/home/team/shared/launch-package/minimalist-cat-coloring-book/"
           "cover-variants")

PAGES = 84
SPINE = PAGES * 0.002252            # 0.189168"
TRIM_W, TRIM_H = 8.5, 11.0
BLEED = 0.125
W = (17 + SPINE + 0.25) * inch      # 17.439168"
H = (TRIM_H + 2 * BLEED) * inch     # 11.25"

BACK_X0 = BLEED * inch
BACK_X1 = (BLEED + TRIM_W) * inch   # 8.625"  (back trim / spine boundary)
SPINE_X1 = BACK_X1 + SPINE * inch   # 8.814168" (spine / front boundary)
FRONT_X1 = SPINE_X1 + TRIM_W * inch # 17.314168"

FRONT_CX = (SPINE_X1 + FRONT_X1) / 2
BACK_CX = (BACK_X0 + BACK_X1) / 2

TITLE_LINES = ("MINIMALIST CAT", "COLORING BOOK")
SUBTITLE = "40 Simple & Sleek Feline Designs"
PRESS = "CRISP LINE PRESS"
SPINE_TITLE = "MINIMALIST CAT COLORING BOOK"
SPINE_PT = 6.2                      # see docstring: max compliant is 6.43 pt
SPINE_GAP = 0.38 * inch             # gap between spine title and press name

BACK_HEAD = "Simple lines. Sophisticated cats."
BLURB_1 = ("A coloring book for people who love clean lines and quiet design. "
           "Forty minimalist cats \u2014 sleeping, stretching, prowling, peeking out "
           "of paper bags, wearing scarves \u2014 rendered in crisp black line art on "
           "a pure white page.")
BLURB_2 = ("No busy backgrounds. No clutter, no tiny fiddly spaces. Just sleek "
           "feline forms and plenty of white space, ready for colored pencils, "
           "gel pens, or fine-tip markers.")
POINTS = [
    "40 unique designs \u2014 one cat per page, from a geometric cat head to a "
    "mother cat and kitten",
    "One-sided printing \u2014 a blank page backs every design, so colors never "
    "ghost through to the next piece",
    "Large 8.5 \u00d7 11 pages \u2014 finished designs slip straight into standard "
    "letter-size frames",
    "For adults, teens, and anyone who colors to unwind",
]

# ---------------------------------------------------------------- palettes --
PALETTES = {
    "D": dict(
        stem="D-navy-cream",
        name="Ink navy & cream",
        field="#24405E",     # deep navy field (front bands, spine)
        panel="#F6EFE3",     # cream art panel / back field
        ink="#F6EFE3",       # cream type on navy
        body="#2E2A27",      # charcoal body type on cream
        press="#F6EFE3",
        head="#24405E",
        rule=None,
        foot="#24405E",
        spine_bg="#24405E", spine_ink="#F6EFE3", spine_text=False,
        art_line=(0, 0, 0),
        disc=None,
    ),
    "E": dict(
        stem="E-slate-cream",
        name="Slate blue & cream",
        field="#4C6E91",     # muted slate blue field
        panel="#F6EFE3",
        ink="#F6EFE3",
        body="#2E2A27",
        press="#F6EFE3",
        head="#4C6E91",
        rule=None,
        foot="#4C6E91",
        spine_bg="#4C6E91", spine_ink="#F6EFE3", spine_text=False,
        art_line=(0, 0, 0),
        disc=None,
    ),
}

# ------------------------------------------------------------------- art ---
def load_art_gray():
    """Cleaned (white point fixed), cropped-to-content grayscale art."""
    im = Image.open(ART).convert("L")
    im = im.point(lambda v: 255 if v >= 250 else v)
    bbox = im.point(lambda v: 0 if v >= 250 else 255).getbbox()
    pad = int(0.04 * max(bbox[2] - bbox[0], bbox[3] - bbox[1]))
    x0 = max(0, bbox[0] - pad); y0 = max(0, bbox[1] - pad)
    x1 = min(im.width, bbox[2] + pad); y1 = min(im.height, bbox[3] + pad)
    return im.crop((x0, y0, x1, y1))


def art_rgba(line_rgb):
    """Art as RGBA: line pixels in line_rgb, background transparent."""
    im = load_art_gray()
    alpha = im.point(lambda v: 255 - v)          # dark -> opaque
    planes = [Image.new("L", im.size, c) for c in line_rgb] + [alpha]
    return Image.merge("RGBA", planes)


# ---------------------------------------------------------------- helpers --
def wrap(text, font, size, maxw):
    lines, cur = [], ""
    for w in text.split():
        cand = (cur + " " + w).strip()
        if stringWidth(cand, font, size) <= maxw:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_par(c, text, font, size, color, x, y, maxw, leading):
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in wrap(text, font, size, maxw):
        c.drawString(x, y, ln)
        y -= leading
    return y


def tracked_center(c, text, font, size, color, cx, y, tracking=0.0):
    w = stringWidth(text, font, size) + tracking * (len(text) - 1)
    t = c.beginText(cx - w / 2, y)
    t.setFont(font, size)
    t.setFillColor(color)
    t.setCharSpace(tracking)
    t.textOut(text)
    c.drawText(t)


def bullet(c, text, color, x, y, maxw, leading=0.20 * inch):
    c.setFont("Helvetica", 10.5)
    c.setFillColor(color)
    c.drawString(x, y, "\u2022")
    for ln in wrap(text, "Helvetica", 10.5, maxw - 0.25 * inch):
        c.drawString(x + 0.25 * inch, y, ln)
        y -= leading
    return y - 0.10 * inch


# ------------------------------------------------------------------ spine --
def spine_panel(c, p, art_im):
    """Spine strip + rotated, centred spine text (KDP-compliant size)."""
    c.setFillColor(HexColor(p["spine_bg"]))
    c.rect(BACK_X1, 0, SPINE * inch, H, stroke=0, fill=1)
    if not p.get("spine_text", True):
        return                                  # spine left as a clean field

    font, size, tracking = "Helvetica-Bold", SPINE_PT, 0.4
    cap = size * 0.718 / 72                    # cap height in inches
    w_title = stringWidth(SPINE_TITLE, font, size) + tracking * (len(SPINE_TITLE) - 1)
    w_press = stringWidth(PRESS, font, size) + tracking * (len(PRESS) - 1)
    total = w_title + SPINE_GAP + w_press      # in points
    x_mid = (BACK_X1 + SPINE_X1) / 2
    baseline_x = x_mid - cap / 2 * inch        # centre cap band on the spine
    y_top = H / 2 + total / 2                  # start of text (reads downward)

    c.saveState()
    c.translate(baseline_x, y_top)
    c.rotate(-90)                              # top-to-bottom, US convention
    t = c.beginText(0, 0)
    t.setFont(font, size)
    t.setFillColor(HexColor(p["spine_ink"]))
    t.setCharSpace(tracking)
    t.textOut(SPINE_TITLE)
    c.drawText(t)
    c.restoreState()

    c.saveState()
    c.translate(baseline_x, y_top - w_title - SPINE_GAP)
    c.rotate(-90)
    t = c.beginText(0, 0)
    t.setFont(font, size)
    t.setFillColor(HexColor(p["spine_ink"]))
    t.setCharSpace(tracking)
    t.textOut(PRESS)
    c.drawText(t)
    c.restoreState()


# ------------------------------------------------------------------ front --
def front_panel(c, p, key, art_im):
    ink = HexColor(p["ink"])

    if p["panel"] is not None:
        # Terracotta field; cream panel band bleeding to the right edge.
        c.setFillColor(HexColor(p["panel"]))
        c.rect(SPINE_X1, 0.95 * inch, W - SPINE_X1, 7.35 * inch, stroke=0, fill=1)
        ah = 6.2 * inch
        aw = ah * art_im.width / art_im.height
        c.drawImage(ImageReader(art_im), FRONT_CX - aw / 2, 0.95 * inch + (7.35 - 6.2) / 2 * inch,
                    aw, ah, mask="auto")
        title_color = HexColor(p["ink"])
        press_color = HexColor(p["press"])
    elif key == "B":
        # Reversed bone line art floating directly on the teal field.
        ah = 6.5 * inch
        aw = ah * art_im.width / art_im.height
        c.drawImage(ImageReader(art_im), FRONT_CX - aw / 2, 1.55 * inch,
                    aw, ah, mask="auto")
        title_color = HexColor(p["ink"])
        press_color = HexColor(p["press"])
    else:
        # Off-white field; one muted ochre disc behind the crescent moon.
        ah = 6.4 * inch
        aw = ah * art_im.width / art_im.height
        ax, ay = FRONT_CX - aw / 2, 1.65 * inch
        cx0, cy0 = ax + aw / 2, ay + ah / 2
        c.setFillColor(HexColor(p["disc"]))
        c.circle(cx0 - 0.05 * aw, cy0 + 0.05 * ah, 0.56 * aw, stroke=0, fill=1)
        c.drawImage(ImageReader(art_im), ax, ay, aw, ah, mask="auto")
        title_color = HexColor(p["ink"])
        press_color = HexColor(p["press"])

    tracked_center(c, TITLE_LINES[0], "Helvetica-Bold", 46, title_color,
                   FRONT_CX, 10.02 * inch, tracking=2.0)
    tracked_center(c, TITLE_LINES[1], "Helvetica-Bold", 46, title_color,
                   FRONT_CX, 9.34 * inch, tracking=2.0)
    c.setFont("Helvetica", 15)
    c.setFillColor(title_color)
    c.drawCentredString(FRONT_CX, 8.72 * inch, SUBTITLE)
    tracked_center(c, PRESS, "Helvetica", 10, press_color, FRONT_CX,
                   0.62 * inch, tracking=2.2)


# ------------------------------------------------------------------- back --
def back_panel(c, p):
    # Back-field fill already applied in build(); this is text only.
    ink = HexColor(p["body"])
    bx = 1.0 * inch
    bw = 6.4 * inch
    y = 10.0 * inch
    if p["rule"]:
        c.setFillColor(HexColor(p["rule"]))
        c.rect(bx, y + 0.09 * inch, 0.55 * inch, 0.035 * inch, stroke=0, fill=1)
        y -= 0.22 * inch
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor(p["head"]))
    c.drawString(bx, y, BACK_HEAD)
    y -= 0.30 * inch
    y = draw_par(c, BLURB_1, "Helvetica", 10.5, ink, bx, y, bw, 0.20 * inch) - 0.14 * inch
    y = draw_par(c, BLURB_2, "Helvetica", 10.5, ink, bx, y, bw, 0.20 * inch) - 0.24 * inch
    for point in POINTS:
        y = bullet(c, point, ink, bx, y, bw)
    tracked_center(c, PRESS, "Helvetica", 9, HexColor(p["foot"]), BACK_CX,
                   0.95 * inch, tracking=2.2)
    # Bottom-right barcode zone (x > 6.375", y < 1.575" from trim corner)
    # deliberately left clear for KDP's auto-placed ISBN barcode.


# ------------------------------------------------------------------ build --
def build(key, art_cache):
    p = PALETTES[key]
    pdf_path = os.path.join(OUT_DIR, f"{p['stem']}.pdf")
    png_path = os.path.join(OUT_DIR, f"{p['stem']}.png")

    art_im = art_cache["bone" if key == "B" else "black"]

    c = canvas.Canvas(pdf_path, pagesize=(W, H))
    c.setTitle(f"Minimalist Cat Coloring Book - Cover Variant {key} ({p['name']})")
    c.setAuthor("Crisp Line Press")
    c.setCreator("Crisp Line Press")
    # Page size carries the bleed; reportlab 5.1 box setters write malformed
    # boxes, so box rects are deliberately not set (same as assemble_cover.py).

    c.setFillColor(HexColor(p["field"]))
    c.rect(0, 0, W, H, stroke=0, fill=1)          # full-bleed base
    if p["panel"] is not None:                                # cream back field over base
        c.setFillColor(HexColor(p["panel"]))
        c.rect(0, 0, BACK_X1, H, stroke=0, fill=1)
    spine_panel(c, p, art_im)
    back_panel(c, p)
    front_panel(c, p, key, art_im)
    c.save()

    pdf = pdfium.PdfDocument(pdf_path)
    img = pdf[0].render(scale=300 / 72).to_pil().convert("RGB")
    img.save(png_path, optimize=True, dpi=(300, 300))

    r = PdfReader(pdf_path)
    mb = r.pages[0].mediabox
    print(f"[{key}] {p['name']}: {pdf_path}")
    print(f"     page {float(mb.width)/72:.6f} x {float(mb.height)/72:.6f} in | "
          f"pdf {os.path.getsize(pdf_path)/1024:.0f} KB | png "
          f"{img.width}x{img.height} {os.path.getsize(png_path)/1024/1024:.2f} MB")
    return png_path


def slug(name):
    return name.lower().replace("&", "and").replace(" ", "-")


# ------------------------------------------------------ spine zoom (evidence)
def spine_zoom(png_paths):
    """Rendered evidence: spine text of each variant, rotated to horizontal,
    magnified. Shows legibility at print size on the 0.189168\" spine."""
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 46)
    rows = []
    for key, path in zip("ABC", png_paths):
        im = Image.open(path)
        # crop spine strip +/- 0.35"; the text group is centred on the spine,
        # so centre the window there with a half-window covering the group
        cx_in = (BACK_X1 / inch + SPINE_X1 / inch) / 2
        w_title = stringWidth(SPINE_TITLE, "Helvetica-Bold", SPINE_PT)
        group_in = (w_title + SPINE_GAP / inch * 72 +
                    stringWidth(PRESS, "Helvetica-Bold", SPINE_PT)) / 72
        half = max(1.55, group_in / 2 + 0.15)
        x0 = int((cx_in - 0.35) * 300); x1 = int((cx_in + 0.35) * 300)
        y0 = int((H / inch / 2 - half) * 300); y1 = int((H / inch / 2 + half) * 300)
        crop = im.crop((x0, im.height - y1, x1, im.height - y0))
        crop = crop.rotate(90, expand=True)         # text reads left-to-right
        scale = 2200 / crop.width
        crop = crop.resize((2200, int(crop.height * scale)), Image.NEAREST)
        rows.append((key, crop))
    label_h, pad = 86, 36
    total_h = sum(r.height for _, r in rows) + len(rows) * (label_h + pad) + pad
    out = Image.new("RGB", (2200, total_h), "#FFFFFF")
    d = ImageDraw.Draw(out)
    y = pad
    for key, r in rows:
        d.text((18, y), f"{key} — {PALETTES[key]['name']}  (spine text, 6.2 pt Helvetica-Bold, magnified)",
               fill="#1A1A1A", font=font)
        y += label_h
        out.paste(r, (0, y))
        y += r.height + pad
    path = os.path.join(OUT_DIR, "spine-zoom.png")
    out.save(path, optimize=True)
    print(f"spine zoom: {path} ({os.path.getsize(path)/1024:.0f} KB)")
    return path


# ------------------------------------------------------------- compare grid --
def compare(png_paths):
    font_big = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    font_small = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    panel_w = 480
    gutter, label_h = 30, 120
    thumbs = []
    for path in png_paths:
        im = Image.open(path)
        # front trim only: x in [SPINE_X1, FRONT_X1], y in [BLEED, BLEED+11]
        # (render is 300 px per inch; page constants are in points -> /inch)
        px = lambda pos_in: int(pos_in * 300)        # inches -> rendered px
        box = (px(SPINE_X1 / inch), px(H / inch - BLEED - 11.0),
               px(FRONT_X1 / inch), px(H / inch - BLEED))
        crop = im.crop(box)
        crop = crop.resize((panel_w, int(panel_w * 11 / 8.5)), Image.LANCZOS)
        thumbs.append(crop)
    tw = len(thumbs) * panel_w + (len(thumbs) + 1) * gutter
    th = thumbs[0].height + label_h + 2 * gutter
    out = Image.new("RGB", (tw, th), "#FFFFFF")
    d = ImageDraw.Draw(out)
    for i, (key, t) in enumerate(zip("ABC", thumbs)):
        x = gutter + i * (panel_w + gutter)
        out.paste(t, (x, gutter))
        cx = x + panel_w / 2
        w = d.textlength(key, font=font_big)
        d.text((cx - w / 2, thumbs[0].height + gutter + 6), key,
               fill="#1A1A1A", font=font_big)
        name = PALETTES[key]["name"]
        w = d.textlength(name, font=font_small)
        d.text((cx - w / 2, thumbs[0].height + gutter + 82), name,
               fill="#555555", font=font_small)
    path = os.path.join(OUT_DIR, "compare.png")
    out.save(path, optimize=True)
    print(f"compare:    {path} ({out.width}x{out.height}, "
          f"{os.path.getsize(path)/1024:.0f} KB)")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    art_cache = {"black": art_rgba((0, 0, 0))}
    for k in "DE":
        build(k, art_cache)


if __name__ == "__main__":
    main()
