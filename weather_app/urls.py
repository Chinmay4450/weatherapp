from django.urls import path
from .views import weather_data_api

app_name = 'weather_app'

urlpatterns = [
	path('', weather_data_api)
]