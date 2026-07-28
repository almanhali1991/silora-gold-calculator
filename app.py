import streamlit as st
import requests
from datetime import datetime
import pytz

# الثوابت
OUNCE_TO_GRAM = 31.1034768
USD_TO_SAR = 3.75
CACHE_TTL = 60

# معاملات الأعيرة
CARAT_FACTORS = {
    24: 1.000,
    22: 0.916,
    21: 0.875,
    18: 0.750
}

# دالة جلب سعر الذهب مع التخزين المؤقت
@st.cache_data(ttl=CACHE_TTL)
def get_gold_price():
    try:
        response = requests.get("https://api.gold-api.com/price/XAU/USD")
        data = response.json()
        return data['price'], data['updatedAt']
    except Exception as e:
        return None, None

# دالة تحويل الوقت إلى توقيت الرياض
def convert_to_riyadh_time(updated_at_str):
    try:
        utc_time = datetime.fromisoformat(updated_at_str.replace('Z', '+00:00'))
        utc_zone = pytz.UTC
        utc_time = utc_time.astimezone(utc_zone)
        riyadh_tz = pytz.timezone('Asia/Riyadh')
        riyadh_time = utc_time.astimezone(riyadh_tz)
        hour = riyadh_time.strftime('%I').lstrip('0') or '12'
        minute = riyadh_time.strftime('%M')
        period = "ص" if riyadh_time.hour < 12 else "م"
        return f"{hour}:{minute} {period}"
    except:
        return "غير متوفر"

# تطبيق CSS للتصميم
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700&display=swap');

* {
    font-family: 'Tajawal', sans-serif !important;
}

body {
    background-color: #FFFFFF;
    color: #1A1A1A;
}

h1, h2, h3, h4, h5, h6 {
    color: #1A1A1A !important;
}

.stApp {
    background-color: #FFFFFF;
}

#MainMenu, footer, header, .viewerBadge_container__1QSdy {
    visibility: hidden !important;
    display: none !important;
}

hr {
    border-color: #C9A227 !important;
    margin: 1rem 0;
}

.price-card {
    background-color: #FAFAFA;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    height: 100%;
}

.highlighted-card {
    border: 2px solid #C9A227 !important;
    position: relative;
}

.popular-badge {
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #C9A227;
    color: white;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: bold;
}

.result-card {
    background-color: #FAFAFA;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 1rem;
}

.calculation-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}

.calculation-table td {
    padding: 10px;
    text-align: right;
    border-bottom: 1px solid #F0F0F0;
}

.calculation-table tr:last-child td {
    border-bottom: none;
}

.final-price {
    color: #C9A227 !important;
    font-size: 1.5rem !important;
    font-weight: bold !important;
}

.stButton>button {
    background-color: #C9A227 !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.5rem 1rem !important;
    font-weight: bold !important;
    width: 100% !important;
}

.stRadio>label {
    font-weight: bold;
}

