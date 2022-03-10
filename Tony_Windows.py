'''
pyttsx3 : Text-to-speech conversion library in Python. (pro) It works offline unlike other libraries.
'''
import pyttsx3
'''
datetime : Class for manipulating dates and times.
'''
import datetime
'''
speech_recognition : Library for recognizing speeches with support for several engines and APIs, both, online and offline.
'''
import speech_recognition
'''
Tkinter : Built-in python interface to the Tcl/Tk GUI toolkit.
'''
import tkinter
'''
Wikipedia : Python library that makes it easy to access and parse data from Wikipedia.
'''
import wikipedia
'''
Webbrowser : Python module provides a high-level interface to allow displaying web-based documents to users.
'''
import webbrowser

# Setup
engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices') # getting list of voices
engine.setProperty('voice', voices[0].id) # setting preferred voice
rate = engine.getProperty('rate') # getting details of current speaking rate
engine.setProperty('rate', rate - 14) # setting up new voice rate
windows = tkinter.Tk() # Generates a new window
windows.configure(background = 'lightblue') # Configure the window background to lightblue

# Audio function that will say the string in the parameter and wait for user response.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('My name is Tony, sir. How may I help you?')

def takeCommand():
    recognition = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        w = tkinter.Label(windows, text = 'Listening...', font = ('Courier', 16))
        w.config(bg='lightblue')
        w.pack()
        windows.update()
        recognition.pause_threshold = 1
        audio = recognition.listen(source)

        try:
            w = tkinter.Label(windows, text = 'Recognizing...', font = ('Courier', 16))
            w.config(bg='lightblue')
            w.pack()
            windows.update()
            query = recognition.recognize_google(audio, language = 'en-US')
            w = tkinter.Label(windows, text = f'User Said: {query}', font = ('Courier', 16))
            w.config(bg='lightblue')
            w.pack()
            windows.update()
        except Exception:
            w = tkinter.Label(windows, text = 'Say that again please...', font = ('Courier', 16), background='lightblue')
            w.pack()
            windows.update()
            return 'None'

        return query


if __name__ == "__main__":
    wishMe()
    while True:
        convo = takeCommand().lower()

        if 'wikipedia' in convo:
            speak('Searching Wikipedia...')
            convo = convo.replace('Wikipedia', '')
            results = wikipedia.summary(convo, sentences=2)
            print(results)
            w = tkinter.Label(windows, )
            speak("According to wikipedia, " + results)
        elif 'open youtube' in convo:
            speak('Opening Youtube')
            webbrowser.open('https://www.youtube.com')
        elif 'github' in convo:
            speak('opening github for you sir')
            webbrowser.open('https://github.com')