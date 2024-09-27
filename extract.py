import requests
import pandas as pd
from datetime import datetime

def extract_data(api_key, city):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame([{
            'city': data['name'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.now().isoformat()
        }])
    else:
        print(f"Error al obtener datos para {city}:", response.status_code)
        return pd.DataFrame()
