    # url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6da8a860863f6aff086783e3a36b3c08"
from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6da8a860863f6aff086783e3a36b3c08'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    return render(request, 'weather/index.html')
