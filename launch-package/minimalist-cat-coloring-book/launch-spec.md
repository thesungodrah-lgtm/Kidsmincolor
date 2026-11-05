# Launch Specification — Minimalist Cat Coloring Book
**Generated:** 2026-11-04
**Updated:** 2026-11-04 — cover finalized as **Variant D "Ink navy & cream"** (art: crescent-moon sleeper; spine deliberately left text-free). Pricing, keywords, description and upload steps unchanged.
**Project:** minimalist-cat-coloring-book
**ISBN Status:** Pending (KDP auto-assigns free ISBN, or upload your own — see §11)

---

## 1. Book Details

| Field | Value |
|---|---|
| **Title** | Minimalist Cat Coloring Book |
| **Subtitle** | 40 Simple & Sleek Feline Designs — Relaxing One-Sided Line Art for Adults, Teens & Cat Lovers |
| **Author** | Crisp Line Press |
| **Series** | None yet (4th standalone title; a "Crisp Line Press Minimalist Coloring" series can be set up later — see §10) |
| **Edition** | First Edition (November 2026) |
| **Language** | English |
| **Trim Size** | 8.5" × 11" (US Letter) |
| **Page Count** | **84 pages** (interior.pdf verified with pypdf) |
| **Interior Type** | Black & White (art embedded as grayscale) |
| **Paper Color** | White (standard for coloring books — maximum contrast) |
| **Bleed** | Yes — 0.125" on all four sides included in the PDF |

**Team decision honored:** the phrase "for adults" is deliberately **not** in the title. The age-neutral minimalist/modern phrasing lives in the title; "adults", "teens", "relaxing" and "simple" are carried in the subtitle (above) and the backend keywords (§3).

### Page Breakdown (exact, 84 pages)
| PDF pages | Content |
|---|---|
| 1 | Title page (typography + small geometric-cat motif) |
| 2 | Copyright page |
| 3 | "How to Use This Book" tips page |
| 4 | Blank — padding so the first design lands on a **recto** (right-hand) page |
| 5, 7 … 83 (odd) | The 40 designs — each on a right-hand page, scaled to the safe area |
| 6, 8 … 84 (even) | 40 blank versos — **every design prints one-sided** (no bleed-through onto the next design) |

### Geometry — including a correction vs. the previous title
- PDF page size: **8.75" × 11.25"** = 8.5" × 11" trim **+ 0.125" bleed on every side**.
- **Correction note:** the `modern-lineart-journal` build script used an **8.625"-wide** page — i.e. only 0.125" of bleed on one side, 0.125" short of a proper full-bleed 8.5" trim. This title uses the correct 8.75" width (bleed on both sides). `assemble_interior.py` documents this in its docstring; older journals may deserve the same fix if they are ever revised.
- Safe area: 0.5" margin inside trim → **7.5" × 10.0"** printable. Each 1024×1536 px (2:3) design is height-limited to **10.0" tall × 6.667" wide**, centered, aspect ratio preserved, never cropped or stretched. No page numbers over art.
- Print-prep fix applied: the source PNGs dither their background between gray values 254 and 255; `assemble_interior.py` clips values ≥ 250 to pure white so no faint gray panel prints (also why the PDF is small).

---

## 2. Product Description

### Marketing Description (Amazon visible — plain text)
> A coloring book for people who love clean lines and quiet design.
>
> Forty minimalist cats — sleeping, stretching, prowling, peeking out of paper bags, wearing scarves — rendered in crisp black line art on a pure white page. No busy backgrounds, no clutter, no tiny fiddly spaces: just sleek feline forms and plenty of white space, ready for colored pencils, gel pens, or fine-tip markers.
>
> **Inside this book:**
> • 40 unique cat designs — one per page, from a geometric cat head to a mother cat and kitten
> • One-sided printing — a blank page backs every design, so colors never ghost through
> • Large 8.5 × 11 pages — finished designs slip straight into standard letter-size frames
> • Bold, clean line art for adults, teens, and anyone who colors to unwind
>
> A thoughtful, low-clutter gift for cat lovers — or a quiet hour for yourself.

