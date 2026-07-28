# theme.py — لوحة أسعار ذهب: سطح أبيض عائم على رمادي شبكي، RTL، متجاوبة، تباين صارم
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&family=Tajawal:wght@400;500;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton {display:none !important;}
[data-testid="stToolbar"]{display:none !important;}
.st-emotion-cache-1v0mbdj, [data-testid="stDecoration"]{display:none !important;}

:root{
  --bg:#E9E9EC; --surface:#FFFFFF; --ink:#18181B; --ink2:#3F3F46;
  --muted:#6B7280; --line:#E4E4E7; --line2:#F4F4F5;
  --gold:#9C7A1E; --gold-soft:#F6E7C1; --gold-ink:#7A5A12;
  --green:#15803D; --green-bg:#DCFCE7;
  --shadow:0 1px 2px rgba(16,16,20,.04), 0 16px 40px -18px rgba(16,16,20,.16);
  --shadow-sm:0 1px 2px rgba(16,16,20,.05), 0 6px 18px -10px rgba(16,16,20,.14);
  --r:18px;
}

html, body, .stApp {direction:rtl; text-align:right;}
[data-testid="stAppViewContainer"], section.main, [data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"] {direction:rtl;}

html, body, .stApp {background:var(--bg) !important; color:var(--ink);
  font-family:'Tajawal','Plus Jakarta Sans',sans-serif; -webkit-font-smoothing:antialiased;}
.stApp{background:transparent !important;}
.stApp::before{content:""; position:fixed; inset:0; z-index:-2; background:var(--bg);}
.stApp::after{content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background-image:
    radial-gradient(820px 420px at 82% -6%, rgba(156,122,30,.10), transparent 60%),
    linear-gradient(rgba(24,24,27,.028) 1px, transparent 1px),
    linear-gradient(90deg, rgba(24,24,27,.028) 1px, transparent 1px);
  background-size:auto, 46px 46px, 46px 46px;
  -webkit-mask-image:radial-gradient(130% 95% at 50% 0%, #000 30%, transparent 82%);
          mask-image:radial-gradient(130% 95% at 50% 0%, #000 30%, transparent 82%);}

[data-testid="stMainBlockContainer"]{
  background:var(--surface) !important; border-radius:26px !important;
  box-shadow:var(--shadow) !important; max-width:1180px !important;
  margin:24px auto !important; padding:24px 32px 38px !important;
  border:1px solid #FFFFFF !important;}

/* الترويسة */
.brand-row{display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding:.1rem 0 1.6rem 0; animation:fadeDown .6s ease both;}
.brand-mark{display:flex; align-items:center; gap:.7rem;}
.brand-diamond{width:36px; height:36px; transform:rotate(45deg); border-radius:10px;
  background:linear-gradient(135deg,#E8C77A,#C9A227 50%,#9C7A1E); box-shadow:0 6px 16px rgba(156,122,30,.34);}
.brand-name{font-family:'Cairo',sans-serif; font-weight:800; font-size:1.45rem; color:var(--ink); line-height:1;}
.brand-name b{color:var(--gold);}
.brand-right{display:flex; align-items:center; gap:.7rem;}
.live-badge{display:inline-flex; align-items:center; gap:.5rem; font-size:.78rem; font-weight:700;
  color:var(--ink2); background:var(--line2); border:1px solid var(--line); border-radius:30px; padding:.42rem .9rem;}
.live-badge .dot{width:8px; height:8px; border-radius:50%; background:var(--green); animation:pulse 1.8s infinite;}
.live-badge.off{color:#991B1B; background:#FEF2F2; border-color:#FECACA;}
.live-badge.off .dot{background:#DC2626; animation:none;}
.brand-tag{font-size:.7rem; color:var(--muted); letter-spacing:2px; font-weight:700;}

/* عناوين الأقسام */
.sec-head{display:flex; align-items:center; gap:.7rem; margin:2.4rem 0 1.1rem 0;}
.sec-head h2{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.2rem; color:var(--ink); margin:0;}
.sec-head .line{flex:1; height:1px; background:var(--line);}
.sec-head .idx{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--muted);
  background:var(--line2); border:1px solid var(--line); border-radius:8px; padding:2px 9px; font-size:.78rem;}

/* البطل: بطاقة سعر كبيرة + بطاقة نبض */
.hero-grid{display:grid; grid-template-columns:1.65fr 1fr; gap:16px; align-items:stretch;}
.hero-card{position:relative; border-radius:22px; padding:1.7rem 1.8rem; overflow:hidden;
  background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow); animation:fadeUp .7s ease both;}
.hero-card::after{content:""; position:absolute; inset-inline-end:-40px; top:-40px; width:180px; height:180px;
  background:radial-gradient(circle, rgba(156,122,30,.10), transparent 70%); pointer-events:none;}
.hero-kicker{font-size:.8rem; letter-spacing:.5px; color:var(--muted); font-weight:700; margin-bottom:.7rem;}
.hero-big{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; line-height:.95;
  font-size:clamp(2.6rem,7vw,4.4rem); color:var(--ink); letter-spacing:-1.5px; font-variant-numeric:tabular-nums;}
.hero-cur{display:inline-block; font-family:'Tajawal',sans-serif; font-weight:700; font-size:1rem;
  color:var(--ink2); background:var(--line2); border:1px solid var(--line); border-radius:8px; padding:.1rem .55rem; margin-inline-start:.5rem; vertical-align:middle;}
.hero-usd{margin-top:.7rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:1.25rem;
  color:var(--gold); font-variant-numeric:tabular-nums;}
.hero-usd .u{font-family:'Tajawal',sans-serif; font-size:.82rem; color:var(--muted); font-weight:600; margin-inline-start:.35rem;}
.hero-meta{margin-top:1rem; padding-top:.9rem; border-top:1px dashed var(--line); font-size:.82rem; color:var(--muted);}
.hero-meta b{color:var(--ink2); font-weight:700;}

/* بطاقة النبض (bar chart حقيقي) */
.pulse-card{display:flex; flex-direction:column; border-radius:22px; padding:1.5rem 1.6rem;
  background:var(--ink); color:#fff; box-shadow:0 18px 40px -18px rgba(24,24,27,.6); animation:fadeUp .75s ease both;}
.pulse-head{display:flex; align-items:center; justify-content:space-between; margin-bottom:1.1rem;}
.pulse-head h3{font-family:'Cairo',sans-serif; font-weight:700; font-size:1rem; margin:0; color:#fff;}
.pulse-head .hint{font-size:.72rem; color:#A1A1AA; font-weight:600;}
.bars{flex:1; display:flex; align-items:flex-end; gap:12px; min-height:120px; direction:rtl;}
.bar-col{flex:1; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; height:100%; gap:.5rem;}
.bar{width:100%; max-width:34px; border-radius:8px 8px 4px 4px; transform-origin:bottom;
  background:linear-gradient(180deg,#E8C77A,#C9A227); animation:grow .9s cubic-bezier(.2,.8,.2,1) both;
  transition:filter .25s, transform .25s;}
.bar-col:hover .bar{filter:brightness(1.12); transform:scaleY(1.04);}
.bar-col.feat .bar{background:linear-gradient(180deg,#FFFFFF,#D4D4D8);}
.bar-lbl{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:.74rem; color:#D4D4D8;}
.bar-col.feat .bar-lbl{color:#fff;}

/* صف بطاقات الأعيرة */
.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:14px;}
.kcard{position:relative; border-radius:var(--r); padding:1.15rem 1.2rem 1.2rem; background:var(--surface);
  border:1px solid var(--line); box-shadow:var(--shadow-sm);
  transition:transform .3s cubic-bezier(.2,.8,.2,1), box-shadow .3s, border-color .3s; animation:fadeUp .6s ease both;}
.kcard:hover{transform:translateY(-4px); box-shadow:var(--shadow); border-color:#D4D4D8;}
.ic{width:40px; height:40px; border-radius:12px; display:flex; align-items:center; justify-content:center;
  background:var(--line2); color:var(--gold); margin-bottom:.9rem;}
.ic svg{width:20px; height:20px;}
.k-label{font-size:.82rem; color:var(--ink2); font-weight:600; margin-bottom:.35rem;}
.k-value{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1.5rem; color:var(--ink);
  line-height:1.05; font-variant-numeric:tabular-nums; letter-spacing:-.5px;}
.k-cur{display:inline-block; font-family:'Tajawal',sans-serif; font-size:.7rem; font-weight:700; color:var(--ink2);
  background:var(--line2); border-radius:6px; padding:1px 6px; margin-inline-start:.35rem; vertical-align:middle;}
.k-usd{margin-top:.4rem; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:.92rem;
  color:var(--gold); font-variant-numeric:tabular-nums;}
.k-usd .u{font-size:.7rem; color:var(--muted); margin-inline-start:.25rem;}
.kcard.feature{background:var(--ink); border-color:var(--ink); box-shadow:0 16px 34px -16px rgba(24,24,27,.55);}
.kcard.feature:hover{border-color:var(--ink);}
.kcard.feature .ic{background:rgba(255,255,255,.12); color:#E8C77A;}
.kcard.feature .k-label{color:#D4D4D8;}
.kcard.feature .k-value{color:#fff;}
.kcard.feature .k-cur{background:rgba(255,255,255,.14); color:#fff;}
.kcard.feature .k-usd{color:#E8C77A;}
.kcard.feature .k-usd .u{color:#A1A1AA;}
.crown{position:absolute; top:1rem; inset-inline-start:1.1rem; font-size:.58rem; letter-spacing:.5px; font-weight:800;
  color:#1A1306; background:#E8C77A; padding:3px 8px; border-radius:20px;}

/* التخطيط الأوسط */
.mid-grid{display:grid; grid-template-columns:1.7fr 1fr; gap:16px; align-items:start;}
.panel{border-radius:var(--r); background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow-sm); animation:fadeUp .7s ease both;}
.panel-head{display:flex; align-items:center; justify-content:space-between; padding:1.1rem 1.3rem; border-bottom:1px solid var(--line2);}
.panel-head h3{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.02rem; color:var(--ink); margin:0;}
.panel-head .hint{font-size:.74rem; color:var(--muted); font-weight:600;}

.tbl-wrap{overflow-x:auto;}
table.gold{width:100%; border-collapse:collapse; font-size:.92rem;}
table.gold thead th{text-align:start; color:var(--ink2); font-weight:700; font-size:.76rem; letter-spacing:.3px;
  padding:.85rem 1.3rem; background:var(--line2); white-space:nowrap;}
table.gold tbody td{padding:.95rem 1.3rem; border-bottom:1px solid var(--line2); color:var(--ink); white-space:nowrap;}
table.gold tbody tr{transition:background .2s; animation:fadeUp .5s ease both;}
table.gold tbody tr:hover{background:var(--line2);}
table.gold tbody tr:last-child td{border-bottom:none;}
.td-karat{font-family:'Cairo',sans-serif; font-weight:700;}
.td-num{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-variant-numeric:tabular-nums;}
.td-sar{color:var(--ink);}
.td-usd{color:var(--gold);}
.td-pur{color:var(--ink2); font-weight:600;}

.pill{display:inline-block; font-size:.7rem; font-weight:700; padding:3px 10px; border-radius:20px; white-space:nowrap;}
.pill.gray{background:var(--line2); color:var(--ink2);}
.pill.gold{background:var(--gold-soft); color:var(--gold-ink);}
.pill.green{background:var(--green-bg); color:var(--green);}

.srow{display:flex; align-items:center; gap:.8rem; padding:.95rem 1.3rem; border-bottom:1px solid var(--line2); animation:fadeUp .5s ease both;}
.srow:last-child{border-bottom:none;}
.s-ic{flex:none; width:34px; height:34px; border-radius:10px; background:var(--line2); color:var(--gold);
  display:flex; align-items:center; justify-content:center;}
.s-ic svg{width:17px; height:17px;}
.s-ic.on{background:var(--green-bg); color:var(--green);}
.s-txt{flex:1; min-width:0;}
.s-title{font-size:.86rem; font-weight:700; color:var(--ink);}
.s-sub{font-size:.76rem; color:var(--ink2); margin-top:1px;}

.diag{border:1px solid #FECACA; border-radius:var(--r); padding:1.2rem 1.3rem; margin-top:1rem; background:#FEF2F2; animation:reveal .5s ease both;}
.diag h3{font-family:'Cairo',sans-serif; color:#B91C1C; margin:0 0 .5rem 0; font-size:1rem;}
.diag .d-row{display:flex; justify-content:space-between; gap:1rem; padding:.3rem 0; font-size:.82rem; color:#7F1D1D; border-bottom:1px dashed #FECACA;}
.diag .fail{color:#DC2626; white-space:nowrap;}

.foot{text-align:center; color:var(--muted); font-size:.78rem; margin:2.6rem 0 .2rem 0; line-height:1.8;}
.foot .sep{color:var(--gold); margin:0 .5rem;}

@media (max-width:900px){
  .hero-grid{grid-template-columns:1fr;}
  .mid-grid{grid-template-columns:1fr;}
  .stat-grid{grid-template-columns:repeat(2,1fr);}
}
@media (max-width:768px){
  [data-testid="stMainBlockContainer"]{border-radius:0 !important; margin:0 !important; padding:18px 15px 30px !important; max-width:100% !important;}
  .brand-tag{display:none;}
  .th-note, .td-note{display:none;}
}
@media (max-width:420px){
  .stat-grid{grid-template-columns:1fr 1fr; gap:10px;}
  .k-value{font-size:1.3rem;}
  .kcard{padding:1rem;}
  .bars{min-height:96px; gap:8px;}
}

@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(21,128,61,.45);}70%{box-shadow:0 0 0 7px rgba(21,128,61,0);}100%{box-shadow:0 0 0 0 rgba(21,128,61,0);}}
@keyframes fadeUp{from{opacity:0; transform:translateY(16px);}to{opacity:1; transform:none;}}
@keyframes fadeDown{from{opacity:0; transform:translateY(-12px);}to{opacity:1; transform:none;}}
@keyframes reveal{from{opacity:0; transform:translateY(10px);}to{opacity:1; transform:none;}}
@keyframes grow{from{transform:scaleY(0); opacity:0;}to{transform:scaleY(1); opacity:1;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
