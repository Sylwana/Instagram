from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #login = models.CharField(max_length=64, unique=True)
    #email = models.CharField(max_length=60, unique=True)
    #is_superuser = models.BooleanField()
    #password = models.CharField(max_length=60)
    pass

