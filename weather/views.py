import requests

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

        try:
            city_weather = {
                'city': city.name,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }
            error = ''
        except KeyError:
            city_weather = ''
            error = 'Please enter a valid city name'

    return render(request, 'weather/weather.html', context={'city_weather': city_weather, 'error': error, 'form': form})
