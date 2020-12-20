import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command = command.lower()
            if 'pinky' in command:
                command =  command.replace('pinky', '')
    except:
        pass
    return command

def run_pinky():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Right now it is ' + time)
    elif 'who is' in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace("what is", '')
        info = wikipedia.summary(thing,2)
        print(info)
        talk(info)
    elif 'date' in command and 'go' in command:
        talk('die single you little shit')
    elif 'date' in command:
        today=datetime.date.today().strftime("%B %d, %Y")
        talk('today is ' + today)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

run_pinky()