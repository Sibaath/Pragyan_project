from django.db import models

class User(models.Model):
    api_token = models.CharField(max_length=255,unique=True)
    
# Create your models here.
