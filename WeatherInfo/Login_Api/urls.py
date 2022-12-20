from django.urls import path
from knox import views as knox_views

# from .views import RegisterAPI, LoginAPI, CityAPIView
from .views import RegisterAPI, LoginAPI
urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('', RegisterAPI.as_view(), name=''),
    # path('api/register/', RegisterAPI.as_view(), name='register'),
]