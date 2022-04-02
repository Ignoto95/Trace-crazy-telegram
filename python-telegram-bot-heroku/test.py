import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '5214904451:AAHpaQ9Z1YqF3MFR0Jb63GyGgStspFBnMd8'
    bot_chatID = 839682181
    send_text = 'https://api.telegram.org/bot' + str(bot_token) + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=MarkdownV2&text=' + str(bot_message)


    request = requests.get(send_text)

