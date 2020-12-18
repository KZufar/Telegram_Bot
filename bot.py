import telebot
bot = telebot.TeleBot('1403134489:AAEwiI6UrTBR-Q3IASA4gt6dSBBnKOUpHw0')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()