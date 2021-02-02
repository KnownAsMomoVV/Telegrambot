import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import subprocess
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

"""
- `/random` - Random nummer 

- `/time` - Aktuelle zeit

- `/up - Zeigt uptime / zeit wie lange der Raspberry schon laeuft

- `/reboot` - Startet den Raspberry neu

- `/memo` - Ochhh memoo

"""
"NEW STUFF"



"NEW STUFF"

bot = telepot.Bot('1506236736:AAHLhlQEJkopd52LgtMvUIml5fk0pfZjTB8')



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

        raspberryinfo = subprocess.check_output("cat /proc/cpuinfo", shell=True)
        bot.sendMessage(chat_id, raspberryinfo)



    elif command == "/testing2":
        bot.sendMessage(chat_id, 'testing custom keyboard',reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                                    [InlineKeyboardButton(text="btn1",callback_data= 'I have Nothing To do'), InlineKeyboardButton(text="btn2",callback_data='0'),InlineKeyboardButton(text="btn3",callback_data='0'), InlineKeyboardButton(text="btn4",callback_data='0')],
                                    [InlineKeyboardButton(text="btn1",callback_data='yep')]
                                ]
                            ))

commands = """

| -`(/random` - Random nummer)
|- `(/time` - Aktuelle zeit), 
| -`(/up` - Zeigt uptime / zeit wie lange der Raspberry schon laeuft)
| - `(/reboot` / startet den Raspberry neu)
| - `(/memo` / Occhhhhh Memo)
 """

MessageLoop(bot, handle).run_as_thread()

print("Empfange Command...")

while 1:
    time.sleep(10)
