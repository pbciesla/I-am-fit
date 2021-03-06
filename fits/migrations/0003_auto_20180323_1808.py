# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 18:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fits', '0002_auto_20180321_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workout',
            name='date_workout',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='text',
            field=models.CharField(choices=[('fit', 'fitness'), ('car', 'cardio'), ('str', 'strenght training')], max_length=3),
        ),
    ]
