# story_image.py — صورة قصة 9:16 مبنية بكسل-بكسل على الخادم (ليست لقطة شاشة)
# عربي صحيح: Raqm/HarfBuzz أساسي (متصل بلا مربعات)، Amiri احتياط لـ reshaper،
# وأسوأ حالة: bidi فقط (منفصل بلا مربعات). المحتوى: الشعار + الاسم + الأسعار فقط.
import io
import streamlit as st
import gold_service as g

WHITE=(252,252,251); INK=(24,24,27); INK2=(82,82,91); MUTED=(113,113,122)
LINE=(228,228,231); DOT=(233,233,233); FAINT=(196,196,201)
_UA = {"User-Agent": "Mozilla/5.0 (compatible; SiloraGold/1.0)"}
_MAGIC = (b'\x00\x01\x00\x00', b'true', b'OTTO', b'ttcf')
_LOG = []
_RAQM = False
_TJ = {}; _PJ = None; _AM = None

def _fetch(urls):
    import requests
    for u in urls:
        try:
            r = requests.get(u, headers=_UA, timeout=30, allow_redirects=True)
            _LOG.append((u.split("/")[-1], r.status_code))
            r.raise_for_status()
            c = r.content
            if len(c) > 4000 and c[:4] in _MAGIC:
                return c
            _LOG.append((u.split("/")[-1], "bad-magic"))
        except Exception as e:
            _LOG.append((u.split("/")[-1], f"{type(e).__name__}"))
    return None

def _tj_urls(fn):
    return [f"https://raw.githubusercontent.com/google/fonts/main/ofl/tajawal/{fn}",
            f"https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/tajawal/{fn}"]
def _pj_urls(fn):
    return [f"https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/plusjakartasans/static/{fn}",
            f"https://raw.githubusercontent.com/google/fonts/main/ofl/plusjakartasans/static/{fn}"]
def _am_urls(fn):
    return [f"https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/amiri/{fn}",
            f"https://raw.githubusercontent.com/google/fonts/main/ofl/amiri/{fn}",
            f"https://cdn.jsdelivr.net/gh/aliftype/amiri@master/{fn}"]

@st.cache_resource
def _load():
    from PIL import ImageFont, features
    global _RAQM, _TJ, _PJ, _AM, _LOG
    _LOG = []
    try:
        _RAQM = bool(features.check('raqm'))
    except Exception:
        _RAQM = False
    for w, fn in [('black','Tajawal-Black.ttf'),('bold','Tajawal-Bold.ttf'),
                  ('medium','Tajawal-Medium.ttf'),('regular','Tajawal-Regular.ttf')]:
        b = _fetch(_tj_urls(fn))
        if b: _TJ[w] = b
    if not _TJ.get('bold'):
        raise RuntimeError("فشل تحميل الخط الأساسي. سجل المحاولات: " + str(_LOG))
    _TJ.setdefault('black', _TJ['bold']); _TJ.setdefault('medium', _TJ['bold']); _TJ.setdefault('regular', _TJ['bold'])
    pj_eb = _fetch(_pj_urls('PlusJakartaSans-ExtraBold.ttf')) or _fetch(_pj_urls('PlusJakartaSans-Bold.ttf'))
    pj_b  = _fetch(_pj_urls('PlusJakartaSans-Bold.ttf'))
    pj_m  = _fetch(_pj_urls('PlusJakartaSans-Medium.ttf')) or pj_b or pj_eb
    if pj_eb: _PJ = {'eb': pj_eb, 'b': pj_b or pj_eb, 'm': pj_m or pj_eb}
    am_b = _fetch(_am_urls('Amiri-Bold.ttf')); am_r = _fetch(_am_urls('Amiri-Regular.ttf'))
    if am_b and am_r: _AM = {'bold': am_b, 'regular': am_r}
    return True

def _tr(b, s):
    from PIL import ImageFont
    return ImageFont.truetype(io.BytesIO(b), s)
def tj(w, s): return _tr(_TJ[w], s)
def lt(s, w='eb'):
    if _PJ: return _tr(_PJ[w], s)
    return tj({'eb':'black','b':'bold','m':'medium'}.get(w,'bold'), s)
def am(w, s): return _tr(_AM[w], s)

def _reshape(t):
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        return get_display(arabic_reshaper.reshape(str(t)))
    except Exception:
        return str(t)
def _bidi_only(t):
    try:
        from bidi.algorithm import get_display
        return get_display(str(t))
    except Exception:
        return str(t)

def _aw(f, t):
    return f.getlength(t, direction='rtl', language='ar') if _RAQM else f.getlength(_reshape(t))

def _ar(d, t, x, y, size, fill, align='right', weight='bold'):
    if _RAQM:
        f = tj(weight if weight in _TJ else 'bold', size)
        a = {'right':'r','center':'m','left':'l'}[align] + 't'
        d.text((x, y), str(t), font=f, fill=fill, anchor=a, direction='rtl', language='ar')
    else:
        if _AM:
            f = am('bold' if weight in ('black','bold') else 'regular', size); s = _reshape(t)
        else:
            f = tj(weight if weight in _TJ else 'bold', size); s = _bidi_only(t)
        w = f.getlength(s)
        xx = (x - w) if align == 'right' else (x - w/2) if align == 'center' else x
        d.text((xx, y), s, font=f, fill=fill)

