from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete, post_save
from manager.models import Fuel_prices
from authentication.models import *
# Create your models here.

FUEL_TYPE = (
    ('Diesel', 'Diesel'),
    ('Super', 'Super'),
)
class Meter_reading(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(Registeration, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length = 200)
    meter_number = models.IntegerField(default = 0) # change to choice
    fuel_type = models.CharField(max_length = 200, choices = FUEL_TYPE , default = 'None')
    opening_time = models.TimeField()
    opening_litter = models.IntegerField(default= 0)
    closing_time = models.TimeField(null = True,blank = True)
    closing_litter = models.IntegerField( null = True, default= 0)
    date = models.DateField(null = True, auto_now = True)
    total_sale = models.IntegerField(null = True, default= 0)

# get the right calculation
@receiver(pre_save, sender = Meter_reading)
def add_user(sender, instance, ** kwargs):
    registration = Registeration.objects.get(username = instance.name)
    instance.user = registration

@receiver(pre_save, sender = Meter_reading)
def calculating_total_sale(sender, instance, **kwarg):
    if instance.closing_litter != 0:
        fuel_prices = Fuel_prices.objects.latest('timestamp')
        if instance.fuel_type == "Diesel":
            price = fuel_prices.diesel
            instance.total_sale = (instance.closing_litter - instance.opening_litter) * price

        elif instance.fuel_type == "Super":
            price = fuel_prices.superfuel
            instance.total_sale = (instance.closing_litter - instance.opening_litter) * price

    # total_sales = Meter_reading.objects.create(
    #     total_sale = instance.total_sale
    # )
    # total_sales.save()
