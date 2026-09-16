import os
import threading
import telebot
from flask import Flask

# --- Настройки бота ---
TOKEN = "8912264336:AAE-WsKKJ4whiNSobgLTwJJo5AtJZKsA4Vg"
bot = telebot.TeleBot(TOKEN)

# --- Маленький веб-сервер для Render ---
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running"

@app.route('/health')
def health():
    return "OK"

# --- Логика бота ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой первый бот. Работаю ✅")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

# --- Запуск ---
def run_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
