# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.DecimalField(decimal_places=2, default=-1, max_digits=3),
            preserve_default=False,
        ),
    ]
