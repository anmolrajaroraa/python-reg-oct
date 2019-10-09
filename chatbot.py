from datetime import *
import os, subprocess, random

helloIntent = ['hi', 'hello', 'hey', 'namaste', 'hola', 'bonjour']
dateIntent = ['date please', 'what\'s the date today', 'can you tell me today\'s date']
timeIntent = ['time please', 'what\'s the time now', 'can you tell me current time']
musicIntent = ['play some music', 'play a song', 'play something for me']

while True:
    message = input("Enter your message: ")

    # if message == 'hi' or message == 'hello' or message == 'hey':
    if message in helloIntent:
        print('hello')
    elif message == 'how are you':
        print('I am fine')
    elif message in dateIntent:
        today = date.today()
        print(f"{today.day}/{today.month}/{today.year}")
    elif message in  timeIntent:
        now = datetime.now()
        print(now.strftime("%a %d %b %Y %I:%M:%S %p"))
    elif message in musicIntent:
        os.chdir('/Users/anmolrajarora/Documents/python')
        songs = os.listdir()
        song = random.choice(songs)
        subprocess.call(['open', song])
    elif message == 'bye' or message == 'ok bye':
        print('bye')
        quit()
    else:
        print('I don\'t understand')