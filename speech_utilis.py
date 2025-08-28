import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        return r.recognize_google(audio)

def text_to_speech(text, filename="response.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"afplay {filename}")  # macOS command to play sound
