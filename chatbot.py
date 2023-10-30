# import requests
# import schedule
# import time
# import threading
# users = {}
#     user_id = message.chat.id
#     users[user_id] = True

import telebot
from telebot import types
import random
import sqlite3

bot_token = "6481788690:AAFU2TT0AqwB84cEB0ctzWhxmSfplRJFAyM"
bot = telebot.TeleBot(bot_token)

motivation = ['Верь в себя, и все возможно!', 'Сегодня твой день, сделай его замечательным!', 'Все начинается с первого шага!', 'Всегда оставайся на пути к своей цели, не отвлекайся на мелочи!', 'Если хочешь изменить мир, начни с себя!', 'Никогда не говори “невозможно”. Все возможно, если ты настойчив и уверен в себе!']

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn_channel = types.KeyboardButton(text='/channel')
    btn_motivation = types.KeyboardButton(text='Мотивация')
    markup.row(btn_channel, btn_motivation)
    bot.send_message(message.chat.id, f'<b>Добро пожаловать, {message.from_user.first_name} {message.from_user.last_name}!</b> Я Ваш психологический помощник от клуба Изнутри! Выберите, чем я могу Вам помочь?', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['channel'])
def channel(message):
    markup = types.InlineKeyboardMarkup()  

    url_button = types.InlineKeyboardButton(text="Перейти в канал", url="https://t.me/zevpsyholok")

    markup.add(url_button) 
    bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти в канал:", reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Какое красивое фото!')

@bot.message_handler(func=lambda message: True)
def message(message):
    if message.text.lower() == 'мотивация':
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Хочу другую!", callback_data='edit_motivation')
        markup.add(button)
        bot.send_message(message.chat.id, f'{random.choice(motivation)}', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def edit_motivation(callback):
    if callback.data == 'edit_motivation':
        bot.edit_message_text(f'{random.choice(motivation)}', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)    