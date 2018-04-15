from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^my_workouts/$', views.my_workouts, name='my_workouts'),
    url(r'^workout/(?P<workout_id>\d+)/$', views.workout, name='workout'),
    url(r'^add_workout/$', views.add_workout, name='add_workout'),
    url(r'^edit_workout/(?P<workout_id>\d+)/$', views.edit_workout, name='edit_workout'),
    url(r'^goal', views.goal, name='goal'),
    url(r'^edit_goal/$', views.edit_goal, name='edit_goal'),
]