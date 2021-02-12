#-----------------------------------------------------"Importierte Librarys"-------------------------------------------------#
import time                             # Time ist für den befehl time (zeitausgabe)
import random                           # Randit befehl dieser kann etwas zufällig machen
import datetime                         # Datetime ist für das Datum & die uhrzeit
import telepot                          # Telegram bot API & Library (dies ist damit der Code mit der Telegram API komuniziert bzw. sich verbindet)
from telepot.loop import MessageLoop    # für das msg loop  (damit dauerhaft nachichten jederzeit geschickt werden können und der code sich dauerhaft wiederholt)
import subprocess                       # führ prozesse auf dem Raspberry aus und kann den output wiedergeben 
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton # eine library für telegram mit der man Buttons statt commands benutzen kann
import pyowm                            # OpenWeatherMap API ist für die Wetter API verantwortlich und fragt die API nach Hamburg DE ab (fragt das wetter ab)
import requests                         # Fragt daten einer website ab und kann diese als output wiedergeben meist auch Scraper genannt
import os                               # Für weitere befehle die man mit dem Raspberry machen kann (Das betriebssystem (cmd) steuern)
#-----------------------------------------------------"Import (END)"-------------------------------------------------#



#-----------------------------------------------------"OpenWeatherMap API"-------------------------------------------------#
# Openweathermap API diese greift auf die API zu und gibt dem code die daten die er benögtigt nämlich genau die für Hamburg
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7fb2b22140ccaf6131939f624e8f3444&units=metric'.format("Hamburg, DE") 

res = requests.get(url) # Datenabfrage an die Website
data = res.json()       # Man definiert die request datei als data, damit diese angenehmer zum verwenden ist
temperatur = data['main']['temp']       # data (datenabfrage an API) -> "main" ist sogesagt einer der Ordner in der API und dort wählt man den Unterordner "temp" dieser steht für temperatur
tempmax = data["main"]['temp_max']      # Hier ist es das selbe prinzip nur mit "temp_max" (maximale temperatur)
tempmin = data["main"]['temp_min']      # Hier das selbe für minimale temperatur
wind_schnelligkeit = data['wind']['speed'] # Hier das selbe für windgeschwindigkeit
Beschreibung = data['weather'][0]['description'] # Hierbei muss man je nach API auf die bezeichnun und "unterordner" achten
#----------------------------------------------------"OpenWeatherMap API (END)"-------------------------------------------------#




#-----------------------------------------------------"TelegramBot Token & github verzeichnis"-------------------------------------------------#

git = "https://github.com/KnownAsMomoVV?tab=repositories"
bot = telepot.Bot('1506236736:AAHLhlQEJkopd52LgtMvUIml5fk0pfZjTB8')
TOKEN = "1506236736:AAHLhlQEJkopd52LgtMvUIml5fk0pfZjTB8"

#-----------------------------------------------------"TelegramBot Token & github verzeichnis (END)"-------------------------------------------------#



#-----------------------------------------------------------------"Befehle für den BOT"-------------------------------------------------#
def handle(msg):
    chat_id = msg['chat']['id'] # Chat_ID ist für Telegram nötig damit eine nachicht gesendet werden kann
    command = msg['text']  # Command definieren damit Telegram weiß was dies ist
    text = msg["text"]



    print("Got command:") + command     # Command erhalten (das senden des command hat funktioniert)

    if command == '/random':

        bot.sendMessage(chat_id, random.randint(1, 6))  # Zufalls befehl randit zufalls zahl aus 1 - 6

    elif command == '/time':

        bot.sendMessage(chat_id, str(datetime.datetime.now()))  # Derzeitige zeit & datum



    elif command == "/up":

        gaming = subprocess.check_output("uptime", shell=True)  # Laufzeit des bots seit dem lezten neustart (dazu noch wie viele personen gerade mit dem Pi per SHH verbunden sind)
        bot.sendMessage(chat_id, gaming)    # bot sendMessage befehl ist festgelegt von der Telepot library und wird immer verwendet wenn der bot etwas senden soll


    elif command == "/help":    # Zeigt alle Commands die man verwenden kann

        bot.sendMessage(chat_id, commands) # Chat_id wir immer benötig damit die nachicht versendet werden kann. Der befehl dahinter ist meist immer der command

    elif command == "/reboot":

        rebootsucces = "Der Raspberry startet neu!"         
        bot.sendMessage(chat_id, rebootsucces)
        rebootpls = subprocess.check_output("sudo reboot", shell=True) # Startet den Raspberry Pi neu
        bot.sendMessage(chat_id, rebootpls)

    elif command == "/memo":
                                # Sendet ein Video & eine Audiodatei (+ text)
        audio_url = "https://cdn.sndup.net/3pwb/MEMOOOOO.mp3?token=yPEpUwUvcIXFZ8DN6GLMTRMJD4RZaTdeDNwt7dL_8K0&token_path=%2F3pwb%2F&expires=1610385160"
        image_url = "https://i.ibb.co/DC3vKGD/MEMOO-GUCK.jpg"
        feini = "MEMO"
        bot.sendMessage(chat_id, feini)
        bot.sendPhoto(chat_id, image_url)
        bot.sendAudio(chat_id, audio_url)


    elif command == "/info":

        raspberryinfo2 = subprocess.check_output("cat /proc/cpuinfo", shell=True)       # Systeminformationen über den Raspberry
        bot.sendMessage(chat_id, raspberryinfo2)

    elif command == "/modell":

        raspberryinfo = subprocess.check_output("cat /sys/firmware/devicetree/base/model", shell=True)
        bot.sendMessage(chat_id, raspberryinfo)


    elif command == "/wetter":

        bot.sendMessage(chat_id,("Derzeitige temperatur : {} grad in celcius".format(temperatur)))          # Die Temperatur befehle
        bot.sendMessage(chat_id,("Derzeitige Hoechsttemperatur (max) : {} grad in celcius".format(tempmax)))    #.format ist für das formatieren 
        bot.sendMessage(chat_id,("Derzeitige Tiefstemperatur (min) : {} grad in celcius".format(tempmin)))  # dadurch wird nicht der Rohe text ausgegeben
        bot.sendMessage(chat_id,("wind geschwindigkeit : {} m pro sekunde".format(wind_schnelligkeit))) # sondern dieser wird zunächst formatiert
        bot.sendMessage(chat_id,("beschreibung : {}".format(Beschreibung)))   

    elif command == "/github":  

        bot.sendMessage(chat_id,("Github Repository vom Telegram bot"))
        bot.sendMessage(chat_id,git)

    elif command =="/oussama":
        ousamma_url = "https://i.ibb.co/sHyq4Nw/photo-2021-01-11-18-09-04.jpg"
        rip = "An gedanke an unseren mitschueler <3"
        bot.sendMessage(chat_id,ousamma_url)
        bot.sendMessage(chat_id,rip)

#-----------------------------------------------------------------"Befehle für den BOT (END)"-------------------------------------------------#


#-----------------------------------------------------------------"Commands für /help"--------------------------------------------------------#
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

#-----------------------------------------------------------------"Commands für /help (END)"-------------------------------------------------#


MessageLoop(bot, handle).run_as_thread() # Damit der Bot durchgängig auf nachichten reagiert & diese auch sendet

print("Empfange Command...") # Damit man erkennt das der Bot einwandfrei gestartet ist

while 1:
    time.sleep(10)


