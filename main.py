"""
💎 حاسبة سيلورا جولد الذكية 💎
تطبيق احترافي لحساب أسعار الذهب بناءً على السعر العالمي الحي
"""

import requests

# الثوابت العالمية
OUNCE_TO_GRAM = 31.1034768  # الأونصة Troy تساوي هذا العدد من الجرامات
USD_TO_SAR = 3.75  # سعر صرف الدولار مقابل الريال السعودي

# رابط API لجلب سعر الذهب
API_URL = "https://api.gold-api.com/price/XAU/USD"


def fetch_gold_price():
    """
    دالة لجلب سعر الذهب العالمي من API
    ترجع سعر الأونصة بالدولار ووقت التحديث، أو None في حال الفشل
    """
    try:
        print("جاري جلب السعر العالمي الحي...")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        # التحقق من وجود مفتاح price
        if "price" not in data:
            print("❌ خطأ: لم يتم العثور على مفتاح 'price' في الاستجابة")
            return None, None
        
        price_per_ounce_usd = data["price"]
        updated_at = data.get("updatedAtReadable", "غير متوفر")
        
        return price_per_ounce_usd, updated_at
    
    except requests.exceptions.RequestException as e:
        print(f"❌ خطأ في الاتصال بالـ API: {e}")
        return None, None
    except ValueError as e:
        print(f"❌ خطأ في تحليل بيانات JSON: {e}")
        return None, None


def calculate_gold_price(price_per_ounce_usd, weight, karat_choice, workmanship):
    """
    دالة لحساب سعر القطعة الذهبية بناءً على الوزن والعيار والمصنعية
    
    المعاملات:
    - price_per_ounce_usd: سعر الأونصة بالدولار
    - weight: وزن القطعة بالجرام
    - karat_choice: اختيار العيار (1=24، 2=21، 3=18)
    - workmanship: قيمة المصنعية بالريال السعودي
    
    ترجع: قاموس يحتوي على تفاصيل الحساب
    """
    # المعادلة 1: سعر الجرام بالدولار
    price_per_gram_usd = price_per_ounce_usd / OUNCE_TO_GRAM
    
    # المعادلة 2: سعر جرام عيار 24 بالريال السعودي
    price_per_gram_24_sar = price_per_gram_usd * USD_TO_SAR
    
    # المعادلة 3: تحديد معامل العيار
    karat_multipliers = {
        1: ("عيار 24", 1.000),
        2: ("عيار 21", 0.875),
        3: ("عيار 18", 0.750)
    }
    
    karat_name, karat_multiplier = karat_multipliers[karat_choice]
    
    # سعر الجرام للعيار المختار
    price_per_gram_for_karat = price_per_gram_24_sar * karat_multiplier
    
    # المعادلة 4: السعر النهائي للقطعة
    gold_value = weight * price_per_gram_for_karat
    final_price = gold_value + workmanship
    
    return {
        "karat_name": karat_name,
        "weight": weight,
        "price_per_gram": price_per_gram_for_karat,
        "gold_value": gold_value,
        "workmanship": workmanship,
        "final_price": final_price
    }


def display_invoice(result, updated_at):
    """
    دالة لعرض الفاتورة النهائية منسقة
    
    المعاملات:
    - result: قاموس نتائج الحساب من دالة calculate_gold_price
    - updated_at: وقت آخر تحديث للسعر
    """
    print("\n" + "=" * 50)
    print("💰 فاتورة شراء الذهب 💰")
    print("=" * 50)
    print(f"📅 آخر تحديث للسعر: {updated_at}")
    print("-" * 50)
    print(f"✨ العيار: {result['karat_name']}")
    print(f"⚖️ الوزن: {result['weight']:.2f} جرام")
    print(f"💵 سعر الجرام: {result['price_per_gram']:.2f} ريال سعودي")
    print("-" * 50)
    print(f"🔸 قيمة الذهب الخام: {result['gold_value']:.2f} ريال")
    print(f"🔹 قيمة المصنعية: {result['workmanship']:.2f} ريال")
    print("-" * 50)
    print(f"🏆 السعر النهائي: {result['final_price']:.2f} ريال سعودي")
    print("=" * 50)


def get_user_input():
    """
    دالة لجمع مدخلات المستخدم من الوزن والعيار والمصنعية
    ترجع: (weight, karat_choice, workmanship) أو (None, None, None) في حال الخطأ
    """
    try:
        # إدخال وزن القطعة
        weight = float(input("\n⚖️ أدخل وزن القطعة بالجرام: "))
        if weight <= 0:
            print("❌ خطأ: الوزن يجب أن يكون رقماً موجباً")
            return None, None, None
        
        # اختيار العيار
        print("\nاختر العيار:")
        print("1️⃣ عيار 24")
        print("2️⃣ عيار 21")
        print("3️⃣ عيار 18")
        karat_choice = int(input("أدخل رقم العيار (1-3): "))
        if karat_choice not in [1, 2, 3]:
            print("❌ خطأ: يجب اختيار رقم بين 1 و 3")
            return None, None, None
        
        # إدخال قيمة المصنعية
        workmanship = float(input("\n🔧 أدخل قيمة المصنعية بالريال السعودي: "))
        if workmanship < 0:
            print("❌ خطأ: المصنعية لا يمكن أن تكون سالبة")
            return None, None, None
        
        return weight, karat_choice, workmanship
    
    except ValueError:
        print("❌ خطأ: الرجاء إدخال أرقام صحيحة")
        return None, None, None


def main():
    """
    الدالة الرئيسية للتطبيق
    """
    # عرض الترحيب
    print("\n" + "💎" * 20)
    print("💎 حاسبة سيلورا جولد الذكية 💎")
    print("💎" * 20 + "\n")
    
    # جلب سعر الذهب
    price_per_ounce_usd, updated_at = fetch_gold_price()
    
    if price_per_ounce_usd is None:
        print("\n❌ تعذر جلب السعر العالمي. يرجى المحاولة لاحقاً.")
        return
    
    # حساب وعرض سعر جرام عيار 24
    price_per_gram_usd = price_per_ounce_usd / OUNCE_TO_GRAM
    price_per_gram_24_sar = price_per_gram_usd * USD_TO_SAR
    
    print(f"\n✅ سعر جرام عيار 24: {price_per_gram_24_sar:.2f} ريال سعودي")
    print(f"🕐 آخر تحديث: {updated_at}")
    
    # جمع مدخلات المستخدم
    weight, karat_choice, workmanship = get_user_input()
    
    if weight is None:
        print("\n❌ تعذر إتمام الحساب بسبب خطأ في الإدخال.")
        return
    
    # حساب السعر النهائي
    result = calculate_gold_price(price_per_ounce_usd, weight, karat_choice, workmanship)
    
    # عرض الفاتورة
    display_invoice(result, updated_at)


if __name__ == "__main__":
    main()
