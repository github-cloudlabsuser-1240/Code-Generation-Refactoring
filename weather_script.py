import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "c9dc503067be26864b7a76c61caacb69"
    city = "Saint Louis, Missouri"
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(weather_data)
    else:
        print("Failed to get weather data")