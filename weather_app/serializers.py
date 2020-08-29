from rest_framework import serializers
from .models import weather_model

class Weather_Serializer(serializers.ModelSerializer):
    class Meta:
        model = weather_model
        fields = ['coord','weather','main','wind','clouds','sys','base','visibility','dt','timezone','name']
        