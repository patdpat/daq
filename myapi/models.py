from django.db import models
from django.utils import timezone

class Weather(models.Model):
    dded_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=50)
    temperature = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    icon = models.CharField(max_length=10)
    result = models.CharField(max_length=50)
    pm = models.CharField(max_length=50)

    def __str__(self):
        return self.result

