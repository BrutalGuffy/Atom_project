import os

from django.db import models
from django.dispatch import receiver

from atom.settings import MEDIA_URL


class FileSynchronizer(models.Model):
    """Класс синхронизатора файлов."""
    file = models.FileField()
    path = models.FileField(null=True, blank=True)
    model_name = models.CharField(max_length=30)
    date = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.model_name)


@receiver(models.signals.post_delete, sender=FileSynchronizer)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Метод удаляет файлы из базы данных, при удалении их через
    Django admin."""
    if instance.model_name:
        if instance.model_name == 'No model':
            if instance.file:
                if os.path.isfile(instance.file.url[MEDIA_URL.__len__():]):
                    os.remove(instance.file.url[MEDIA_URL.__len__():])
        else:
            if instance.path:
                if os.path.isfile(instance.path.path):
                    os.remove(instance.path.path)
