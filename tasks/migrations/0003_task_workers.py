# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='workers',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]