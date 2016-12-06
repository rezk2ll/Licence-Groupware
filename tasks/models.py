from __future__ import unicode_literals

from django.db import models

# Create your models here.
class task(models.Model):
    project = models.DecimalField( max_digits=3 , decimal_places=2)
    subject = models.CharField(max_length=30)
    priority= models.CharField(max_length=10)
    content = models.TextField()
    progress= models.DecimalField( max_digits=5, decimal_places=2)
    workers = models.CharField(max_length=100)
