from django.db import models
from django.contrib.auth.models import User
from tournaments.models import Tournament

class Request(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    gmail = models.EmailField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"