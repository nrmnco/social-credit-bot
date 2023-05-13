import CONFIG
import telebot
from queries import Database


bot = telebot.TeleBot(CONFIG.TOKEN)
db = Database()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'дарова ептеть')


# adding and removing credits
@bot.message_handler(content_types=['sticker'])
def social_credit(message):
    try:
        if message.chat.type == 'supergroup' and message.reply_to_message.from_user.is_bot == False and message.reply_to_message.from_user.id != message.from_user.id:
            if message.sticker.emoji == '😄' and message.sticker.set_name == 'PoohSocialCredit':
                db.adding_point(message.reply_to_message.from_user.id)
                res = db.show_point(message.reply_to_message.from_user.id)
                bot.send_message(message.chat.id, 'плюс миска рис для {} \nнащалника у тебя {} ачков'.format(message.reply_to_message.from_user.first_name, res[0][0]))

            elif message.sticker.emoji == '😞' and message.sticker.set_name == 'PoohSocialCredit':
                db.subtract_point(message.reply_to_message.from_user.id)
                res = db.show_point(message.reply_to_message.from_user.id)
                bot.send_message(message.chat.id, 'минус миска рис для {} \nв санаторий его у него {} ачков'.format(message.reply_to_message.from_user.first_name, res[0][0]))
    except:
        pass

# showing the current number of social credits
@bot.message_handler(commands=['points'])
def show_points(message):
    if message.chat.type == 'supergroup':
        res = db.show_point(message.from_user.id)
        bot.send_message(message.chat.id, 'у тебя {} баллов нащалника'.format(res[0][0]))


bot.polling(none_stop=True, interval=0)