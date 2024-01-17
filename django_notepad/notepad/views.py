from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Homepage for notepad"""
    return render(request, 'notepad/index.html')


@login_required
def topics(request):
    """Shows list of topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notepad/topics.html', context)


@login_required
def topic(request, topic_id):
    """Shows 1 topic and its notes"""
    topic = Topic.objects.get(id=topic_id)
    # Checks if topic belongs to the right user
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'notepad/topic.html', context)


@login_required
def new_topic(request):
    """"Defines new topic"""
    if request.method != 'POST':
        # No data was sent so we're creating an empty form
        form = TopicForm()
    else:
        # Data was sent so we process it
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('notepad:topics')

    # Empty or not valid form
    context = {'form': form}
    return render(request, 'notepad/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """"Add a new entry into specific topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # No data was sent so we're creating an empty form
        form = EntryForm()
    else:
        # Data was sent so we process it
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('notepad:topic', topic_id=topic_id)

    # Empty or not valid form
    context = {'topic': topic, 'form': form}
    return render(request, 'notepad/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """"Editing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Form fills with existing text
        form = EntryForm(instance=entry)
    else:
        # Sent data, process it
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notepad:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'notepad/edit_entry.html', context)


def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404
