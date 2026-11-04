#!/usr/bin/env python3
"""
Assemble "Minimalist Cat Coloring Book" - KDP print-ready interior PDF.

Geometry (CORRECTION vs the modern-lineart-journal script, which used an
8.625"-wide page = only 0.125" of bleed on one side, 0.125" short of a proper
full-bleed 8.5"-wide trim):

    page size  = 8.75" x 11.25"
                 = 8.5" x 11" trim + 0.125" bleed on ALL four sides
    safe area  = 7.5" x 10.0"  (0.5" margin inside trim on each side)
    designs    = 40 line-art PNGs (1024x1536 px, 2:3 portrait), converted to
                 grayscale, scaled to fit the safe area with aspect ratio
                 preserved -> rendered 6.667" x 10.0", centered, never cropped
                 or stretched. Pure black line art on white.

Page order (84 pages total):
    1         title page
    2         copyright page
    3         "how to use" tips page
    4         blank (padding so the first design starts on a recto page)
    5,7..83   the 40 designs (each on a right-hand / odd page)
    6,8..84   40 blank versos - every design prints one-sided, no bleed-through

Standard PDF base fonts only (Helvetica / Helvetica-Bold). Art is embedded as
grayscale (DeviceGray) - no tinting, no color cast.
"""
import os
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from PIL import Image
from pypdf import PdfReader

SRC = "/home/team/shared/assets/minimalist-cat-coloring-book"
OUT_DIR = "/home/team/shared/launch-package/minimalist-cat-coloring-book"
OUT_PDF = os.path.join(OUT_DIR, "interior.pdf")

TRIM_W, TRIM_H = 8.5, 11.0
BLEED = 0.125
MARGIN = 0.5

WIDTH = (TRIM_W + 2 * BLEED) * inch      # 8.75"
HEIGHT = (TRIM_H + 2 * BLEED) * inch     # 11.25"
SAFE = (MARGIN + BLEED) * inch           # 0.625" from page edge
SAFE_W = WIDTH - 2 * SAFE                # 7.5"  printable width
SAFE_H = HEIGHT - 2 * SAFE               # 10.0" printable height

TITLE = "Minimalist Cat Coloring Book"
DISPLAY_SUB = "40 Simple & Sleek Feline Designs"

TIPS = [
    ("Pick any tools you like.",
     "Colored pencils, gel pens, fine-tip markers and crayons all sit nicely "
     "on the white interior paper."),
    ("Every design is one-sided.",
     "A blank page backs each design, so your colors never ghost onto the next "
     "piece \u2014 and finished pages are easy to trim out and frame."),
    ("The pages fit standard frames.",
     "The trim size is 8.5 \u00d7 11 inches, so a finished design slips straight "
     "into a standard letter-size frame."),
    ("Using alcohol markers?",
     "Slip a spare sheet of paper behind the page you are coloring \u2014 alcohol "
     "inks can bleed through even a blank page."),
    ("Color outside the rules.",
     "Fill every line, or leave areas white and let the minimal lines do the "
     "work. There is no wrong way to use this book."),
]


def load_gray(path):
    """Load art as grayscale and force a pure-white background.

    The source PNGs dither their background between 254 and 255, which can
    print as a faint gray panel against the white page. Clipping values
    >= 250 to 255 is a white-point correction, not an artistic edit: line
    art (all values below 250) stays untouched.
    """
    im = Image.open(path).convert("L")
    im = im.point(lambda v: 255 if v >= 250 else v)
    return im


def wrap(text, font, size, maxw):
    """Greedy word-wrap using real font metrics."""
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


def draw_par(c, text, font, size, x, y, maxw, leading):
    """Left-aligned wrapped paragraph starting at baseline y. Returns next y."""
    c.setFont(font, size)
    for ln in wrap(text, font, size, maxw):
        c.drawString(x, y, ln)
        y -= leading
    return y


def title_page(c):
    # Small geometric-cat motif, centered in the upper third.
    motif = os.path.join(SRC, "05_geometric_cat_head.png")
    im = load_gray(motif)
    mh = 3.4 * inch
    mw = mh * im.size[0] / im.size[1]           # 2.267" wide
    c.drawImage(ImageReader(im), (WIDTH - mw) / 2, 6.35 * inch, mw, mh)

    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(WIDTH / 2, 5.55 * inch, "MINIMALIST CAT")
    c.drawCentredString(WIDTH / 2, 5.00 * inch, "COLORING BOOK")
    c.setFont("Helvetica", 13.5)
    c.drawCentredString(WIDTH / 2, 4.25 * inch, DISPLAY_SUB)
    c.setFont("Helvetica", 11)
    c.drawCentredString(WIDTH / 2, 1.05 * inch, "CRISP LINE PRESS")


