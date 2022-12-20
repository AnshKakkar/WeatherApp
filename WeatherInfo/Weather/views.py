from django.shortcuts import render,redirect
import requests
from Preferences.models import Preference
from .forms import CityForm
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from Preferences.serializers import CitySerializer

# Create your views here.
@csrf_exempt
def cityweather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=83f420865bf8e11581a53634c001adb0'

    cities = Preference.objects.all()

    if request.method == 'POST': 
        form = CityForm(request.POST) # add actual request data to form for processing
        # form.is_valid()
        if form.is_valid():
            city_new=form.cleaned_data['city_name']
            serializer_data = {"city_name": city_new, "account": request.user.id}
            serializer=CitySerializer(data=serializer_data)

            if serializer.is_valid():
                serializer.save()

            # form.save()
        # form.save() # will validate and save if validate

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

@api_view(['DELETE'])
def deleteAll(request, username):
        delcity = Preference.objects.filter(account__username=username)
        delcity.delete()
        return render(request, "thankyou.html") 

# class ArticleDetails(APIView):

#     def delete(self, request, id):
#         article= self.get_object(id)
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
