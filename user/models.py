from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255,unique=True)
    bio = models.TextField(blank=True,null=True)
    