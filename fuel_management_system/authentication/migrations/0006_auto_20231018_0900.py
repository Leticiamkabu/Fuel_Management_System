# Generated by Django 3.2.20 on 2023-10-18 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20231003_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='attendance',
            name='clockin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='attendance',
            name='clockout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
