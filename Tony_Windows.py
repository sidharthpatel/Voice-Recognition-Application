import pyttsx3
import datetime
import speech_recognition
import tkinter
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 14)
windows = tkinter.Tk()
windows.configure(background = 'lightblue')

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

    speak('I am Tony, sir. How may I help you?')

def takeCommand():
    recognition = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        w = tkinter.Label(windows, text = 'Listening...', font = ('Courier', 16))
        w.pack()
        windows.update()
        recognition.pause_threshold = 1
        audio = recognition.listen(source)

        try:
            w = tkinter.Label(windows, text = 'Recognizing...', font = ('Courier', 16))
            w.pack()
            windows.update()
            query = recognition.recognize_google(audio, language = 'en-US')
            w = tkinter.Label(windows, text = f'User Said: {query}', font = ('Courier', 16))
            w.pack()
            windows.update()
        except Exception:
            w = tkinter.Label(windows, text = 'Say that again please...', font = ('Courier', 16))
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