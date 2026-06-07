import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# ===== НАСТРОЙКИ =====
TOKEN = '8923053719:AAFkZ82m_sdB19s542Cag2n7cjjiaJ9CYos'  # СЮДА ВСТАВЬ ТОКЕН ОТ @BotFather
REF_LINK = 'https://clck.ru/3U3cNU'  # ТВОЯ РЕФЕРАЛЬНАЯ ССЫЛКА (УЖЕ ВСТАВЛЕНА)

# ===== ЗАПУСК БОТА =====
bot = telebot.TeleBot(TOKEN)

# Фальшивые коды для игр (выглядят правдоподобно)
fake_codes = {
    "Standoff 2": "SO2-X9F7-3GK5-PL2M",
    "Brawl Stars": "BS-M1K3-PWNZ-2026",
    "Roblox": "RBX-FR33-1000-GOLD",
    "CS2 (Counter-Strike)": "CS2-DROP-SKIN-4F9",
    "Genshin Impact": "GI-PRIM0-5000-X7",
    "PUBG Mobile": "PUBG-UC-9999-ALPHA"
}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥🔥🔥 БЕСПЛАТНЫЕ КОДЫ ДЛЯ ИГР 🔥🔥🔥\n\n"
        "🎮 Standoff 2\n"
        "🎮 Brawl Stars\n"
        "🎮 Roblox\n"
        "🎮 CS2\n"
        "🎮 Genshin Impact\n"
        "🎮 PUBG Mobile\n\n"
        "👇 Нажми /get и выбери свою игру 👇"
    )

# Команда /get — выбор игры
@bot.message_handler(commands=['get'])
def get_game(message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for game in fake_codes.keys():
        keyboard.add(InlineKeyboardButton(game, callback_data=game))
    bot.send_message(
        message.chat.id,
        "🎮 Выбери игру, для которой хочешь получить код:",
        reply_markup=keyboard
    )

# Обработка нажатия на кнопку с игрой
@bot.callback_query_handler(func=lambda call: True)
def handle_game(call):
    game = call.data
    fake_code = fake_codes[game]
    
    # Сначала отправляем фальшивый код
    bot.send_message(
        call.message.chat.id,
        f"✅ Твой код для {game}:\n"
        f"`{fake_code}`\n\n"
        "⚠️ КОД НЕ АКТИВИРОВАН! ⚠️",
        parse_mode='Markdown'
    )
    
    # Потом отправляем кнопку с реферальной ссылкой
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔥 АКТИВИРОВАТЬ КОД 🔥", url=REF_LINK))
    
    bot.send_message(
        call.message.chat.id,
        "🔐 Чтобы код заработал, нужно подтвердить, что ты человек.\n\n"
        "👉 Нажми на кнопку ниже 👈\n"
        "Это бесплатно и займёт 30 секунд.\n\n"
        "⚠️ БЕЗ ПОДТВЕРЖДЕНИЯ КОД НЕ СРАБОТАЕТ! ⚠️",
        reply_markup=markup
    )

# Команда /help (для приличия)
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🤖 Как пользоваться ботом:\n"
        "1. Напиши /start\n"
        "2. Напиши /get\n"
        "3. Выбери игру\n"
        "4. Нажми на кнопку активации\n"
        "5. Подтверди регистрацию\n"
        "6. Код станет активным!\n\n"
        "🚀 Удачи!"
    )

# На случай если пользователь напишет что-то другое
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(
        message.chat.id,
        "❓ Не понял команду.\n"
        "Напиши /start для начала\n"
        "Или /get чтобы получить код"
    )

# ===== ЗАПУСК =====
if __name__ == '__main__':
    print("Бот запущен и работает...")
    bot.infinity_polling()