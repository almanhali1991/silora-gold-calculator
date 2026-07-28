# app.py — سيلورا جولد | لوحة أسعار نقية (عاجية دافئة، RTL، متجاوبة، تحديث 60ث)
import streamlit as st
from urllib.parse import quote
import theme
import gold_service as g

# ===== أيقونة تبويب المتصفح مطابقة للشعار (دائرة كريمية + ماسة ذهبية) =====
_FAV = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<circle cx="16" cy="16" r="15" fill="#F3E7C4" stroke="#C9A227" stroke-width="1.5"/>'
        '<path d="M10 13h12l2.5 3.5L16 25 7.5 16.5Z" fill="none" stroke="#8A6D1F" stroke-width="1.7" stroke-linejoin="round"/>'
        '<path d="M7.5 16.5h17M13 13l-3 3.5 6 8.5 6-8.5-3-3.5" fill="none" stroke="#8A6D1F" stroke-width="1.1" stroke-linejoin="round"/>'
        '</svg>')
ICON_SVG = "data:image/svg+xml," + quote(_FAV)

LOGO = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M6 5h12l3 4.5-9 10.5L3 9.5Z"/>'
        '<path d="M3 9.5h18M9 5 6 9.5l6 10.5 6-10.5L15 5"/></svg>')

st.set_page_config(page_title="سيلورا جولد", page_icon=ICON_SVG, layout="wide", initial_sidebar_state="collapsed")
theme.inject()

# ===== تحديث تلقائي كل 60 ثانية =====
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=60 * 1000, key="silora_gold_refresh")
except Exception:
    pass

price_24, upd, errors = g.fetch_gold()

def f2(v): return "—" if v is None else f"{v:,.2f}"
def f0(v): return "—" if v is None else f"{v:,.0f}"

OUNCE_SAR = price_24 * g.OUNCE_TO_GRAM if price_24 else None
OUNCE_USD = OUNCE_SAR / g.USD_TO_SAR if OUNCE_SAR else None
GRAM      = {k: (g.gram_price(price_24, k) if price_24 else None) for k in g.KARAT_FACTORS}
GRAM_USD  = {k: (GRAM[k] / g.USD_TO_SAR if GRAM[k] else None) for k in GRAM}

# ===== الترويسة =====
if price_24:
    live = '<span class="live-badge"><span class="dot"></span> مباشر الآن</span>'
else:
    live = '<span class="live-badge off"><span class="dot"></span> تعذّر الاتصال</span>'
time_html = f'<span class="brand-time">آخر تحديث {upd or "—"}</span>' if price_24 else ''
st.markdown(f"""
<div class="brand-row">
  <div class="brand-mark">
    <div class="brand-logo">{LOGO}</div>
    <div class="brand-name">سيلورا <b>جولد</b></div>
  </div>
  <div class="brand-right">{time_html}{live}</div>
</div>
""", unsafe_allow_html=True)

# ===== الأونصة: الكبير = دولار، الصغير = ريال =====
st.markdown('<div class="sec-head"><span class="idx">01</span><h2>سعر الأونصة العالمي</h2><span class="line"></span></div>', unsafe_allow_html=True)
if price_24:
    st.markdown(f"""
    <div class="hero-card">
      <div class="hero-kicker">الأونصة · السعر العالمي المباشر</div>
      <div><span class="hero-big">{f2(OUNCE_USD)}</span><span class="hero-cur">USD</span></div>
      <div class="hero-sar">{f0(OUNCE_SAR)}<span class="u">ريال سعودي / أونصة</span></div>
      <div class="hero-meta">المصدر <b>gold-api.com</b></div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="hero-card"><div class="hero-kicker">سيلورا جولد</div>'
                '<div class="hero-big" style="font-size:2.4rem">لوحة الأسعار</div>'
                '<div class="hero-meta">تعذّر جلب السعر لحظياً — راجع لوحة التشخيص بالأسفل.</div></div>', unsafe_allow_html=True)

# ===== الأعيرة: ريال كبير + دولار صغير (ترتيب ثابت) =====
st.markdown('<div class="sec-head"><span class="idx">02</span><h2>أسعار الجرام</h2><span class="line"></span></div>', unsafe_allow_html=True)

def kcard(label, sar, usd, featured=False, badge=None, delay="0s"):
    cls = "kcard feature" if featured else "kcard"
    bdg = f'<span class="crown">{badge}</span>' if badge else ""
    return (f'<div class="{cls}" style="animation-delay:{delay}">{bdg}'
            f'<div class="k-label">{label}</div>'
            f'<div class="k-value">{f2(sar)}<span class="k-cur">ر.س</span></div>'
            f'<div class="k-usd">{f2(usd)}<span class="u">USD</span></div></div>')

if price_24:
    cards = "".join([
        kcard("عيار 24", GRAM["عيار 24"], GRAM_USD["عيار 24"], featured=True, badge="الأكثر تداولاً", delay=".04s"),
        kcard("عيار 22", GRAM["عيار 22"], GRAM_USD["عيار 22"], delay=".10s"),
        kcard("عيار 21", GRAM["عيار 21"], GRAM_USD["عيار 21"], delay=".16s"),
        kcard("عيار 18", GRAM["عيار 18"], GRAM_USD["عيار 18"], delay=".22s"),
    ])
    st.markdown(f'<div class="stat-grid">{cards}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stat-grid"><div class="kcard" style="grid-column:1/-1">تعذّر عرض الأسعار لحظياً من المصدر.</div></div>', unsafe_allow_html=True)

# ===== جدول ملخّص: 3 أعمدة فقط (بلا كلمات إضافية) =====
st.markdown('<div class="sec-head"><span class="idx">03</span><h2>ملخّص الأسعار</h2><span class="line"></span></div>', unsafe_allow_html=True)
rows = ""
for i, k in enumerate(g.KARAT_FACTORS):
    rows += (f'<tr style="animation-delay:{0.05*i}s">'
             f'<td class="td-karat">{k}</td>'
             f'<td class="td-num td-sar">{f2(GRAM[k])}</td>'
             f'<td class="td-num td-usd">{f2(GRAM_USD[k])}</td></tr>')
st.markdown(f"""
<div class="panel"><div class="tbl-wrap"><table class="gold">
  <thead><tr><th>العيار</th><th>ريال / جرام</th><th>دولار / جرام</th></tr></thead>
  <tbody>{rows}</tbody>
</table></div></div>
""", unsafe_allow_html=True)

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
