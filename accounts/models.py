from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True)    
    username = models.CharField(unique='True', null=True, max_length=100)

    def __str__(self):
        return self.username