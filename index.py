
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
   wishMe()
speak("I am david sir. Please tell me how may help you")

while True:
    if 1:
     query = takecommand().lower()

    if 'wikipedia' in query:
           speak('Searching wikipedia.....')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

    elif  'open youtube' in query:
           webbrowser.open("youtube.com")  

    elif  'open google' in query:
           webbrowser.open("google.com")  

    elif  'open facebook' in query:
          webbrowser.open("facebook.com") 

    elif  'open instagram' in query:
          webbrowser.open("instagram.com") 

    elif  'open twitter' in query:
          webbrowser.open("twitter.com")
                      


    elif  'play music' in query: 
         music_dir = 'D:\\song'  
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(F"sir, the time is {strTime}")
    
    elif 'open code' in query:
      codepath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(codepath)

    