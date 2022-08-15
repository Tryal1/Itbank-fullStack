from django.db import models

# Create your models here.

class UserItbank(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    pin = models.IntegerField(max_length=6)
