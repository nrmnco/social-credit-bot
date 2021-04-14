import telebot
import time
import re

bot = telebot.TeleBot('1730912703:AAEJDYn2Eh68NahmEXeIuWNwOS6cAQ6f2rw')

dict = {
    "joe": 200,
    "Nariman": 200,
    "Багдат": 200,
    "John Doe": 200,
    "Daniyar": 200,
    "Merey": 200,
    "Karina": 200,
    "Kalibekoff": 200,
    "Amina🐳": 200,
    "aiya": 200,
    "Baluha": 200,
    "Muslim": 200,
}
@bot.message_handler(commands=['points'])
def start(message):
    lst = ''
    for key in dict:
        lst += key + ' ' + str(dict[key]) + '\n'
    bot.send_message(-1001164820292, lst)



@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    if message.chat.id == 529158582 or message.chat.id == 406340756 or message.chat.id == 1257906397:
        bot.send_sticker(-1001164820292, message.sticker.file_id)



    try:
        if message.reply_to_message.from_user.is_bot == False:

            if message.sticker.thumb.file_unique_id == 'AQAD16puBgAENEwAAg':
                dict[message.reply_to_message.from_user.first_name] -= 20
                bot.send_message(-1001164820292,
                                 message.reply_to_message.from_user.first_name + ' ебать ты лошара получай -20 ачьков\nУ тебя осталось ' +
                                 str(dict[message.reply_to_message.from_user.first_name]) + ' ачьков')

            elif message.sticker.thumb.file_unique_id == 'AQADuhVtBgAEaU0AAg':
                dict[message.reply_to_message.from_user.first_name] += 20
                bot.send_message(-1001164820292,
                                 message.reply_to_message.from_user.first_name + ' брат уважуха от души +20 ачьков\nУ тебя осталось ' +
                                 str(dict[message.reply_to_message.from_user.first_name]) + ' ачьков')
    except Exception:
        pass




@bot.message_handler(content_types=['text'])
def send_message(message):

    if message.chat.id == 529158582 or message.chat.id == 406340756 or message.chat.id == 1257906397:
        bot.send_message(-1001164820292, message.text)
    elif '=)' in message.text or '=(' in message.text or ')=' in message.text or '(=' in message.text:
        bot.delete_message(-1001164820292, message.message_id)

@bot.edited_message_handler(content_types=['text'])
def handler_function(message):
    if '=)' in message.text or '=(' in message.text or ')=' in message.text or '(=' in message.text:
        bot.delete_message(-1001164820292, message.message_id)



try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass