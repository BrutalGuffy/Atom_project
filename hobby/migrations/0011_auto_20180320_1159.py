# Generated by Django 2.0 on 2018-03-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0010_auto_20180320_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]