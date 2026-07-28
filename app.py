# app.py — سيلورا جولد | لوحة بيضاء + تصدير قصة 9:16 (RTL، متجاوبة، تحديث 60ث)
import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import quote
import theme
import gold_service as g

_FAV = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<rect width="32" height="32" rx="8" fill="#18181B"/>'
        '<path d="M10 13h12l2.5 3.5L16 25 7.5 16.5Z" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linejoin="round"/>'
        '<path d="M7.5 16.5h17M13 13l-3 3.5 6 8.5 6-8.5-3-3.5" fill="none" stroke="#FFFFFF" stroke-width="1.1" stroke-linejoin="round"/>'
        '</svg>')
ICON_SVG = "data:image/svg+xml," + quote(_FAV)

LOGO = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M6 5h12l3 4.5-9 10.5L3 9.5Z"/>'
        '<path d="M3 9.5h18M9 5 6 9.5l6 10.5 6-10.5L15 5"/></svg>')
GEM = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
       'stroke-linecap="round" stroke-linejoin="round">'
       '<path d="M6 5h12l3 4.5-9 10.5L3 9.5Z"/><path d="M3 9.5h18M9 5 6 9.5l6 10.5 6-10.5L15 5"/></svg>')

# ===== قالب بطاقة القصة 9:16 (مكوّن معزول + html2canvas) =====
STORY_TEMPLATE = r"""
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&family=Tajawal:wght@500;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;}
.s-wrap{margin:0; padding:18px 12px 8px; font-family:'Tajawal','Plus Jakarta Sans',sans-serif; direction:rtl; text-align:center;}
.s-stage{width:320px; height:569px; margin:0 auto 16px; overflow:hidden; position:relative;
  border-radius:12px; box-shadow:0 12px 34px -14px rgba(0,0,0,.28); background:#fff;}
.s-scaler{position:absolute; top:0; left:0; width:1080px; height:1920px; transform:scale(0.2962963); transform-origin:top left;}
#storyCard{width:1080px; height:1920px; position:relative; overflow:hidden; background:#FFFFFF;}
#storyCard::before{content:""; position:absolute; inset:0; z-index:0;
  background-image:radial-gradient(rgba(24,24,27,.05) 1.4px, transparent 1.6px); background-size:26px 26px;}
#storyCard::after{content:""; position:absolute; z-index:0; width:760px; height:760px; left:-240px; bottom:-260px;
  border-radius:50%; background:radial-gradient(circle, rgba(24,24,27,.05), transparent 70%);}
.s-pad{position:relative; z-index:2; height:100%; padding:84px 76px 70px; display:flex; flex-direction:column; text-align:right;}
.s-top{display:flex; align-items:center; justify-content:space-between; gap:20px;}
.s-brandrow{display:flex; align-items:center; gap:28px;}
.s-logo{width:116px; height:116px; border-radius:28px; background:#18181B; display:flex; align-items:center; justify-content:center; flex:none;}
.s-logo svg{width:62px; height:62px; color:#fff;}
.s-brand h1{font-family:'Cairo',sans-serif; font-weight:800; font-size:64px; color:#18181B; line-height:1; margin:0;}
.s-brand .sub{font-family:'Plus Jakarta Sans',sans-serif; font-size:24px; letter-spacing:7px; color:#71717A; margin-top:12px; font-weight:700;}
.s-live{display:inline-flex; align-items:center; gap:12px; font-size:26px; font-weight:700; color:#52525B;
  background:#F5F5F5; border:1px solid #ECECEC; border-radius:40px; padding:14px 26px;}
.s-live .dot{width:16px; height:16px; border-radius:50%; background:#16A34A;}
.s-hero{margin-top:62px; background:#fff; border:2px solid #18181B; border-radius:40px; padding:54px 56px;
  box-shadow:0 26px 64px -30px rgba(0,0,0,.32); text-align:center;}
.s-hero .k{font-size:30px; color:#71717A; font-weight:700; letter-spacing:1px;}
.s-hero .big{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:148px; color:#18181B; line-height:.95; letter-spacing:-4px; margin-top:12px;}
.s-hero .cur{display:inline-block; font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:40px; color:#52525B;
  background:#F5F5F5; border:1px solid #ECECEC; border-radius:16px; padding:6px 20px; vertical-align:middle;}
.s-hero .sar{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:58px; color:#52525B; margin-top:18px;}
.s-hero .sar .u{font-family:'Tajawal',sans-serif; font-size:30px; color:#71717A; font-weight:600;}
.s-grid{margin-top:46px; display:grid; grid-template-columns:1fr 1fr; gap:30px; flex:1;}
.s-gcard{background:#fff; border:1px solid #E4E4E7; border-radius:32px; padding:38px 44px;
  box-shadow:0 16px 44px -26px rgba(0,0,0,.22); display:flex; flex-direction:column; justify-content:center;}
.s-gcard.feat{border:2px solid #18181B;}
.s-gcard .gn{font-family:'Cairo',sans-serif; font-weight:700; font-size:42px; color:#52525B;}
.s-gcard.feat .gn{color:#18181B;}
.s-gcard .gv{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:70px; color:#18181B; letter-spacing:-2px; margin-top:8px;}
.s-gcard .gc{display:inline-block; font-family:'Tajawal',sans-serif; font-size:26px; font-weight:700; color:#52525B;
  background:#F5F5F5; border-radius:10px; padding:2px 12px; vertical-align:middle;}
.s-gcard .gu{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:34px; color:#71717A; margin-top:8px;}
.s-foot{margin-top:38px; border-top:1px dashed #E4E4E7; padding-top:30px; display:flex; justify-content:space-between; align-items:center; font-size:26px; color:#71717A; font-weight:600;}
.num{direction:ltr; unicode-bidi:isolate; display:inline-block;}
.s-btn{display:inline-flex; align-items:center; justify-content:center; gap:10px; background:#18181B; color:#fff;
  border:none; border-radius:14px; padding:15px 30px; font-family:'Cairo',sans-serif; font-weight:700; font-size:17px; cursor:pointer;
  transition:transform .2s, opacity .2s;}
.s-btn:hover{transform:translateY(-2px);}
.s-btn:disabled{opacity:.6; cursor:default; transform:none;}
.s-note{display:block; margin-top:10px; font-size:12px; color:#9CA3AF;}
</style>

<div class="s-wrap">
  <div class="s-stage">
    <div class="s-scaler">
      <div id="storyCard">
        <div class="s-pad">
          <div class="s-top">
            <div class="s-brandrow">
              <div class="s-logo">__LOGO__</div>
              <div class="s-brand"><h1>سيلورا جولد</h1><div class="sub">GOLD DESK</div></div>
            </div>
            <div class="s-live"><span class="dot"></span><span>مباشر</span></div>
          </div>
          <div class="s-hero">
            <div class="k">سعر الأونصة العالمي</div>
            <div class="big"><span class="num">__USD__</span> <span class="cur">USD</span></div>
            <div class="sar"><span class="num">__SAR__</span> <span class="u">ريال سعودي / أونصة</span></div>
          </div>
          <div class="s-grid">__KARATS__</div>
          <div class="s-foot"><span>gold-api.com</span><span>آخر تحديث <span class="num">__UPD__</span></span></div>
        </div>
      </div>
    </div>
  </div>
  <button id="dlBtn" class="s-btn" onclick="downloadStory()">تصدير القصة (9:16)</button>
  <span class="s-note">صورة جاهزة للنشر بمقاس ستوري 1080×1920</span>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
function downloadStory(){
  var card = document.getElementById('storyCard');
  var btn = document.getElementById('dlBtn');
  if(typeof html2canvas === 'undefined'){ btn.textContent = 'تعذّر تحميل أداة التصدير'; return; }
  btn.disabled = true; btn.textContent = 'جارٍ التجهيز…';
  var done = function(){
    html2canvas(card, {scale:2, backgroundColor:'#ffffff', useCORS:true, logging:false,
      width:1080, height:1920, windowWidth:1080, windowHeight:1920}).then(function(canvas){
      var a = document.createElement('a');
      a.download = 'silora-gold-' + Date.now() + '.png';
      a.href = canvas.toDataURL('image/png');
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      btn.disabled = false; btn.textContent = 'تصدير القصة (9:16)';
    }).catch(function(){ btn.disabled = false; btn.textContent = 'حدث خطأ، أعد المحاولة'; });
  };
  if(document.fonts && document.fonts.ready){ document.fonts.ready.then(done); } else { done(); }
}
</script>
"""

