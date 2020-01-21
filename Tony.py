import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Tony. How may I assist you today sir?")

# Here the command fails either because it cannot access the built-in microphone which in my case is extremely
# rare because python is built in such a way to accommodate for it. I made sure by printing out the list of
# microphones which gives me the a built-in microphone, and an output stream.
# If the microphone works then, the listener called on line 38 fails to stop leading to a constant loop.
# Only on the manual termination of the program does the loop stop.
# OKAY! FINALLY FIXED THE BUG!! THATS AN ACHIEVEMENT!
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        speech = r.recognize_google(audio)
        print(f'You Said: {speech}')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service")
    return speech


if __name__ == '__main__':
    wishme()
    while True:
        convo = takeCommand().lower()
        if 'wikipedia' in convo:
            speak('Searching Wikipedia...')
            convo = convo.replace('Wikipedia', '')
            results = wikipedia.summary(convo, sentences=2)
            print(results)
            speak("According to wikipedia, " + results)
        elif 'open youtube' in convo:
            speak('Opening Youtube')
            webbrowser.open('https://www.youtube.com')
        elif 'github' in convo:
            speak('opening github for you sir')
            webbrowser.open('https://github.com')