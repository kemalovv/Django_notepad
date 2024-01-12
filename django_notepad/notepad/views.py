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


def topic(request, topic_id):
    """Shows 1 topic and it's notes"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'notepad/topic.html', context)