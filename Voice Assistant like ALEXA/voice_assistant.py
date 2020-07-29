import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
#sapi5 is speech api(to take voice )
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=6 and hour<8:
        print('Good Morning User')
        speak("Hey User")
    elif hour>=12 and hour<18:
        print('Good Afternoon User')
        speak("Hey User")
    else :
        print('Hello User!!!')
        speak("Hey User")
    speak("How may I help you")

def takeCommand():
    """

    It takes audio input and returns string output

    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        """
        To pause staring speak
        """
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognising.... Wait")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
 
    except :
        print("Speak again Unable to recognise")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    
    #logic for executing the task
    while True:
        query = takeCommand().lower()
        if 'bye' in query:
            speak('Bye bye')
            break
        elif 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace('Wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)        
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("youtube.com")
        elif 'open github' in query:
            speak('Opening Github')
            webbrowser.open("github.com")
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,len(songs))]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is {strTime}")
            speak(f"Sir the time is {strTime}")
        elif 'play video' in query:
            tom_dir = 'path'
            toms = os.listdir(tom_dir)
            print(toms)
            os.startfile(os.path.join(tom_dir,toms[random.randrange(0,len(toms))]))
        elif 'open calendar' in query:
            speak('Opening Google Calendar ')
            webbrowser.open("https://calendar.google.com/calendar/r?tab=rc")
        elif 'open course' in query:
            speak('Opening Coursera')
            webbrowser.open("https://www.coursera.org/in-progress")
        elif 'open zara' in query:
            webbrowser.open("https://www.zara.com/in/en/sale-l879.html?v1=984796")
        
        else:
            print("I was not trained, sorry sir ")
        
 
