from django.urls import path
from Preferences import views
from .views import CityAPIView

urlpatterns = [
    path('city_preference/',views.Citysave),
    path('city_names/', CityAPIView.as_view(), name='city_names'),
]