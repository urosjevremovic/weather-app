import requests
import json

from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=464a1d9339dc2282caf9b17e02224f3b'

    if request.method == 'POST':
        pass

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        # print(city_weather)
        # city_weather = json.dumps(city_weather)
        # print(city_weather)
        weather_data.append(city_weather)

    # print(weather_data)
    return render(request, 'weather/weather.html', context={'weather_data': weather_data, 'form':form})
