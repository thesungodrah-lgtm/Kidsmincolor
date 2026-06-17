#!/usr/bin/env python3
"""Assemble Modern Line Art Journal — print-ready PDF."""
import os
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PIL import Image

SRC = "/home/team/shared/assets/modern-line-art-journal"
OUT_DIR = "/home/team/shared/books/modern-lineart-journal"
OUT_PDF = os.path.join(OUT_DIR, "interior.pdf")
os.makedirs(OUT_DIR, exist_ok=True)

WIDTH = 8.625 * inch
HEIGHT = 11.25 * inch
BLEED = 0.125 * inch
MARGIN = 0.5 * inch
SAFE = MARGIN + BLEED

pngs = sorted([f for f in os.listdir(SRC) if f.endswith(".png")])
print(f"Found {len(pngs)} images")

c = canvas.Canvas(OUT_PDF, pagesize=(WIDTH, HEIGHT))
c.setTitle("Modern Line Art Journal")
c.setAuthor("Crisp Line Press")

# Title page
c.setFont("Helvetica-Bold", 30)
c.drawCentredString(WIDTH/2, HEIGHT/2 + 1*inch, "Modern Line Art Journal")
c.setFont("Helvetica", 18)
c.drawCentredString(WIDTH/2, HEIGHT/2 + 0.3*inch, "Minimalist Black & White Patterns")
c.setFont("Helvetica", 14)
c.setFillColorRGB(0.5, 0.5, 0.5)
c.drawCentredString(WIDTH/2, HEIGHT/2 - 0.8*inch, "Crisp Line Press")
c.showPage()

# Copyright
c.setFillColorRGB(0.5, 0.5, 0.5)
c.setFont("Helvetica", 10)
c.drawCentredString(WIDTH/2, HEIGHT/2, "\u00a9 2026 Crisp Line Press. All rights reserved.")
c.showPage()

# Pattern pages — each image fills the full page (centered, scaled to fit trim area)
for fname in pngs:
    img_path = os.path.join(SRC, fname)
    try:
        im = Image.open(img_path)
    except:
        continue
    
    iw, ih = im.size
    
    # Scale image to fill the safe printable area
    max_w = WIDTH - 2*SAFE
    max_h = HEIGHT - 2*SAFE
    scale = min(max_w/iw, max_h/ih)
    dw, dh = iw*scale, ih*scale
    
    bx = BLEED * inch
    x = bx + (WIDTH - 2*bx - dw) / 2
    y = bx + (HEIGHT - 2*bx - dh) / 2
    
    c.drawImage(img_path, x, y, width=dw, height=dh, preserveAspectRatio=True)
    c.showPage()

c.save()
print(f"PDF saved: {OUT_PDF}")
print(f"Pages: {2 + len(pngs)} ({2} front matter + {len(pngs)} pattern pages)")
print(f"Size: {os.path.getsize(OUT_PDF)/1024/1024:.1f} MB")