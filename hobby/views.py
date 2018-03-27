from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from accounts.forms import SignUpForm
from hobby.forms import ProfileForm
from hobby.models import Board
from hobby.models import Event
from hobby.models import Like
from hobby.models import Profile


def home(request):
    boards = Board.objects.all()
    return  render(request, 'home.html', {'boards': boards})


def board_events(request, pk):
    board = Board.objects.get(pk=pk)
    events = board.events.all()
    like = events.count()
    return render(request, 'events.html', {'events': events, 'board': board, 'like': like})



def profile(request):
    if request.method == 'POST':

        bio = request.POST['bio']

        user = User.objects.last()

        profile = Profile.objects.update(
            user=user,
            bio=bio
        )
        return redirect('home')

    else:

        return render(request, 'profile.html')

