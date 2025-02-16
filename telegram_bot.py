import telebot
from telebot import types

# 🔹 توکن ربات
TOKEN = "8029816870:AAHdwNNGINwMswvompu7e4P-bPqOJhlHjSE"
bot = telebot.TeleBot(TOKEN)

# 🔹 منوی اصلی
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("معرفی محصولات", "پشتیبانی", "تماس با ما")
    bot.send_message(message.chat.id, "خوش آمدید! لطفاً یک گزینه را انتخاب کنید:", reply_markup=markup)

# 🔹 منوی محصولات
@bot.message_handler(func=lambda message: message.text == "معرفی محصولات")
def show_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("محصول شماره 1", "محصول شماره 2")
    markup.add("بازگشت به منو اصلی")
    bot.send_message(message.chat.id, "لطفاً یک محصول را انتخاب کنید:", reply_markup=markup)

# 🔹 اطلاعات محصول شماره 1
@bot.message_handler(func=lambda message: message.text == "محصول شماره 1")
def product_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("قیمت محصول 1", "فیلم معرفی محصول 1", "صدای مشتری محصول 1")
    markup.add("بازگشت به محصولات")
    
    bot.send_photo(message.chat.id, photo="AgACAgQAAxkBAWEZeGew6Oidju-ldy6JC7UUHEBHs-UAA33GMRu2iolRwrVC2pMGbP0BAAMCAANzAAM2BA")
    bot.send_message(message.chat.id, "🔹 محصول 1: لطفاً یک گزینه را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "قیمت محصول 1")
def price_product_1(message):
    bot.send_message(message.chat.id, "💰 قیمت محصول 1: 200,000 تومان")

@bot.message_handler(func=lambda message: message.text == "فیلم معرفی محصول 1")
def video_product_1(message):
    bot.send_video(message.chat.id, "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ")

@bot.message_handler(func=lambda message: message.text == "صدای مشتری محصول 1")
def voice_product_1(message):
    bot.send_audio(message.chat.id, "CQACAgQAAxkBAWE_H2ex-mcekZ2HkZamLsS3SyIwCz8UAALmFQACtoqRUZrwK8nU1BzbNgQ")

# 🔹 اطلاعات محصول شماره 2
@bot.message_handler(func=lambda message: message.text == "محصول شماره 2")
def product_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("قیمت محصول 2", "فیلم معرفی محصول 2", "صدای مشتری محصول 2")
    markup.add("بازگشت به محصولات")
    
    bot.send_photo(message.chat.id, photo="AgACAgQAAxkBAWEZgWew6QztdJVI6gSXGF-DvrCepi9hAAJ-xjEbtoqJUaKXU1Gaj4DPAQADAgADcwADNgQ")
    bot.send_message(message.chat.id, "🔹 محصول 2: لطفاً یک گزینه را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "قیمت محصول 2")
def price_product_2(message):
    bot.send_message(message.chat.id, "💰 قیمت محصول 2: 120,000 تومان")

@bot.message_handler(func=lambda message: message.text == "فیلم معرفی محصول 2")
def video_product_2(message):
    bot.send_video(message.chat.id, "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ")

@bot.message_handler(func=lambda message: message.text == "صدای مشتری محصول 2")
def voice_product_2(message):
    bot.send_audio(message.chat.id, "CQACAgQAAxkBAWE_62ex_4yKCC-Rs3T9HturokmB54faAALrFQACtoqRUS8IJkw7c35XNgQ")

# 🔹 منوی پشتیبانی
@bot.message_handler(func=lambda message: message.text == "پشتیبانی")
def show_support(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("پشتیبانی محصول 1", "پشتیبانی محصول 2")
    markup.add("بازگشت به منو اصلی")
    bot.send_message(message.chat.id, "لطفاً محصول مورد نظر را برای پشتیبانی انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "پشتیبانی محصول 1")
def support_1(message):
    bot.send_message(message.chat.id, "📞 پشتیبانی محصول 1\nنام: مائده جماعتی\nآیدی: @abcd")

@bot.message_handler(func=lambda message: message.text == "پشتیبانی محصول 2")
def support_2(message):
    bot.send_message(message.chat.id, "📞 پشتیبانی محصول 2\nنام: ملورین مرواریدی\nآیدی: @hello")

# 🔹 تماس با ما
@bot.message_handler(func=lambda message: message.text == "تماس با ما")
def contact_us(message):
    bot.send_message(message.chat.id, "📞 تماس با ما\n🔹 آیدی کانال: @Pinterest_cute\n🔹 وب‌سایت: www.pinterest_cute.com\n🔹 شماره تماس: 5555555")

# 🔹 دکمه‌های بازگشت
@bot.message_handler(func=lambda message: message.text == "بازگشت به محصولات")
def back_to_products(message):
    show_products(message)

@bot.message_handler(func=lambda message: message.text == "بازگشت به منو اصلی")
def back_to_main_menu(message):
    send_welcome(message)

# 🔹 اجرای ربات
bot.polling(none_stop=True, interval=0, timeout=20, threaded=False)
