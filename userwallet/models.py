from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=56,)
    phone = models.IntegerField(max_length=32)
    balance = models.IntegerField(max_length=265, default=0)
    postalcode = models.CharField(max_length=15)
    currency = models.CharField(max_length=255)
    
    
    
    def __str__(self):
        return self.firstname