def _lt(d, t, x, y, size, fill, align='center', weight='eb'):
    f = lt(size, weight); a = {'right':'r','center':'m','left':'l'}[align] + 't'
    d.text((x, y), str(t), font=f, fill=fill, anchor=a)

def _logo(d, x0, y0, sz):
    d.rounded_rectangle([x0, y0, x0+sz, y0+sz], radius=int(sz*0.24), fill=INK)
    cx, cy = x0+sz/2, y0+sz/2; s = sz*0.30; c = (255,255,255)
    top = cy-s*0.62; gline = cy-s*0.08; bot = cy+s*0.98
    l = cx-s; r = cx+s; tl = cx-s*0.52; tr = cx+s*0.52
    d.line([(l,gline),(tl,top),(tr,top),(r,gline)], fill=c, width=4, joint='curve')
    d.line([(l,gline),(r,gline)], fill=c, width=4)
    d.line([(l,gline),(cx,bot),(r,gline)], fill=c, width=4)
    d.line([(tl,top),(cx,bot)], fill=c, width=2); d.line([(tr,top),(cx,bot)], fill=c, width=2)

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

    base = Image.new('RGB', (W, H), WHITE); d = ImageDraw.Draw(base)
    for yy in range(18, H, 30):
        for xx in range(18, W, 30):
            d.ellipse([xx, yy, xx+2, yy+2], fill=DOT)

    hero = (M, 322, W-M, 902)
    cards = {"عيار 24": (W-M-446, 1036), "عيار 22": (M, 1036),
             "عيار 21": (W-M-446, 1372), "عيار 18": (M, 1372)}
    CW, CH = 446, 308

    amb = Image.new('RGBA', (W, H), (0,0,0,0))
    ImageDraw.Draw(amb).ellipse([W//2-460, -320, W//2+460, 540], fill=(24,24,27,12))
    base = Image.alpha_composite(base.convert('RGBA'), amb.filter(ImageFilter.GaussianBlur(40))).convert('RGB')
    sh = Image.new('RGBA', (W, H), (0,0,0,0)); sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([hero[0], hero[1]+20, hero[2], hero[3]+20], radius=40, fill=(18,18,22,46))
    for k,(cx0,cy0) in cards.items():
        sd.rounded_rectangle([cx0, cy0+16, cx0+CW, cy0+CH+16], radius=32, fill=(18,18,22,30))
    base = Image.alpha_composite(base.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(26))).convert('RGB')
    d = ImageDraw.Draw(base)

    LS = 126; lx = W-M-LS; ly = 92
    _logo(d, lx, ly, LS)
    _ar(d, "سيلورا جولد", lx-32, ly+10, 66, INK, 'right', 'bold')
    _lt(d, "GOLD  DESK", lx-32, ly+92, 23, MUTED, 'right', 'b')
    d.line([(M, 262), (W-M, 262)], fill=LINE, width=2)

    x0,y0,x1,y1 = hero; cx = W//2
    d.rounded_rectangle([x0,y0,x1,y1], radius=40, fill=WHITE, outline=INK, width=3)
    _ar(d, "سعر الأونصة العالمية", cx, y0+58, 37, MUTED, 'center', 'regular')
    big = f2(ounce_usd); fbig = lt(182, 'eb')
    _lt(d, big, cx, y0+128, 182, INK, 'center', 'eb')
    _lt(d, "$", cx-fbig.getlength(big)/2-22, y0+186, 104, INK2, 'right', 'eb')
    d.line([(cx-92, y0+352), (cx+92, y0+352)], fill=LINE, width=2)
    sar = f0(ounce_sar); fsar = lt(76, 'eb')
    _lt(d, sar, cx, y0+386, 76, INK, 'center', 'eb')
    _ar(d, "ر.س", cx+fsar.getlength(sar)/2+18, y0+414, 31, INK2, 'left', 'bold')

    ft = tj('bold', 44) if _RAQM else tj('bold', 44); wt = _aw(ft, "أسعار الجرام")
    _ar(d, "أسعار الجرام", W-M, 972, 44, INK, 'right', 'bold')
    d.line([(M, 1002), (W-M-wt-26, 1002)], fill=LINE, width=2)

    for k,(cx0,cy0) in cards.items():
        feat = (k == "عيار 24"); rx0,ry0,rx1,ry1 = cx0,cy0,cx0+CW,cy0+CH; pad = 44
        if feat: d.rounded_rectangle([rx0,ry0,rx1,ry1], radius=32, fill=WHITE, outline=INK, width=3)
        else:    d.rounded_rectangle([rx0,ry0,rx1,ry1], radius=32, fill=WHITE, outline=LINE, width=2)
        re = rx1-pad
        _ar(d, k, re, ry0+42, 42, INK if feat else INK2, 'right', 'bold')
        val = f2(grams[k]); fv = lt(80, 'eb')
        _lt(d, val, re, ry0+112, 80, INK, 'right', 'eb')
        _ar(d, "ر.س", re-fv.getlength(val)-16, ry0+156, 29, MUTED, 'right', 'regular')
        _lt(d, f2(grams_usd[k]) + "   USD", re, ry0+226, 33, MUTED, 'right', 'b')

    d.line([(W//2-44, 1752), (W//2+44, 1752)], fill=LINE, width=2)
    _lt(d, "SILORA  GOLD", W//2, 1782, 22, FAINT, 'center', 'b')

    buf = io.BytesIO(); base.save(buf, 'PNG'); return buf.getvalue()
