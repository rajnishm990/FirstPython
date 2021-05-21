import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[0].id)

def speak(audio):
    """ This fucntion would set up voices and speak the text passed """
    engine.say(audio)
    engine.runAndWait()
    

   
def Salutations():
 hour=int(datetime.datetime.now().hour)
 if hour>=0 and hour <12:
        speak("BAD MORNING, HUMAN")
 elif hour >=12 and hour <18:
        speak("BAD AFTERNOON, HUMAN")
 else :
        speak("HAIL NIGHT TIME , HUMAN")
 
 speak ("my name is LUCIFER , WHAT DO YOU WANT ME TO DO  ? ")

def takecommand():
    r=sr.Recognizer ()
    with sr.Microphone() as source:
        print("I AM LISTENING HUMAN, SPEAK.......")
        speak("I am listening , speak")
        r.pause_threshold =1
        audio =r.listen(source)

        try:
            print("RECOGNIZING ")
            query =r.recognize_google(audio, language='en-in')
            print(f"YOU SAID {query} \n")

        except Exception as e:
                print("CAN YOU REPEAT THAT...")
                return "none"
        return query

if __name__ =="__main__":
    Salutations()
    
    while True:
        query=takecommand().lower()

        if 'Wikipedia' in query:
            speak("Searching on Wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According To wikipedia")
            print(results)
            speak(results)
            #Can't open wikipedia , Will have to solve this .

        elif 'open youtube' in query:
            speak("Opening Youtube.....")
            webbrowser.open("youtube.com")
        
        elif 'open facebook' in query:
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")
        
        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow.....")
            webbrowser.open("stackoverflow.com")
            #Leaving it empty , can put any number web browser of operations here
        
        elif 'play music' in query:
            speak("Playing Music")
            music_dir= 'E:\\songs'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

    








    
