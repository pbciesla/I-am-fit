# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fits', '0004_auto_20180323_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date_workout',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='text',
            field=models.CharField(choices=[('fit', 'Fitness'), ('car', 'Cardio'), ('str', 'Strength training')], max_length=3),
        ),
    ]
