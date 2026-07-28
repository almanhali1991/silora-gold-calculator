# theme.py — لوحة بيضاء نقية | RTL قسري | متجاوبة | بلا شارة | نص الأونصة موسَّط
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@500;600;700&family=Tajawal:wght@400;500;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton, [data-testid="stAppDeployButton"] {display:none !important;}
[data-testid="stToolbar"]{display:none !important;}
[data-testid="stDecoration"]{display:none !important;}
footer, [data-testid="stFooter"]{visibility:hidden !important; display:none !important;}

/* RTL قسري */
html, body, .stApp, section.main,
[data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"],
[data-testid="stMarkdownContainer"], .element-container {direction:rtl !important;}
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3, [data-testid="stMarkdownContainer"] span,
.stCaption, [data-testid="stCaptionContainer"] {text-align:right !important;}

:root{
  --bg:#FFFFFF; --surface:#FFFFFF; --ink:#18181B; --ink2:#52525B;
  --muted:#71717A; --line:#ECECEC; --line2:#F5F5F5;
  --shadow:0 1px 2px rgba(16,16,20,.04), 0 14px 34px -18px rgba(16,16,20,.14);
  --shadow-sm:0 1px 2px rgba(16,16,20,.04), 0 8px 22px -14px rgba(16,16,20,.12);
  --r:20px;
}

html, body, .stApp {background:var(--bg) !important; color:var(--ink);
  font-family:'Tajawal','Plus Jakarta Sans',sans-serif; -webkit-font-smoothing:antialiased; min-height:100vh;}
.stApp{background:transparent !important;}
/* خلفية بيضاء بنسيج نقطي باهت جداً + توهج علوي خفيف = الفرق البسيط عن الكروت */
.stApp::before{content:""; position:fixed; inset:0; z-index:-2; background:var(--bg);}
.stApp::after{content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background-image:
    radial-gradient(rgba(24,24,27,.045) 1px, transparent 1.4px),
    radial-gradient(620px 320px at 50% -6%, rgba(24,24,27,.04), transparent 70%);
  background-size:22px 22px, auto;
  -webkit-mask-image:radial-gradient(135% 100% at 50% 0%, #000 30%, transparent 82%);
          mask-image:radial-gradient(135% 100% at 50% 0%, #000 30%, transparent 82%);}

/* لا حاوية حاضنة */
[data-testid="stMainBlockContainer"]{
  background:transparent !important; box-shadow:none !important; border:none !important;
  border-radius:0 !important; max-width:1080px !important;
  margin:30px auto !important; padding:10px 30px 48px !important;}

/* الترويسة */
.brand-row{display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding:.4rem 0 2.2rem 0; animation:fadeDown .6s ease both;}
.brand-mark{display:flex; align-items:center; gap:.8rem;}
.brand-logo{width:44px; height:44px; border-radius:13px; background:var(--ink);
  display:flex; align-items:center; justify-content:center; color:#fff; flex:none; box-shadow:var(--shadow-sm);}
.brand-logo svg{width:22px; height:22px;}
.brand-name{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.45rem; color:var(--ink); line-height:1;}
.brand-name b{color:var(--ink); font-weight:800;}
.brand-right{display:flex; align-items:center; gap:.8rem;}
.live-badge{display:inline-flex; align-items:center; gap:.5rem; font-size:.78rem; font-weight:700;
  color:var(--ink2); background:var(--surface); border:1px solid var(--line); border-radius:30px; padding:.45rem .95rem; box-shadow:var(--shadow-sm);}
.live-badge .dot{width:8px; height:8px; border-radius:50%; background:#16A34A; animation:pulse 1.8s infinite;}
.live-badge.off{color:#991B1B; background:#FEF2F2; border-color:#FECACA;}
.live-badge.off .dot{background:#DC2626; animation:none;}
.brand-time{font-size:.78rem; color:var(--muted); font-weight:600;}

/* عناوين الأقسام */
.sec-head{display:flex; align-items:center; gap:.75rem; margin:2.8rem 0 1.3rem 0;}
.sec-head h2{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.2rem; color:var(--ink); margin:0;}
.sec-head .line{flex:1; height:1px; background:var(--line);}
.sec-head .idx{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--muted);
  background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:3px 10px; font-size:.78rem; box-shadow:var(--shadow-sm);}

/* بطاقة الأونصة — النص موسَّط */
.hero-card{position:relative; border-radius:24px; padding:2.4rem 2rem; overflow:hidden; text-align:center;
  background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow); animation:fadeUp .7s ease both;}
.hero-card::after{content:""; position:absolute; left:50%; top:-90px; transform:translateX(-50%);
  width:340px; height:200px; background:radial-gradient(circle, rgba(24,24,27,.05), transparent 70%); pointer-events:none;}
.hero-kicker{font-size:.82rem; letter-spacing:.4px; color:var(--muted); font-weight:700; margin-bottom:1rem; text-align:center;}
.hero-big{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; line-height:.95;
  font-size:clamp(3rem,9vw,5.4rem); color:var(--ink); letter-spacing:-2px; font-variant-numeric:tabular-nums; text-align:center;}
.hero-cur{display:inline-block; font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1rem;
  color:var(--ink2); background:var(--line2); border:1px solid var(--line); border-radius:9px;
  padding:.18rem .65rem; margin-inline-start:.6rem; vertical-align:middle;}
.hero-sar{margin-top:1rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:1.35rem;
  color:var(--ink2); font-variant-numeric:tabular-nums; text-align:center;}
.hero-sar .u{font-family:'Tajawal',sans-serif; font-size:.84rem; color:var(--muted); font-weight:600; margin-inline-start:.4rem;}
.hero-meta{margin:1.2rem auto 0; padding-top:1rem; max-width:420px; border-top:1px dashed var(--line);
  font-size:.82rem; color:var(--muted); text-align:center;}
.hero-meta b{color:var(--ink2); font-weight:700;}

/* بطاقات الأعيرة */
.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:16px;}
.kcard{position:relative; border-radius:var(--r); padding:1.5rem 1.45rem 1.55rem; text-align:right;
  background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow-sm);
  transition:transform .3s cubic-bezier(.2,.8,.2,1), box-shadow .3s, border-color .3s; animation:fadeUp .6s ease both;}
.kcard:hover{transform:translateY(-5px); box-shadow:var(--shadow); border-color:#DCDCDC;}
.kcard:hover .ic{transform:scale(1.06) rotate(-3deg);}
.ic{width:42px; height:42px; border-radius:13px; display:flex; align-items:center; justify-content:center;
  background:var(--line2); color:var(--ink); margin-bottom:1rem;
  transition:transform .3s cubic-bezier(.2,.8,.2,1);}
.ic svg{width:21px; height:21px;}
.k-label{font-family:'Cairo',sans-serif; font-size:.98rem; color:var(--ink2); font-weight:700; margin-bottom:.55rem;}
.k-value{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1.6rem; color:var(--ink);
  line-height:1.05; font-variant-numeric:tabular-nums; letter-spacing:-.5px;}
.k-cur{display:inline-block; font-family:'Tajawal',sans-serif; font-size:.7rem; font-weight:700; color:var(--ink2);
  background:var(--line2); border-radius:6px; padding:1px 6px; margin-inline-start:.35rem; vertical-align:middle;}
.k-usd{margin-top:.5rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:.94rem;
  color:var(--muted); font-variant-numeric:tabular-nums;}
.k-usd .u{font-size:.7rem; color:var(--muted); margin-inline-start:.25rem;}
/* البطاقة السوداء — بلا إطار، ظل ناعم موحّد */
.kcard.feature{background:var(--ink); border:1px solid transparent; box-shadow:var(--shadow);}
.kcard.feature:hover{border-color:transparent; box-shadow:0 18px 40px -18px rgba(24,24,27,.4);}
.kcard.feature .ic{background:rgba(255,255,255,.14); color:#fff;}
.kcard.feature .k-label{color:#D4D4D8;}
.kcard.feature .k-value{color:#fff;}
.kcard.feature .k-cur{background:rgba(255,255,255,.16); color:#fff;}
.kcard.feature .k-usd{color:#A1A1AA;}
.kcard.feature .k-usd .u{color:#71717A;}

.diag{border:1px solid #FECACA; border-radius:var(--r); padding:1.2rem 1.3rem; margin-top:1rem; background:#FEF2F2; animation:reveal .5s ease both;}
.diag h3{font-family:'Cairo',sans-serif; color:#B91C1C; margin:0 0 .5rem 0; font-size:1rem;}
.diag .d-row{display:flex; justify-content:space-between; gap:1rem; padding:.3rem 0; font-size:.82rem; color:#7F1D1D; border-bottom:1px dashed #FECACA;}
.diag .fail{color:#DC2626; white-space:nowrap;}

.foot{text-align:center !important; color:var(--muted); font-size:.78rem; margin:3.2rem 0 .2rem 0; line-height:1.8;}
.foot .sep{color:var(--ink2); margin:0 .5rem;}

@media (max-width:900px){ .stat-grid{grid-template-columns:repeat(2,1fr);} }
@media (max-width:768px){
  [data-testid="stMainBlockContainer"]{padding:8px 16px 34px !important; max-width:100% !important;}
  .brand-time{display:none;}
  .hero-card{padding:2rem 1.3rem;}
}
@media (max-width:420px){
  .stat-grid{grid-template-columns:1fr 1fr; gap:12px;}
  .k-value{font-size:1.35rem;} .kcard{padding:1.15rem;}
}

@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(22,163,74,.45);}70%{box-shadow:0 0 0 7px rgba(22,163,74,0);}100%{box-shadow:0 0 0 0 rgba(22,163,74,0);}}
@keyframes fadeUp{from{opacity:0; transform:translateY(16px);}to{opacity:1; transform:none;}}
@keyframes fadeDown{from{opacity:0; transform:translateY(-12px);}to{opacity:1; transform:none;}}
@keyframes reveal{from{opacity:0; transform:translateY(10px);}to{opacity:1; transform:none;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
