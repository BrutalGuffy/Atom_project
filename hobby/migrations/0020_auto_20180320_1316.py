# Generated by Django 2.0 on 2018-03-20 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0019_auto_20180320_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='associated_with',
            new_name='events',
        ),
    ]
