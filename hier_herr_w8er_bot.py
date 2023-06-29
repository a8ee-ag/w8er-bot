import pytz
import locale
from datetime import datetime
import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler
########################################################################################################################
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
tz = pytz.timezone('Europe/Moscow')
now = datetime.now(tz)
########################################################################################################################
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
########################################################################################################################
async def gay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ко мне или к тебе?))")
########################################################################################################################
async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    await context.bot.send_message(chat_id=update.effective_chat.id, text= now.strftime("%d %B %Y (%A)"))
########################################################################################################################

########################################################################################################################
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Напиши нормальную команду...")
########################################################################################################################
if __name__ == '__main__':
    with open ('token.txt', 'r') as file:
        token = file.read().strip()
    application = ApplicationBuilder().token(token).build()
    gay_handler = CommandHandler('itsokaytobegay', gay)
    date_handler = CommandHandler ('date', date)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(gay_handler)
    application.add_handler(date_handler)
    application.add_handler(unknown_handler)
    
    application.run_polling()