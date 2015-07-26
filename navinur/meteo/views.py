import requests

# Create your views here.

def fetch_weather_data():

    r = requests.get('http://api.worldweatheronline.com/free/v2/marine.ashx?key=8617cae64d58edff70c6940a764fc'
                     '&format=json&q=28,-89')
    print(r.text)

fetch_weather_data()