def copyright_page(c):
    g = 0.35
    c.setFillColorRGB(g, g, g)
    x = WIDTH / 2
    y = 8.2 * inch
    c.setFont("Helvetica-Bold", 11.5)
    c.drawCentredString(x, y, TITLE)
    y -= 0.30 * inch
    c.setFont("Helvetica", 9.5)
    c.drawCentredString(x, y, "Copyright \u00a9 2026 Crisp Line Press")
    y -= 0.42 * inch
    for ln in [
        "All rights reserved. No part of this publication may be reproduced, distributed, or transmitted",
        "in any form or by any means, including photocopying, recording, or other electronic or mechanical",
        "methods, without the prior written permission of the publisher, except in the case of brief",
        "quotations embodied in critical reviews and certain other noncommercial uses permitted by",
        "copyright law.",
    ]:
        c.drawCentredString(x, y, ln)
        y -= 0.19 * inch
    y -= 0.15 * inch
    for ln in [
        "The designs in this book are licensed for personal, non-commercial use only:",
        "please do not resell or redistribute the artwork in any form.",
    ]:
        c.drawCentredString(x, y, ln)
        y -= 0.19 * inch
    y -= 0.32 * inch
    c.drawCentredString(x, y, "First Edition: November 2026")
    y -= 0.22 * inch
    c.drawCentredString(x, y, "Independently published by Crisp Line Press")
    y -= 0.22 * inch
    c.drawCentredString(x, y, "All illustrations are original artwork created for this edition.")


def tips_page(c):
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(WIDTH / 2, 9.75 * inch, "How to Use This Book")
    y = 9.00 * inch
    tx = 1.05 * inch
    tw = 6.65 * inch
    for head, body in TIPS:
        c.setFont("Helvetica-Bold", 11.5)
        c.drawString(tx, y, head)
        y -= 0.24 * inch
        y = draw_par(c, body, "Helvetica", 10.5, tx, y, tw, 0.21 * inch)
        y -= 0.16 * inch


def design_page(c, path):
    """Scale to fit the safe area, centered, aspect preserved, never cropped."""
    im = load_gray(path)           # grayscale, white background normalized
    iw, ih = im.size
    scale = min(SAFE_W / iw, SAFE_H / ih)
    dw, dh = iw * scale, ih * scale
    c.drawImage(ImageReader(im), (WIDTH - dw) / 2, (HEIGHT - dh) / 2, dw, dh)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    pngs = sorted(f for f in os.listdir(SRC) if f.endswith(".png"))
    assert len(pngs) == 40, f"expected 40 designs, found {len(pngs)}"

    c = canvas.Canvas(OUT_PDF, pagesize=(WIDTH, HEIGHT))
    c.setTitle(TITLE)
    c.setAuthor("Crisp Line Press")
    c.setSubject("Minimalist line-art coloring book: 40 sleek feline designs, one-sided pages")
    c.setCreator("Crisp Line Press")
    # NOTE: page size itself carries the bleed (8.75 x 11.25 = trim + 0.125).
    # reportlab 5.1's setTrimBox/setBleedBox write malformed boxes, so we
    # deliberately do not set them - KDP sizes the trim from the page box.

    title_page(c)
    c.showPage()
    copyright_page(c)
    c.showPage()
    tips_page(c)
    c.showPage()
    c.showPage()                       # page 4: blank so designs start recto
    for f in pngs:
        design_page(c, os.path.join(SRC, f))
        c.showPage()                   # design (odd / right-hand page)
        c.showPage()                   # blank verso
    c.save()

    # --- verification ---
    r = PdfReader(OUT_PDF)
    n = len(r.pages)
    mb = r.pages[0].mediabox
    print(f"saved:    {OUT_PDF}")
    print(f"pages:    {n} (expected 84)")
    print(f"mediabox: {float(mb.width) / 72:.4f} x {float(mb.height) / 72:.4f} in")
    print(f"size:     {os.path.getsize(OUT_PDF) / 1024 / 1024:.1f} MB")
    print(f"metadata: title={r.metadata.title!r} author={r.metadata.author!r}")
    assert n == 84, "page count mismatch"
    assert abs(float(mb.width) / 72 - 8.75) < 1e-6
    assert abs(float(mb.height) / 72 - 11.25) < 1e-6
    print("VERIFIED: 84 pages, 8.75 x 11.25 in with bleed")


if __name__ == "__main__":
    main()
