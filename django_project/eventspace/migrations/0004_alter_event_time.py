# Generated by Django 5.0.4 on 2024-04-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventspace', '0003_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]