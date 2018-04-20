# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Workout, Goal, Weight
from .forms import WorkoutForm, GoalForm, WeightForm


def index(request):
    """Main page"""
    context = {'goal': Goal.objects.get(pk=1)}
    return render(request, 'fits/index.html', context)


@login_required
def my_workouts(request):
    my_workouts = Workout.objects.filter(owner=request.user).order_by('-date_workout')
    context = {'my_workouts': my_workouts}
    return render(request, 'fits/my_workouts.html', context)


@login_required
def workout(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    context = {'workout': workout}
    return render(request, 'fits/workout.html', context)


@login_required
def add_workout(request):
    if request.method != "POST":
        form = WorkoutForm()
    else:
        form = WorkoutForm(request.POST)
        if form.is_valid():
            new_workout = form.save(commit=False)
            new_workout.owner = request.user
            new_workout.save()
            return HttpResponseRedirect(reverse('fits:my_workouts'))
    context = {'form': form}
    return render(request, 'fits/add_workout.html', context)


@login_required
def edit_workout(request, workout_id):
    edited_workout = Workout.objects.get(id=workout_id)

    if request.method != 'POST':
        form = WorkoutForm(instance=edited_workout)
    else:
        form = WorkoutForm(instance=edited_workout, data=request.POST)
        if form.is_valid():
            edited_workout = form.save(commit=False)
            edited_workout.owner = request.user
            edited_workout.save()
            return HttpResponseRedirect(reverse('fits:my_workouts'))
    context = {'workout': edited_workout, 'workout_id': workout_id, 'form': form}
    return render(request, 'fits/edit_workout.html', context)


# TODO create a goal
@login_required
def goal(request):
    goals = Goal.objects.filter(owner=request.user).order_by('date_added')
    context = {'goal': goals[0]}
    return render(request, 'fits/goal.html', context)


def edit_goal(request):
    goal = Goal.objects.filter(owner=request.user).order_by('date_added')[0]
    if request.method != 'POST':
        form = GoalForm(instance=goal)
    else:
        form = GoalForm(instance=goal, data=request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.owner = request.user
            goal.save()
            return HttpResponseRedirect(reverse('fits:goal'))
    context = {'goal': goal, 'form': form}
    return render(request, 'fits/edit_goal.html', context)


@login_required
def weight(request):
    my_weight = Weight.objects.filter(owner=request.user).order_by('-date_added')
    context = {'my_weight': my_weight}
    return render(request, 'fits/my_weight.html', context)


@login_required
def add_weight(request):
    if request.method != "POST":
        form = WeightForm()
    else:
        form = WeightForm(request.POST)
        if form.is_valid():
            new_weight = form.save(commit=False)
            new_weight.owner = request.user
            new_weight.save()
            return HttpResponseRedirect(reverse('fits:my_weight'))
    context = {'form': form}
    return render(request, 'fits/add_weight.html', context)