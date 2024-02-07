import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import random
from tkinter import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am your personal assistant")
    speak("Please tell me how may i help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 4000
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again please....")
        print("Say that again please....")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail
    server.login('Enter your email id', 'Enter your username')
    server.sendmail('Enter your email id', to, content)
    server.close()




def callVirtualAssistant():
    os.system('cls')
    #This function will clean any command before execution of this python file
    # wishMe()
    #username()
    while True:
    # if 1:
        query = takeCommand().lower()  #Converting user query into lower case
    #Logic for executing tasks based on query
        if 'wikipedia' in query:    #if wikipedia found in the query then this block will be executed
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            print("Opening Youtube")
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            print("Opening Google")
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            print("Opening Facebook")
            speak("Opening Facebook")
            webbrowser.open("facebook.com")
        elif 'play music' in query or "play song" in query:
            music_dir = 'C:\\Users\\nehak\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            print("Playing Music")
            speak("Playing Music")
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Ma'am, the time is {strTime}")
        elif 'open code' in query:
            print("Opening VS Code")
            speak("Opening VS Code")
            codePath = 'C:\\Users\\nehak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'send a mail' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                print("Whom should I send")
                speak("Whom should I send")
                to = input()
                sendEmail(to, content)
                print("Email has been sent !")
                speak("Email has been sent !")
            except Exception as e:
                #print(e)
                print("I am not able to send this email")
                speak("I am not able to send this email")
        elif 'how are you' in query:
            print("I am fine. Thank you!")
            speak("I am fine. Thank you!")
            print("How are you?")
            speak("How are you?")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        #elif 'exit' or 'bye' or 'stop' in query:
           # speak("Thanks for giving me your time")
           # exit()
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Neha.")     
        elif 'joke' in query:
            result = pyjokes.get_joke()
            print(result)
            speak(result)
        
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")  
            print("This is the searching results I have found")
            speak("This is the searching results I have found")       
            webbrowser.open(query)
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        elif "why you came to world" in query:
            speak("Thanks to Neha. further It's a secret")
        elif ' what is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I am your virtual assistant created by Neha")
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Neha ")
        # elif 'shutdown system' in query:
        #     speak("Hold On a Sec ! Your system is on its way to shut down")
        #     subprocess.call('shutdown\\p\\f')
        # elif 'don\'t listen' or 'stop listening' in query:
        #     speak("for how much time you want to stop listening commands")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)
        
        elif 'news' in query:
            print("Opening a news site")
            speak("Opening a news site")
            webbrowser.open("hindustantimes.com")


def main_screen():
      global screen
      screen = Tk()
      screen.title()
      screen.geometry("300x250")
      screen.config(bg="black")


      name_label = Label(text = "Welcome to the Voice Assistant",width = 300, bg = "black", fg="white", font = ("Calibri", 22))
      name_label.pack()
    
      
      microphone_photo = PhotoImage(file = "gif.gif")
      microphone_button = Button(image=microphone_photo, command = wishMe)
      microphone_button.pack(pady=10)

      name_label = Label(text = "Tap to Start",width = 300, bg = "black", fg="blue", font = ("Calibri", 16))
      name_label.pack()

      
      microphone_button1 = Button(text="Tap to Speak", bg='green', fg='black',font=("calibri", 16), command = callVirtualAssistant)
      microphone_button1.pack(pady=10)

      screen.mainloop()
main_screen()
#python version-3.10