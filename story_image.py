# story_image.py — بناء صورة قصة 9:16 (1080x1920) على الخادم عبر Pillow
# صورة مبنية من الصفر (لا التقاط). عربية صحيحة عبر reshaper+bidi. الخطوط تُحمّل على الخادم.
import io
from datetime import datetime
import streamlit as st
import gold_service as g

_FONTS = None
_AR_MONTHS = ["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو",
              "أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"]

WHITE=(255,255,255); INK=(24,24,27); INK2=(82,82,91); MUTED=(113,113,122)
LINE=(228,228,231); LINE2=(245,245,245); DOT=(232,232,232)

def f2(v): return "—" if v is None else f"{v:,.2f}"
def f0(v): return "—" if v is None else f"{v:,.0f}"

def ar(text):
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        return get_display(arabic_reshaper.reshape(str(text)))
    except Exception:
        return str(text)

def date_ar():
    n = datetime.now()
    return f"{n.day} {_AR_MONTHS[n.month-1]} {n.year}"

@st.cache_resource
def _load_fonts():
    import requests
    base = "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/tajawal/"
    names = {'black':'Tajawal-Black.ttf','bold':'Tajawal-Bold.ttf',
             'medium':'Tajawal-Medium.ttf','regular':'Tajawal-Regular.ttf'}
    out = {}
    for k, fn in names.items():
        try:
            r = requests.get(base + fn, timeout=20); r.raise_for_status(); out[k] = r.content
        except Exception:
            out[k] = None
    return out

def _font(weight, size):
    from PIL import ImageFont
    b = _FONTS.get(weight) or _FONTS.get('bold')
    if b:
        try: return ImageFont.truetype(io.BytesIO(b), size)
        except Exception: pass
    return ImageFont.load_default()

def _w(d, t, f):
    b = d.textbbox((0, 0), t, font=f); return b[2] - b[0]
def rtext(d, t, x, y, f, fill): d.text((x - _w(d, t, f), y), t, font=f, fill=fill)
def ltext(d, t, x, y, f, fill): d.text((x, y), t, font=f, fill=fill)
def ctext(d, t, x, y, f, fill): d.text((x - _w(d, t, f) / 2, y), t, font=f, fill=fill)

def _diamond(d, cx, cy):
    pts = [(cx-26, cy-8), (cx-14, cy-22), (cx+14, cy-22), (cx+26, cy-8), (cx, cy+28)]
    d.polygon(pts, outline=(255,255,255), width=4)
    d.line([(cx-26, cy-8), (cx+26, cy-8)], fill=(255,255,255), width=3)
    d.line([(cx-14, cy-22), (cx, cy+28)], fill=(255,255,255), width=2)
    d.line([(cx+14, cy-22), (cx, cy+28)], fill=(255,255,255), width=2)

