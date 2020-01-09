import pyttsx3
from gtts import gTTS
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[36].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Tony. How may I assist you today sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en')
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "none"
    return query


if __name__ == '__main__':
    wishme()
    takeCommand()