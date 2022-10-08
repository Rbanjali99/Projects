import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()
def cmd():
    with sr.Microphone() as source:
        print("clearing background noises..Please Wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("Ask me anything")
        recordedaudio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(recordedaudio)
        print("Your Message",format(command))
    except Exception as ex:
        print(ex)
    if 'chrome' in command:
        a="Opening chrome"
        engine.say(a)
        engine.runAndWait()
        program="C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(program)
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in command:
        b='Opening Youtube'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(command)
    if 'youtube' in command:
        b='Opening youtube'
        engine.say(b)
        engine.runAndWait()
        program='http://youtube.com'
        subprocess.Popen(program)
while True:
    cmd()
