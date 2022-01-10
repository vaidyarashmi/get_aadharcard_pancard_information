from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class aadhar_card(models.Model):
    number=models.IntegerField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    mobile_number=models.IntegerField()

class pan_card(models.Model):
    number=models.CharField(max_length=15)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    mobile_number=models.IntegerField()
