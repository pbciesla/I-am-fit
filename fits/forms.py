from django import forms

from .models import Workout, Goal, Weight


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['text', 'date_workout', 'duration']
        widgets = {'date_workout': DateTimeInput()}
        labels = {'text': 'Kind of workout', 'date_workout': 'Date of workout', 'duration': 'duration (in minutes)'}


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal']
        labels = {'goal': 'My goal'}


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['value']
        labels = {'value': 'My current weight'}
