import requests
from django.shortcuts import render

from .models import City


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=464a1d9339dc2282caf9b17e02224f3b'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    print(weather_data)
    return render(request, 'weather/weather.html', context={'weather_data': weather_data})
