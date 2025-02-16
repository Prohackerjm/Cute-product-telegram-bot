import telebot
from telebot import types

# توکن ربات (اینجا مقدار واقعی توکن خودت رو قرار بده)
TOKEN = "8029816870:AAHdwNNGINwMswvompu7e4P-bPqOJhlHjSE"
bot = telebot.TeleBot(TOKEN)

# دکمه اصلی
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📦 معرفی محصولات", "🛠 پشتیبانی", "📞 تماس با ما")
    return markup

# دکمه برگشت
def back_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🔙 برگشت به منوی اصلی")
    return markup

# شروع ربات
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "خوش آمدید! لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=main_menu())

# منوی معرفی محصولات
@bot.message_handler(func=lambda message: message.text == "📦 معرفی محصولات")
def show_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛍 محصول شماره 1", "🛍 محصول شماره 2", "🔙 برگشت به منوی اصلی")
    bot.send_message(message.chat.id, "لطفاً محصول مورد نظر را انتخاب کنید:", reply_markup=markup)

# اطلاعات محصول 1
@bot.message_handler(func=lambda message: message.text == "🛍 محصول شماره 1")
def product_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💰 قیمت", "🎥 فیلم معرفی", "🎤 صدای مشتری", "🔙 برگشت به محصولات")
    bot.send_photo(message.chat.id, "AgACAgQAAxkBAWEZeGew6Oidju-ldy6JC7UUHEBHs-UAA33GMRu2iolRwrVC2pMGbP0BAAMCAANzAAM2BA")
    bot.send_message(message.chat.id, "🔹 محصول شماره 1: لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=markup)

# قیمت محصول 1
@bot.message_handler(func=lambda message: message.text == "💰 قیمت")
def price_product_1(message):
    bot.send_message(message.chat.id, "💰 قیمت محصول 1: 200,000 تومان")

# فیلم محصول 1
@bot.message_handler(func=lambda message: message.text == "🎥 فیلم معرفی")
def video_product_1(message):
    bot.send_video(message.chat.id, "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ")

# صدای مشتری محصول 1
@bot.message_handler(func=lambda message: message.text == "🎤 صدای مشتری")
def customer_voice_1(message):
    bot.send_audio(message.chat.id, "CQACAgQAAxkBAWE_H2ex-mcekZ2HkZamLsS3SyIwCz8UAALmFQACtoqRUZrwK8nU1BzbNgQ")

# منوی پشتیبانی
@bot.message_handler(func=lambda message: message.text == "🛠 پشتیبانی")
def show_support(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛠 پشتیبانی محصول 1", "🛠 پشتیبانی محصول 2", "🔙 برگشت به منوی اصلی")
    bot.send_message(message.chat.id, "📞 لطفاً محصولی که به پشتیبانی نیاز دارد را انتخاب کنید:", reply_markup=markup)

# اطلاعات پشتیبانی
@bot.message_handler(func=lambda message: message.text == "🛠 پشتیبانی محصول 1")
def support_1(message):
    bot.send_message(message.chat.id, "📞 شماره پشتیبانی محصول 1: 1234\n👤 نام: مائده جماعتی\n🔗 آیدی: @abcd")

@bot.message_handler(func=lambda message: message.text == "🛠 پشتیبانی محصول 2")
def support_2(message):
    bot.send_message(message.chat.id, "📞 شماره پشتیبانی محصول 2: 4567\n👤 نام: ملورین مرواریدی\n🔗 آیدی: @hello")

# تماس با ما
@bot.message_handler(func=lambda message: message.text == "📞 تماس با ما")
def contact_us(message):
    bot.send_message(message.chat.id, "📢 کانال: @Pinterest_cute\n🌐 سایت: Www.pinterest_cute.com\n📞 شماره: 5555555")

# دکمه‌های برگشت
@bot.message_handler(func=lambda message: message.text == "🔙 برگشت به منوی اصلی")
def back_to_main(message):
    bot.send_message(message.chat.id, "🏠 بازگشت به منوی اصلی", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "🔙 برگشت به محصولات")
def back_to_products(message):
    show_products(message)

# شروع ربات بدون ارور
bot.polling(none_stop=True, interval=0, timeout=20)
