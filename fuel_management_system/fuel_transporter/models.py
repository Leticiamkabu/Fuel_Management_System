from django.db import models
from django.contrib.auth.models import AbstractUser, User
from authentication.models import *
# Create your models here.


class Fuel_purchased_details(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(Registeration, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length = 200)
    supplier_name = models.CharField(max_length = 200)
    supplier_contact = models.IntegerField()
    litters_bought = models.CharField(max_length = 50)
    date = models.DateField()
    time = models.TimeField()
    receipt = models.ImageField(upload_to=('img/fuel_transporter/receipt'), )



@receiver(pre_save, sender = Fuel_purchased_details)
def add_user(sender, instance, ** kwargs):
    registration = Registeration.objects.get(username = instance.name)
    instance.user = registration
    