# Generated by Django 2.0.3 on 2018-04-03 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0010_auto_20180330_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='comment',
        ),
    ]
