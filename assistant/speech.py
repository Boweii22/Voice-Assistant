# assistant/speech.py
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"You said: {command}")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "None"
    return command
