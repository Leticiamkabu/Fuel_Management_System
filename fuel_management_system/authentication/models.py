from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver

# Create your models here.
ROLE = (
    ('Manager', 'Manager'),
    ('Fuel Attendant', 'Fuel Attendant'),
    ('Fuel Transporter', 'Fuel Transporter'),
)
class Registeration(AbstractUser):
    phone_number = models.IntegerField(default = 0)
    role = models.CharField(max_length = 200, choices = ROLE, default = 'None')


    
@receiver(pre_save, sender= Registeration)
def generate_username(sender, instance, *args, **kwargs):
    if not instance.username:  # Only generate if the field is empty
        instance.username = instance.first_name +'_' + instance.last_name


