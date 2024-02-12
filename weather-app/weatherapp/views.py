from django.shortcuts import render
import requests
from . models import City
from . forms import CityForm


def index(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6da8a860863f6aff086783e3a36b3c08'
    
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    
    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    
    context = {'weather_data' : weather_data}
    return render(request, 'weather/index.html', context)
