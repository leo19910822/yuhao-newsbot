import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler

# 從環境變數拿 Token
TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

bot = Bot(token=TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('哈囉，宇浩老大的Bot已啟動！')

def send_news(context: CallbackContext):
    message = "🚀 早安！這是每日更新的 GPT、大和牛、國際重大新聞！"
    bot.send_message(chat_id=CHANNEL_ID, text=message)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # 加 /start 指令
    dispatcher.add_handler(CommandHandler('start', start))

    # 加入排程：每天早上8點推播
    scheduler = BackgroundScheduler(timezone="Asia/Taipei")
    scheduler.add_job(send_news, 'cron', hour=8, minute=0, args=[dispatcher])
    scheduler.start()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
