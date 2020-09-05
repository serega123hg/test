import requests
import telebot
from telebot.types import Message
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup


TOKEN = "740790711:AAHeei-Xi5r8YCYxuMelZZuj5VXWc9BID4U"
bot = telebot.TeleBot(TOKEN)
# post_id = "post-173426930_539"
useru = {}





@bot.message_handler(commands = ['start'])
def hello(message):
	try:
		global useru
		#global useru[f"{message.from_user.id}"] = "post-173426930_539"
		#print(message.from_user)
		if f"{message.from_user.id}" not in useru:
			useru[f"{message.from_user.id}"] = "post-173426930_544"

		bot.reply_to(message, "Добрый вечер, я диспетчер, если хочешь проверить, нет ли новых постов, просто отправь '1'")
	except:
		k = 0


@bot.message_handler(func=lambda message: True)
def smile(message: Message):
	#global post_id
	global useru
	post_id = useru[f"{message.from_user.id}"]
	try:
		page = requests.get("https://vk.com/prepod_mtuci").text
		soup = BeautifulSoup(page)
		if message.text == "1":
			#current_post = soup.find('div', {'id': f'{post_id}'}).find("div", class_="wall_post_text").get_text()
			for i in range(1, 100):
				if soup.findAll('div', {'class': 'post'})[i]["id"] == post_id:
					bot.reply_to(message, "Увы, на этом всё")
					break
				else:
					bot.reply_to(message, soup.findAll('div', {'class': 'post'})[i].find("div", class_="wall_post_text").get_text())
			useru[f"{message.from_user.id}"] = soup.findAll('div', {'class': 'post'})[1]["id"]

		else:
			bot.reply_to(message, "Каво?")
	except:
		bot.reply_to(message, "Я сломался(")


if __name__ == '__main__':
		bot.infinity_polling(True)
