import os

from django.db import models
from django.dispatch import receiver


class FileSynchronizer(models.Model):
    file = models.FileField()
    model_name = models.CharField(max_length=30)
    date = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.model_name)


@receiver(models.signals.post_delete, sender=FileSynchronizer)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
