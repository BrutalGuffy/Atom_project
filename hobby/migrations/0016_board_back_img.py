# Generated by Django 2.0.3 on 2018-04-06 20:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0015_auto_20180403_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='back_img',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
    ]