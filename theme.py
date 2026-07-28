# theme.py — الهوية البصرية: صالة ذهب ليلية دافئة + حركة حية
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@500;700&family=Tajawal:wght@400;500;700&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,900;1,9..144,600&display=swap');

#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton {display:none !important;}
html, body, .stApp {background-color:#0E0B08; color:#F3EAD8; font-family:'Tajawal',sans-serif;}
.stApp {background:transparent !important;}

/* خلفية طبقاتية + نسيج حُبيبي */
.stApp::before {content:""; position:fixed; inset:0; z-index:-2;
  background:
    radial-gradient(900px 600px at 78% -8%, rgba(201,162,39,.22), transparent 60%),
    radial-gradient(700px 500px at 8% 18%, rgba(120,84,28,.20), transparent 55%),
    radial-gradient(1000px 700px at 50% 118%, rgba(232,199,122,.10), transparent 60%),
    linear-gradient(180deg,#100C08 0%,#0B0805 100%);}
.stApp::after {content:""; position:fixed; inset:0; z-index:-1; pointer-events:none; opacity:.05;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* الترويسة */
.brand-row {display:flex; align-items:center; justify-content:space-between; gap:1rem; padding:.4rem 0 1.2rem 0; animation:fadeDown .8s ease both;}
.brand-mark {display:flex; align-items:center; gap:.7rem;}
.brand-diamond {width:38px; height:38px; transform:rotate(45deg); border-radius:8px;
  background:linear-gradient(135deg,#E8C77A,#C9A227 45%,#8A6516); box-shadow:0 0 24px rgba(201,162,39,.45); animation:breathe 5s ease-in-out infinite;}
.brand-name {font-family:'Reem Kufi',sans-serif; font-weight:700; font-size:1.7rem; color:#F3EAD8; line-height:1;}
.brand-name b {color:#E8C77A;}
.brand-tag {font-size:.78rem; color:#9A8C72; letter-spacing:3px;}

/* شريط السعر الحي */
.ticker {position:relative; overflow:hidden; white-space:nowrap; padding:.55rem 0; margin:.2rem 0 2.4rem 0;
  border-top:1px solid rgba(201,162,39,.25); border-bottom:1px solid rgba(201,162,39,.25); background:rgba(201,162,39,.05);}
.ticker-track {display:inline-block; padding-left:100%; animation:scroll 26s linear infinite;}
.ticker-track:hover {animation-play-state:paused;}
.tick {display:inline-flex; align-items:center; gap:.5rem; margin:0 2.2rem; font-size:.92rem; color:#C9B78F;}
.tick .num {font-family:'Fraunces',serif; font-weight:600; color:#F3EAD8; font-size:1.05rem; font-variant-numeric:tabular-nums;}
.live-dot {width:8px; height:8px; border-radius:50%; background:#7BD88F; animation:pulse 1.8s infinite;}

/* البطل */
.hero {animation:fadeUp .9s ease both;}
.hero-kicker {font-size:.8rem; letter-spacing:4px; text-transform:uppercase; color:#9A8C72;}
.hero-price {font-family:'Fraunces',serif; font-weight:900; line-height:.92; font-size:clamp(3.4rem,9vw,6.6rem);
  background:linear-gradient(100deg,#8A6516,#E8C77A 30%,#FFF4D6 50%,#E8C77A 70%,#8A6516); background-size:220% auto;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; animation:shimmer 6s linear infinite;}
.hero-unit {font-family:'Fraunces',serif; font-style:italic; font-size:1.3rem; color:#C9B78F; margin-left:.4rem;}
.hero-sub {color:#9A8C72; font-size:.95rem; margin-top:.4rem;}

/* عناوين الأقسام */
.sec-head {display:flex; align-items:baseline; gap:.8rem; margin:3rem 0 1.2rem 0;}
.sec-head h2 {font-family:'Reem Kufi',sans-serif; font-weight:700; font-size:1.5rem; color:#F3EAD8; margin:0;}
.sec-head .line {flex:1; height:1px; background:linear-gradient(90deg,rgba(201,162,39,.5),transparent);}
.sec-head .idx {font-family:'Fraunces',serif; font-style:italic; color:#8A6516;}

/* لوحة الأعيرة — تخطيط تحرري غير متماثل */
.karat-grid {display:grid; grid-template-columns:1.4fr 1fr 1fr; grid-template-rows:auto auto; gap:14px;}
.kcard {position:relative; border-radius:16px; padding:1.3rem 1.4rem; overflow:hidden;
  background:linear-gradient(160deg,rgba(255,255,255,.04),rgba(255,255,255,.01)); border:1px solid rgba(201,162,39,.18);
  transition:transform .35s cubic-bezier(.2,.8,.2,1),border-color .35s,box-shadow .35s; animation:fadeUp .8s ease both;}
.kcard:hover {transform:translateY(-6px); border-color:rgba(232,199,122,.6); box-shadow:0 18px 40px -18px rgba(201,162,39,.5);}
.kcard .k-name {font-family:'Reem Kufi',sans-serif; font-size:1.05rem; color:#C9B78F;}
.kcard .k-price {font-family:'Fraunces',serif; font-weight:900; font-size:2rem; color:#F3EAD8; margin-top:.3rem; font-variant-numeric:tabular-nums;}
.kcard .k-cur {font-size:.78rem; color:#8A7C63; letter-spacing:1px;}
.kcard.feature {grid-row:span 2; display:flex; flex-direction:column; justify-content:center;
  background:linear-gradient(160deg,rgba(201,162,39,.16),rgba(138,101,22,.06)); border:1px solid rgba(232,199,122,.55);}
.kcard.feature .k-name {font-size:1.5rem; color:#F3EAD8;}
.kcard.feature .k-price {font-size:clamp(2.6rem,5vw,3.8rem);
  background:linear-gradient(100deg,#C9A227,#FFF4D6,#C9A227); background-size:200% auto;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; animation:shimmer 5s linear infinite;}
.kcard .crown {position:absolute; top:1rem; left:1.2rem; font-size:.62rem; letter-spacing:2px; text-transform:uppercase;
  color:#0E0B08; background:#E8C77A; padding:3px 9px; border-radius:20px; font-weight:700;}

/* نموذج الحاسبة (stForm) */
[data-testid="stForm"] {border:1px solid rgba(201,162,39,.22); border-radius:20px; padding:1.6rem 1.8rem;
  background:linear-gradient(160deg,rgba(255,255,255,.035),rgba(255,255,255,.008)); animation:fadeUp .9s ease both;}
[data-testid="stForm"] form {background:transparent !important;}
[data-testid="stNumberInput"] input, [data-testid="stSelectbox"] select,
div[data-baseweb="select"] > div, div[data-baseweb="popover"] {
  background-color:#16110B !important; color:#F3EAD8 !important; border:1px solid rgba(201,162,39,.3) !important; border-radius:10px !important;}
[data-testid="stRadio"] label, [data-testid="stNumberInput"] label, [data-testid="stSelectbox"] label {color:#C9B78F !important;}
div[role="radiogroup"] label, div[role="radiogroup"] label span {color:#F3EAD8 !important;}
[data-testid="stFormSubmitButton"] > button, .stButton > button {
  background:linear-gradient(135deg,#E8C77A,#C9A227) !important; color:#1A1306 !important; border:none !important;
  border-radius:12px !important; font-family:'Reem Kufi',sans-serif !important; font-weight:700 !important; letter-spacing:1px !important;
  padding:.7rem 1.2rem !important; transition:transform .25s,box-shadow .25s,filter .25s !important;}
[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover {
  transform:translateY(-2px); box-shadow:0 14px 30px -12px rgba(232,199,122,.7); filter:brightness(1.06);}

/* الفاتورة */
.invoice {margin-top:1.6rem; border-radius:18px; padding:1.8rem; position:relative; overflow:hidden;
  background:linear-gradient(160deg,rgba(201,162,39,.10),rgba(0,0,0,.2)); border:1px solid rgba(232,199,122,.4); animation:reveal .7s cubic-bezier(.2,.8,.2,1) both;}
.invoice::before {content:""; position:absolute; top:0; right:0; width:120px; height:120px; background:radial-gradient(circle,rgba(232,199,122,.25),transparent 70%);}
.inv-row {display:flex; justify-content:space-between; padding:.55rem 0; border-bottom:1px dashed rgba(201,162,39,.18); color:#C9B78F;}
.inv-row span:last-child {color:#F3EAD8; font-family:'Fraunces',serif; font-weight:600; font-variant-numeric:tabular-nums;}
.inv-total {display:flex; justify-content:space-between; align-items:flex-end; margin-top:1rem; padding-top:1rem; border-top:1px solid rgba(232,199,122,.4);}
.inv-total .lbl {font-family:'Reem Kufi',sans-serif; color:#C9B78F; font-size:1.1rem;}
.inv-total .val {font-family:'Fraunces',serif; font-weight:900; font-size:clamp(2rem,5vw,3rem);
  background:linear-gradient(100deg,#C9A227,#FFF4D6,#C9A227); background-size:200% auto;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; animation:shimmer 5s linear infinite;}

/* لوحة التشخيص */
.diag {border:1px solid rgba(214,120,92,.4); border-radius:16px; padding:1.4rem; margin-top:1rem;
  background:linear-gradient(160deg,rgba(214,120,92,.10),rgba(0,0,0,.2)); animation:reveal .6s ease both;}
.diag h3 {font-family:'Reem Kufi',sans-serif; color:#E8A98C; margin:0 0 .6rem 0; font-size:1.1rem;}
.diag .d-row {display:flex; justify-content:space-between; gap:1rem; padding:.35rem 0; font-size:.86rem; color:#C9B78F; border-bottom:1px dashed rgba(255,255,255,.06);}
.diag .fail {color:#E08A6E; white-space:nowrap;}

/* الفوتر */
.foot {text-align:center; color:#7A6E58; font-size:.82rem; margin:3.5rem 0 1rem 0; line-height:1.8;}
.foot .sep {color:#C9A227; margin:0 .6rem;}

/* الحركات */
@keyframes shimmer {to {background-position:200% center;}}
@keyframes scroll {to {transform:translateX(-100%);}}
@keyframes pulse {0%{box-shadow:0 0 0 0 rgba(123,216,143,.5);}70%{box-shadow:0 0 0 8px rgba(123,216,143,0);}100%{box-shadow:0 0 0 0 rgba(123,216,143,0);}}
@keyframes breathe {0%,100%{box-shadow:0 0 18px rgba(201,162,39,.35);}50%{box-shadow:0 0 34px rgba(232,199,122,.6);}}
@keyframes fadeUp {from{opacity:0; transform:translateY(22px);}to{opacity:1; transform:none;}}
@keyframes fadeDown {from{opacity:0; transform:translateY(-16px);}to{opacity:1; transform:none;}}
@keyframes reveal {from{opacity:0; transform:translateY(14px) scale(.98);}to{opacity:1; transform:none;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
