import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

# 從環境變數拿 Token
TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

bot = Bot(token=TOKEN)

def start(update: Update, context):
    update.message.reply_text('哈囉，宇浩老大的Bot已啟動！')

def send_news(context):
    message = "🚀 早安！這是每日更新的 GPT 和和牛新聞！"
    bot.send_message(chat_id=CHANNEL_ID, text=message)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # 加 /start 指令
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
