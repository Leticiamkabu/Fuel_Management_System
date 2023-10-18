from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils import timezone

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
        instance.username = instance.first_name + '_' + instance.last_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


ATTENDANCE_CHOICE = (
    ('Login', 'Login'),
    ('Logout', 'Logout'),
)

class Attendance(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(Registeration, on_delete=models.CASCADE)
    clockin= models.DateTimeField(default=timezone.now)
    clockout = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length = 10, choices = ATTENDANCE_CHOICE)



