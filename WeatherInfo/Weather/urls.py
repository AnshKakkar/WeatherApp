from django.urls import path
from Weather import views

urlpatterns = [
    path('weather/',views.cityweather)
]