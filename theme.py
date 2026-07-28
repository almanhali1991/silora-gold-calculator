# theme.py — لوحة عاجية دافئة بلمسة ذهبية | RTL | متجاوبة | تباين صارم | بدون أي كلمة تحريرية
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@500;600;700&family=Tajawal:wght@400;500;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton, [data-testid="stAppDeployButton"] {display:none !important;}
[data-testid="stToolbar"]{display:none !important;}
[data-testid="stDecoration"]{display:none !important;}
footer, [data-testid="stFooter"]{visibility:hidden !important; display:none !important;}

:root{
  --bg1:#FBF8F1; --bg2:#F3EAD8; --surface:#FFFFFF; --surface2:#FFFDF8;
  --ink:#2B2620; --ink2:#5C5347; --muted:#8A7F6E;
  --line:#EADFC9; --line2:#F6EFE0;
  --gold:#8A6D1F; --gold-line:#C9A227; --gold-soft:#F3E7C4; --gold-ink:#6E5614;
  --shadow:0 1px 2px rgba(80,60,20,.05), 0 18px 44px -20px rgba(120,90,25,.22);
  --shadow-sm:0 1px 2px rgba(80,60,20,.05), 0 8px 22px -14px rgba(120,90,25,.20);
  --r:18px;
}

