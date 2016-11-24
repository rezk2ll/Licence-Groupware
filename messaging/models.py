from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mail(models.Model):
    sender = models.CharField(max_length=50)
    reciver= models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    message= models.TextField()
