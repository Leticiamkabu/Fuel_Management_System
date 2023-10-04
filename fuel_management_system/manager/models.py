from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete, post_save
# from fuel_attendant.models import Meter_reading
from authentication.models import *
import datetime
from datetime import timedelta, date
from background_task import background
# Create your models here.

class Fuel_dipping(models.Model):
    id = models.AutoField(primary_key = True)
    user = user = models.ForeignKey(Registeration, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length = 200)
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    date_time = models.DateTimeField(auto_now = True)


@receiver(pre_save, sender = Fuel_dipping)
def add_user(sender, instance, ** kwargs):
    registration = Registeration.objects.get(username = instance.name)
    instance.user = registration
   


@receiver(post_save, sender = Fuel_dipping)
def getting_dipping_data(sender,created, instance, **kwarg):
    # diesel_dipping = 
    if created :
        dips = Daily_statistics(
            diesel_dipping = instance.diesel_dipping,
            super_dipping = instance.super_dipping
        ) 

        dips.save()


class Fuel_prices(models.Model):
    id = models.AutoField(primary_key = True)
    user = user = models.ForeignKey(Registeration, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length = 200, default = 'None') 
    diesel = models.IntegerField(default = 0)
    superfuel = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now = True)



@receiver(pre_save, sender = Fuel_prices)
def add_user(sender, instance, ** kwargs):
    registration = Registeration.objects.get(username = instance.name)
    instance.user = registration



class Daily_statistics(models.Model):
    id = models.AutoField(primary_key = True)
    date = models.DateField(auto_now= True)
    meter1_opening_reading = models.IntegerField(default = 0)
    meter1_opening_time = models.TimeField(default = datetime.time(0, 0))
    meter1_closing_reading = models.IntegerField(default = 0)
    meter1_closing_time = models.TimeField(default = datetime.time(0, 0))
    meter1_amount_sold = models.IntegerField(default = 0)
    meter2_opening_reading = models.IntegerField(default = 0)
    meter2_opening_time = models.TimeField(default = datetime.time(0, 0))
    meter2_closing_reading = models.IntegerField(default = 0)
    meter2_closing_time = models.TimeField(default = datetime.time(0, 0))
    meter2_amount_sold = models.IntegerField(default = 0)
    diesel_litters_sold = models.IntegerField(default = 0)
    diesel_amount_sold = models.IntegerField(default = 0)
    diesel_dipping = models.IntegerField(default = 0)
    diesel_variance = models.IntegerField(default = 0)
    super_litters_sold = models.IntegerField(default = 0)
    super_amount_sold = models.IntegerField(default = 0)
    super_dipping = models.IntegerField(default = 0)
    super_variance = models.IntegerField(default = 0)

# from fuel_attendant.models import Meter_reading
@receiver(pre_save, sender = Daily_statistics)
def getting_meter1_data(sender, instance, **kwarg):
    from fuel_attendant.models import Meter_reading
    current_meter_entry = Meter_reading.objects.latest('date')

    if current_meter_entry.meter_number == 1:
        meter1 = current_meter_entry
        instance.meter1_opening_reading = meter1.opening_litter
        instance.meter1_opening_time = meter1.opening_time
        instance.meter1_closing_reading = meter1.closing_litter
        instance.meter1_closing_time = meter1.closing_time
        instance.meter1_amount_sold = meter1.total_sale

    if current_meter_entry.meter_number == 2:
        meter2 = current_meter_entry
        instance.meter2_opening_reading = meter2.opening_litter
        instance.meter2_opening_time = meter2.opening_time
        instance.meter2_closing_reading = meter2.closing_litter
        instance.meter2_closing_time = meter2.closing_time
        instance.meter2_amount_sold = meter2.total_sale


    if current_meter_entry.fuel_type == 'Diesel':
        instance.diesel_amount_sold = current_meter_entry.total_sale
        instance.diesel_litter_sold = current_meter_entry.closing_litter - current_meter_entry.opening_litter
       
        instance.diesel_variance = current_meter_entry.total_sale + instance.diesel_litter_sold

    if current_meter_entry.fuel_type == 'Super':
        instance.super_amount_sold = current_meter_entry.total_sale
        instance.super_litter_sold = current_meter_entry.closing_litter - current_meter_entry.opening_litter
        
        instance.super_variance = current_meter_entry.total_sale + instance.super_litter_sold


@background(schedule=timedelta(days=7))  # Schedule it to run every 7 days
def accumulate_weekly_data(self):
    from django.core.management import call_command
    call_command('accumulate_weekly_data')  # Replace with your command name



    
class Weekly_statistics(models.Model):
    id = models.AutoField(primary_key = True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    diesel_litter_sold = models.IntegerField()
    super_litter_sold = models.IntegerField()
    diesel_amount_sold = models.IntegerField()
    super_amount_sold = models.IntegerField()
    diesel_variance = models.IntegerField()
    super_variance = models.IntegerField()


class Monthly_statistics(models.Model):
    id = models.AutoField(primary_key = True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    diesel_litter_sold = models.IntegerField()
    super_litter_sold = models.IntegerField()
    diesel_amount_sold = models.IntegerField()
    super_amount_sold = models.IntegerField()
    diesel_variance = models.IntegerField()
    super_variance = models.IntegerField()

class Yearly_statistics(models.Model):
    id = models.AutoField(primary_key = True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    diesel_litter_sold = models.IntegerField()
    super_litter_sold = models.IntegerField()
    diesel_amount_sold = models.IntegerField()
    super_amount_sold = models.IntegerField()
    diesel_variance = models.IntegerField()
    super_variance = models.IntegerField()
