#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
💎 حاسبة سيلورا جولد الذكية 💎
تطبيق احترافي لحساب أسعار الذهب بناءً على السعر العالمي الحي
"""

import requests

# ========================================
# الثوابت العالمية
# ========================================
# الأونصة Troy تساوي هذا العدد من الجرامات
OUNCE_TO_GRAM = 31.1034768
# سعر صرف الدولار مقابل الريال السعودي
USD_TO_SAR = 3.75
# رابط API لجلب سعر الذهب العالمي
API_URL = "https://api.gold-api.com/price/XAU/USD"


def fetch_gold_price():
    """
    دالة لجلب سعر الذهب العالمي من الـ API
    ترجع: (سعر الأونصة بالدولار, وقت آخر تحديث) أو (None, None) في حال الخطأ
    """
    print("جاري جلب السعر العالمي الحي...")
    
    try:
        # إرسال طلب GET للرابط
        response = requests.get(API_URL)
        # التحقق من نجاح الطلب
        response.raise_for_status()
        
        # تحويل الاستجابة إلى قاموس
        data = response.json()
        
        # التحقق من وجود مفتاح "price" في الاستجابة
        if "price" not in data:
            print("❌ خطأ: لم يتم العثور على مفتاح 'price' في استجابة الـ API")
            return None, None
        
        # استخراج سعر الأونصة بالدولار
        price_per_ounce_usd = data["price"]
        
        # استخراج وقت التحديث
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
    دالة لحساب سعر القطعة الذهبية
    
    المعاملات:
    - price_per_ounce_usd: سعر الأونصة بالدولار
    - weight: وزن القطعة بالجرام
    - karat_choice: اختيار العيار (1=24، 2=21، 3=18)
    - workmanship: قيمة المصنعية بالريال السعودي
    
    ترجع: (العيار، سعر الجرام للعيار، سعر الذهب الخام، السعر النهائي)
    """
    # المعادلة 1: سعر الجرام بالدولار
    price_per_gram_usd = price_per_ounce_usd / OUNCE_TO_GRAM
    
    # المعادلة 2: سعر جرام عيار 24 بالريال السعودي
    price_per_gram_24_sar = price_per_gram_usd * USD_TO_SAR
    
    # المعادلة 3: تحديد معامل العيار المختار
    karat_factors = {
        1: (24, 1.000),
        2: (21, 0.875),
        3: (18, 0.750)
    }
    
    karat_value, karat_factor = karat_factors[karat_choice]
    
    # حساب سعر الجرام للعيار المختار
    price_per_gram_for_karat = price_per_gram_24_sar * karat_factor
    
    # المعادلة 4: السعر النهائي للقطعة
    raw_gold_price = weight * price_per_gram_for_karat
    final_price = raw_gold_price + workmanship
    
    return karat_value, price_per_gram_for_karat, raw_gold_price, final_price


def display_invoice(karat, weight, price_per_gram, raw_gold_price, workmanship, final_price, updated_at):
    """
    دالة لعرض الفاتورة النهائية منسّقة
    """
    print("\n" + "=" * 50)
    print("🧾 فاتورة شراء الذهب 💎")
    print("=" * 50)
    print(f"العيار:           عيار {karat}")
    print(f"الوزن:            {weight:.2f} جرام")
    print(f"سعر الجرام:       {price_per_gram:.2f} ريال سعودي")
    print("-" * 50)
    print(f"قيمة الذهب الخام: {raw_gold_price:.2f} ريال سعودي")
    print(f"المصنعية:         {workmanship:.2f} ريال سعودي")
    print("-" * 50)
    print(f"💰 السعر النهائي: {final_price:.2f} ريال سعودي")
    print("=" * 50)
    print(f"🕐 آخر تحديث للسعر: {updated_at}")
    print("=" * 50)


def get_user_input():
    """
    دالة لجمع مدخلات المستخدم مع معالجة الأخطاء
    ترجع: (الوزن، اختيار العيار، المصنعية) أو (None, None, None) في حال الخطأ
    """
    # طلب وزن القطعة
    try:
        weight = float(input("أدخل وزن القطعة بالجرام: "))
        if weight <= 0:
            print("❌ خطأ: الوزن يجب أن يكون رقماً موجباً")
            return None, None, None
    except ValueError:
        print("❌ خطأ: الرجاء إدخال رقم صحيح للوزن")
        return None, None, None
    
    # طلب اختيار العيار
    print("\nاختر العيار:")
    print("1. عيار 24")
    print("2. عيار 21")
    print("3. عيار 18")
    
    try:
        karat_choice = int(input("أدخل رقم العيار (1-3): "))
        if karat_choice not in [1, 2, 3]:
            print("❌ خطأ: الرجاء اختيار رقم بين 1 و 3")
            return None, None, None
    except ValueError:
        print("❌ خطأ: الرجاء إدخال رقم صحيح للعيار")
        return None, None, None
    
    # طلب قيمة المصنعية
    try:
        workmanship = float(input("أدخل قيمة المصنعية بالريال السعودي: "))
        if workmanship < 0:
            print("❌ خطأ: المصنعية لا يمكن أن تكون سالبة")
            return None, None, None
    except ValueError:
        print("❌ خطأ: الرجاء إدخال رقم صحيح للمصنعية")
        return None, None, None
    
    return weight, karat_choice, workmanship


def main():
    """
    الدالة الرئيسية للتطبيق
    """
    # عرض الترحيب
    print("\n" + "=" * 50)
    print("💎 حاسبة سيلورا جولد الذكية 💎")
    print("=" * 50 + "\n")
    
    # جلب السعر العالمي
    price_per_ounce, updated_at = fetch_gold_price()
    
    if price_per_ounce is None:
        print("\n❌ تعذر جلب السعر العالمي. يرجى التحقق من اتصال الإنترنت والمحاولة لاحقاً.")
        return
    
    # عرض السعر الحالي
    # حساب سعر جرام عيار 24 بالريال السعودي للعرض
    price_per_gram_usd = price_per_ounce / OUNCE_TO_GRAM
    price_per_gram_24_sar = price_per_gram_usd * USD_TO_SAR
    
    print("\n✅ تم جلب السعر بنجاح!")
    print(f"📊 سعر جرام عيار 24: {price_per_gram_24_sar:.2f} ريال سعودي")
    print(f"🕐 آخر تحديث: {updated_at}\n")
    
    # جمع مدخلات المستخدم
    weight, karat_choice, workmanship = get_user_input()
    
    if weight is None:
        print("\n❌ تعذر إتمام الحساب بسبب خطأ في المدخلات.")
        return
    
    # حساب السعر
    karat, price_per_gram, raw_gold_price, final_price = calculate_gold_price(
        price_per_ounce, weight, karat_choice, workmanship
    )
    
    # عرض الفاتورة
    display_invoice(karat, weight, price_per_gram, raw_gold_price, workmanship, final_price, updated_at)


if __name__ == "__main__":
    main()
