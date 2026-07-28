# تطبيق حاسبة أسعار الذهب بواجهة Streamlit
# سيلورا جولد

import streamlit as st
import requests
from datetime import datetime, timezone, timedelta

# ===== الثوابت =====
OUNCE_TO_GRAM = 31.1034768
USD_TO_SAR = 3.75
API_URL = "https://api.gold-api.com/price/XAU/USD "
RIYADH_TZ = timezone(timedelta(hours=3))  # توقيت الرياض UTC+3

# معاملات نقاء الأعيرة
KARAT_FACTORS = {
    "عيار 24": 1.000,
    "عيار 22": 0.916,
    "عيار 21": 0.875,
    "عيار 18": 0.750,
}

# ===== تنسيقات التصميم الراقي البسيط =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #FFFFFF; }
    .brand-title { font-size: 3rem; font-weight: 800; color: #1A1A1A; text-align: center; margin-bottom: 0; }
    .brand-subtitle { font-size: 1.1rem; color: #6B7280; text-align: center; margin-top: 0; }
    .gold-divider { height: 2px; background: linear-gradient(90deg, transparent, #C9A227, transparent); margin: 1rem auto 2rem auto; width: 60%; }
    .section-title { font-size: 1.3rem; font-weight: 700; color: #1A1A1A; margin-top: 1.5rem; margin-bottom: 0.5rem; }
    .price-card { background-color: #FAFAFA; border: 1px solid #E5E7EB; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .price-card-featured { background-color: #FFFDF5; border: 2px solid #C9A227; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(201,162,39,0.15); }
    .karat-name { font-size: 0.95rem; color: #6B7280; font-weight: 500; }
    .karat-price { font-size: 1.6rem; font-weight: 800; color: #1A1A1A; margin-top: 0.3rem; }
    .badge-popular { display: inline-block; background-color: #C9A227; color: white; font-size: 0.7rem; padding: 2px 8px; border-radius: 10px; margin-bottom: 0.4rem; }
    .update-time { text-align: center; color: #9CA3AF; font-size: 0.85rem; margin-top: 1rem; }
    .invoice-box { background-color: #FAFAFA; border: 1px solid #E5E7EB; border-radius: 12px; padding: 1.5rem; margin-top: 1rem; }
    .invoice-box table { width: 100%; border-collapse: collapse; }
    .invoice-box td { padding: 8px 4px; color: #1A1A1A; font-size: 1rem; }
    .invoice-box td:last-child { text-align: left; font-weight: 500; }
    .final-price { font-size: 2rem; font-weight: 800; color: #C9A227; text-align: center; }
    .footer-text { text-align: center; color: #9CA3AF; font-size: 0.85rem; margin-top: 3rem; }
</style>
""", unsafe_allow_html=True)

# ===== دالة جلب السعر الحي =====
@st.cache_data(ttl=60)
def get_gold_price():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        price_per_ounce_usd = data["price"]
        updated_at = data.get("updatedAt", "")
        price_per_gram_usd = price_per_ounce_usd / OUNCE_TO_GRAM
        price_per_gram_24_sar = price_per_gram_usd * USD_TO_SAR
        update_time_str = ""
        if updated_at:
            try:
                updated_dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00")).astimezone(RIYADH_TZ)
                update_time_str = updated_dt.strftime("%I:%M %p")
            except Exception:
                update_time_str = ""
        return price_per_gram_24_sar, update_time_str, None
    except requests.exceptions.RequestException as e:
        return None, None, str(e)

# ===== الهيدر =====
st.markdown('<div class="brand-title">سيلورا جولد</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-subtitle">حاسبة أسعار الذهب — أسعار محدثة لحظياً بالريال السعودي</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ===== جلب السعر =====
price_24, update_time, error = get_gold_price()
if error:
    st.error("تعذر جلب السعر العالمي، يرجى التحقق من اتصال الإنترنت.")
    st.stop()

# ===== لوحة الأسعار =====
st.markdown('<div class="section-title">أسعار الجرام اليوم</div>', unsafe_allow_html=True)
cols = st.columns(4)
karat_list = ["عيار 24", "عيار 22", "عيار 21", "عيار 18"]
for i, karat in enumerate(karat_list):
    gram_price = price_24 * KARAT_FACTORS[karat]
    with cols[i]:
        if karat == "عيار 21":
            card = f'<div class="price-card-featured"><div class="badge-popular">الأكثر تداولاً</div><div class="karat-name">{karat}</div><div class="karat-price">{gram_price:,.2f}</div><div class="karat-name">ريال سعودي</div></div>'
        else:
            card = f'<div class="price-card"><div class="karat-name">{karat}</div><div class="karat-price">{gram_price:,.2f}</div><div class="karat-name">ريال سعودي</div></div>'
        st.markdown(card, unsafe_allow_html=True)

if update_time:
    st.markdown(f'<div class="update-time">آخر تحديث: {update_time} بتوقيت الرياض</div>', unsafe_allow_html=True)

# ===== نموذج الحساب =====
st.markdown('<div class="section-title">احسب قيمة قطعتك</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("الوزن (جرام)", min_value=0.1, value=10.0, step=0.1)
    karat_choice = st.selectbox("العيار", list(KARAT_FACTORS.keys()), index=2)
with col2:
    operation = st.radio("نوع العملية", ["شراء", "بيع"], horizontal=True)
    if operation == "شراء":
        workmanship = st.number_input("المصنعية (ريال)", min_value=0.0, value=50.0, step=10.0)
    else:
        workmanship = 0.0
        st.caption("عند البيع تُحتسب قيمة الذهب الخام فقط دون مصنعية.")

# ===== زر الحساب والنتيجة =====
if st.button("احسب القيمة", type="primary", use_container_width=True):
    price_per_gram_karat = price_24 * KARAT_FACTORS[karat_choice]
    raw_gold = weight * price_per_gram_karat
    final_price = raw_gold + workmanship
    rows = f"""
    <tr><td>العيار</td><td>{karat_choice}</td></tr>
    <tr><td>الوزن</td><td>{weight:.2f} جرام</td></tr>
    <tr><td>سعر الجرام</td><td>{price_per_gram_karat:,.2f} ريال</td></tr>
    <tr><td>قيمة الذهب الخام</td><td>{raw_gold:,.2f} ريال</td></tr>
    """
    if operation == "شراء":
        rows += f"<tr><td>المصنعية</td><td>{workmanship:,.2f} ريال</td></tr>"
    invoice = f'''
    <div class="invoice-box">
        <table>{rows}</table>
        <hr style="border: none; border-top: 1px solid #E5E7EB; margin: 1rem 0;">
        <div class="final-price">{final_price:,.2f} ريال سعودي</div>
    </div>
    '''
    st.markdown(invoice, unsafe_allow_html=True)

# ===== الفوتر =====
st.markdown('<div class="footer-text">© 2026 سيلورا جولد — جميع الحقوق محفوظة<br>الأسعار استرشادية وفق السوق العالمي وقد تختلف عن أسعار المتجر</div>', unsafe_allow_html=True)
