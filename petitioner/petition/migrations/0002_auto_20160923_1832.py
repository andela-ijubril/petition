# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='time_signed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
