# Generated by Django 5.1.1 on 2024-09-08 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_videopreference_video_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videopreference',
            name='video_id',
        ),
    ]
