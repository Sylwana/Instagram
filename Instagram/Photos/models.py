from django.db import models

from Igers.models import User


class Photo(models.Model):
    path = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    users = models.ForeignKey(User)
 #  images = models.ImageField(upload_to = 'pic_folder/', blank=True)