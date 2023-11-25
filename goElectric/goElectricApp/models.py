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

    def __str__(self):
        return self.car_name