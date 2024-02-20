from django.db import models
import uuid
from django.contrib.auth.models import User

class News(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to='media/', default='media/default.jpeg')
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'News: id - {self.id}'