import speech_recognition as sr
import pyttsx3
from beeply import notes

mybeep = notes.beeps()

recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id) # Use female voice

def speechrecognition():
    speechrecognition_microphone()
    speechrecognition_checker()
 
def speechrecognition_microphone():
    while True:
        try:
            mybeep.hear('C',250)
            with sr.Microphone() as source:
                print("Say Something")
                global audio
                audio = recognizer.listen(source)
                print("Input successful")
                return audio
 
        except LookupError:
            engine.say("Could not understand please try again")
            engine.runAndWait()
            speechrecognition()
          
def speechrecognition_checker():
    global speech
    speech = recognizer.recognize_google(audio).lower()
    engine.say(f"You said: {speech}. Is this correct? Yes or No")
    engine.runAndWait()
    
    while True:
        
        speechrecognition_microphone()
        yes_or_no = recognizer.recognize_google(audio).lower()
        
        if yes_or_no == 'yes':
            with open("audio.txt", "a") as file:
                file.write(speech + '\n')
            return speech
        
        elif yes_or_no == "no":
            engine.say("Okay, Try again.")
            engine.runAndWait()
            speechrecognition()
            
        else:
            engine.say("Couldn't understand. Please try again.")  
            engine.runAndWait()