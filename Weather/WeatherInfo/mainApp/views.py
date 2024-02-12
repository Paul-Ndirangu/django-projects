from django.shortcuts import render
import requests
from .models import City 
from .forms import CityForm

def index(request):
    cities = City.objects.all()
    
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6da8a860863f6aff086783e3a36b3c08"


    if requests.method == "POST":
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'humidity': city_weather['weather']['humidity'],
            'pressure': city_weather['weather']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }

        weather_data.append(weather)
        context = {'weather_data': weather_data, 'form': form}

    return render(request, 'index.html', context)
