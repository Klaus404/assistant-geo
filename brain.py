import os
import time
import chatFunctions


def go_Geo():

    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file

    clear()
    # say_hi()
    # usrname()

    sem = 1

    while sem:

        querty = str(chatFunctions.takeCommand().lower())

        if 'time' in querty and 'timer' not in querty:
            chatFunctions.get_time()

        elif 'game' in querty:
            chatFunctions.play_game(querty)

        elif 'summary' in querty or 'wiki summary' in querty:
            chatFunctions.wiki_search(querty)

        elif 'google' in querty or 'gogu' in querty:
            chatFunctions.openGogu()

        elif 'university' in querty:
            chatFunctions.openAse()

        elif 'picture' in querty:
            chatFunctions.take_picture()

        elif "music" in querty:
            chatFunctions.play_music(querty)

        elif 'stack overflow' in querty:
            chatFunctions.openStack()

        elif 'joke' in querty or 'jokes' in querty:
            chatFunctions.joker()

        elif 'generate' in querty and 'random' in querty:
            chatFunctions.get_random_number()

        elif 'league of legends' in querty or 'lol' in querty:
            chatFunctions.openLol()

        elif 'valorant' in querty:
            chatFunctions.openValorant()

        elif 'who made you' in querty or 'who created you' in querty:
            chatFunctions.speak('I have been created by Klaus')

        elif 'git' in querty or 'github' in querty:
            chatFunctions.openGitHub()

        elif 'school' in querty and 'folder' in querty:
            chatFunctions.openSchoolFolder()

        elif 'bitcoin' in querty or 'ethereum' in querty or 'coin' in querty:
            chatFunctions.get_ecoin_value(querty)

        elif "where is" in querty:
            chatFunctions.get_location(querty)

        elif 'good job' in querty:
            chatFunctions.speak("Thank you sir!")

        elif 'beautiful' in querty or 'pretty' in querty:
            chatFunctions.speak("Im pretty sure it is Beatrice!")

        # elif "what is" in querty or "who is" in querty:
        #
        #     # Use the same API key
        #     # that we have generated earlier
        #     app_id = "8TJH9Y-4EJPQWA9V7"
        #     client = wolframalpha.Client(app_id)
        #     res = client.query(querty)
        #     answear = next(res.results).text
        #     print(answear)
        #     speak(answear)

        elif "will you be my girlfriend" in querty or "will you be my boyfriend" in querty:
            chatFunctions.speak("I'm not sure about, may be you should give me some time")

        elif "directory" in querty or "where am i" in querty:
            chatFunctions.current_working_dir()

        elif "how are you" in querty:
            chatFunctions.speak("I'm fine, glad you me that")

        elif "i love you" in querty or "love you" in querty:
            chatFunctions.speak("It's hard to understand")

        elif 'is love' in querty:
            chatFunctions.speak("It is 7th sense that destroy all other senses")

        # elif 'search' in querty or 'play' in querty:
        #     querty = querty.replace("search", "")
        #     querty = querty.replace("play", "")
        #
        #     if 'for' in querty:
        #         querty = querty.replace("for", "")
        #
        #     webbrowser.open(querty)

        elif 'search' in querty or 'find' in querty:
            chatFunctions.search_something(querty)

        elif 'shutdown system' in querty or "restart" in querty or "log off" in querty:
            chatFunctions.system_state(querty)

        elif 'add' and 'to do' in querty:
            chatFunctions.to_do(querty)

        elif "timer" in querty or "set timer" in querty:
            chatFunctions.set_timer(querty)

        elif 'repeat' in querty and 'me' in querty:
            chatFunctions.speak(querty)

        elif 'exit' in querty or 'bye' in querty:
            chatFunctions.speak("Bye sir, thanks for giving me your time.")
            sem = 0

        else:
            chatFunctions.no_answer_questions(querty)

        time.sleep(1)


def ItSOver():
    chatFunctions.speak("Bye sir, see you next time!")
    quit()
