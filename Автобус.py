import telebot
import geocoder
from geopy.distance import geodesic
from multiprocessing import Process


bot = telebot.TeleBot("2145763251:AAH7lMEcX1jcr-4Y44FzHq7dGIUYdwF2oXk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "0")
bot.infinity_polling()


bot1 = telebot.TeleBot("2132111620:AAFr0nIxkzGDKTZcE5Mx8EaJ1uHp9iijuqQ")
@bot.message_handler(content_types=['text'])
    def send_echo(message):
        h = geocoder.ip('me')
        z,r=h.lat,h.lng
        you = (f"{x} {y}")
        miles = geodesic(f"{z} {r}",you).miles
        bot.send_message(message.chat.id, miles)

bot1.infinity_polling()