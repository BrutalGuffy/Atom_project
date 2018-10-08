"""Модуль для управления приложением через Django admin."""

from django.contrib import admin
from file_synchronizer.models import FileSynchronizer
from file_synchronizer.utils import search_for_files
from file_synchronizer.utils import get_classes
from file_synchronizer.utils import get_files_list


def delete_unknown_photos(modeladmin, request, queryset):
    """Метод для удаления всех объектов, не привязанных ни к одной
    из существующих в проекте моделей. Выполнен с помощью Admin actions.
    Не требует выделения объектов в панели админа."""
    queryset.filter(model_name='No model').delete()


delete_unknown_photos.short_description = 'Delete unknown files'


def refresh(modeladmin, request, queryset):
    """Метод для получения актуальной информации касательно привязанных
    и не привязанных к моделям файлов. Выполнен с помощью Admin actions.
    Не требует выделения объектов в панели админа."""
    search_for_files(classes=get_classes(), media_files=get_files_list())


@admin.register(FileSynchronizer)
class FileSynchronizerAdmin(admin.ModelAdmin):
    """Класс Django admin."""
    date_hierarchy = 'date'
    search_fields = ['file', 'model_name', 'created_by']
    list_display = ('file', 'model_name', 'date', 'created_by')
    list_filter = ('model_name', 'date',)
    actions = [delete_unknown_photos, refresh]

    def changelist_view(self, request, extra_context=None):
        """Метод позволяет использовать команды 'delete_unknown_photos'
        и 'refresh' через Admin actions без выделения
        без выделения инстансов"""
        if 'action' in request.POST and request.POST.get('action') \
                == 'delete_unknown_photos' \
                or request.POST.get('action') == 'refresh':
            if not request.POST.getlist(admin.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in FileSynchronizer.objects.all():
                    post.update({admin.ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(FileSynchronizerAdmin, self)\
            .changelist_view(request, extra_context)
