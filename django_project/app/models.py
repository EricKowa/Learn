from django.db import models
from django.utils import timezone

import datetime



# Create your models here.

class FirstDatabase(models.Model):
    name = models.CharField(max_length=100)
    entry_created = models.DateTimeField("Date entry created")

    entry_type= models.CharField(max_length=100, default="Supertype")
    def __str__(self):
        return self.name
    
    def created_recently(self):
        return self.entry_created >= timezone.now() - datetime.timedelta(days=2)
    

class SecondDatabase(models.Model):
    filling = models.CharField(max_length=100)
    first = models.ForeignKey(FirstDatabase, on_delete=models.CASCADE, blank=True)
    super_number = models.IntegerField(default=0)

    def __str__(self):
        return self.filling