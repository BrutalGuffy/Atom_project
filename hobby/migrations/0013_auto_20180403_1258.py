# Generated by Django 2.0.3 on 2018-04-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0012_auto_20180403_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.TextField(max_length=4000),
        ),
    ]
