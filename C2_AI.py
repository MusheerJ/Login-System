'''
source : code with harry 
updated by : MusheerAhmed Jamadar
'''
import pyttsx3
import speech_recognition as sr
import datetime
from time import sleep
from datetime import date
import wikipedia
import webbrowser
import os
import random
import pyjokes
from PyDictionary import PyDictionary
from TicTacToe import *
from passWordGenerator import passWordGenerator
from passWordManager import *
from memo import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def game1():
    randNum = random.randint(11, 20)
    no_of_guesses = 1
    speak("Hint for You , the number is between, 10 to 20")
    while True:
        speak("Tell me a number Marcus.")
        try:
            guess = int(takeCommand())
            if guess == randNum:
                speak(
                    f"congratulations!!! you Guessed the Number Correctly in {str(no_of_guesses)} guesses "
                )
                break
            elif (guess > randNum):
                speak("Your number is greater. Try a smaller one ")
            else:
                speak("Your number is smaller. Try a greater one ")
            no_of_guesses += 1
        except Exception as e:
            pass
            speak("Tell the number again")
            continue


def game2():
    speak("Tell any one , between rock paper and scissor ")
    userInput = takeCommand().lower()
    if userInput == "caesar":
        userInput = "scissor"
    list = ["rock", "paper", "scissor"]
    computerInput = random.choice(list)
    result = [
        "congratulations, You Win", "You Lose, better luck next time",
        "its a Draw"
    ]
    if userInput == "rock" and computerInput == "rock":
        print("Computer Choose : " + computerInput)
        speak(result[2])
    elif userInput == "rock" and computerInput == "paper":
        print("Computer Choose : " + computerInput)
        speak(result[1])
    elif userInput == "rock" and computerInput == "scissor":
        print("Computer Choose : " + computerInput)
        speak(result[0])
    elif userInput == "paper" and computerInput == "rock":
        print("Computer Choose : " + computerInput)
        speak(result[0])
    elif userInput == "paper" and computerInput == "paper":
        print("Computer Choose : " + computerInput)
        speak(result[2])
    elif userInput == "paper" and computerInput == "scissor":
        print("Computer Choose : " + computerInput)
        speak(result[1])
    elif userInput == "scissor" and computerInput == "rock":
        print("Computer Choose : " + computerInput)
        speak(result[1])
    elif userInput == "scissor" and computerInput == "paper":
        print("Computer Choose : " + computerInput)
        speak(result[0])
    elif userInput == "scissor" and computerInput == "scissor":
        print("Computer Choose : " + computerInput)
        speak(result[2])


def game3():
    # speak("with whom  you wanna play ?. With friends or with computer ?")
    # withPlay = takeCommand().lower
    # if withPlay == "friends":
    #     x_player = HumanPlayer('X')
    #     y_player = HumanPlayer("O")
    #     game = TicTacToe()
    #     play(game, x_player, o_player, print_game=True)
    # elif withPlay == "computer":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Marcus!!")
    elif hour >= 12 and hour < 18:
        speak(" Good AfterNoon Marcus!!")
    else:
        speak("Good Evening. Marcus!")
    speak("I am C2. How can i help you Marcus ?")


def takeCommand():
    # it taked microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query} \n")

    except Exception as e:
        # print(e)
        print("Say that again please ")
        speak("I Cannot recognise Marcus ,please say it again")
        return "None"
    return query


def sendEmail(to, content):
    pass


