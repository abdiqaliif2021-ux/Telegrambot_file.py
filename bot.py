import os
from telegram import Bot

# Ka akhri variables ka .env
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

bot.send_message(chat_id=CHANNEL_ID, text="Bot-kan waa online!")
