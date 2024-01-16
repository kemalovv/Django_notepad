from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """"Register a new user"""
    if request.method != "POST":
        # Empty registration form
        form = UserCreationForm()
    else:
        # Processing of the completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Performing an entry and redirect to homepage
            login(request, new_user)
            return redirect('notepad:index')

    # Shows empty or incorrect form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

