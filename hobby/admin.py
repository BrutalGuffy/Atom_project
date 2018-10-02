from os import listdir
from django.contrib import admin
from hobby.disable_signals import DisableSignals
from .models import Board
from .models import Event
from .models import Message
from .models import Like
from .models import Profile
from .models import Associate
from .models import Task
from pathlib import Path
import django.apps
from os.path import isfile, join
from django.db.models.fields.files import FileField, ImageField

admin.site.register(Board)
admin.site.register(Event)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Associate)


def delete_unknown_photos(modeladmin, request, queryset):
    queryset.filter(model_name='No model').delete()
delete_unknown_photos.short_description = 'delete unknown photos'

def refresh(modeladmin, request, queryset):
    with DisableSignals():
        tasks = Task.objects.all()
        for task in tasks:
            task.delete()

    model_list = django.apps.apps.get_models()
    media_files = [f for f in listdir('media') if isfile(join('media', f))]

    classes = []
    for model in model_list:
        try:
            ff = model._meta.get_fields()
        except AttributeError:
            ff = 'None'

        for field in ff:
            if field.__class__ == FileField or field.__class__ == ImageField:
                if model != Task:
                    classes.append(model)

    for c in classes:
        fields = c._meta.get_fields()
        instances = c.objects.all()
        for instance in instances:
            for field in fields:
                if field.__class__ == FileField or field.__class__ == ImageField:
                    file = getattr(instance, field.name)
                    if Path(file.path).exists():
                        Task.objects.create(
                            file=file,
                            model_name=instance.__class__.__name__,
                            date=instance.date,
                            created_by=instance.created_by,
                        )

                    if file in media_files:
                        media_files.pop(media_files.index(file))

    for media_file in media_files:
        Task.objects.create(
            file=media_file,
            model_name='No model',
        )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    search_fields = ['file', 'model_name', 'created_by']
    list_display = ('file','model_name', 'date', 'created_by')
    list_filter = ('model_name', 'date',)
    actions = [delete_unknown_photos, refresh]

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST.get('action') == 'delete_unknown_photos' or request.POST.get('action') == 'refresh':
            if not request.POST.getlist(admin.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Task.objects.all():
                    post.update({admin.ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(TaskAdmin, self).changelist_view(request, extra_context)