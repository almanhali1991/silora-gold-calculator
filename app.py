# app.py — سيلورا جولد | لوحة أسعار نقية (فاتحة، RTL، متجاوبة)
import streamlit as st
import theme
import gold_service as g

st.set_page_config(page_title="سيلورا جولد", page_icon="💎", layout="wide", initial_sidebar_state="collapsed")
theme.inject()

price_24, upd, errors = g.fetch_gold()

# ===== حسابات مشتقة من سعر جرام 24 (بدون لمس gold_service) =====
def f2(v):  return "—" if v is None else f"{v:,.2f}"
def f0(v):  return "—" if v is None else f"{v:,.0f}"

ounce_sar = price_24 * g.OUNCE_TO_GRAM if price_24 else None
ounce_usd = ounce_sar / g.USD_TO_SAR if ounce_sar else None
grams     = {k: (g.gram_price(price_24, k) if price_24 else None) for k in g.KARAT_FACTORS}
grams_usd = {k: (grams[k] / g.USD_TO_SAR if grams[k] else None) for k in grams}

# ===== الترويسة =====
if price_24:
    live = f'<span class="live-badge"><span class="dot"></span> مباشر · {upd or "—"}</span>'
else:
    live = '<span class="live-badge off"><span class="dot"></span> تعذّر الاتصال</span>'
st.markdown(f"""
<div class="brand-row">
  <div class="brand-mark">
    <div class="brand-diamond"></div>
    <div class="brand-name">سيلورا <b>جولد</b></div>
  </div>
  <div style="display:flex; align-items:center; gap:.8rem;">
    {live}
    <div class="brand-tag">GOLD&nbsp;DESK</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ===== صف البطاقات (الأونصة + العيار المميز) =====
def stat(icon, label, value, unit, featured=False, badge=None, delay="0s"):
    cls = "kcard feature" if featured else "kcard"
    bdg = f'<span class="crown">{badge}</span>' if badge else ""
    return (f'<div class="{cls}" style="animation-delay:{delay}">{bdg}'
            f'<div class="ic">{icon}</div>'
            f'<div class="k-value">{value}<span class="k-unit">{unit}</span></div>'
            f'<div class="k-label">{label}</div></div>')

cards = [
    stat("$",  "الأونصة · دولار",  f2(ounce_usd), "USD", delay=".04s"),
    stat("﷼", "الأونصة · ريال",   f0(ounce_sar), "SAR", delay=".10s"),
    stat("24", "الجرام · عيار 24", f2(grams["عيار 24"]), "ر.س", delay=".16s"),
    stat("21", "الجرام · عيار 21", f2(grams["عيار 21"]), "ر.س", featured=True, badge="الأكثر تداولاً", delay=".22s"),
]
st.markdown(f'<div class="stat-grid">{"".join(cards)}</div>', unsafe_allow_html=True)

# ===== القسم الأوسط: جدول تفصيلي + تفاصيل السوق =====
st.markdown('<div class="sec-head"><span class="idx">01</span><h2>لوحة الأسعار التفصيلية</h2><span class="line"></span></div>', unsafe_allow_html=True)

NOTES = {"عيار 24": ("سبائك", "gray"), "عيار 22": ("خليجي", "gray"),
         "عيار 21": ("الأكثر طلباً", "gold"), "عيار 18": ("مشغولات", "gray")}
PUR   = {"عيار 24": "99.9%", "عيار 22": "91.6%", "عيار 21": "87.5%", "عيار 18": "75.0%"}

rows = ""
for i, k in enumerate(g.KARAT_FACTORS):
    note, ncls = NOTES[k]
    rows += (f'<tr style="animation-delay:{0.05*i}s">'
             f'<td class="td-karat">{k}</td>'
             f'<td class="td-pur">{PUR[k]}</td>'
             f'<td class="td-num td-sar">{f2(grams[k])}</td>'
             f'<td class="td-num td-usd">{f2(grams_usd[k])}</td>'
             f'<td class="td-note"><span class="pill {ncls}">{note}</span></td></tr>')

table_html = f"""
<div class="panel">
  <div class="panel-head"><h3>أسعار الجرام والأونصة</h3><span class="hint">ريال · دولار</span></div>
  <div class="tbl-wrap">
    <table class="gold">
      <thead><tr>
        <th>العيار</th><th>النقاء</th><th>السعر / جرام (ر.س)</th>
        <th>السعر / جرام ($)</th><th class="th-note">ملاحظة</th>
      </tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
</div>
"""

STAR = ('<svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 1 L9.8 6.2 L15 8 L9.8 9.8 L8 15 L6.2 9.8 L1 8 L6.2 6.2 Z"/></svg>')
side_items = [
    ("on",  "مصدر السعر",   "gold-api.com",            "متصل",  "green", ".04s"),
    ("",    "آخر تحديث",    (upd or "—") + " · الرياض",  "UTC+3", "gray",  ".10s"),
    ("",    "سعر الصرف",    "دولار → ريال سعودي",       "3.75",  "gray",  ".16s"),
    ("",    "وزن الأونصة",  "Troy Ounce",               "31.10 جم", "gray", ".22s"),
]
srows = ""
for on, title, sub, pill, pcls, d in side_items:
    ic_cls = "s-ic on" if on == "on" else "s-ic"
    srows += (f'<div class="srow" style="animation-delay:{d}">'
              f'<div class="{ic_cls}">{STAR}</div>'
              f'<div class="s-txt"><div class="s-title">{title}</div><div class="s-sub">{sub}</div></div>'
              f'<span class="pill {pcls}">{pill}</span></div>')

side_html = f"""
<div class="panel">
  <div class="panel-head"><h3>تفاصيل السوق</h3><span class="hint">مباشر</span></div>
  {srows}
</div>
"""

st.markdown(f'<div class="mid-grid">{table_html}{side_html}</div>', unsafe_allow_html=True)

# ===== لوحة التشخيص عند الفشل فقط =====
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