.info-message {
    background-color: #F3F4F6;
    padding: 0.8rem;
    border-radius: 6px;
    color: #6B7280;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# إعداد الصفحة
st.set_page_config(page_title="سيلورا جولد", page_icon="💎", layout="centered")

# جلب البيانات
gold_price, updated_at = get_gold_price()

if gold_price:
    # حساب أسعار الجرام حسب العيار
    price_per_gram_24 = (gold_price / OUNCE_TO_GRAM) * USD_TO_SAR
    prices = {}
    for carat, factor in CARAT_FACTORS.items():
        prices[carat] = price_per_gram_24 * factor

    # الهيدر
    st.markdown("<h1 style='text-align: center; margin-bottom: 0.5rem;'>سيلورا جولد</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6B7280; margin-bottom: 1.5rem;'>حاسبة أسعار الذهب — أسعار محدثة لحظياً بالريال السعودي</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # لوحة الأسعار
    st.markdown("<h3 style='color: #1A1A1A; margin-bottom: 1rem;'>أسعار الجرام اليوم</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="price-card">
            <div style="font-size: 0.85rem; color: #6B7280; margin-bottom: 0.5rem;">عيار 24</div>
            <div style="font-size: 1.4rem; font-weight: bold; color: #1A1A1A;">{prices[24]:,.2f}</div>
            <div style="font-size: 0.75rem; color: #9CA3AF;">ريال سعودي</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="price-card highlighted-card">
            <div class="popular-badge">الأكثر تداولاً</div>
            <div style="font-size: 0.85rem; color: #6B7280; margin-bottom: 0.5rem;">عيار 21</div>
            <div style="font-size: 1.4rem; font-weight: bold; color: #1A1A1A;">{prices[21]:,.2f}</div>
            <div style="font-size: 0.75rem; color: #9CA3AF;">ريال سعودي</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="price-card">
            <div style="font-size: 0.85rem; color: #6B7280; margin-bottom: 0.5rem;">عيار 22</div>
            <div style="font-size: 1.4rem; font-weight: bold; color: #1A1A1A;">{prices[22]:,.2f}</div>
            <div style="font-size: 0.75rem; color: #9CA3AF;">ريال سعودي</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="price-card">
            <div style="font-size: 0.85rem; color: #6B7280; margin-bottom: 0.5rem;">عيار 18</div>
            <div style="font-size: 1.4rem; font-weight: bold; color: #1A1A1A;">{prices[18]:,.2f}</div>
            <div style="font-size: 0.75rem; color: #9CA3AF;">ريال سعودي</div>
        </div>
        """, unsafe_allow_html=True)
    
    # عرض وقت التحديث
    update_time_arabic = convert_to_riyadh_time(updated_at)
    st.markdown(f"<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem; margin: 1.5rem 0;'>آخر تحديث: {update_time_arabic}</p>", unsafe_allow_html=True)

    # فاصل
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

    # نموذج الحساب
    st.markdown("<h3 style='color: #1A1A1A; margin-bottom: 1rem;'>احسب قيمة قطعتك</h3>", unsafe_allow_html=True)
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        weight = st.number_input("الوزن (جرام)", min_value=0.1, value=10.0, step=0.1)
        carat = st.selectbox("العيار", options=[24, 22, 21, 18], format_func=lambda x: f"عيار {x}")
    
    with col_input2:
        operation = st.radio("نوع العملية", options=["شراء", "بيع"], horizontal=True)
        if operation == "شراء":
            fee = st.number_input("المصنعية (ريال)", min_value=0.0, value=50.0, step=1.0)
        else:
            fee = 0.0
            st.markdown('<div class="info-message">عند البيع تُحتسب قيمة الذهب الخام فقط دون مصنعية</div>', unsafe_allow_html=True)

    if st.button("احسب القيمة"):
        # الحسابات
        price_per_gram = prices[carat]
        base_value = weight * price_per_gram
        
        if operation == "شراء":
            total_value = base_value + fee
        else:
            total_value = base_value
        
        # عرض النتيجة
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top: 0; color: #1A1A1A;'>فاتورة الحساب</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <table class="calculation-table">
            <tr><td><strong>العيار:</strong></td><td>عيار {carat}</td></tr>
            <tr><td><strong>الوزن:</strong></td><td>{weight} جرام</td></tr>
            <tr><td><strong>سعر الجرام:</strong></td><td>{price_per_gram:,.2f} ريال</td></tr>
            <tr><td><strong>قيمة الذهب الخام:</strong></td><td>{base_value:,.2f} ريال</td></tr>
        """, unsafe_allow_html=True)
        
        if operation == "شراء":
            st.markdown(f"""
            <tr><td><strong>المصنعية:</strong></td><td>{fee:,.2f} ريال</td></tr>
            <tr><td><strong>السعر النهائي:</strong></td><td class='final-price'>{total_value:,.2f} ريال</td></tr>
            </table>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <tr><td><strong>السعر النهائي:</strong></td><td class='final-price'>{total_value:,.2f} ريال</td></tr>
            </table>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    # الفوتر
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6B7280; font-size: 0.9rem;'>© 2026 سيلورا جولد — جميع الحقوق محفوظة</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.75rem;'>الأسعار استرشادية وفق السوق العالمي وقد تختلف عن أسعار المتجر</p>", unsafe_allow_html=True)
else:
    st.error("تعذر جلب السعر العالمي، تحقق من الاتصال بالإنترنت")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.75rem;'>© 2026 سيلورا جولد — جميع الحقوق محفوظة</p>", unsafe_allow_html=True)
