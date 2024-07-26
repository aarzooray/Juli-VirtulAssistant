# import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
# import smtplib
import yt_dlp
import pyaudio
import smtplib
import random
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Check if voices are available
for voice in voices:
    if 'en-in' in voice.languages:
        engine.setProperty('voice', voice.id)
        break

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am juli. Please tell me how may I help you, Bro")

def alarmClock():
     hr = int(datetime.datetime.now().hour)
     min = int(datetime.datetime.now().minute)
     if hr==4 and min==0:
         speak("Wake Up Aarzoo, Uth Jao, Subah Ho Gya!!")
     elif hr==8 and min==00:
         speak("Go for having Breakfast, Bhaiya!!")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjusts to ambient noise
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    return query

def sendEmail(subject, body, to_email):
    sender_email = "techyray35@gmail.com"
    password = "tyie dcru ifgc rrsc"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


def search_youtube(query):
    speak('Searching YouTube...')
    query = query.replace("juli", "").strip()  # Remove "youtube" from the query

    # Use yt_dlp to search for videos
    ydl_opts = {
        'quiet': False,
        'format': 'best',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
          
            # print(random_float)  # Example output: 0.37444887175646646
            # Search for the video
            info_dict = ydl.extract_info(f"ytsearch:{query}", download=False)
            video_info = info_dict['entries'][0]  # Get the first result
            title = video_info['title']
            url = video_info['url']
            results = f"Here is a video titled '{title}'. You can watch it at {url}."
            print(results)
            # speak(results)
            webbrowser.open(url)
        except Exception as e:
            speak("Sorry, I couldn't find any results on YouTube.")
            print(e)

if __name__ == "__main__":

    alarmClock()

    wishMe()
    while True:
        query = takeCommand().lower()



        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif query and 'juli' in query.lower():
            search_youtube(query)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open github' in query:
            webbrowser.open("https://github.com/aarzooray")



        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'gate khol' in query:
            speak("Chal,  chutiya")


        elif 'rajkumar' in query:
            speak("RajKumar, Bhosdi wala")

        elif 'lokesh' in query:
            speak("lokesh, Machikne")          

        elif 'prince' in query:
            speak("Chal beta aage Chal")          

        elif 'nitin' in query:
            speak("Gandu, Gand me Bamboo")          

        elif 'stop program' in query:
             os.system("taskkill /im juli.exe") 

      

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:

            # music_dir = 'C:\Users\dell\Music'
            random_float = random.randint(1,16)
            music_dir = 'C:/Users/Lokesh Bohara/Music'
            songs = os.listdir(music_dir)
            print(songs[random_float])
            os.startfile(os.path.join(music_dir, songs[random_float]))


        elif 'stop music' in query.lower():
             # Code to stop the music
            os.system("taskkill /im VLC.exe")  



        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Bhaiya, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C://Users//Lokesh Bohara//AppData//Local/Programs//Microsoft VS Code//Code.exe"
            speak(" Vs code is opening")
            os.startfile(codePath)

        elif 'open brave' in query:
            codePath = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"
            os.startfile(codePath)

        elif 'open ms edge' in query:
            codePath = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"
            os.startfile(codePath)

        elif 'email' in query:
           speak("What's the subject?")
           subject = takeCommand()
           
           speak("What to say?")
           body = takeCommand()
           

           speak("Tell me Receipent Email:")
           to_email = "shivshankarpandit212@gmail.com"
           sendEmail(subject, body, to_email)
           

        else:
            print("No query matched")





            