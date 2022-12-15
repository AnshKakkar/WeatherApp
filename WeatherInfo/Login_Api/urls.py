from django.urls import path

# from .views import RegisterAPI, LoginAPI, CityAPIView
from .views import RegisterAPI, LoginAPI
urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]