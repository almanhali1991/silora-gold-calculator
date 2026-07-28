# تطبيق حاسبة أسعار الذهب بواجهة Streamlit الرسومية
# المطور: فريق سيلورا

import streamlit as st
import requests

# ========================================
# الثوابت العالمية (نفسها في main.py)
# ========================================
OUNCE_TO_GRAM = 31.1034768  # الأونصة Troy تساوي هذا العدد من الجرامات
USD_TO_SAR = 3.75           # سعر صرف الدولار مقابل الريال السعودي

# ========================================
# دالة جلب السعر العالمي للذهب
# ========================================
@st.cache_data(ttl=60)  # تخزين مؤقت لمدة 60 ثانية لتجنب طلب API متكرر
def get_gold_price():
    """
    تجلب السعر العالمي للذهب من API وتعيد:
    - سعر جرام عيار 24 بالريال السعودي
    - وقت آخر تحديث
    """
    url = "https://api.gold-api.com/price/XAU/USD"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # التحقق من وجود مفتاح price
        if "price" not in data:
            return None, None
        
        # استخراج سعر الأونصة بالدولار
        price_per_ounce_usd = data["price"]
        
        # استخراج وقت التحديث
        updated_at = data.get("updatedAtReadable", "غير متاح")
        
        # المعادلة 1: سعر الجرام بالدولار
        price_per_gram_usd = price_per_ounce_usd / OUNCE_TO_GRAM
        
        # المعادلة 2: سعر جرام عيار 24 بالريال السعودي
        price_per_gram_24_sar = price_per_gram_usd * USD_TO_SAR
        
        return price_per_gram_24_sar, updated_at
    
    except requests.exceptions.RequestException as e:
        return None, None

# ========================================
# إعداد الصفحة
# ========================================
st.set_page_config(
    page_title="حاسبة سيلورا جولد",
    page_icon="💎",
    layout="centered"
)

# ========================================
# العنوان والترحيب
# ========================================
st.title("💎 حاسبة سيلورا جولد الذكية")
st.caption("حاسبة أسعار الذهب بالسعر العالمي الحي - بالريال السعودي")

# ========================================
# عرض السعر الحي في أعلى الصفحة
# ========================================
price_24_sar, last_update = get_gold_price()

if price_24_sar is None:
    st.error("⚠️ تعذر جلب السعر العالمي، تحقق من الاتصال بالإنترنت")
else:
    st.metric(
        label="سعر جرام عيار 24",
        value=f"{price_24_sar:.2f} ريال سعودي",
        delta=f"آخر تحديث: {last_update}"
    )

# ========================================
# نموذج الإدخال (عمودين)
# ========================================
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "وزن القطعة بالجرام",
        min_value=0.1,
        value=10.0,
        step=0.1,
        help="أدخل وزن القطعة بالجرام"
    )
    
    karat_options = ["عيار 24", "عيار 21", "عيار 18"]
    selected_karat = st.selectbox(
        "اختر العيار",
        options=karat_options,
        index=0
    )

with col2:
    workmanship = st.number_input(
        "قيمة المصنعية بالريال السعودي",
        min_value=0.0,
        value=50.0,
        step=1.0,
        help="أدخل قيمة المصنعية بالريال"
    )

# ========================================
# زر الحساب
# ========================================
if st.button("احسب السعر النهائي 💰", type="primary"):
    
    # تحديد معامل العيار
    karat_multipliers = {
        "عيار 24": 1.000,
        "عيار 21": 0.875,
        "عيار 18": 0.750
    }
    
    karat_multiplier = karat_multipliers[selected_karat]
    
    if price_24_sar is not None:
        # المعادلة 3: سعر الجرام للعيار المختار
        price_per_gram_for_karat = price_24_sar * karat_multiplier
        
        # المعادلة 4: حساب القيم النهائية
        gold_value = weight * price_per_gram_for_karat
        final_price = gold_value + workmanship
        
        # ========================================
        # عرض النتيجة
        # ========================================
        st.success(f"**السعر النهائي: {final_price:.2f} ريال سعودي**", icon="✅")
        
        # عرض تفاصيل الفاتورة
        st.subheader("📋 تفاصيل الفاتورة")
        
        invoice_data = {
            "العيار": [selected_karat],
            "الوزن (جرام)": [f"{weight:.2f}"],
            "سعر الجرام للعيار (ريال)": [f"{price_per_gram_for_karat:.2f}"],
            "قيمة الذهب الخام (ريال)": [f"{gold_value:.2f}"],
            "المصنعية (ريال)": [f"{workmanship:.2f}"],
            "السعر النهائي (ريال)": [f"{final_price:.2f}"]
        }
        
        st.table(invoice_data)
        
        # عرض إضافي بأعمدة منظمة
        st.divider()
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info(f"**العيار:**\n{selected_karat}")
        with c2:
            st.info(f"**الوزن:**\n{weight:.2f} جرام")
        with c3:
            st.info(f"**سعر الجرام:**\n{price_per_gram_for_karat:.2f} ريال")
        
        c4, c5, c6 = st.columns(3)
        with c4:
            st.warning(f"**قيمة الذهب:**\n{gold_value:.2f} ريال")
        with c5:
            st.warning(f"**المصنعية:**\n{workmanship:.2f} ريال")
        with c6:
            st.success(f"**الإجمالي:**\n{final_price:.2f} ريال")
    else:
        st.error("⚠️ لا يمكن الحساب: تعذر جلب السعر العالمي")

# ========================================
# تذييل الصفحة
# ========================================
st.divider()
st.caption("© 2024 حاسبة سيلورا جولد الذكية - جميع الحقوق محفوظة")
