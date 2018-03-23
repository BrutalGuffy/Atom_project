from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from hobby.models import Board


class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'home.html'

