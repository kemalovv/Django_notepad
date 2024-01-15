from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


def index(request):
    """Homepage for notepad"""
    return render(request, 'notepad/index.html')


def topics(request):
    """Shows list of topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notepad/topics.html', context)


def topic(request, topic_id):
    """Shows 1 topic and its notes"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'notepad/topic.html', context)


def new_topic(request):
    """"Defines new topic"""
    if request.method != 'POST':
        # No data was sent so we're creating an empty form
        form = TopicForm()
    else:
        # Data was sent so we process it
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notepad:topics')

    # Empty or not valid form
    context = {'form': form}
    return render(request, 'notepad/new_topic.html', context)