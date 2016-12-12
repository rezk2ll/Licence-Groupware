from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user   = models.OneToOneField(User)
    link   = models.CharField(max_length=255 , default="user.png")
