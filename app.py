# app.py — سيلورا جولد | هوية فاتحة متجاوبة RTL
import streamlit as st
import theme
import gold_service as g

st.set_page_config(page_title="سيلورا جولد", page_icon="💎", layout="wide", initial_sidebar_state="collapsed")
theme.inject()

price_24, upd, errors = g.fetch_gold()

# ===== الترويسة =====
st.markdown("""
<div class="brand-row">
  <div class="brand-mark">
    <div class="brand-diamond"></div>
    <div class="brand-name">سيلورا <b>جولد</b></div>
  </div>
  <div class="brand-tag">SILORA · GOLD DESK</div>
</div>
""", unsafe_allow_html=True)

# ===== شريط السعر الحي =====
if price_24:
    ticks = "".join(
        f'<span class="tick">{k} <span class="num">{g.gram_price(price_24, k):,.2f}</span> ر.س</span>'
        for k in g.KARAT_FACTORS
    )
    head = '<span class="tick"><span class="live-dot"></span> مباشر الآن</span>'
    st.markdown(f'<div class="ticker"><div class="ticker-track">{head}{ticks}{ticks}{ticks}</div></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="ticker"><div class="ticker-track"><span class="tick">⚠ تعذّر الاتصال بمصدر الأسعار — راجع لوحة التشخيص بالأسفل</span></div></div>', unsafe_allow_html=True)

# ===== البطل =====
if price_24:
    st.markdown(f"""
    <div class="hero">
      <div class="hero-kicker">سعر الذهب العالمي · محوَّل فورياً للريال السعودي</div>
      <div><span class="hero-price">{price_24:,.2f}</span><span class="hero-unit">ريال / جرام 24</span></div>
      <div class="hero-sub">آخر تحديث {upd or '—'} بتوقيت الرياض · المصدر <span class="src">gold-api.com</span></div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="hero"><div class="hero-kicker">سيلورا جولد</div><div class="hero-price">لوحة الأسعار</div></div>', unsafe_allow_html=True)

# ===== لوحة الأعيرة =====
st.markdown('<div class="sec-head"><span class="idx">01</span><h2>أسعار الجرام الآن</h2><span class="line"></span></div>', unsafe_allow_html=True)

if price_24:
    p = {k: g.gram_price(price_24, k) for k in g.KARAT_FACTORS}
    st.markdown(f"""
    <div class="karat-grid">
      <div class="kcard feature" style="animation-delay:.05s">
        <span class="crown">الأكثر تداولاً</span>
        <div class="k-name">عيار 21</div>
        <div class="k-price">{p['عيار 21']:,.2f}</div>
        <div class="k-cur">ريال / جرام</div>
      </div>
      <div class="kcard" style="animation-delay:.10s"><div class="k-name">عيار 24</div><div class="k-price">{p['عيار 24']:,.2f}</div><div class="k-cur">ريال / جرام</div></div>
      <div class="kcard" style="animation-delay:.15s"><div class="k-name">عيار 22</div><div class="k-price">{p['عيار 22']:,.2f}</div><div class="k-cur">ريال / جرام</div></div>
      <div class="kcard" style="animation-delay:.20s"><div class="k-name">عيار 18</div><div class="k-price">{p['عيار 18']:,.2f}</div><div class="k-cur">ريال / جرام</div></div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="kcard" style="grid-column:1/-1">تعذّر عرض الأسعار لحظياً من المصدر.</div>', unsafe_allow_html=True)

# ===== الحاسبة =====
st.markdown('<div class="sec-head"><span class="idx">02</span><h2>احسب قيمة قطعتك</h2><span class="line"></span></div>', unsafe_allow_html=True)

with st.form("calc_form", clear_on_submit=False):
    c1, c2 = st.columns(2)
    with c1:
        weight = st.number_input("الوزن بالجرام", min_value=0.1, value=10.0, step=0.1)
        karat = st.selectbox("العيار", list(g.KARAT_FACTORS.keys()), index=2)
    with c2:
        op = st.radio("نوع العملية", ["شراء", "بيع"], horizontal=True)
        if op == "شراء":
            workmanship = st.number_input("المصنعية بالريال", min_value=0.0, value=50.0, step=10.0)
        else:
            workmanship = 0.0
            st.caption("عند البيع تُحتسب قيمة الذهب الخام فقط دون مصنعية.")
    submitted = st.form_submit_button("احسب القيمة")

if submitted and price_24:
    gp = g.gram_price(price_24, karat)
    raw = weight * gp
    total = raw + workmanship
    rows = f"""
      <div class="inv-row"><span>العيار</span><span>{karat}</span></div>
      <div class="inv-row"><span>الوزن</span><span>{weight:.2f} جرام</span></div>
      <div class="inv-row"><span>سعر الجرام</span><span>{gp:,.2f} ر.س</span></div>
      <div class="inv-row"><span>قيمة الذهب الخام</span><span>{raw:,.2f} ر.س</span></div>
    """
    if op == "شراء":
        rows += f'<div class="inv-row"><span>المصنعية</span><span>{workmanship:,.2f} ر.س</span></div>'
    st.markdown(f"""
    <div class="invoice">
      {rows}
      <div class="inv-total"><span class="lbl">السعر النهائي</span><span class="val">{total:,.2f} ر.س</span></div>
    </div>
    """, unsafe_allow_html=True)
elif submitted and not price_24:
    st.markdown('<div class="diag"><h3>لا يمكن الحساب الآن</h3><div class="d-row"><span>تعذّر جلب السعر من المصدر.</span><span class="fail">—</span></div></div>', unsafe_allow_html=True)

# ===== لوحة التشخيص عند الفشل =====
if not price_24 and errors:
    items = "".join(f'<div class="d-row"><span>{e}</span><span class="fail">فشل</span></div>' for e in errors)
    st.markdown(f"""
    <div class="diag">
      <h3>لوحة تشخيص الاتصال · gold-api.com</h3>
      {items}
    </div>
    """, unsafe_allow_html=True)

# ===== الفوتر =====
st.markdown("""
<div class="foot">
  سيلورا جولد <span class="sep">◆</span> أسعار استرشادية وفق السوق العالمي وقد تختلف عن أسعار المتجر
  <br>© 2026 جميع الحقوق محفوظة
</div>
""", unsafe_allow_html=True)
