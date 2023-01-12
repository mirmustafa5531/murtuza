from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    

class showing(models.Model):
    filmtitle = models.CharField(max_length=100)
    agerating = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

