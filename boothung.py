import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
hung = pyttsx3.init()
voice =hung.getProperty('voices')
hung.setProperty('voices',voice[1].id)

def speak(audio):
    print('Hung: ' +audio)
    hung.say(audio)
    hung.runAndWait()
speak("Hello hung")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <=12:
        speak("Good morning boss")
    elif hour >12 and hour <=18:
        speak("Good afternoon boss")
    else:
        speak("Good evening boss")
    speak("How can I help you ")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio =c.listen(source)
    try:
        query= c.recognize_google(audio,language='en')
        print("Hung dai ca said: " +query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input("Your oder is: "))
    return query
if __name__ =="__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What shold i search on Google boss")
            search = command().lower()
            url =f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")
        if "youtube" in query:
            speak("What shold i search on Youtube boss")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "open video" in query:
            meme=r"C:\Users\Pro 2004\Videos\cmt\Pewpew - Em có thấy tủi nhục không, em có thấy buồn không.mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit"  in query:
            speak("Hung iss quitting sir. Goodbye boss")
            quit()