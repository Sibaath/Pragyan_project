from django.db import models

class User(models.Model):
    api_token = models.CharField(max_length=50, unique=True)
