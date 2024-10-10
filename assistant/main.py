from assistant.speech import take_command, speak
from assistant.functions import get_time, search_wikipedia, get_weather, open_app, greet

def main():
    greet()
    while True:
        command = take_command()

        if 'time' in command:
            print("Calling 'get_time' function...")
            get_time()

        elif 'wikipedia' in command or 'meaning' in command:
            speak('What should I search on Wikipedia?')
            query = take_command()
            if query != "None":
                print(f"Calling 'search_wikipedia' with query: {query}")
                search_wikipedia(query)

        elif 'weather' in command:
            speak('Which city?')
            city = take_command()
            if city != "None":
                print(f"Calling 'get_weather' for city: {city}")
                get_weather(city)

        elif 'open' in command:
            app_name = command.replace('open', '').strip()
            print(f"Calling 'open_app' for app: {app_name}")
            open_app(app_name)

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't catch that.")
            print(f"Unrecognized command: {command}")
