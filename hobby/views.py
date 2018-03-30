from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from accounts.forms import SignUpForm
from hobby.forms import ProfileForm, MessageForm
from hobby.models import Board
from hobby.models import Event
from hobby.models import Message
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
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})


def event_detail(request, pk, event_pk):
    event = get_object_or_404(Event, boards__pk=pk, pk=event_pk)
    form = MessageForm(request.POST)
    try:
        messages = event.messages.all()
    except:
        Message.DoesNotExist
        messages = None

    return render(request, 'event_detail.html',
                  {'event': event,
                   'messages': messages,
                   'total_likes': event.total_likes,
                  'form': form})


def add_like(request, pk, event_pk):
    user = request.user
    event = get_object_or_404(Event, boards__pk=pk, pk=event_pk)
    like = event.likes.filter(user=user)

    if not like:
        like = event.likes.create(user=user)
    else:
        like.delete()

    print(like)

    return JsonResponse({"new_total_likes": event.total_likes})

