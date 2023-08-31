from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete, post_save

# Create your models here.

FUEL_TYPE = (
    ('Diesel', 'Diesel'),
    ('Super', 'Super'),
)
class Meter_reading(models.Model):
    name = models.CharField(max_length = 200)
    meter_number = models.IntegerField(default = 0)
    fuel_type = models.CharField(max_length = 200, choices = FUEL_TYPE , default = 'None')
    opening_time = models.TimeField()
    opening_litter = models.IntegerField(default= 0)
    closing_time = models.TimeField(null = True,blank = True)
    closing_litter = models.IntegerField( null = True, default= 0)
    date = models.DateField(null = True, auto_now = True)
    total_sale = models.IntegerField(null = True, default= 0)

# get the right calculation
@receiver(post_save, sender = Meter_reading)
def calculating_total_sale(sender, instance, **kwarg):
    if instance.closing_litter != 0:
        instance.total_sale = instance.closing_litter - instance.opening_litter