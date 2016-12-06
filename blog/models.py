from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author  = models.ForeignKey(User)
    title   = models.CharField(max_length=100)
    body    = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    comments= models.IntegerField(blank=True , default=0)


class Comment(models.Model):
    post     = models.ForeignKey(Post)
    poster   = models.ForeignKey(User)
    date     = models.DateTimeField(auto_now_add=True)
    bodytext = models.TextField()
