import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Load environment variables from .env file
load_dotenv()

# Get the Telegram bot token from the environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Define a function to handle normal text messages
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create an Updater object
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for /start command and normal text messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