st.set_page_config(page_title="سيلورا جولد", page_icon=ICON_SVG, layout="wide", initial_sidebar_state="collapsed")
theme.inject()

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

# الترويسة
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

# الأونصة
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

# الأعيرة (بلا شارة، 24 بحدّ فحمي)
st.markdown('<div class="sec-head"><span class="idx">02</span><h2>أسعار الجرام</h2><span class="line"></span></div>', unsafe_allow_html=True)

def kcard(label, sar, usd, featured=False, delay="0s"):
    cls = "kcard feature" if featured else "kcard"
    return (f'<div class="{cls}" style="animation-delay:{delay}">'
            f'<div class="ic">{GEM}</div>'
            f'<div class="k-label">{label}</div>'
            f'<div class="k-value">{f2(sar)}<span class="k-cur">ر.س</span></div>'
            f'<div class="k-usd">{f2(usd)}<span class="u">USD</span></div></div>')

if price_24:
    cards = "".join([
        kcard("عيار 24", GRAM["عيار 24"], GRAM_USD["عيار 24"], featured=True, delay=".04s"),
        kcard("عيار 22", GRAM["عيار 22"], GRAM_USD["عيار 22"], delay=".10s"),
        kcard("عيار 21", GRAM["عيار 21"], GRAM_USD["عيار 21"], delay=".16s"),
        kcard("عيار 18", GRAM["عيار 18"], GRAM_USD["عيار 18"], delay=".22s"),
    ])
    st.markdown(f'<div class="stat-grid">{cards}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stat-grid"><div class="kcard" style="grid-column:1/-1">تعذّر عرض الأسعار لحظياً من المصدر.</div></div>', unsafe_allow_html=True)

