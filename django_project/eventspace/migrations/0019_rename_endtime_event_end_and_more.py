# Generated by Django 5.0.4 on 2024-04-09 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventspace', '0018_alter_event_endtime_alter_event_starttime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='endTime',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='startTime',
            new_name='start',
        ),
    ]