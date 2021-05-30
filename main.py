import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import datetime
import webbrowser
import os
import pyjokes
import time
import shutil
from random import randrange
import wikipedia
import requests
import json
import random
# import winshell
# import feedparser
# import smtplib
# import ctypes
# from twilio.rest import Client
# from clint.textui import progress
from ecapture import ecapture as ec
# from bs4 import BeautifulSoup
# import win32com.client as wincl
# from urllib.request import urlopen
# import tkinter
# import operator

# print(json.__doc__)

# engine is something awesome
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 250)
engine.setProperty('voice', voices[1].id)


j_file = open("intelepciune.json", "r")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def say_hi():

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir")

    elif hour <= 19:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    assname = "Geo"
    speak("I am your assistant" + assname)


def usrname():
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.".center(columns), uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Im listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        data = r.recognize_google(audio, language='en-in')
        speak(f"User said: {data}\n")
        print(f"User said: {data}\n")

    except Exception as e:
        print(e)
        speak("Could not understand.Can you repeat what you have said, please.")
        return "None"

    return data


def take_picture():
    ec.capture(0, False, "poza.jpg")


def play_game(game_play):

    while True:
        if 'bye' in game_play or 'stop playing' in game_play or 'end' in game_play:
            break

        speak("What game would you like to play?")
        game_name = takeCommand()

        if 'guess' in game_name or 'guess the number' in game_name or 'number ' in game_name:
            speak("What s the limit?")
            x = takeCommand()
            if x.isnumeric():
                x = int(x)

            while type(x) != int:
                speak("Could not understand, can you repeat?")
                x = takeCommand()
                if x.isnumeric():
                    x = int(x)

            random_number = random.randint(1, x)
            guess = 0

            while guess != random_number:
                speak(f'Guess a number betweeen 1 and {x}: ')
                speak("Tell me a number: ")
                guess = takeCommand()
                if guess.isnumeric():
                    guess = int(guess)

                while type(guess) != int:
                    speak("Couldn t understand, can you repeat?")
                    guess = takeCommand()
                    if guess.isnumeric():
                        guess = int(guess)

                if guess < random_number:
                    speak("Too low")

                elif guess > random_number:
                    speak("Too high")

                else:
                    speak(f"On the point.The number was {random_number}")
                    speak("Do you want to continue?")
                    cont = takeCommand()
                    if 'yes' in cont:
                        game_name = 'guess the number'
                    else:
                        break

        if 'rock' in game_name or 'paper' in game_name or 'scissors' in game_name:
            speak("TO BE ADDED")

        else:
            speak("There is no game with that name.")


def get_random_number():
    speak("What is the first number?")
    first_limit = takeCommand()

    if first_limit.isnumeric():
        first_limit = int(first_limit)

    while type(first_limit) != int:
        speak("Could not understand, can you repeat?")
        first_limit = takeCommand()
        if first_limit.isnumeric():
            first_limit = int(first_limit)

    speak("What is the second number?")
    b = takeCommand()

    if b.isnumeric():
        b = int(b)

    while type(b) != int:
        speak("Could not understand, can you repeat?")
        b = takeCommand()
        if b.isnumeric():
            b = int(b)

    if first_limit > b:
        aux = first_limit
        first_limit = b
        b = aux

    speak(randrange(first_limit, b))


def search_something():
    thing = takeCommand()
    webbrowser.open(f"https://{thing}.com")


def to_do(to_do_info):
    if 'add' in to_do_info:
        to_do_info = to_do_info.replace('add', "")

    to_do_info = to_do_info.replace('to do', "")

    if 'list' in to_do_info:
        to_do_info = to_do_info.replace('list', "")

    td = open("de_facut.txt", "a")
    td.write(to_do_info + "\n")
    td.close()
    speak(f"{to_do_info} added to your to do list!")


def get_location(location):
    location = location.replace("where is", "")
    speak("User asked to Locate")
    speak(location)
    webbrowser.open("https://www.google.ro/maps/place/" + location + "")


