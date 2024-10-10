import datetime
import wikipediaapi
import os
import requests
from assistant.speech import speak
from assistant.config import WEATHER_API_KEY

# Define the user agent for Wikipedia requests
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="VoiceAssistant/1.0 (tombribowei01@gmail.com)"
)

# Tell the time
def get_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {now}")

# Search Wikipedia
def search_wikipedia(query):
    result = wiki_wiki.page(query)
    if result.exists():
        speak(f"According to Wikipedia, {result.summary[:200]}")
    else:
        speak(f"Sorry, I couldn't find any information on {query}")

# Get Weather Info
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(base_url).json()
    
    if response["cod"] != "404":
        main = response["main"]
        temperature = main["temp"]
        speak(f"The temperature in {city} is {temperature} degrees Celsius.")
    else:
        speak(f"Sorry, I couldn't find weather information for {city}.")

# Open system apps
def open_app(app_name):
    if app_name == "notepad":
        os.system("notepad")
    elif app_name == "calculator":
        os.system("calc")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

# Greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
