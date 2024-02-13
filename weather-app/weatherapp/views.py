from django.shortcuts import render
import requests
import json
from . models import City
from . forms import CityForm
from . import config

# Create your views here.
def index(request):
    cities = City.objects.all()
    url = config.weather_api
    
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        
    
    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
    
        weather = {
            'city':city,
            'temperature':city_weather['main']['temp'],
            'temp_min':city_weather['main']['temp_min'],
            'temp_max':city_weather['main']['temp_max'],
            'wind':city_weather['wind']['speed'],
            'country':city_weather['sys']['country'],
            'sunrise':city_weather['sys']['sunrise'],
            'sunset':city_weather['sys']['sunset'],
            'description':city_weather['weather'][0]['description'],
            'icon':city_weather['weather'][0]['icon'],
            'pressure':city_weather['main']['pressure'],
            'humidity':city_weather['main']['humidity']
        }
        
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form' : form}
    return render(request, 'weatherapp/index.html',context) #returns index.html template
