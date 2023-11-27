from django.contrib import admin
from goElectricApp.models import Car
from goElectricApp.models import UserCredentials

# Register your models here.
admin.site.register(Car)
admin.site.register(UserCredentials)