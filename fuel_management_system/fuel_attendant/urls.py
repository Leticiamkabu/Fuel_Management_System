from django.urls import path
from .views import *

urlpatterns = [
    path('meter_reading/',  Meter_reading_View.as_view(), name = 'meter_reading'),
    path('meter_reading/<int:id>',  Meter_reading_View.as_view(), name = 'get_meter_reading_by_id'),
    
]