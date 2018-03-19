from django.contrib import admin
from .models import Board
from .models import Event
from .models import Message
from .models import Like
from .models import User_profile

admin.site.register(Board)
admin.site.register(Event)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(User_profile)