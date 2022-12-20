from django.shortcuts import render,redirect

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
# from .serializers import UCitySerializer
from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from django.http import HttpResponseRedirect
from django.urls import reverse


# from .models import Preference
# from .serializers import CitySerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status

# class CityAPIView(APIView):

#     def get(self, request):
#         articles=Preference.objects.all()
#         serializer=CitySerializer(articles, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         serializer=CitySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        res=({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # Token.objects.create returns a tuple (instance, token). So in order to get token use the index 1
        "token": AuthToken.objects.create(user)[1]
        })
        return redirect('/api/login/')
        # return Response({
        # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # # Token.objects.create returns a tuple (instance, token). So in order to get token use the index 1
        # "token": AuthToken.objects.create(user)[1]
        # })


class LoginAPI(KnoxLoginView):
    # The AllowAny permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        # Token authentication
        serializer = AuthTokenSerializer(data=request.data)
        # we use raise_exception mostly unless we wnt to handle the serializers errors themselves
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # super denotes parent class(KnoxLoginView) of the current class
        # return super(LoginAPI, self).post(request)
        return HttpResponseRedirect('/city_preference/')




