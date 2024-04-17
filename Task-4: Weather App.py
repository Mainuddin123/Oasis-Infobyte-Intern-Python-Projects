import requests

def fetch_weather(location):
    api_key = "dd285381fb0f0abfd9b1d07f0882f251"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("Error fetching weather data. Please check your input.")
            return None
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching weather data:", e)
        return None

def display_weather(weather_data):
    if weather_data:
        print("Current Weather:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Weather data not available.")

def main():
    print("Welcome to the Weather App!")
    location = input("Enter a city or ZIP code: ")
    
    weather_data = fetch_weather(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
