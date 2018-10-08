"""Модуль содержит методы, вызываемые в admin.py."""

import os
from collections import defaultdict
from pathlib import Path

import django.apps
from django.db.models.fields.files import FileField
from django.db.models.fields.files import ImageField
from django.db.models.signals import post_delete
from django.db.models.signals import post_init
from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_init
from django.db.models.signals import pre_migrate
from django.db.models.signals import pre_save

from file_synchronizer.models import FileSynchronizer

MEDIA = 'media'


class DisableSignals(object):
    """Класс для управления сигналами."""
    def __init__(self, disabled_signals=None):
        self.stashed_signals = defaultdict(list)
        self.disabled_signals = disabled_signals or [
            pre_init, post_init,
            pre_save, post_save,
            pre_delete, post_delete,
            pre_migrate, post_migrate,
        ]

    def __enter__(self):
        for signal in self.disabled_signals:
            self.disconnect(signal)

    def __exit__(self, exc_type, exc_val, exc_tb):
        for signal in list(self.stashed_signals):
            self.reconnect(signal)

    def disconnect(self, signal):
        """Метод отключающий сигналы."""
        self.stashed_signals[signal] = signal.receivers
        signal.receivers = []

    def reconnect(self, signal):
        """Метод включающий сигналы"""
        signal.receivers = self.stashed_signals.get(signal, [])
        del self.stashed_signals[signal]


def get_classes():
    """Метод возвращает список классов, в которых потенциально могут
    храниться медиафайлы."""
    with DisableSignals():
        """Сигналы отключаются для удаления всех инстансов без
        удаления файлов из базы данных"""
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
