import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import requests

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("User said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")
        return ""

# Function to execute commands
def execute_command(query):
    if "hello" in query:
        speak("Hello! How can I help you?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in query:
        speak("What would you like me to search for?")
        search_query = recognize_speech()
        try:
            search_result = wikipedia.summary(search_query, sentences=2)
            speak("According to Wikipedia, " + search_result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple options. Can you be more specific?")
            print(e)
        except wikipedia.exceptions.PageError as e:
            speak("Sorry, I couldn't find any information on that topic.")
            print(e)
    elif "weather" in query:
        # Replace "YOUR_OPENWEATHERMAP_API_KEY" with your actual OpenWeatherMap API key
        api_key = "dd285381fb0f0abfd9b1d07f0882f251"
        city = "Chennai"  # Replace with your city name
        country_code = "IN"  # Replace with your country code

        # Construct the API URL
        endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"

        # Make a request to the OpenWeatherMap API
        response = requests.get(endpoint)
        data = response.json()

        # Process the response and speak the weather information
        if "weather" in data:
            weather_info = data["weather"][0]["description"]
            speak(f"The weather in {city} is {weather_info}")
        else:
            speak("Sorry, I couldn't fetch the weather information.")

    else:
        speak("Sorry, I don't understand that command.")

# Main function
def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")
    while True:
        query = recognize_speech()
        execute_command(query)

if __name__ == "__main__":
    main()
