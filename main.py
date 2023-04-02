import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sreeganesh Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sreeganesh Sir!")

    else:
        speak("Good Evening Sreeganesh Sir!")

    speak("I am Rocky Balboa, your personal assistant. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif 'are you in a relationship' in query:
            speak('I am in a relationship with wifi')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'comedy' in query:
            speak(pyjokes.get_joke())

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\GNAX\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open brave' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sreeganesh112@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'exit' in query:
            exit()