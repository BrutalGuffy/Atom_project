from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Board(models.Model):
    title = models.CharField(max_length=30, unique=True)
    subject = models.CharField(max_length=240)
    created_by = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    subject = models.TextField(max_length=4000)
    date = models.DateTimeField
    created_by = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    associated_with = models.ManyToManyField(Board)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()


class Message(models.Model):
    message = models.TextField(max_length=4000)
    event = models.ForeignKey(Event, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.created_by


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_organizer = models.BooleanField
    profile_image = models.ImageField(upload_to='userpicks', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()