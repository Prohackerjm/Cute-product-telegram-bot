import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8029816870:AAHdwNNGINwMswvompu7e4P-bPqOJhlHjSE"
bot = telebot.TeleBot(TOKEN)

# دیکشنری محصولات
products = {
    "محصول 1": {
        "photo": "AgACAgQAAxkBAWEZeGew6Oidju-ldy6JC7UUHEBHs-UAA33GMRu2iolRwrVC2pMGbP0BAAMCAANzAAM2BA",
        "price": "200000",
        "video": "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ",
        "reviews": {
            "1": "CQACAgQAAxkBAWE_H2ex-mcekZ2HkZamLsS3SyIwCz8UAALmFQACtoqRUZrwK8nU1BzbNgQ",
            "2": "CQACAgQAAxkBAWE_62ex_4yKCC-Rs3T9HturokmB54faAALrFQACtoqRUS8IJkw7c35XNgQ",
            "3": "CQACAgQAAxkBAWE_8Gex_7eqwIfajlXmaZdEy5KLlhI4AALsFQACtoqRUSU4Dr3-bSp7NgQ"
        }
    },
    "محصول 2": {
        "photo": "AgACAgQAAxkBAWEZgWew6QztdJVI6gSXGF-DvrCepi9hAAJ-xjEbtoqJUaKXU1Gaj4DPAQADAgADcwADNgQ",
        "price": "120000",
        "video": "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ",
        "reviews": {}
    },
    "محصول 3": {
        "photo": "AgACAgQAAxkBAWEZhmew6SSR5fpMXU_KNzgCj-8vWLFbAAJ_xjEbtoqJUTeaVxiwCIB0AQADAgADcwADNgQ",
        "price": "80000",
        "video": "BAACAgQAAxkBAWE--Wex-Wl7lJLVDC4HBk_PGZKTBIk1AALiFQACtoqRUd9JHu_e9bLdNgQ",
        "reviews": {}
    }
}

support_info = {
    "1": {"name": "مائده جماعتی", "phone": "1234", "id": "@abcd"},
    "2": {"name": "ملورین مرواریدی", "phone": "4567", "id": "@hello"},
    "3": {"name": "کارین رضایی", "phone": "7890", "id": "@krkr"}
}

contact_info = {
    "channel": "@Pinterest_cute",
    "join_link": "@Pinterest_cute",
    "website": "Www.pinterest_cute.com",
    "phone": "5555555"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("📦 معرفی محصولات"))
    markup.add(KeyboardButton("🛠 پشتیبانی"), KeyboardButton("📞 تماس با ما"))
    bot.send_message(message.chat.id, "به ربات فروش خوش آمدید!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📦 معرفی محصولات")
def show_products(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for product in products.keys():
        markup.add(KeyboardButton(product))
    markup.add(KeyboardButton("🔙 بازگشت"))
    bot.send_message(message.chat.id, "لطفاً محصول مورد نظر را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in products.keys())
def show_product_details(message):
    product = products[message.text]
    bot.send_photo(message.chat.id, product["photo"])
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("💰 قیمت محصول"), KeyboardButton("🎥 ویدیو معرفی"))
    if product["reviews"]:
        markup.add(KeyboardButton("🔊 صدای مشتریان"))
    markup.add(KeyboardButton("🔙 بازگشت"))
    
    bot.send_message(message.chat.id, "لطفاً گزینه مورد نظر را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "💰 قیمت محصول")
def show_price(message):
    for product, data in products.items():
        if message.reply_to_message and message.reply_to_message.text == product:
            bot.send_message(message.chat.id, f"قیمت {product}: {data['price']} تومان")

@bot.message_handler(func=lambda message: message.text == "🎥 ویدیو معرفی")
def show_video(message):
    for product, data in products.items():
        if message.reply_to_message and message.reply_to_message.text == product:
            bot.send_video(message.chat.id, data["video"])

@bot.message_handler(func=lambda message: message.text == "🔊 صدای مشتریان")
def show_reviews(message):
    for product, data in products.items():
        if message.reply_to_message and message.reply_to_message.text == product and data["reviews"]:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for num, review in data["reviews"].items():
                markup.add(KeyboardButton(f"🎤 صدای مشتری {num}"))
            markup.add(KeyboardButton("🔙 بازگشت"))
            bot.send_message(message.chat.id, "انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith("🎤 صدای مشتری"))
def send_review(message):
    num = message.text.split(" ")[-1]
    for product, data in products.items():
        if num in data["reviews"]:
            bot.send_audio(message.chat.id, data["reviews"][num])

@bot.message_handler(func=lambda message: message.text == "🛠 پشتیبانی")
def support_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for key in support_info.keys():
        markup.add(KeyboardButton(f"پشتیبانی محصول {key}"))
    markup.add(KeyboardButton("🔙 بازگشت"))
    bot.send_message(message.chat.id, "لطفاً محصول موردنظر را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith("پشتیبانی محصول"))
def show_support(message):
    num = message.text.split(" ")[-1]
    if num in support_info:
        info = support_info[num]
        bot.send_message(message.chat.id, f"پشتیبان: {info['name']}")
        bot.send_message(message.chat.id, f"شماره: {info['phone']}")
        bot.send_message(message.chat.id, f"آیدی: {info['id']}")

@bot.message_handler(func=lambda message: message.text == "📞 تماس با ما")
def contact_info_handler(message):
    info = contact_info
    bot.send_message(message.chat.id, f"نام کانال: {info['channel']}
لینک عضویت: {info['join_link']}
وب‌سایت: {info['website']}
شماره: {info['phone']}")

bot.polling()
