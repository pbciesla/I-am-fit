from django import forms

# from bootstrap3_datepicker.widgets import DatePickerInput
from .models import Workout, Goal

class WorkoutForm(forms.ModelForm):
  #  date_workout = forms.DateField(widget=DatePickerInput())

    class Meta:
        model = Workout
        fields = ['text', 'date_workout', 'duration']
        labels = {'text': 'Kind of workout', 'date_workout': 'Date of workout (YYYY-MM-DD)', 'duration': 'duration (in minutes)'}


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal']
        labels = {'goal': 'My goal'}