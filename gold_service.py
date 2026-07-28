# gold_service.py — جلب السعر من gold-api.com (المصدر الوحيد) + الحسابات
# لا يعتمد على pytz إطلاقاً (يستخدم datetime القياسية فقط)

import time
import requests
from datetime import datetime, timezone, timedelta

API_URL = "https://api.gold-api.com/price/XAU/USD"
OUNCE_TO_GRAM = 31.1034768
USD_TO_SAR = 3.75
RIYADH_TZ = timezone(timedelta(hours=3))

KARAT_FACTORS = {
    "عيار 24": 1.000,
    "عيار 22": 0.916,
    "عيار 21": 0.875,
    "عيار 18": 0.750,
}

# بصمة متصفح حقيقية + قبول JSON (تجنّب الحجب من خوادم السحابة)
_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/json",
}


def _riyadh_time(iso):
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(RIYADH_TZ)
        return dt.strftime("%I:%M %p")
    except Exception:
        return ""


def fetch_gold(retries=3):
    """يجلب السعر من gold-api.com مع إعادة محاولة لنفس المصدر.
    يُرجع: (سعر جرام 24 بالريال, وقت التحديث بالعربية, قائمة الأخطاء)."""
    errors = []
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(API_URL, headers=_HEADERS, timeout=20)
            r.raise_for_status()
            d = r.json()
            ounce = float(d["price"])
            gram24 = (ounce / OUNCE_TO_GRAM) * USD_TO_SAR
            return gram24, _riyadh_time(d.get("updatedAt", "")), errors
        except Exception as e:
            errors.append(f"محاولة {attempt} — {type(e).__name__}: {e}")
            if attempt < retries:
                time.sleep(2)
    return None, None, errors


def gram_price(price_24, karat):
    return price_24 * KARAT_FACTORS[karat]
