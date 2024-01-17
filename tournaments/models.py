from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
    picture = models.ImageField(upload_to='media/', default='media/nurbek.jpeg')
    price_fund = models.DecimalField(max_digits=10, decimal_places=2)
    whoisowner = models.TextField()  
    price_for_participating = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    time_for_registration_left = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Tournament: {self.description}'