import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
speaker= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()
    speaker.runAndWait()
def take_command():

    try:
        with sr.Microphone() as source:
            print('listening.........')

            voice= listener.listen(source)
            command= listener.recognize_google(voice)

            command=command.lower()
            if  'alexa' in command:
                  command=command.replace('alexa' , '')
                  print(command)
                  talk(command)

    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play ' in command:
        song= command.replace('play' , '')
        talk('playing' + song )
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'  +time)
    elif 'where' in command:
        serching= command.replace('where'   ,'')
        info = wikipedia.summary(serching , 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('no, i am in a relationship with wifi ')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('please say the command again')
while True:
    run_alexa()


