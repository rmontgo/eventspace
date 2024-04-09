# Generated by Django 5.0.4 on 2024-04-09 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventspace', '0016_alter_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='endTime',
            field=models.TimeField(default=datetime.time(0, 33, 43, 452463)),
        ),
        migrations.AddField(
            model_name='event',
            name='startTime',
            field=models.TimeField(default=datetime.time(0, 33, 43, 452463)),
        ),
    ]
