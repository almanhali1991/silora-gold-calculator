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
# تحسين المظهر بهوية ذهبية فاخرة (CSS مخصص)
# ========================================
st.markdown("""
<style>
    /* خلفية متدرجة ذهبية فاتحة للصفحة */
    .stApp {
        background: linear-gradient(135deg, #FFF8E7 0%, #FFFBF0 50%, #FFF8DC 100%);
    }
    
    /* عنوان رئيسي بلون ذهبي داكن وخط أنيق */
    h1 {
        color: #B8860B;
        font-family: 'Georgia', serif;
        font-weight: bold;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(184, 134, 11, 0.3);
    }
    
    /* حدود ذهبية خفيفة حول العناصر */
    .gold-border {
        border: 2px solid #DAA520;
        border-radius: 10px;
        padding: 15px;
        background: linear-gradient(135deg, #FFFACD 0%, #FAFAD2 100%);
        box-shadow: 0 4px 6px rgba(218, 165, 32, 0.2);
    }
    
    /* تنسيق المقاييس */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #FFFACD 0%, #FAFAD2 100%);
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #DAA520;
    }
    
    /* تنسيق الأزرار */
    .stButton > button {
        background: linear-gradient(135deg, #B8860B 0%, #DAA520 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #DAA520 0%, #FFD700 100%);
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# العنوان والترحيب
# ========================================
st.markdown("<h1>💎 سيلورا جولد | حاسبة أسعار الذهب</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B7355; font-size: 16px;'>أسعار محدثة لحظياً وفق السوق العالمي — بالريال السعودي</p>", unsafe_allow_html=True)

# ========================================
# عرض السعر الحي ولوحة الأسعار
# ========================================
price_24_sar, last_update = get_gold_price()

if price_24_sar is None:
    st.error("⚠️ تعذر جلب السعر العالمي، تحقق من الاتصال بالإنترنت")
else:
    # عرض سعر عيار 24 الرئيسي
    st.metric(
        label="💰 سعر جرام عيار 24",
        value=f"{price_24_sar:.2f} ريال سعودي",
        delta=f"🕐 آخر تحديث: {last_update}"
    )
    
    st.divider()
    
    # ========================================
    # الميزة 2: لوحة أسعار الأعيرة الحية
    # ========================================
    st.markdown("<h3 style='color: #B8860B; text-align: center;'>📊 أسعار الجرام الحية بالريال السعودي</h3>", unsafe_allow_html=True)
    
    # قاموس معاملات النقاء للأعيرة (الميزة 1: إضافة عيار 22)
    KARAT_FACTORS = {
        "عيار 24": 1.000,
        "عيار 22": 0.916,
        "عيار 21": 0.875,
        "عيار 18": 0.750
    }
    
    # إنشاء 4 أعمدة لعرض أسعار جميع الأعيرة
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        price_24 = price_24_sar * KARAT_FACTORS["عيار 24"]
        st.metric(label="✨ عيار 24", value=f"{price_24:.2f} ر.س")
    
    with col2:
        price_22 = price_24_sar * KARAT_FACTORS["عيار 22"]
        st.metric(label="⭐ عيار 22", value=f"{price_22:.2f} ر.س")
    
    with col3:
        price_21 = price_24_sar * KARAT_FACTORS["عيار 21"]
        st.metric(label="🏆 عيار 21", value=f"{price_21:.2f} ر.س")
    
    with col4:
        price_18 = price_24_sar * KARAT_FACTORS["عيار 18"]
        st.metric(label="💫 عيار 18", value=f"{price_18:.2f} ر.س")
    
    st.markdown("---")

# ========================================
# نموذج الإدخال (عمودين)
# ========================================
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "⚖️ وزن القطعة بالجرام",
        min_value=0.1,
        value=10.0,
        step=0.1,
        help="أدخل وزن القطعة بالجرام"
    )

    karat_options = ["عيار 24", "عيار 22", "عيار 21", "عيار 18"]
    selected_karat = st.selectbox(
        "💍 اختر العيار",
        options=karat_options,
        index=0
    )

with col2:
    # الميزة 4: خيار نوع العملية (شراء / بيع)
    operation_type = st.radio(
        "🔄 نوع العملية",
        options=["🛒 شراء", "💵 بيع"],
        horizontal=True,
        help="في حالة البيع لا تُحتسب المصنعية"
    )
    
    workmanship = st.number_input(
        "💎 قيمة المصنعية بالريال السعودي",
        min_value=0.0,
        value=50.0,
        step=1.0,
        help="أدخل قيمة المصنعية بالريال",
        disabled=(operation_type == "💵 بيع")
    )
    
    # عرض ملاحظة عند اختيار بيع
    if operation_type == "💵 بيع":
        st.info("📌 عند البيع لا تُحتسب المصنعية")

# ========================================
# زر الحساب
# ========================================
if st.button("احسب السعر النهائي 💰", type="primary", use_container_width=True):

    if price_24_sar is not None:
        # تحديد معامل العيار
        karat_multiplier = KARAT_FACTORS[selected_karat]

        # المعادلة 3: سعر الجرام للعيار المختار
        price_per_gram_for_karat = price_24_sar * karat_multiplier

        # حساب قيمة الذهب الخام
        gold_value = weight * price_per_gram_for_karat
        
        # الميزة 4: حساب السعر النهائي حسب نوع العملية
        if operation_type == "🛒 شراء":
            final_price = gold_value + workmanship
            operation_note = "شراء (تم إضافة المصنعية)"
        else:  # بيع
            final_price = gold_value
            workmanship = 0.0
            operation_note = "بيع (لا تُحتسب المصنعية)"

        # ========================================
        # عرض النتيجة
        # ========================================
        st.success(f"**💰 السعر النهائي: {final_price:.2f} ريال سعودي**", icon="✅")
        st.caption(f"نوع العملية: {operation_note}")

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
