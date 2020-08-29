from django.db import models


class weather_model(models.Model):
    coord = models.JSONField()
    weather=models.JSONField()
    main=models.JSONField()
    wind=models.JSONField()
    clouds=models.JSONField()
    sys=models.JSONField()
    base=models.CharField(max_length=20)
    visibility=models.IntegerField() 
    dt=models.IntegerField() 
    timezone=models.IntegerField() 
    name= models.CharField(max_length=20)
    def __str__(self):
        return self.name