# تصدير القصة 9:16 (يظهر فقط عند توفّر الأسعار)
if price_24:
    st.markdown('<div class="sec-head"><span class="idx">03</span><h2>تصدير القصة</h2><span class="line"></span></div>', unsafe_allow_html=True)
    karat_html = ""
    for k in g.KARAT_FACTORS:
        feat = " feat" if k == "عيار 24" else ""
        karat_html += (f'<div class="s-gcard{feat}"><div class="gn">{k}</div>'
                       f'<div class="gv"><span class="num">{f2(GRAM[k])}</span> <span class="gc">ر.س</span></div>'
                       f'<div class="gu"><span class="num">{f2(GRAM_USD[k])}</span> USD</div></div>')
    story = (STORY_TEMPLATE
             .replace("__LOGO__", LOGO)
             .replace("__USD__", f2(OUNCE_USD))
             .replace("__SAR__", f0(OUNCE_SAR))
             .replace("__UPD__", upd or "—")
             .replace("__KARATS__", karat_html))
    components.html(story, height=680, scrolling=False)

# التشخيص عند الفشل فقط
if not price_24 and errors:
    items = "".join(f'<div class="d-row"><span>{e}</span><span class="fail">فشل</span></div>' for e in errors)
    st.markdown(f'<div class="diag"><h3>تعذّر جلب السعر من gold-api.com</h3>{items}</div>', unsafe_allow_html=True)

# الفوتر
st.markdown("""
<div class="foot">
  سيلورا جولد <span class="sep">◆</span> أسعار استرشادية وفق السوق العالمي وقد تختلف عن أسعار المتجر
  <br>© 2026 جميع الحقوق محفوظة
</div>
""", unsafe_allow_html=True)
