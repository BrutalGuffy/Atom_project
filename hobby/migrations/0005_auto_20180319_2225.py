from django.db import migrations
from django.contrib.auth.models import User

def filler(apps, schema_editor):
    for i in range(100000):
        i = User.objects.create(username='user_%s' % i, email='test@mail.ru', password='qwerty1234')
        i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0004_user_profile'),
    ]

    operations = [
        migrations.RunPython(filler),
    ]
