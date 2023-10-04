# Generated by Django 3.2.20 on 2023-10-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_registeration_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='role',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Fuel Attendant', 'Fuel Attendant'), ('Fuel Transporter', 'Fuel Transporter')], default='None', max_length=200),
        ),
    ]