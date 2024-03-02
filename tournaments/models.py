from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime

class Tournament(models.Model):
    SPORT = 'sport'
    CYBERSPORT = 'cybersport'

    SINGLE = 'single'
    TEAM = 'team'

    FORMAT_CHOICES = [
        (SINGLE, 'Single'),
        (TEAM, 'Team'),
    ]

    TYPE_CHOICES = [
        (SPORT, 'Sport'),
        (CYBERSPORT, 'Cybersport'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Tournament')
    picture = models.ImageField(upload_to='', default='media/default.jpeg')
    sports = models.CharField(max_length=255, default='sports')
    cyberSports = models.CharField(max_length=255, default='cybersports')
    price_fund = models.DecimalField(max_digits=10, decimal_places=2)
    whoisowner = models.ForeignKey(User, on_delete=models.CASCADE)  
    teamsallowed = models.IntegerField(default=0)
    price_for_participating = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    players = models.IntegerField(default=0)
    date = models.DateField(default=datetime.today)
    alreadyin = models.IntegerField(default=0)
    formatt = models.CharField(max_length=10, choices=FORMAT_CHOICES, default=SINGLE)
    typee = models.CharField(max_length=11, choices=TYPE_CHOICES, default=SPORT)

    def __str__(self):
        return f'Tournament: {self.name}'
