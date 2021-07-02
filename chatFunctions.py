import datetime
import os
import random
import shutil
import subprocess
import time
# from bs4 import BeautifulSoup
# import win32com.client as wincl
# from urllib.request import urlopen
# import tkinter as tk
import webbrowser
from datetime import datetime
from random import randrange
import pyjokes
# import wolframalpha
import pyttsx3
import requests
import simplejson as json
import speech_recognition as sr
import wikipedia
# import winshell
# import feedparser
# import smtplib
# import ctypes
# from twilio.rest import Client
# from clint.textui import progress
from ecapture import ecapture as ec
from selenium import webdriver
import chatFunctions

# import operator

# print(json.__doc__)


# engine is something awesome
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 250)
engine.setProperty('voice', voices[1].id)


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

    speak(f"Is your name {uname}?")
    answer = takeCommand()

    while "yes" not in answer:
        uname = takeCommand()
        speak(f"Is your name {uname}?")
        answer = takeCommand()

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
        said = r.recognize_google(audio, language='en-in')
        speak(f"User said: {said}\n")
        print(f"User said: {said}\n")

    except Exception as e:
        print("EXCEPTION:" + str(e))
        speak("Could not understand.Can you repeat what you have said, please.")
        return "None"

    return said


def current_working_dir():
    print(os.getcwd())
    speak(os.getcwd())


def take_picture():
    ec.capture(0, False, "poza.jpg")


def play_game(game_play):

    while True:
        if 'bye' in game_play or 'stop playing' in game_play or 'end' in game_play or 'stop' in game_play:
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


def wiki_search(searched):
    if 'search for' in searched:
        ser = searched.replace("search for", "")
    else:
        ser = searched.replace("search", "")

    f = open(f"{ser}.txt", "w")
    f.write(wikipedia.summary(ser))
    engine.setProperty('rate', 150)
    speak(wikipedia.summary(ser))
    print(wikipedia.summary(ser))


def search_something(thing):
    searched_querry = ""

    for element in thing:
        searched_querry = searched_querry + "+" + element

    url = "https://www.google.com/search?q=" + searched_querry
    chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

    driver = webdriver.Chrome(chrome_path)
    driver.get(url)


def get_time():
    now = datetime.datetime.now()
    speak(f"The time is{now.hour, now.minute}")


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


def set_timer(data):
    data = data.replace("set", "")
    data = data.replace("the timer", "")
    data = data.replace("for", "")

    if "minute" or "minutes" in data:
        data = data.replace("minutes", "")
        data = data.replace("minute", "")
        data = int(data)
        time.sleep(60*data)
        speak(f"Your {data} minutes have ended.")

    if "second" or "seconds" in data:
        data = data.replace("seconds", "")
        data = data.replace("second", "")
        data = int(data)
        time.sleep(data)
        speak(f"Your {data} seconds have ended.")


def get_location(location):
    location = location.replace("where is", "")
    speak("User asked to Locate")
    speak(location)
    webbrowser.open("https://www.google.ro/maps/place/" + location + "")


def get_ecoin_value(ecoin):

    if 'ethereum' in ecoin:
        ecoin = 'ethereum'

    if 'bitcoin' in ecoin:
        ecoin = 'bitcoin'

    value = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={ecoin}&vs_currencies=eur')
    a = json.loads(value.text)

    speak(f"1 {ecoin} will cost you " + str(a[f"{ecoin}"]["eur"]) + " EURO.")
    print(f"1 {ecoin} will cost you " + str(a[f"{ecoin}"]["eur"]) + " EURO.")


def no_answer_questions(not_answered):
    not_answered = not_answered.lower()

    if not_answered != 'none':
        f = open("intrebari.txt", "a")
        f.write(not_answered + "\n")
        f.close()
        speak('I don t know how to respond to this question. Try again!')
    else:
        speak('Microphone got no input')


def play_music(song):
    song = song.replace("music", "")
    speak("Opening the best songs for you")
    link = ""

    if "some":
        song = song.replace("some", "")

    if "play":
        song = song.replace("play", "")
    for word in song:
        link = word + link
    webbrowser.open(f"https://music.youtube.com/search?q={song}")


def system_state(action):
    if "shutdown" in action:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
    elif "restart" in action:
        speak("Restarting computer.Please wait.")
        subprocess.call(["shutdown", "/r"])
    elif "log off" in action:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

