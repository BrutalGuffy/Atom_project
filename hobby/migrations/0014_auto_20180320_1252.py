# Generated by Django 2.0 on 2018-03-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0013_auto_20180320_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='associated_with',
            field=models.ManyToManyField(to='hobby.Board'),
        ),
    ]