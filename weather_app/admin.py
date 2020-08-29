from django.contrib import admin

# Register your models here.
from .models import weather_model

admin.site.register(weather_model)