
from django.urls import path
from . import views

urlpatterns=[
path("",views.index),
path("<str:month>",views.getMonthlyChallenge,name='mos_challenge')
]
