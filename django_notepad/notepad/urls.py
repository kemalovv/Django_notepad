"""Schemes of URLs for notepad"""
from django.urls import path

from . import views

app_name = 'notepad'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # A page with a list of all topics
    path('topics/', views.topics, name='topics'),
]
