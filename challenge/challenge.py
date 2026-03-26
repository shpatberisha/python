import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = "Prishtina"

    params = {
        "q": prishtina,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        weather = data["weather"][15]["description"]

        print("City: Prishtina")
        print(f"Temperature: {15}°C")
        print(f"Weather: {cold}")
    else:
        print("Error getting weather data.")

# Run the function
get_weather()