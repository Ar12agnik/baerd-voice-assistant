from bardapi import Bard
import pyttsx3
import speech_recognition as sr
from googlesearch import search
import webbrowser
import pywhatkit 
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
def generate_maps_link(f,t):
    f=f.replace(" ",'_')
    t=t.replace(" ","_")
    return f"https://www.google.co.in/maps/dir{f}/{t}"

running=True
speak("Hello I am your Assistant Jarvis. Press enter to start talking")
while running:
    input("press enter to start!")
    x=hear()
    if x is not None:
        x=x.lower()
    if x is None:
        pass
    elif  'open' in x:
        x=x.replace('open','')
        for url in search(x):
            f_url=url
            break
        webbrowser.open(f_url)  
    elif 'play' in x:
        speak("playing...")
        pywhatkit.playonyt(x.replace("play",""))
    elif 'send' in x:
        pywhatkit.sendwhatmsg_instantly(input("enter the phone number with country code: "),input("what is the message ?"))
        speak("Done! Message Sent!")
    elif ('find') and ('phone') in x:
        webbrowser.open_new_tab('https://www.google.com/android/find/')
        speak("Here's a website that can help you may need to login first.")
    elif 'directions' in x:
        speak("where from?")
        f=hear()
        speak("where to?")
        t=hear()
        webbrowser.open_new_tab(generate_maps_link(f,t))
    else:
        count=10
        for lines in get_responce(x).split("."):
            count-=1
            if count>=0:
                speak(lines)
            else:
                print(lines)