### Same description, HTML-ready (KDP-safe tags: `<b>`, `<br>`)
```html
<b>A coloring book for people who love clean lines and quiet design.</b><br><br>
Forty minimalist cats — sleeping, stretching, prowling, peeking out of paper bags, wearing scarves — rendered in crisp black line art on a pure white page. No busy backgrounds, no clutter, no tiny fiddly spaces: just sleek feline forms and plenty of white space, ready for colored pencils, gel pens, or fine-tip markers.<br><br>
<b>Inside this book:</b><br>
• 40 unique cat designs — one per page, from a geometric cat head to a mother cat and kitten<br>
• One-sided printing — a blank page backs every design, so colors never ghost through<br>
• Large 8.5 × 11 pages — finished designs slip straight into standard letter-size frames<br>
• Bold, clean line art for adults, teens, and anyone who colors to unwind<br><br>
A thoughtful, low-clutter gift for cat lovers — or a quiet hour for yourself.
```

### Back Cover Description
The back cover (already composed in `cover.pdf`) carries the two-paragraph blurb plus four bullet selling points: 40 one-per-page designs; one-sided printing; large frame-ready pages; for adults, teens, and anyone who colors to unwind. No reviews, no star ratings, no bestseller claims.

---

## 3. Backend Keywords (7 slots)

