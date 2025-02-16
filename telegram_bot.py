import telebot
from telebot import types

TOKEN = '8029816870:AAHdwNNGINwMswvompu7e4P-bPqOJhlHjSE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("معرفی محصولات")
    item2 = types.KeyboardButton("پشتیبانی")
    item3 = types.KeyboardButton("تماس با ما")
    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "خوش آمدید! به ربات ما، لطفا یکی از گزینه‌ها را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "معرفی محصولات")
def show_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("محصول شماره 1")
    item2 = types.KeyboardButton("محصول شماره 2")
    item3 = types.KeyboardButton("محصول شماره 3")
    item4 = types.KeyboardButton("محصول شماره 4")
    markup.add(item1, item2, item3, item4)
    
    bot.send_message(message.chat.id, "لطفا محصول مورد نظر را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "محصول شماره 1")
def product_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("قیمت محصول")
    item2 = types.KeyboardButton("فیلم معرفی محصول")
    item3 = types.KeyboardButton("صدای مشتری")
    markup.add(item1, item2, item3)
    
    bot.send_photo(message.chat.id, photo="AgACAgQAAxkBAWEZeGew6Oidju-ldy6JC7UUHEBHs-UAA33GMRu2iolRwrVC2pMGbP0BAAMCAANzAAM2BA")
    bot.send_message(message.chat.id, "محصول 1: لطفا یکی از گزینه‌ها را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "قیمت محصول")
def price_product_1(message):
    bot.send_message(message.chat.id, "قیمت محصول 1: 200000")

@bot.message_handler(func=lambda message: message.text == "فیلم معرفی محصول")
def video_product_1(message):
    bot.send_video(message.chat.id, video="BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ")

@bot.message_handler(func=lambda message: message.text == "صدای مشتری")
def customer_voice_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("صدای مشتری اول")
    item2 = types.KeyboardButton("صدای مشتری دوم")
    item3 = types.KeyboardButton("صدای مشتری سوم")
    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "لطفا صدای مشتری را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "صدای مشتری اول")
def voice_1(message):
    bot.send_audio(message.chat.id, audio="CQACAgQAAxkBAWE_H2ex-mcekZ2HkZamLsS3SyIwCz8UAALmFQACtoqRUZrwK8nU1BzbNgQ")

@bot.message_handler(func=lambda message: message.text == "تماس با ما")
def contact_us(message):
    bot.send_message(message.chat.id, "نام آیدی کانال: @Pinterest_cute\nلینک عضویت در کانال: @Pinterest_cute\nآدرس وب‌سایت: Www.pinterest_cute.com\nشماره تماس شرکت: 5555555")

bot.polling()
