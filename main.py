import pyttsx3
from requests import Request, request #pip install pyttsx3
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

def news():
    newsapi = NewsApiClient(api_key='d4cb49bf88d7493da38284b5b394ef8a')
   
    data = newsapi.get_top_headlines(language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        speak(y["description"])

def weather():
    city = "Nagpur"
    res = Request.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c651e20acb64c367b992335a8f90c8bd&units=metric").json()
    temp = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(
        f"Temprature is {format(temp2)} degree Celsius \n Weather is {format(temp)}")

if __name__ == "__main__":
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


            

