# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0008_auto_20181008_0207'),
        ('publish', '0004_auto_20181008_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publish',
            name='pet',
        ),
        migrations.AddField(
            model_name='publish',
            name='pet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Publishs', to='pet.Pet'),
        ),
    ]
