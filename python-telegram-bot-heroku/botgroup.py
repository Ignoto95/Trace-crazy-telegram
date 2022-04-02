import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from script import Allert
#from test import telegram_bot_sendtext
import time
import telegram
api_key = '5214904451:AAHpaQ9Z1YqF3MFR0Jb63GyGgStspFBnMd8'
user_id = '-1001719143657'
bot = telegram.Bot(token=api_key)
def main():
    """Start the bot."""
    allert = Allert()
    lista = allert.load()
    starttime = 0.0
    #print(lista)
    scarto = 10
    minlimit= 50
    checklist = []
#+ checklist.map(lambda e: e.titolo)
    while True:
        for x in range(len(lista)):
            lista = allert.load()
            #print(list(map(lambda e: e.valore,lista)))
            if int(lista[x].valore) > minlimit:
                #print(list(map(lambda e: e.titolo,checklist)))
                stringlist = list(map(lambda e: e.titolo,checklist))
                if lista[x].titolo in stringlist:
                    #print("lista [x] e' in checklist")
                    index = stringlist.index(lista[x].titolo)
                    if (int(checklist[index].valore) + scarto) <= int(lista[x].valore) :
                        #print("valore checlist piu alto di 10")
                        bot.send_message(chat_id=user_id, text= lista[x].titolo + " non esce da: " + lista[x].valore + " giri" )
                        temp = int(checklist[index].valore) + scarto
                        checklist[index].valore = str(temp)
                else:
                    #print("lista valore maggiore di 10")
                    checklist.append(lista[x])
                    bot.send_message(chat_id=user_id, text= lista[x].titolo + " non esce da: " + lista[x].valore + " giri" )
        time.sleep(30.0)
if __name__ == '__main__':
    main()
