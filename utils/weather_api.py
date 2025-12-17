# utils/weather_api.py
import requests
import config

def get_weather(city):
    # call OpenWeather geocoding first to get exact name and coords
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={config.OPENWEATHER_KEY}"
    g = requests.get(geo_url).json()
    if not g:
        return "City not found. Try full name (e.g. Hyderabad,IN) or pin code."
    lat, lon = g[0]['lat'], g[0]['lon']
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.OPENWEATHER_KEY}&units=metric"
    r = requests.get(url).json()
    if r.get("cod") != 200:
        return "Weather service error."
    return (
        f"🌤 Weather in {g[0]['name']} ({g[0].get('country','')}):\n"
        f"Temp: {r['main']['temp']}°C\n"
        f"Humidity: {r['main']['humidity']}%\n"
        f"Condition: {r['weather'][0]['description']}"
    )
