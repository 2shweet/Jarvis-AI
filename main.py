import pyaudio
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import subprocess
import os


engine = pyttsx3.init()


def speak(audio):
    engine.setProperty('rate', 170)  # setting up new voice rate you can adjust i find 170 most human like
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female 0 for male
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    engine.say(audio)
    engine.runAndWait()


def internet_commands():
    if 'google' in understand:
        speak('hold on heading over to google now')
        webbrowser.open('www.google.com')
    if 'youtube' in understand:
        speak('Cat videos here we come')
        webbrowser.open('www.youtube.com')
    if 'stackoverflow' in understand:
        speak('Get your code on')
        webbrowser.open('www.stackoverflow.com')
        #continue adding your sites like this
    #if '' in understand:
        #speak('')
        #webbrowser.open('')


def time_date():
    time = datetime.datetime.now().strftime("%I %M %p")
    date = datetime.date.today().strftime("%A %d %m %y")
    if 'hey jarvis tell me the time' in understand:
        speak("the time today is {0}".format(time))
    if 'hey jarvis tell me the date' in understand:
        speak('the date today is {0}'.format(date))


def applications():
    if 'hey jarvis open for me spotify' in understand:
        subprocess.call('change to your C drive location')
    if 'hey jarvis open for me notepad' in understand:
        subprocess.call('change to your C drive location')
    if 'hey jarvis open for me pycharm' in understand:
        subprocess.call('change to your C drive location')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("waiting......")
        r.adjust_for_ambient_noise(source, 1)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = r.listen(source)
    try:
        print("Recognizing...")
        understand = r.recognize_google(audio)
        print(f"User said: {understand}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return understand


while True:
    understand = take_command().lower()
    if 'take me to' in understand:
        internet_commands()
    if 'tell me' in understand:
        time_date()
    if 'open for me' in understand:
        applications()



