from django.shortcuts import render

# Create your views here.
from .models import Preference
from .serializers import CitySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from django.shortcuts import render
from rest_framework.decorators import api_view

class CityAPIView(APIView):

    # def get(self, request):
    #     articles=Preference.objects.all()
    #     serializer=CitySerializer(articles, many=True)
    #     return Response(serializer.data)


    def post(self, request):
        serializer=CitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



def Citysave(request):
    if request.method=="POST":
        Cityname1=request.POST.get('Cityname1')
        data1={'city_name':Cityname1}
        Cityname2=request.POST.get('Cityname2')
        data2={'city_name':Cityname2}
        Cityname3=request.POST.get('Cityname3')
        data3={'city_name':Cityname3}
        headers={"Content-Type": "application/json"}
        apipath1=requests.post('http://127.0.0.1:8000/city_names/',json=data1, headers=headers)
        apipath2=requests.post('http://127.0.0.1:8000/city_names/',json=data2, headers=headers)
        apipath3=requests.post('http://127.0.0.1:8000/city_names/',json=data3, headers=headers)
        return render(request,"index.html")
    else:
        return render(request,"index.html")
