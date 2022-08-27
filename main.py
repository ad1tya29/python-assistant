import json
from urllib.request import urlopen
import pyttsx3
from requests import Request, request
import requests #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from newsapi import NewsApiClient
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def greet():

    speak("Welcome Aditya")


def speak(audio):

    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your assistant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example@xyz.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# def news():
#     newsapi = NewsApiClient(api_key='d4cb49bf88d7493da38284b5b394ef8a')
   
#     data = newsapi.get_top_headlines(language="en", page_size=5)
#     newsData = data["articles"]
#     for y in newsData:
#         speak(y["description"])




if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    greet()
    wishMe()
    
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

        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'music' in query:
            music_dir = 'E:\SONGS\Various Artist - 100 Uplifting Songs (2021) Mp3 320kbps [PMEDIA] ⭐️'    
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

        elif 'news' in query:
             
            try:
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=in&apiKey=d4cb49bf88d7493da38284b5b394ef8a')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

                    if i==4:
                        break
            except Exception as e:
                 
                print(str(e))
 

        elif 'thank you'  in query:
            speak("welcome")
            
        


        elif ("joke" in query):
            speak(pyjokes.get_joke())
            print()


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")






            

