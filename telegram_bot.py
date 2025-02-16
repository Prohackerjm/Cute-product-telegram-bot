import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8029816870:AAHdwNNGINwMswvompu7e4P-bPqOJhlHjSE"
bot = telebot.TeleBot(TOKEN)

# اطلاعات محصولات
products = {
    "محصول 1": {
        "photo": "AgACAgQAAxkBAWEZeGew6Oidju-ldy6JC7UUHEBHs-UAA33GMRu2iolRwrVC2pMGbP0BAAMCAANzAAM2BA",
        "price": "200000 تومان",
    },
    "محصول 2": {
        "photo": "AgACAgQAAxkBAWEZgWew6QztdJVI6gSXGF-DvrCepi9hAAJ-xjEbtoqJUaKXU1Gaj4DPAQADAgADcwADNgQ",
        "price": "120000 تومان",
    },
    "محصول 3": {
        "photo": "AgACAgQAAxkBAWEZhmew6SSR5fpMXU_KNzgCj-8vWLFbAAJ_xjEbtoqJUTeaVxiwCIB0AQADAgADcwADNgQ",
        "price": "80000 تومان",
    }
}

# اطلاعات پشتیبانی
support_info = {
    "پشتیبانی 1": {"name": "مائده جماعتی", "phone": "1234", "id": "@abcd"},
    "پشتیبانی 2": {"name": "ملورین مرواریدی", "phone": "4567", "id": "@hello"},
    "پشتیبانی 3": {"name": "کارین رضایی", "phone": "7890", "id": "@krkr"},
}

# آی‌دی‌های فایل‌ها
video_intro = "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ"
customer_voices = [
    "CQACAgQAAxkBAWE_H2ex-mcekZ2HkZamLsS3SyIwCz8UAALmFQACtoqRUZrwK8nU1BzbNgQ",
    "CQACAgQAAxkBAWE_62ex_4yKCC-Rs3T9HturokmB54faAALrFQACtoqRUS8IJkw7c35XNgQ",
    "CQACAgQAAxkBAWE_8Gex_7eqwIfajlXmaZdEy5KLlhI4AALsFQACtoqRUSU4Dr3-bSp7NgQ",
]
customer_feedback = "AgACAgQAAxkBAWFAFGeyAAFi-jWDAAFfEalQyXSpFSm8IKsAAr7HMRu2ipFRkjg-7wJnSDkBAAMCAANzAAM2BA"

# اطلاعات تماس
contact_info = """
📢 نام کانال: @Pinterest_cute  
🔗 لینک عضویت: @Pinterest_cute  
🌍 وب‌سایت: www.pinterest_cute.com  
📞 شماره تماس: 5555555
"""

# دکمه‌های منوی اصلی
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📦 معرفی محصولات", "📞 پشتیبانی", "📱 تماس با ما")
    return markup

# دکمه‌های محصولات
def product_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*products.keys(), "🔙 بازگشت")
    return markup

# دکمه‌های اطلاعات محصول
def product_options():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💰 قیمت", "🎥 فیلم معرفی", "🔊 صدای مشتری", "📸 رضایت مشتریان", "🔙 بازگشت")
    return markup

# دکمه‌های صدای مشتری
def customer_voice_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎙 صدای مشتری ۱", "🎙 صدای مشتری ۲", "🎙 صدای مشتری ۳", "🔙 بازگشت")
    return markup

# دکمه‌های پشتیبانی
def support_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*support_info.keys(), "🔙 بازگشت")
    return markup

# شروع ربات
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "🎉 خوش آمدید!", reply_markup=main_menu())

# نمایش محصولات
@bot.message_handler(func=lambda message: message.text == "📦 معرفی محصولات")
def show_products(message):
    bot.send_message(message.chat.id, "📦 لطفا محصول مورد نظر را انتخاب کنید:", reply_markup=product_menu())

# اطلاعات محصول
@bot.message_handler(func=lambda message: message.text in products)
def show_product(message):
    product = products[message.text]
    bot.send_photo(message.chat.id, product["photo"], caption=f"🔹 {message.text}", reply_markup=product_options())

# نمایش قیمت محصول
@bot.message_handler(func=lambda message: message.text == "💰 قیمت")
def show_price(message):
    for product_name, product in products.items():
        bot.send_message(message.chat.id, f"💰 قیمت {product_name}: {product['price']}")

# نمایش ویدیو معرفی محصول
@bot.message_handler(func=lambda message: message.text == "🎥 فیلم معرفی")
def send_video(message):
    bot.send_video(message.chat.id, video_intro)

# نمایش منوی صدای مشتریان
@bot.message_handler(func=lambda message: message.text == "🔊 صدای مشتری")
def show_customer_voice_menu(message):
    bot.send_message(message.chat.id, "🔊 لطفا یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=customer_voice_menu())

# ارسال صدای مشتریان
@bot.message_handler(func=lambda message: message.text in ["🎙 صدای مشتری ۱", "🎙 صدای مشتری ۲", "🎙 صدای مشتری ۳"])
def send_customer_voice(message):
    index = int(message.text[-1]) - 1
    bot.send_audio(message.chat.id, customer_voices[index])

# نمایش رضایت مشتریان
@bot.message_handler(func=lambda message: message.text == "📸 رضایت مشتریان")
def send_customer_feedback(message):
    bot.send_photo(message.chat.id, customer_feedback)

# نمایش پشتیبانی
@bot.message_handler(func=lambda message: message.text == "📞 پشتیبانی")
def show_support(message):
    bot.send_message(message.chat.id, "📞 لطفا محصول مورد نظر را انتخاب کنید:", reply_markup=support_menu())

# اطلاعات پشتیبانی
@bot.message_handler(func=lambda message: message.text in support_info)
def send_support_info(message):
    support = support_info[message.text]
    bot.send_message(message.chat.id, f"📞 شماره: {support['phone']}\n👤 نام: {support['name']}\n🔗 آیدی: {support['id']}")

# اطلاعات تماس
@bot.message_handler(func=lambda message: message.text == "📱 تماس با ما")
def contact_info_handler(message):
    bot.send_message(message.chat.id, contact_info)

# دکمه بازگشت
@bot.message_handler(func=lambda message: message.text == "🔙 بازگشت")
def go_back(message):
    bot.send_message(message.chat.id, "🔙 بازگشت به منوی اصلی", reply_markup=main_menu())

bot.polling()
