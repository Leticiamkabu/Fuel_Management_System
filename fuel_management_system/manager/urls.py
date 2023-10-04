from django.urls import path
from .views import *

urlpatterns = [
    path('dipping/',Fuel_dipping_view.as_view(),name = 'dipping'),
    path('fuel_prices/',Fuel_prices_view.as_view(),name = 'fuel_price'),
]