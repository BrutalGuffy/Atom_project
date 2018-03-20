from django.db import migrations
from django.contrib.auth.models import User
from hobby.models import Board

def filler(apps, schema_editor):
    for i in range(10):
        i = User.objects.create(username='user_%s' % i, email='test@mail.ru', password='qwerty1234')
        i.save()

        i = Board.objects.create(title='title_%s' % i, subject='subject', created_by_id=i)
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0006_auto_20180319_2253'),
    ]

    operations = [
        migrations.RunPython(filler),
    ]
