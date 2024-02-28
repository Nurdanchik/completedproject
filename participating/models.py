from django.db import models
from django.contrib.auth.models import User
from tournaments.models import Tournament

class Coupon(models.Model):
    cupon = models.CharField(max_length=10)
    valid = models.BooleanField(default=True)
    validuntil = models.DateField()

    def __str__(self):
        return f"Coupon {self.cupon}"

class Request(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    gmail = models.EmailField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    cupon = models.CharField(max_length=10, default='uUka7Q')

    def __str__(self):
        return f"{self.name} {self.surname}"