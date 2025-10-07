# morning_bot_phone_now_final.py
import jdatetime
import requests

# ====== تنظیمات ربات ======
TOKEN = "8105222132:AAEW90Kog9vieGPurTQxGi08xhlsYrnmR9s"      # جایگزین کن
CHAT_ID = "@Ali66017105"       # جایگزین کن (کانال یا چت)

# ====== لیست ماه‌ها به فارسی ======
persian_months = [
    "فروردین", "اردیبهشت", "خرداد", "تیر",
    "مرداد", "شهریور", "مهر", "آبان",
    "آذر", "دی", "بهمن", "اسفند"
]

# ====== روزهای هفته به فارسی ======
persian_weekdays = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]

# ====== تابع ارسال پیام ======
def send_daily_message():
    today = jdatetime.date.today()
    weekday_name = persian_weekdays[today.weekday()]
    day = today.day
    month_name = persian_months[today.month - 1]
    year = today.year

    message = f"سلام، صبح بخیر و شادی 🌼\n*امروز {weekday_name}، {day} {month_name} {year}*"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        r = requests.post(url, data=payload)
        print("✅ پیام ارسال شد:", r.text)
    except Exception as e:
        print("❌ خطا در ارسال پیام:", e)

# ====== ارسال پیام همین حالا ======
send_daily_message()