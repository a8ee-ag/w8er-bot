import pytz
import locale
import random
import time
import datetime
import asyncio
from datetime import datetime, date
from telegram import Update, Bot
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackContext


async def re_msg(update: Update, context: CallbackContext):
    while True:
        n = random.randint(1, 14)
        n = str(n)
        m = random.randint(1, 17)
        m = str(m)
        message = "txt/" + m + ".txt"
        img_path = "img/rnd_igm/" + n + ".jpg"
        with open (message, "r") as msg_path:
            msg = msg_path.read().strip()
        with open ('tokens/token2.txt', 'r') as file:
            token = file.read().strip()
        bot = Bot(token)
        await context.bot.send_photo(chat_id=update.effective_chat.id, caption = msg, photo = open(img_path, "rb"))
        time.sleep(1*1*15)
        

if __name__ == '__main__':
    with open ('tokens/token2.txt', 'r') as file:
        token = file.read().strip()
    application = ApplicationBuilder().token(token).build()

    re_msg_handler = CommandHandler('cerf', re_msg)

    application.add_handler(re_msg_handler)
    application.run_polling()