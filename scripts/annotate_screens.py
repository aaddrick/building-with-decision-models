#!/usr/bin/env python3
"""Annotate the README walkthrough screenshots.

The raw captures hold account details, and the API key ones a live key, so they
never enter the repo. Capture them yourself, then run:

    python3 scripts/annotate_screens.py api-key /path/to/raw-dir
    python3 scripts/annotate_screens.py plugin-marketplace /path/to/raw-dir

api-key: 1512x807 captures of console.typesafe.ai, named 01-home.jpg,
02-keys.jpg, 03-name.jpg, 04-created.jpg.
plugin-marketplace: captures of the Plugins page with a dark theme. Steps 1-2
are 1510x812 captures of claude.ai/customize/plugins named 01-add-menu.jpg and
02-chooser.jpg. Steps 3-5 are tighter crops of the dialog and the Discover list:
03-repo.png (1286x612), 04-listed.png and 05-added.png (1912x612).
Each flow writes .github/assets/<flow>/step-1.png onward. Pass step numbers
after the folder to redo only those steps, e.g. `plugin-marketplace raw 3 4 5`.

Every image gets the same treatment: blur the account details (and, for API
keys, every existing key row and the new key's value), then draw an amber
highlight box, a numbered badge, and an arrow with a label on the one control
the step is about. Coordinates are in the capture frame.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "assets" / "fonts"
ASSETS = ROOT / ".github" / "assets"

AMBER = (0xD9, 0x8B, 0x0B)
INK = (0x1B, 0x19, 0x16)
WHITE = (0xFF, 0xFF, 0xFF)

ACCOUNT = (0, 740, 265, 807)            # avatar, name, org
ROWS = (298, 162, 1480, 436)            # every key row: names, prefixes, creator
SIDEBAR = (0, 300, 288, 812)            # claude.ai: projects, pins, chat titles, account


def font(size, weight="SemiBold"):
    return ImageFont.truetype(str(FONTS / f"SairaCondensed-{weight}.ttf"), size)


def blur(img, box, radius=14):
    region = img.crop(box).filter(ImageFilter.GaussianBlur(radius))
    img.paste(region, box[:2])


def mask_key(img, box):
    d = ImageDraw.Draw(img)
    d.rectangle(box, fill=(0xF4, 0xF4, 0xF2), outline=(0xE2, 0xE2, 0xDE))
    mono = ImageFont.truetype(str(FONTS / "IBMPlexMono-Medium.ttf"), 18)
    d.text((box[0] + 14, box[1] + (box[3] - box[1]) // 2 - 12), "apikey_••••••••••••••••••••",
           font=mono, fill=(0x55, 0x55, 0x55))


def highlight(img, box, step, label, arrow_from, s=1.0):
    """Amber box around the target, a numbered badge, and an arrow with a label.

    s scales the strokes and text, so a wider capture gets marks of the same
    size relative to the page once it is resized for the README.
    """
    d = ImageDraw.Draw(img)
    pad = round(6 * s)
    x0, y0, x1, y1 = box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad
    for w in range(round(4 * s)):
        d.rounded_rectangle([x0 - w, y0 - w, x1 + w, y1 + w], radius=round(10 * s), outline=AMBER)

    # arrow from the label toward the nearest edge midpoint of the box
    ax, ay = arrow_from
    tx = min(max(ax, x0), x1)
    ty = min(max(ay, y0), y1)
    d.line([(ax, ay), (tx, ty)], fill=AMBER, width=round(5 * s))
    import math
    ang = math.atan2(ty - ay, tx - ax)
    head = 18 * s
    for sign in (-1, 1):
        hx = tx - head * math.cos(ang + sign * 0.45)
        hy = ty - head * math.sin(ang + sign * 0.45)
        d.line([(tx, ty), (hx, hy)], fill=AMBER, width=round(5 * s))

    # label pill with the step number
    f = font(round(26 * s))
    text_w = d.textlength(label, font=f)
    r = round(20 * s)
    pill_w = int(text_w + 2 * r + 34 * s)
    px, py = ax - pill_w // 2, ay - r - 2 * s
    d.rounded_rectangle([px, py, px + pill_w, py + 2 * r + 4 * s], radius=r + 2 * s, fill=INK)
    cx, cy = px + r + 4 * s, py + r + 2 * s
    d.ellipse([cx - r + 3 * s, cy - r + 3 * s, cx + r - 3 * s, cy + r - 3 * s], fill=AMBER)
    nf = font(round(24 * s), "Bold")
    n = str(step)
    d.text((cx - d.textlength(n, font=nf) / 2, cy - 16 * s), n, font=nf, fill=INK)
    d.text((cx + r + 8 * s, cy - 18 * s), label, font=f, fill=WHITE)


# flow: (output width, steps). Each step is raw file, capture size, blurs,
# dialog kept sharp, key mask, target box, label, label position, extra rows of
# background added below the capture to make room for the label, and a mark
# scale for a capture zoomed in further than the rest.
FLOWS = {
    "api-key": (1210, [
        ("01-home.jpg",    (1512, 807), [ACCOUNT],       None,                  None,                 (8, 182, 256, 214),   "Open API Keys",            (132, 420), 0, 1),
        ("02-keys.jpg",    (1512, 807), [ACCOUNT, ROWS], None,                  None,                 (1361, 14, 1479, 47), "Click Create key",         (1180, 560), 0, 1),
        ("03-name.jpg",    (1512, 807), [ACCOUNT, ROWS], (492, 281, 1021, 527), None,                 (517, 410, 996, 502), "Name it, then Create key", (756, 640), 0, 1),
        ("04-created.jpg", (1512, 807), [ACCOUNT, ROWS], (492, 266, 1021, 542), (517, 354, 914, 434), (922, 378, 996, 410), "Copy it now: shown once",  (1180, 640), 0, 1),
    ]),
    "plugin-marketplace": (1208, [
        ("01-add-menu.jpg", (1510, 812), [SIDEBAR], None, None, (1206, 159, 1388, 193), "Add, then Add marketplace", (1100, 330), 0, 1),
        ("02-chooser.jpg",  (1510, 812), [SIDEBAR], None, None, (410, 410, 1102, 479),  "Add from a repository",     (755, 660), 0, 1),
        ("03-repo.png",     (1286, 612), [],        None, None, (56, 352, 1231, 563),   "Enter the repo, then Sync", (643, 690), 140, 1.7),
        ("04-listed.png",   (1912, 612), [],        None, None, (1509, 220, 1597, 274), "Add the plugin",            (1290, 430), 0, 1),
        ("05-added.png",    (1912, 612), [],        None, None, (1445, 220, 1597, 274), "Added and ready",           (1230, 430), 0, 1),
    ]),
}

REFERENCE_WIDTH = 1510  # the capture width the mark sizes were tuned on


def main(flow: str, raw_dir: Path, only: set[int]) -> None:
    out_w, steps = FLOWS[flow]
    out_dir = ASSETS / flow
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, (name, size, blurs, dialog, key_box, target, label, label_at, extra, mark) in enumerate(steps, start=1):
        if only and i not in only:
            continue
        img = Image.open(raw_dir / name).convert("RGB")
        if img.size != size:
            sys.exit(f"{name}: expected {size[0]}x{size[1]}, got {img.size}")
        sharp = img.crop(dialog) if dialog else None
        for box in blurs:
            blur(img, box)
        if sharp:
            img.paste(sharp, dialog[:2])     # the dialog is the subject; keep it readable
        if key_box:
            mask_key(img, key_box)
        if extra:
            grown = Image.new("RGB", (img.width, img.height + extra), img.getpixel((2, img.height - 2)))
            grown.paste(img, (0, 0))
            img = grown
        highlight(img, target, i, label, label_at, mark * img.width / REFERENCE_WIDTH)
        out = out_dir / f"step-{i}.png"
        img.resize((out_w, round(img.height * out_w / img.width)), Image.LANCZOS).save(out, optimize=True)
        print(f"wrote {out}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in FLOWS:
        sys.exit(__doc__)
    main(sys.argv[1], Path(sys.argv[2]), {int(n) for n in sys.argv[3:]})
