"""Schemes of URLs for notepad"""
from django.urls import path

from . import views

app_name = 'notepad'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # A page with a list of all topics
    path('topics/', views.topics, name='topics'),
    # A page with info about specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # A page to create new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]
