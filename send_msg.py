import random
from random import randint
import string
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу тебе создать пароль. Какой длины пароль тебе нужен?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    psw = 0
    try:
        # Проверяем - число ли длина пароля
        count_symbol = int(message.text)
        # Генерируем пароль посимвольно
        for i in range(0, count_symbol):
            # Определяем буква или число будет в этом знаке
            letter_or_number = random.randint(1, 2)
            # Если выпала единица - выбираем случайную букву и подклеиваем её к предыдущему паролю
            if letter_or_number == 1:
                psw = str(psw) + str(random.choice(string.ascii_letters))
            # Если выпала двойка - выбираем случайную цифру 0-9
            else:
                psw = str(psw) + str(randint(0, 9))
        # Формируем пароль, отбрасывая первый ноль
        password = psw[1:count_symbol+1]
        # Отправляем пароль
        bot.send_message(message.chat.id, password)
    # Если пришло не число
    except ValueError:
        bot.send_message(message.chat.id, 'Введи, пожалуйста, ')

# Запускаем опрос новых сообщений
bot.polling()
