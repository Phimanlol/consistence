# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0005_auto_20181008_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]