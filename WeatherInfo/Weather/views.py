from django.shortcuts import render
import requests
from Preferences.models import Preference
from .forms import CityForm


# Create your views here.

def cityweather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=83f420865bf8e11581a53634c001adb0'

    cities = Preference.objects.all()

    if request.method == 'POST': 
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form=CityForm()
    
    weather_data=[]

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #requesting the API data and returns the json object

        weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather.html',context) 
