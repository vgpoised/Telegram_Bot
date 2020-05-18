from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def welcome_msg(bot,update):
    chat_id = update.message.chat_id
    msg_str = "Welcome aboard !!"
    bot.send_message(chat_id=chat_id,text=msg_str)
def main():
    updater = Updater('1061615492:AAHTgMfEOKuelx_Tq_XpkeTOt5AkdSvUw2A')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('start',welcome_msg))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()