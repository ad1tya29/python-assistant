This is a python virtual assistant which comes in handy with many features like getting news, weather, playing songs, searching a query etc. This program runs mainly due to the help from the extensive library support which python provides including some of the most important like speech recognition, pyttsx3(text to speech), and many more. 

All the modules and packages required for this Voice assistant to work:
import pyttsx3
from requests import Request, request #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
from newsapi import NewsApiClient


Initializing Speech recognition and Input Output Functions:

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def greet():

    speak("Welcome Aditya")


def speak(audio):

    engine.say(audio)
    engine.runAndWait()



Just like this we define various functions assigned to various queries they fetch.

The logic of executing the methods goes here:

while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' or 'music' in query:
            music_dir = 'C:\VA - New Music Releases Week 28 of 2022 (Mp3 320kbps Songs) [PMEDIA] ⭐️'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

    

        elif 'email to someone' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jainaditya.ngp@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Email is not sent")    

        elif 'news' or 'tell me news' in query:
            news()

        elif 'thank you'  in query:
            speak("welcome")
            
        elif 'weather' in query:
            speak("here is the weather")
            weather()

        elif ("joke" in query):
            speak(pyjokes.get_joke())


            

