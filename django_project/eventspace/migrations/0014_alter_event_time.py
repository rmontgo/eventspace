# Generated by Django 5.0.4 on 2024-04-09 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventspace', '0013_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(0, 24, 28, 952320)),
        ),
    ]