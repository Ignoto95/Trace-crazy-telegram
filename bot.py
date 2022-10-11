import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from script import Allert
from test import telegram_bot_sendtext
import time
import telegram_send
from bestwin import load
PORT = int(os.environ.get('PORT', '8443'))
# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5214904451:AAHpaQ9Z1YqF3MFR0Jb63GyGgStspFBnMd8'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    #update.message.reply_text('Ciao! Benvenuto nel gruppo di TraceCrazyTime! Per utilizzare le funzioni ....')
    telegram_bot_sendtext(load())
    
def bigwin(update, context):
    """Send a message when the command /help is issued."""
    #update.message.reply_text(bot_message_win)
    telegram_bot_sendtext(bot_message_win)
#def echo(update, context):
 #   """Echo the user message."""
 #   update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bigwin", bigwin))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler("porcodio", echo))

    #dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors

    dp.add_error_handler(error)
    #telegram_bot_sendtext("lollogaio")
    # Start the Bot
    #updater.start_webhook(
    #    listen="0.0.0.0",
     #   port=int(PORT),
     #   url_path=TOKEN,
    #    webhook_url='https://pumpkin-cake-34056.herokuapp.com/' + TOKEN
    #
    i = 10
    updater.start_polling()
    #while i > 0 :
    i-=1
    time.sleep(2)
    allert = Allert()
    lista = allert.load()
    #print(lista)
    for x in range(len(lista)):
        if int(lista[x].valore) > 10 :
            telegram_bot_sendtext(lista[x].titolo + " non esce da: " + lista[x].valore + " giri" )
    #telegram_send.send(messages=["Wow that was easy!"])        
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    #updater.idle()

if __name__ == '__main__':
    main()
