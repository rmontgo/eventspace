# Generated by Django 5.0.4 on 2024-04-08 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventspace', '0010_alter_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
