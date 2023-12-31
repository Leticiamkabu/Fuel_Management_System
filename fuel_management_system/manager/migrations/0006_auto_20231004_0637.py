# Generated by Django 3.2.20 on 2023-10-04 06:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0005_auto_20231003_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_prices',
            name='name',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='fuel_prices',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='daily_statistics',
            name='meter1_closing_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='daily_statistics',
            name='meter1_opening_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='daily_statistics',
            name='meter2_closing_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='daily_statistics',
            name='meter2_opening_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
