from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import weather_model
from .serializers import Weather_Serializer
import urllib
import json
import requests
from datetime import date,timedelta

@api_view(['GET', ])
def weather_data_api(request):
    response=requests.get("http://api.openweathermap.org/data/2.5/weather?q=pune&appid=dad821d427bc3930968fb64174392a68")
    jsondata=response.json()

    prime=primenumberfunction()
    today = date.today()
    dayy = int(today.strftime("%d"))
    
    if dayy in prime:
       serializer = Weather_Serializer(data=jsondata)
       if serializer.is_valid():
          serializer.save()
          return Response(jsondata)   
    
    else:
        return Response("Date is not prime so no data") 

def primenumberfunction():
    primenumbers=[]

    for i in range(2,32):
        isPrime = True
        for num in range(2, i):
            if i % num == 0:
                isPrime = False
        
        if isPrime:
            primenumbers.append(i)
    return primenumbers