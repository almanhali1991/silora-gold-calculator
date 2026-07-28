# theme.py — هوية فاتحة نظيفة: لوحة بيضاء عائمة على رمادي، RTL، متجاوبة
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&family=Tajawal:wght@400;500;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

#MainMenu, footer, header {visibility:hidden !important;}
.stAppDeployButton {display:none !important;}
[data-testid="stToolbar"]{display:none !important;}

:root{
  --bg:#E9E9EC; --surface:#FFFFFF; --ink:#18181B; --ink2:#3F3F46;
  --muted:#71717A; --line:#E4E4E7; --line2:#F4F4F5; --gold:#9C7A1E;
  --green:#15803D; --green-bg:#DCFCE7;
  --shadow:0 1px 2px rgba(16,16,20,.04), 0 14px 38px -16px rgba(16,16,20,.14);
  --shadow-sm:0 1px 2px rgba(16,16,20,.05), 0 4px 14px -8px rgba(16,16,20,.12);
  --r:18px;
}

/* RTL شامل */
html, body, .stApp {direction:rtl; text-align:right;}
[data-testid="stAppViewContainer"], section.main, [data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"] {direction:rtl;}

/* الخلفية الرمادية الفاتحة + نمط شبكي باهت كاللوحة المرجعية */
html, body, .stApp {background:var(--bg) !important; color:var(--ink);
  font-family:'Tajawal','Plus Jakarta Sans',sans-serif;}
.stApp{background:transparent !important;}
.stApp::before{content:""; position:fixed; inset:0; z-index:-1; pointer-events:none;
  background-color:var(--bg);
  background-image:
    linear-gradient(rgba(24,24,27,.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(24,24,27,.025) 1px, transparent 1px);
  background-size:46px 46px;
  -webkit-mask-image:radial-gradient(120% 90% at 50% 0%, #000 35%, transparent 80%);
          mask-image:radial-gradient(120% 90% at 50% 0%, #000 35%, transparent 80%);}

/* اللوحة البيضاء العائمة */
[data-testid="stMainBlockContainer"]{
  background:var(--surface) !important; border-radius:26px !important;
  box-shadow:var(--shadow) !important; max-width:1160px !important;
  margin:24px auto !important; padding:24px 32px 40px !important;
  border:1px solid rgba(255,255,255,.6) !important;}

/* الترويسة */
.brand-row{display:flex; align-items:center; justify-content:space-between; gap:1rem;
  padding:.1rem 0 1.5rem 0; animation:fadeDown .6s ease both;}
.brand-mark{display:flex; align-items:center; gap:.7rem;}
.brand-diamond{width:34px; height:34px; transform:rotate(45deg); border-radius:9px;
  background:linear-gradient(135deg,#E8C77A,#C9A227 50%,#9C7A1E); box-shadow:0 5px 14px rgba(156,122,30,.32);}
.brand-name{font-family:'Cairo',sans-serif; font-weight:800; font-size:1.4rem; color:var(--ink); line-height:1;}
.brand-name b{color:var(--gold);}
.brand-tag{font-size:.7rem; color:var(--muted); letter-spacing:2px; font-weight:700;}
.live-badge{display:inline-flex; align-items:center; gap:.45rem; font-size:.78rem; font-weight:700;
  color:var(--ink2); background:var(--line2); border:1px solid var(--line); border-radius:30px; padding:.4rem .85rem;}
.live-badge .dot{width:8px; height:8px; border-radius:50%; background:var(--green); animation:pulse 1.8s infinite;}
.live-badge.off .dot{background:#A1A1AA; animation:none;}

/* عناوين الأقسام */
.sec-head{display:flex; align-items:center; gap:.7rem; margin:2.2rem 0 1.1rem 0;}
.sec-head h2{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.2rem; color:var(--ink); margin:0;}
.sec-head .line{flex:1; height:1px; background:var(--line);}
.sec-head .idx{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:var(--muted);
  background:var(--line2); border:1px solid var(--line); border-radius:8px; padding:2px 9px; font-size:.78rem;}

/* صف البطاقات (Quick Stats) */
.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:14px;}
.kcard{position:relative; border-radius:var(--r); padding:1.15rem 1.2rem 1.25rem; background:var(--surface);
  border:1px solid var(--line); box-shadow:var(--shadow-sm);
  transition:transform .3s cubic-bezier(.2,.8,.2,1), box-shadow .3s, border-color .3s; animation:fadeUp .6s ease both;}
.kcard:hover{transform:translateY(-4px); box-shadow:var(--shadow); border-color:#D4D4D8;}
.ic{width:38px; height:38px; border-radius:11px; display:flex; align-items:center; justify-content:center;
  background:var(--line2); color:var(--ink); font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1rem;
  margin-bottom:.85rem;}
.k-label{font-size:.82rem; color:var(--ink2); font-weight:600; margin-bottom:.25rem;}
.k-value{font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:1.55rem; color:var(--ink);
  line-height:1.05; font-variant-numeric:tabular-nums; letter-spacing:-.5px;}
.k-unit{font-family:'Tajawal',sans-serif; font-size:.72rem; font-weight:600; color:var(--muted); margin-right:.3rem;}
/* البطاقة السوداء المميزة */
.kcard.feature{background:var(--ink); border-color:var(--ink); box-shadow:0 16px 34px -16px rgba(24,24,27,.55);}
.kcard.feature:hover{transform:translateY(-4px); border-color:var(--ink);}
.kcard.feature .ic{background:rgba(255,255,255,.12); color:#fff;}
.kcard.feature .k-label{color:#D4D4D8;}
.kcard.feature .k-value{color:#fff;}
.kcard.feature .k-unit{color:#A1A1AA;}
.crown{position:absolute; top:1rem; left:1.1rem; font-size:.58rem; letter-spacing:1px; font-weight:800;
  color:#1A1306; background:#E8C77A; padding:3px 8px; border-radius:20px;}

/* التخطيط الأوسط: جدول + بطاقة جانبية */
.mid-grid{display:grid; grid-template-columns:1.7fr 1fr; gap:16px; align-items:start;}
.panel{border-radius:var(--r); background:var(--surface); border:1px solid var(--line); box-shadow:var(--shadow-sm); animation:fadeUp .7s ease both;}
.panel-head{display:flex; align-items:center; justify-content:space-between; padding:1.1rem 1.3rem; border-bottom:1px solid var(--line2);}
.panel-head h3{font-family:'Cairo',sans-serif; font-weight:700; font-size:1.02rem; color:var(--ink); margin:0;}
.panel-head .hint{font-size:.74rem; color:var(--muted); font-weight:600;}

/* الجدول */
.tbl-wrap{overflow-x:auto;}
table.gold{width:100%; border-collapse:collapse; font-size:.92rem;}
table.gold thead th{text-align:right; color:var(--ink2); font-weight:700; font-size:.76rem; letter-spacing:.3px;
  padding:.85rem 1.3rem; background:var(--line2); white-space:nowrap;}
table.gold thead th:first-child{border-top-right-radius:0;}
table.gold tbody td{padding:.95rem 1.3rem; border-bottom:1px solid var(--line2); color:var(--ink); white-space:nowrap;}
table.gold tbody tr{transition:background .2s; animation:fadeUp .5s ease both;}
table.gold tbody tr:hover{background:var(--line2);}
table.gold tbody tr:last-child td{border-bottom:none;}
.td-karat{font-family:'Cairo',sans-serif; font-weight:700;}
.td-num{font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-variant-numeric:tabular-nums;}
.td-sar{color:var(--ink);}
.td-usd{color:var(--gold);}
.td-pur{color:var(--muted); font-weight:600;}

/* الشارات */
.pill{display:inline-block; font-size:.7rem; font-weight:700; padding:3px 10px; border-radius:20px; white-space:nowrap;}
.pill.gray{background:var(--line2); color:var(--ink2);}
.pill.gold{background:#F6E7C1; color:#7A5A12;}
.pill.green{background:var(--green-bg); color:var(--green);}

/* البطاقة الجانبية */
.srow{display:flex; align-items:center; gap:.8rem; padding:.95rem 1.3rem; border-bottom:1px solid var(--line2); animation:fadeUp .5s ease both;}
.srow:last-child{border-bottom:none;}
.s-ic{flex:none; width:34px; height:34px; border-radius:10px; background:var(--line2); color:var(--gold);
  display:flex; align-items:center; justify-content:center;}
.s-ic svg{width:17px; height:17px;}
.s-ic.on{background:var(--green-bg); color:var(--green);}
.s-txt{flex:1; min-width:0;}
.s-title{font-size:.86rem; font-weight:700; color:var(--ink);}
.s-sub{font-size:.76rem; color:var(--ink2); margin-top:1px;}

/* لوحة التشخيص */
.diag{border:1px solid #FECACA; border-radius:var(--r); padding:1.2rem 1.3rem; margin-top:1rem; background:#FEF2F2; animation:reveal .5s ease both;}
.diag h3{font-family:'Cairo',sans-serif; color:#B91C1C; margin:0 0 .5rem 0; font-size:1rem;}
.diag .d-row{display:flex; justify-content:space-between; gap:1rem; padding:.3rem 0; font-size:.82rem; color:#7F1D1D; border-bottom:1px dashed #FECACA;}
.diag .fail{color:#DC2626; white-space:nowrap;}

/* الفوتر */
.foot{text-align:center; color:var(--muted); font-size:.78rem; margin:2.6rem 0 .2rem 0; line-height:1.8;}
.foot .sep{color:var(--gold); margin:0 .5rem;}

/* التجاوب */
@media (max-width:900px){
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
}

@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(21,128,61,.45);}70%{box-shadow:0 0 0 7px rgba(21,128,61,0);}100%{box-shadow:0 0 0 0 rgba(21,128,61,0);}}
@keyframes fadeUp{from{opacity:0; transform:translateY(16px);}to{opacity:1; transform:none;}}
@keyframes fadeDown{from{opacity:0; transform:translateY(-12px);}to{opacity:1; transform:none;}}
@keyframes reveal{from{opacity:0; transform:translateY(10px);}to{opacity:1; transform:none;}}
"""

def inject():
    import streamlit as st
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
