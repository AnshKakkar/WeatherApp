
# Create your views here.
from .models import Preference
from .serializers import CitySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

class CityAPIView(APIView):

    # def get(self, request):
    #     articles=Preference.objects.all()
    #     serializer=CitySerializer(articles, many=True)
    #     return Response(serializer.data)


    def post(self, request):

        city_names = request.data.get("city_names")
        print(request.POST)

        for city in city_names:
            serializer_data = {"city_name": city, "account": request.user.id}
            serializer=CitySerializer(data=serializer_data)

            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def Citysave(request):
    if request.method=="POST":
        print(request.user.username)
        # Gets the value of the name parameter in a POST request
        print(request.POST)
        Cityname1=request.POST.get('Cityname1')
        data1={'city_name':Cityname1}
        # data1={'city_name':Cityname1, "account_id": request.user.id}
        Cityname2=request.POST.get('Cityname2')
        data2={'city_name':Cityname2}
        Cityname3=request.POST.get('Cityname3')
        data3={'city_name':Cityname3}
        headers={"Content-Type": "application/json"}
        city_names=[]
        city_names.append(Cityname1)
        city_names.append(Cityname2)
        city_names.append(Cityname3)
        for city in city_names:
            serializer_data = {"city_name": city, "account": request.user.id}
            serializer=CitySerializer(data=serializer_data)

            if serializer.is_valid():
                serializer.save()
                
        apipath1=requests.post('http://127.0.0.1:8000/city_names/',json=data1, headers=headers)
        apipath2=requests.post('http://127.0.0.1:8000/city_names/',json=data2, headers=headers)
        apipath3=requests.post('http://127.0.0.1:8000/city_names/',json=data3, headers=headers)
        return redirect("/weather/")
        # http response to send data back
    else:
        return render(request,"preference.html")
