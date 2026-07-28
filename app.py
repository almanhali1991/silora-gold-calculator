# app.py — سيلورا جولد | لوحة أسعار نقية (فاتحة، RTL، متجاوبة، بأيقونات SVG ورسم أعمدة حي)
import streamlit as st
import theme
import gold_service as g

st.set_page_config(page_title="سيلورا جولد", page_icon="💎", layout="wide", initial_sidebar_state="collapsed")
theme.inject()

price_24, upd, errors = g.fetch_gold()

# ===== أدوات تنسيق آمنة (لا رموز عملة ملتصقة بالأرقام في نص RTL) =====
def f2(v): return "—" if v is None else f"{v:,.2f}"
def f0(v): return "—" if v is None else f"{v:,.0f}"

OUNCE_SAR = price_24 * g.OUNCE_TO_GRAM if price_24 else None
OUNCE_USD = OUNCE_SAR / g.USD_TO_SAR if OUNCE_SAR else None
GRAM      = {k: (g.gram_price(price_24, k) if price_24 else None) for k in g.KARAT_FACTORS}
GRAM_USD  = {k: (GRAM[k] / g.USD_TO_SAR if GRAM[k] else None) for k in GRAM}

# ===== أيقونات SVG خطية متسقة (بدون رموز نصية مكسورة) =====
IC = {
 "usd": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 6.5v11M14.6 9c-.5-.9-1.5-1.3-2.6-1.3-1.4 0-2.5.7-2.5 1.9s1.1 1.6 2.5 2 2.5.8 2.5 2-1.1 1.9-2.5 1.9c-1.1 0-2.1-.4-2.6-1.3"/></svg>',
 "sar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="6.5" rx="7" ry="2.8"/><path d="M5 6.5v5c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8v-5"/><path d="M5 11.5v5c0 1.5 3.1 2.8 7 2.8s7-1.3 7-2.8v-5"/></svg>',
 "bar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 9h10l2 9H5z"/><path d="M9.5 9l1-3.5h3l1 3.5"/></svg>',
 "gem": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h12l3 5-9 11L3 9z"/><path d="M3 9h18M9 4 6 9l6 11 6-11-3-5"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.5 5.6L20 9.3l-4 4 1 5.7-5-2.8-5 2.8 1-5.7-4-4 5.5-.7z"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "swap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h13l-3-3M20 16H7l3 3"/></svg>',
 "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v16M7 20h10M5 8h14M5 8l-2.5 5a3 3 0 0 0 5 0zM19 8l-2.5 5a3 3 0 0 0 5 0z"/></svg>',
}

# ===== الترويسة =====
if price_24:
    live = '<span class="live-badge"><span class="dot"></span> مباشر الآن</span>'
else:
    live = '<span class="live-badge off"><span class="dot"></span> تعذّر الاتصال</span>'
st.markdown(f"""
<div class="brand-row">
  <div class="brand-mark">
    <div class="brand-diamond"></div>
    <div class="brand-name">سيلورا <b>جولد</b></div>
  </div>
  <div class="brand-right">{live}<span class="brand-tag">GOLD&nbsp;DESK</span></div>
</div>
""", unsafe_allow_html=True)

# ===== البطل =====
st.markdown('<div class="sec-head"><span class="idx">01</span><h2>سعر الأونصة العالمي</h2><span class="line"></span></div>', unsafe_allow_html=True)

if price_24:
    # أعمدة حقيقية: ارتفاع كل عمود = نسبة نقاء العيار (بيانات فعلية لا زخرفة)
    order = ["عيار 24", "عيار 22", "عيار 21", "عيار 18"]
    bars = ""
    for i, k in enumerate(order):
        h = g.KARAT_FACTORS[k] * 100
        feat = " feat" if k == "عيار 21" else ""
        bars += (f'<div class="bar-col{feat}" style="animation-delay:{i*0.08}s">'
                 f'<div class="bar" style="height:{h:.0f}%; animation-delay:{0.2+i*0.1}s"></div>'
                 f'<div class="bar-lbl">{k.replace("عيار ","")}</div></div>')
    hero = f"""
    <div class="hero-grid">
      <div class="hero-card">
        <div class="hero-kicker">الأونصة · محوَّلة فورياً للريال السعودي</div>
        <div><span class="hero-big">{f0(OUNCE_SAR)}</span><span class="hero-cur">SAR</span></div>
        <div class="hero-usd">{f2(OUNCE_USD)}<span class="u">دولار أمريكي / أونصة</span></div>
        <div class="hero-meta">آخر تحديث <b>{upd or '—'}</b> بتوقيت الرياض · المصدر <b>gold-api.com</b></div>
      </div>
      <div class="pulse-card">
        <div class="pulse-head"><h3>نبض الأعيرة</h3><span class="hint">نسبة النقاء</span></div>
        <div class="bars">{bars}</div>
      </div>
    </div>
    """
else:
    hero = """
    <div class="hero-grid">
      <div class="hero-card"><div class="hero-kicker">سيلورا جولد</div>
        <div class="hero-big" style="font-size:2.4rem">لوحة الأسعار</div>
        <div class="hero-meta">تعذّر جلب السعر لحظياً — راجع لوحة التشخيص بالأسفل.</div></div>
      <div class="pulse-card"><div class="pulse-head"><h3>نبض الأعيرة</h3></div>
        <div class="bars"><div class="bar-col"><div class="bar" style="height:30%"></div></div></div></div>
    </div>
    """
