from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Filemodel(models.Model):
    owner       = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    size        = models.IntegerField()
    name        = models.CharField(max_length=255)
    date        = models.DateTimeField(auto_now_add=True)
