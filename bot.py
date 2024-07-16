import telebot
import requests
from telebot import types

API_KEY = '7164017432:AAG4Sdz5aYCMbew8dgz8go9jL5tTXDQ9D1c'
NBRB_API_URL = 'https://www.nbrb.by/api/exrates/rates'

bot = telebot.TeleBot(API_KEY)

def get_conversion_rate(currency):
    response = requests.get(f'{NBRB_API_URL}/{currency.upper()}?parammode=2')
    return response.json().get('Cur_OfficialRate')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/convert")
    markup.add(item1)
    bot.send_message(message.chat.id, "Привет! Я бот для конвертации валют. Введите команду в формате: /convert <сумма> <из валюты> <в валюту>", reply_markup=markup)

@bot.message_handler(commands=['convert'])
def convert_currency(message):
    try:
        msg = bot.send_message(message.chat.id, "Введите сумму, исходную валюту и целевую валюту через пробел:")
        bot.register_next_step_handler(msg, process_conversion)
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка. Попробуйте снова.")

def process_conversion(message):
    try:
        amount, from_currency, to_currency = message.text.split()
        amount = float(amount)
        
        from_rate = get_conversion_rate(from_currency)
        to_rate = get_conversion_rate(to_currency)
        
        if from_rate and to_rate:
            converted_amount = amount * (from_rate / to_rate)
            bot.send_message(message.chat.id, f'{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}')
        else:
            bot.send_message(message.chat.id, "Не удалось получить курс валют.")
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка. Убедитесь, что вы ввели данные в правильном формате: <сумма> <из валюты> <в валюту>")

bot.polling()
