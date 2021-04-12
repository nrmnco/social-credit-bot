import telebot
import sqlite3
import re

bot = telebot.TeleBot('1730912703:AAEJDYn2Eh68NahmEXeIuWNwOS6cAQ6f2rw')

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


albums = [('Nariman', 200),
          ('joe', 200),
          ('John Doe', 200),
          ('Merey', 200),
          ('Doner', 200),
          ('Karina', 200),
          ('Muslim', 200),
          ('Ice', 200),
          ('Aya', 200),
          ('Balausa', 200),
          ('Багдат', 200),
          ('Amina', 200),]

cursor.executemany("INSERT INTO albums VALUES (?,?)", albums)
conn.commit()

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    if message.chat.id == 529158582 or message.chat.id == 406340756 or message.chat.id == 1257906397:
        bot.send_sticker(-1001164820292, message.sticker.file_id)

@bot.message_handler(content_types=['text'])
def send_message(message):
    print(message.from_user)

    id = message.message_id
    mes = message.text

    if message.chat.id == 529158582 or message.chat.id == 406340756 or message.chat.id == 1257906397:
        bot.send_message(-1001164820292, mes)

    elif 'бот' in message.text.lower() or 'б от' in message.text.lower() or 'б о т' in message.text.lower() or 'бо т' in message.text.lower():
        bot.delete_message(-1001164820292, id)


bot.polling(none_stop=True)