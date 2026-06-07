import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# ===== НАСТРОЙКИ =====
TOKEN = os.environ.get('BOT_TOKEN')
REF_LINK = 'https://clck.ru/3U3cNU'

# ===== ЗАПУСК БОТА =====
bot = telebot.TeleBot(TOKEN)

fake_codes = {
    "Standoff 2": "SO2-X9F7-3GK5-PL2M",
    "Brawl Stars": "BS-M1K3-PWNZ-2026",
    "Roblox": "RBX-FR33-1000-GOLD",
    "CS2 (Counter-Strike)": "CS2-DROP-SKIN-4F9",
    "Genshin Impact": "GI-PRIM0-5000-X7",
    "PUBG Mobile": "PUBG-UC-9999-ALPHA"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥🔥🔥 БЕСПЛАТНЫЕ КОДЫ ДЛЯ ИГР 🔥🔥🔥\n\n"
        "🎮 Standoff 2\n🎮 Brawl Stars\n🎮 Roblox\n"
        "🎮 CS2\n🎮 Genshin Impact\n🎮 PUBG Mobile\n\n"
        "👇 Нажми /get и выбери свою игру 👇"
    )

@bot.message_handler(commands=['get'])
def get_game(message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for game in fake_codes.keys():
        keyboard.add(InlineKeyboardButton(game, callback_data=game))
    bot.send_message(message.chat.id, "🎮 Выбери игру:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_game(call):
    game = call.data
    fake_code = fake_codes[game]
    bot.send_message(call.message.chat.id, f"✅ Твой код для {game}:\n`{fake_code}`\n\n⚠️ КОД НЕ АКТИВИРОВАН! ⚠️", parse_mode='Markdown')
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔥 АКТИВИРОВАТЬ КОД 🔥", url=REF_LINK))
    bot.send_message(call.message.chat.id, "🔐 Нажми на кнопку, чтобы активировать код. Бесплатно и быстро!", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "🤘 Напиши /start, потом /get, выбери игру и нажми на кнопку.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "❓ Напиши /start")

if __name__ == '__main__':
    print("Бот запущен на Render...")
    bot.infinity_polling()