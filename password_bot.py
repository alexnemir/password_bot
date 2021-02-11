import random
from random import randint
import string
import telegram
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)

def create_psw(symbol):
    psw = 0
    try:
        test_int = int(symbol)
        for i in range(1, symbol+1):
            letter_or_number = random.randint(1, 2)
            if letter_or_number == 1:
                psw = str(psw) + str(random.choice(string.ascii_letters))
            else:
                psw = str(psw) + str(randint(0, 9))
        send_message(psw[1:symbol+1])
    except ValueError:
        send_message('Длинна пароля не число')

symbol = 3

create_psw(symbol)


