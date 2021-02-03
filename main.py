import pyaudio
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import subprocess
import os
import requests
from bs4 import BeautifulSoup


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
    #add more if following top example


    #added google search still needs a bit of cleaning but works good
def search():
    if " " in understand:
        headers = {'google my user-agent goes here'}
        url = requests.get(f'https://www.google.com/search?q={understand}', headers=headers)
        soup = BeautifulSoup(url.content, 'html.parser')
        name = soup.find("div", {'class': "ifM9O"})
        speak("searching web now for your answers")
        speak(name)


def time_date():
    time = datetime.datetime.now().strftime("%I %M %p")
    date = datetime.date.today().strftime("%A %d %m %y")
    if 'time' in understand:
        speak("the time today is {0}".format(time))
    if 'date' in understand:
        speak('the date today is {0}'.format(date))


def applications():
    if 'spotify' in understand:
        subprocess.call('Change to your C drive')
        #example
    if 'notepad' in understand:
        subprocess.call('C:\\Windows\\Notepad.exe')
    if 'pycharm' in understand:
        subprocess.call('Change to your C drive')


def entertain():
    if 'movies' in understand:
        movies = os.listdir('C:\\path\\to\\tv_shows\\folder')
        speak(movies)
        print(movies)
    if 'tv' in understand:
        tv = os.listdir('C:\\path\\to\\tv_shows\\folder')
        speak(tv)
        print(tv)


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
    if 'take me over to' in understand:
        internet_commands()
    if 'please tell me the' in understand:
        time_date()
    if 'can you open for me' in understand:
        applications()
    if 'tell me my playlist for' in understand:
        entertain()
    if 'search' in understand:
        search()