def no_answer_questions(not_answered):
    not_answered = not_answered.lower()
    if not_answered != 'none':
        f = open("intrebari.txt", "a")
        f.write(not_answered + "\n")
        f.close()
        speak('I don t know how to respond to this question. Try again!')
    else:
        speak('Microphone got no input')


if __name__ == '__main__':

    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file

    clear()
    # say_hi()
    # usrname()
    while True:

        querty = str(takeCommand().lower())

        if 'time' in querty:
            now = datetime.datetime.now()
            speak(f"The time is{now.hour, now.minute}")

        elif 'game' in querty:
            play_game(querty)

        elif 'search' in querty or 'search for' in querty:
            if 'search for' in querty:
                ser = querty.replace("search for", "")
            else:
                ser = querty.replace("search", "")

            engine.setProperty('rate', 150)
            speak(wikipedia.summary(ser))
            print(wikipedia.summary(ser))

        elif 'google' in querty or 'gogu' in querty:
            speak("Opening Google.Com")
            webbrowser.open("https://google.com/")

        elif 'university' in querty:
            speak("Opening Hybrid Learning")
            webbrowser.open("https://online.ase.ro/")

        elif 'picture' in querty:
            take_picture()

        elif 'youtube' in querty:
            speak("Opening the best songs for you")
            webbrowser.open("https://youtube.com/")

        elif 'stack overflow' in querty:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://stackoverflow.com/")

        elif 'joke' in querty or 'jokes' in querty:
            speak(pyjokes.get_joke())

        elif 'generate' and 'random' in querty:
            get_random_number()

        elif 'league of legends' in querty or 'lol' in querty:
            speak("Good luck to no feeders")
            path = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
            os.startfile(path)

        elif 'valorant' in querty:
            speak("Good luck Omen")
            path = "C:\\Riot Games\\VALORANT\\live\\VALORANT.exe"
            os.startfile(path)

        elif 'who made you' in querty or 'who created you' in querty:
            speak('I have been created by Klaus')

        elif 'git' in querty or 'github' in querty:
            speak('Programming day.')
            webbrowser.open("https://github.com/Klaus404")

        elif 'school' in querty:
            path = "C:\\Users\\Claudiu\\OneDrive\\Desktop\\facultate"
            os.startfile(path)

        elif "wikipedia" in querty:
            webbrowser.open("https://wikipedia.com/")

        elif 'bitcoin' in querty:
            btc = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur')
            a = json.loads(btc.text)
            speak("1 bitcoin will cost you " + str(a["bitcoin"]["eur"]) + " EURO.")

        elif 'ethereum' in querty or 'coin' in querty:
            eth = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur')
            a = json.loads(eth.text)
            speak("1 ethereum will cost you " + str(a["ethereum"]["eur"]) + " EURO.")

        elif "where is" in querty:
            get_location(querty)

        elif 'good job' in querty:
            speak("Thank you sir!")

        elif 'beautiful' in querty or 'pretty' in querty:
            speak("Im pretty sure it is Beatrice!")

        elif "what is" in querty or "who is" in querty:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("8TJH9Y-4EJPQWA9V7")
            res = client.query(querty)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "will you be my girlfriend" in querty or "will you be my boyfriend" in querty:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in querty:
            speak("I'm fine, glad you me that")

        elif "i love you" in querty or "love you" in querty:
            speak("It's hard to understand")

        elif 'is love' in querty:
            speak("It is 7th sense that destroy all other senses")

        elif 'search' in querty or 'play' in querty:
            querty = querty.replace("search", "")
            querty = querty.replace("play", "")

            if 'for' in querty:
                querty = querty.replace("for", "")

            webbrowser.open(querty)

        elif 'shutdown system' in querty:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'search' in querty or 'find' in querty:
            search_something()

        elif "restart" in querty:
            subprocess.call(["shutdown", "/r"])

        elif "log off" in querty or "sign out" in querty:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'exit' in querty:
            speak("Thanks for giving me your time")
            exit()

        elif 'bye' in querty:
            speak("Bye sir")
            break

        elif 'add' and 'to do' in querty:
            to_do(querty)

        else:
            no_answer_questions(querty)

        time.sleep(2)
