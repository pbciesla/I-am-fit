# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from fits.models import Workout, Goal

admin.site.register(Workout)
admin.site.register(Goal)