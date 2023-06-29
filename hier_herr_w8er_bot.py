import pytz
import locale
from datetime import datetime
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler
########################################################################################################################
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
########################################################################################################################
async def gay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = "Ко мне или к тебе?))")
########################################################################################################################
async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(tz)
    await context.bot.send_message(chat_id=update.effective_chat.id, text = now.strftime("Во ты дурик, дату сегодняшнюю забыл, ладно, напомню" "\n" "%d %B %Y (%A)"))
########################################################################################################################
async def hh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hh = datetime(2023, 6, 29, 3, 1, 0)
    await context.bot.send_message(chat_id=update.effective_chat.id, text = hh.strftime("Уехал в армию %d %B %Y в %H:%M, это был затянутый тучами депрессивный %A"))
########################################################################################################################
async def nap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = " «Мое вам последнее напутствие." "\n" "В New Vegas и 3 фолыче можно толкать браминов, нажав на них клавишу действия, находясь в режиме скрытности»" "\n" "© Товарищ hier Herr ")
########################################################################################################################
async def ost(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id, text =)
########################################################################################################################
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Напиши нормальную команду...")
########################################################################################################################
if __name__ == '__main__':
    with open ('token.txt', 'r') as file:
        token = file.read().strip()
    application = ApplicationBuilder().token(token).build()
    gay_handler = CommandHandler('itsokaytobegay', gay)
    date_handler = CommandHandler('date', date)
    hh_handler = CommandHandler('hh', hh)
    nap_handler = CommandHandler('naputstvie', nap)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(gay_handler)
    application.add_handler(hh_handler)
    application.add_handler(nap_handler)
    application.add_handler(date_handler)
    application.add_handler(unknown_handler)
    
    application.run_polling()