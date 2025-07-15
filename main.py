import os
from flask import Flask, request
import telegram

TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text.lower() in ["/start", "hola", "hey", "buenas"]:
        bot.send_message(chat_id=chat_id, text="Hola, amor 😘 Soy Ari Vega. ¿Quieres fotos, audios o... algo más?")
    elif "foto" in text.lower():
        bot.send_message(chat_id=chat_id, text="Tengo packs privados solo para ti. Elige:\n1️⃣ Pack básico - 20€\n2️⃣ Pack personalizado - 80€\n\n¿Con cuál te caliento primero?")
    elif "audio" in text.lower():
        bot.s
