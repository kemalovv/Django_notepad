from django.shortcuts import render


def index(request):
    """Homepage for notepad"""
    return render(request, 'notepad/index.html')
