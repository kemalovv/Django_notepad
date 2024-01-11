from django.shortcuts import render
from .models import Topic


def index(request):
    """Homepage for notepad"""
    return render(request, 'notepad/index.html')


def topics(request):
    """Shows list of topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notepad/topics.html', context)