Market basis (not invented): `keyword_research.md`, Niche 5 — target keyword **"minimalist cat coloring book"**, competition Low (~900 competing books per that research), noting cat coloring books are popular while minimalist/clean versions are underrepresented. The exact target keyword is carried by the **title itself** (Amazon auto-indexes title words), so backend slots target adjacent long-tails instead of repeating it. Each slot is ≤ 50 characters (KDP's per-keyword limit).

| Slot | Keyword Phrase | Rationale |
|---|---|---|
| 1 | cat coloring book for adults stress relief | Highest-intent adult buyer phrasing; "stress relief" is not in title/subtitle |
| 2 | easy relaxing designs to color and unwind | "easy"/"unwind" capture relaxation searches |
| 3 | modern black and white line art to color | Matches the aesthetic-searcher; "modern", "black and white" not in metadata |
| 4 | kitten and cat coloring pages for teens | "kitten" (design #26) and the teen audience |
| 5 | single sided pages for markers no bleed | Marker users search this exact concern; matches the book's real structure |
| 6 | gift for cat mom cat dad cat lovers | Gift-angle long-tail with fresh phrasing |
| 7 | sophisticated grown ups coloring book | Catches "grown-ups" phrasing; sets the adult expectation without "for adults" |

**Notes:** no trademarked terms, no competitor brand names, no claims in keywords. Do **not** add "Amazon", "Kindle", "free" — KDP rejects these.

---

## 4. Categories & Browse Nodes

Choose 3 in KDP's category picker during upload (verify the exact paths the picker offers — they shift; no fake node IDs listed here):

1. **Books > Crafts, Hobbies & Home > Crafts & Hobbies > Coloring Books for Grown-Ups** — primary; the core audience
2. **Books > Crafts, Hobbies & Home > Crafts & Hobbies > Drawing** — line-art adjacency (if offered)
3. **Books > Humor & Entertainment > Activities, Crafts & Games > Activity Books** — secondary discovery path (if offered)

---

## 5. A+ Content Suggestions (Basic A+ — add after launch)

1. **Brand banner:** "Crisp Line Press — crisp black-and-white line art" with a strip of 3–4 interior designs side by side.
2. **"What's inside" image/text module:** a grid of 4–6 design thumbnails (use `05_geometric_cat_head`, `14_regal_sitting_cat`, `10_two_cats_entwined`, `36_cat_in_paper_bag`), with the one-sided-pages and 8.5×11 frame-fit callouts.
3. **"How to use / tools" module:** pencils vs. gel pens vs. markers on white paper; scrap-sheet tip for alcohol markers.
4. **Series cross-sell module:** the other Crisp Line Press titles (toddler animals, line-art journal, etc.) once ≥ 2 more are live.

---

## 6. Cover Design Specs

**Final cover: Variant D — "Ink navy & cream"** (owner's choice, finalized 2026-11-04). A flat-color design — navy and cream appear only in fields, panels and type; the artwork itself is **uncolored black line art**, so the book is still honestly a black-and-white coloring book inside.

### Cover
| Field | Value |
|---|---|
| **Cover File (PDF)** | `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover.pdf` — 68,893 bytes (68.9 kB), 1 page |
| **Cover File (PNG, 300 dpi)** | `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover.png` — 916,958 bytes (~917 kB), 5232 × 3376 px |
| **Flat wrap preview** | `/home/team/shared/launch-package/minimalist-cat-coloring-book/wrap-preview.png` — 457,597 bytes (~458 kB), 2200 × 1419 px (back + spine + front laid flat) |
| **Format** | Full-wrap PDF (back + spine + front) — KDP requires PDF for cover upload |
| **Dimensions (design)** | **17.439168" × 11.25"** — width = 17 + spine 0.189168 + 0.25 bleed; height = 11 + 0.25 |
| **Dimensions (pypdf page box)** | 1255.62 × 810 pt = **17.439167" × 11.25"** (PDF page units are 1/72"; identical to the design value to within a thousandth of an inch) |
| **Spine Width** | **0.189168"** = 84 pages × 0.002252"/page (KDP black-ink, white-paper formula) |
| **Panel layout (L→R)** | 0.125" bleed \| back trim 8.5" \| spine 0.189168" \| front trim 8.5" \| 0.125" bleed |
| **Palette ("Ink navy & cream")** | Navy field `#24405E` (front bands, spine) · Cream `#F6EFE3` (art panel, back field, type on navy) · Charcoal `#2E2A27` (body copy on cream) |
| **Front art** | `04_cat_sleeping_crescent_moon.png` — the "crescent-moon sleeper", from `/home/team/shared/assets/minimalist-cat-coloring-book/` (1024 × 1536 source, content-cropped, white-point corrected, placed on the cream panel as uncolored black line art) |
| **Provenance** | `cover.pdf` / `cover.png` are byte-identical (md5-verified) to `cover-variants/D-navy-cream.pdf` / `.png`, built by `cover-variants/make_blue.py` (palette "D") |

**Layout (as seen in wrap-preview.png)**
- **Front:** navy band across the top carrying the cream title "MINIMALIST CAT / COLORING BOOK" (tracked Helvetica-Bold) and subtitle "40 Simple & Sleek Feline Designs"; cream art panel between the bands with the sleeping cat curled on a crescent moon in **black line art**; navy band at the foot with a small cream "CRISP LINE PRESS" line.
- **Spine: deliberately blank — an unprinted navy field, no text.** This is the owner's design choice, made after reviewing the variants (a ~6.2 pt spine title was mocked up during the variant round and rejected): at 0.189" the spine is below any comfortable spine-text size, so it stays a clean navy strip.
- **Back (cream field):** navy heading "Simple lines. Sophisticated cats.", charcoal two-paragraph blurb and four bullet selling points, navy "CRISP LINE PRESS" footer; the bottom-right **barcode zone (x > 6.375", y < 1.575" from the trim corner) is left clear** for KDP's auto-placed ISBN barcode.
- No invented reviews, ratings, badges, or claims anywhere on the cover; no photographs or gradients — flat fills and line art only.

**Cover upload notes:** in KDP choose "Upload a cover you already have" → `cover.pdf`; finish size 8.5 × 11, bleed **yes**. Check the previewer shows front/spine/back alignment (the spine will look like a plain navy strip with no text — expected).

---

## 7. Pricing (all figures are **estimates** from KDP's published table)

**Source:** KDP Help, "Printing Cost & Royalty Calculation" (kdp.amazon.com/en_US/help/topic/G201834340), retrieved **2026-11-04**. Amazon's calculator at upload time is authoritative; do not treat any number here as guaranteed.

**Printing cost estimate (84 pages, black ink, white paper, Amazon.com):**
- 8.5 × 11 is a **Large Trim Size** under KDP's definition (> 6.12" wide or > 9" high) → the large-trim column applies.
- For 24–108 page books (Amazon.com), printing cost is a **flat fixed cost, no per-page charge**: Regular trim $2.30, **Large trim $2.84**.
- **Estimated printing cost: $2.84 per unit.** (The per-page rate — $0.012 regular / $0.017 large — only kicks in above 108 pages.)
- Correction vs. the toddler spec, which estimated "$2.15 + $0.012 × pages": that used the older table's regular-trim figures and mixed the two cost tiers. 8.5 × 11 books were always in the large-trim column — worth re-checking the toddler title's price, too.

**Royalty at the 60% plan:** royalty = (list × 0.60) − printing cost.

| List price | 60% of list | − printing (est. $2.84) | **Royalty/unit (est.)** |
|---|---|---|---|
| $6.99 | $4.19 | − $2.84 | **$1.35** |
| **$7.99** | $4.79 | − $2.84 | **$1.95** ← recommended |
| $8.99 | $5.39 | − $2.84 | **$2.55** |

**Recommendation: $7.99.**
- vs $6.99: **+$0.60 per unit (+44% royalty)** for one dollar of list price.
- vs $8.99: $8.99 maximizes margin but is a hard sell for a 4th title with no review base; it is a sensible step-up after early reviews accumulate.
- $6.99 (est. $1.35/unit) is the fallback penetration price — e.g. if the title has no traction after ~30 days (see §9).
- Royalty floor: with a $2.84 estimated cost, list must stay above ~$4.73 (est.) for non-negative royalty at the 60% plan.
- No sales projections are made anywhere in this spec.

---

## 8. KDP Upload Checklist & Steps

### Pre-flight — re-verified 2026-11-04 against the final files (pypdf + on-disk checks)
- [x] Interior PDF is 84 pages, 8.75" × 11.25" (630 × 810 pt; trim 8.5 × 11 + 0.125" bleed on all four sides) — pypdf
- [x] The 40 designs sit on the odd (recto) pages 5–83; every even page carries no image object (blank versos → one-sided printing); title-page motif on p. 1 — pypdf image-object scan
- [x] Only standard base fonts in the interior: Helvetica / Helvetica-Bold — pypdf font scan
- [x] Interior PDF metadata: Title "Minimalist Cat Coloring Book", Author "Crisp Line Press" — pypdf
- [x] Cover is a full wrap, 1 page, 1255.62 × 810 pt = 17.439167" × 11.25" (design geometry 17.439168" × 11.25"; spine 0.189168" = 84 × 0.002252") — pypdf
- [x] Spine is an unprinted navy field — **no spine text, deliberately** (owner's design choice; 0.189" is below comfortable spine-text size anyway) — confirmed on wrap-preview.png and in the build script (`spine_text=False`)
- [x] Cover art is `04_cat_sleeping_crescent_moon.png` as uncolored black line art on the cream panel; palette D navy `#24405E` / cream `#F6EFE3` / charcoal `#2E2A27` — confirmed on wrap-preview.png
- [x] `cover.pdf` and `cover.png` are byte-identical (md5) to the approved `cover-variants/D-navy-cream.pdf` / `.png`
- [x] Back-cover bottom-right barcode zone left clear for KDP's auto-placed ISBN barcode — build script + wrap preview
- [x] No reviews/ratings/badges/claims anywhere on cover or description — wrap preview
- [x] Source art: exactly 40 original AI-assisted PNGs in `/home/team/shared/assets/minimalist-cat-coloring-book/`, including `04_cat_sleeping_crescent_moon.png` — directory listing

Carried from the original build-time verification (interior.pdf is unchanged since and is the approved file):
- [x] Designs fit the 7.5" × 10.0" safe area, centered, aspect preserved, never cropped/stretched (placed by `assemble_interior.py`)
- [x] Line art white-point corrected / grayscale-embedded, no page numbers over art (per `assemble_interior.py`)

### Upload steps (owner performs)
1. Log in at https://kdp.amazon.com → **Create** → **Paperback**.
2. Language: English. Title / Subtitle / Author exactly as in §1.
3. ISBN: use the **free KDP-assigned ISBN** (or your own — see §11).
4. **Interior upload:** `/home/team/shared/launch-package/minimalist-cat-coloring-book/interior.pdf`
   - Print options: Black & white interior, **White paper**, Trim size **8.5 × 11 in**, Bleed: **Bleed (PDF)**.
   - Run the Launch Previewer: flip through title/copyright/tips pages, spot-check a few designs and confirm the page after each design is blank.
5. **Cover upload:** "Upload a cover you already have" → `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover.pdf` (finish size 8.5 × 11, bleed yes). Verify panel alignment in the previewer.
6. **Content:** paste the HTML description from §2; enter the 7 keyword slots from §3; pick the categories from §4; age verification: not children's content (audience is teens/adults); answer the **AI-content question** per §11.
7. **Rights & pricing:** own/all territories; royalty plan **60%**; list price **$7.99** (§7); leave Expanded Distribution off unless decided (§11).
8. Review, approve the previewer, publish. Listings typically go live within ~72 hours of approval.

---

## 9. Post-Launch Monitoring

- **First 72 hours:** confirm the listing is live and the "Look inside" preview renders designs correctly (blank backs should be visible).
- **Week 1:** check organic rank for the target keyword "minimalist cat coloring book"; note the starting position (no benchmark claims made here — record what you see).
- **Week 2:** watch for first ratings; if the listing has zero reviews, consider the standard KDP review pathways (no incentivized reviews).
- **Month 1:** add Basic A+ content (§5); evaluate price: if no traction, temporarily move to $6.99 (est. $1.35/unit royalty); if it sells steadily, test $8.99 (est. $2.55/unit).
- **Ongoing:** cross-link this title from the other Crisp Line Press listings and vice versa once A+ modules exist.

---

## 10. File Inventory

Sizes are exact on-disk bytes, verified 2026-11-04.

| File | Path | Size | Notes |
|---|---|---|---|
| Interior PDF | `/home/team/shared/launch-package/minimalist-cat-coloring-book/interior.pdf` | 2,793,106 B (~2.8 MB) | **FINAL** — 84 pages, 8.75" × 11.25" with bleed; approved, do not rebuild |
| Cover PDF | `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover.pdf` | 68,893 B (~69 kB) | **FINAL** — Variant D full wrap, 17.439167" × 11.25" |
| Cover PNG (300 dpi) | `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover.png` | 916,958 B (~917 kB) | 5232 × 3376 px — Variant D |
| Wrap preview | `/home/team/shared/launch-package/minimalist-cat-coloring-book/wrap-preview.png` | 457,597 B (~458 kB) | 2200 × 1419 px flat back+spine+front rendering of the final cover |
| Interior build script | `/home/team/shared/launch-package/minimalist-cat-coloring-book/assemble_interior.py` | 8,727 B | Reproduces interior.pdf end-to-end |
| Superseded cover script | `/home/team/shared/launch-package/minimalist-cat-coloring-book/assemble_cover.py` | 7,084 B | ⚠️ builds the OLD all-white cover — **do not run it** to regenerate the cover; it would overwrite the approved Variant D files |
| Final-cover build script | `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover-variants/make_blue.py` | 17,142 B | Built the current cover files (palettes D + E into `cover-variants/`) |
| Cover variant archive | `/home/team/shared/launch-package/minimalist-cat-coloring-book/cover-variants/` | 5 variants (A–E), PDF+PNG + comparisons + README | Owner reviewed; **D chosen** and copied to the package root. Its README documents the variant round only (incl. the rejected spine-text mock-up — the final spine is text-free) |
| Launch spec | `/home/team/shared/launch-package/minimalist-cat-coloring-book/launch-spec.md` | this file | |
| Source art (read-only) | `/home/team/shared/assets/minimalist-cat-coloring-book/` | 40 PNGs | 1024 × 1536, RGB line art |

Rebuild the interior with `python3 assemble_interior.py` (requires `reportlab`, `pillow`, `pypdf`, `pypdfium2`). To regenerate the final cover: `python3 cover-variants/make_blue.py`, then copy `cover-variants/D-navy-cream.pdf` → `cover.pdf` and `cover-variants/D-navy-cream.png` → `cover.png` in the package root — exactly how the current files were produced. **Never** run `assemble_cover.py` for the cover.

---

## 11. Notes for the Owner (only you can do these)

1. **KDP account:** the upload requires your KDP account, with bank details for royalty payments and the tax interview completed.
2. **Imprint name:** enter the imprint exactly as you want it of record — the spec assumes **"Crisp Line Press"** everywhere (cover, copyright page, metadata). If your legal imprint string differs, tell us and we'll rebuild the PDFs (one-line change).
3. **ISBN choice:** free KDP ISBN (recommended; ISBN stays usable only with KDP printing) vs. your own purchased ISBN (portable across printers). An ASIN is always assigned regardless.
4. **AI-content disclosure:** KDP's flow asks whether AI tools were used. The interior art and cover art are AI-generated and human-assembled — answer honestly per KDP's AI-content policy (you remain responsible for the rights and accuracy of AI-assisted content).
5. **Confirm pricing:** $7.99 is our recommendation (§7); the KDP calculator's live print-cost figure is authoritative — confirm the royalty it shows before approving.
6. **Categories & A+:** §4 paths are recommendations; the picker's live options win. A+ can only be added after the title is live.
7. **Expanded Distribution:** off by default in our steps; enabling it widens reach but changes costs/timing — check the calculator before enabling.
8. **Nothing was uploaded or submitted to Amazon** by the team, per the standing constraint — the owner performs the upload manually.

---

*Prepared by the Publishing Specialist — Crisp Line Press*
