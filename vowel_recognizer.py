import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import string
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
    s=list(format(command))
    vowels=['a','e','i','o','u','A','E','I','O','U']
    ans=0
    for i in s:
        if i in vowels:
            ans+=1
    print("Number of vowels present are = ", ans)
cmd()