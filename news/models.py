from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    picture = models.ImageField(upload_to='media/')
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)