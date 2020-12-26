# Voice-Recognition-Application
Voice-Recognition-Application is a human speech recognition application. It recognises human speech and converts it into text.
This allows the user to then process the text into desired feature implementation.

### Features
- [x] Start the application by greeting the user depending on the time through the datetime library.
- [x] Detect speech and convert it into text for further processing commands by allowing the computer to read the reponse back to the user.
  - [x] Detect phrases such as `Search Wikipedia for Bill Gates` resulting in a wikipedia search.
  - [x] Allow the computer to read the response back to the user through speech.
- [x] Open websites in the web browser through voice commands like `Open Github` will detect the phrases and open github website.
- [x] To implement a smooth user experience, switch from Command Line interactions to a Graphical User Interface.

### App Walkthrough GIF

### Notes
Description of any challenges encountered while building the application.
- Processing of Voice Recognition in Mac and windows interface were two different challenges as Windows provides built-in voice drivers, their cortana, while Mac leans towards privacy neglecting the access to any voice drivers.
- Initially, I did not set up a threshold for the application to wait for the user input, so it would immediately listen and stop in split seconds.
- Moreover, the application would execute once and end afterwards, but we want to implement it in such way that it is constantly overhearing and detecting user's commands.
### Open-Source Libraries Used
[pyttsx3](https://pypi.org/project/pyttsx3/) - text-to-speech conversion library in Python.
[datetime](https://docs.python.org/3/library/datetime.html) - Class for manipulating dates and times.
[speech_recognition](https://pypi.org/project/SpeechRecognition/) - Library for performing speech recognition, with support for several engines and APIs, online and offline, in our case, Google Speech Recognition engine.
[tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI package.
[wikipedia](https://pypi.org/project/wikipedia/) - Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
[webbrowser](https://docs.python.org/3/library/webbrowser.html) - A python module that provides a high-level interface to allow displaying web-based documents to the users.