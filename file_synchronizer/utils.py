"""Модуль содержит методы, вызываемые в admin.py."""


import os
from pathlib import Path

import django.apps
from django.db.models.fields.files import FileField
from django.db.models.fields.files import ImageField

from file_synchronizer.disable_signals import DisableSignals
from file_synchronizer.models import FileSynchronizer

MEDIA = 'media'


def get_classes():
    """Метод возвращает список классов, в которых потенциально могут
    храниться медиафайлы."""
    with DisableSignals():
        instances = FileSynchronizer.objects.all()
        for instance in instances:
            instance.delete()

    model_list = django.apps.apps.get_models()
    classes = []

    for model in model_list:
        try:
            ff = model._meta.get_fields()
        except AttributeError:
            ff = 'None'

        for field in ff:
            if field.__class__ == FileField or field.__class__ == ImageField:
                if model != FileSynchronizer:
                    classes.append(model)
    return classes


def get_files_list():
    """Метод возвращает список всех файлов в указанной директории
    'MEDIA' и её сабдиректориях вместе с путями,
    относительно 'MEDIA'."""
    media_files = []
    for path, subdirs, files in os.walk(MEDIA):
        for name in files:
            if path == MEDIA:
                media_files.append(os.path.join(name))
            else:
                media_files.append(os.path.join
                                   (path[len(MEDIA) + 1: len(path)], name))

    return media_files


def search_for_files(classes, media_files):
    """Метод принимает список классов, в которых могут потенциально храниться
    медиафайлы и список всех файлов. Для каждого файла создается объект с
    ссылкой на файл и указанием к какой модели он привязан.
    Если файл не привязан ни к одной из существующих моделей,
    он будет помечен соответвующим образом."""
    for c in classes:
        fields = c._meta.get_fields()
        instances = c.objects.all()
        for instance in instances:
            for field in fields:
                if field.__class__ == FileField or field.__class__ \
                        == ImageField:
                    file = getattr(instance, field.name)
                    if Path(file.path).exists():
                        FileSynchronizer.objects.create(
                            file=file,
                            model_name=instance.__class__.__name__,
                            date=instance.date,
                            created_by=instance.created_by,
                        )

                    if file in media_files:
                        media_files.pop(media_files.index(file))

    for media_file in media_files:
        FileSynchronizer.objects.create(
            file=media_file,
            model_name='No model',
        )
