from django.db import migrations
from django.contrib.auth.models import User
from hobby.models import Board

def filler(apps, schema_editor):
    for i in User.objects.all():
        i.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0008_auto_20180319_2324'),
    ]

    operations = [
        migrations.RunPython(filler),
    ]