import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import subprocess
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import pyowm
import requests
import os

"Stuff2"

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7fb2b22140ccaf6131939f624e8f3444&units=metric'.format("Hamburg, DE")

res = requests.get(url)
data = res.json()
temperatur = data['main']['temp']
tempmax = data["main"]['temp_max']
tempmin = data["main"]['temp_min']
wind_schnelligkeit = data['wind']['speed']
GeoBreite = data['coord']['lat']
GeoLeange = data['coord']['lon']
Beschreibung = data['weather'][0]['description']


"""
- `/random` - Random nummer 

- `/time` - Aktuelle zeit

- `/up - Zeigt uptime / zeit wie lange der Raspberry schon laeuft

- `/reboot` - Startet den Raspberry neu

- `/memo` - Ochhh memoo

"""
"NEW STUFF"



"NEW STUFF"
git = "https://github.com/KnownAsMomoVV?tab=repositories"


bot = telepot.Bot('1506236736:AAHLhlQEJkopd52LgtMvUIml5fk0pfZjTB8')

TOKEN = "1506236736:AAHLhlQEJkopd52LgtMvUIml5fk0pfZjTB8"


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    text = msg["text"]



    print("Got command:") + command

    if command == '/random':

        bot.sendMessage(chat_id, random.randint(1, 6))

    elif command == '/time':

        bot.sendMessage(chat_id, str(datetime.datetime.now()))



    elif command == "/up":

        gaming = subprocess.check_output("uptime", shell=True)
        bot.sendMessage(chat_id, gaming)


    elif command == "/help":

        bot.sendMessage(chat_id, commands)

    elif command == "/reboot":

        rebootsucces = "Der Raspberry startet neu!"
        bot.sendMessage(chat_id, rebootsucces)
        rebootpls = subprocess.check_output("sudo reboot", shell=True)
        bot.sendMessage(chat_id, rebootpls)

    elif command == "/memo":

        audio_url = "https://cdn.sndup.net/3pwb/MEMOOOOO.mp3?token=yPEpUwUvcIXFZ8DN6GLMTRMJD4RZaTdeDNwt7dL_8K0&token_path=%2F3pwb%2F&expires=1610385160"
        image_url = "https://i.ibb.co/DC3vKGD/MEMOO-GUCK.jpg"
        feini = "MEMO"
        bot.sendMessage(chat_id, feini)
        bot.sendPhoto(chat_id, image_url)
        bot.sendAudio(chat_id, audio_url)


    elif command == "/info":

        raspberryinfo2 = subprocess.check_output("cat /proc/cpuinfo", shell=True)
        bot.sendMessage(chat_id, raspberryinfo2)

    elif command == "/modell":

        raspberryinfo = subprocess.check_output("cat /sys/firmware/devicetree/base/model", shell=True)
        bot.sendMessage(chat_id, raspberryinfo)


    elif command == "/wetter":

        bot.sendMessage(chat_id,("Derzeitige temperatur : {} grad in celcius".format(temperatur)))
        bot.sendMessage(chat_id,("Derzeitige Hoechsttemperatur (max) : {} grad in celcius".format(tempmax)))
        bot.sendMessage(chat_id,("Derzeitige Tiefstemperatur (min) : {} grad in celcius".format(tempmin)))
        bot.sendMessage(chat_id,("wind geschwindigkeit : {} m pro sekunde".format(wind_schnelligkeit)))
        bot.sendMessage(chat_id,("beschreibung : {}".format(Beschreibung)))   

    elif command == "/github":

        bot.sendMessage(chat_id,("Github Repository vom Telegram bot"))
        bot.sendMessage(chat_id,git)

    elif command =="/oussama":
        ousamma_url = "https://i.ibb.co/sHyq4Nw/photo-2021-01-11-18-09-04.jpg"
        rip = "An gedanke an unseren mitschueler <3"
        bot.sendMessage(chat_id,ousamma_url)
        bot.sendMessage(chat_id,rip)


commands = """

| -`(/random` - Random nummer)
|- `(/time` - Aktuelle zeit), 
| -`(/up` - Zeigt uptime / zeit wie lange der Raspberry schon laeuft)
| - `(/reboot` / startet den Raspberry neu)
| - `(/memo` / Occhhhhh Memo)
| - `(/wetter` / derzeitiges wetter in Hamburg DE)
| - `(/info` / Informationen ueber den Raspberry (Erweitert))
| - `(/modell` / Raspberry PI Model)
| - `(/github` / github Repo (TelegramBot))
| - `(/oussama` / Gedanke an unseren oussama)
 """

MessageLoop(bot, handle).run_as_thread()

print("Empfange Command...")

while 1:
    time.sleep(10)


