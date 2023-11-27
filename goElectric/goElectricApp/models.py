from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    images = models.ImageField(upload_to='static/images/')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    hp = models.IntegerField()
    km = models.IntegerField()
    cc = models.IntegerField()
    
class UserCredentials(models.Model):
    profile_picture = models.ImageField(upload_to='static/images/', blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    credentail = models.CharField(blank=False, null=False, max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class UserLogin(models.Model):
    email = models.EmailField(unique=True)
    credentail = models.CharField(blank=False, null=False, max_length=200)