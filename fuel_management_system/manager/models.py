from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete, post_save
from fuel_attendant.models import *
# Create your models here.

class Fuel_dipping(models.Model):
    name = models.CharField(max_length = 200)
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    date_time = models.DateTimeField(auto_now = True)


class Daily_statistics(models.Model):
    date = models.DateField(auto_now= True)
    meter1_opening_reading = models.IntegerField(default = 0)
    meter1_opening_time = models.TimeField(default = 0)
    meter1_closing_reading = models.IntegerField(default = 0)
    meter1_closing_time = models.TimeField(default = 0)
    meter1_amount_sold = models.IntegerField(default = 0)
    meter2_opening_reading = models.IntegerField(default = 0)
    meter2_opening_time = models.TimeField(default = 0)
    meter2_closing_reading = models.IntegerField(default = 0)
    meter2_closing_time = models.TimeField(default = 0)
    meter2_amount_sold = models.IntegerField(default = 0)
    diesel_litters_sold = models.IntegerField(default = 0)
    diesel_amount_sold = models.IntegerField(default = 0)
    diesel_dipping = models.IntegerField(default = 0)
    diesel_variance = models.IntegerField(default = 0)
    super_litters_sold = models.IntegerField(default = 0)
    super_amount_sold = models.IntegerField(default = 0)
    super_dipping = models.IntegerField(default = 0)
    super_variance = models.IntegerField(default = 0)


@receiver(post_save, sender = Meter_reading)
def getting_meter1_data(sender, instance, **kwarg):
    if meter_number == 1:
        meter1_opening_reading = instance.opening_litter
        meter1_opening_time = instance.opening_time
        meter1_closing_reading = instance.closing_litter
        meter1_closing_time = instance.closing_time
        meter1_amount_sold = instance.total_sale

    if meter_number == 2:
        meter2_opening_reading = instance.opening_litter
        meter2_opening_time = instance.opening_time
        meter2_closing_reading = instance.closing_litter
        meter2_closing_time = instance.closing_time
        meter2_amount_sold = instance.total_sale


    if fuel_type == Diesel:
        diesel_amount_sold = instance.total_sale
        diesel_litter_sold = instance.closing_litter - opening_litter
       
        diesel_variance = instance.total_sale + diesel_litter_sold

    if fuel_type == Super:
        super_amount_sold = instance.total_sale
        super_litter_sold = instance.closing_litter - opening_litter
        
        super_variance = instance.total_sale + super_litter_sold


@receiver(post_save, sender = Fuel_dipping)
def getting_dipping_data(sender, instance, **kwarg):

    if created and instance.date == Daily_statistics.objects.get(date = instance.date):
        diesel_dipping = instance.diesel_dipping
        super_dipping = instance.super_dipping

    
class Weekly_statistics(models.Model):
    duration = models.DateField()
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    diesel_litter_sold = models.IntegerField()
    super_litter_sold = models.IntegerField()
    diesel_amount_sold = models.IntegerField()
    super_amount_sold = models.IntegerField()
    diesel_variance = models.IntegerField()
    super_variance = models.IntegerField()


class Monthly_statistics(models.Model):
    duration = models.DateField()
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    diesel_litter_sold = models.IntegerField()
    super_litter_sold = models.IntegerField()
    diesel_amount_sold = models.IntegerField()
    super_amount_sold = models.IntegerField()
    diesel_variance = models.IntegerField()
    super_variance = models.IntegerField()

class Yearly_statistics(models.Model):
    duration = models.DateField()
    diesel_dipping = models.IntegerField()
    super_dipping = models.IntegerField()
    diesel_litter_sold = models.IntegerField()
    super_litter_sold = models.IntegerField()
    diesel_amount_sold = models.IntegerField()
    super_amount_sold = models.IntegerField()
    diesel_variance = models.IntegerField()
    super_variance = models.IntegerField()
