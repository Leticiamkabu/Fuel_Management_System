from django.urls import path
from .views import *

urlpatterns = [
    path('dipping/',Fuel_dipping_view.as_view(),name = 'dipping'),
]