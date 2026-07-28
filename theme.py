# theme.py — هوية فاتحة نظيفة مستوحاة من لوحة Jobgio + RTL + متجاوب
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&family=Cairo:wght@600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

/* إخفاء إطار Streamlit */
#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton {display:none !important;}

/* ===== المتغيرات ===== */
:root{
  --bg:#ECECEF; --surface:#FFFFFF; --ink:#18181B; --ink2:#52525B;
  --muted:#A1A1AA; --line:#E4E4E7; --line2:#F4F4F5; --gold:#9C7A1E;
  --shadow:0 1px 2px rgba(16,16,20,.04), 0 10px 30px -12px rgba(16,16,20,.10);
  --shadow-sm:0 1px 2px rgba(16,16,20,.05);
  --r:20px;
}

/* ===== RTL عام ===== */
html, body, .stApp {direction:rtl; text-align:right;}
[data-testid="stAppViewContainer"], section.main,
[data-testid="stMainBlockContainer"], [data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"] {direction:rtl;}

/* ===== الخلفية الرمادية الفاتحة ===== */
html, body, .stApp {background:var(--bg) !important; color:var(--ink);
  font-family:'Tajawal','Plus Jakarta Sans',sans-serif;}
.stApp {background:transparent !important;}

/* ===== الحاوية البيضاء العائمة (كاللوحة في الصورة) ===== */
[data-testid="stMainBlockContainer"]{
  background:var(--surface) !important;
  border-radius:28px !important;
  box-shadow:var(--shadow) !important;
  max-width:1180px !important;
  margin:22px auto !important;
  padding:26px 34px 44px !important;
}

/* ===== الترويسة ===== */
.brand-row{display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding:.2rem 0 1.4rem 0; animation:fadeDown .7s ease both;}
.brand-mark{display:flex; align-items:center; gap:.7rem;}
.brand-diamond{width:34px; height:34px; transform:rotate(45deg); border-radius:9px;
  background:linear-gradient(135deg,#E8C77A,#C9A227 50%,#9C7A1E); box-shadow:0 4px 12px rgba(156,122,30,.30);}
.brand-name{font-family:'Cairo',sans-serif; font-weight:800; font-size:1.45rem; color:var(--ink); line-height:1;}
.brand-name b{color:var(--gold);}
.brand-tag{font-size:.72rem; color:var(--muted); letter-spacing:2px; font-weight:600;}

/* ===== شريط السعر الحي ===== */
.ticker{direction:ltr; position:relative; overflow:hidden; white-space:nowrap;
  background:var(--line2); border:1px solid var(--line); border-radius:14px;
  padding:.5rem 0; margin:.2rem 0 2rem 0;}
.ticker-track{display:inline-block; padding-left:100%; animation:scroll 28s linear infinite;}
.ticker-track:hover{animation-play-state:paused;}
.tick{direction:rtl; display:inline-flex; align-items:center; gap:.45rem; margin:0 1.8rem;
  font-size:.88rem; color:var(--ink2);}
.tick .num{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--ink);
  font-size:1rem; font-variant-numeric:tabular-nums;}
.live-dot{width:8px; height:8px; border-radius:50%; background:#16A34A; animation:pulse 1.8s infinite;}

/* ===== البطل ===== */
.hero{animation:fadeUp .8s ease both; padding:.4rem 0 .2rem 0;}
.hero-kicker{font-size:.78rem; letter-spacing:1px; color:var(--muted); font-weight:600;}
.hero-price{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; line-height:1;
  font-size:clamp(2.6rem,8vw,4.6rem); color:var(--ink); font-variant-numeric:tabular-nums; letter-spacing:-1px;}
.hero-unit{font-family:'Tajawal',sans-serif; font-weight:600; font-size:1.05rem; color:var(--ink2); margin-right:.5rem;}
.hero-sub{color:var(--muted); font-size:.9rem; margin-top:.5rem;}
.hero-sub .src{color:var(--gold); font-weight:700;}

/* ===== عناوين الأقسام ===== */
.sec-head{display:flex; align-items:center; gap:.7rem; margin:2.4rem 0 1.1rem 0;}
.sec-head h2{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.25rem; color:var(--ink); margin:0;}
.sec-head .line{flex:1; height:1px; background:var(--line);}
.sec-head .idx{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--muted);
  background:var(--line2); border:1px solid var(--line); border-radius:8px; padding:2px 9px; font-size:.8rem;}

/* ===== لوحة الأعيرة (متجاوبة) ===== */
.karat-grid{display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:14px;}
.kcard{border-radius:var(--r); padding:1.2rem 1.3rem; background:var(--surface);
  border:1px solid var(--line); box-shadow:var(--shadow-sm);
  transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s,border-color .3s; animation:fadeUp .7s ease both;}
.kcard:hover{transform:translateY(-4px); box-shadow:var(--shadow); border-color:#D4D4D8;}
.kcard .k-name{font-family:'Tajawal',sans-serif; font-size:.95rem; color:var(--ink2); font-weight:600;}
.kcard .k-price{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1.7rem;
  color:var(--ink); margin-top:.35rem; font-variant-numeric:tabular-nums;}
.kcard .k-cur{font-size:.72rem; color:var(--muted); margin-top:.15rem;}
/* البطاقة السوداء المميزة (كالصورة) */
.kcard.feature{background:var(--ink); border-color:var(--ink); box-shadow:0 12px 30px -12px rgba(24,24,27,.5);}
.kcard.feature .k-name{color:#D4D4D8;}
.kcard.feature .k-price{color:#FFFFFF; font-size:clamp(1.8rem,4vw,2.3rem);}
.kcard.feature .k-cur{color:#A1A1AA;}
.kcard .crown{display:inline-block; font-size:.6rem; letter-spacing:1px; font-weight:700;
  color:#fff; background:var(--gold); padding:2px 8px; border-radius:20px; margin-bottom:.5rem;}

/* ===== نموذج الحاسبة ===== */
[data-testid="stForm"]{border:1px solid var(--line); border-radius:var(--r); padding:1.5rem 1.6rem;
  background:var(--line2); animation:fadeUp .8s ease both;}
[data-testid="stForm"] form{background:transparent !important;}
[data-testid="stNumberInput"] input, [data-testid="stSelectbox"] select,
div[data-baseweb="select"] > div{
  background:#fff !important; color:var(--ink) !important; border:1px solid var(--line) !important;
  border-radius:12px !important; text-align:right !important; direction:rtl !important;}
[data-testid="stRadio"] label, [data-testid="stNumberInput"] label, [data-testid="stSelectbox"] label{
  color:var(--ink2) !important; font-weight:600 !important;}
div[role="radiogroup"]{direction:rtl !important;}
div[role="radiogroup"] label, div[role="radiogroup"] label span{color:var(--ink) !important;}
.stCaption, [data-testid="stCaptionContainer"]{color:var(--muted) !important;}
[data-testid="stFormSubmitButton"] > button, .stButton > button{
  background:var(--ink) !important; color:#fff !important; border:none !important; border-radius:12px !important;
  font-family:'Cairo',sans-serif !important; font-weight:700 !important; padding:.7rem 1.2rem !important;
  transition:transform .25s,box-shadow .25s,opacity .25s !important;}
[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover{
  transform:translateY(-2px); box-shadow:0 12px 26px -12px rgba(24,24,27,.5); opacity:.92;}

/* ===== الفاتورة ===== */
.invoice{margin-top:1.4rem; border-radius:var(--r); padding:1.6rem; background:var(--surface);
  border:1px solid var(--line); box-shadow:var(--shadow); animation:reveal .6s cubic-bezier(.2,.8,.2,1) both;}
.inv-row{display:flex; justify-content:space-between; padding:.55rem 0; border-bottom:1px dashed var(--line); color:var(--ink2);}
.inv-row span:last-child{color:var(--ink); font-family:'Plus Jakarta Sans',sans-serif; font-weight:600; font-variant-numeric:tabular-nums;}
.inv-total{display:flex; justify-content:space-between; align-items:flex-end; margin-top:1rem; padding-top:1rem; border-top:2px solid var(--ink);}
.inv-total .lbl{font-family:'Cairo',sans-serif; color:var(--ink); font-size:1.05rem; font-weight:700;}
.inv-total .val{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; color:var(--gold);
  font-size:clamp(1.8rem,5vw,2.6rem); font-variant-numeric:tabular-nums;}

/* ===== لوحة التشخيص ===== */
.diag{border:1px solid #FECACA; border-radius:var(--r); padding:1.3rem; margin-top:1rem;
  background:#FEF2F2; animation:reveal .6s ease both;}
.diag h3{font-family:'Cairo',sans-serif; color:#B91C1C; margin:0 0 .6rem 0; font-size:1.05rem;}
.diag .d-row{display:flex; justify-content:space-between; gap:1rem; padding:.35rem 0; font-size:.85rem; color:var(--ink2); border-bottom:1px dashed #FECACA;}
.diag .fail{color:#DC2626; white-space:nowrap;}

/* ===== الفوتر ===== */
.foot{text-align:center; color:var(--muted); font-size:.8rem; margin:3rem 0 .5rem 0; line-height:1.8;}
.foot .sep{color:var(--gold); margin:0 .5rem;}

/* ===== التجاوب مع الشاشات ===== */
@media (max-width:768px){
  [data-testid="stMainBlockContainer"]{border-radius:0 !important; margin:0 !important;
    padding:18px 16px 32px !important; max-width:100% !important;}
  [data-testid="stHorizontalBlock"]{flex-direction:column !important;}
  .brand-tag{display:none;}
  .tick{margin:0 1.1rem; font-size:.82rem;}
}
@media (max-width:420px){
  .karat-grid{grid-template-columns:repeat(2,1fr); gap:10px;}
  .kcard{padding:1rem;}
  .kcard .k-price{font-size:1.4rem;}
}

/* ===== الحركات ===== */
@keyframes scroll{to{transform:translateX(-100%);}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(22,163,74,.5);}70%{box-shadow:0 0 0 7px rgba(22,163,74,0);}100%{box-shadow:0 0 0 0 rgba(22,163,74,0);}}
@keyframes fadeUp{from{opacity:0; transform:translateY(18px);}to{opacity:1; transform:none;}}
@keyframes fadeDown{from{opacity:0; transform:translateY(-14px);}to{opacity:1; transform:none;}}
@keyframes reveal{from{opacity:0; transform:translateY(12px) scale(.99);}to{opacity:1; transform:none;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
