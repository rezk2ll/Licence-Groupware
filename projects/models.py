from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    name     = models.CharField(max_length=50)
    progress = models.DecimalField(decimal_places=2 , max_digits=3)
