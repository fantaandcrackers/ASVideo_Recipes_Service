# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_recipes', '0006_video_created_ms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_ms',
            field=models.BigIntegerField(),
        ),
    ]