html, body, .stApp {direction:rtl; text-align:right;}
[data-testid="stAppViewContainer"], section.main, [data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"] {direction:rtl;}

html, body, .stApp {background:linear-gradient(180deg,var(--bg1),var(--bg2)) !important; color:var(--ink);
  font-family:'Tajawal','Plus Jakarta Sans',sans-serif; -webkit-font-smoothing:antialiased; min-height:100vh;}
.stApp{background:transparent !important;}
.stApp::after{content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background:radial-gradient(760px 380px at 50% -8%, rgba(201,162,39,.14), transparent 62%);}

[data-testid="stMainBlockContainer"]{
  background:var(--surface) !important; border-radius:26px !important;
  box-shadow:var(--shadow) !important; max-width:1120px !important;
  margin:26px auto !important; padding:26px 34px 40px !important;
  border:1px solid #FFFFFF !important;}

/* الترويسة */
.brand-row{display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding:.1rem 0 1.7rem 0; animation:fadeDown .6s ease both;}
.brand-mark{display:flex; align-items:center; gap:.75rem;}
.brand-logo{width:42px; height:42px; border-radius:50%; background:var(--gold-soft);
  border:1.5px solid var(--gold-line); display:flex; align-items:center; justify-content:center;
  color:var(--gold); flex:none; box-shadow:inset 0 0 0 3px rgba(255,255,255,.6);}
.brand-logo svg{width:21px; height:21px;}
.brand-name{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.4rem; color:var(--ink); line-height:1;}
.brand-name b{color:var(--gold); font-weight:700;}
.brand-right{display:flex; align-items:center; gap:.7rem;}
.live-badge{display:inline-flex; align-items:center; gap:.5rem; font-size:.78rem; font-weight:700;
  color:var(--gold-ink); background:var(--gold-soft); border:1px solid var(--gold-line); border-radius:30px; padding:.42rem .9rem;}
.live-badge .dot{width:8px; height:8px; border-radius:50%; background:#15803D; animation:pulse 1.8s infinite;}
.live-badge.off{color:#991B1B; background:#FEF2F2; border-color:#FECACA;}
.live-badge.off .dot{background:#DC2626; animation:none;}
.brand-time{font-size:.78rem; color:var(--muted); font-weight:600;}

/* عناوين الأقسام */
.sec-head{display:flex; align-items:center; gap:.7rem; margin:2.4rem 0 1.1rem 0;}
.sec-head h2{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.18rem; color:var(--ink); margin:0;}
.sec-head .line{flex:1; height:1px; background:var(--line);}
.sec-head .idx{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--gold-ink);
  background:var(--gold-soft); border:1px solid var(--gold-line); border-radius:8px; padding:2px 9px; font-size:.78rem;}

/* بطاقة الأونصة */
.hero-card{position:relative; border-radius:22px; padding:1.9rem 2rem; overflow:hidden;
  background:linear-gradient(135deg,var(--surface2),#FFFFFF); border:1px solid var(--line);
  box-shadow:var(--shadow); animation:fadeUp .7s ease both;}
.hero-card::after{content:""; position:absolute; inset-inline-end:-50px; top:-60px; width:240px; height:240px;
  background:radial-gradient(circle, rgba(201,162,39,.16), transparent 70%); pointer-events:none;}
.hero-kicker{font-size:.82rem; letter-spacing:.4px; color:var(--muted); font-weight:700; margin-bottom:.9rem;}
.hero-big{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; line-height:.95;
  font-size:clamp(2.8rem,8vw,5rem); color:var(--ink); letter-spacing:-1.5px; font-variant-numeric:tabular-nums;}
.hero-cur{display:inline-block; font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:.95rem;
  color:var(--gold-ink); background:var(--gold-soft); border:1px solid var(--gold-line); border-radius:8px;
  padding:.15rem .6rem; margin-inline-start:.6rem; vertical-align:middle;}
.hero-sar{margin-top:.85rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:1.3rem;
  color:var(--ink2); font-variant-numeric:tabular-nums;}
.hero-sar .u{font-family:'Tajawal',sans-serif; font-size:.82rem; color:var(--muted); font-weight:600; margin-inline-start:.4rem;}
.hero-meta{margin-top:1.1rem; padding-top:.95rem; border-top:1px dashed var(--line); font-size:.82rem; color:var(--muted);}
.hero-meta b{color:var(--ink2); font-weight:700;}

/* بطاقات الأعيرة */
.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:14px;}
.kcard{position:relative; border-radius:var(--r); padding:1.25rem 1.3rem 1.3rem; background:var(--surface);
  border:1px solid var(--line); box-shadow:var(--shadow-sm);
  transition:transform .3s cubic-bezier(.2,.8,.2,1), box-shadow .3s, border-color .3s; animation:fadeUp .6s ease both;}
.kcard:hover{transform:translateY(-4px); box-shadow:var(--shadow); border-color:var(--gold-line);}
.crown{display:inline-block; font-size:.62rem; letter-spacing:.4px; font-weight:800; color:#FFFDF6;
  background:var(--gold); padding:3px 10px; border-radius:20px; margin-bottom:.7rem;}
.k-label{font-family:'Cairo',sans-serif; font-size:.95rem; color:var(--ink2); font-weight:700; margin-bottom:.5rem;}
.k-value{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1.55rem; color:var(--ink);
  line-height:1.05; font-variant-numeric:tabular-nums; letter-spacing:-.5px;}
.k-cur{display:inline-block; font-family:'Tajawal',sans-serif; font-size:.7rem; font-weight:700; color:var(--ink2);
  background:var(--line2); border-radius:6px; padding:1px 6px; margin-inline-start:.35rem; vertical-align:middle;}
.k-usd{margin-top:.45rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:.92rem;
  color:var(--gold); font-variant-numeric:tabular-nums;}
.k-usd .u{font-size:.7rem; color:var(--muted); margin-inline-start:.25rem;}
/* البطاقة المميزة = عيار 24 (ذهبية دافئة، لا سوداء) */
.kcard.feature{background:linear-gradient(150deg,#FBF3DD,#F6E9C6); border:1.5px solid var(--gold-line);
  box-shadow:0 16px 34px -16px rgba(138,109,31,.45);}
.kcard.feature:hover{border-color:var(--gold);}
.kcard.feature .k-label{color:var(--gold-ink);}
.kcard.feature .k-value{color:var(--ink);}
.kcard.feature .k-cur{background:rgba(255,255,255,.7); color:var(--gold-ink);}

/* الجدول الملخّص (3 أعمدة فقط) */
.panel{border-radius:var(--r); background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow-sm); animation:fadeUp .7s ease both; overflow:hidden;}
.tbl-wrap{overflow-x:auto;}
table.gold{width:100%; border-collapse:collapse; font-size:.95rem;}
table.gold thead th{text-align:start; color:var(--ink2); font-weight:700; font-size:.78rem; letter-spacing:.3px;
  padding:.95rem 1.4rem; background:var(--line2); white-space:nowrap;}
table.gold tbody td{padding:1.05rem 1.4rem; border-bottom:1px solid var(--line2); color:var(--ink); white-space:nowrap;}
table.gold tbody tr{transition:background .2s; animation:fadeUp .5s ease both;}
table.gold tbody tr:hover{background:var(--surface2);}
table.gold tbody tr:last-child td{border-bottom:none;}
.td-karat{font-family:'Cairo',sans-serif; font-weight:700;}
.td-num{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-variant-numeric:tabular-nums;}
.td-sar{color:var(--ink);}
.td-usd{color:var(--gold);}

.diag{border:1px solid #FECACA; border-radius:var(--r); padding:1.2rem 1.3rem; margin-top:1rem; background:#FEF2F2; animation:reveal .5s ease both;}
.diag h3{font-family:'Cairo',sans-serif; color:#B91C1C; margin:0 0 .5rem 0; font-size:1rem;}
.diag .d-row{display:flex; justify-content:space-between; gap:1rem; padding:.3rem 0; font-size:.82rem; color:#7F1D1D; border-bottom:1px dashed #FECACA;}
.diag .fail{color:#DC2626; white-space:nowrap;}

.foot{text-align:center; color:var(--muted); font-size:.78rem; margin:2.8rem 0 .2rem 0; line-height:1.8;}
.foot .sep{color:var(--gold-line); margin:0 .5rem;}

@media (max-width:900px){ .stat-grid{grid-template-columns:repeat(2,1fr);} }
@media (max-width:768px){
  [data-testid="stMainBlockContainer"]{border-radius:0 !important; margin:0 !important; padding:18px 15px 30px !important; max-width:100% !important;}
  .brand-time{display:none;}
}
@media (max-width:420px){
  .stat-grid{grid-template-columns:1fr 1fr; gap:10px;}
  .k-value{font-size:1.3rem;} .kcard{padding:1rem;}
}

@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(21,128,61,.45);}70%{box-shadow:0 0 0 7px rgba(21,128,61,0);}100%{box-shadow:0 0 0 0 rgba(21,128,61,0);}}
@keyframes fadeUp{from{opacity:0; transform:translateY(16px);}to{opacity:1; transform:none;}}
@keyframes fadeDown{from{opacity:0; transform:translateY(-12px);}to{opacity:1; transform:none;}}
@keyframes reveal{from{opacity:0; transform:translateY(10px);}to{opacity:1; transform:none;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
