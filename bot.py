import telebot
import sqlite3

bot = telebot.TeleBot('1730912703:AAEJDYn2Eh68NahmEXeIuWNwOS6cAQ6f2rw')

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


albums = [('Nariman', 200),
          ('Azamat', 200),
          ('Kadir', 200),
          ('Merey', 200),
          ('Doner', 200),
          ('Karina', 200),
          ('Muslim', 200),
          ('Ice', 200),
          ('Aya', 200),
          ('Balausa', 200),
          ('Bagdat', 200),
          ('Amina', 200),]

cursor.executemany("INSERT INTO albums VALUES (?,?)", albums)
conn.commit()



@bot.message_handler(content_types=['sticker'])
def start(message):
    print(message.sticker)
    username = message.reply_to_message.from_user.first_name
    if message.sticker.thumb.file_unique_id == 'AQAD16puBgAENEwAAg':
        bot.send_message(-1001164820292, username + ' гей')

    elif message.sticker.thumb.file_unique_id == "AQADuhVtBgAEaU0AAg":
        bot.send_message(-1001164820292, username + ' крутой')

@bot.message_handler(content_types=['text'])
def send_message(message):
    mes = message.text
    if message.chat.id == 529158582:
        bot.send_message(-1001164820292, mes)

bot.polling(none_stop=True)