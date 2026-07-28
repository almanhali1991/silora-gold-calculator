# story_image.py — صورة قصة 9:16 مبنية بكسل-بكسل على الخادم (ليست لقطة شاشة)
# عربية صحيحة عبر Raqm/HarfBuzz داخل Pillow (احتياط: reshaper + Noto Naskh).
# المحتوى: الشعار + الاسم + الأسعار فقط. لا معلومات إضافية.
import io
import streamlit as st
import gold_service as g

# ---- ألوان ----
WHITE=(252,252,251); INK=(24,24,27); INK2=(82,82,91); MUTED=(113,113,122)
LINE=(228,228,231); DOT=(233,233,233); FAINT=(196,196,201)

_RAQM = None
_AR_B = _AR_R = _LT_EB = _LT_B = _LT_M = None

def _feat_raqm():
    try:
        from PIL import features
        return bool(features.check('raqm'))
    except Exception:
        return False

def _get(urls):
    import requests
    for u in urls:
        try:
            r = requests.get(u, timeout=25); r.raise_for_status()
            if len(r.content) > 4000:
                return r.content
        except Exception:
            continue
    return None

@st.cache_resource
def _load():
    from PIL import ImageFont
    global _RAQM, _AR_B, _AR_R, _LT_EB, _LT_B, _LT_M
    _RAQM = _feat_raqm()
    ar_b = _get([
        "https://github.com/notofonts/arabic/raw/main/fonts/NotoNaskhArabic/unhinted/ttf/NotoNaskhArabic-Bold.ttf",
        "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/amiri/Amiri-Bold.ttf",
        "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/tajawal/Tajawal-Bold.ttf"])
    ar_r = _get([
        "https://github.com/notofonts/arabic/raw/main/fonts/NotoNaskhArabic/unhinted/ttf/NotoNaskhArabic-Regular.ttf",
        "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/amiri/Amiri-Regular.ttf",
        "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/tajawal/Tajawal-Regular.ttf"])
    lt_eb = _get(["https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/plusjakartasans/static/PlusJakartaSans-ExtraBold.ttf",
                  "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/plusjakartasans/static/PlusJakartaSans-Bold.ttf"])
    lt_b  = _get(["https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/plusjakartasans/static/PlusJakartaSans-Bold.ttf"])
    lt_m  = _get(["https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/plusjakartasans/static/PlusJakartaSans-Medium.ttf",
                  "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/plusjakartasans/static/PlusJakartaSans-Regular.ttf"])
    if not (ar_b and ar_r and lt_eb):
        raise RuntimeError("تعذّر تحميل الخطوط على الخادم")
    _AR_B = ar_b; _AR_R = ar_r; _LT_EB = lt_eb; _LT_B = lt_b or lt_eb; _LT_M = lt_m or lt_b or lt_eb
    return True

def arB(s):
    from PIL import ImageFont
    return ImageFont.truetype(io.BytesIO(_AR_B), s)
def arR(s):
    from PIL import ImageFont
    return ImageFont.truetype(io.BytesIO(_AR_R), s)
def ltEB(s):
    from PIL import ImageFont
    return ImageFont.truetype(io.BytesIO(_LT_EB), s)
def ltB(s):
    from PIL import ImageFont
    return ImageFont.truetype(io.BytesIO(_LT_B), s)
def ltM(s):
    from PIL import ImageFont
    return ImageFont.truetype(io.BytesIO(_LT_M), s)

def _reshape(t):
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        return get_display(arabic_reshaper.reshape(str(t)))
    except Exception:
        return str(t)

def _aw(f, t):
    return f.getlength(t, direction='rtl', language='ar') if _RAQM else f.getlength(_reshape(t))

def _ar(d, t, x, y, f, fill, align='right', v='t'):
    s = t if _RAQM else _reshape(t)
    a = {'right':'r','center':'m','left':'l'}[align] + v
    kw = dict(font=f, fill=fill, anchor=a)
    if _RAQM:
        kw.update(direction='rtl', language='ar')
    d.text((x, y), s, **kw)

def _lt(d, t, x, y, f, fill, align='center', v='t'):
    a = {'right':'r','center':'m','left':'l'}[align] + v
    d.text((x, y), str(t), font=f, fill=fill, anchor=a)

def _logo(d, x0, y0, sz):
    d.rounded_rectangle([x0, y0, x0+sz, y0+sz], radius=int(sz*0.24), fill=INK)
    cx, cy = x0+sz/2, y0+sz/2; s = sz*0.30; c = (255,255,255)
    top = cy-s*0.62; g = cy-s*0.08; bot = cy+s*0.98
    l = cx-s; r = cx+s; tl = cx-s*0.52; tr = cx+s*0.52
    d.line([(l,g),(tl,top),(tr,top),(r,g)], fill=c, width=4, joint='curve')
    d.line([(l,g),(r,g)], fill=c, width=4)
    d.line([(l,g),(cx,bot),(r,g)], fill=c, width=4)
    d.line([(tl,top),(cx,bot)], fill=c, width=2)
    d.line([(tr,top),(cx,bot)], fill=c, width=2)
    d.line([(tl,top),(l,g)], fill=c, width=2)
    d.line([(tr,top),(r,g)], fill=c, width=2)

