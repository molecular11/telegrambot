import random
import schedule
import time
from telegram import Bot
from telegram.error import TelegramError

# تنظیمات ربات
BOT_TOKEN = "7611495009:AAHTjL12m8wwkA_u9a1DahtKgtg8M7_ZuyM"  # توکن ربات
CHANNEL_ID = "@pvatahghigh"  # آدرس عمومی کانال
ADMIN_ID = "@Mehsonam"  # آدرس ادمین

# لیست پیام‌ها (دو خطی با اموجی‌های جذاب)
messages = [
    f"✍️📚 مقاله علمی در بیولوژی نیاز داری؟\nما با کیفیت بالا برات آماده می‌کنیم! 🌟🎉\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🩺📝 پایان‌نامه پزشکی رو به ما بسپار!\nاستاندارد بین‌المللی و تضمینی! 🔬✨\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📑🌟 تولید محتوای تخصصی پزشکی!\nبرای وب‌سایت و شبکه‌های اجتماعی! 🚀🎯\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📖🦷 کتاب دندانپزشکی بنویس!\nاز ایده تا چاپ با ما! ✍️🎉\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🌍📜 ترجمه متون تخصصی داروسازی!\nدقیق و سریع مثل برق! ⚡✨\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🎙️📝 ویس کلاست رو متن کن!\nتبدیل وی,truncated,س به متن با دقت 100%! 🌟🚀\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🔬📚 مقاله ISI در بیولوژی!\nحرفه‌ای و آماده انتشار! ✍️🎯\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🩺📖 پایان‌نامه داروسازی با کیفیت!\nما تضمین می‌کنیم! 🌟🔥\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📱🌟 محتوای دیجیتال پزشکی!\nجذاب و علمی برای کلینیک‌ها! 🚀🎉\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📕✍️ کتاب علمی در پزشکی!\nنگارش و ویرایش حرفه‌ای! 📚✨\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🌐📜 ترجمه مقالات به انگلیسی!\nبا استانداردهای جهانی! 🌍⚡\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🎤📝 تبدیل ویس‌های آموزشی!\nمتن دقیق و سریع تحویل بگیر! 🚀🌟\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📚🔬 پروپوزال بیولوژی و پزشکی!\nسریع و حرفه‌ای آماده می‌شه! ✍️🎯\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🦷📝 مقاله دندانپزشکی تخصصی!\nبرای ژورنال‌های معتبر! 🌟🔥\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📑🚀 محتوای علمی برای شبکه‌ها!\nجذاب و کاربرپسند! 🌟🎉\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📖📚 نگارش کتاب بیولوژی!\nاز صفر تا صد با کیفیت! ✍️✨\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🌍📜 ترجمه متون دندانپزشکی!\nبه هر زبانی که بخوای! ⚡🌟\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🎙️📝 ویس پزشکی رو متن کن!\nدقیق و سریع تحویل می‌دم! 🚀🎯\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🔬📚 مقاله علمی برای کنفرانس!\nحرفه‌ای و جذاب! ✍️🌟\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🩺📖 پایان‌نامه داروسازی!\nبا استانداردهای بالا! 📚🔥\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📑🌟 محتوای آموزشی پزشکی!\nبرای دانشجویان و اساتید! 🚀🎉\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📕✍️ کتاب آموزشی بیولوژی!\nنگارش حرفه‌ای و سریع! 📚✨\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🌐📜 ترجمه متون علمی پزشکی!\nبه زبان دلخواهت! 🌍⚡\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🎤📝 تبدیل ویس جلسات علمی!\nدقیق و با سرعت بالا! 🚀🌟\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📚🦷 پروپوزال دندانپزشکی!\nسریع و با کیفیت آماده می‌شه! ✍️🎯\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🔬📝 مقاله پزشکی تخصصی!\nبرای ژورنال‌های معتبر! 🌟🔥\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📱🚀 محتوای اپلیکیشن پزشکی!\nعلمی و جذاب! 🌟🎉\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"📖📚 کتاب داروسازی بنویس!\nبا استانداردهای جهانی! ✍️✨\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🌍📜 ترجمه متون بیولوژی!\nدقیق و سریع تحویل بگیر! ⚡🌟\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}",
    f"🎙️📝 ویس کنفرانس پزشکی!\nتبدیل به متن با کیفیت! 🚀🎯\n📩 تماس: {ADMIN_ID}\n🌐 کانال: {CHANNEL_ID}"
]

# تابع ارسال پیام
async def send_random_message():
    bot = Bot(token=BOT_TOKEN)
    message = random.choice(messages)
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        print(f"Message sent: {message}")
    except TelegramError as e:
        print(f"Error sending message: {e}")

# زمان‌بندی ارسال پیام هر 3 ساعت
schedule.every(3).hours.do(lambda: asyncio.run(send_random_message()))

# حلقه اصلی برای اجرای زمان‌بندی
if __name__ == "__main__":
    import asyncio
    print("Bot is running...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # بررسی هر دقیقه
