# Generated by Django 4.1.6 on 2023-06-24 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audify', '0002_alter_video_audio_file_alter_video_subtitles_file_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
    ]
