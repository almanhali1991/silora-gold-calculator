# theme.py — لوحة أحادية (أبيض/فحمي/رمادي) كالمرجع | RTL قسري | متجاوبة | بلا حاوية حاضنة
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@500;600;700&family=Tajawal:wght@400;500;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton, [data-testid="stAppDeployButton"] {display:none !important;}
[data-testid="stToolbar"]{display:none !important;}
[data-testid="stDecoration"]{display:none !important;}
footer, [data-testid="stFooter"]{visibility:hidden !important; display:none !important;}

/* ===== RTL قسري على كل شيء ===== */
html, body, .stApp, section.main,
[data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"],
[data-testid="stMarkdownContainer"], .element-container {direction:rtl !important;}
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3, [data-testid="stMarkdownContainer"] span,
.stCaption, [data-testid="stCaptionContainer"] {text-align:right !important;}

:root{
  --bg:#ECECEF; --surface:#FFFFFF; --ink:#18181B; --ink2:#52525B;
  --muted:#71717A; --line:#E4E4E7; --line2:#F4F4F5;
  --shadow:0 1px 2px rgba(16,16,20,.04), 0 12px 30px -16px rgba(16,16,20,.12);
  --shadow-sm:0 1px 2px rgba(16,16,20,.05), 0 6px 18px -12px rgba(16,16,20,.12);
  --r:18px;
}

html, body, .stApp {background:var(--bg) !important; color:var(--ink);
  font-family:'Tajawal','Plus Jakarta Sans',sans-serif; -webkit-font-smoothing:antialiased; min-height:100vh;}
.stApp{background:transparent !important;}
/* شبكة رمادية باهتة على الأطراف كالمرجع */
.stApp::after{content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background-image:
    linear-gradient(rgba(24,24,27,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(24,24,27,.03) 1px, transparent 1px);
  background-size:46px 46px;
  -webkit-mask-image:radial-gradient(130% 95% at 50% 0%, #000 25%, transparent 78%);
          mask-image:radial-gradient(130% 95% at 50% 0%, #000 25%, transparent 78%);}

/* ===== لا حاوية حاضنة: شفافة ومتمركزة فقط ===== */
[data-testid="stMainBlockContainer"]{
  background:transparent !important; box-shadow:none !important; border:none !important;
  border-radius:0 !important; max-width:1120px !important;
  margin:24px auto !important; padding:8px 24px 36px !important;}

/* الترويسة */
.brand-row{display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding:.4rem 0 1.8rem 0; animation:fadeDown .6s ease both;}
.brand-mark{display:flex; align-items:center; gap:.75rem;}
.brand-logo{width:42px; height:42px; border-radius:12px; background:var(--ink);
  display:flex; align-items:center; justify-content:center; color:#fff; flex:none; box-shadow:var(--shadow-sm);}
.brand-logo svg{width:21px; height:21px;}
.brand-name{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.4rem; color:var(--ink); line-height:1;}
.brand-name b{color:var(--ink); font-weight:800;}
.brand-right{display:flex; align-items:center; gap:.7rem;}
.live-badge{display:inline-flex; align-items:center; gap:.5rem; font-size:.78rem; font-weight:700;
  color:var(--ink2); background:var(--surface); border:1px solid var(--line); border-radius:30px; padding:.42rem .9rem; box-shadow:var(--shadow-sm);}
.live-badge .dot{width:8px; height:8px; border-radius:50%; background:#16A34A; animation:pulse 1.8s infinite;}
.live-badge.off{color:#991B1B; background:#FEF2F2; border-color:#FECACA;}
.live-badge.off .dot{background:#DC2626; animation:none;}
.brand-time{font-size:.78rem; color:var(--muted); font-weight:600;}

/* عناوين الأقسام */
.sec-head{display:flex; align-items:center; gap:.7rem; margin:2.4rem 0 1.1rem 0;}
.sec-head h2{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.18rem; color:var(--ink); margin:0;}
.sec-head .line{flex:1; height:1px; background:var(--line);}
.sec-head .idx{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--muted);
  background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:2px 9px; font-size:.78rem; box-shadow:var(--shadow-sm);}

/* بطاقة الأونصة */
.hero-card{position:relative; border-radius:22px; padding:1.9rem 2rem; overflow:hidden; text-align:right;
  background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow); animation:fadeUp .7s ease both;}
.hero-kicker{font-size:.82rem; letter-spacing:.3px; color:var(--muted); font-weight:700; margin-bottom:.9rem;}
.hero-big{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; line-height:.95;
  font-size:clamp(2.8rem,8vw,5rem); color:var(--ink); letter-spacing:-1.5px; font-variant-numeric:tabular-nums;}
.hero-cur{display:inline-block; font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:.95rem;
  color:var(--ink2); background:var(--line2); border:1px solid var(--line); border-radius:8px;
  padding:.15rem .6rem; margin-inline-start:.6rem; vertical-align:middle;}
.hero-sar{margin-top:.85rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:1.3rem;
  color:var(--ink2); font-variant-numeric:tabular-nums;}
.hero-sar .u{font-family:'Tajawal',sans-serif; font-size:.82rem; color:var(--muted); font-weight:600; margin-inline-start:.4rem;}
.hero-meta{margin-top:1.1rem; padding-top:.95rem; border-top:1px dashed var(--line); font-size:.82rem; color:var(--muted);}
.hero-meta b{color:var(--ink2); font-weight:700;}

/* بطاقات الأعيرة */
.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:14px;}
.kcard{position:relative; border-radius:var(--r); padding:1.25rem 1.3rem 1.3rem; text-align:right;
  background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow-sm);
  transition:transform .3s cubic-bezier(.2,.8,.2,1), box-shadow .3s, border-color .3s; animation:fadeUp .6s ease both;}
.kcard:hover{transform:translateY(-4px); box-shadow:var(--shadow); border-color:#D4D4D8;}
.crown{display:inline-block; font-size:.62rem; letter-spacing:.4px; font-weight:800; color:var(--ink);
  background:#fff; border:1px solid var(--line); padding:3px 10px; border-radius:20px; margin-bottom:.7rem; box-shadow:var(--shadow-sm);}
.ic{width:40px; height:40px; border-radius:12px; display:flex; align-items:center; justify-content:center;
  background:var(--line2); color:var(--ink); margin-bottom:.85rem;}
.ic svg{width:20px; height:20px;}
.k-label{font-family:'Cairo',sans-serif; font-size:.95rem; color:var(--ink2); font-weight:700; margin-bottom:.5rem;}
.k-value{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1.55rem; color:var(--ink);
  line-height:1.05; font-variant-numeric:tabular-nums; letter-spacing:-.5px;}
.k-cur{display:inline-block; font-family:'Tajawal',sans-serif; font-size:.7rem; font-weight:700; color:var(--ink2);
  background:var(--line2); border-radius:6px; padding:1px 6px; margin-inline-start:.35rem; vertical-align:middle;}
.k-usd{margin-top:.45rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:.92rem;
  color:var(--muted); font-variant-numeric:tabular-nums;}
.k-usd .u{font-size:.7rem; color:var(--muted); margin-inline-start:.25rem;}
/* البطاقة المميزة = عيار 24 (سوداء كالمرجع) */
.kcard.feature{background:var(--ink); border-color:var(--ink); box-shadow:0 16px 34px -16px rgba(24,24,27,.5);}
.kcard.feature:hover{border-color:var(--ink);}
.kcard.feature .ic{background:rgba(255,255,255,.14); color:#fff;}
.kcard.feature .k-label{color:#D4D4D8;}
.kcard.feature .k-value{color:#fff;}
.kcard.feature .k-cur{background:rgba(255,255,255,.16); color:#fff;}
.kcard.feature .k-usd{color:#A1A1AA;}
.kcard.feature .k-usd .u{color:#71717A;}
.kcard.feature .crown{background:#fff; color:var(--ink); border-color:#fff;}

.diag{border:1px solid #FECACA; border-radius:var(--r); padding:1.2rem 1.3rem; margin-top:1rem; background:#FEF2F2; animation:reveal .5s ease both;}
.diag h3{font-family:'Cairo',sans-serif; color:#B91C1C; margin:0 0 .5rem 0; font-size:1rem;}
.diag .d-row{display:flex; justify-content:space-between; gap:1rem; padding:.3rem 0; font-size:.82rem; color:#7F1D1D; border-bottom:1px dashed #FECACA;}
.diag .fail{color:#DC2626; white-space:nowrap;}

.foot{text-align:center !important; color:var(--muted); font-size:.78rem; margin:2.8rem 0 .2rem 0; line-height:1.8;}
.foot .sep{color:var(--ink2); margin:0 .5rem;}

@media (max-width:900px){ .stat-grid{grid-template-columns:repeat(2,1fr);} }
@media (max-width:768px){
  [data-testid="stMainBlockContainer"]{padding:8px 15px 30px !important; max-width:100% !important;}
  .brand-time{display:none;}
}
@media (max-width:420px){
  .stat-grid{grid-template-columns:1fr 1fr; gap:10px;}
  .k-value{font-size:1.3rem;} .kcard{padding:1rem;}
}

@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(22,163,74,.45);}70%{box-shadow:0 0 0 7px rgba(22,163,74,0);}100%{box-shadow:0 0 0 0 rgba(22,163,74,0);}}
@keyframes fadeUp{from{opacity:0; transform:translateY(16px);}to{opacity:1; transform:none;}}
@keyframes fadeDown{from{opacity:0; transform:translateY(-12px);}to{opacity:1; transform:none;}}
@keyframes reveal{from{opacity:0; transform:translateY(10px);}to{opacity:1; transform:none;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
