from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
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
    return render(request, 'home.html', {'boards': boards})


def board_events(request, pk):
    board = Board.objects.get(pk=pk)
    events = board.events.all()
    like = events.count()


    return render(request, 'events.html', {'events': events, 'board': board, 'like': like})


def profile(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})


def event_detail(request, pk, event_pk):
    board = get_object_or_404(Board, pk=pk)
    event = get_object_or_404(Event, boards__pk=pk, pk=event_pk)
    messages = event.messages.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.event = event
            message.created_by = request.user
            message.save()
            return redirect('event_detail', pk=pk, event_pk=event_pk)
    else:
        form = MessageForm()

    return render(request, 'event_detail.html',
                  {'event': event,
                   'total_likes': event.total_likes,
                   'board': board,
                   'form': form,
                   'messages': messages,
                   })


def add_like(request):
    if request.method == "GET" and request.is_ajax():
        event_id = request.GET['event_id']
        user = request.user
        event = get_object_or_404(Event, pk=event_id)
        like = event.likes.filter(user=user)

        if not like:
            like = event.likes.create(user=user)
        else:
            like.delete()

        return JsonResponse({"new_total_likes": event.likes.count()})


def more_comments(request, pk, event_pk):
    page = int(request.GET['page'])
    event = get_object_or_404(Event, boards__pk=pk, pk=event_pk)
    comments = event.messages.all().order_by('created_at')[(page-1) * 10:page * 10].values()
    if request.method == "GET" and request.is_ajax():

        return JsonResponse({'comments': list(comments.values('created_at', 'created_by__username', 'comment', 'id', 'likes'))})