if __name__ == "__main__":
    _ = os.system('cls')
    friday = "C2 VERSION 0.0"
    print(friday)
    WishMe()
    while True:
        # _ = os.system('cls')
        query = takeCommand().lower()
        # query = query.lower()
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia ,")
            print(result)
            speak(result)

        elif "open youtube" in query:
            speak("Opening youtube Marcus")
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            speak("Starting google Marcus")
            webbrowser.open("https://www.google.com/")

        elif "open stack overflow" in query:
            speak("Opening StackoverFlow Marcus")
            webbrowser.open("https://stackoverflow.com/")

        elif "play music" in query:
            pass

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The time now is " + strTime)
            speak("Marcus The time now is " + strTime)

        elif "date" in query:
            today = date.today()
            cdate = today.strftime("%B %d, %Y")
            print("date is " + cdate)
            speak("Marcus today's date is " + cdate)

        elif "open vs code" in query:
            speak("Starting VS code Marcus")
            path = r"C:\Users\mushe\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)

        elif "open pycharm" in query:
            speak("Starting pycharm Marcus")
            path = r"C:\PyCharm Community Edition 2020.2.1\bin\pycharm64.exe"
            os.startfile(path)

        elif "open chrome" in query:
            path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            speak("Starting Chrome Marcus")
            os.startfile(path)

        elif "open whatsapp" in query:
            speak("opening whats app !!!!")
            webbrowser.open("https://web.whatsapp.com/")

        elif "open instagram" in query:
            speak("opening instagram !!!!")
            webbrowser.open("https://www.instagram.com/")

        elif "email to mushir" in query:
            try:
                speak("what should be in the mail marcus ?")
                content = takeCommand()
                to = "musheerjamadar1024@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent marcus")
            except Exception as e:
                speak("Sorry marcus there was some error in sending the Email")

        elif "quit" in query:
            speak("Thankyou Marcus for using me. Visit me again . Byee!")
            break

        elif "search for" in query:
            query = query.replace("search for", "")
            speak("Searching for " + query)
            url = "https://www.google.com.tr/search?q={}".format(query)
            webbrowser.open(url)

        elif "show videos" in query:
            query = query.replace("show videos of", "")
            speak("Showing  videos for " + query)
            url = "https://www.youtube.com/results?search_query={}".format(
                query)
            webbrowser.open(url)

        elif "my playlist" in query:
            speak("Playing")
            url = "https://www.youtube.com/watch?v=NxQHMidmLqU&list=PLv0jTTZA-VfYBbeZC0reJ9mdtQoTTO053&index=1"
            webbrowser.open(url)

        elif "about you" in query:
            speak(
                "I am C2 . I am the simplest variant of AI . Marcus is the one who created me . Thankyou for asking  about me ."
            )

        elif "game" in query:
            gameList = [1, 2, 3]
            gameNum = random.choice(gameList)
            if gameNum == 1:
                speak("Lets play a Number Guessing Game, Marcus ")
                game1()
            elif gameNum == 2:
                speak("Lets play , rock paper and scissor ! ")
                game2()
            elif gameNum == 3:
                speak("Lets play,Tic Tac Toe ")
                game3()

        elif "joke" in query:
            speak("Here is a joke for You ..")
            speak(pyjokes.get_joke())

        elif "meaning" in query:
            dict = PyDictionary()
            query = query.replace("meaning of", "")
            meaning = dict.meaning(query)
            print(meaning)
            speak(meaning)

        elif "sleep" in query:
            speak("for How many minutes should I sleep . ")
            minute = int(takeCommand())
            # seconds = random.randint(0,50)
            speak(f"Sleeping for {str(minute)} minutes ")
            sleep(minute * 60)
            speak("Sleep complete .")

        elif "generate password" in query:
            speak(
                "Please fill the details required to generate a password ...")
            passWord = passWordGenerator()
            speak("Pass word generated Successfully .....")
            print(f"The generated password is {passWord}")

        elif "save password" in query:
            speak(
                "Please follow the steps shown on the screen to save the passWord"
            )
            savePassword()
            speak("Password saved successfully......")

        elif "memo" in query:
            speak("Opening Memo for you .....")
            memoWriting()
            sleep(3)
            speak("Do you want to read the meme . Say yes to read the Memo ")
            choice = takeCommand()
            if choice == "yes":
                memoReading()
