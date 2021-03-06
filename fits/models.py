# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    goal_type = (
        ('ls', 'loose weight'),
        ('ms', 'build a mass'),
        ('ft', 'fit lifestyle'),
        ('ot', 'other')
    )
    # goal = models.CharField(max_length='2', choices=goal_type)
    goal = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.goal

    def __str__(self):
        return self.goal


class Workout(models.Model):
    workout_type = (
        ('fit', 'Fitness'),
        ('car', 'Cardio'),
        ('str', 'Strength training')
    )
    text = models.CharField(max_length=3, choices=workout_type)
    date_added = models.DateTimeField(auto_now_add=True)
    date_workout = models.DateTimeField()
    duration = models.IntegerField()
    owner = models.ForeignKey(User)

    def workout_type(self):
        return self.get_workout_type_display()

    def __unicode__(self):
        return unicode(self.date_workout.strftime('%d-%m-%Y'))


class Weight(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    value = models.FloatField()

    def __str__(self):
        return str(self.value)
