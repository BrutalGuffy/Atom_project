# Generated by Django 2.0.3 on 2018-10-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0025_auto_20181001_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]