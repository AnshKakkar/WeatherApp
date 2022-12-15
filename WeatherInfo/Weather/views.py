from django.shortcuts import render
import requests
# Create your views here.

def cityweather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=83f420865bf8e11581a53634c001adb0'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #requesting the API data and returns the json object
    
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather' : weather}

    return render(request, 'weather.html',context) 