st.markdown(hero, unsafe_allow_html=True)

# ===== صف بطاقات الأعيرة =====
st.markdown('<div class="sec-head"><span class="idx">02</span><h2>أسعار الجرام</h2><span class="line"></span></div>', unsafe_allow_html=True)

def kcard(icon, label, sar, usd, featured=False, badge=None, delay="0s"):
    cls = "kcard feature" if featured else "kcard"
    bdg = f'<span class="crown">{badge}</span>' if badge else ""
    return (f'<div class="{cls}" style="animation-delay:{delay}">{bdg}'
            f'<div class="ic">{icon}</div>'
            f'<div class="k-label">{label}</div>'
            f'<div class="k-value">{f2(sar)}<span class="k-cur">ر.س</span></div>'
            f'<div class="k-usd">{f2(usd)}<span class="u">USD</span></div></div>')

if price_24:
    cards = "".join([
        kcard(IC["bar"], "عيار 24 · سبائك",     GRAM["عيار 24"], GRAM_USD["عيار 24"], delay=".04s"),
        kcard(IC["sar"], "عيار 22 · خليجي",     GRAM["عيار 22"], GRAM_USD["عيار 22"], delay=".10s"),
        kcard(IC["gem"], "عيار 21 · الأكثر طلباً", GRAM["عيار 21"], GRAM_USD["عيار 21"], featured=True, badge="الأكثر تداولاً", delay=".16s"),
        kcard(IC["star"],"عيار 18 · مشغولات",    GRAM["عيار 18"], GRAM_USD["عيار 18"], delay=".22s"),
    ])
    st.markdown(f'<div class="stat-grid">{cards}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stat-grid"><div class="kcard" style="grid-column:1/-1">تعذّر عرض الأسعار لحظياً من المصدر.</div></div>', unsafe_allow_html=True)

# ===== اللوحة التفصيلية =====
st.markdown('<div class="sec-head"><span class="idx">03</span><h2>اللوحة التفصيلية</h2><span class="line"></span></div>', unsafe_allow_html=True)

NOTES = {"عيار 24": ("سبائك", "gray"), "عيار 22": ("خليجي", "gray"),
         "عيار 21": ("الأكثر طلباً", "gold"), "عيار 18": ("مشغولات", "gray")}
PUR   = {"عيار 24": "99.9%", "عيار 22": "91.6%", "عيار 21": "87.5%", "عيار 18": "75.0%"}

rows = ""
for i, k in enumerate(g.KARAT_FACTORS):
    note, ncls = NOTES[k]
    rows += (f'<tr style="animation-delay:{0.05*i}s">'
             f'<td class="td-karat">{k}</td>'
             f'<td class="td-pur">{PUR[k]}</td>'
             f'<td class="td-num td-sar">{f2(GRAM[k])}</td>'
             f'<td class="td-num td-usd">{f2(GRAM_USD[k])}</td>'
             f'<td class="td-note"><span class="pill {ncls}">{note}</span></td></tr>')

table_html = f"""
<div class="panel">
  <div class="panel-head"><h3>الجرام والأونصة</h3><span class="hint">ريال · دولار</span></div>
  <div class="tbl-wrap"><table class="gold">
    <thead><tr><th>العيار</th><th>النقاء</th><th>ر.س / جرام</th><th>USD / جرام</th><th class="th-note">ملاحظة</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
</div>
"""

side = [
    ("on", IC["star"],  "مصدر السعر",  "gold-api.com",            "متصل",   "green", ".04s"),
    ("",   IC["clock"], "آخر تحديث",   (upd or "—"),               "الرياض", "gray",  ".10s"),
    ("",   IC["swap"],  "سعر الصرف",   "دولار → ريال",            "3.75",   "gray",  ".16s"),
    ("",   IC["scale"], "وزن الأونصة", "Troy Ounce",              "31.10 جم","gray", ".22s"),
]
srows = ""
for on, ic, title, sub, pill, pcls, d in side:
    icc = "s-ic on" if on == "on" else "s-ic"
    srows += (f'<div class="srow" style="animation-delay:{d}"><div class="{icc}">{ic}</div>'
              f'<div class="s-txt"><div class="s-title">{title}</div><div class="s-sub">{sub}</div></div>'
              f'<span class="pill {pcls}">{pill}</span></div>')

side_html = f"""
<div class="panel">
  <div class="panel-head"><h3>تفاصيل السوق</h3><span class="hint">مباشر</span></div>
  {srows}
</div>
"""

st.markdown(f'<div class="mid-grid">{table_html}{side_html}</div>', unsafe_allow_html=True)

# ===== التشخيص عند الفشل فقط =====
if not price_24 and errors:
    items = "".join(f'<div class="d-row"><span>{e}</span><span class="fail">فشل</span></div>' for e in errors)
    st.markdown(f'<div class="diag"><h3>تعذّر جلب السعر من gold-api.com</h3>{items}</div>', unsafe_allow_html=True)

# ===== الفوتر =====
st.markdown("""
<div class="foot">
  سيلورا جولد <span class="sep">◆</span> أسعار استرشادية وفق السوق العالمي وقد تختلف عن أسعار المتجر
  <br>© 2026 جميع الحقوق محفوظة
</div>
""", unsafe_allow_html=True)
