import asyncio
from telegram import Bot
from django.conf import settings

async def send_notify(message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
