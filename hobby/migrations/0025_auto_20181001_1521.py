# Generated by Django 2.0.3 on 2018-10-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0024_remove_board_back_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
