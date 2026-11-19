# UC Subscription

این ریپو هر ۳ ساعت یک بار منابع کانفیگ را می‌خواند، کانفیگ‌های vless و ss را با تست واقعی از طریق Xray بررسی می‌کند و حداکثر ۲۰۰ کانفیگ سالم‌تر را در `output/` قرار می‌دهد.

## لینک‌های اشتراک
- متنی: https://raw.githubusercontent.com/CafeWhale/UC/main/output/sub.txt
- base64: https://raw.githubusercontent.com/CafeWhale/UC/main/output/sub_base64.txt

## افزودن منبع جدید
فایل `sources.txt` را ویرایش کنید و هر منبع را در یک خط بنویسید. خطوط شروع‌شونده با `#` نادیده گرفته می‌شوند.

## اجرای دستی
تب Actions را باز کنید، workflow با نام Update subscription را انتخاب کنید و Run workflow را بزنید.

## تغییر تنظیمات
- آستانه‌ی سلامت و هدف تست: `scripts/test_xray.py` (MAX_MS و TEST_URL)
- تعداد خروجی: `scripts/score.py` (TOP)
- بازه‌ی زمانی اجرا: `.github/workflows/update.yml` (cron)
