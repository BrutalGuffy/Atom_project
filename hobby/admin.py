from django.contrib import admin
from .models import Board
from .models import Event
from .models import Message
from .models import Like
from .models import Profile
from .models import Associate

admin.site.register(Board)
admin.site.register(Event)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Associate)
