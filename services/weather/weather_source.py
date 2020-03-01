import os
import requests

weatherstack_access_key = os.getenv('WEATHERSTACK_ACCESS_KEY')
#weatherstack_access_key = 'asdf'
weatherstack_base_url = 'http://api.weatherstack.com/current'
openweather_app_id = os.getenv('OPENWEATHER_APP_ID')
#openweather_app_id = 'asdf'
openweather_base_url = 'http://api.openweathermap.org/data/2.5/weather'
 
def source_data(city):
    ws = source_weatherstack(city)
    if ws['success'] == True:
        return { 'wind_speed': ws['data']['current']['wind_speed'], 'temperature_degrees':
              ws['data']['current']['temperature'] }
    else:
        ow = source_openweather(city)
        if ow['success'] == True:
            return { 'wind_speed': ow['data']['wind']['speed'],
                    'temperature_degrees': ow['data']['main']['temp'] }
    # TODO memoisation
    return { 'wind_speed': 0, 'temperature_degrees': 0 }

def source_weatherstack(city):
    params = { 'access_key': weatherstack_access_key, 'query': city }
    r = requests.get(weatherstack_base_url, params=params)
    response = r.json()
    success = not key_exists('error', response)
    return { 'success': success, 'data': response }

def source_openweather(city):
    params = { 'q': 'melbourne,AU', 'appid': openweather_app_id, 'units':
              'metric' }
    r = requests.get(openweather_base_url, params=params)
    response = r.json()
    success = True if response['cod'] == 200 else False
    return { 'success': success, 'data': response }

def key_exists(key, dict):
    if key in dict:
        return True
    return False
