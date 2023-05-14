import CONFIG
import telebot
from queries import Database
from datetime import datetime, timedelta


bot = telebot.TeleBot(CONFIG.TOKEN)
db = Database()
time_limit = 5 * 60

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'дарова ептеть')

# adding and removing credits with restrictions
@bot.message_handler(content_types=['sticker'])
def social_credit(message):
    try:
        if message.chat.type == 'supergroup' and message.reply_to_message.from_user.is_bot == False and message.reply_to_message.from_user.id != message.from_user.id:
            now = datetime.now()
            last_time = db.get_last_sticker_time(message.from_user.id)
            if message.sticker.set_name == 'PoohSocialCredit' and time_limit < (now - last_time).total_seconds():
                if message.sticker.emoji == '😄':
                    db.adding_point(message.reply_to_message.from_user.id)
                    res = db.show_point(message.reply_to_message.from_user.id)
                    db.add_last_sticker_time(message.from_user.id)
                    bot.send_message(message.chat.id, 'плюс миска рис для {} \nнащалника у тебя {} ачков'.format(message.reply_to_message.from_user.first_name, res[0][0]))

                elif message.sticker.emoji == '😞':
                    db.subtract_point(message.reply_to_message.from_user.id)
                    res = db.show_point(message.reply_to_message.from_user.id)
                    db.add_last_sticker_time(message.from_user.id)
                    bot.send_message(message.chat.id, 'минус миска рис для {} \nв санаторий его у него {} ачков'.format(message.reply_to_message.from_user.first_name, res[0][0]))
            else:
                bot.send_message(message.chat.id, 'осуждать можно раз в 5 минут\nжди давай {} секунд'.format(int(300 - (now - last_time).total_seconds())))
    except:
        pass

# showing the current number of social credits
@bot.message_handler(commands=['points'])
def show_points(message):
    if message.chat.type == 'supergroup':
        res = db.show_point(message.from_user.id)
        bot.send_message(message.chat.id, 'у тебя {} баллов нащалника'.format(res[0][0]))


bot.polling(none_stop=True, interval=0)