def build(price_24):
    from PIL import Image, ImageDraw, ImageFilter
    _load()
    f2 = lambda v: "—" if v is None else f"{v:,.2f}"
    f0 = lambda v: "—" if v is None else f"{v:,.0f}"

    W, H, M = 1080, 1920, 84
    ounce_sar = price_24 * g.OUNCE_TO_GRAM
    ounce_usd = ounce_sar / g.USD_TO_SAR
    grams = {k: g.gram_price(price_24, k) for k in g.KARAT_FACTORS}
    grams_usd = {k: grams[k] / g.USD_TO_SAR for k in grams}

    base = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(base)
    for yy in range(18, H, 30):
        for xx in range(18, W, 30):
            d.ellipse([xx, yy, xx+2, yy+2], fill=DOT)

    hero = (M, 322, W-M, 902)
    cards = {"عيار 24": (W-M-446, 1036), "عيار 22": (M, 1036),
             "عيار 21": (W-M-446, 1372), "عيار 18": (M, 1372)}
    CW, CH = 446, 308

    amb = Image.new('RGBA', (W, H), (0,0,0,0))
    ImageDraw.Draw(amb).ellipse([W//2-460, -320, W//2+460, 540], fill=(24,24,27,12))
    amb = amb.filter(ImageFilter.GaussianBlur(40))
    base = Image.alpha_composite(base.convert('RGBA'), amb).convert('RGB')

    sh = Image.new('RGBA', (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([hero[0], hero[1]+20, hero[2], hero[3]+20], radius=40, fill=(18,18,22,46))
    for k,(cx0,cy0) in cards.items():
        sd.rounded_rectangle([cx0, cy0+16, cx0+CW, cy0+CH+16], radius=32, fill=(18,18,22,30))
    sh = sh.filter(ImageFilter.GaussianBlur(26))
    base = Image.alpha_composite(base.convert('RGBA'), sh).convert('RGB')
    d = ImageDraw.Draw(base)

    # ---- الترويسة ----
    LS = 126; lx = W-M-LS; ly = 92
    _logo(d, lx, ly, LS)
    nx = lx-32
    _ar(d, "سيلورا جولد", nx, ly+10, arB(66), INK, 'right')
    _lt(d, "GOLD  DESK", nx, ly+92, ltB(23), MUTED, 'right')
    d.line([(M, 262), (W-M, 262)], fill=LINE, width=2)

    # ---- بطاقة الأونصة ----
    x0,y0,x1,y1 = hero
    d.rounded_rectangle([x0,y0,x1,y1], radius=40, fill=WHITE, outline=INK, width=3)
    cx = W//2
    _ar(d, "سعر الأونصة العالمية", cx, y0+58, arR(37), MUTED, 'center')
    big = f2(ounce_usd); fbig = ltEB(182)
    _lt(d, big, cx, y0+128, fbig, INK, 'center')
    wb = fbig.getlength(big)
    _lt(d, "$", cx-wb/2-22, y0+186, ltEB(104), INK2, 'right')
    d.line([(cx-92, y0+352), (cx+92, y0+352)], fill=LINE, width=2)
    sar = f0(ounce_sar); fsar = ltEB(76)
    _lt(d, sar, cx, y0+386, fsar, INK, 'center')
    ws = fsar.getlength(sar)
    _ar(d, "ر.س", cx+ws/2+18, y0+414, arB(31), INK2, 'left')

    # ---- عنوان الأعيرة ----
    ft = arB(44); wt = _aw(ft, "أسعار الجرام")
    _ar(d, "أسعار الجرام", W-M, 972, ft, INK, 'right')
    d.line([(M, 1002), (W-M-wt-26, 1002)], fill=LINE, width=2)

    # ---- بطاقات الأعيرة ----
    for k,(cx0,cy0) in cards.items():
        feat = (k == "عيار 24"); rx0,ry0,rx1,ry1 = cx0,cy0,cx0+CW,cy0+CH; pad = 44
        if feat:
            d.rounded_rectangle([rx0,ry0,rx1,ry1], radius=32, fill=WHITE, outline=INK, width=3)
        else:
            d.rounded_rectangle([rx0,ry0,rx1,ry1], radius=32, fill=WHITE, outline=LINE, width=2)
        re = rx1-pad
        _ar(d, k, re, ry0+42, arB(42), INK if feat else INK2, 'right')
        val = f2(grams[k]); fv = ltEB(80)
        _lt(d, val, re, ry0+112, fv, INK, 'right')
        wv = fv.getlength(val)
        _ar(d, "ر.س", re-wv-16, ry0+156, arR(29), MUTED, 'right')
        _lt(d, f2(grams_usd[k]) + "   USD", re, ry0+226, ltB(33), MUTED, 'right')

    # ---- ختم سفلي خفيف ----
    d.line([(W//2-44, 1752), (W//2+44, 1752)], fill=LINE, width=2)
    _lt(d, "SILORA  GOLD", W//2, 1782, ltB(22), FAINT, 'center')

    buf = io.BytesIO(); base.save(buf, 'PNG'); return buf.getvalue()
