import requests
import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=464a1d9339dc2282caf9b17e02224f3b'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        response = requests.get(url.format(city)).json()
        print(response)

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        # print(city_weather)
        # city_weather = json.dumps(city_weather)
        # print(city_weather)
        # weather_data.append(city_weather)

    # print(weather_data)
    return render(request, 'weather/weather.html', context={'city_weather': city_weather, 'form': form})
    # return HttpResponse(city_weather, content_type='text/json')