def build(price_24, upd):
    global _FONTS
    from PIL import Image, ImageDraw, ImageFilter
    if _FONTS is None:
        _FONTS = _load_fonts()
    if not any(_FONTS.values()):
        raise RuntimeError("تعذّر تحميل الخطوط على الخادم")

    W, H, M = 1080, 1920, 72
    F = _font

    base = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(base)
    for yy in range(20, H, 30):
        for xx in range(20, W, 30):
            d.ellipse([xx, yy, xx+2, yy+2], fill=DOT)

    ounce_sar = price_24 * g.OUNCE_TO_GRAM
    ounce_usd = ounce_sar / g.USD_TO_SAR
    grams = {k: g.gram_price(price_24, k) for k in g.KARAT_FACTORS}
    grams_usd = {k: grams[k] / g.USD_TO_SAR for k in grams}

    hero_rect = (M, 360, W-M, 900)
    krects = [(554,1040,1008,1330), (72,1040,526,1330), (554,1358,1008,1648), (72,1358,526,1648)]

    overlay = Image.new('RGBA', (W, H), (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([W//2-420, -300, W//2+420, 520], fill=(24,24,27,14))
    for r in [hero_rect] + krects:
        od.rounded_rectangle([r[0], r[1]+16, r[2], r[3]+16], radius=34, fill=(15,15,18,44))
    overlay = overlay.filter(ImageFilter.GaussianBlur(24))
    base = Image.alpha_composite(base.convert('RGBA'), overlay).convert('RGB')
    d = ImageDraw.Draw(base)

    # الهوية
    lx, ly = W-M-104, 92
    d.rounded_rectangle([lx, ly, lx+104, ly+104], radius=26, fill=INK)
    _diamond(d, lx+52, ly+52)
    name_right = lx - 30
    rtext(d, ar("سيلورا جولد"), name_right, ly+6, F('bold', 62), INK)
    rtext(d, "GOLD DESK", name_right, ly+80, F('bold', 24), MUTED)
    f_live = F('bold', 26); live_txt = ar("مباشر"); lw = _w(d, live_txt, f_live); badge_w = lw + 70; bx, by = M, ly+30
    d.rounded_rectangle([bx, by, bx+badge_w, by+52], radius=26, fill=LINE2, outline=LINE, width=2)
    d.ellipse([bx+22, by+18, bx+38, by+34], fill=(22,163,74))
    ltext(d, live_txt, bx+50, by+8, f_live, INK2)

    d.line([(M, 250), (W-M, 250)], fill=LINE, width=2)
    rtext(d, ar("لوحة أسعار الذهب المباشرة"), W-M, 296, F('bold', 32), MUTED)

    # بطاقة الأونصة
    x0, y0, x1, y1 = hero_rect
    d.rounded_rectangle([x0, y0, x1, y1], radius=36, fill=WHITE, outline=INK, width=3)
    ctext(d, ar("سعر الأونصة العالمي"), W//2, y0+52, F('bold', 34), MUTED)
    ctext(d, f2(ounce_usd), W//2, y0+110, F('black', 150), INK)
    ctext(d, ar("دولار أمريكي / أونصة"), W//2, y0+300, F('medium', 32), INK2)
    d.line([(W//2-90, y0+360), (W//2+90, y0+360)], fill=LINE, width=2)
    ctext(d, f0(ounce_sar), W//2, y0+388, F('bold', 64), INK)
    ctext(d, ar("ريال سعودي / أونصة"), W//2, y0+470, F('medium', 30), MUTED)

    # عنوان الأعيرة
    rtext(d, ar("أسعار الجرام"), W-M, 980, F('bold', 40), INK)
    tw = _w(d, ar("أسعار الجرام"), F('bold', 40))
    d.line([(M, 1002), (W-M-tw-24, 1002)], fill=LINE, width=2)

    # بطاقات الأعيرة
    order = ["عيار 24", "عيار 22", "عيار 21", "عيار 18"]
    rects = {"عيار 24": krects[0], "عيار 22": krects[1], "عيار 21": krects[2], "عيار 18": krects[3]}
    for k in order:
        cx0, cy0, cx1, cy1 = rects[k]; pad = 40; feat = (k == "عيار 24")
        if feat:
            d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=30, fill=WHITE, outline=INK, width=3)
        else:
            d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=30, fill=WHITE, outline=LINE, width=2)
        rtext(d, ar(k), cx1-pad, cy0+34, F('bold', 40), INK if feat else INK2)
        f_val = F('black', 72)
        rtext(d, f2(grams[k]), cx1-pad, cy0+104, f_val, INK)
        vw = _w(d, f2(grams[k]), f_val)
        f_cur = F('bold', 26); cur = ar("ر.س"); cw = _w(d, cur, f_cur)
        bbx = cx1-pad-vw-14-cw-16
        d.rounded_rectangle([bbx, cy0+150, bbx+cw+16, cy0+188], radius=8, fill=LINE2)
        ltext(d, cur, bbx+8, cy0+152, f_cur, INK2)
        rtext(d, f2(grams_usd[k]) + "  USD", cx1-pad, cy0+214, F('bold', 32), MUTED)

    # التذييل
    d.line([(M, 1720), (W-M, 1720)], fill=LINE, width=2)
    f_foot = F('medium', 26)
    ltext(d, "gold-api.com", M, 1756, f_foot, INK2)
    ar_upd = ar("آخر تحديث"); wu = _w(d, ar_upd, f_foot)
    rtext(d, ar_upd, W-M, 1756, f_foot, MUTED)
    rtext(d, (upd or "—"), W-M-wu-12, 1756, f_foot, INK2)
    ctext(d, ar("© 2026 سيلورا جولد · أسعار استرشادية وفق السوق العالمي"), W//2, 1820, F('medium', 24), MUTED)
    ctext(d, ar(date_ar()), W//2, 1862, F('medium', 24), MUTED)

    buf = io.BytesIO(); base.save(buf, 'PNG'); return buf.getvalue()
