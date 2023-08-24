from django.urls import path
from .views import *

urlpatterns = [
    path('meter_reading/',  Meter_reading_View.as_view(), name = 'meter_reading'),
]