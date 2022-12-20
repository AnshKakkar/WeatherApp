from django.urls import path, include
from Weather import views

urlpatterns = [
    path('',include('Login_Api.urls')),
    path('weather/',views.cityweather),
    path('delete_all/<str:username>/', views.deleteAll, name='delete_all')
]