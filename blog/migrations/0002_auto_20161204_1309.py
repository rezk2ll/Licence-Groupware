# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='bodytext',
            field=models.TextField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]