from bardapi import Bard
import pyttsx3
import speech_recognition as sr
from googlesearch import search
import webbrowser
def get_responce(prompt):   

    token = 'WgiS6pA9JILal8aWQ4P2ObGEr_sky4LhqhbNmnHJfhG0Cynbk0YOfVj7p_gWRiWbUtBUBw.'
    bard = Bard(token=token)
    return bard.get_answer(f"{prompt}")['content']
def speak(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def hear():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("I didn't understand what you said.")

running=True
speak("Hello I am your Assistant Jarvis. Press enter to start talking")
while running:
    input("press enter to start!")
    x=hear()
    if x is None:
        pass
    elif  'open' in x:
        x=x.replace('open','')
        for url in search(x):
            f_url=url
            break
        webbrowser.open(f_url)        
    else:
        count=10
        for lines in get_responce(x).split("."):
            count-=1
            if count>=0:
                speak(lines)
            else:
                print(lines)

