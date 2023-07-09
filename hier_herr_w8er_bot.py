import pytz
import locale
import random
import time
import datetime
import asyncio
from datetime import datetime, date
from telegram import Update, Bot
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackContext



locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")



async def gay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = "Ко мне или к тебе?))")



async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    def day_word():
        tz = pytz.timezone('Europe/Moscow')
        now = datetime.now(tz)
        day_now = now.strftime("%d")
        return day_now
    
    def date_n0w():
        tz = pytz.timezone('Europe/Moscow')
        now = datetime.now(tz)
        date_now = now.strftime("%B %Y")
        return date_now
    
    def dweek():
        tz = pytz.timezone('Europe/Moscow')
        now = datetime.now(tz)
        wday = now.strftime("%A")
        return wday
    
    now = day_word()
    date_now = date_n0w()
    week_day = dweek()

    message = "Сегодня " + now + " " + date_now + " года. А если интересен день недели, то сегодня " + week_day
    await context.bot.send_message(chat_id=update.effective_chat.id, text = message)



async def hh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = "Уехал в армию 29 июля 2023 года в 3:01 утра")



async def nap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text = " «Мое вам последнее напутствие." "\n" "В New Vegas и 3 фолыче можно толкать браминов, нажав на них клавишу действия, находясь в режиме скрытности»" "\n" "© Товарищ hier Herr ")



async def ost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(tz)
    hh = tz.localize(datetime(2023, 6, 29, 3, 1, 0))
    diff = now - hh
    days = diff.days
    dAys = str(diff.days)
    def decline_day_word (some_day):
        dl = some_day % 10
        if dl == 1 and some_day != 11:
            return "день "
        elif 2 <= dl <= 4 and not (12 <= some_day <= 14):
            return "дня "
        else:
            return "дней "
    
    qday = decline_day_word(days)

    h0urs = diff.seconds//3600
    hours = str(diff.seconds//3600)
    def decline_hour_word(some_hours):
        dl = some_hours % 10
        if dl == 1 and some_hours != 11:
            return "час "
        elif 2 <= dl <= 4 and not (12 <= some_hours <= 14):
            return "часа "
        else:
            return "часов "
        
    qhour = decline_hour_word(h0urs)
        
    mins = (diff.seconds//60)%60
    min = str((diff.seconds//60)%60)
    def decline_minute_word(some_minute):
        dl = some_minute % 10
        if dl == 1 and some_minute != 11:
            return "минута "
        elif 2 <= dl <= 4 and not (12 <= some_minute <= 14):
            return "минуты "
        else:
            return "минут "
        
    qmin = decline_minute_word(mins)

    sEc = diff.seconds%60
    sec = str(diff.seconds%60)
    def decline_sec_word(some_sec):
        dl = some_sec % 10
        if dl == 1 and some_sec != 11:
            return "секунду "
        elif 2 <= dl <= 4 and not (12 <= some_sec <= 14):
            return "секунды "
        else:
            return "секунд "
        
    qsec = decline_sec_word(sEc)
    
    massage = "Товарищ уехал в армию " + dAys + " " + qday + hours + " " + qhour + min + " " + qmin + "и "+ sec + " " + qsec + "назад"
    await context.bot.send_message(chat_id=update.effective_chat.id, text = massage)



async def left(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tz = pytz.timezone('Europe/Moscow')
    lf = tz.localize(datetime(2024, 6, 29, 3, 1, 0))
    now = datetime.now(tz)
    diff = lf - now
    days = diff.days
    dAys = str(diff.days)
    def decline_day_word (some_day):
        dl = some_day % 10
        if dl == 1 and some_day != 11:
            return " день"
        elif 2 <= dl <= 4 and not (12 <= some_day <= 14):
            return " дня"
        else:
            return " дней"

    date = decline_day_word(days)
        
    massage = "До возвращения Товарища осталось примерно " + dAys + date
    await context.bot.send_message(chat_id=update.effective_chat.id, text = massage)



async def img(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Я сейчас сижу за рулем БМП-2"
    img_path = "img/bmp2.jpg"
    await context.bot.send_photo(chat_id=update.effective_chat.id, caption = message, photo = open(img_path, "rb"))



async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Напиши нормальную команду...")



if __name__ == '__main__':
    with open ('tokens/token2.txt', 'r') as file:
        token = file.read().strip()
    application = ApplicationBuilder().token(token).build()
    gay_handler = CommandHandler('itsokaytobegay', gay)
    date_handler = CommandHandler('date', date)
    hh_handler = CommandHandler('hh', hh)
    nap_handler = CommandHandler('nap', nap)
    ost_handler = CommandHandler('ost', ost)
    left_handler = CommandHandler('left', left)
    img_handler = CommandHandler('cdt', img)
    re_msg_handler = CommandHandler('start', re_msg)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(gay_handler)
    application.add_handler(date_handler)
    application.add_handler(hh_handler)
    application.add_handler(nap_handler)
    application.add_handler(ost_handler)
    application.add_handler(left_handler)
    application.add_handler(img_handler)
    application.add_handler(re_msg_handler)
    application.add_handler(unknown_handler)
    application.run_polling()