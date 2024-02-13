from django.shortcuts import render
import requests
import json
from . models import City
from . forms import CityForm
from config import weather_api

# Create your views here.
def index(request):
    cities = City.objects.all()
    url = weather_api
    
    
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
            'description':city_weather['weather'][0]['description'],
            'icon':city_weather['weather'][0]['icon'],
            'pressure':city_weather['main']['pressure'],
            'humidity':city_weather['main']['humidity']
        }
        
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form' : form}
    return render(request, 'weatherapp/index.html',context) #returns index.html template
