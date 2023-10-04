# Generated by Django 3.2.20 on 2023-10-03 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuel_transporter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_purchased_details',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]