from telegram.ext import *
import telegram_token
from telebot import types

API_KEY = telegram_token.token


def handle_message(update, context):
    text = update.message.text

    response = create_responses(text)
    update.message.reply_text(response)

def create_responses(input_text):
    if input_text == "hi":
        return "was gibt es neues"
    else:
        return "ha nicht verstanden, noch ein mal bitte."

def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message)) # Start von Command

    updater.start_polling(0)  # Star von Bot. Aktualisirung in Telegram auf neue Nachrichten

if __name__ == "__main__":
    main()